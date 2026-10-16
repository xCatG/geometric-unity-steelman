"""B07 Phase 2 gates on a linear span of algebraic maps X: C1, SO, C2 under N0/N1/N2, and the curvature response.

C2 (Phase 1 H3, general form): C2 = 1/3 Tr(alpha ^ X b(T,T)) + 1/3 Tr(T ^ X(b(alpha,T) + b(T,alpha))) - Tr(alpha ^ X(T^T)).
    N1, N2: b symmetric on 1-forms (Phase 1 `variation.c2_value`); N0: b == 0, so C2 = -Tr(alpha ^ X(T^T)).
Curvature response (B02 closed-form basis; 4D): *X(xi(R)) = a E_F(Ric) + b E_F'(Ric) + c S E_F(g) + d S E_F'(g),
    fitted exactly on all Kulkarni-Nomizu generators and verified on every one (a residual is an error, not a fit).
    Einstein (B02's ratio kappa = 1/2): (a, b) != (0, 0), c = -a/2, d = -b/2.
All arithmetic is exact (Gaussian rationals; sympy Rational for kernels).
"""
from __future__ import annotations

from fractions import Fraction

import numbers

import numpy as np
import sympy as sp

from gu.cliffform import GQ, plus, scale, star
from gu.curvature import kulkarni_nomizu, ricci, scalar
from gu.shiab import embed_tensor, eta_of, xi
from experiments.B02.response import spanning_pairs, sym_basis
from experiments.B07 import variation as V

NORMS = ("N0", "N1", "N2")


def exact(x):
    """An exact scalar as a sympy expression; rejects Python, numpy and sympy floats anywhere in it (P4). Fixed-width
    numpy integers are exact: they are converted to Python int before any arithmetic."""
    if isinstance(x, numbers.Integral):
        x = int(x)
    elif isinstance(x, (float, complex, np.generic)):
        raise TypeError(f"inexact scalar: {x!r}")
    x = sp.sympify(x)
    if x.has(sp.Float):
        raise TypeError(f"inexact scalar: {x!r}")
    return sp.expand(x)


def gq(x) -> GQ:
    """Exact Gaussian rational -> GQ; rejects floats (before any simplification) and non-Gaussian-rationals."""
    x = exact(x)
    re, im = sp.re(x), sp.im(x)
    if not (re.is_Rational and im.is_Rational):
        raise TypeError(f"not a Gaussian rational: {x}")
    return GQ(Fraction(int(re.p), int(re.q)), Fraction(int(im.p), int(im.q)))


def combine(maps: list, vec: list):
    """sum_i vec[i] * maps[i] as one map."""
    terms = [(m, c) for m, c in ((m, gq(c)) for m, c in zip(maps, vec)) if c]
    return lambda x: plus(*[scale(m(x), c) for m, c in terms]) if terms else {}


def c2_value(X, alpha: dict, T: dict, norm: str, eta: list[int]) -> GQ:
    if norm == "N0":
        return GQ() - V.pair(alpha, X(V.wedge_prod(T, T, eta)), eta)
    return V.c2_value(X, alpha, T, norm, eta)


def c2_residual(X, n: int, eta: list[int], norm: str) -> dict:
    """{(a, i, j): polarized C2} as in Phase 1 `variation.c2_residual`, for N0, N1 or N2."""
    if norm not in NORMS:
        raise ValueError("norm must be N0, N1 or N2")
    X, basis = V.Linear(X), V.one_forms(n)
    diag = [[c2_value(X, al, t, norm, eta) for t in basis] for al in basis]
    out = {}
    for a, al in enumerate(basis):
        for i in range(len(basis)):
            if diag[a][i]:
                out[(a, i, i)] = diag[a][i]
            for j in range(i + 1, len(basis)):
                v = c2_value(X, al, plus(basis[i], basis[j]), norm, eta) - diag[a][i] - diag[a][j]
                if v:
                    out[(a, i, j)] = v
    return out


def response(X, p: int, q: int) -> list:
    """Exact (a, b, c, d); raises if the response is not in the four-dimensional span on some generator."""
    eta, n = eta_of(p, q), p + q
    g = np.diag(eta).astype(np.int64)
    sym = sym_basis(n)
    rows, rhs = [], []
    for s, t in spanning_pairs(n):
        R = kulkarni_nomizu(sym[s], sym[t])
        Ric, S = ricci(R, eta), Fraction(int(scalar(R, eta)))
        basis = [embed_tensor(Ric, 1, 0, p, q), embed_tensor(Ric, 0, 1, p, q),
                 scale(embed_tensor(g, 1, 0, p, q), S), scale(embed_tensor(g, 0, 1, p, q), S)]
        got = star(X(xi(R, eta)), eta)
        for k in set(got) | {k for b in basis for k in b}:
            rows.append([V._sym(b.get(k, GQ())) for b in basis])
            rhs.append(V._sym(got.get(k, GQ())))
    sol, params = sp.Matrix(rows).gauss_jordan_solve(sp.Matrix(rhs))  # raises ValueError if inconsistent
    if params.shape[0]:
        raise AssertionError("response basis not independent on the generators")
    return [exact(x) for x in sol]


def is_einstein(r: list) -> bool:
    """B02 kappa = 1/2 with a nonzero Ricci term: 2c + a = 0, 2d + b = 0, (a, b) != 0 (exact; no division)."""
    a, b, c, d = (exact(x) for x in r)
    return (a != 0 or b != 0) and 2 * c + a == 0 and 2 * d + b == 0


def gate_survey(maps: list, p: int, q: int, norms=NORMS) -> dict:
    """Kernels of C1, SO and C1 + C2 (per norm) over span(maps), with responses of every kernel basis vector."""
    from experiments.B07.phase2 import symmetric as Sy
    eta, n = eta_of(p, q), p + q
    c1 = {i: V.c1_residual(m, n, eta) for i, m in enumerate(maps)}
    so = {i: Sy.sym_obstruction(m, n, eta) for i, m in enumerate(maps)}
    K1, KS = V.kernel(c1), V.kernel(so)
    R1 = [response(combine(maps, v), p, q) for v in K1]
    out = {"dim": len(maps), "c1_kernel_dim": len(K1), "so_kernel_dim": len(KS),
           "c1_kernel_responses": [[str(x) for x in r] for r in R1],
           "c1_kernel_einstein_dim": _einstein_dim(R1), "joint": {}}
    k1maps = [combine(maps, v) for v in K1]
    for norm in norms:
        c2 = {i: c2_residual(m, n, eta, norm) for i, m in enumerate(k1maps)}
        J = V.kernel(c2) if K1 else []
        RJ = [[sum(x * r[k] for x, r in zip(w, R1)) for k in range(4)] for w in J]
        out["joint"][norm] = {"dim": len(J), "responses": [[str(x) for x in r] for r in RJ],
                              "einstein_dim": _einstein_dim(RJ)}
    return out


def _einstein_dim(R: list) -> int:
    """dim of {kernel vectors whose response satisfies 2c + a = 0, 2d + b = 0} minus dim of those with a = b = 0.

    > 0 iff the kernel contains an Einstein operator (B02 kappa = 1/2, nonzero Ricci term)."""
    if not R:
        return 0
    R = [[exact(x) for x in r] for r in R]
    M = sp.Matrix([[2 * r[2] + r[0] for r in R], [2 * r[3] + r[1] for r in R]])
    lin = M.nullspace()
    if not lin:
        return 0
    L = sp.Matrix.hstack(*lin)
    ab = sp.Matrix([[r[0] for r in R], [r[1] for r in R]]) * L
    return len(lin) - len(ab.nullspace())
