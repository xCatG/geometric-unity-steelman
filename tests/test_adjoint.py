# tests/test_adjoint.py
import numpy as np
import pytest
from flint import fmpq, fmpq_mat

from gu.adjoint import (SingularCayley, cayley, embed, from_mono, is_in_algebra,
                        is_in_group, random_algebra_element)
from gu.clifford import dirac_pairing, gammas


@pytest.fixture(scope="module", params=[(1, 1), (3, 1), (7, 7), (9, 5)])
def setup(request):
    p, q = request.param
    return p, q, gammas(p, q), from_mono(dirac_pairing(p, q))


def _eye(n):
    return fmpq_mat(n, n, [1 if i == j else 0 for i in range(n) for j in range(n)])


def test_A_is_symmetric_involution(setup):
    _, _, _, A = setup
    assert A.transpose() == A and A * A == _eye(A.nrows())


def test_spin_generators_in_algebra(setup):
    p, q, G, A = setup
    for a in range(p + q):
        for b in range(a + 1, p + q):
            assert is_in_algebra(from_mono(G[a] @ G[b]), A)


def test_central_iI_in_algebra(setup):
    _, _, _, A = setup
    n = A.nrows() // 2
    assert is_in_algebra(embed(np.zeros((n, n), dtype=np.int64), np.eye(n, dtype=np.int64)), A)


def test_cayley_of_random_algebra_elements(setup):
    _, _, _, A = setup
    rng = np.random.default_rng(0)
    for _ in range(3):
        X = random_algebra_element(A, rng)
        assert is_in_algebra(X, A)
        assert is_in_group(cayley(X), A)


def test_spacelike_timelike_product_not_in_group(setup):
    p, _, G, A = setup
    h = from_mono(G[0] @ G[p])
    assert not is_in_group(h, A)
    assert h.transpose() * A * h == -A


def test_singular_cayley_guard():
    A = embed(np.diag([1, -1]), np.zeros((2, 2), dtype=np.int64))
    X = embed(np.array([[0, 1], [1, 0]]), np.zeros((2, 2), dtype=np.int64))  # unit boost
    assert is_in_algebra(X, A)
    with pytest.raises(SingularCayley):
        cayley(X)
    h = cayley(X * fmpq(1, 2))
    assert is_in_group(h, A)


def test_cayley_half_boost_value():
    """Control: (I-tK)/(I+tK)=((1+t²)I-2tK)/(1-t²), K²=I, t=1/2."""
    X = fmpq_mat([[0, fmpq(1, 2)], [fmpq(1, 2), 0]])
    assert cayley(X) == fmpq_mat([[fmpq(5, 3), fmpq(-4, 3)],
                                 [fmpq(-4, 3), fmpq(5, 3)]])


def test_embed_preserves_rationals_and_complex_structure():
    """Control: multiplication by 1/2+i/3 on (x,y) has the literal real block below."""
    from fractions import Fraction
    re = np.array([[Fraction(1, 2)]], dtype=object)
    im = np.array([[fmpq(1, 3)]], dtype=object)
    assert embed(re, im) == fmpq_mat([[fmpq(1, 2), fmpq(-1, 3)],
                                    [fmpq(1, 3), fmpq(1, 2)]])


@pytest.mark.parametrize('part', ['re', 'im'])
def test_embedding_rejects_float_input(part):
    """Control: int(0.5) must not silently erase a matrix entry."""
    re, im = np.zeros((1, 1), dtype=int), np.zeros((1, 1), dtype=int)
    if part == 're':
        re = np.array([[0.5]])
    else:
        im = np.array([[0.5]])
    with pytest.raises(ValueError):
        embed(re, im)


def test_real_orthogonal_is_not_necessarily_complex_unitary():
    """Counterexample control: complex conjugation is orthogonal, but not complex-linear."""
    A = _eye(2)
    conjugation = fmpq_mat([[1, 0], [0, -1]])
    assert conjugation.transpose() * A * conjugation == A
    assert not is_in_group(conjugation, A)
    M = fmpq_mat([[0, 0, 1, 0], [0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0]])
    assert M.transpose() + M == fmpq_mat(4, 4)
    assert not is_in_algebra(M, _eye(4))


def test_random_algebra_requires_hermitian_involution():
    """Control: A²=I alone is insufficient for the A-skew projection formula."""
    A = embed(np.array([[1, 1], [0, -1]]), np.zeros((2, 2), dtype=int))
    assert A * A == _eye(4)
    with pytest.raises(ValueError):
        random_algebra_element(A, np.random.default_rng(0))


def test_shape_and_sampling_guards():
    """Control: refuse broadcast matrices and fractional/zero sampling parameters."""
    for operation in (lambda: embed(np.zeros((2, 2), dtype=int), np.zeros((1, 1), dtype=int)),
                      lambda: random_algebra_element(_eye(2), np.random.default_rng(0), nonzeros=1.5),
                      lambda: random_algebra_element(_eye(2), np.random.default_rng(0), scale=0)):
        with pytest.raises(ValueError):
            operation()
