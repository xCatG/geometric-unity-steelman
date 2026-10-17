"""E2 at 14D: bounded Weyl-leak witnesses for the dressed Shiab operator at (7,7) and (9,5).

Scope: counterexample. Per signature, two Ricci-flat algebraic-curvature inputs: B02's `weyl_control` (axes 0-3)
and the same construction on the Lorentzian 4-plane (0, 1, 2, p), of signature (3,1). Each is dressed by the Cayley transform
h = (1 - X)(1 + X)^-1, X = t u_I (t = 1/2 exact), for eight named blades I: the in-plane vector a0, the six in-plane
bivectors a_i a_j (on the Lorentzian plane, those with a3 = p are boosts) and one bivector on the first two axes outside
the plane. For each (input, blade, mode) record:
  in_u_a         - h^t A h = A for the Dirac pairing A (gu.adjoint.is_in_group);
  spin0          - bivectors only: h = a + b G_I with a > 0 and a^2 - s b^2 = 1, s = G_I^2: the coefficient form of
                   derivations E2.3, whose Spin_0 proof holds for a simple bivector in any dimension (None for the vector);
  commutes       - h^-1 (xi W) h == xi W;
  transport_in_weyl - c_h^-1 xi W = h (xi W) h^-1 is xi of an algebraic, Ricci-flat tensor (then the dressed output is 0
                   by the sufficient direction of derivations E2.5);
  undressed_zero - Shiab(xi W) = 0 (P4 for the undressed operator, B02);
  output         - every nonzero entry of *Shiab_h(xi W), sorted, as [[form mask, Clifford mask], [re, im]];
  leak_terms     - len(output); > 0 is a witness that P4 fails under that dressing;
  cov_zero       - Shiab_h(c_h xi W) = 0 with c_h x = h^-1 x h (covariance control).
A bivector outside the input's 4-plane commutes with each G_c (c in the plane), hence with every G_c G_d of xi W, so its
output is 0 by hand.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np

from gu.adjoint import from_mono, is_in_algebra
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import GQ, I, blade_to_mono, scale, star
from gu.curvature import is_algebraic_curvature, ricci
from gu.shiab import blade_mul, cayley_blade, eta_of, shiab, shiab_dressed, xi
from experiments.B07.escape.weyl_dressing import MODES, conj, in_group, phis_for

SIGS_14D = [(7, 7), (9, 5)]


def weyl_on(p: int, q: int, axes: tuple[int, int, int, int]) -> np.ndarray:
    """B02's weyl_control on the orthogonal 4-plane `axes`: sectional curvatures +-1, Ricci-flat by construction."""
    eta, n = eta_of(p, q), p + q
    a0, a1, a2, a3 = axes
    W = np.zeros((n, n, n, n), dtype=np.int64)
    for a, b, val in [(a0, a1, 1), (a2, a3, 1), (a0, a2, -1), (a1, a3, -1)]:
        val *= eta[a] * eta[b]
        W[a, b, a, b] = W[b, a, b, a] = val
        W[a, b, b, a] = W[b, a, a, b] = -val
    assert is_algebraic_curvature(W) and not np.any(ricci(W, eta)) and W.any()
    return W


def u_phase(blade: int, p: int, q: int) -> int:
    """0 if G_blade is in u(A), 1 if i G_blade is (experiments.B07.phase2.universal.phases, one blade)."""
    gs, A = gammas(p, q), from_mono(dirac_pairing(p, q))
    ok = [is_in_algebra(from_mono(blade_to_mono(blade, gs).times_i_power(k)), A) for k in (0, 1)]
    if ok.count(True) != 1:
        raise AssertionError(f"blade {blade}: u(A) membership {ok}")
    return ok.index(True)


def dressing(blade: int, p: int, q: int, t: Fraction = Fraction(1, 2)) -> tuple[dict, dict]:
    """(h, h^-1) for X = t u_blade. t must be an exact Fraction (GQ(1, 2) would be 1 + 2i, not 1/2)."""
    if not isinstance(t, Fraction):
        raise TypeError(f"t must be a Fraction, got {t!r}")
    return cayley_blade(blade, GQ(t) * (I if u_phase(blade, p, q) else GQ(1)), eta_of(p, q))


def is_spin0_exponential(h: dict, blade: int, eta: list[int]) -> bool:
    _, s = blade_mul(blade, blade, eta)
    if set(h) - {(0, 0), (0, blade)}:
        return False
    a, b = h.get((0, 0), GQ(0)), h.get((0, blade), GQ(0))
    if a.im or b.im or a.re <= 0:
        return False
    return a.re * a.re - s * b.re * b.re == 1


def transport_in_weyl(y: dict, p: int, q: int) -> bool:
    """True iff y = xi(W') for an algebraic, Ricci-flat W' (read off, scaled to integers, and rebuilt with xi)."""
    eta, n = eta_of(p, q), p + q
    if any(f.bit_count() != 2 or c.bit_count() != 2 or v.im for (f, c), v in y.items()):
        return False
    den = math.lcm(*(v.re.denominator for v in y.values())) if y else 1
    R = np.zeros((n, n, n, n), dtype=np.int64)
    for (f, c), v in y.items():
        a, b = [i for i in range(n) if f >> i & 1]
        k, l = [i for i in range(n) if c >> i & 1]
        r = 2 * v.re * eta[k] * eta[l] * den
        assert r.denominator == 1
        r = r.numerator
        R[a, b, k, l], R[b, a, k, l], R[a, b, l, k], R[b, a, l, k] = r, -r, -r, r
    return xi(R, eta) == scale(y, den) and is_algebraic_curvature(R) and not np.any(ricci(R, eta))


def named_blades(n: int, axes: tuple[int, int, int, int]) -> dict[str, int]:
    out = {"vector a0": 1 << axes[0]}
    for i, j in itertools.combinations(range(4), 2):
        out[f"bivector a{i}a{j}"] = (1 << axes[i]) | (1 << axes[j])
    o0, o1 = [k for k in range(n) if k not in axes][:2]
    out["bivector outside"] = (1 << o0) | (1 << o1)
    return out


def entries(x: dict) -> list:
    return [[list(k), [str(x[k].re), str(x[k].im)]] for k in sorted(x)]


def witnesses(p: int, q: int) -> list[dict]:
    eta = eta_of(p, q)
    rows = []
    for label, axes in (("weyl_control (axes 0-3)", (0, 1, 2, 3)), ("Lorentzian plane", (0, 1, 2, p))):
        x = xi(weyl_on(p, q, axes), eta)
        for bname, blade in named_blades(p + q, axes).items():
            h, hinv = dressing(blade, p, q)
            row = {"input": label, "axes": list(axes), "blade": blade, "blade_name": bname,
                   "phase": u_phase(blade, p, q), "in_u_a": in_group(h, p, q),
                   "spin0": is_spin0_exponential(h, blade, eta) if blade.bit_count() == 2 else None,
                   "commutes": conj(x, h, hinv, eta) == x,
                   "transport_in_weyl": transport_in_weyl(conj(x, hinv, h, eta), p, q), "modes": {}}
            for mode in MODES:
                P1, P2 = phis_for(mode, p, q)
                out = star(shiab_dressed(P1, P2, x, mode, eta, h, hinv), eta)
                row["modes"][mode] = {
                    "undressed_zero": not shiab(P1, P2, x, mode, eta),
                    "output": entries(out), "leak_terms": len(out),
                    "cov_zero": not shiab_dressed(P1, P2, conj(x, h, hinv, eta), mode, eta, h, hinv)}
            rows.append(row)
    return rows
