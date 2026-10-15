"""B01 [ext] family checks; no GU reconciliation verdict.

The symbolic spectrum is an identity. Numeric matrices are exact sampled
regressions of that identity; expected table values follow the hand derivation
in ansatz.md (direct-sum inertias, with signs swapping positive/negative counts).
Fault targets: sign of lambda and omission of the two Lorentzian metric factors.
"""
# tests/test_b01.py
import pytest
import sympy as sp

from experiments.B01.dewitt_family import ETA, LAM, chimeric_gram, dewitt, run, vertical_gram
from gu.inertia import inertia

R = sp.Rational


def test_vertical_eigenvalues_symbolic():
    """Identity: off-diagonal norms and a rank-one diagonal perturbation."""
    assert vertical_gram(LAM).eigenvals() == {-2: 3, 2: 3, 1: 3, 1 - 4 * LAM: 1}


@pytest.mark.parametrize("lam,expected", [
    (R(-1), (7, 3, 0)), (R(0), (7, 3, 0)), (R(1, 8), (7, 3, 0)),
    (R(1, 4), (6, 3, 1)),
    (R(1, 2), (6, 4, 0)), (R(1), (6, 4, 0)),
])
def test_vertical_inertia(lam, expected):
    """Sampled: exact regressions on both sides and at the degeneracy."""
    assert inertia(vertical_gram(lam)) == expected


CHIMERIC = {
    (R(0), 1, 1): (8, 6, 0), (R(0), 1, -1): (4, 10, 0),
    (R(0), -1, 1): (10, 4, 0), (R(0), -1, -1): (6, 8, 0),
    (R(1, 4), 1, 1): (7, 6, 1), (R(1, 4), 1, -1): (4, 9, 1),
    (R(1, 4), -1, 1): (9, 4, 1), (R(1, 4), -1, -1): (6, 7, 1),
    (R(1), 1, 1): (7, 7, 0), (R(1), 1, -1): (5, 9, 0),
    (R(1), -1, 1): (9, 5, 0), (R(1), -1, -1): (7, 7, 0),
}


@pytest.mark.parametrize("key", sorted(CHIMERIC, key=str))
def test_chimeric_inertia(key):
    """Sampled: direct-sum counts derived by hand, never from run()."""
    lam, hs, vs = key
    assert inertia(chimeric_gram(lam, hs, vs)) == CHIMERIC[key]


def test_rejects_float_lambda():
    with pytest.raises(ValueError):
        inertia(vertical_gram(0.25))


def test_run_reports_exact_table():
    out = run([R(0), R(1, 4), R(1)])
    assert out["cases"][2]["chimeric"]["-1,1"] == [9, 5, 0]
    assert out["method"] == "exact Hermitian congruence (gu.inertia)"


@pytest.mark.parametrize("value", [0.0, 0.25, sp.Float(1)])
def test_public_gram_rejects_float_before_arithmetic(value):
    """Control: P4 rejects inexact input at the API, including zero."""
    with pytest.raises(ValueError):
        vertical_gram(value)


def test_dewitt_rejects_float_tensor():
    """Control: a float tensor must not enter the contraction claim path."""
    h = sp.zeros(4)
    h[0, 0] = sp.Float(0.5)
    with pytest.raises(ValueError):
        dewitt(h, ETA, R(0))


@pytest.mark.parametrize("hs,vs", [(0, 1), (1, 2), (1.0, 1), (1, -1.0)])
def test_chimeric_rejects_invalid_signs(hs, vs):
    """Control: only exact signs from the registered family are admissible."""
    with pytest.raises(ValueError):
        chimeric_gram(R(0), hs, vs)
