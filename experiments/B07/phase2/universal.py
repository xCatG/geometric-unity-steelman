"""B07 Phase 2, unreduced search: every Spin(p,q)-equivariant real algebraic map X: Omega^2(ad) -> Omega^(n-1)(ad) in 4D.

ad = u(A) inside Cl(p,q) (A the Dirac pairing). Real basis of u(A)-valued k-forms: e^I (x) u_c with u_c = i^{ph(c)} G_c,
ph(c) in {0, 1} the phase that puts the blade in u(A) (B02, tests/test_shiab.py::_in_u_A). In this basis the Spin
generators 1/2 G_a G_b act by rational matrices, and X is u(A)-preserving iff its matrix is real. The equivariant maps
are the exact rational nullspace of rho_out(J) M - M rho_in(J) = 0 over the generators J of spin(p,q). Spin preserves
form degree and Clifford grade, so the space splits over Clifford-grade blocks (j in, l out), solved separately.
All arithmetic is exact (python-flint fmpq_mat; no floats).
"""
from __future__ import annotations

import itertools
from fractions import Fraction

from flint import fmpq, fmpq_mat

from gu.adjoint import from_mono, is_in_algebra
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import GQ, I, blade_to_mono, plus, scale
from gu.shiab import eta_of, generator_action

def phases(p: int, q: int) -> list[int]:
    gs, A = gammas(p, q), from_mono(dirac_pairing(p, q))
    out = []
    for c in range(1 << (p + q)):
        ok = [is_in_algebra(from_mono(blade_to_mono(c, gs).times_i_power(k)), A) for k in (0, 1)]
        if ok.count(True) != 1:
            raise AssertionError(f"blade {c}: u(A) membership {ok}")
        out.append(ok.index(True))
    return out


def basis(n: int, deg: int, grade: int) -> list[tuple[int, int]]:
    """(form mask, blade) pairs of the given form degree and Clifford grade."""
    fs = [sum(1 << i for i in c) for c in itertools.combinations(range(n), deg)]
    cs = [sum(1 << i for i in c) for c in itertools.combinations(range(n), grade)]
    return [(f, c) for f in fs for c in cs]


def to_phased(x: dict, ph: list[int]) -> dict:
    """Coordinates in the e^I (x) u_c basis: v G_c = (v i^{-ph}) u_c."""
    out = {}
    for (f, c), v in x.items():
        w = v * (GQ(0, -1) if ph[c] else GQ(1))
        if w.im:
            raise AssertionError(f"not u(A)-valued at {(f, c)}: {v}")
        out[(f, c)] = Fraction(w.re)
    return out


def from_phased(coords: dict, ph: list[int]) -> dict:
    return plus(*[{k: GQ(v) * (I if ph[k[1]] else GQ(1))} for k, v in coords.items() if v]) if coords else {}


def rho(p: int, q: int, deg: int, grade: int, ph: list[int]) -> list[list[list[Fraction]]]:
    """Matrices of the generators 1/2 G_a G_b (a < b) on the phased basis of one (degree, grade) block."""
    eta, n = eta_of(p, q), p + q
    B = basis(n, deg, grade)
    idx = {k: i for i, k in enumerate(B)}
    mats = []
    for a, b in itertools.combinations(range(n), 2):
        M = [[Fraction(0)] * len(B) for _ in B]
        for col, (f, c) in enumerate(B):
            img = to_phased(generator_action(from_phased({(f, c): Fraction(1)}, ph), a, b, eta), ph)
            for k, v in img.items():
                M[idx[k]][col] += v  # KeyError here would mean Spin mixes blocks
        mats.append(M)
    return mats


def equivariant_block(p: int, q: int, j: int, l: int, ph: list[int]) -> list[dict]:
    """Basis of equivariant maps from (2-forms, grade j) to ((n-1)-forms, grade l), each as {(out_key, in_key): q}."""
    n = p + q
    Bi, Bo = basis(n, 2, j), basis(n, n - 1, l)
    ri, ro = rho(p, q, 2, j, ph), rho(p, q, n - 1, l, ph)
    ni, no = len(Bi), len(Bo)
    unk = lambda r, s: r * ni + s
    rows = []
    for Ri, Ro in zip(ri, ro):
        for r in range(no):
            for s in range(ni):
                row = {}
                for k in range(no):
                    if Ro[r][k]:
                        row[unk(k, s)] = row.get(unk(k, s), 0) + Ro[r][k]
                for k in range(ni):
                    if Ri[k][s]:
                        row[unk(r, k)] = row.get(unk(r, k), 0) - Ri[k][s]
                row = {c: v for c, v in row.items() if v}
                if row:
                    rows.append(row)
    N = no * ni
    if not rows:
        null = [[Fraction(int(i == k)) for i in range(N)] for k in range(N)]
    else:
        A = fmpq_mat(len(rows), N)
        for i, row in enumerate(rows):
            for c, v in row.items():
                A[i, c] = fmpq(v.numerator, v.denominator)
        R, rank = A.rref()
        pivots, r = [], 0
        for c in range(N):
            if r < rank and R[r, c] != 0:
                pivots.append(c)
                r += 1
        free = [c for c in range(N) if c not in set(pivots)]
        null = []
        for fcol in free:
            v = [Fraction(0)] * N
            v[fcol] = Fraction(1)
            for i, pc in enumerate(pivots):
                e = R[i, fcol]
                v[pc] = -Fraction(int(e.p), int(e.q))
            null.append(v)
    return [{(Bo[u // ni], Bi[u % ni]): x for u, x in enumerate(v) if x} for v in null]


def equivariant_basis(p: int, q: int) -> list[dict]:
    ph, n = phases(p, q), p + q
    out = []
    for j in range(n + 1):
        for l in range(n + 1):
            out += equivariant_block(p, q, j, l, ph)
    return out


def as_map(M: dict, p: int, q: int, ph: list[int] | None = None):
    """The basis map M as a function on GQ-coefficient 2-forms (Linear-compatible)."""
    ph = ph or phases(p, q)
    by_in: dict = {}
    for (o, i), v in M.items():
        by_in.setdefault(i, []).append((o, v))

    def X(x: dict) -> dict:
        out: dict = {}
        for (f, c), v in x.items():
            w = v * (GQ(0, -1) if ph[c] else GQ(1))  # coordinate on u_c (complex allowed: complex-linear extension)
            for o, m in by_in.get((f, c), []):
                out = plus(out, {o: w * GQ(m) * (I if ph[o[1]] else GQ(1))})
        return out
    return X


def matrix_of(X, p: int, q: int, ph: list[int] | None = None) -> dict:
    """{(out_key, in_key): rational} of X in the phased real basis; raises if X does not preserve u(A)."""
    ph, n = ph or phases(p, q), p + q
    out = {}
    for j in range(n + 1):
        for k in basis(n, 2, j):
            img = X(from_phased({k: Fraction(1)}, ph))
            for o, v in (to_phased(img, ph) if img else {}).items():
                out[(o, k)] = v
    return out


def block_dims(p: int, q: int) -> dict:
    """{"j,l": dim} of the equivariant maps from Clifford grade j to grade l (nonzero blocks only)."""
    ph, n = phases(p, q), p + q
    out = {}
    for j in range(n + 1):
        for l in range(n + 1):
            d = len(equivariant_block(p, q, j, l, ph))
            if d:
                out[f"{j},{l}"] = d
    return out
