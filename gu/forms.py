# gu/forms.py
"""Exterior algebra on R^{p,q} with exact integer coefficients.

A k-form is a dict {I: coeff}, I a strictly increasing index tuple.
Hodge star convention (pinned, spec rev 4.1): a ^ *b = <a, b>_eta vol,
with <e_I, e_I> = eta_I = prod_{i in I} eta_i. Then ** = (-1)^{k(n-k)+q}.
The Lambda^{n-1} = Lambda^1 identification is hodge() restricted to (n-1)-forms.
"""
from __future__ import annotations

from itertools import combinations
from math import prod
from numbers import Integral


def _integer(x):
    if not isinstance(x, Integral):
        raise ValueError('forms require exact integer coefficients and indices')
    return int(x)


def _dimension(n):
    n = _integer(n)
    if n < 0:
        raise ValueError('dimension/degree must be nonnegative')
    return n


def _indices(I, n=None):
    if not isinstance(I, tuple):
        raise ValueError('form indices must be tuples')
    J = tuple(_integer(i) for i in I)
    if any(i < 0 or (n is not None and i >= n) for i in J) or tuple(sorted(set(J))) != J:
        raise ValueError('indices must be strictly increasing and in range')
    return J


def _form(a, n=None):
    return {_indices(I, n): _integer(x) for I, x in a.items()}


def _metric(eta):
    e = [_integer(x) for x in eta]
    if any(x not in (-1, 1) for x in e):
        raise ValueError('metric entries must be +1 or -1')
    return e


def basis(n: int, k: int) -> list[tuple[int, ...]]:
    return list(combinations(range(_dimension(n)), _dimension(k)))


def _sort_sign(idx: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    if len(set(idx)) < len(idx):
        return 0, ()
    inversions = sum(1 for i in range(len(idx)) for j in range(i + 1, len(idx)) if idx[i] > idx[j])
    return (-1) ** inversions, tuple(sorted(idx))


def _clean(f: dict) -> dict:
    return {K: v for K, v in f.items() if v != 0}


def wedge(a: dict, b: dict) -> dict:
    a, b = _form(a), _form(b)
    out: dict = {}
    for I, x in a.items():
        for J, y in b.items():
            s, K = _sort_sign(I + J)
            if s:
                out[K] = out.get(K, 0) + s * x * y
    return _clean(out)


def eta_I(eta: list[int], I: tuple[int, ...]) -> int:
    eta = _metric(eta)
    I = _indices(I, len(eta))
    return prod(eta[i] for i in I)


def vol(n: int) -> dict:
    return {tuple(range(_dimension(n))): 1}


def inner(a: dict, b: dict, eta: list[int]) -> int:
    eta = _metric(eta)
    a, b = _form(a, len(eta)), _form(b, len(eta))
    return sum(x * b[I] * eta_I(eta, I) for I, x in a.items() if I in b)


def hodge(a: dict, eta: list[int]) -> dict:
    eta = _metric(eta)
    a = _form(a, len(eta))
    n = len(eta)
    out: dict = {}
    for I, x in a.items():
        Ic = tuple(i for i in range(n) if i not in I)
        s, _ = _sort_sign(I + Ic)
        out[Ic] = out.get(Ic, 0) + s * eta_I(eta, I) * x
    return _clean(out)
