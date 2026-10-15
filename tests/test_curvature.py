# tests/test_curvature.py
import numpy as np
import pytest
from flint import fmpz_mat

from gu.curvature import (decompose, dims, is_algebraic_curvature, kulkarni_nomizu,
                          random_curvature, ricci, scalar)

SIGS = [(4, 0), (3, 1), (9, 5), (7, 7)]


def _eta(p, q):
    return np.array([1] * p + [-1] * q, dtype=np.int64)


@pytest.mark.parametrize("p,q", SIGS)
def test_constant_curvature_is_pure_scalar(p, q):
    # Positive control for the argon sign bug: W must be 0, not 2R.
    eta = _eta(p, q); g = np.diag(eta); n = p + q
    R = kulkarni_nomizu(g, g) // 2  # eta_ac eta_bd - eta_ad eta_bc
    assert np.array_equal(ricci(R, eta), (n - 1) * g)
    s = decompose(R, eta)
    assert not s.weyl.any() and not s.ricci_part.any()
    assert np.array_equal(s.scalar_part, s.denominator * R)


@pytest.mark.parametrize("p,q", SIGS)
def test_pure_traceless_ricci(p, q):
    eta = _eta(p, q); g = np.diag(eta); n = p + q
    rng = np.random.default_rng(1)
    h = rng.integers(-3, 4, (n, n)); h = h + h.T
    h[0, 0] -= eta[0] * int((eta * np.diag(h)).sum())  # make eta-traceless
    assert int((eta * np.diag(h)).sum()) == 0
    R = kulkarni_nomizu(h, g)
    s = decompose(R, eta)
    assert scalar(R, eta) == 0
    assert not s.weyl.any() and not s.scalar_part.any()
    assert np.array_equal(s.ricci_part, s.denominator * R)


@pytest.mark.parametrize("p,q", SIGS)
def test_generic_split(p, q):
    eta = _eta(p, q)
    R = random_curvature(p + q, np.random.default_rng(2))
    assert is_algebraic_curvature(R)
    s = decompose(R, eta)
    assert np.array_equal(s.weyl + s.ricci_part + s.scalar_part, s.denominator * R)
    assert is_algebraic_curvature(s.weyl)
    assert not ricci(s.weyl, eta).any()
    assert s.weyl.any()


@pytest.mark.parametrize("p,q", [(4, 0), (3, 1), (5, 0), (4, 2)])
def test_component_ranks_small_n(p, q):
    eta, n = _eta(p, q), p + q
    rng = np.random.default_rng(3)
    total = n * n * (n * n - 1) // 12
    Rs = [random_curvature(n, rng) for _ in range(total + 10)]
    rank = lambda arrs: fmpz_mat([[int(x) for x in a.ravel()] for a in arrs]).rank()
    assert rank(Rs) == total
    assert rank([decompose(R, eta).weyl for R in Rs]) == dims(n)[2]


def test_dims_d14():
    assert dims(14) == (1, 104, 3080)
    assert sum(dims(14)) == 14 * 14 * (14 * 14 - 1) // 12 == 3185


def test_hand_built_pure_weyl():
    """Control: sectional entries have zero row sums, hence Ric=0 without using a projector."""
    R = np.zeros((4, 4, 4, 4), dtype=np.int64)
    for (a, b), value in { (0, 1): 1, (0, 2): -1, (1, 3): -1, (2, 3): 1 }.items():
        R[a, b, a, b] = R[b, a, b, a] = value
        R[a, b, b, a] = R[b, a, a, b] = -value
    assert is_algebraic_curvature(R)
    assert not ricci(R, _eta(4, 0)).any()
    s = decompose(R, _eta(4, 0))
    assert not s.scalar_part.any() and not s.ricci_part.any()
    assert np.array_equal(s.weyl, s.denominator * R)


def test_bianchi_is_not_just_pair_symmetry():
    """Counterexample control: a volume 4-form has pair symmetry but cyclic sum 3*vol."""
    from itertools import permutations
    R = np.zeros((4, 4, 4, 4), dtype=np.int64)
    for I in permutations(range(4)):
        R[I] = (-1) ** sum(I[i] > I[j] for i in range(4) for j in range(i + 1, 4))
    assert not is_algebraic_curvature(R)


def test_exact_input_guards():
    """Control: float tensors/metrics and malformed shapes must not enter exact claims."""
    R = np.zeros((4, 4, 4, 4), dtype=np.int64)
    e = _eta(4, 0)
    operations = [lambda: kulkarni_nomizu(np.eye(4), np.eye(4)),
                  lambda: is_algebraic_curvature(R.astype(float)),
                  lambda: ricci(R.astype(float), e), lambda: scalar(R, e.astype(float)),
                  lambda: decompose(R, e.astype(float)), lambda: dims(4.0),
                  lambda: random_curvature(4, np.random.default_rng(0), terms=1.5),
                  lambda: ricci(R, np.array([1, 1, 1, 0])),
                  lambda: decompose(R, _eta(3, 0))]
    for op in operations:
        with pytest.raises(ValueError):
            op()


def test_overflow_is_rejected_not_wrapped():
    """Control: KN entry 2*(2^62)^2 exceeds int64; returning zero would be false exactness."""
    g = np.eye(4, dtype=np.int64) * (2 ** 62)
    with pytest.raises(OverflowError):
        kulkarni_nomizu(g, g)


def test_near_int64_limit_cancellation_is_exact():
    """Control: in dimension one KN vanishes, even when intermediate products exceed int64."""
    g = np.array([[2 ** 62]], dtype=np.int64)
    assert not kulkarni_nomizu(g, g).any()
