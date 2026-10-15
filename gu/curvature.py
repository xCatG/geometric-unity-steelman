# gu/curvature.py
"""Algebraic curvature tensors and their exact scalar / traceless-Ricci / Weyl split.

Convention (pinned, spec rev 4.1): R[a,b,c,d] is antisymmetric in (a,b) and (c,d),
pair-symmetric, and satisfies first Bianchi. Ric[b,d] = eta^{ac} R[a,b,c,d]
(contract slots 1 and 3). Unit sphere: R = eta_ac eta_bd - eta_ad eta_bc, Ric = (n-1) eta.
R = W + Ric0 (KN) g / (n-2) + S g (KN) g / (2n(n-1)). Integer arithmetic with an explicit denominator.
Intermediate arithmetic uses Python integers. Returned arrays are int64; an
out-of-range result raises OverflowError instead of silently wrapping.
"""
from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral

import numpy as np


def _integer(x):
    if not isinstance(x, Integral):
        raise ValueError('curvature operations require exact integers')
    return int(x)


def _array(a, rank):
    a = np.asarray(a)
    if a.ndim != rank or len(set(a.shape)) != 1:
        raise ValueError(f'expected equal-sided rank-{rank} array')
    if a.dtype.kind in 'iu':
        return a.astype(object)
    return np.array([_integer(x) for x in a.flat], dtype=object).reshape(a.shape)


def _metric(eta, n):
    eta = _array(eta, 1)
    if len(eta) != n or any(x not in (-1, 1) for x in eta):
        raise ValueError('eta must have one +/-1 entry per dimension')
    return eta


def _int64(a):
    bounds = np.iinfo(np.int64)
    if a.size and (a.min() < bounds.min or a.max() > bounds.max):
        raise OverflowError('exact curvature result exceeds int64')
    return np.asarray(a, dtype=np.int64)


def kulkarni_nomizu(h: np.ndarray, k: np.ndarray) -> np.ndarray:
    h, k = _array(h, 2), _array(k, 2)
    if h.shape != k.shape:
        raise ValueError('bilinear forms must have the same shape')
    return _int64(np.einsum("ac,bd->abcd", h, k) + np.einsum("bd,ac->abcd", h, k)
                  - np.einsum("ad,bc->abcd", h, k) - np.einsum("bc,ad->abcd", h, k))


def ricci(R: np.ndarray, eta: np.ndarray) -> np.ndarray:
    R = _array(R, 4)
    eta = _metric(eta, len(R))
    return _int64(np.einsum("a,abad->bd", eta, R))


def scalar(R: np.ndarray, eta: np.ndarray) -> int:
    R = _array(R, 4)
    eta = _metric(eta, len(R))
    return int(np.einsum("b,bb->", eta, ricci(R, eta).astype(object)))


def is_algebraic_curvature(R: np.ndarray) -> bool:
    R = _array(R, 4)
    return bool(np.array_equal(R, -np.einsum("bacd->abcd", R))
                and np.array_equal(R, -np.einsum("abdc->abcd", R))
                and np.array_equal(R, np.einsum("cdab->abcd", R))
                and not (R + np.einsum("acdb->abcd", R) + np.einsum("adbc->abcd", R)).any())


@dataclass
class Split:
    denominator: int
    scalar_part: np.ndarray
    ricci_part: np.ndarray
    weyl: np.ndarray


def decompose(R: np.ndarray, eta: np.ndarray) -> Split:
    R = _array(R, 4)
    eta = _metric(eta, len(R))
    n = len(eta)
    if n < 3:
        raise ValueError("decompose() needs n >= 3")
    g = np.diag(eta)
    S = scalar(R, eta)
    N = 2 * n * (n - 1) * (n - 2)
    n_ric0 = n * ricci(R, eta).astype(object) - S * g     # n * Ric0, integer
    ricci_part = 2 * (n - 1) * kulkarni_nomizu(n_ric0, g).astype(object)
    scalar_part = (n - 2) * S * kulkarni_nomizu(g, g).astype(object)
    return Split(N, _int64(scalar_part), _int64(ricci_part),
                 _int64(N * R - ricci_part - scalar_part))


def dims(n: int) -> tuple[int, int, int]:
    n = _integer(n)
    if n < 3:
        raise ValueError('curvature component dimensions require n >= 3')
    return 1, n * (n + 1) // 2 - 1, n * (n + 1) * (n + 2) * (n - 3) // 12


def random_curvature(n: int, rng: np.random.Generator, terms: int = 6) -> np.ndarray:
    n, terms = _integer(n), _integer(terms)
    if n < 1 or terms < 0:
        raise ValueError('n must be positive and terms nonnegative')
    R = np.zeros((n, n, n, n), dtype=object)
    for _ in range(terms):
        h = rng.integers(-3, 4, (n, n)); h = h + h.T
        k = rng.integers(-3, 4, (n, n)); k = k + k.T
        R += kulkarni_nomizu(h, k)
    return _int64(R)
