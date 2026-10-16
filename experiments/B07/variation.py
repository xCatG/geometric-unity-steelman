"""B07: the first variation of GU (9.4) in the varpi direction, order by order in the augmented torsion T.

Reading V (pre-registered in experiments/B07/transcription.md): with eps, the metric and hence B, *, Phi fixed,
    I1 = int Tr(T ^ X(F_B + 1/2 d_B T + 1/3 b(T, T))) + (kappa/2) int Tr(T ^ *T),
and (9.7) claims d/ds I1(varpi + s alpha) = int Tr(alpha ^ X(F_A)) + kappa int Tr(alpha ^ *T), F_A = F_B + d_B T + T^T.
X is a member of the Shiab family (9.3) (gu.shiab), an ad-valued map Omega^2 -> Omega^(n-1).
b is the draft's [ , ] on ad-valued 1-forms: N1  b(x, y) = 1/2 [x ^ y]  (so b(T,T) = T^T),
                                         N2  b(x, y) = [x ^ y]        (so b(T,T) = 2 T^T).
Order T^0 holds identically. Order T^1 (flat B = d, eps = 1) reduces to the symbol condition C1; order T^2 to C2:
    C1(k; t, a) = Tr(t ^ X(e^k ^ a)) + Tr(a ^ X(e^k ^ t))                         = 0 for all k, t, a;
    C2(alpha; T) = 1/3 Tr(alpha ^ X(b(T,T))) + 2/3 Tr(T ^ X(b(alpha,T))) - Tr(alpha ^ X(T^T)) = 0 for all alpha, T.
Tr is represented by the scalar (blade 0) coefficient of the Clifford factor of the top form. For even n this is
Tr / 2^(n/2) on the irreducible spinor module (every nonscalar blade is traceless); for the n = 3 controls it is the
canonical scalar Clifford trace. The conditions are homogeneous, so the factor is irrelevant. All arithmetic is exact.
"""
from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp

from gu.cliffform import GQ, blade_mul, bracket, plus, reorder_sign, scale
from gu.shiab import eta_of, phi_basis, shiab_parts

MODES = tuple("".join(m) for m in itertools.product("CA", repeat=3))
NORMS = ("N1", "N2")
COLUMNS = (("F",), ("F", "B"), ("F", "B'"), ("F'",), ("F'", "B"), ("F'", "B'"))
# shiab = first[m0](Phi1) - 1/2 second[m1 m2](Phi1, Phi2) with Phi1 = alpha F + beta F', Phi2 = gamma B + delta B'.
MONOMIALS = {("F",): "alpha", ("F", "B"): "-alpha*gamma/2", ("F", "B'"): "-alpha*delta/2",
             ("F'",): "beta", ("F'", "B"): "-beta*gamma/2", ("F'", "B'"): "-beta*delta/2"}


def wedge_prod(x: dict, y: dict, eta: list[int]) -> dict:
    """x ^ y with the Clifford factors multiplied (x's factor on the left)."""
    out: dict = {}
    for (f, a), u in x.items():
        for (g, b), v in y.items():
            if f & g:
                continue
            c, z = blade_mul(a, b, eta)
            k = (f | g, c)
            w = out.get(k, GQ()) + u * v * (reorder_sign(f, g) * z)
            if w:
                out[k] = w
            else:
                out.pop(k, None)
    return out


def pair(x: dict, y: dict, eta: list[int]) -> GQ:
    """Tr(x ^ y) / 2^(n/2): the scalar coefficient of the top-form part of x ^ y."""
    full = (1 << len(eta)) - 1
    return wedge_prod(x, y, eta).get((full, 0), GQ())


def b_bracket(x: dict, y: dict, norm: str, eta: list[int]) -> dict:
    """The draft's [x, y] on ad-valued 1-forms under normalization N1 (= 1/2 [x ^ y]) or N2 (= [x ^ y])."""
    if norm not in NORMS:
        raise ValueError("norm must be N1 or N2")
    full = bracket(x, y, "C", eta)
    return scale(full, Fraction(1, 2)) if norm == "N1" else full


def one_forms(n: int) -> list[dict]:
    return [{(1 << i, A): GQ(1)} for i in range(n) for A in range(1 << n)]


def shiab_column(col: tuple, mode: str, p: int, q: int):
    """The linear map Omega^2 -> Omega^(n-1) of one column of the Shiab family, for bracket string `mode`."""
    eta, ph = eta_of(p, q), phi_basis(p, q)
    if len(col) == 1:
        return lambda x: shiab_parts(ph[col[0]], ph["B"], x, eta)["first"][mode[0]]
    return lambda x: shiab_parts(ph[col[0]], ph[col[1]], x, eta)["second"][mode[1:]]


class Linear:
    """A linear map on 2-forms, memoized on basis elements (form mask, blade)."""

    def __init__(self, X):
        self.X, self.memo = X, {}

    def __call__(self, x: dict) -> dict:
        out: dict = {}
        for k, v in x.items():
            if k not in self.memo:
                self.memo[k] = self.X({k: GQ(1)})
            out = plus(out, scale(self.memo[k], v))
        return out


def c1_residual(X, n: int, eta: list[int]) -> dict:
    """{(k, i, j): C1} over basis covectors k and basis ad-valued 1-forms i <= j (C1 is symmetric in t, a)."""
    X, basis = Linear(X), one_forms(n)
    out = {}
    for k in range(n):
        ek = {(1 << k, 0): GQ(1)}
        S = [X(wedge_prod(ek, a, eta)) for a in basis]
        for i, t in enumerate(basis):
            for j in range(i, len(basis)):
                v = pair(t, S[j], eta) + pair(basis[j], S[i], eta)
                if v:
                    out[(k, i, j)] = v
    return out


def c2_value(X, alpha: dict, T: dict, norm: str, eta: list[int]) -> GQ:
    """C2(alpha; T) for one alpha and one T (cubic in nothing: quadratic in T, linear in alpha)."""
    first = pair(alpha, X(b_bracket(T, T, norm, eta)), eta) * GQ(Fraction(1, 3))
    second = pair(T, X(b_bracket(alpha, T, norm, eta)), eta) * GQ(Fraction(2, 3))
    expected = pair(alpha, X(wedge_prod(T, T, eta)), eta)
    return first + second - expected


def c2_residual(X, n: int, eta: list[int], norm: str) -> dict:
    """{(a, i, j): polarized C2} over basis alpha = a and T = t_i + t_j (i <= j), minus the diagonal parts."""
    X, basis = Linear(X), one_forms(n)
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


def _sym(v: GQ):
    return sp.Rational(v.re) + sp.I * sp.Rational(v.im)


def kernel(columns: dict) -> list[list]:
    """Exact nullspace of the residual columns {name: {entry: GQ}}: coefficient vectors that make the residual vanish."""
    keys = sorted(set().union(*[c.keys() for c in columns.values()]))
    names = list(columns)
    if not keys:
        return [[1 if m == i else 0 for m in range(len(names))] for i in range(len(names))]
    M = sp.Matrix([[_sym(columns[nm].get(k, GQ())) for nm in names] for k in keys])
    return [list(v) for v in M.nullspace()]


def survey(p: int, q: int, mode: str, norm: str = "N1", with_c2: bool = True) -> dict:
    """C1 (and C2) residual columns of the six Shiab-family monomials for one bracket mode, and their kernels."""
    eta, n = eta_of(p, q), p + q
    c1 = {col: c1_residual(shiab_column(col, mode, p, q), n, eta) for col in COLUMNS}
    out = {"signature": [p, q], "mode": mode, "columns": [list(c) for c in COLUMNS],
           "c1_nonzero": {"+".join(c): len(v) for c, v in c1.items()},
           "c1_kernel": [[str(x) for x in v] for v in kernel(c1)]}
    if with_c2:
        c2 = {col: c2_residual(shiab_column(col, mode, p, q), n, eta, norm) for col in COLUMNS}
        both = {col: {**{("c1",) + k: v for k, v in c1[col].items()}, **{("c2",) + k: v for k, v in c2[col].items()}}
                for col in COLUMNS}
        out.update({"norm": norm, "c2_nonzero": {"+".join(c): len(v) for c, v in c2.items()},
                    "c2_kernel": [[str(x) for x in v] for v in kernel(c2)],
                    "joint_kernel": [[str(x) for x in v] for v in kernel(both)]})
    return out


BRANCHES = {  # named Shiab members: (mode, {column: coefficient}); B02's headline readings (experiments/B02/README.md)
    "CCC literal, Phi1=F, Phi2=B": ("CCC", {("F",): 1, ("F", "B"): Fraction(-1, 2)}),
    "CAA Einstein, Phi1=F, gamma=1, delta=0": ("CAA", {("F",): 1, ("F", "B"): Fraction(-1, 2)}),
    "CAC chiral, Phi1=F+F', delta=1, gamma=0": ("CAC", {("F",): 1, ("F'",): 1, ("F", "B'"): Fraction(-1, 2),
                                                         ("F'", "B'"): Fraction(-1, 2)}),
}


def branch_map(name: str, p: int, q: int):
    mode, coeffs = BRANCHES[name]
    cols = {c: shiab_column(c, mode, p, q) for c in coeffs}
    return lambda x: plus(*[scale(cols[c](x), v) for c, v in coeffs.items()])


def c1_entry(X, k: int, t: dict, a: dict, eta: list[int]) -> GQ:
    ek = {(1 << k, 0): GQ(1)}
    return pair(t, X(wedge_prod(ek, a, eta)), eta) + pair(a, X(wedge_prod(ek, t, eta)), eta)


def c1_witness(name: str, p: int, q: int, max_k: int = 2, max_form: int = 4) -> dict | None:
    """First (k, t, a) with nonzero C1 for a named branch: t = e^i (x) G_A with |A| <= 1, a = e^j (x) G_B with |B| <= 2,
    over small indices first (k < max_k, i, j < max_form; blade indices < max_form + 1).

    Scope: counterexample (one exact nonzero entry), or None if this bounded search finds none.
    """
    eta, n = eta_of(p, q), p + q
    X = Linear(branch_map(name, p, q))
    r = range(min(n, max_form + 1))
    ta = [0] + [1 << i for i in r]
    ab = [0] + [1 << i for i in r] + [(1 << i) | (1 << j) for i, j in itertools.combinations(r, 2)]
    for k in range(min(n, max_k)):
        for i in range(min(n, max_form)):
            for j in range(min(n, max_form)):
                for A in ta:
                    for Bb in ab:
                        t, a = {(1 << i, A): GQ(1)}, {(1 << j, Bb): GQ(1)}
                        v = c1_entry(X, k, t, a, eta)
                        if v:
                            return {"branch": name, "signature": [p, q], "k": k, "t": [i, A], "a": [j, Bb],
                                    "value": [str(v.re), str(v.im)]}
    return None
