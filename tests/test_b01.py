"""B01 [ext] family checks; no GU reconciliation verdict.

The symbolic spectrum is an identity. Numeric matrices are exact sampled
regressions of that identity; expected table values follow the hand derivation
in ansatz.md (direct-sum inertias, with signs swapping positive/negative counts).
Fault targets: sign of lambda and omission of the two Lorentzian metric factors.
The F1 findings use the independent trace/traceless proof in rederivation.md.
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


def test_base_mirror_preserves_vertical_gram_symbolically():
    """F1 identity: two metric factors make B_lambda even under eta -> -eta.

    Catches an erroneous overall base sign on the vertical summand.
    """
    assert vertical_gram(LAM, base_sign=-1) == vertical_gram(LAM)


def test_base_mirror_changes_draft_split_signature():
    """F1 counterexample: a base-only mirror sends split to (5,9,0).

    Hand counts: horizontal (3,1)->(1,3), vertical stays (4,6).
    Catches ignoring the base mirror or negating both summands.
    """
    original = chimeric_gram(R(1, 2), -1, -1)
    mirrored = chimeric_gram(R(1, 2), -1, -1, base_sign=-1)
    assert original[:4, :4] == -ETA
    assert mirrored[:4, :4] == ETA
    assert mirrored[4:, 4:] == original[4:, 4:]
    assert inertia(original) == (7, 7, 0)
    assert inertia(mirrored) == (5, 9, 0)


@pytest.mark.parametrize("base_sign", [0, 1.0])
@pytest.mark.parametrize("api", [
    lambda sign: dewitt(ETA, ETA, R(0), base_sign=sign),
    lambda sign: vertical_gram(R(0), base_sign=sign),
    lambda sign: chimeric_gram(R(0), 1, 1, base_sign=sign),
])
def test_rejects_invalid_base_sign(api, base_sign):
    """Control: mirror selection must be exact +/-1 at each public boundary."""
    with pytest.raises(ValueError):
        api(base_sign)
