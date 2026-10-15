# tests/test_shiab.py
"""B02 claims about GU (9.3). Scope tags per P1; small signature first (P5)."""
import itertools
from fractions import Fraction

import numpy as np
import pytest

from gu.adjoint import from_mono, is_in_algebra
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import GQ, I, blade_to_mono, bits, plus, scale, star
from gu.curvature import kulkarni_nomizu, ricci, scalar
from gu.shiab import (embed_tensor, eta_of, generator_action, phi_basis, shiab,
                      shiab_parts, xi)

SIGS = [(3, 1), (7, 7), (9, 5)]


def _in_u_A(x: dict, p: int, q: int) -> bool:
    """x is u(A)-valued. Distinct blades are linearly independent and each blade is
    sharp-even or sharp-odd, so this holds iff every coefficient is purely real or
    purely imaginary with the phase its blade requires (sign is irrelevant)."""
    gs, A = gammas(p, q), from_mono(dirac_pairing(p, q))
    for (f, c), v in x.items():
        if v.re and v.im:
            return False
        if not is_in_algebra(from_mono(blade_to_mono(c, gs).times_i_power(1 if v.im else 0)), A):
            return False
    return True


@pytest.mark.parametrize("p,q", SIGS)
def test_phi_bases_are_u_A_valued(p, q):
    """Test 2(b), scope: identity (every coefficient checked)."""
    for name, phi in phi_basis(p, q).items():
        assert _in_u_A(phi, p, q), name


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7)])
def test_impostors_outside_u_A_are_rejected(p, q):
    """P2b impostors: right shape, wrong phase."""
    phis = phi_basis(p, q)
    assert not _in_u_A(scale(phis["F"], I), p, q)       # i F
    assert not _in_u_A(scale(phis["B'"], -I), p, q)     # B C without the i
    assert not _in_u_A({(1, 1): GQ(1, 1)}, p, q)         # mixed phase on one blade


@pytest.mark.parametrize("p,q", SIGS)
def test_phi_bases_are_spin_invariant(p, q):
    """Test 4(i), scope: identity (identity component; all 13 adjacent generators)."""
    eta, n = eta_of(p, q), p + q
    for name, phi in phi_basis(p, q).items():
        for a in range(n - 1):
            assert generator_action(phi, a, a + 1, eta) == {}, (name, a)


@pytest.mark.parametrize("p,q", SIGS)
def test_index_raised_impostor_is_not_invariant(p, q):
    """P2b impostor: sum e^a (x) eta_a G_a has the right grades but is not invariant."""
    eta, n = eta_of(p, q), p + q
    bad = {(1 << a, 1 << a): GQ(eta[a]) for a in range(n)}
    assert any(generator_action(bad, a, a + 1, eta) for a in range(n - 1))


@pytest.mark.parametrize("p,q", SIGS)
def test_star_is_equivariant(p, q):
    """Test 4(ii), scope: identity on the degrees (9.3) uses (full bases)."""
    eta, n = eta_of(p, q), p + q
    for k in sorted({0, 1, 2, n - 2, n - 1, n}):
        for idx in itertools.combinations(range(n), k):
            w = {(sum(1 << i for i in idx), 0): GQ(1)}
            for a in range(n - 1):
                assert star(generator_action(w, a, a + 1, eta), eta) == \
                    generator_action(star(w, eta), a, a + 1, eta)


def _sym_basis(n):
    out = []
    for i in range(n):
        for j in range(i, n):
            s = np.zeros((n, n), dtype=np.int64)
            s[i, j] = s[j, i] = 1
            out.append(s)
    return out


def predicted(R, eta, modes, al, be, ga, de, p, q):
    """Closed form (hand-derived, review derivation.md; extended bilinearly):
    *shiab(xi) = -[m0=C] E_T(Ric) + S/2 ([m1m2=AA] ga E_T(g) + [m1m2=AC] de E_T'(g)),
    with T = (al, be), T' = (be, al)."""
    n = len(eta)
    g = np.diag(eta).astype(np.int64)
    out = {}
    if modes[0] == "C":
        out = plus(out, scale(embed_tensor(ricci(R, eta), al, be, p, q), -1))
    S = Fraction(int(scalar(R, eta)), 2)
    if modes[1:] == "AA":
        out = plus(out, scale(embed_tensor(g, al, be, p, q), S * ga))
    if modes[1:] == "AC":
        out = plus(out, scale(embed_tensor(g, be, al, p, q), S * de))
    return out


@pytest.mark.parametrize("p,q", [(3, 1)])
def test_response_closed_form_on_spanning_set_small(p, q):
    """Test 5, scope: identity for (3,1) on all KN products of a symmetric basis
    (spanning set; rank certified in tests/test_b02_response.py, Task 4)."""
    eta = eta_of(p, q)
    phis = phi_basis(p, q)
    sym = _sym_basis(p + q)
    for s, t in itertools.combinations_with_replacement(range(len(sym)), 2):
        R = kulkarni_nomizu(sym[s], sym[t])
        x = xi(R, eta)
        for p1, (al, be) in (("F", (1, 0)), ("F'", (0, 1))):
            for p2, (ga, de) in (("B", (1, 0)), ("B'", (0, 1)), (None, (0, 0))):
                phi2 = phis[p2] if p2 else {}
                for modes in map("".join, itertools.product("CA", repeat=3)):
                    got = star(shiab(phis[p1], phi2, x, modes, eta), eta)
                    assert got == predicted(R, eta, modes, al, be, ga, de, p, q), (s, t, p1, p2, modes)


def test_shiab_parts_assemble_to_shiab():
    eta = eta_of(3, 1)
    phis = phi_basis(3, 1)
    R = kulkarni_nomizu(np.diag([1, 2, 0, 0]).astype(np.int64), np.eye(4, dtype=np.int64))
    x = xi(R, eta)
    parts = shiab_parts(phis["F"], phis["B"], x, eta)
    for modes in map("".join, itertools.product("CA", repeat=3)):
        assert shiab(phis["F"], phis["B"], x, modes, eta) == \
            plus(parts["first"][modes[0]], scale(parts["second"][modes[1:]], Fraction(-1, 2)))


def _R31():
    h = np.diag([1, 2, 0, -1]).astype(np.int64)
    k = np.zeros((4, 4), dtype=np.int64)
    k[0, 1] = k[1, 0] = 1
    k[2, 2] = 3
    return kulkarni_nomizu(h, k)


MODES = ["".join(m) for m in itertools.product("CA", repeat=3)]


def test_mixed_phi_matches_formula():
    """Control on the bilinear extension: a genuinely mixed Phi1, Phi2 (argon review)."""
    p, q = 3, 1
    eta, phis, R = eta_of(p, q), phi_basis(p, q), _R31()
    phi1 = plus(scale(phis["F"], 2), scale(phis["F'"], -3))
    phi2 = plus(scale(phis["B"], 5), scale(phis["B'"], 7))
    x = xi(R, eta)
    assert x
    for m in MODES:
        assert star(shiab(phi1, phi2, x, m, eta), eta) == predicted(R, eta, m, 2, -3, 5, 7, p, q), m


def test_shiab_is_equivariant_end_to_end():
    """Test 4, scope: sampled direct check of the composition proof (argon review);
    includes a non-Levi-Civita gauge term."""
    p, q = 3, 1
    eta, phis = eta_of(p, q), phi_basis(p, q)
    x = plus(xi(_R31(), eta), {(0b11, 0b111): GQ(0, 1)})
    for m in MODES:
        for a in range(3):
            assert generator_action(shiab(phis["F"], phis["B'"], x, m, eta), a, a + 1, eta) == \
                shiab(phis["F"], phis["B'"], generator_action(x, a, a + 1, eta), m, eta)


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_outputs_stay_in_u_A(p, q):
    """Test 2, scope: sampled direct check of the closure proof on shiab outputs."""
    eta, phis, n = eta_of(p, q), phi_basis(p, q), p + q
    s = np.zeros((n, n), dtype=np.int64)
    s[0, 1] = s[1, 0] = 1
    t = np.diag([1, 2, 3] + [0] * (n - 3)).astype(np.int64)
    t[0, 2] = t[2, 0] = 1
    x = plus(xi(kulkarni_nomizu(s, t), eta), {(0b11, 0b111): GQ(0, 1)})
    assert x and _in_u_A(x, p, q)
    nonzero = 0
    for m in (MODES if n == 4 else ["CCC", "CAA", "CAC"]):
        for k1, k2 in itertools.product(["F", "F'"], ["B", "B'"]):
            out = shiab(phis[k1], phis[k2], x, m, eta)
            assert _in_u_A(out, p, q), (m, k1, k2)
            nonzero += bool(out)
    assert nonzero > 0


def test_adapters_take_exact_rationals_and_reject_floats():
    """Exactness controls (review R2, P4)."""
    eta = eta_of(3, 1)
    half = Fraction(1, 2)
    R = np.zeros((4, 4, 4, 4), dtype=object)
    R[:] = 0
    R[0, 1, 0, 1] = R[1, 0, 1, 0] = half
    R[0, 1, 1, 0] = R[1, 0, 0, 1] = -half
    assert xi(R, eta) == {(0b11, 0b11): GQ(Fraction(1, 4))}    # 1/2 * R_0101 * eta0 eta1
    H = np.zeros((4, 4), dtype=object)
    H[:] = 0
    H[0, 0] = half
    assert embed_tensor(H, 1, 0, 3, 1) == {(1, 1): GQ(half)}
    with pytest.raises(TypeError):
        xi(np.full((4, 4, 4, 4), 0.5), eta)
    with pytest.raises(TypeError):
        embed_tensor(np.diag([1.9, 0.0, 0.0, 0.0]), 1, 0, 3, 1)
