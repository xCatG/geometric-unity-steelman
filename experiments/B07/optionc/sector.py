"""B07 option C, the linear T-sector of I2 (design: docs/superpowers/specs/2026-10-17-b07-optionc-design.md, rev 3.1).

Flat background, B = d, eps = 1, metric frozen, delta T = delta A (Phase 2 reading V); 4D, pinned star; exact.
Real field basis: phased u(A)-valued forms e^I (x) i^{ph(c)} G_c (`universal.phases`), ordered by Clifford grade
(`universal.basis(n, deg, g)` for g = 0..n), so the Spin generators `universal.rho` act block-diagonally.

First-order symbol of the linearized Upsilon = X(dT) + kappa *T (9.7) on T = t e^{ik.x}:
    U(k) = X(iK ^ .) + kappa * = i A(k) + kappa S,  A(k) = X(K ^ .), S = *: Omega^1 -> Omega^3 (both 64-dim, rational).
    N(k) = S^-1 A(k), so U(k) = S (i N(k) + kappa).
Hessian (Phase 2 H14's first variation B(a, t) = 2 <U(-k) a, U(k) t>):
    M(k) = 2 U(-k)^T G3 U(k) = S0(k) + kappa S1(k) + kappa^2 S2,
    S0 = 2 A^T G3 A,  S1 = 2i (S^T G3 A - A^T G3 S),  S2 = 2 S^T G3 S = 2 (-1)^q G1.
G1, G3: the Gram matrices of the pinned pairing <x, y> = Tr(x ^ *y)/2^(n/2) (`second_order.mpair`) on the phased bases.
"""
from __future__ import annotations

import itertools
from fractions import Fraction

from flint import fmpq, fmpq_mat

from gu.cliffform import GQ, plus, scale
from experiments.B07 import variation as V
from experiments.B07.phase2 import second_order as SO2, universal as U
from experiments.B07.phase2.run import e_op

OPERATORS = ("CCC", "CAA", "CAC", "E_OP")
SIGS = [(3, 1), (1, 3)]
AUX_SIGS = [(2, 2), (4, 0)]
EXTRA_K = [1, -2, 3, 1]   # a wavevector outside every determining set (reconstruction control)


def operator(name: str, p: int, q: int):
    if name == "E_OP":
        return e_op(p, q)
    return V.branch_map(next(k for k in V.BRANCHES if k.startswith(name)), p, q)


def grade_basis(n: int, deg: int) -> list[tuple[int, int]]:
    return [k for g in range(n + 1) for k in U.basis(n, deg, g)]


def fq(x: Fraction) -> fmpq:
    return fmpq(x.numerator, x.denominator)


def mat(rows: list[list[Fraction]]) -> fmpq_mat:
    return fmpq_mat(len(rows), len(rows[0]), [fq(Fraction(v)) for r in rows for v in r])


def entries(M: fmpq_mat) -> list[list[Fraction]]:
    return [[Fraction(int(M[i, j].p), int(M[i, j].q)) for j in range(M.ncols())] for i in range(M.nrows())]


def is_zero(M: fmpq_mat) -> bool:
    return all(M[i, j] == 0 for i in range(M.nrows()) for j in range(M.ncols()))


class Sector:
    """Phased-basis matrices of one operator X at one signature (exact rationals)."""

    def __init__(self, X, p: int, q: int):
        self.p, self.q, self.n = p, q, p + q
        self.eta, self.ph = V.eta_of(p, q), U.phases(p, q)
        self.X = V.Linear(X)
        self.B1, self.B3 = grade_basis(self.n, 1), grade_basis(self.n, self.n - 1)
        self.i1 = {k: i for i, k in enumerate(self.B1)}
        self.i3 = {k: i for i, k in enumerate(self.B3)}
        self.S = self._matrix(lambda t: SO2.star_c(t, self.eta, "pinned"), self.B1, self.i3)
        self.A = [self._matrix(lambda t, m=m: self.X(V.wedge_prod({(1 << m, 0): GQ(1)}, t, self.eta)),
                               self.B1, self.i3) for m in range(self.n)]
        self.G1, self.G3 = self._gram(self.B1), self._gram(self.B3)
        self.Sinv = self.S.inv()
        self._ft: dict = {}

    def element(self, key) -> dict:
        return U.from_phased({key: Fraction(1)}, self.ph)

    def _matrix(self, f, src: list, dst: dict) -> fmpq_mat:
        """Columns: phased coordinates of f(basis element); to_phased raises if the image is not u(A)-valued."""
        cols = []
        for key in src:
            img = f(self.element(key))
            c = U.to_phased(img, self.ph) if img else {}
            col = [Fraction(0)] * len(dst)
            for k, v in c.items():
                col[dst[k]] = v
            cols.append(col)
        return mat([[cols[j][i] for j in range(len(src))] for i in range(len(dst))])

    def _gram(self, B: list) -> fmpq_mat:
        """Full Gram matrix of the pinned pairing on a phased basis; asserted real, diagonal and +-1."""
        els = [self.element(k) for k in B]
        rows = []
        for i, x in enumerate(els):
            row = []
            for j, y in enumerate(els):
                g = SO2.mpair(x, y, self.eta, "pinned")
                if g.im:
                    raise AssertionError(f"Gram not real at {B[i]}, {B[j]}: {g}")
                if (i == j and g.re not in (1, -1)) or (i != j and g.re):
                    raise AssertionError(f"Gram not diagonal +-1 at {B[i]}, {B[j]}: {g}")
                row.append(Fraction(g.re))
            rows.append(row)
        return mat(rows)

    def A_of(self, k: list) -> fmpq_mat:
        out = fmpq_mat(len(self.B3), len(self.B1))
        for m, c in enumerate(k):
            if c:
                out += self.A[m] * fq(Fraction(c))
        return out

    def N_of(self, k: list) -> fmpq_mat:
        return self.Sinv * self.A_of(k)

    def parts(self, k: list) -> tuple[fmpq_mat, fmpq_mat, fmpq_mat]:
        """(S0(k), R1(k), S2) with S1(k) = i R1(k): all rational."""
        A, S, G = self.A_of(k), self.S, self.G3
        return 2 * A.transpose() * G * A, 2 * (S.transpose() * G * A - A.transpose() * G * S), \
            2 * S.transpose() * G * S

    # ---- comparison with Phase 2's fourier_terms (raw basis variation.one_forms) ----
    def fourier(self, k: list[int], conv: str = "pinned") -> dict:
        """second_order.fourier_terms for this operator, memoized per (k, conv)."""
        key = (tuple(k), conv)
        if key not in self._ft:
            self._ft[key] = SO2.fourier_terms(self.X, self.p, self.q, k, conv)
        return self._ft[key]

    def phased_from_raw(self, raw: dict) -> list[list[GQ]]:
        """Pi^T M_raw Pi in the grade-ordered phased basis (bilinear congruence, no conjugation)."""
        nb, size = 1 << self.n, len(self.B1)
        out = [[GQ() for _ in range(size)] for _ in range(size)]
        pi = [GQ(0, 1) if self.ph[c] else GQ(1) for (_, c) in self.B1]
        ridx = [(f.bit_length() - 1) * nb + c for (f, c) in self.B1]
        back = {r: i for i, r in enumerate(ridx)}
        for (ra, rt), v in raw.items():
            a, t = back[ra], back[rt]
            out[a][t] = v * pi[a] * pi[t]
        return out


def fourier_parts(sec: Sector, X, k: list[int], conv: str = "pinned") -> dict:
    """{"k0","k1","k2"}: Phase 2 fourier_terms' action parts, phased (an independent code path from Sector)."""
    m = sec.fourier(k, conv)
    return {name: sec.phased_from_raw(m["action_" + name]) for name in ("k0", "k1", "k2")}


def gram_identity(sec: Sector, X, k: list[int]) -> bool:
    """Control 4: fourier_terms' (k0, k1, k2) equal (S0, i R1, S2) entrywise."""
    S0, R1, S2 = sec.parts(k)
    f = fourier_parts(sec, X, k)
    want = {"k0": (S0, False), "k1": (R1, True), "k2": (S2, False)}
    for name, (M, imag) in want.items():
        for i, row in enumerate(f[name]):
            for j, v in enumerate(row):
                w = Fraction(int(M[i, j].p), int(M[i, j].q))
                if (v.re, v.im) != ((Fraction(0), w) if imag else (w, Fraction(0))):
                    return False
    return True


def prime_identity(sec: Sector, X, k: list[int]) -> bool:
    """Fixed-X prime convention: M'(k; kappa) = -M(k; -kappa), i.e. k0' = -k0, k1' = k1, k2' = -k2."""
    a, b = fourier_parts(sec, X, k, "pinned"), fourier_parts(sec, X, k, "prime")
    sign = {"k0": -1, "k1": 1, "k2": -1}
    return all(b[nm][i][j] == a[nm][i][j] * GQ(sign[nm])
               for nm in sign for i in range(len(sec.B1)) for j in range(len(sec.B1)))


def reconstruction(sec: Sector, X) -> bool:
    """Control 2: fourier_terms' S0 (degree 2) and S1 (degree 1), fitted on the determining wavevectors, predict
    their values at EXTRA_K; S2 equals its k = 0 value there."""
    n = sec.n
    e = lambda *ix: [int(i in ix) for i in range(n)]
    f1 = {i: fourier_parts(sec, X, e(i)) for i in range(n)}
    f2 = {(i, j): fourier_parts(sec, X, e(i, j)) for i, j in itertools.combinations(range(n), 2)}
    fx = fourier_parts(sec, X, EXTRA_K)
    size, kx = len(sec.B1), EXTRA_K
    for a in range(size):
        for t in range(size):
            s0 = sum((f1[i]["k0"][a][t] * GQ(kx[i] ** 2) for i in range(n)), GQ())
            s0 = s0 + sum(((f2[i, j]["k0"][a][t] - f1[i]["k0"][a][t] - f1[j]["k0"][a][t]) * GQ(kx[i] * kx[j])
                           for i, j in itertools.combinations(range(n), 2)), GQ())
            s1 = sum((f1[i]["k1"][a][t] * GQ(kx[i]) for i in range(n)), GQ())
            if s0 != fx["k0"][a][t] or s1 != fx["k1"][a][t] or fx["k2"][a][t] != f1[0]["k2"][a][t]:
                return False
    return True


def fourier_symmetry(sec: Sector) -> bool:
    """Control 1: S0, S2 symmetric and real, S1 = i R1 antisymmetric (so M(k) = M(-k)^T and conj M(k) = M(-k));
    N rational holds by construction (to_phased raises otherwise)."""
    for m in range(sec.n):
        S0, R1, S2 = sec.parts([int(i == m) for i in range(sec.n)])
        if S0 != S0.transpose() or S2 != S2.transpose() or R1 != -R1.transpose():
            return False
    return True


def rho_full(sec: Sector, deg: int) -> list[fmpq_mat]:
    """The six spin(p,q) generators on the grade-ordered phased basis of `deg`-forms (block diagonal)."""
    blocks = [U.rho(sec.p, sec.q, deg, g, sec.ph) for g in range(sec.n + 1)]
    size, out = sum(len(b[0]) for b in blocks), []
    for J in range(len(blocks[0])):
        M, off = fmpq_mat(size, size), 0
        for b in blocks:
            for i, row in enumerate(b[J]):
                for j, v in enumerate(row):
                    if v:
                        M[off + i, off + j] = fq(v)
            off += len(b[J])
        out.append(M)
    return out


def covariance(sec: Sector) -> dict:
    """Control 5: rho3 A(e_m) - A(e_m) rho1 = sum_l Lam[l][m] A(e_l), rho3 S = S rho1, tr rho = 0 (identity component);
    the invariant-pairing condition rho^T G + G rho = 0 on 1- and 3-forms, and the covariance equations
    rho^T S(k) + S(k) rho + (d/ds) S(k + s Lam k)|_0 = 0 for S0, S1 = i R1 and S2, at EXTRA_K."""
    r1, r3 = rho_full(sec, 1), rho_full(sec, sec.n - 1)
    lam = U.rho(sec.p, sec.q, 1, 0, sec.ph)          # covector action, basis (1 << l, 0)
    ok_A = ok_S = ok_G = ok_eq = True
    k = EXTRA_K
    S0, R1, S2 = sec.parts(k)
    for J in range(len(r1)):
        ok_G &= is_zero(r1[J].transpose() * sec.G1 + sec.G1 * r1[J]) and             is_zero(r3[J].transpose() * sec.G3 + sec.G3 * r3[J])
        v = [sum((Fraction(lam[J][l][m]) * k[m] for m in range(sec.n)), Fraction(0)) for l in range(sec.n)]
        Pv, Pkv = sec.parts(v), sec.parts([a + b for a, b in zip(k, v)])
        d0 = Pkv[0] - S0 - Pv[0]                       # S0 is quadratic: d/ds S0(k + s v)|_0 = S0(k+v) - S0(k) - S0(v)
        ok_eq &= is_zero(r1[J].transpose() * S0 + S0 * r1[J] + d0) and             is_zero(r1[J].transpose() * R1 + R1 * r1[J] + Pv[1]) and is_zero(r1[J].transpose() * S2 + S2 * r1[J])
        ok_S &= r3[J] * sec.S == sec.S * r1[J]
        for m in range(sec.n):
            rhs = fmpq_mat(len(sec.B3), len(sec.B1))
            for l in range(sec.n):
                if lam[J][l][m]:
                    rhs += sec.A[l] * fq(lam[J][l][m])
            ok_A &= r3[J] * sec.A[m] - sec.A[m] * r1[J] == rhs
    traces = all(sum((R[i, i] for i in range(R.nrows())), fmpq(0)) == 0 for R in r1 + r3)
    return {"A_intertwines": bool(ok_A), "star_intertwines": bool(ok_S), "traceless": bool(traces),
            "pairing_invariant": bool(ok_G), "hessian_covariant": bool(ok_eq),
            "covariance_verified": bool(ok_A and ok_S and traces and ok_G and ok_eq)}


def s1_closed_form(sec: Sector, m: int) -> bool:
    """Q1 closed form: S1(e_m)(a, t) = 2 (-1)^(q+1) i [pair(t, X(e^m ^ a)) - pair(a, X(e^m ^ t))] (pair = Tr/2^(n/2))."""
    _, R1, _ = sec.parts([int(i == m) for i in range(sec.n)])
    K = {(1 << m, 0): GQ(1)}
    els = [sec.element(k) for k in sec.B1]
    img = [sec.X(V.wedge_prod(K, x, sec.eta)) for x in els]
    s = 2 * (-1) ** (sec.q + 1)
    for a, xa in enumerate(els):
        for t, xt in enumerate(els):
            v = (V.pair(xt, img[a], sec.eta) - V.pair(xa, img[t], sec.eta)) * GQ(0, s)
            if v != GQ(0, Fraction(int(R1[a, t].p), int(R1[a, t].q))):
                return False
    return True


def direct_hessian(sec: Sector, k: list[int], pairs: list[tuple[int, int]]) -> list[GQ]:
    """Control 3: B(a, t) = 2 <X(-iK ^ a) + *a, X(iK ^ t) + *t> (kappa = 1) evaluated directly on dicts."""
    K = {(1 << m, 0): GQ(c) for m, c in enumerate(k) if c}
    out = []
    for a, t in pairs:
        xa, xt = sec.element(sec.B1[a]), sec.element(sec.B1[t])
        ua = plus(sec.X(scale(V.wedge_prod(K, xa, sec.eta), GQ(0, -1))), SO2.star_c(xa, sec.eta, "pinned"))
        ut = plus(sec.X(scale(V.wedge_prod(K, xt, sec.eta), GQ(0, 1))), SO2.star_c(xt, sec.eta, "pinned"))
        out.append(SO2.mpair(ua, ut, sec.eta, "pinned") * GQ(2))
    return out


# ---- control 8: raw-basis convention controls (valid with or without real u(A)-closure; complex bilinear over Q(i)) ----
# `ft(k, conv)` is second_order.fourier_terms(X, p, q, k, conv) for one operator (memoized by the caller).
def raw_gram(p: int, q: int) -> dict:
    """{(a, t): <a, t>} of the pinned pairing on the raw basis variation.one_forms (no phases, no closure needed)."""
    eta, basis = V.eta_of(p, q), V.one_forms(p + q)
    out = {}
    for ai, a in enumerate(basis):
        for ti, t in enumerate(basis):
            g = SO2.mpair(a, t, eta, "pinned")
            if g:
                out[(ai, ti)] = g
    return out


def raw_s2_identity(ft, p: int, q: int) -> bool:
    """S2 = 2 (-1)^q G1 on the raw basis, from fourier_terms at k = 0."""
    m, G = ft((0,) * (p + q), "pinned")["action_k2"], raw_gram(p, q)
    return all(m.get(k, GQ()) == G.get(k, GQ()) * GQ(2 * (-1) ** q) for k in set(m) | set(G))


def raw_prime_identity(ft, k: tuple) -> bool:
    """Fixed-X prime convention on raw fourier_terms: k0' = -k0, k1' = k1, k2' = -k2."""
    a, b = ft(k, "pinned"), ft(k, "prime")
    for nm, s in (("k0", -1), ("k1", 1), ("k2", -1)):
        A, B = a["action_" + nm], b["action_" + nm]
        if any(B.get(key, GQ()) != A.get(key, GQ()) * GQ(s) for key in set(A) | set(B)):
            return False
    return True


def raw_reconstruction(ft, n: int) -> bool:
    """Control 2 on raw fourier_terms (as `reconstruction`, without the phased basis)."""
    e = lambda *ix: tuple(int(i in ix) for i in range(n))
    f1 = {i: ft(e(i), "pinned") for i in range(n)}
    f2 = {(i, j): ft(e(i, j), "pinned") for i, j in itertools.combinations(range(n), 2)}
    fx, kx = ft(tuple(EXTRA_K), "pinned"), EXTRA_K
    g = lambda m, nm, key: m["action_" + nm].get(key, GQ())
    keys = set()
    for m in [*f1.values(), *f2.values(), fx]:
        for nm in ("k0", "k1", "k2"):
            keys |= set(m["action_" + nm])
    for key in keys:
        s0 = sum((g(f1[i], "k0", key) * GQ(kx[i] ** 2) for i in range(n)), GQ())
        s0 = s0 + sum(((g(f2[i, j], "k0", key) - g(f1[i], "k0", key) - g(f1[j], "k0", key)) * GQ(kx[i] * kx[j])
                       for i, j in itertools.combinations(range(n), 2)), GQ())
        s1 = sum((g(f1[i], "k1", key) * GQ(kx[i]) for i in range(n)), GQ())
        if s0 != g(fx, "k0", key) or s1 != g(fx, "k1", key) or g(fx, "k2", key) != g(f1[0], "k2", key):
            return False
    return True
