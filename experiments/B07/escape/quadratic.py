"""E1: the curvature sector of the second-order Lagrangian (9.11) at a 4D point (flat model, T = 0).

I2 = <U, U> with U = X(F) + kappa *T (`second_order`). At T = 0 and F = xi(R) for algebraic curvature R this is the
quadratic form Q_X(R) = <X(xi R), X(xi R)>, with the metric trace pairing `mpair` (both Hodge conventions).
Q_X is fitted, as a bilinear form on a basis of the 20-dimensional space of algebraic curvature tensors, to the four
Spin(p,q)-invariant bilinear forms W.W, W.*W, Ric0.Ric0 and S S. Identity scope: all basis pairs (i <= j), exact.
An inconsistent fit is recorded as such (not raised): a non-equivariant X, e.g. a dressed one, need not fit.
"""
from __future__ import annotations

import functools
import itertools
from fractions import Fraction

import numpy as np
import sympy as sp
from flint import fmpq, fmpq_mat

from gu.cliffform import GQ
from gu.curvature import decompose, kulkarni_nomizu, ricci, scalar
from gu.shiab import xi
from experiments.B02.response import spanning_pairs, sym_basis
from experiments.B07.phase2 import second_order as SO2

INVARIANTS = ("W.W", "W.*W", "Ric0.Ric0", "S.S")


def _q(x) -> Fraction:
    """Exact coercion (P4): integers (Python or numpy) and Fractions only; everything else raises TypeError."""
    if isinstance(x, (bool, np.bool_)) or not isinstance(x, (int, np.integer, Fraction)):
        raise TypeError(f"inexact or non-numeric entry {x!r}")
    return Fraction(int(x)) if isinstance(x, (int, np.integer)) else x


def independent(tensors: list[np.ndarray]) -> list[int]:
    """Indices of a maximal independent subset (greedy, in order) of integer tensors, by exact rank."""
    chosen: list[int] = []
    flat = [t.reshape(-1) for t in tensors]
    for i in range(len(flat)):
        rows = [flat[j] for j in chosen + [i]]
        M = fmpq_mat(len(rows), len(rows[0]), [fmpq(f.numerator, f.denominator) for r in rows for f in map(_q, r)])
        if M.rank() == len(rows):
            chosen.append(i)
    return chosen


def curvature_basis(n: int) -> list[np.ndarray]:
    """A basis of algebraic curvature tensors: an independent subset of the B02 spanning set KN(h_s, h_t)."""
    sym = sym_basis(n)
    span = [kulkarni_nomizu(sym[s], sym[t]) for s, t in spanning_pairs(n)]
    return [span[i] for i in independent(span)]


def _levi(idx: tuple) -> int:
    if len(set(idx)) < len(idx):
        return 0
    s = 1
    for i, j in itertools.combinations(range(len(idx)), 2):
        if idx[i] > idx[j]:
            s = -s
    return s


def parts(R: np.ndarray, eta: list[int]) -> tuple:
    """(W, Ric0, S) as exact Fraction arrays (W = Weyl part, Ric0 = trace-free Ricci)."""
    n = len(eta)
    sp_ = decompose(R, eta)
    den = _q(sp_.denominator)
    W = np.vectorize(lambda v: _q(v) / den, otypes=[object])(sp_.weyl)
    S = Fraction(int(scalar(R, eta)))
    Ric = np.vectorize(_q, otypes=[object])(ricci(R, eta))
    Ric0 = Ric - np.diag([S * e for e in eta]).astype(object) / n
    return W, Ric0, S


def invariant_bilinears(R1: np.ndarray, R2: np.ndarray, eta: list[int]) -> list[Fraction]:
    """[W1.W2, W1.*W2, Ric0_1.Ric0_2, S1 S2], all indices contracted with eta (4D only for W.*W).

    *W is the last-pair Hodge dual (1/2) eps_cd^fg W_abfg with eps_0123 = +1."""
    n = len(eta)
    if n != 4:
        raise ValueError("4D only")
    (W1, A1, S1), (W2, A2, S2) = parts(R1, eta), parts(R2, eta)
    e = eta
    ww = sum(W1[a, b, c, d] * W2[a, b, c, d] * e[a] * e[b] * e[c] * e[d]
             for a, b, c, d in itertools.product(range(n), repeat=4))
    # W1.*W2 with (*W)_abcd = (1/2) eps_cd^fg W_abfg (last-pair Hodge dual); the sum runs over both f, g orders.
    wsw = Fraction(1, 2) * sum(W1[a, b, c, d] * _levi((c, d, f, g)) * e[c] * e[d] * W2[a, b, f, g] * e[a] * e[b] * e[f] * e[g]
              for a, b, c, d, f, g in itertools.product(range(n), repeat=6) if _levi((c, d, f, g)))
    rr = sum(A1[a, b] * A2[a, b] * e[a] * e[b] for a, b in itertools.product(range(n), repeat=2))
    return [Fraction(ww), Fraction(wsw), Fraction(rr), S1 * S2]


@functools.lru_cache(maxsize=None)
def _setup(p: int, q: int):
    """(basis, invariant rows over basis pairs i <= j), cached per signature."""
    eta = [1] * p + [-1] * q
    basis = curvature_basis(p + q)
    pairs = list(itertools.combinations_with_replacement(range(len(basis)), 2))
    rows = [[sp.Rational(x.numerator, x.denominator) for x in invariant_bilinears(basis[i], basis[j], eta)]
            for i, j in pairs]
    return basis, pairs, sp.Matrix(rows)


def bilinear_fit(f, g, p: int, q: int, conv: str = "pinned") -> dict:
    """Fit B(R, R') = <f(R), g(R')> on all basis pairs (i <= j) to the invariant bilinears.

    f, g: algebraic curvature -> form. Returns {"re": coeffs | None, "im": coeffs | None} (None = not in the span)."""
    eta = [1] * p + [-1] * q
    basis, pairs, A = _setup(p, q)
    fs, gs = [f(R) for R in basis], [g(R) for R in basis]
    re, im = [], []
    for i, j in pairs:
        v = SO2.mpair(fs[i], gs[j], eta, conv) if fs[i] and gs[j] else GQ()
        re.append(sp.Rational(v.re.numerator, v.re.denominator))
        im.append(sp.Rational(v.im.numerator, v.im.denominator))
    out = {}
    for part, rhs in (("re", re), ("im", im)):
        try:
            sol, params = A.gauss_jordan_solve(sp.Matrix(rhs))
        except ValueError:
            out[part] = None
            continue
        if params.shape[0]:
            raise AssertionError("invariant bilinears are not independent on the basis")
        out[part] = [str(x) for x in sol]
    return out


def quadratic_form(X, p: int, q: int, conv: str = "pinned") -> dict:
    """Q_X fitted to INVARIANTS (identity scope on the 20-dim basis)."""
    eta = [1] * p + [-1] * q
    f = lambda R: X(xi(R, eta))
    return bilinear_fit(f, f, p, q, conv)


def response_basis(p: int, q: int) -> list:
    """The four maps R -> *^-1 b_i(R) whose span contains X(xi R) for X with B02 response (a, b, c, d):
    *X(xi R) = a E_F(Ric) + b E_F'(Ric) + c S E_F(g) + d S E_F'(g) (`gates.response`)."""
    from gu.shiab import embed_tensor
    from gu.cliffform import scale
    eta = [1] * p + [-1] * q
    g = np.diag(eta).astype(np.int64)
    inv = lambda x: SO2.star_inv(x, eta, "pinned")
    return [lambda R: inv(embed_tensor(ricci(R, eta), 1, 0, p, q)),
            lambda R: inv(embed_tensor(ricci(R, eta), 0, 1, p, q)),
            lambda R: inv(scale(embed_tensor(g, 1, 0, p, q), GQ(int(scalar(R, eta))))),
            lambda R: inv(scale(embed_tensor(g, 0, 1, p, q), GQ(int(scalar(R, eta)))))]


def response_gram(p: int, q: int, conv: str = "pinned") -> list[list[dict]]:
    """G[i][j] = bilinear_fit(b_i, b_j). For X with response r, Q_X = sum_ij r_i r_j G[i][j] (bilinearity)."""
    bs = response_basis(p, q)
    return [[bilinear_fit(bi, bj, p, q, conv) for bj in bs] for bi in bs]
