"""Controls (scope: sampled exact matrices), with textbook inertia expectations.

Congruence expectations follow Sylvester's law and the explicitly given
diagonal D; off-diagonal 2x2 blocks have eigenvalues +/-|z|.
Mutations targeted: sign of the Schur complement and loss of zero-diagonal pivot.
"""
# tests/test_inertia.py
import pytest
import sympy as sp

from gu.inertia import inertia


def test_diagonal():
    assert inertia(sp.diag(1, -1, 0, 3)) == (2, 1, 1)


def test_all_zero():
    assert inertia(sp.zeros(3)) == (0, 0, 3)


def test_zero_diagonal_needs_off_diagonal_pivot():
    assert inertia(sp.Matrix([[0, 1], [1, 0]])) == (1, 1, 0)


def test_zero_diagonal_with_null_row():
    assert inertia(sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])) == (1, 1, 1)


def test_hermitian_complex_offdiagonal():
    assert inertia(sp.Matrix([[0, sp.I], [-sp.I, 0]])) == (1, 1, 0)


def test_real_congruence_invariance():
    D = sp.diag(3, -2, 0, 5, -1)
    P = sp.Matrix([[1, 2, 0, -1, 1],
                   [0, 1, 3, 0, 0],
                   [0, 0, 1, -1, 4],
                   [0, 0, 0, 1, 2],
                   [0, 0, 0, 0, 1]])
    P = P.T * P.permute([4, 2, 0, 1, 3])  # mix rows; still invertible
    assert P.det() != 0
    assert inertia(P * D * P.T) == (2, 2, 1)


def test_complex_congruence_invariance():
    D = sp.diag(1, -1, 0)
    P = sp.Matrix([[1, sp.I, 0], [0, 1, 2 - sp.I], [0, 0, 1]])
    assert inertia((P * D * P.H).applyfunc(sp.expand)) == (1, 1, 1)


def test_rational_entries():
    assert inertia(sp.Matrix([[sp.Rational(1, 3), 0], [0, sp.Rational(-2, 7)]])) == (1, 1, 0)


def test_accepts_unexpanded_gaussian_expressions():
    z = (1 + sp.I) ** 2  # = 2i
    assert inertia(sp.Matrix([[0, z], [sp.conjugate(z), 0]])) == (1, 1, 0)


def test_rejects_float():
    with pytest.raises(ValueError):
        inertia(sp.Matrix([[0.5]]))


def test_rejects_non_hermitian():
    with pytest.raises(ValueError):
        inertia(sp.Matrix([[1, 2], [3, 4]]))


def test_rejects_non_square():
    with pytest.raises(ValueError):
        inertia(sp.Matrix([[1, 2]]))
