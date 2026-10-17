"""B07 escape, Task 4: independent re-derivation of E1 and E2 (exact arithmetic only).

Imports only the standard library, numpy and gu.clifford (gamma matrices, chirality,
Dirac pairing).  Every other construction is rebuilt here from the formulas in
experiments/B07/escape/derivations.md, experiments/B02/transcription.md,
experiments/B02/proofs.md, experiments/B02/README.md and
experiments/B07/phase2/derivations.md / README.md:

* forms on R^{p,q}: dict {bitmask: 4x4 Gaussian-rational matrix}; bit a <-> e^a;
* pinned Hodge star  alpha ^ *beta = <alpha, beta> vol,  vol = e^0 ^ e^1 ^ e^2 ^ e^3;
* xi(R) = 1/2 sum_{a<b, c<d} R_abcd eta_c eta_d e^{ab} (x) G_c G_d   (B02 README, normalization
  pinned by B02's documented response -E_F(Ric); see fix note in xi);
* F = sum e^a G_a, F' = sum e^a G_a C, B = sum_{a<b} e^{ab} G_a G_b, B' = ... i G_a G_b C;
* brackets: C: X Y - Y X ; A: i (X Y + Y X), componentwise, ungraded (B02 proofs);
* Shiab(x) = [Phi1 ^ *x]_{m0} - 1/2 * [Phi1 ^ *[Phi2 ^ *x]_{m1}]_{m2}   (9.3);
* E_OP = -2 first[C](F) - second[CC](F,B) + second[AA](F,B), second = *[F ^ *[B ^ *x]]
  (B07 phase2 README; checked here against its stated response 2E_F(Ric) - S E_F(g));
* pairing <x, y> = Tr(x ^ *y) / 2^{n/2} with the actual matrix trace;
* u(A): X# = A^{-1} X^dagger A = -X; blade phase = smallest k with i^k G_I in u(A);
* dressing h = (1 - X)(1 + X)^{-1}, X = u_I / 2;  c_h(x) = h^{-1} x h.

Run:  uv run python -m experiments.B07.escape.rederive
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

from gu.clifford import chirality, dirac_pairing, gammas

N = 4
DIM = 4  # spinor dimension 2^{n/2}
FULL = (1 << N) - 1
RESULT = Path(__file__).with_name("result.json")


# --------------------------------------------------------------------------- exactness

def q(x) -> Fraction:
    """The single exact coercion helper: ints, numpy ints and Fractions only."""
    if isinstance(x, bool):
        raise TypeError("bool is not a number here")
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, np.integer):
        return Fraction(x.item())
    raise TypeError(f"inexact or unsupported number {x!r} ({type(x).__name__})")


def qs(s: str) -> Fraction:
    return Fraction(s)


# --------------------------------------------------------------------------- Gaussian-rational matrices

def _zeros():
    return np.array([[Fraction(0)] * DIM for _ in range(DIM)], dtype=object)


class GM:
    """4x4 matrix over Q(i), stored as (re, im) object arrays of Fractions."""
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re, self.im = re, im

    @staticmethod
    def zero():
        return GM(_zeros(), _zeros())

    @staticmethod
    def eye():
        m = GM.zero()
        for k in range(DIM):
            m.re[k, k] = Fraction(1)
        return m

    def __add__(self, o):
        return GM(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return GM(self.re - o.re, self.im - o.im)

    def __neg__(self):
        return GM(-self.re, -self.im)

    def __matmul__(self, o):
        return GM(self.re.dot(o.re) - self.im.dot(o.im), self.re.dot(o.im) + self.im.dot(o.re))

    def smul(self, a, b=0):
        """(a + i b) * self."""
        a, b = q(a), q(b)
        return GM(a * self.re - b * self.im, a * self.im + b * self.re)

    def times_i(self):
        return GM(-self.im, self.re.copy())

    def dagger(self):
        return GM(self.re.T.copy(), -self.im.T)

    def is_zero(self):
        return all(v == 0 for v in self.re.flat) and all(v == 0 for v in self.im.flat)

    def __eq__(self, o):
        return (self - o).is_zero()

    __hash__ = None

    def trace(self):
        return (sum(self.re[k, k] for k in range(DIM)), sum(self.im[k, k] for k in range(DIM)))

    def flat(self):
        return list(self.re.flat) + list(self.im.flat)


def from_mono(m) -> GM:
    re, im = m.to_dense()
    R = np.array([[q(v) for v in row] for row in re], dtype=object)
    I = np.array([[q(v) for v in row] for row in im], dtype=object)
    return GM(R, I)


# --------------------------------------------------------------------------- exact linear algebra

def rref_rank(rows):
    """Rank of a list of Fraction row vectors (exact Gaussian elimination)."""
    M = [list(r) for r in rows if any(v != 0 for v in r)]
    if not M:
        return 0
    ncol = len(M[0])
    rank, col = 0, 0
    while rank < len(M) and col < ncol:
        piv = next((i for i in range(rank, len(M)) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        M[rank] = [v / pv for v in M[rank]]
        for i in range(len(M)):
            if i != rank and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rank])]
        rank += 1
        col += 1
    return rank


def solve(A, b):
    """Exact solution x of A x = b (unique required), or None if inconsistent."""
    m, n = len(A), len(A[0])
    M = [list(A[i]) + [b[i]] for i in range(m)]
    rank, col, pivcols = 0, 0, []
    while rank < m and col < n:
        piv = next((i for i in range(rank, m) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        M[rank] = [v / pv for v in M[rank]]
        for i in range(m):
            if i != rank and M[i][col] != 0:
                f = M[i][col]
                M[i] = [x - f * y for x, y in zip(M[i], M[rank])]
        pivcols.append(col)
        rank += 1
        col += 1
    if any(M[i][n] != 0 for i in range(rank, m)):
        return None
    if rank != n:
        raise AssertionError("fit is underdetermined: invariants not independent on the basis")
    x = [Fraction(0)] * n
    for i, c in enumerate(pivcols):
        x[c] = M[i][n]
    return x


# --------------------------------------------------------------------------- forms

def popcount(m):
    return bin(m).count("1")


def bits(m):
    return [a for a in range(N) if m >> a & 1]


def wsign(I, J):
    """e^I ^ e^J = wsign * e^{I|J}; 0 if they overlap."""
    if I & J:
        return 0
    c = sum(1 for i in bits(I) for j in bits(J) if i > j)
    return -1 if c % 2 else 1


def fadd(*forms):
    out = {}
    for f in forms:
        for k, v in f.items():
            out[k] = out[k] + v if k in out else v
    return {k: v for k, v in out.items() if not v.is_zero()}


def fscale(f, a, b=0):
    return {k: v.smul(a, b) for k, v in f.items()}


def fmap(f, fn):
    return {k: fn(v) for k, v in f.items()}


def fzero(f):
    return all(v.is_zero() for v in f.values())


def feq(f, g):
    return fzero(fadd(f, fscale(g, -1)))


def fflat(f, degree):
    out = []
    for m in range(1 << N):
        if popcount(m) == degree:
            out += f[m].flat() if m in f else [Fraction(0)] * (2 * DIM * DIM)
    return out


class Geometry:
    def __init__(self, p, qq):
        self.p, self.q = p, qq
        self.eta = [1] * p + [-1] * qq
        self.G = [from_mono(g) for g in gammas(p, qq)]
        self.C = from_mono(chirality(p, qq))
        self.A = from_mono(dirac_pairing(p, qq))
        self.Ainv = self.A.dagger()  # monomial with unit phases -> unitary
        assert self.A @ self.Ainv == GM.eye()
        self.one = GM.eye()
        for a in range(N):
            for b in range(N):
                ac = self.G[a] @ self.G[b] + self.G[b] @ self.G[a]
                assert ac == self.one.smul(2 * self.eta[a] if a == b else 0)
        self.blade = {}
        for m in range(1 << N):
            M = GM.eye()
            for a in bits(m):
                M = M @ self.G[a]
            self.blade[m] = M
        self.phase = {m: self._phase(m) for m in range(1, 1 << N)}

    def eta_mask(self, m):
        s = 1
        for a in bits(m):
            s *= self.eta[a]
        return s

    # Hodge star, pinned: e^I ^ *e^I = eta_I vol
    def star(self, f, prime=False):
        out = {}
        for I, X in f.items():
            J = FULL ^ I
            s = self.eta_mask(I) * wsign(I, J)
            if prime:
                s *= (-1) ** popcount(I)
            out = fadd(out, {J: X.smul(s)})
        return out

    def star_inv(self, f):
        """Inverse of the pinned star: z with star(z) = f."""
        out = {}
        for J, Y in f.items():
            I = FULL ^ J
            s = self.eta_mask(I) * wsign(I, J)
            out = fadd(out, {I: Y.smul(s)})  # s = +-1, so 1/s = s
        assert feq(self.star(out), f)
        return out

    @staticmethod
    def bracket(x, y, mode):
        out = {}
        for I, X in x.items():
            for J, Y in y.items():
                s = wsign(I, J)
                if s == 0:
                    continue
                P, Qm = X @ Y, Y @ X
                v = (P - Qm) if mode == "C" else (P + Qm).times_i()
                out = fadd(out, {I | J: v.smul(s)})
        return out

    def pair(self, x, y, prime=False):
        """<x, y> = Tr(x ^ *y) / 2^{n/2}: returns (re, im)."""
        top = self.wedge_trace_form(x, self.star(y, prime))
        return top

    def wedge_trace_form(self, x, y):
        re, im = Fraction(0), Fraction(0)
        for I, X in x.items():
            J = FULL ^ I
            if J in y:
                s = wsign(I, J)
                t = (X @ y[J]).trace()
                re += s * t[0]
                im += s * t[1]
        return (re / DIM, im / DIM)

    # u(A)
    def sharp(self, X):
        return self.Ainv @ X.dagger() @ self.A

    def in_uA(self, X):
        return self.sharp(X) == -X

    def _phase(self, m):
        M = self.blade[m]
        for k in range(4):
            if self.in_uA(M):
                return k
            M = M.times_i()
        raise AssertionError(f"no u(A) phase for blade {m}")

    def u(self, m, extra=0):
        M = self.blade[m]
        for _ in range((self.phase[m] + extra) % 4):
            M = M.times_i()
        return M

    # Phi bases
    def F(self):
        return {1 << a: self.G[a] for a in range(N)}

    def Fp(self):
        return {1 << a: self.G[a] @ self.C for a in range(N)}

    def B(self):
        return {(1 << a) | (1 << b): self.G[a] @ self.G[b] for a in range(N) for b in range(a + 1, N)}

    def Bp(self):
        return {(1 << a) | (1 << b): (self.G[a] @ self.G[b] @ self.C).times_i()
                for a in range(N) for b in range(a + 1, N)}

    # xi
    def xi(self, R):
        out = {}
        for a in range(N):
            for b in range(a + 1, N):
                M = GM.zero()
                for c in range(N):
                    for d in range(c + 1, N):
                        # sum over a<b, c<d with weight 1/2: the normalization that reproduces
                        # B02's documented KN(g,g) response -2(n-1)F (CCC) and *Shiab = -E_F(Ric).
                        # (Reading the README's 1/2 sum over all a,b,c,d gives 4x this; run 1 log.)
                        coef = Fraction(1, 2) * R[a, b, c, d] * self.eta[c] * self.eta[d]
                        if coef != 0:
                            M = M + (self.G[c] @ self.G[d]).smul(coef)
                if not M.is_zero():
                    out[(1 << a) | (1 << b)] = M
        return out

    def E(self, H, chiral=False):
        out = {}
        for a in range(N):
            M = GM.zero()
            for b in range(N):
                coef = H[a, b] * self.eta[b]
                if coef != 0:
                    g = self.G[b] @ self.C if chiral else self.G[b]
                    M = M + g.smul(coef)
            if not M.is_zero():
                out[1 << a] = M
        return out


# --------------------------------------------------------------------------- operators

def shiab(g, x, phi1, phi2, modes):
    m0, m1, m2 = modes
    sx = g.star(x)
    first = g.bracket(phi1, sx, m0)
    inner = g.bracket(phi2, sx, m1)
    second = g.star(g.bracket(phi1, g.star(inner), m2))
    return fadd(first, fscale(second, Fraction(-1, 2)))


def e_op(g, x):
    F, B = g.F(), g.B()
    sx = g.star(x)
    first_C = g.bracket(F, sx, "C")

    def second(m1, m2):
        return g.star(g.bracket(F, g.star(g.bracket(B, sx, m1)), m2))

    return fadd(fscale(first_C, -2), fscale(second("C", "C"), -1), second("A", "A"))


def dress(phi, h, hinv):
    return {k: hinv @ v @ h for k, v in phi.items()}


MODES = {
    "CCC": ("F", "B", ("C", "C", "C")),
    "CAA": ("F", "B", ("C", "A", "A")),
    "CAC": ("F+F'", "B'", ("C", "A", "C")),
}


def phis(g, which):
    return {"F": g.F(), "B": g.B(), "F+F'": fadd(g.F(), g.Fp()), "B'": g.Bp()}[which]


def mode_op(g, mode, h=None, hinv=None):
    p1, p2, modes = MODES[mode]
    P1, P2 = phis(g, p1), phis(g, p2)
    if h is not None:
        P1, P2 = dress(P1, h, hinv), dress(P2, h, hinv)
    return lambda x: shiab(g, x, P1, P2, modes)


# --------------------------------------------------------------------------- curvature

def zero4():
    return np.array([Fraction(0)] * N ** 4, dtype=object).reshape((N,) * 4)


BIV = [(a, b) for a in range(N) for b in range(a + 1, N)]


def from_pairs(entries):
    """entries: {(P, Q): c} over bivector pairs; builds R with all algebraic symmetries but Bianchi."""
    R = zero4()
    for (P, Qp), c in entries.items():
        (a, b), (cc, d) = P, Qp
        for (x1, x2, s1) in ((a, b, 1), (b, a, -1)):
            for (y1, y2, s2) in ((cc, d, 1), (d, cc, -1)):
                R[x1, x2, y1, y2] += s1 * s2 * c
                if P != Qp:
                    R[y1, y2, x1, x2] += s1 * s2 * c
    return R


def curvature_basis():
    special = {((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))}
    basis = []
    for i, P in enumerate(BIV):
        for Qp in BIV[i:]:
            if (P, Qp) not in special:
                basis.append(from_pairs({(P, Qp): Fraction(1)}))
    basis.append(from_pairs({((0, 1), (2, 3)): Fraction(1), ((0, 2), (1, 3)): Fraction(1)}))
    basis.append(from_pairs({((0, 2), (1, 3)): Fraction(1), ((0, 3), (1, 2)): Fraction(1)}))
    for R in basis:
        assert is_algebraic(R)
    assert rref_rank([list(R.flat) for R in basis]) == 20
    return basis


def is_algebraic(R):
    for a, b, c, d in itertools.product(range(N), repeat=4):
        if R[a, b, c, d] != -R[b, a, c, d] or R[a, b, c, d] != -R[a, b, d, c]:
            return False
        if R[a, b, c, d] != R[c, d, a, b]:
            return False
        if R[a, b, c, d] + R[a, c, d, b] + R[a, d, b, c] != 0:
            return False
    return True


def ricci(g, R):
    Ric = np.array([Fraction(0)] * N * N, dtype=object).reshape(N, N)
    for b in range(N):
        for d in range(N):
            Ric[b, d] = sum(g.eta[a] * R[a, b, a, d] for a in range(N))
    return Ric


def scalar(g, Ric):
    return sum(g.eta[b] * Ric[b, b] for b in range(N))


def metric(g):
    m = np.array([Fraction(0)] * N * N, dtype=object).reshape(N, N)
    for a in range(N):
        m[a, a] = Fraction(g.eta[a])
    return m


def kn_gg(g):
    gm = metric(g)
    R = zero4()
    for a, b, c, d in itertools.product(range(N), repeat=4):
        R[a, b, c, d] = 2 * (gm[a, c] * gm[b, d] - gm[a, d] * gm[b, c])
    return R


def weyl(g, R):
    gm, Ric = metric(g), ricci(g, R)
    S = scalar(g, Ric)
    W = zero4()
    for a, b, c, d in itertools.product(range(N), repeat=4):
        W[a, b, c, d] = (R[a, b, c, d]
                         - Fraction(1, N - 2) * (gm[a, c] * Ric[b, d] - gm[a, d] * Ric[b, c]
                                                 - gm[b, c] * Ric[a, d] + gm[b, d] * Ric[a, c])
                         + S * Fraction(1, (N - 1) * (N - 2)) * (gm[a, c] * gm[b, d] - gm[a, d] * gm[b, c]))
    return W


def dot4(g, A, B):
    return sum(A[a, b, c, d] * B[a, b, c, d] * g.eta[a] * g.eta[b] * g.eta[c] * g.eta[d]
               for a, b, c, d in itertools.product(range(N), repeat=4))


def dot2(g, A, B):
    return sum(A[a, b] * B[a, b] * g.eta[a] * g.eta[b] for a in range(N) for b in range(N))


def levi(perm):
    if len(set(perm)) < N:
        return 0
    c = sum(1 for i in range(N) for j in range(i + 1, N) if perm[i] > perm[j])
    return -1 if c % 2 else 1


def dual_tensor(g, W):
    """(*W)_abcd = 1/2 eps_cd^{fg} W_abfg, eps_0123 = +1."""
    D = zero4()
    for a, b, c, d in itertools.product(range(N), repeat=4):
        D[a, b, c, d] = Fraction(1, 2) * sum(levi((c, d, f, h)) * g.eta[f] * g.eta[h] * W[a, b, f, h]
                                             for f in range(N) for h in range(N))
    return D


def dual_by_forms(g, W):
    """Hand-built dual, entry by entry: apply the pinned 2-form star to the last pair."""
    D = zero4()
    for a in range(N):
        for b in range(N):
            # 2-form omega = sum_{c<d} W_abcd e^{cd}; its components are omega_cd = W_abcd
            omega = {}
            for c in range(N):
                for d in range(c + 1, N):
                    if W[a, b, c, d] != 0:
                        omega[(1 << c) | (1 << d)] = W[a, b, c, d]
            for mask, val in omega.items():
                J = FULL ^ mask
                s = g.eta_mask(mask) * wsign(mask, J)
                c, d = bits(J)
                D[a, b, c, d] += s * val
                D[a, b, d, c] -= s * val
    return D


def invariants(g, R1, R2):
    W1, W2 = weyl(g, R1), weyl(g, R2)
    Ric1, Ric2 = ricci(g, R1), ricci(g, R2)
    S1, S2 = scalar(g, Ric1), scalar(g, Ric2)
    gm = metric(g)
    R01 = Ric1 - gm * (S1 / N)
    R02 = Ric2 - gm * (S2 / N)
    ww = dot4(g, W1, W2)
    wsw = Fraction(1, 2) * (dot4(g, W1, dual_tensor(g, W2)) + dot4(g, W2, dual_tensor(g, W1)))
    return [ww, wsw, dot2(g, R01, R02), S1 * S2]


# --------------------------------------------------------------------------- fits

def fit_bilinear(basis, inv_cache, bil):
    """Fit bil(i, j) -> (re, im) to the four invariants on all pairs i <= j."""
    A, bre, bim = [], [], []
    for i in range(len(basis)):
        for j in range(i, len(basis)):
            A.append(inv_cache[(i, j)])
            re, im = bil(i, j)
            bre.append(re)
            bim.append(im)
    return {"re": solve(A, bre), "im": solve(A, bim), "equations": len(A)}


def inv_table(g, basis):
    return {(i, j): invariants(g, basis[i], basis[j])
            for i in range(len(basis)) for j in range(i, len(basis))}


def q_fit(g, basis, inv_cache, X, prime=False):
    outs = [X(g.xi(R)) for R in basis]
    for o in outs:
        assert all(popcount(k) == N - 1 for k in o), "output is not a 3-form"
    return fit_bilinear(basis, inv_cache, lambda i, j: g.pair(outs[i], outs[j], prime))


def fmt(v):
    if v is None:
        return None
    return [str(x) for x in v]


# --------------------------------------------------------------------------- E1

def e1(p, qq, log):
    g = Geometry(p, qq)
    basis = curvature_basis()
    inv = inv_table(g, basis)
    out = {"signature": [p, qq]}

    # sanity of invariants: 4 columns independent on the basis
    assert rref_rank(list(inv.values())) == 4

    # ---- *W normalization control (hand-built dual)
    wbasis = weyl_basis(g, basis)
    norm_ok = True
    for W in wbasis:
        D1, D2 = dual_tensor(g, W), dual_by_forms(g, W)
        norm_ok &= all(x == y for x, y in zip(D1.flat, D2.flat))
        DD = dual_by_forms(g, D2)
        norm_ok &= all(x == -y for x, y in zip(DD.flat, W.flat))      # ** = -1 on Lorentzian 2-forms
        norm_ok &= dot4(g, W, DD) == -dot4(g, W, W)                    # W.*(*W) = -W.W
        norm_ok &= dot4(g, W, D2) == invariants(g, W, W)[1]            # W.D = W.*W
    nonzero_wsw = any(dot4(g, W1, dual_tensor(g, W2)) != 0 for W1 in wbasis for W2 in wbasis)
    out["dual_control"] = bool(norm_ok)
    out["dual_nonvacuous"] = bool(nonzero_wsw)

    # ---- operators
    ops = {
        "E_OP": lambda x: e_op(g, x),
        "CCC literal": mode_op(g, "CCC"),
        "CAA Einstein": mode_op(g, "CAA"),
        "CAC chiral": mode_op(g, "CAC"),
    }

    # ---- response checks against the B02 closed form / phase2 README (convention pinning)
    def expected(name, R):
        Ric = ricci(g, R)
        S = scalar(g, Ric)
        gm = metric(g)
        EF, EFp = g.E(Ric), g.E(Ric, True)
        EFg, EFpg = g.E(gm), g.E(gm, True)
        if name == "E_OP":
            return fadd(fscale(EF, 2), fscale(EFg, -S))
        if name == "CCC literal":
            return fscale(EF, -1)
        if name == "CAA Einstein":
            return fadd(fscale(EF, -1), fscale(EFg, S / 2))
        if name == "CAC chiral":
            return fadd(fscale(EF, -1), fscale(EFp, -1), fscale(EFg, S / 2), fscale(EFpg, S / 2))

    resp = {}
    for name, X in ops.items():
        ok = all(feq(g.star(X(g.xi(R))), expected(name, R)) for R in basis)
        resp[name] = ok
    out["response_matches_closed_form"] = resp

    # ---- quadratic-form fits
    out["Q"] = {"pinned": {}, "prime": {}}
    for name, X in ops.items():
        for conv in ("pinned", "prime"):
            f = q_fit(g, basis, inv, X, prime=(conv == "prime"))
            out["Q"][conv][name] = {"re": fmt(f["re"]), "im": fmt(f["im"])}
            out["equations"] = f["equations"]

    # ---- KN(g, g) direct control
    R = kn_gg(g)
    assert is_algebraic(R)
    Ric = ricci(g, R)
    S = scalar(g, Ric)
    gm = metric(g)
    W = weyl(g, R)
    y = e_op(g, g.xi(R))
    qv = g.pair(y, y)
    out["KN_gg"] = {
        "Ric_is_6g": all(Ric[a, b] == 6 * gm[a, b] for a in range(N) for b in range(N)),
        "S": str(S),
        "RicRic": str(dot2(g, Ric, Ric)),
        "W_zero": all(v == 0 for v in W.flat),
        "Q_EOP": [str(qv[0]), str(qv[1])],
        "Q_EOP_from_fit": None,
    }
    c = out["Q"]["pinned"]["E_OP"]["re"]
    if c is not None:
        R0 = Ric - gm * (S / N)
        fitv = qs(c[2]) * dot2(g, R0, R0) + qs(c[3]) * S * S
        out["KN_gg"]["Q_EOP_from_fit"] = str(fitv)

    # ---- response Gram
    def bmaps(R):
        Ric = ricci(g, R)
        S = scalar(g, Ric)
        gm = metric(g)
        return [g.star_inv(g.E(Ric)), g.star_inv(g.E(Ric, True)),
                g.star_inv(fscale(g.E(gm), S)), g.star_inv(fscale(g.E(gm, True), S))]

    bm = [bmaps(R) for R in basis]
    gram = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            def bil(r, s, i=i, j=j):
                x1 = g.pair(bm[r][i], bm[s][j])
                x2 = g.pair(bm[s][i], bm[r][j])
                return ((x1[0] + x2[0]) / 2, (x1[1] + x2[1]) / 2)
            f = fit_bilinear(basis, inv, bil)
            gram[i][j] = {"re": fmt(f["re"]), "im": fmt(f["im"])}
    out["response_gram"] = gram
    log(f"E1 {p},{qq} done")
    return out, g, basis


# --------------------------------------------------------------------------- E2

def weyl_basis(g, basis):
    ws, rows = [], []
    for R in basis:
        W = weyl(g, R)
        cand = rows + [list(W.flat)]
        if rref_rank(cand) > len(rows):
            rows, ws = cand, ws + [W]
    for W in ws:
        assert is_algebraic(W)
        Ric = ricci(g, W)
        assert all(v == 0 for v in Ric.flat)
    assert len(ws) == 10
    return ws


def cayley(g, m, extra=0):
    u = g.u(m, extra)
    assert g.in_uA(u)
    X = u.smul(Fraction(1, 2))
    one = g.one
    sq = u @ u
    s = None
    for cand in (1, -1):
        if sq == one.smul(cand):
            s = cand
    assert s is not None, "u_I^2 is not +-1"
    den = 1 - Fraction(s, 4)
    if den == 0:
        return None
    inv_1pX = (one - X).smul(1 / den)
    assert (one + X) @ inv_1pX == one
    h = (one - X) @ inv_1pX
    inv_1mX = (one + X).smul(1 / den)
    hinv = (one + X) @ inv_1mX
    assert h @ hinv == one
    return h, hinv


def centralizer_dim(g, h):
    rows = []
    for a in range(N):
        for b in range(a + 1, N):
            J = (g.G[a] @ g.G[b]).smul(Fraction(1, 2))
            rows.append((J @ h - h @ J).flat())
    return 6 - rref_rank(rows)


def grade_coeffs(g, M):
    """Coefficients of M in the blade basis: c_J = Tr(G_J^{-1} M) / 4."""
    out = {}
    for m in range(1 << N):
        Gm = g.blade[m]
        sq = Gm @ Gm
        s = 1 if sq == g.one else -1
        assert sq == g.one.smul(s)
        t = (Gm.smul(s) @ M).trace()
        if t != (0, 0):
            out[m] = (t[0] / DIM, t[1] / DIM)
    return out


def e2(g, basis, log, task_rows):
    p, qq = g.p, g.q
    wb = weyl_basis(g, basis)
    xiW = [g.xi(W) for W in wb]
    inv = inv_table(g, basis)
    out = {"signature": [p, qq], "weyl_dim": len(wb), "modes": {}, "blades": {}}

    # u(A) membership and phases
    out["phases"] = {m: g.phase[m] for m in range(1, 1 << N)}

    for m in range(1, 1 << N):
        cz = cayley(g, m)
        assert cz is not None
        h, hinv = cz
        inU = h.dagger() @ g.A @ h == g.A
        out["blades"][m] = {"grade": popcount(m), "in_U(A)": bool(inU), "centralizer": centralizer_dim(g, h)}

    for mode in MODES:
        und = mode_op(g, mode)
        und_rank = rref_rank([fflat(und(x), N - 1) for x in xiW])
        rows = []
        for m in range(1, 1 << N):
            h, hinv = cayley(g, m)

            def c_h(f):
                return fmap(f, lambda X: hinv @ X @ h)

            def c_hinv(f):
                return fmap(f, lambda X: h @ X @ hinv)

            ident = [c_h(und(c_hinv(x))) for x in xiW]
            direct_op = mode_op(g, mode, h, hinv)
            direct = [direct_op(x) for x in xiW]
            same = all(feq(a, b) for a, b in zip(ident, direct))
            cov = sum(0 if fzero(direct_op(c_h(x))) else 1 for x in xiW)
            leak = rref_rank([fflat(y, N - 1) for y in ident])
            f = q_fit(g, basis, inv, direct_op)
            rows.append({"blade": m, "grade": popcount(m), "leak_rank": leak,
                         "identity_route_equals_direct": same, "cov_defect": cov,
                         "dressed_Q": {"re": fmt(f["re"]), "im": fmt(f["im"])}})
        out["modes"][mode] = {"undressed_leak_rank": und_rank, "rows": rows}
        log(f"E2 {p},{qq} {mode} done")

    # leak ranks with the opposite phase sign (u -> -u, i.e. h -> h^{-1}) for the four named blades
    alt = {}
    for m in (1, 3, 7, 15):
        h, hinv = cayley(g, m, extra=2)
        und = mode_op(g, "CCC")
        ys = [fmap(und(fmap(x, lambda X: h @ X @ hinv)), lambda X: hinv @ X @ h) for x in xiW]
        alt[m] = rref_rank([fflat(y, N - 1) for y in ys])
    out["CCC_leak_opposite_phase"] = alt
    return out


def counterexample(g, basis):
    """CCC at (3,1), blade 0111 (= 7): zero dressed output, grade-3 parts in c_h^{-1} x."""
    G = g.blade
    x = {3: G[9].smul(-12), 9: G[3].smul(12), 6: G[12].smul(-12), 12: G[6].smul(12)}
    wb = weyl_basis(g, basis)
    xiW = [g.xi(W) for W in wb]
    r0 = rref_rank([fflat(y, 2) for y in xiW])
    r1 = rref_rank([fflat(y, 2) for y in xiW] + [fflat(x, 2)])
    res = {"in_xi_Weyl": r0 == r1 == 10}
    for label, extra in (("phase", 0), ("opposite_phase", 2)):
        h, hinv = cayley(g, 7, extra)
        op = mode_op(g, "CCC", h, hinv)
        y = op(x)
        cx = fmap(x, lambda X: h @ X @ hinv)  # c_h^{-1} x
        grades = {}
        for k, M in cx.items():
            for mm, c in grade_coeffs(g, M).items():
                grades.setdefault(popcount(mm), set()).add((k, mm))
        g3 = sorted(grades.get(3, set()))
        # undressed sanity: x is annihilated by CCC (P4) and c_h^{-1}x lies in ker CCC
        und = mode_op(g, "CCC")
        res[label] = {"dressed_output_zero": fzero(y),
                      "undressed_output_zero": fzero(und(x)),
                      "c_inv_x_in_ker": fzero(und(cx)),
                      "grade3_terms": len(g3),
                      "grades_present": sorted(grades),
                      "c_inv_x_in_xi_Weyl": rref_rank([fflat(v, 2) for v in xiW] + [fflat(cx, 2)]) == 10}
    return res


# --------------------------------------------------------------------------- comparison

def compare(e1s, e2s, cex):
    task = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = []

    def add(qty, mine, theirs):
        rows.append((qty, mine, theirs, mine == theirs))

    t_e1 = {tuple(e["signature"]): e for e in task["E1"]}
    for e in e1s:
        sig = tuple(e["signature"])
        te = t_e1[sig]
        for conv in ("pinned", "prime"):
            for name, v in e["Q"][conv].items():
                tv = te["Q"][conv][name]
                add(f"E1 {sig} Q[{conv}] {name} re", v["re"], tv["re"])
                add(f"E1 {sig} Q[{conv}] {name} im", v["im"], tv["im"])
        for i in range(4):
            for j in range(4):
                add(f"E1 {sig} response_gram[{i}][{j}]", e["response_gram"][i][j],
                    {"re": te["response_gram"][i][j]["re"], "im": te["response_gram"][i][j]["im"]})
        add(f"E1 {sig} basis_dim", 20, te["basis_dim"])
        add(f"E1 {sig} KN(g,g) Q(E_OP) (plan: -576)", e["KN_gg"]["Q_EOP"], ["-576", "0"])
        add(f"E1 {sig} KN(g,g) Ric.Ric (plan: 144)", e["KN_gg"]["RicRic"], "144")
        add(f"E1 {sig} KN(g,g) Ric=6g (plan)", e["KN_gg"]["Ric_is_6g"], True)
        add(f"E1 {sig} KN(g,g) W=0 (plan)", e["KN_gg"]["W_zero"], True)
        add(f"E1 {sig} KN(g,g) Q(E_OP) via fit (plan: -576)", e["KN_gg"]["Q_EOP_from_fit"], "-576")
        add(f"E1 {sig} *W normalization control (derivations E1.2)", e["dual_control"], True)
        add(f"E1 {sig} W.*W nonzero on Weyl basis (non-vacuity)", e["dual_nonvacuous"], True)
        for name, ok in e["response_matches_closed_form"].items():
            add(f"E1 {sig} response of {name} = documented closed form", ok, True)

    t_e2 = {tuple(e["signature"]): e for e in task["E2"]}
    plan_stab = {1: 3, 2: 2, 3: 3, 4: 6}
    for e in e2s:
        sig = tuple(e["signature"])
        te = t_e2[sig]
        add(f"E2 {sig} weyl_dim", e["weyl_dim"], te["weyl_dim"])
        for m, b in e["blades"].items():
            trow = next(r for r in te["modes"]["CCC"]["rows"] if r["blade"] == m)
            add(f"E2 {sig} blade {m:04b} centralizer dim vs stabilizer (CCC)", b["centralizer"], trow["residual"])
            add(f"E2 {sig} blade {m:04b} h in U(A)", b["in_U(A)"], True)
            for mode in ("CAA", "CAC"):
                tr = next(r for r in te["modes"][mode]["rows"] if r["blade"] == m)
                add(f"E2 {sig} blade {m:04b} centralizer dim vs stabilizer ({mode})", b["centralizer"], tr["residual"])
            add(f"E2 {sig} blade {m:04b} centralizer vs plan grade table", b["centralizer"], plan_stab[b["grade"]])
        for mode, mv in e["modes"].items():
            tm = te["modes"][mode]
            add(f"E2 {sig} {mode} undressed leak rank", mv["undressed_leak_rank"], tm["undressed_leak_rank"])
            for r in mv["rows"]:
                tr = next(x for x in tm["rows"] if x["blade"] == r["blade"])
                tag = f"E2 {sig} {mode} blade {r['blade']:04b}"
                add(f"{tag} leak rank (identity route)", r["leak_rank"], tr["leak_rank"])
                add(f"{tag} identity route = direct dressed operator", r["identity_route_equals_direct"], True)
                add(f"{tag} covariance defect", r["cov_defect"], tr["cov_defect"])
                add(f"{tag} dressed Q re", r["dressed_Q"]["re"], tr["dressed_Q"]["re"])
                add(f"{tag} dressed Q im", r["dressed_Q"]["im"], tr["dressed_Q"]["im"])
        for m, rk in e["CCC_leak_opposite_phase"].items():
            tr = next(x for x in te["modes"]["CCC"]["rows"] if x["blade"] == m)
            add(f"E2 {sig} CCC blade {m:04b} leak rank with opposite u_I sign (h -> h^-1)", rk, tr["leak_rank"])

    add("P4 counterexample: x in xi(Weyl)", cex["in_xi_Weyl"], True)
    c = cex["phase"]
    add("P4 counterexample: dressed CCC output zero (blade 0111, (3,1))", c["dressed_output_zero"], True)
    add("P4 counterexample: c_h^-1 x has grade-3 parts", c["grade3_terms"] > 0, True)
    add("P4 counterexample: c_h^-1 x not in xi(Weyl)", c["c_inv_x_in_xi_Weyl"], False)
    add("P4 counterexample: undressed CCC kills x (P4)", c["undressed_output_zero"], True)
    return rows


def main():
    t0 = time.time()

    def log(msg):
        print(f"[{time.time() - t0:7.1f}s] {msg}", flush=True)

    e1s, e2s = [], []
    cex = None
    for p, qq in ((3, 1), (1, 3)):
        e, g, basis = e1(p, qq, log)
        e1s.append(e)
        e2s.append(e2(g, basis, log, None))
        if (p, qq) == (3, 1):
            cex = counterexample(g, basis)
            log("counterexample done")
    rows = compare(e1s, e2s, cex)
    print()
    print("| quantity | rederived | Task 2/3 or plan value | agree |")
    print("|---|---|---|---|")
    for qty, mine, theirs, ok in rows:
        print(f"| {qty} | {json.dumps(mine, default=str)} | {json.dumps(theirs, default=str)} | {'agree' if ok else 'DISAGREE'} |")
    bad = [r for r in rows if not r[3]]
    print()
    print(f"comparisons: {len(rows)}, disagreements: {len(bad)}")
    for qty, mine, theirs, _ in bad:
        print(f"FINDING: {qty}: rederived {json.dumps(mine, default=str)} vs {json.dumps(theirs, default=str)}")
    print()
    print("extra detail:")
    print(json.dumps({"counterexample": cex,
                      "phases": {str(tuple(e['signature'])): e["phases"] for e in e2s},
                      "E1": [{k: v for k, v in e.items() if k in ("signature", "KN_gg", "response_matches_closed_form",
                                                                   "dual_control", "equations")} for e in e1s]},
                     default=str, indent=1))
    print(f"runtime {time.time() - t0:.1f} s")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
