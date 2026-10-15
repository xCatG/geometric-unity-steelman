# gu/shiab.py
"""GU (9.3), undressed (epsilon = 1), on sparse Lambda (x) Cl elements.

Pinned conventions (experiments/B02/ansatz.md, amendment 1):
  e^{ab} = e^a ^ e^b and G_{ab} = G_a G_b for a < b; all sums over increasing sets;
  xi(R) = 1/2 sum_{a<b, c<d} R_abcd eta_c eta_d e^{ab} (x) G_c G_d;
  F = sum e^a G_a, F' = F*C, B = sum e^{ab} G_a G_b, B' = B*(i C), C = gu chirality;
  E_T(H) = sum e^a (x) H_a^b T_b with T_b = alpha G_b + beta G_b C (2nd index raised).
"""
from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np

from gu.cliffform import (GQ, I, bracket, chirality_phase, clean, exact, plus, reorder_sign,
                          right_mul_volume, scale, star)


def eta_of(p: int, q: int) -> list[int]:
    return [1] * p + [-1] * q


def phi_basis(p: int, q: int) -> dict[str, dict]:
    """Real bases of the Spin-invariant spaces: F, F' (degree 1) and B, B' (degree 2)."""
    eta, n = eta_of(p, q), p + q
    cph = chirality_phase(p, q)
    F = {(1 << a, 1 << a): GQ(1) for a in range(n)}
    B = {((1 << a) | (1 << b), (1 << a) | (1 << b)): GQ(1)
         for a, b in itertools.combinations(range(n), 2)}
    return {"F": F, "F'": right_mul_volume(F, cph, eta),
            "B": B, "B'": right_mul_volume(B, I * cph, eta)}


def xi(R: np.ndarray, eta: list[int]) -> dict:
    """Entries must be exact integers or rationals (floats raise TypeError)."""
    n = len(eta)
    out = {}
    for a, b in itertools.combinations(range(n), 2):
        for c, d in itertools.combinations(range(n), 2):
            r = exact(R[a, b, c, d])
            if r:
                out[((1 << a) | (1 << b), (1 << c) | (1 << d))] = GQ(r * eta[c] * eta[d] / 2)
    return out


def shiab_parts(phi1: dict, phi2: dict, x: dict, eta: list[int]) -> dict:
    """The six bracket pieces of (9.3), before assembly.

    first[m0] = [phi1 ^ *x]_m0;  second[m1+m2] = *[phi1 ^ *[phi2 ^ *x]_m1]_m2.
    """
    sx = star(x, eta)
    first = {m: bracket(phi1, sx, m, eta) for m in "CA"}
    inner = {m: star(bracket(phi2, sx, m, eta), eta) for m in "CA"}
    second = {m1 + m2: star(bracket(phi1, inner[m1], m2, eta), eta) for m1 in "CA" for m2 in "CA"}
    return {"first": first, "second": second}


def assemble(parts: dict, modes: str) -> dict:
    """(9.3): first[m0] - (1/2) * second[m1+m2]. The only place the -1/2 lives."""
    if len(modes) != 3 or set(modes) - {"C", "A"}:
        raise ValueError("modes must be three of 'C'/'A'")
    return plus(parts["first"][modes[0]], scale(parts["second"][modes[1:]], Fraction(-1, 2)))


def shiab(phi1: dict, phi2: dict, x: dict, modes: str, eta: list[int]) -> dict:
    """(9.3) with epsilon = 1; `modes` = brackets for (Ricci term, inner, outer).

    Returns an ad-valued (n-1)-form.
    """
    return assemble(shiab_parts(phi1, phi2, x, eta), modes)


def generator_action(x: dict, a: int, b: int, eta: list[int]) -> dict:
    """Infinitesimal Spin(p,q) action of X = 1/2 G_a G_b (a < b) on Lambda (x) Cl.

    On the Clifford factor: ad_X. On vectors this gives E_b -> eta_b E_a, E_a -> -eta_a E_b,
    so on covectors (dual, minus transpose): e^a -> -eta_b e^b, e^b -> eta_a e^a,
    extended to forms as a derivation.
    """
    if not a < b:
        raise ValueError("need a < b")
    X = {(0, (1 << a) | (1 << b)): GQ(Fraction(1, 2))}
    cl = bracket(X, x, "C", eta)
    fm: dict = {}
    for (f, c), v in x.items():
        for src, dst, s in ((a, b, -eta[b]), (b, a, eta[a])):
            if f >> src & 1 and not f >> dst & 1:
                g = f ^ (1 << src)                  # remove e^src at its sorted slot
                sign_out = reorder_sign(1 << src, g)  # e^src ^ rest -> sorted f
                sign_in = reorder_sign(1 << dst, g)
                fm = plus(fm, {(g | (1 << dst), c): v * (s * sign_out * sign_in)})
    return plus(cl, fm)


def embed_tensor(H: np.ndarray, alpha, beta, p: int, q: int) -> dict:
    """E_T(H) = sum e^a (x) H_a^b (alpha G_b + beta G_b C)."""
    eta, n = eta_of(p, q), p + q
    base = clean({(1 << a, 1 << b): GQ(exact(H[a, b]) * eta[b])
                  for a in range(n) for b in range(n) if exact(H[a, b])})
    return plus(scale(base, alpha), scale(right_mul_volume(base, chirality_phase(p, q), eta), beta))
