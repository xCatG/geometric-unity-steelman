"""B07 Phase 2 runner: writes experiments/B07/phase2/result.json.

Item 1 (reading V, flat model, varpi direction): over (a) the 20 Shiab building blocks across bracket modes (B07-M),
quotiented by their exact zero-operator relations, and (b) the unreduced space of all Spin(p,q)-equivariant
u(A)-preserving algebraic maps Omega^2 -> Omega^(n-1) (4D), record the kernels of C1 (L = L^dag), SO (L^dag algebraic),
and C1 + C2 under N0, N1, N2, with the B02 curvature response of every kernel vector. 14D: bounded witnesses only.
Item 2: the exact Fourier-mode variation of (9.11) against (9.12)/(9.13), the *^dag sign table, and for (9.14) both
X*X ~ Id (the scalar shortcut) and the kinetic principal symbol against ordinary Yang-Mills.
Draft comparisons are recorded, not asserted.
"""
import itertools
import json
import subprocess
import sys
import time
from pathlib import Path

from flint import fmpq, fmpq_mat

from gu.cliffform import GQ, plus, scale
from experiments.B07 import variation as V
from experiments.B07.phase2 import gates as G, second_order as SO2, symmetric as Sy, universal as U

OUT = Path(__file__).with_name("result.json")
OUT_REL = "experiments/B07/phase2/result.json"
# Every producing source and input: the packages imported (gu, B02's curvature basis, B07), the tests, the dependency
# manifests. Only the generated output itself is exempt.
PRODUCERS = ("gu", "experiments/B02", "experiments/B07", "tests", "pyproject.toml", "uv.lock")
SIGS_4D = [(3, 1), (1, 3)]
SIGS_14D = [(7, 7), (9, 5)]
# The self-adjoint Einstein operator found in the block span (one representative; see derivations.md).
E_OP = ((("first", "C", ("F",)), -2), (("second", "CC", ("F", "B")), -1), (("second", "AA", ("F", "B")), 1))


def dirty_paths(porcelain_z: str) -> list[str]:
    """Paths in `git status --porcelain=v1 -z` output other than the exempt output. A rename/copy record (R or C in
    either status column) is followed by an unprefixed source-path record, which is consumed and checked too."""
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


def rank(mats: list[dict]) -> int:
    keys = sorted({k for m in mats for k in m})
    if not keys:
        return 0
    ix = {k: i for i, k in enumerate(keys)}
    A = fmpq_mat(len(keys), len(mats))
    for j, m in enumerate(mats):
        for k, v in m.items():
            A[ix[k], j] = fmpq(v.numerator, v.denominator)
    return A.rank()


def e_op(p: int, q: int):
    ms = [(Sy.block_map(b, p, q), c) for b, c in E_OP]
    return lambda x: plus(*[scale(m(x), c) for m, c in ms])


def independent_blocks(p: int, q: int) -> tuple[list, int]:
    """A maximal independent subset of the 20 blocks (greedy, in BLOCKS order) and the number of zero relations."""
    ph, chosen, mats = U.phases(p, q), [], []
    for b in Sy.BLOCKS:
        m = U.matrix_of(Sy.block_map(b, p, q), p, q, ph)
        if rank(mats + [m]) > len(mats):
            chosen.append(b)
            mats.append(m)
    return chosen, len(Sy.BLOCKS) - len(chosen)


def item1_4d(p: int, q: int) -> dict:
    ph = U.phases(p, q)
    basis = U.equivariant_basis(p, q)
    umaps = [U.as_map(M, p, q, ph) for M in basis]
    blocks, relations = independent_blocks(p, q)
    bmats = [U.matrix_of(Sy.block_map(b, p, q), p, q, ph) for b in blocks]
    out = {"signature": [p, q],
           "universal_dim": len(basis),
           "universal_block_dims": U.block_dims(p, q),
           "blocks_rank": len(blocks), "block_zero_relations": relations,
           "blocks_in_universal_span": rank(basis + bmats) == len(basis),
           "blocks": G.gate_survey([Sy.block_map(b, p, q) for b in blocks], p, q),
           "universal": G.gate_survey(umaps, p, q)}
    out["blocks"]["names"] = [Sy.block_name(b) for b in blocks]
    out["e_op_response"] = [str(x) for x in G.response(e_op(p, q), p, q)]
    out["e_op_c1_nonzero"] = len(V.c1_residual(e_op(p, q), p + q, V.eta_of(p, q)))
    return out


def e_op_witnesses(p: int, q: int) -> dict:
    """Bounded searches at 14D for the block representative E_OP: C1 (counterexample or none found) and C2/N0-N2."""
    eta, n = V.eta_of(p, q), p + q
    X = V.Linear(e_op(p, q))
    r = range(5)
    blades = [0] + [1 << i for i in r] + [(1 << i) | (1 << j) for i, j in itertools.combinations(r, 2)]
    c1 = None
    checked = 0
    for k, i, j, A, B in itertools.product(range(3), range(5), range(5), blades, blades):
        checked += 1
        v = V.c1_entry(X, k, {(1 << i, A): GQ(1)}, {(1 << j, B): GQ(1)}, eta)
        if v:
            c1 = {"k": k, "t": [i, A], "a": [j, B], "value": [str(v.re), str(v.im)]}
            break
    c2 = {}
    small = [{(1 << i, A): GQ(1)} for i in range(3) for A in blades]
    for norm in G.NORMS:
        c2[norm] = None
        for (ai, al), (ti, t), (si, s) in itertools.product(enumerate(small), enumerate(small), enumerate(small)):
            if si < ti:
                continue
            T = t if si == ti else plus(t, s)
            v = G.c2_value(X, al, T, norm, eta)
            if si != ti:
                v = v - G.c2_value(X, al, t, norm, eta) - G.c2_value(X, al, s, norm, eta)
            if v:
                c2[norm] = {"alpha": ai, "t": ti, "s": si, "value": [str(v.re), str(v.im)]}
                break
    return {"signature": [p, q], "c1_entries_checked": checked, "c1_witness": c1, "c2_witness": c2}


def item2() -> dict:
    signs = [{"signature": [p, n - p], "conv": conv, "star_dag_sign_1form": SO2.star_adjoint_sign(p, n - p, 1, conv),
              "mass_sign": SO2.mass_sign(p, n - p, conv)}
             for n in (4, 14) for p in range(n + 1) for conv in ("pinned", "prime")]
    maps = {name: (lambda name: lambda p, q: V.branch_map(name, p, q))(name) for name in V.BRANCHES}
    maps["E_OP block representative"] = e_op
    fourier = [dict(SO2.compare(f(p, q), p, q, conv), map=name)
               for name, f in maps.items() for p, q in [(3, 1), (1, 3), (2, 2), (4, 0)] for conv in ("pinned", "prime")]
    xx = [dict(SO2.xstar_x(f(p, q), p, q), map=name) for name, f in maps.items() for p, q in SIGS_4D]
    ym = [dict(SO2.ym_symbol(f(p, q), p, q), map=name) for name, f in maps.items() for p, q in SIGS_4D]
    return {"star_signs": signs, "fourier": fourier, "xstar_x": xx, "ym_symbol": ym}


def main() -> None:
    commit = git_commit()
    t0 = time.time()
    item1 = [item1_4d(p, q) for p, q in SIGS_4D]
    print("item 1 4D done", round(time.time() - t0), flush=True)
    so_w = [Sy.so_witness(name, p, q) for name in list(V.BRANCHES)[1:] for p, q in SIGS_4D + SIGS_14D]
    e_w = [e_op_witnesses(p, q) for p, q in SIGS_14D]
    print("14D witnesses done", round(time.time() - t0), flush=True)
    result = {
        "scope": "identity (4D: exact kernels over the quotiented block span and the unreduced Spin-equivariant "
                 "u(A)-preserving algebraic maps; exact Fourier variation over wavevectors determining each homogeneous kappa coefficient (degrees 2, 1, 0)); "
                 "counterexample (14D: bounded witnesses; 'None' means none found in the bounded search, not a proof)",
        "reading": "V (experiments/B07/transcription.md), varpi direction, flat model; Phase 2 derivations in "
                   "experiments/B07/phase2/derivations.md",
        "item1_4d": item1,
        "so_witnesses": so_w,
        "e_op_14d": e_w,
        "item2": item2(),
        "seconds": round(time.time() - t0, 1),
        "source_commit": commit,
    }
    OUT.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT}", flush=True)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
