"""B07 option C (design docs/superpowers/specs/2026-10-17-b07-optionc-design.md rev 3.1): controls only.

Outcomes (Q1-Q4) are recorded by experiments/B07/optionc/run.py, never asserted here. Exact (P4).
"""
import json
from fractions import Fraction

import pytest
import sympy as sp

from gu.cliffform import GQ
from experiments.B07 import variation as V
from experiments.B07.optionc import run as R, sector as S, spectrum as SP, torsion as T
from experiments.B07.optionc.sector import mat
from experiments.B07.phase2 import gates as G


@pytest.fixture(scope="module")
def caa():
    X = S.operator("CAA", 3, 1)
    return X, S.Sector(X, 3, 1)


def test_gram_identity_hessian_factor_and_fourier_symmetry(caa):
    """Controls 1 and 4: fourier_terms = (S0, i R1, S2) at a basis and an off-set wavevector; S2 = 2(-1)^q G1."""
    X, sec = caa
    assert S.gram_identity(sec, X, [0, 1, 0, 0])
    assert S.gram_identity(sec, X, S.EXTRA_K)
    assert sec.parts([0, 0, 0, 0])[2] == sec.G1 * (-2)
    assert S.fourier_symmetry(sec)
    assert S.s1_closed_form(sec, 2)


def test_prime_identity_and_reconstruction(caa):
    """Controls 2 and 4: fixed-X prime M'(k; kappa) = -M(k; -kappa); homogeneous reconstruction at EXTRA_K."""
    X, sec = caa
    assert S.prime_identity(sec, X, [1, 1, 0, 0])
    assert S.reconstruction(sec, X)


def test_direct_hessian_on_the_toy_exercises_s1():
    """Control 3: the dict-level Hessian of the toy X(beta) = e^0 ^ beta equals fourier_terms, with nonzero S1 entries."""
    eta = V.eta_of(3, 1)
    toy = S.Sector(lambda x: V.wedge_prod({(1, 0): GQ(1)}, x, eta), 3, 1)
    f = S.fourier_parts(toy, toy.X, R.DIRECT_K)
    d = S.direct_hessian(toy, R.DIRECT_K, R.DIRECT_PAIRS)
    assert d == [f["k0"][a][t] + f["k1"][a][t] + f["k2"][a][t] for a, t in R.DIRECT_PAIRS]
    # (0, 0): t = e^0 (x) iI, toy X(e^1 ^ t) = 0, so B = 2 <*t, *t> = 2 (-1)^q <t, t> = 2 (<t, t> = i^2 = -1).
    assert [str(v) for v in d] == ["GQ(2, 0)", "GQ(0, 4)", "GQ(0, -4)", "GQ(0, -4)", "GQ(0, 0)"]


def test_covariance_and_ray_relations(caa):
    """Controls 4, 5 and 9: intertwining, invariant pairing, Hessian covariance, traceless generators;
    chi_s(i y) = chi_t(y); the null ray is nilpotent; det M = det(2 G3) u(w) u(-w) on the timelike ray."""
    X, sec = caa
    assert S.covariance(sec) == {"A_intertwines": True, "star_intertwines": True, "traceless": True,
                                 "pairing_invariant": True, "hessian_covariant": True, "covariance_verified": True}
    rays = R.RAYS[(3, 1)]
    t_, s_, n_ = (SP.coeffs(sec.N_of(rays[r])) for r in ("timelike", "spacelike", "null"))
    assert SP.spacelike_relation(t_, s_)
    assert n_ == [Fraction(0)] * 64 + [Fraction(1)]
    S0, R1, S2 = sec.parts(rays["timelike"])
    assert SP.det_identity(S0, R1, S2, sec.N_of(rays["timelike"]), sec.S, sec.G3)


def test_b02_responses_on_the_algebraic_part():
    """Control 6: gates.response reproduces the pinned B02 responses for all four operators at (3,1)."""
    for name in S.OPERATORS:
        assert [str(x) for x in G.response(S.operator(name, 3, 1), 3, 1)] == R.B02_RESPONSE[name], name


def _dim_intersection(U_: list, W_: list) -> int:
    """dim(span U cap span W) through column-space bases and a nullspace (not the rank-sum formula)."""
    cs = lambda vs: sp.Matrix.hstack(*sp.Matrix([[sp.Rational(x) for x in v] for v in vs if any(v)]).T.columnspace())
    BU, BW = cs(U_), cs(W_)
    return len(sp.Matrix.hstack(BU, -BW).nullspace())


def test_projectors_and_q2_schur_controls():
    """Control 6: projectors; the hand xi entry; Schur bounds and the CCC inner cancellation; and the reported Q2
    measurements re-derived through an independent intersection routine (no outcome value is pinned)."""
    P = T.projectors()
    pc = T.projector_controls(P, 3, 1)
    assert pc == {"idempotent": True, "mutually_annihilating": True, "sum_identity": True,
                  "ranks": {"P20": 20, "P1": 1, "P15": 15}, "equivariant": True,
                  "algebraic_part_is_curvature_span": True}
    assert T.hand_xi_entry(3, 1) and T.hand_xi_entry(1, 3)
    sec = S.Sector(S.operator("CCC", 3, 1), 3, 1)
    q = T.q2(sec, P, True)
    assert q["controls"] == {"dims_E_Ea": [20, 12, 32], "schur_15_in_E_plus_Ea": True,
                             "intersections_sum_to_rank": True, "schur_1_in_span_g": True,
                             "ccc_inner_zero_on_20_and_1": True}
    basis15 = [T.tensor([Fraction(int(P["P15"][r, j].p), int(P["P15"][r, j].q)) for r in range(36)]) for j in range(36)]
    img = [T.response(sec, Rt) for Rt in basis15]
    vs = T.value_spaces(sec)
    assert q["rank_15"] == sp.Matrix([[sp.Rational(x) for x in v] for v in img]).rank()
    assert q["dim_15_in_E"] == _dim_intersection(img, vs["E"])
    assert q["dim_15_in_Ea"] == _dim_intersection(img, vs["Ea"])
    R1 = T.tensor(T.coords(T.alt(T.tensor([Fraction(int(j == T.COORDS.index(((0, 1), (2, 3))))) for j in range(36)]))))
    y = T.response(sec, R1)
    a, b = (Fraction(x) for x in q["one_part"]["coefficients_EF_g_EFprime_g"])
    assert y == [a * g0 + b * g1 for g0, g1 in zip(*vs["g"])]
    assert q["one_part"]["rank"] == sp.Matrix([[sp.Rational(x) for x in y]]).rank()
    inner = [T.vec0(T.ccc_inner(sec, Rt), sec) for Rt in basis15]
    assert q["ccc_inner_rank_15"] == sp.Matrix([[sp.Rational(x) for x in v] for v in inner]).rank()


BACKEND = ["scalar_massless_timelike", "scalar_massless_null_zero_polynomial", "scalar_massive",
           "singular_leading_degree_deficit", "classify_massive", "classify_tachyonic", "classify_non_real",
           "nilpotent_algebraic_multiplicity", "gram_toy_[1, 1]", "gram_toy_[1, 1]_over_field", "gram_toy_[1, -1]",
           "gram_toy_[1, -1]_over_field", "jordan_chain", "jordan_chain_realified", "real_eigenvalue_root",
           "hermitian_d1_vs_gu_inertia", "hermitian_d2_hand", "conjugation_convention", "second_order_form_d2",
           "second_order_form_d1_4"]


def test_spectral_backend_toys():
    """Control 7: every backend toy matches its pinned hand answer (spectrum.backend_controls), none dropped."""
    assert SP.backend_controls() == {k: True for k in BACKEND}


def test_nested_kernel_toys_and_gate():
    """Q3 (iii) / Q4 (iii) on hand toys, and the nesting controls rejecting an inconsistent input."""
    A = mat([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    rec = SP.kernel_s0_data(2 * A.transpose() * A, A * 0, mat([[1, 0, 0], [0, -1, 0], [0, 0, 1]]),
                            mat([[0], [0], [1]]), A, exact_dim=1)
    assert all(rec["controls"].values())
    assert (rec["dim_exact_directions"], rec["dim_ker_A"], rec["dim_ker_S0"], rec["quotient_kerA_over_exact"],
            rec["quotient_kerS0_over_kerA"], rec["G1_restricted_inertia"], rec["S1_restricted_inertia"]) == \
        (1, 2, 2, 1, 0, [1, 1, 0], [0, 0, 2])
    A2 = mat([[1, 0, 0], [1, 0, 0]])            # G3 = diag(1, -1): A^T G3 A = 0, a one-dimensional radical
    S0 = 2 * A2.transpose() * mat([[1, 0], [0, -1]]) * A2
    rec = SP.kernel_s0_data(S0, S0 * 0, mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), mat([[0], [0], [1]]), A2, exact_dim=1)
    assert (rec["dim_ker_A"], rec["dim_ker_S0"], rec["quotient_kerS0_over_kerA"], rec["G1_restricted_inertia"]) == \
        (2, 3, 1, [3, 0, 0])
    # a nonzero restriction of i R1 to ker S0: S = [[1, 0, 0], [0, 1, 0]], same A2 and G3; inertia (1, 1, 1)
    Sx, G3 = mat([[1, 0, 0], [0, 1, 0]]), mat([[1, 0], [0, -1]])
    R1 = 2 * (Sx.transpose() * G3 * A2 - A2.transpose() * G3 * Sx)
    rec = SP.kernel_s0_data(S0, R1, mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), mat([[0], [0], [1]]), A2, exact_dim=1)
    assert rec["S1_restricted_inertia"] == [1, 1, 1]
    bad = SP.kernel_s0_data(mat([[0]]), mat([[0]]), mat([[1]]), mat([[1]]), mat([[1]]), exact_dim=1)
    assert bad == {"controls": {"exact_rank": True, "exact_in_ker_A": False, "ker_A_in_ker_S0": True,
                                "nullity_S0_at_least_exact": True}}


def test_runner_gates_nesting_and_signature_closure(monkeypatch, caa):
    """A false nesting flag and a signature-level closure/Gram assertion both become FailedControl."""
    _, sec = caa
    monkeypatch.setattr(R.SP, "kernel_s0_data", lambda *a: {"controls": {"exact_in_ker_A": False}})
    with pytest.raises(R.FailedControl, match="nested kernels"):
        R.kernel_s0(sec, [0, 0, 0, 1], "CAA", "timelike")

    def no_closure(*a):
        raise AssertionError("not u(A)-valued")
    monkeypatch.setattr(R.S, "Sector", no_closure)
    with pytest.raises(R.FailedControl, match="real closure"):
        R.signature_controls(3, 1)


def test_auxiliary_signature_branch():
    """Control 8 at (2,2): real closure is a recorded fact; raw transpose, S2, prime and reconstruction hold."""
    out = R.aux_controls(2, 2, names=("E_OP",))
    assert out["mass_sign"] == 1 and out["backend_controls"]
    rec = out["operators"]["E_OP"]
    assert all(rec[k] for k in ("transpose_identity", "S2_identity", "prime_identity", "reconstruction"))


def _stub(monkeypatch, op):
    monkeypatch.setattr(R.SP, "backend_controls", lambda: {"stub": True})
    monkeypatch.setattr(R, "signature_controls", lambda p, q: ({}, {}))
    monkeypatch.setattr(R, "operator_run", op)
    monkeypatch.setattr(R, "aux_controls", lambda p, q: {"signature": [p, q]})


def test_runner_failure_routing_and_checkpoints(monkeypatch, tmp_path):
    """Stop policy: a failed control or consistency failure is written (completed records kept) with exit code 2;
    an unexpected error is written as `error` and re-raised; deadline exhaustion gives `partial` (exit 3)."""
    path = tmp_path / "result.json"
    for exc in (R.FailedControl("x"), SP.ConsistencyFailure("y")):
        calls = []

        def op(nm, p, q, P, clock, exc=exc, calls=calls):
            calls.append(nm)
            if len(calls) == 2:
                raise exc
            return {"operator": nm}
        _stub(monkeypatch, op)
        assert R.run(path, provenance=False) == 2
        out = json.loads(path.read_text(encoding="utf-8"))
        assert out["status"] == "failed_control" and out["signatures"][0]["operators"] == [{"operator": "CCC"}]

    def boom(*a):
        raise RuntimeError("unexpected")
    _stub(monkeypatch, boom)
    with pytest.raises(RuntimeError):
        R.run(path, provenance=False)
    assert json.loads(path.read_text(encoding="utf-8"))["status"] == "error"
    _stub(monkeypatch, lambda nm, p, q, P, clock: {"operator": nm})
    assert R.run(path, provenance=False, deadline_s=-1) == 3
    out = json.loads(path.read_text(encoding="utf-8"))
    assert out["status"] == "partial" and [s["status"] for s in out["signatures"]] == ["partial", "partial"]
    assert len(out["uncomputed"]) == 8 and len(out["auxiliary"]) == 2
    assert R.run(path, provenance=False) == 0 and json.loads(path.read_text(encoding="utf-8"))["status"] == "complete"


def test_runner_deadline_after_last_stage_and_late_provenance(monkeypatch, tmp_path):
    """A last stage that crosses the deadline gives `partial` (exit 3), not `complete`; a late provenance rejection
    is written as `error` with its reason."""
    path, now = tmp_path / "result.json", [0.0]
    monkeypatch.setattr(R.time, "monotonic", lambda: now[0])

    def slow_last(nm, p, q, P, clock):
        if nm == S.OPERATORS[-1]:
            now[0] += 100
        return {"operator": nm}
    _stub(monkeypatch, slow_last)
    assert R.run(path, provenance=False, deadline_s=50) == 3
    out = json.loads(path.read_text(encoding="utf-8"))
    assert out["status"] == "partial" and all(s["status"] == "partial" for s in out["signatures"])
    _stub(monkeypatch, lambda nm, p, q, P, clock: {"operator": nm})
    calls = []

    def git(calls=calls):
        calls.append(1)
        if len(calls) > 1:
            raise SystemExit("uncommitted producing code or inputs:\nexperiments/B07/optionc/README.md")
        return "abc"
    monkeypatch.setattr(R, "git_commit", git)
    with pytest.raises(SystemExit):
        R.run(path)
    out = json.loads(path.read_text(encoding="utf-8"))
    assert out["status"] == "error" and out["error"].startswith("final provenance check")


def test_covariance_fallback_stops_q1_q2(monkeypatch):
    """Exception (a): with covariance failed, only labelled ray diagnostics follow (no Q1/Q2 records)."""
    for f in ("fourier_symmetry", "reconstruction", "gram_identity", "prime_identity", "s1_closed_form"):
        monkeypatch.setattr(R.S, f, lambda *a: True)
    monkeypatch.setattr(R.SP, "det_identity", lambda *a: True)
    monkeypatch.setattr(R.G, "response", lambda X, p, q: [Fraction(-1), 0, Fraction(1, 2), 0])
    monkeypatch.setattr(R.S, "covariance", lambda sec: {"covariance_verified": False})
    out = R.operator_run("CAA", 3, 1, T.projectors(), R.Clock(3600))
    assert set(out) == {"operator", "response", "Q3_Q4"} and set(out["Q3_Q4"]) == {"covariance", "ray_diagnostics"}
    assert set(out["Q3_Q4"]["ray_diagnostics"].values()) <= {"zero_on_sampled_ray", "constant_on_sampled_ray",
                                                              "nonconstant_on_sampled_ray"}


def test_provenance_parser():
    """The dirty-tree gate exempts exactly result.json (untracked or modified) and sees both sides of a rename."""
    res, readme = R.OUT_REL, "experiments/B07/optionc/README.md"
    assert R.dirty_paths(f"?? {res}\0 M {res}\0") == []
    assert R.dirty_paths(f"?? {readme}\0") == [readme]
    assert R.dirty_paths(f"R  {readme}\0{res}\0") == [readme]
    assert R.dirty_paths(f"R  {res}\0{readme}\0") == [readme]
