"""B07 Phase 2, item 1: the operator that the variation of (9.4) actually produces, and whether it is a Shiab.

Flat model (B = d, eps = 1, constant coefficients; Phase 1 H5 removes the dressing). X: Omega^2 -> Omega^(n-1) is an
algebraic ad-valued map (Clifford coefficients), L = X o d. pair(x, y) = Tr(x ^ y)/2^(n/2) as in Phase 1.

  Wedge transpose  X^t: Omega^1 -> Omega^(n-2),  pair(t, X(beta)) = pair(X^t(t), beta) for every 2-form beta.
  Formal transpose L^dag = d o X^t  (int Tr(T ^ L alpha) = int Tr(alpha ^ L^dag T), compact support; H9).
  Symbol identity  pair(a, e^k ^ X^t(t)) = -pair(t, X(e^k ^ a)), so <a, sigma(L^dag - L)(e^k) t> = -C1(k; t, a).
  The variation of 1/2 int Tr(T ^ L T) is int Tr(alpha ^ L_sym T), L_sym = 1/2 (L + L^dag).
  Factorization (H10): L^dag = X# o d with X# algebraic iff, for all k <= j, blades c and basis 1-forms a,
      SO(k, j; c, a) = pair(e^j c, X(e^k ^ a)) + pair(e^k c, X(e^j ^ a)) = 0;
  then X#(e^k ^ e^j c) = e^k ^ X^t(e^j c), and L_sym = X_sym o d with X_sym = 1/2 (X + X#).
All arithmetic is exact (Gaussian rationals).
"""
from __future__ import annotations

import itertools

from gu.cliffform import GQ, plus, scale
from experiments.B07 import variation as V

# The 20 distinct building blocks of the Shiab family across all bracket modes (B07-M):
# first[m0](Phi1) for m0 in {C, A}, Phi1 in {F, F'}; second[m1 m2](Phi1, Phi2) for m1 m2 in {C, A}^2, Phi2 in {B, B'}.
BLOCKS = tuple([("first", m0, (p1,)) for m0 in "CA" for p1 in ("F", "F'")]
               + [("second", m1 + m2, (p1, p2)) for m1 in "CA" for m2 in "CA" for p1 in ("F", "F'")
                  for p2 in ("B", "B'")])


def block_map(block: tuple, p: int, q: int):
    """The linear map of one building block (the second term without its -1/2)."""
    kind, m, cols = block
    mode = m + "CC" if kind == "first" else "C" + m
    return V.shiab_column(cols, mode, p, q)


def block_name(block: tuple) -> str:
    return f"{block[0]}[{block[1]}]({','.join(block[2])})"


def two_forms(n: int) -> list[dict]:
    return [{((1 << i) | (1 << j), A): GQ(1)} for i, j in itertools.combinations(range(n), 2) for A in range(1 << n)]


def wedge_transpose(X, n: int, eta: list[int]):
    """X^t as a function on 1-forms, built from the dual basis of 2-forms under pair."""
    X, full = V.Linear(X), (1 << n) - 1
    duals = []
    for beta in two_forms(n):
        (G, B), = beta
        d = {(full ^ G, B): GQ(1)}
        v = V.pair(d, beta, eta)
        if v.im != 0 or v.re not in (1, -1):
            raise AssertionError(f"pair is not a signed permutation on basis {(G, B)}: {v}")
        duals.append((beta, scale(d, v.re)))

    def Xt(t: dict) -> dict:
        return plus(*[scale(d, V.pair(t, X(beta), eta)) for beta, d in duals])
    return Xt


def sym_obstruction(X, n: int, eta: list[int]) -> dict:
    """{(k, j, c, a): SO} over k <= j, blades c and basis 1-forms a (index into V.one_forms(n)); nonzero entries only."""
    X, basis = V.Linear(X), V.one_forms(n)
    S = [[X(V.wedge_prod({(1 << k, 0): GQ(1)}, a, eta)) for a in basis] for k in range(n)]
    out = {}
    for k in range(n):
        for j in range(k, n):
            for c in range(1 << n):
                ej, ek = {(1 << j, c): GQ(1)}, {(1 << k, c): GQ(1)}
                for ai in range(len(basis)):
                    v = V.pair(ej, S[k][ai], eta) + V.pair(ek, S[j][ai], eta)
                    if v:
                        out[(k, j, c, ai)] = v
    return out


def sharp(X, n: int, eta: list[int]):
    """X# on 2-forms, defined by X#(e^k ^ e^j c) = e^k ^ X^t(e^j c) (k < j). Meaningful only where SO vanishes."""
    Xt = wedge_transpose(X, n, eta)

    def Xs(x: dict) -> dict:
        out: dict = {}
        for (f, c), v in x.items():
            k, j = [i for i in range(n) if f >> i & 1]
            img = V.wedge_prod({(1 << k, 0): GQ(1)}, Xt({(1 << j, c): GQ(1)}), eta)
            out = plus(out, scale(img, v))
        return out
    return Xs


def survey(p: int, q: int) -> dict:
    """C1 and SO kernels over the 20 building blocks, and over each fixed mode's six-monomial family."""
    eta, n = V.eta_of(p, q), p + q
    maps = {b: block_map(b, p, q) for b in BLOCKS}
    c1 = {b: V.c1_residual(m, n, eta) for b, m in maps.items()}
    so = {b: sym_obstruction(m, n, eta) for b, m in maps.items()}
    out = {"signature": [p, q], "blocks": [block_name(b) for b in BLOCKS],
           "c1_nonzero": {block_name(b): len(v) for b, v in c1.items()},
           "so_nonzero": {block_name(b): len(v) for b, v in so.items()},
           "c1_kernel_20": [[str(x) for x in v] for v in V.kernel(c1)],
           "so_kernel_20": [[str(x) for x in v] for v in V.kernel(so)],
           "so_kernel_by_mode": {}}
    for mode in V.MODES:
        cols = {}
        for col in V.COLUMNS:
            b = ("first", mode[0], col) if len(col) == 1 else ("second", mode[1:], col)
            cols[col] = so[b]
        out["so_kernel_by_mode"][mode] = [[str(x) for x in v] for v in V.kernel(cols)]
    return out


def so_entry(X, k: int, j: int, c: int, a: dict, eta: list[int]) -> GQ:
    ej, ek = {(1 << j, c): GQ(1)}, {(1 << k, c): GQ(1)}
    return (V.pair(ej, X(V.wedge_prod({(1 << k, 0): GQ(1)}, a, eta)), eta)
            + V.pair(ek, X(V.wedge_prod({(1 << j, 0): GQ(1)}, a, eta)), eta))


def so_witness(name: str, p: int, q: int, max_form: int = 4) -> dict | None:
    """First (k, j, c, a) with nonzero SO for a named Phase 1 branch, over small indices (counterexample scope)."""
    eta, n = V.eta_of(p, q), p + q
    X = V.Linear(V.branch_map(name, p, q))
    r = range(min(n, max_form + 1))
    blades = [0] + [1 << i for i in r] + [(1 << i) | (1 << j) for i, j in itertools.combinations(r, 2)]
    for k in range(min(n, max_form)):
        for j in range(k, min(n, max_form)):
            for i in range(min(n, max_form)):
                for c in blades:
                    for B in blades:
                        a = {(1 << i, B): GQ(1)}
                        v = so_entry(X, k, j, c, a, eta)
                        if v:
                            return {"branch": name, "signature": [p, q], "k": k, "j": j, "c": c, "a": [i, B],
                                    "value": [str(v.re), str(v.im)]}
    return None
