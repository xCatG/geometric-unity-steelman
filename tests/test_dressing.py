# tests/test_dressing.py
"""B02 test 3(b) (sampled) and 5' (open data); sparse Cayley adapter controls."""
import itertools
from fractions import Fraction

import pytest
from flint import fmpq, fmpq_mat

from gu.adjoint import cayley, from_mono, is_in_group
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import GQ, I, blade_to_mono, plus
from gu.curvature import kulkarni_nomizu
from gu.shiab import cayley_blade, eta_of, left, phi_basis, right, shiab, shiab_dressed, xi


def dense(u: dict, p: int, q: int) -> fmpq_mat:
    """Adapter: sparse 0-form Clifford element -> gu.adjoint real embedding."""
    gs = gammas(p, q)
    out = None
    for (f, b), v in u.items():
        assert f == 0
        m = blade_to_mono(b, gs)
        term = from_mono(m) * fmpq(v.re.numerator, v.re.denominator) + \
            from_mono(m.times_i_power(1)) * fmpq(v.im.numerator, v.im.denominator)
        out = term if out is None else out + term
    return out


HALF = GQ(Fraction(1, 2))
# (blade, coefficient): elements of u(A): grade 1 real, grade 2 real, grade 3 imaginary.
GENERATORS = [(0b1, HALF), (0b11, HALF), (0b111, HALF * I), (0b1010, HALF), (0b1000, HALF)]


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_sparse_cayley_matches_library_cayley(p, q):
    """Positive adapter control (P2b): same matrix as gu.adjoint.cayley; in U(A)."""
    A = from_mono(dirac_pairing(p, q))
    eta = eta_of(p, q)
    for blade, t in GENERATORS:
        h, hinv = cayley_blade(blade, t, eta)
        assert dense(h, p, q) == cayley(dense({(0, blade): t}, p, q))
        assert is_in_group(dense(h, p, q), A)
        assert left(h, hinv, eta) == {(0, 0): GQ(1)}


def test_cayley_of_non_algebra_element_is_rejected():
    """P2b impostor: i*G_0 is not in u(A); its Cayley transform is not in U(A)."""
    p, q = 3, 1
    h, _ = cayley_blade(0b1, HALF * I, eta_of(p, q))
    assert not is_in_group(dense(h, p, q), from_mono(dirac_pairing(p, q)))


def _xi_samples(p, q):
    """General u(A)-valued 2-forms (not only Levi-Civita), plus one curvature input."""
    import numpy as np
    eta = eta_of(p, q)
    n = p + q
    s = np.zeros((n, n), dtype=np.int64); s[0, 1] = s[1, 0] = 1
    t = np.diag([1, 2, 3] + [0] * (n - 3)).astype(np.int64); t[0, 2] = t[2, 0] = 1
    return [{(0b11, 0b101): GQ(1), (0b110, 0b1): GQ(2)},
            {(0b101, 0b111): GQ(0, 1)},
            xi(kulkarni_nomizu(s, t), eta)]


def test_xi_samples_are_nonzero():
    assert all(all(_xi_samples(*sig)) for sig in [(3, 1), (7, 7), (9, 5)])


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_dressed_covariance_samples(p, q):
    """Test 3(b), scope: sampled. Shiab_{eps h}(h^-1 xi h) == h^-1 Shiab_eps(xi) h."""
    eta = eta_of(p, q)
    phis = phi_basis(p, q)
    hs = [cayley_blade(b, t, eta) for b, t in GENERATORS[:3]]
    epss = [cayley_blade(b, t, eta) for b, t in GENERATORS[3:]]
    modes = ["CAA", "CCC", "ACA"] if p + q == 4 else ["CAA"]   # 14D: keep the suite fast
    for (h, hi), (e, ei), x, m in itertools.product(hs, epss, _xi_samples(p, q), modes):
        eh, ehi = left(e, h, eta), left(hi, ei, eta)
        lhs = shiab_dressed(phis["F"], phis["B"], left(hi, right(x, h, eta), eta), m, eta, eh, ehi)
        rhs = left(hi, right(shiab_dressed(phis["F"], phis["B"], x, m, eta, e, ei), h, eta), eta)
        assert lhs == rhs


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7)])
def test_central_dressing_is_a_no_op(p, q):
    """Control: eps = Cayley(i/2 * I) is central in U(A), so conjugation is trivial.
    (A Spin-image eps is NOT a no-op: Phi is invariant only under the joint action
    on form and Clifford factors, while dressing acts on the Clifford factor alone.)"""
    eta = eta_of(p, q)
    phis = phi_basis(p, q)
    e, ei = cayley_blade(0, HALF * I, eta)
    assert is_in_group(dense(e, p, q), from_mono(dirac_pairing(p, q)))
    for x in _xi_samples(p, q):
        assert shiab_dressed(phis["F"], phis["B"], x, "CAA", eta, e, ei) == shiab(phis["F"], phis["B"], x, "CAA", eta)


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_open_data_weyl_under_non_spin_dressing(p, q, record_property):
    """Test 5', scope: sampled, open data (no expectation). Records whether
    Shiab_eps(xi(W)) vanishes for odd eps (outside the even Spin image)."""
    import numpy as np
    from gu.curvature import is_algebraic_curvature, ricci
    eta, n = eta_of(p, q), p + q
    W = np.zeros((n, n, n, n), dtype=np.int64)
    for a, b, val in [(0, 1, 1), (2, 3, 1), (0, 2, -1), (1, 3, -1)]:
        val *= eta[a] * eta[b]
        W[a, b, a, b] = W[b, a, b, a] = val
        W[a, b, b, a] = W[b, a, a, b] = -val
    assert is_algebraic_curvature(W) and not np.any(ricci(W, eta))
    phis = phi_basis(p, q)
    x = xi(W, eta)
    assert shiab(phis["F"], phis["B"], x, "CAA", eta) == {}       # undressed: annihilated
    for blade, t in [(0b1, HALF), (0b111, HALF * I)]:
        e, ei = cayley_blade(blade, t, eta)
        out = shiab_dressed(phis["F"], phis["B"], x, "CAA", eta, e, ei)
        record_property(f"weyl_{blade:b}", "zero" if not out else f"nonzero({len(out)} terms)")
        print(p, q, bin(blade), "zero" if not out else f"nonzero ({len(out)} terms)")
