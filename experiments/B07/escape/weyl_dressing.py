"""E2: the Weyl response of the dressed Shiab operator Shiab_eps (B02 test 5', made exact) at a 4D point.

Shiab_eps is (9.3) with Phi^i -> eps^-1 Phi^i eps (`gu.shiab.shiab_dressed`). The dressing family is the Cayley
transform h = (1 - X)(1 + X)^-1 of X = (1/2) u_I for every blade I != 0, where u_I is the u(A) generator on blade I
(G_I or i G_I by `universal.phases`). Grade-2 blades give elements of the Spin image; every other grade does not.
For each mode (CCC, CAA with Phi = F, B; CAC with Phi1 = F + F', Phi2 = B') and each eps, record:
  leak_rank   - rank of W -> *Shiab_eps(xi W) on a basis of the 10-dimensional Weyl space (undressed: 0);
  cov_defect  - number of Weyl basis inputs with Shiab_eps(c_eps xi W) != c_eps Shiab(xi W), c_eps x = eps^-1 x eps
                (B02 proofs.md identity at eps = 1, h = eps; expected 0 for every eps);
  dressed_Q   - Q of the dressed operator fitted to the invariants (`quadratic.bilinear_fit`), or None if not in span;
  residual    - dimension of {L in spin(p,q) : rho(L) Shiab_eps = Shiab_eps rho(L) on xi(algebraic curvature)}.
Every member is checked to lie in U(A) (h^t A h = A) before the survey; skipped (singular) blades are recorded.
Identity scope on the stated finite family and bases; not a search over U(A).
"""
from __future__ import annotations

import itertools

from fractions import Fraction

from flint import fmpq, fmpq_mat

from gu.adjoint import from_mono, is_in_group
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import blade_to_mono

from gu.cliffform import GQ, I, plus, scale, star
from gu.curvature import decompose
from gu.shiab import cayley_blade, eta_of, generator_action, left, phi_basis, right, shiab, shiab_dressed, xi
from experiments.B07.escape import quadratic as Q
from experiments.B07.phase2 import universal as U

MODES = ("CCC", "CAA", "CAC")


def phis_for(mode: str, p: int, q: int) -> tuple[dict, dict]:
    ph = phi_basis(p, q)
    if mode == "CAC":
        return plus(ph["F"], ph["F'"]), ph["B'"]
    return ph["F"], ph["B"]


def rank(vecs: list[dict]) -> int:
    """Exact real rank of GQ-valued vectors (real and imaginary parts as separate rows)."""
    keys = sorted({k for v in vecs for k in v})
    if not keys:
        return 0
    ix = {k: i for i, k in enumerate(keys)}
    M = fmpq_mat(2 * len(keys), len(vecs))
    for j, v in enumerate(vecs):
        for k, x in v.items():
            M[ix[k], j] = fmpq(x.re.numerator, x.re.denominator)
            M[len(keys) + ix[k], j] = fmpq(x.im.numerator, x.im.denominator)
    return M.rank()


def weyl_basis(p: int, q: int) -> list:
    """xi of an independent set of Weyl tensors (denominator * W, integer), from the curvature basis."""
    eta = eta_of(p, q)
    Ws = [decompose(R, eta).weyl for R in Q.curvature_basis(p + q)]
    Ws = [W for W in Ws if W.any()]
    return [xi(Ws[i], eta) for i in Q.independent(Ws)]


def family_report(p: int, q: int, t: Fraction = Fraction(1, 2)) -> dict:
    """{"members": [(blade, grade, eps, eps_inv)], "attempted": [...], "skipped": [...]} for X = t u_blade.

    A blade is skipped (and listed) when 1 + X is singular. t must be exact."""
    eta, ph = eta_of(p, q), U.phases(p, q)
    t = Q._q(t)
    members, attempted, skipped = [], [], []
    for blade in range(1, 1 << (p + q)):
        attempted.append(blade)
        try:
            e, ei = cayley_blade(blade, GQ(t) * (I if ph[blade] else GQ(1)), eta)
        except ZeroDivisionError:
            skipped.append(blade)
            continue
        members.append((blade, blade.bit_count(), e, ei))
    return {"members": members, "attempted": attempted, "skipped": skipped}


def family(p: int, q: int) -> list[tuple[int, int, dict, dict]]:
    """The members of family_report at t = 1/2."""
    return family_report(p, q)["members"]


def as_matrix(x: dict, p: int, q: int) -> fmpq_mat:
    """The real embedded matrix of a 0-form Clifford element {(0, blade): GQ} (gu.adjoint conventions)."""
    gs = gammas(p, q)
    M = None
    for (f, c), v in x.items():
        if f:
            raise ValueError("0-form expected")
        for coeff, ipow in ((v.re, 0), (v.im, 1)):
            if coeff:
                term = from_mono(blade_to_mono(c, gs).times_i_power(ipow)) * fmpq(coeff.numerator, coeff.denominator)
                M = term if M is None else M + term
    return M


def in_group(e: dict, p: int, q: int) -> bool:
    """h^t A h = A for the Dirac pairing A (gu.adjoint.is_in_group)."""
    return is_in_group(as_matrix(e, p, q), from_mono(dirac_pairing(p, q)))


def conj(x: dict, e: dict, ei: dict, eta: list[int]) -> dict:
    return left(ei, right(x, e, eta), eta)


def survey_one(mode: str, p: int, q: int, e: dict, ei: dict, weyl: list, curv: list) -> dict:
    eta, n = eta_of(p, q), p + q
    P1, P2 = phis_for(mode, p, q)
    S = lambda x: shiab_dressed(P1, P2, x, mode, eta, e, ei)
    leak = rank([v for v in (star(S(x), eta) for x in weyl) if v])
    defect = sum(1 for x in weyl
                 if plus(S(conj(x, e, ei, eta)), scale(conj(shiab(P1, P2, x, mode, eta), e, ei, eta), -1)))
    cols = []
    for a, b in itertools.combinations(range(n), 2):
        col = {}
        for j, x in enumerate(curv):
            d = plus(generator_action(S(x), a, b, eta), scale(S(generator_action(x, a, b, eta)), -1))
            col.update({(j,) + k: v for k, v in d.items()})
        cols.append(col)
    dq = Q.bilinear_fit(lambda R: S(xi(R, eta)), lambda R: S(xi(R, eta)), p, q)
    return {"leak_rank": leak, "cov_defect": defect, "residual": len(cols) - rank(cols), "dressed_Q": dq}


def survey(p: int, q: int, modes=MODES) -> dict:
    eta = eta_of(p, q)
    weyl = weyl_basis(p, q)
    curv = [xi(R, eta) for R in Q.curvature_basis(p + q)]
    rep = family_report(p, q)
    outside = [b for b, _, e, _ in rep["members"] if not in_group(e, p, q)]
    if outside:
        raise AssertionError(f"dressings not in U(A): blades {outside}")
    out = {"signature": [p, q], "weyl_dim": rank(weyl), "modes": {},
           "family": {"t": "1/2", "attempted": len(rep["attempted"]), "accepted": len(rep["members"]),
                      "skipped": rep["skipped"]}}
    for mode in modes:
        P1, P2 = phis_for(mode, p, q)
        rows = [{"blade": blade, "grade": g, **survey_one(mode, p, q, e, ei, weyl, curv)}
                for blade, g, e, ei in rep["members"]]
        out["modes"][mode] = {"undressed_leak_rank": rank([v for v in (shiab(P1, P2, x, mode, eta) for x in weyl) if v]),
                              "rows": rows}
    return out
