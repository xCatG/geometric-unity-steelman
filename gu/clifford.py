# gu/clifford.py
"""Exact gamma matrices for Cl(p,q) as monomial matrices over Z[i].

Convention: {G_a, G_b} = 2 eta_ab I, eta = diag(+1 x p, -1 x q).
A monomial matrix has one nonzero entry per column: M[perm[j], j] = i**phase[j].
Euclidean gammas come from the Jordan-Wigner construction; timelike ones are i times them.
"""
from __future__ import annotations

import numpy as np
from numbers import Integral

_RE = np.array([1, 0, -1, 0], dtype=np.int64)
_IM = np.array([0, 1, 0, -1], dtype=np.int64)


def _integer(value, name):
    if not isinstance(value, Integral):
        raise ValueError(f'{name} must be an exact integer')
    return int(value)


def _signature(p, q):
    p, q = _integer(p, 'p'), _integer(q, 'q')
    if p < 0 or q < 0:
        raise ValueError('signature counts must be nonnegative')
    return p, q


class Mono:
    __slots__ = ("perm", "phase")

    def __init__(self, perm, phase):
        perm, phase = np.asarray(perm, dtype=object), np.asarray(phase, dtype=object)
        if perm.ndim != 1 or phase.shape != perm.shape:
            raise ValueError('permutation and phase must be equal-length vectors')
        indices = [_integer(x, 'permutation entry') for x in perm]
        if sorted(indices) != list(range(len(indices))):
            raise ValueError('perm must permute 0..n-1')
        self.perm = np.array(indices, dtype=np.int64)
        self.phase = np.array([_integer(x, 'phase') % 4 for x in phase], dtype=np.int64)

    @staticmethod
    def identity(n: int) -> "Mono":
        n = _integer(n, 'dimension')
        if n < 0:
            raise ValueError('dimension must be nonnegative')
        return Mono(np.arange(n), np.zeros(n, dtype=np.int64))

    @property
    def n(self) -> int:
        return len(self.perm)

    def __matmul__(self, other: "Mono") -> "Mono":
        if self.n != other.n:
            raise ValueError('monomial dimensions must agree')
        return Mono(self.perm[other.perm], other.phase + self.phase[other.perm])

    def times_i_power(self, k: int) -> "Mono":
        return Mono(self.perm, self.phase + _integer(k, 'phase power') % 4)

    def __neg__(self) -> "Mono":
        return self.times_i_power(2)

    def dagger(self) -> "Mono":
        inv = np.empty_like(self.perm)
        inv[self.perm] = np.arange(self.n)
        phase = np.empty_like(self.phase)
        phase[self.perm] = -self.phase
        return Mono(inv, phase)

    def __eq__(self, other) -> bool:
        return (isinstance(other, Mono) and np.array_equal(self.perm, other.perm)
                and np.array_equal(self.phase, other.phase))

    __hash__ = None

    def trace(self) -> tuple[int, int]:
        fixed = self.phase[self.perm == np.arange(self.n)]
        return int(_RE[fixed].sum()), int(_IM[fixed].sum())

    def to_dense(self) -> tuple[np.ndarray, np.ndarray]:
        re = np.zeros((self.n, self.n), dtype=np.int64)
        im = np.zeros((self.n, self.n), dtype=np.int64)
        cols = np.arange(self.n)
        re[self.perm, cols] = _RE[self.phase]
        im[self.perm, cols] = _IM[self.phase]
        return re, im


def _kron(a: Mono, b: Mono) -> Mono:
    ja, jb = np.divmod(np.arange(a.n * b.n), b.n)
    return Mono(a.perm[ja] * b.n + b.perm[jb], a.phase[ja] + b.phase[jb])


_I2 = Mono([0, 1], [0, 0])
_X = Mono([1, 0], [0, 0])
_Y = Mono([1, 0], [1, 3])  # [[0,-i],[i,0]]
_Z = Mono([0, 1], [0, 2])


def _kron_all(ms: list[Mono]) -> Mono:
    out = ms[0]
    for m in ms[1:]:
        out = _kron(out, m)
    return out


def eta(p: int, q: int) -> list[int]:
    p, q = _signature(p, q)
    return [1] * p + [-1] * q


def gammas(p: int, q: int) -> list[Mono]:
    p, q = _signature(p, q)
    d = p + q
    if d % 2 or d == 0:
        raise ValueError("gammas() supports even p+q >= 2 only")
    m = d // 2
    euclid = []
    for k in range(m):
        for P in (_X, _Y):
            euclid.append(_kron_all([_Z] * k + [P] + [_I2] * (m - k - 1)))
    return [g if a < p else g.times_i_power(1) for a, g in enumerate(euclid)]


def _product(ms: list[Mono], n: int) -> Mono:
    out = Mono.identity(n)
    for m in ms:
        out = out @ m
    return out


def dirac_pairing(p: int, q: int) -> Mono:
    """Phase times the product of the timelike gammas, chosen Hermitian."""
    G = gammas(p, q)
    A0 = _product(G[p:], G[0].n)
    for k in range(4):
        A = A0.times_i_power(k)
        if A.dagger() == A:
            return A
    raise AssertionError("no Hermitian phase for A")  # unreachable: A0^dagger = +-A0


def chirality(p: int, q: int) -> Mono:
    """Phase times G_0...G_{d-1}, chosen with C^2 = I and C Hermitian."""
    G = gammas(p, q)
    P = _product(G, G[0].n)
    I = Mono.identity(G[0].n)
    for k in range(4):
        C = P.times_i_power(k)
        if C @ C == I and C.dagger() == C:
            return C
    raise AssertionError("no chirality phase")
