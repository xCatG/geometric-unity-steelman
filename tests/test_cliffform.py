# tests/test_cliffform.py
"""Controls for the sparse Lambda (x) Cl engine (P1: no scope tag = control)."""
import itertools
import random
from fractions import Fraction

import numpy as np
import pytest

from gu.clifford import chirality, gammas
from gu.cliffform import (GQ, I, blade_mul, blade_to_mono, bracket, chirality_phase,
                          reorder_sign, right_mul_volume, star)
from gu.forms import hodge


def _eta(p, q):
    return [1] * p + [-1] * q


def _signed(m, s):
    return m if s == 1 else -m


def test_gq_rejects_floats_and_bools():
    for bad in (0.5, 1e0, True, complex(1, 0), np.float64(1)):
        with pytest.raises(TypeError):
            GQ(bad)


def test_gq_arithmetic_against_hand_values():
    a, b = GQ(1, 2), GQ(Fraction(1, 2), -1)
    assert a * b == GQ(Fraction(5, 2), 0)          # (1+2i)(1/2-i) = 1/2 - i + i + 2
    assert I * I == -1 and (a / a) == 1 and a - a == 0 and not (a - a)
    assert GQ(np.int64(3)) == 3


def test_gq_numpy_integers_cannot_overflow():
    """Exactness control (review R1): numpy fixed-width ints become Python ints."""
    big = GQ(np.int64(2**62)) * 4
    assert big == 2**64 and type(big.re.numerator) is int
    assert GQ(Fraction(np.int64(3), np.int64(4))) == Fraction(3, 4)


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (2, 2)])
def test_blade_mul_matches_mono_on_all_pairs(p, q):
    """Positive adapter control (P2b): every blade pair, against gu.clifford."""
    eta, n, gs = _eta(p, q), p + q, gammas(p, q)
    mono = [blade_to_mono(a, gs) for a in range(1 << n)]
    for a, b in itertools.product(range(1 << n), repeat=2):
        c, s = blade_mul(a, b, eta)
        assert mono[a] @ mono[b] == _signed(mono[c], s)


@pytest.mark.parametrize("p,q", [(7, 7), (9, 5)])
def test_blade_mul_matches_mono_sampled_14d(p, q):
    eta, gs, rng = _eta(p, q), gammas(p, q), random.Random(20261015)
    for _ in range(200):
        a, b = rng.randrange(1 << 14), rng.randrange(1 << 14)
        c, s = blade_mul(a, b, eta)
        assert blade_to_mono(a, gs) @ blade_to_mono(b, gs) == _signed(blade_to_mono(c, gs), s)


def test_reorder_sign_hand_values():
    assert reorder_sign(0b10, 0b01) == -1      # e1 e0 = -e0 e1
    assert reorder_sign(0b01, 0b10) == 1
    assert reorder_sign(0b110, 0b001) == 1     # e1 e2 e0: two swaps


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (7, 7), (9, 5)])
def test_star_matches_gu_forms_hodge(p, q):
    """Positive adapter control: every basis form of the degrees (9.3) uses."""
    eta, n = _eta(p, q), p + q
    for k in sorted({0, 1, 2, n - 2, n - 1, n}):
        for idx in itertools.combinations(range(n), k):
            f = sum(1 << i for i in idx)
            want = {(sum(1 << i for i in J), 0): GQ(v) for J, v in hodge({idx: 1}, eta).items()}
            assert star({(f, 0): GQ(1)}, eta) == want


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (7, 7), (9, 5)])
def test_chirality_phase_reproduces_library_chirality(p, q):
    gs = gammas(p, q)
    ph = chirality_phase(p, q)
    k = {GQ(1): 0, I: 1, GQ(-1): 2, -I: 3}[ph]
    assert blade_to_mono((1 << (p + q)) - 1, gs).times_i_power(k) == chirality(p, q)


def test_bracket_hand_values_3_1():
    eta = _eta(3, 1)
    g0, g1 = {(0, 1): GQ(1)}, {(0, 2): GQ(1)}     # 0-forms G_0, G_1
    assert bracket(g0, g1, "C", eta) == {(0, 3): GQ(2)}       # [G0,G1] = 2 G0G1
    assert bracket(g0, g1, "A", eta) == {}                    # i{G0,G1} = 0
    assert bracket(g0, g0, "A", eta) == {(0, 0): GQ(0, 2)}    # i{G0,G0} = 2i
    t = {(0, 8): GQ(1)}                                       # timelike G_3, G3^2 = -1
    assert bracket(t, t, "A", eta) == {(0, 0): GQ(0, -2)}
    e0, e1 = {(1, 0): GQ(1)}, {(2, 0): GQ(1)}
    assert bracket(e0, e1, "A", eta) == {(3, 0): GQ(0, 2)}    # e0 ^ e1 (x) i{1,1}
    assert bracket(e1, e0, "A", eta) == {(3, 0): GQ(0, -2)}


def test_bracket_rejects_unknown_mode():
    with pytest.raises(ValueError):
        bracket({}, {}, "X", [1, -1])


def test_right_mul_volume_is_mono_product():
    eta, gs = _eta(3, 1), gammas(3, 1)
    for a in range(16):
        ((f, c), v), = right_mul_volume({(0, a): GQ(1)}, GQ(1), eta).items()
        assert blade_to_mono(a, gs) @ blade_to_mono(15, gs) == _signed(blade_to_mono(c, gs), int(v.re))
