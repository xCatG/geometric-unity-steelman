"""B07 option C runner: writes experiments/B07/optionc/result.json. Run: uv run python -m experiments.B07.optionc.run

Design (pre-registration): docs/superpowers/specs/2026-10-17-b07-optionc-design.md, rev 3.1. Every control in §3 is a
hard gate (`failed_control`, the run stops) except the two declared exceptions: covariance failure (ray diagnostics only)
and real-closure failure at the auxiliary signatures (2,2)/(4,0) (raw complex-bilinear branch). Outcomes are recorded,
never asserted. Runtime: 2 h per primary signature; exhaustion gives `partial` (not an outcome). The result file is
rewritten atomically after every operator; a file left in status `running` is an interrupted run. Exit codes:
0 complete, 2 failed_control, 3 partial; an unexpected error writes status `error` and re-raises.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
from fractions import Fraction
from pathlib import Path

from experiments.B07 import variation as V
from experiments.B07.escape.run import jsonable
from experiments.B07.optionc import sector as S, spectrum as SP, torsion as T
from experiments.B07.optionc.sector import mat
from experiments.B07.phase2 import gates as G, second_order as SO2, universal as U

OUT = Path(__file__).with_name("result.json")
OUT_REL = "experiments/B07/optionc/result.json"
PRODUCERS = ("gu", "experiments/B02", "experiments/B07", "tests", "pyproject.toml", "uv.lock")
DESIGN = "docs/superpowers/specs/2026-10-17-b07-optionc-design.md rev 3.1"
SCOPE = ("identity: 4D point, (3,1) and (1,3), flat background, eps = 1, metric frozen, delta T = delta A, quadratic "
         "order; operators CCC, CAA, CAC (variation.BRANCHES) and E_OP (phase2 run.e_op); pinned star, fixed-X prime "
         "convention as a control; (2,2)/(4,0) convention controls only")
DEADLINE_S = 2 * 3600          # per primary signature (design §8, decision 2)
# B02 responses (a, b, c, d) in (E_F Ric, E_F' Ric, S E_F g, S E_F' g) at odd q, pinned star (control 6).
B02_RESPONSE = {"CCC": ["-1", "0", "0", "0"], "CAA": ["-1", "0", "1/2", "0"], "CAC": ["-1", "-1", "1/2", "1/2"],
                "E_OP": ["2", "0", "-1", "0"]}
# Pinned rays: timelike, spacelike, null.
RAYS = {(3, 1): {"timelike": [0, 0, 0, 1], "spacelike": [1, 0, 0, 0], "null": [1, 0, 0, 1]},
        (1, 3): {"timelike": [1, 0, 0, 0], "spacelike": [0, 1, 0, 0], "null": [1, 1, 0, 0]}}
# Control 3: direct-Hessian pairs (a, t) in the grade-ordered phased basis, k = e_1, with a toy X(beta) = e^0 ^ beta.
DIRECT_K, DIRECT_PAIRS = [0, 1, 0, 0], [(0, 0), (2, 3), (3, 2), (12, 16), (5, 7)]
RAY_SAMPLES = list(range(129))  # > deg det M on a ray (<= 128): ray diagnostics in the covariance fallback


class FailedControl(Exception):
    pass


class Deadline(Exception):
    pass


def gate(name: str, ok: bool) -> None:
    if not ok:
        raise FailedControl(name)


class Clock:
    """The per-signature deadline (monotonic), checked at every stage boundary, including after the last stage.
    Policy: an indivisible stage (at most a few minutes on the smoke machine) is not interrupted, so a signature can
    overrun by at most one stage before it is marked `partial`."""

    def __init__(self, seconds: float):
        self.end = time.monotonic() + seconds

    def tick(self, stage: str) -> None:
        if time.monotonic() > self.end:
            raise Deadline(stage)


def dirty_paths(porcelain_z: str) -> list[str]:
    entries, dirty = iter(porcelain_z.split("\0")), []
    for e in entries:
        if not e:
            continue
        if set(e[:2]) & set("RC"):
            src = next(entries)
            if src != OUT_REL:
                dirty.append(src)
        if e[3:] != OUT_REL:
            dirty.append(e[3:])
    return dirty


def git_commit() -> str:
    out = subprocess.run(["git", "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", *PRODUCERS],
                         capture_output=True, text=True, check=True).stdout
    dirty = dirty_paths(out)
    if dirty:
        raise SystemExit("uncommitted producing code or inputs:\n" + "\n".join(dirty))
    return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()


def write_result(out: dict, path: Path) -> None:
    """Atomic: a reader never sees a half-written file, and an earlier result never survives a later attempt."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(jsonable(out), indent=1, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def make_sector(X, p: int, q: int, label: str) -> S.Sector:
    """Sector construction; its closure (to_phased) and diagonal-real-Gram assertions are declared controls."""
    try:
        return S.Sector(X, p, q)
    except AssertionError as exc:
        raise FailedControl(f"{label}: real closure / Gram: {exc}") from exc


def signature_controls(p: int, q: int) -> tuple[dict, dict]:
    """Operator-independent controls: star signs, toy direct Hessian (exercises S1), hand xi entry, projectors."""
    eta = V.eta_of(p, q)
    toy = make_sector(lambda x: V.wedge_prod({(1, 0): V.GQ(1)}, x, eta), p, q, "direct-Hessian toy")
    f = S.fourier_parts(toy, toy.X, DIRECT_K)
    d = S.direct_hessian(toy, DIRECT_K, DIRECT_PAIRS)
    want = [f["k0"][a][t] + f["k1"][a][t] + f["k2"][a][t] for a, t in DIRECT_PAIRS]
    gate("direct_hessian", d == want)
    gate("direct_hessian_nonvacuous", any(v for v in d) and any(f["k1"][a][t] for a, t in DIRECT_PAIRS))
    out = {"star_adjoint_sign_1": SO2.star_adjoint_sign(p, q, 1, "pinned"), "mass_sign": SO2.mass_sign(p, q, "pinned"),
           "direct_hessian": [str(v) for v in d]}
    gate("mass_sign", out["mass_sign"] == (-1) ** q)
    out["hand_xi_entry"] = T.hand_xi_entry(p, q)
    gate("hand xi entry", out["hand_xi_entry"])
    P = T.projectors()
    pc = T.projector_controls(P, p, q)
    gate("projectors", pc["idempotent"] and pc["mutually_annihilating"] and pc["sum_identity"] and pc["equivariant"]
         and pc["ranks"] == {"P20": 20, "P1": 1, "P15": 15} and pc["algebraic_part_is_curvature_span"])
    out["projectors"] = pc
    return out, P


def exact_directions(sec: S.Sector, u: list[int]):
    """L: the columns u (x) lambda (lambda over the 16 phased blades) in the grade-ordered phased 1-form basis."""
    return mat([[Fraction(u[f.bit_length() - 1]) if c == cc else Fraction(0) for cc in range(1 << sec.n)]
                for (f, c) in sec.B1])


def kernel_s0(sec: S.Sector, u: list[int], name: str, ray: str) -> dict:
    S0, R1, _ = sec.parts(u)
    rec = SP.kernel_s0_data(S0, R1, sec.G1, exact_directions(sec, u), sec.A_of(u))
    for k, ok in rec["controls"].items():
        gate(f"{name}: nested kernels {ray}: {k}", ok)
    return rec


def s0_fourier(sec: S.Sector, u: list[int]):
    """S0(u) from fourier_terms (the independent path for the Q_U check); real by the Gram identity."""
    return mat([[v.re for v in row] for row in S.fourier_parts(sec, sec.X, u)["k0"]])


def ray_spectrum(sec: S.Sector, u: list[int], name: str) -> dict:
    """Q3 (i)-(ii) and Q4 (i)-(ii) on the timelike ray (kappa = 1)."""
    N = sec.N_of(u)
    cf = SP.charpoly_factors(N)
    S0, R1, S2 = sec.parts(u)
    A = sec.A_of(u)
    AtGA = A.transpose() * sec.G3 * A
    S0f = s0_fourier(sec, u)
    factors = []
    for fac in cf["factors"]:
        cs, e = fac["coeffs"], fac["exponent"]
        c = SP.classify_factor(cs) | {"exponent": e}
        c["Q3"] = SP.factor_root_data(N, S0, R1, S2, c, cs, e)
        gate(f"{name}: ker U in ker M ({c['factor']})", c["Q3"]["control_ker_U_in_ker_M"])
        c["Q4_status"] = SP.q4_status(c, cs)
        if c["Q4_status"] == "computed":
            c["Q4"] = SP.root_data(N, S0, R1, S2, AtGA, 1 / cs[0], e, S0_check=S0f)
            for rec in c["Q4"]:
                gate(f"{name}: ker U in ker M ({rec['w0']})", rec["control_ker_U_in_ker_M"])
                gate(f"{name}: derivative form zero on ker U ({rec['w0']})",
                     rec["control_derivative_form_zero_on_ker_U"])
                gate(f"{name}: Q_U = (1/4) V^dag M'' V ({rec['w0']})", rec["control_QU_quarter_second_derivative"])
                gate(f"{name}: realified and over-field kernels agree ({rec['w0']})",
                     (rec["dim_ker_U"], rec["dim_ker_M"]) == (c["Q3"]["dim_ker_U"], c["Q3"]["dim_ker_M"]))
        factors.append(c)
    return {"charpoly": cf | {"factors": factors}, "kernel_S0": kernel_s0(sec, u, name, "timelike"),
            "rank_S0_kappa0": S0.rank()}


def operator_run(name: str, p: int, q: int, P: dict, clock: Clock) -> dict:
    X = S.operator(name, p, q)
    sec = make_sector(X, p, q, name)
    n, rays = sec.n, RAYS[(p, q)]
    e = lambda *ix: [int(i in ix) for i in range(n)]
    # controls 1, 2, 4, 6 (operator-independent ones in signature_controls; backend 7 before any operator)
    gate(f"{name}: fourier_symmetry", S.fourier_symmetry(sec))
    gate(f"{name}: reconstruction", S.reconstruction(sec, X))
    for k in [e(i) for i in range(n)] + [e(i, j) for i in range(n) for j in range(i + 1, n)] + [S.EXTRA_K]:
        gate(f"{name}: gram_identity {k}", S.gram_identity(sec, X, k))
    gate(f"{name}: S2 = 2(-1)^q G1", sec.parts([0] * n)[2] == sec.G1 * 2 * (-1) ** q)
    gate(f"{name}: prime_identity", S.prime_identity(sec, X, e(0, 1)))
    gate(f"{name}: s1_closed_form", all(S.s1_closed_form(sec, m) for m in range(n)))
    resp = [str(x) for x in G.response(X, p, q)]
    gate(f"{name}: B02 response", resp == B02_RESPONSE[name])
    for r, u in rays.items():
        S0, R1, S2 = sec.parts(u)
        gate(f"{name}: det M = det(2 G3) u(w) u(-w) on the {r} ray",
             SP.det_identity(S0, R1, S2, sec.N_of(u), sec.S, sec.G3))
    clock.tick(f"{name}: controls")
    cov = S.covariance(sec)
    if not cov["covariance_verified"]:        # exception (a): only labelled ray diagnostics continue
        diag = {r: SP.ray_label(SP.det_values(*sec.parts(u), RAY_SAMPLES)) for r, u in rays.items()}
        return {"operator": name, "response": resp, "Q3_Q4": {"covariance": cov, "ray_diagnostics": diag}}
    # control 9 and the covariance consequences
    t_, s_, n_ = (SP.coeffs(sec.N_of(rays[r])) for r in ("timelike", "spacelike", "null"))
    gate(f"{name}: u even (odd coefficients of chi vanish)", all(not c for j, c in enumerate(t_) if j % 2))
    gate(f"{name}: spacelike relation", SP.spacelike_relation(t_, s_))
    gate(f"{name}: null ray nilpotent", n_ == [Fraction(0)] * 64 + [Fraction(1)])
    S0, R1, S2 = sec.parts(rays["null"])
    gate(f"{name}: det M constant = det M(0) on the null ray",
         all(v == S2.det() for v in SP.det_values(S0, R1, S2, RAY_SAMPLES)))
    c1 = len(V.c1_residual(X, n, sec.eta))
    # Q1
    ranks = [sec.parts(e(m))[1].rank() for m in range(n)]
    grades = sorted({(bin(sec.B1[a][1]).count("1"), bin(sec.B1[t][1]).count("1"))
                     for m in range(n) for a, t in _nonzero(sec.parts(e(m))[1])})
    ft = sec.fourier(e(0))
    q1 = {"c1_nonzero": c1, "S1_rank_at_e_m": ranks, "S1_identically_zero": not any(ranks),
          "grade_pairs_coupled": [list(g) for g in grades],
          "repaired_term2_nonzero_at_e0": bool(ft["printed_2"]), "derived_term3_nonzero_at_e0": bool(ft["derived_3"])}
    if c1 == 0:
        gate(f"{name}: control 9 (C1 = 0 => S1 != 0)", any(ranks))
    if name == "E_OP":
        gate("E_OP: c1 = 0 as recorded", c1 == 0)
    clock.tick(f"{name}: Q1")
    # Q2
    q2 = T.q2(sec, P, name == "CCC")
    gate(f"{name}: Q2 Schur controls", all(v for k, v in q2["controls"].items() if k != "dims_E_Ea")
         and q2["controls"]["dims_E_Ea"] == [20, 12, 32])
    clock.tick(f"{name}: Q2")
    # Q3/Q4
    q3 = {"covariance": cov, "timelike": ray_spectrum(sec, rays["timelike"], name)}
    clock.tick(f"{name}: Q3 timelike")
    q3["kernel_S0_spacelike"] = kernel_s0(sec, rays["spacelike"], name, "spacelike")
    q3["kernel_S0_null"] = kernel_s0(sec, rays["null"], name, "null")
    q3["rank_S0_kappa0"] = {r: sec.parts(rays[r])[0].rank() for r in rays}
    return {"operator": name, "response": resp, "Q1": q1, "Q2": q2, "Q3_Q4": q3}


def _nonzero(M):
    return [(i, j) for i in range(M.nrows()) for j in range(M.ncols()) if M[i, j] != 0]


def aux_controls(p: int, q: int, names=S.OPERATORS) -> dict:
    """Control 8 at (2,2)/(4,0): star signs, the backend toys, and per operator real closure (a recorded fact), the
    transpose identity, S2 = 2(-1)^q G1, the prime identity and homogeneous reconstruction, all on raw fourier_terms
    (complex bilinear over Q(i), valid whatever closure says); control 1's Hermiticity only if closure holds."""
    out = {"signature": [p, q], "star_adjoint_sign_1": SO2.star_adjoint_sign(p, q, 1, "pinned"),
           "mass_sign": SO2.mass_sign(p, q, "pinned")}
    gate(f"({p},{q}) mass sign", out["mass_sign"] == (-1) ** q)
    out["backend_controls"] = all(SP.backend_controls().values())
    gate(f"({p},{q}) backend controls", out["backend_controls"])
    out["operators"] = {}
    for name in names:
        X = S.operator(name, p, q)
        memo: dict = {}

        def ft(k, conv, X=X, memo=memo):
            key = (tuple(k), conv)
            if key not in memo:
                memo[key] = SO2.fourier_terms(X, p, q, list(k), conv)
            return memo[key]
        try:
            U.matrix_of(X, p, q)
            closed = True
        except AssertionError:
            closed = False
        rec = {"real_closure": closed}
        m = ft((1, 1, 0, 0), "pinned")
        rec["transpose_identity"] = _sym(m["action_k0"], 1) and _sym(m["action_k1"], -1) and _sym(m["action_k2"], 1)
        rec["S2_identity"] = S.raw_s2_identity(ft, p, q)
        rec["prime_identity"] = S.raw_prime_identity(ft, (1, 1, 0, 0))
        rec["reconstruction"] = S.raw_reconstruction(ft, p + q)
        for k in ("transpose_identity", "S2_identity", "prime_identity", "reconstruction"):
            gate(f"({p},{q}) {name}: {k}", rec[k])
        if closed:
            rec["fourier_symmetry"] = S.fourier_symmetry(S.Sector(X, p, q))
            gate(f"({p},{q}) {name}: fourier_symmetry", rec["fourier_symmetry"])
        out["operators"][name] = rec
    return out


def _sym(m: dict, s: int) -> bool:
    return all(m.get((t, a), V.GQ()) == v * V.GQ(s) for (a, t), v in m.items())


def run(path: Path = OUT, provenance: bool = True, deadline_s: float = DEADLINE_S) -> int:
    commit = git_commit() if provenance else "no-provenance (test)"
    json.dumps(jsonable({"smoke": Fraction(1, 2)}))
    t = time.time()
    out = {"scope": SCOPE, "source_commit": commit, "design": DESIGN, "status": "running", "signatures": []}
    todo = [f"({p},{q}) {nm}" for p, q in S.SIGS for nm in S.OPERATORS] + [f"({p},{q}) auxiliary" for p, q in S.AUX_SIGS]
    out["uncomputed"] = list(todo)
    write_result(out, path)
    try:
        out["backend_controls"] = SP.backend_controls()
        gate("backend controls (control 7)", all(out["backend_controls"].values()))
        for p, q in S.SIGS:
            clock = Clock(deadline_s)
            sig = {"signature": [p, q], "status": "running", "operators": []}
            out["signatures"].append(sig)
            try:
                sig["controls"], P = signature_controls(p, q)
                for nm in S.OPERATORS:
                    clock.tick(f"({p},{q}) {nm}")
                    sig["operators"].append(operator_run(nm, p, q, P, clock))
                    out["uncomputed"].remove(f"({p},{q}) {nm}")
                    write_result(out, path)
                    clock.tick(f"({p},{q}) after {nm}")
                sig["status"] = "complete"
            except Deadline as exc:
                sig["status"], sig["deadline_hit_at"] = "partial", str(exc)
        out["auxiliary"] = []
        for p, q in S.AUX_SIGS:
            out["auxiliary"].append(aux_controls(p, q))
            out["uncomputed"].remove(f"({p},{q}) auxiliary")
            write_result(out, path)
        done = not out["uncomputed"] and all(s["status"] == "complete" for s in out["signatures"])
        out["status"] = "complete" if done else "partial"
    except (FailedControl, SP.ConsistencyFailure) as exc:
        out["status"], out["failed_control"] = "failed_control", f"{type(exc).__name__}: {exc}"
    except BaseException as exc:
        out["status"], out["error"] = "error", repr(exc)
        out["seconds"] = round(time.time() - t, 1)
        write_result(out, path)
        raise
    out["seconds"] = round(time.time() - t, 1)
    if provenance:                            # final provenance inside the error-serialization boundary
        try:
            moved = git_commit() != commit
        except BaseException as exc:
            out["status"], out["error"] = "error", f"final provenance check: {exc}"
            write_result(out, path)
            raise
        if moved:
            out["status"], out["error"] = "error", "final provenance check: HEAD moved during the run"
            write_result(out, path)
            raise SystemExit("HEAD moved during the run")
    write_result(out, path)
    print(f"wrote {path} ({out['status']})")
    return {"complete": 0, "failed_control": 2, "partial": 3}[out["status"]]


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
