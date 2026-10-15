# gu/inertia.py
"""Exact inertia of Hermitian matrices over QQ(i).

Hermitian congruence (symmetric Gaussian elimination) with sympy. Sylvester's
law of inertia makes the result independent of pivot order. No floating point.
"""
from __future__ import annotations

import sympy as sp


def _is_zero(x) -> bool:
    return sp.expand(x) == 0


def _check_exact(M: sp.Matrix) -> None:
    for e in M:
        re, im = sp.re(e), sp.im(e)
        if not (re.is_Rational and im.is_Rational):
            raise ValueError(f"inertia() needs entries in QQ(i), got {e!r}")


def inertia(M) -> tuple[int, int, int]:
    """Return (n_pos, n_neg, n_zero) of a Hermitian matrix with entries in QQ(i)."""
    M = sp.Matrix(M).applyfunc(sp.expand)  # unexpanded QQ(i) expressions like (1+I)**2 confuse sp.im
    if M.rows != M.cols:
        raise ValueError("matrix must be square")
    _check_exact(M)
    if not (M - M.H).applyfunc(sp.expand).is_zero_matrix:
        raise ValueError("matrix must be Hermitian")

    pos = neg = 0
    while M.rows:
        n = M.rows
        k = next((i for i in range(n) if not _is_zero(M[i, i])), None)
        if k is None:
            off = next(((i, j) for i in range(n) for j in range(n)
                        if i != j and not _is_zero(M[i, j])), None)
            if off is None:
                return pos, neg, n
            i, j = off
            # Add conj(M[j,i]) * row j to row i (and the conjugate on columns):
            # the new (i,i) entry is 2|M[j,i]|^2 > 0.
            P = sp.eye(n)
            P[i, j] = sp.conjugate(M[j, i])
            M = (P * M * P.H).applyfunc(sp.expand)
            k = i
        d = sp.re(M[k, k])
        if d > 0:
            pos += 1
        else:
            neg += 1
        rest = [r for r in range(n) if r != k]
        v = M.extract(rest, [k])
        M = (M.extract(rest, rest) - v * v.H / d).applyfunc(sp.expand)
    return pos, neg, 0
