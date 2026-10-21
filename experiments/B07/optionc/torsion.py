"""B07 option C, Q2: pointwise Lorentz-valued curvature values that are not algebraic (design rev 3.1, §4 Q2).

Domain: R in Lambda^2 (x) Lambda^2 (36-dim), coordinates R_abcd at a < b, c < d, fed to gu.shiab.xi
    xi(R) = 1/2 sum_{a<b, c<d} R_abcd eta_c eta_d e^{ab} (x) G_c G_d      (no pair symmetry used).
Split 36 = 20 + 1 + 15 by P20 = (I + tau)/2 - Alt, P1 = Alt, P15 = (I - tau)/2 (tau swaps the pairs).
Output value spaces (after *, as 1-forms): E = {E_F(H) + E_F'(K): H, K symmetric} (20-dim, B02's value space) and
E^a = {... : H, K antisymmetric} (12-dim); by Schur the 15-part lands in E + E^a and the 1-part in span{E_F(g), E_F'(g)}.
"""
from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np
from flint import fmpq_mat

from gu.cliffform import bracket, star
from gu.shiab import embed_tensor, phi_basis, xi
from experiments.B07.escape.quadratic import curvature_basis
from experiments.B07.optionc.sector import fq, is_zero, mat
from experiments.B07.phase2 import universal as U

N4 = 4
PAIRS = list(itertools.combinations(range(N4), 2))
COORDS = [(P, Q) for P in PAIRS for Q in PAIRS]


def tensor(v: list[Fraction]) -> np.ndarray:
    R = np.full((N4,) * 4, Fraction(0), dtype=object)
    for ((a, b), (c, d)), x in zip(COORDS, v):
        R[a, b, c, d], R[b, a, c, d], R[a, b, d, c], R[b, a, d, c] = x, -x, -x, x
    return R


def coords(R: np.ndarray) -> list[Fraction]:
    return [Fraction(R[a, b, c, d]) if isinstance(R[a, b, c, d], Fraction) else Fraction(int(R[a, b, c, d]))
            for (a, b), (c, d) in COORDS]


def _perm_sign(p: tuple) -> int:
    s = 1
    for i, j in itertools.combinations(range(len(p)), 2):
        if p[i] > p[j]:
            s = -s
    return s


def tau(R: np.ndarray) -> np.ndarray:
    return R.transpose(2, 3, 0, 1)


def alt(R: np.ndarray) -> np.ndarray:
    out = np.full(R.shape, Fraction(0), dtype=object)
    for p in itertools.permutations(range(4)):
        out = out + R.transpose(p) * _perm_sign(p)
    return out / 24


def projectors() -> dict[str, fmpq_mat]:
    """36 x 36 matrices (columns = images of the coordinate basis vectors)."""
    cols = {"P20": [], "P1": [], "P15": []}
    for i in range(len(COORDS)):
        R = tensor([Fraction(int(i == j)) for j in range(len(COORDS))])
        t, a = tau(R), alt(R)
        cols["P15"].append(coords((R - t) / 2))
        cols["P1"].append(coords(a))
        cols["P20"].append(coords((R + t) / 2 - a))
    return {k: mat([[c[r] for c in v] for r in range(len(COORDS))]) for k, v in cols.items()}


def projector_controls(P: dict, p: int, q: int) -> dict:
    I = mat([[Fraction(int(i == j)) for j in range(36)] for i in range(36)])
    names = list(P)
    lam = [mat(L) for L in U.rho(p, q, 1, 0, U.phases(p, q))]     # covector action on every slot
    act = [lorentz_on_coords(L) for L in lam]
    curv = mat([[c[r] for c in [coords(R) for R in curvature_basis(N4)]] for r in range(36)])
    return {"idempotent": all(P[k] * P[k] == P[k] for k in names),
            "mutually_annihilating": all(is_zero(P[a] * P[b]) for a in names for b in names if a != b),
            "sum_identity": P["P20"] + P["P1"] + P["P15"] == I,
            "ranks": {k: P[k].rank() for k in names},
            "equivariant": all(P[k] * J == J * P[k] for k in names for J in act),
            "algebraic_part_is_curvature_span": curv.rank() == 20 and P["P20"] * curv == curv}


def lorentz_on_coords(L: fmpq_mat) -> fmpq_mat:
    """The derivation action of a 4x4 covector generator L on all four slots, in the 36 coordinates."""
    Ln = np.array([[Fraction(int(L[i, j].p), int(L[i, j].q)) for j in range(4)] for i in range(4)], dtype=object)
    cols = []
    for i in range(len(COORDS)):
        R = tensor([Fraction(int(i == j)) for j in range(len(COORDS))])
        out = np.full(R.shape, Fraction(0), dtype=object)
        for slot in range(4):
            out = out + np.moveaxis(np.tensordot(Ln, R, axes=([1], [slot])), 0, slot)
        cols.append(coords(out))
    return mat([[c[r] for c in cols] for r in range(36)])


def vec1(x: dict, sec) -> list[Fraction]:
    """Phased coordinates of a u(A)-valued 1-form in sec.B1 order (raises if not u(A)-valued)."""
    c = U.to_phased(x, sec.ph) if x else {}
    out = [Fraction(0)] * len(sec.B1)
    for k, v in c.items():
        out[sec.i1[k]] = v
    return out


def value_spaces(sec) -> dict[str, list[list[Fraction]]]:
    n, p, q = sec.n, sec.p, sec.q
    sym = [np.array([[int((i, j) in ((a, b), (b, a))) for j in range(n)] for i in range(n)])
           for a in range(n) for b in range(a, n)]
    asym = [np.array([[(i, j) == (a, b) and 1 or ((i, j) == (b, a) and -1 or 0) for j in range(n)] for i in range(n)])
            for a, b in itertools.combinations(range(n), 2)]
    E = [vec1(embed_tensor(H, al, be, p, q), sec) for H in sym for al, be in ((1, 0), (0, 1))]
    Ea = [vec1(embed_tensor(H, al, be, p, q), sec) for H in asym for al, be in ((1, 0), (0, 1))]
    g = np.diag(sec.eta)
    return {"E": E, "Ea": Ea, "g": [vec1(embed_tensor(g, 1, 0, p, q), sec), vec1(embed_tensor(g, 0, 1, p, q), sec)]}


def rank_of(vs: list[list[Fraction]]) -> int:
    vs = [v for v in vs if any(v)]
    return mat([[v[i] for v in vs] for i in range(len(vs[0]))]).rank() if vs else 0


def response(sec, R: np.ndarray) -> list[Fraction]:
    return vec1(star(sec.X(xi(R, sec.eta)), sec.eta), sec)


def ccc_inner(sec, R: np.ndarray) -> dict:
    """The CCC inner term: *[B ^ *xi(R)]_C (gu.shiab.shiab_parts' inner['C'] with Phi2 = B), before the outer bracket."""
    return star(bracket(phi_basis(sec.p, sec.q)["B"], star(xi(R, sec.eta), sec.eta), "C", sec.eta), sec.eta)


def q2(sec, P: dict, is_ccc: bool) -> dict:
    """Q2 measurements and the Schur controls for one operator."""
    vs = value_spaces(sec)
    E, Ea, g = vs["E"], vs["Ea"], vs["g"]
    basis15 = [tensor([Fraction(int(P["P15"][r, j].p), int(P["P15"][r, j].q)) for r in range(36)]) for j in range(36)]
    img15 = [response(sec, R) for R in basis15]
    r15, rE, rEa = rank_of(img15), rank_of(E), rank_of(Ea)
    in_E = r15 + rE - rank_of(img15 + E)
    in_Ea = r15 + rEa - rank_of(img15 + Ea)
    R1 = tensor(coords(alt(tensor([Fraction(int(j == COORDS.index(((0, 1), (2, 3))))) for j in range(36)]))))
    y1 = response(sec, R1)
    sol = _solve2(g, y1)
    out = {"rank_15": r15, "dim_15_in_E": in_E, "dim_15_in_Ea": in_Ea,
           "controls": {"dims_E_Ea": [rE, rEa, rank_of(E + Ea)], "schur_15_in_E_plus_Ea":
                        rank_of(img15 + E + Ea) == rank_of(E + Ea), "intersections_sum_to_rank": in_E + in_Ea == r15,
                        "schur_1_in_span_g": sol is not None},
           "one_part": {"rank": int(any(y1)), "coefficients_EF_g_EFprime_g": [str(x) for x in sol] if sol else None}}
    if is_ccc:
        alg = [ccc_inner(sec, R) for R in curvature_basis(N4)]
        inner15 = [vec0(ccc_inner(sec, R), sec) for R in basis15]
        out["ccc_inner_rank_15"] = rank_of(inner15)
        out["controls"]["ccc_inner_zero_on_20_and_1"] = not any(alg) and not ccc_inner(sec, R1)
    return out


def vec0(x: dict, sec) -> list[Fraction]:
    c = U.to_phased(x, sec.ph) if x else {}
    out = [Fraction(0)] * (1 << sec.n)
    for (f, b), v in c.items():
        assert f == 0
        out[b] = v
    return out


def _solve2(g: list[list[Fraction]], y: list[Fraction]):
    """(alpha, beta) with y = alpha g0 + beta g1, or None."""
    import sympy as sp
    M = sp.Matrix([[sp.Rational(g[0][i]), sp.Rational(g[1][i])] for i in range(len(y))])
    try:
        sol, params = M.gauss_jordan_solve(sp.Matrix([sp.Rational(v) for v in y]))
    except ValueError:
        return None
    if params.shape[0]:
        raise AssertionError("E_F(g), E_F'(g) dependent")
    return [Fraction(str(x)) for x in sol]


def hand_xi_entry(p: int, q: int) -> bool:
    """Control 6 (hand xi entry): the off-algebraic R with R_1203 = 1 (pair (1,2) then pair (0,3)) gives exactly
    xi(R) = (1/2) eta_0 eta_3 e^{12} (x) G_0 G_3 = -(1/2) e^{12} (x) G_0 G_3 at (3,1) and (1,3) (eta_0 eta_3 = -1)."""
    from experiments.B07 import variation as V
    from gu.cliffform import GQ
    R = tensor([Fraction(int(c == ((1, 2), (0, 3)))) for c in COORDS])
    return xi(R, V.eta_of(p, q)) == {((1 << 1) | (1 << 2), (1 << 0) | (1 << 3)): GQ(Fraction(-1, 2))}
