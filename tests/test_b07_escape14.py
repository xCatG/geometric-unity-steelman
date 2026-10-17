"""14D E2 witnesses (experiments/B07/escape/witness14.py). Exact (P4); counterexample scope at (7,7) and (9,5)."""
from fractions import Fraction

import numpy as np
import pytest

from gu.cliffform import GQ
from gu.shiab import eta_of, xi
from experiments.B02.run import weyl_control
from experiments.B07.escape import witness14 as W
from experiments.B07.escape.weyl_dressing import conj, rank, weyl_basis
from experiments.B07.phase2 import universal as U

# Leak-term counts per mode (CCC, CAA, CAC), pinned from the smoke run; > 0 is the claim, the counts a regression lock.
# The vector a0 on axes 0-3 under CCC and CAA reproduces B02 F5 (open data 5'); its CAC count and the Lorentzian plane
# are new for the vector. The Spin_0 bivector rows are the new 14D content.
LEAK = {"vector a0": (4, 4, 6), "bivector a0a1": (6, 16, 32), "bivector a0a2": (6, 16, 32),
        "bivector a1a3": (6, 16, 32), "bivector a2a3": (6, 16, 32),
        "bivector a0a3": (0, 0, 0), "bivector a1a2": (0, 0, 0), "bivector outside": (0, 0, 0)}


def test_weyl_on_generalizes_the_b02_control():
    for p, q in W.SIGS_14D:
        assert np.array_equal(W.weyl_on(p, q, (0, 1, 2, 3)), weyl_control(p, q))
        L = W.weyl_on(p, q, (0, 1, 2, p))                     # asserts algebraic, Ricci-flat, nonzero
        assert L[1, p, 1, p] == 1 and L[0, 1, 0, 1] == 1     # sectional -1 on a1 a3 times eta_1 eta_p = -1


def test_u_phase_matches_universal_phases_in_4d():
    assert [W.u_phase(b, 3, 1) for b in range(16)] == U.phases(3, 1)


def test_transport_in_weyl_matches_rank_membership_in_4d():
    """At (3,1), for every blade, transport_in_weyl agrees with membership in the span of xi(Weyl basis)."""
    eta = eta_of(3, 1)
    x, wb = xi(weyl_control(3, 1), eta), weyl_basis(3, 1)
    assert W.transport_in_weyl(x, 3, 1)
    seen = set()
    for b in range(1, 16):
        h, hinv = W.dressing(b, 3, 1)
        y = conj(x, hinv, h, eta)
        member = rank(wb + [y]) == rank(wb)
        assert W.transport_in_weyl(y, 3, 1) == member, b
        seen.add(member)
    assert seen == {True, False}


def test_dressing_rejects_inexact_t_and_bivector_cayley_is_an_exponential():
    with pytest.raises(TypeError):
        W.dressing(1, 3, 1, 0.5)
    eta = eta_of(7, 7)
    h, _ = W.dressing(0b11, 7, 7)                              # G_0 G_1, square -1: h = 3/5 - (4/5) G_0 G_1
    assert h == {(0, 0): GQ(Fraction(3, 5)), (0, 0b11): GQ(Fraction(-4, 5))}
    h, _ = W.dressing((1 << 0) | (1 << 7), 7, 7)               # G_0 G_7, square +1: h = 5/3 - (4/3) G_0 G_7
    assert h == {(0, 0): GQ(Fraction(5, 3)), (0, 0b10000001): GQ(Fraction(-4, 3))}
    assert W.is_spin0_exponential(h, 0b10000001, eta)


@pytest.fixture(scope="module", params=W.SIGS_14D)
def rows(request):
    return W.witnesses(*request.param)


def test_14d_witnesses(rows):
    """Every dressing is in U(A) (bivectors in Spin_0); P4 holds undressed; the covariance control is 0; the vector and
    four of the six in-plane Spin_0 bivectors leak in every mode; a0a3, a1a2 and the outside bivector give 0, and for
    them c_h^-1 xi W is again xi of a Weyl tensor. Observed on these rows: zero output iff transport_in_weyl (not a
    theorem: derivations E2.5 has a zero output without it). The vector a0 on axes 0-3 under CCC/CAA is B02 F5."""
    assert len(rows) == 16
    for r in rows:
        assert r["in_u_a"] and r["spin0"] is (True if r["blade"].bit_count() == 2 else None)
        assert r["commutes"] == (r["blade_name"] == "bivector outside")
        for mode, m in r["modes"].items():
            assert m["undressed_zero"] and m["cov_zero"], (r["blade_name"], mode)
            assert (m["leak_terms"] == 0) == r["transport_in_weyl"] == (m["output"] == []), (r["blade_name"], mode)
        counts = tuple(r["modes"][mode]["leak_terms"] for mode in W.MODES)
        assert counts == LEAK[r["blade_name"]], (r["input"], r["blade_name"], counts)
        first = r["modes"]["CCC"]["output"][:1]
        if r["blade_name"] == "vector a0":
            assert first == [[[2, 2], ["32/9", "0"]]], first
        if r["blade_name"] == "bivector a0a1":
            assert first == [[[1, 1], ["1952/625", "0"]]], first
