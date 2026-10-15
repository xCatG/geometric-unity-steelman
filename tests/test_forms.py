# tests/test_forms.py
import pytest

from gu.forms import basis, eta_I, hodge, inner, vol, wedge


def _eta(p, q):
    return [1] * p + [-1] * q


@pytest.mark.parametrize("p,q,k", [(p, q, k) for p, q in [(1, 1), (3, 1), (9, 5), (7, 7)]
                                  for k in [0, 1, 2, 7, 13, 14] if k <= p + q])
def test_pinned_convention_and_star_squared(p, q, k):
    eta, n = _eta(p, q), p + q
    sign = (-1) ** (k * (n - k) + q)
    for I in basis(n, k):
        e = {I: 1}
        assert wedge(e, hodge(e, eta)) == {tuple(range(n)): eta_I(eta, I)}
        assert hodge(hodge(e, eta), eta) == {I: sign}


def test_lorentzian_known_values():
    eta = _eta(3, 1)  # e3 timelike
    assert hodge({(0, 1): 1}, eta) == {(2, 3): 1}
    assert hodge(hodge({(0, 1): 1}, eta), eta) == {(0, 1): -1}  # star^2 = -1 on 2-forms in 4D Lorentzian


def test_wedge_basics():
    assert wedge({(0,): 1}, {(0,): 1}) == {}
    assert wedge({(1,): 1}, {(0,): 1}) == {(0, 1): -1}
    assert wedge({(0,): 2}, {(1,): 3}) == {(0, 1): 6}


def test_inner_and_vol():
    eta = _eta(1, 1)
    assert inner({(1,): 1}, {(1,): 1}, eta) == -1
    assert inner(vol(2), vol(2), eta) == -1


def test_mixed_form_pairing_and_cancellation():
    """Sampled control: diagonal (3,1) form metric gives 2*3 - 4*5 = -14."""
    a, b = {(0, 1): 2, (2, 3): 4}, {(0, 1): 3, (2, 3): 5}
    assert inner(a, b, _eta(3, 1)) == -14
    assert wedge(a, hodge(b, _eta(3, 1))) == {(0, 1, 2, 3): -14}
    assert wedge({(0,): 1, (1,): 1}, {(0,): 1, (1,): 1}) == {}


@pytest.mark.parametrize('form', [{(0,): 1.0}, {(0.0,): 1}, {(1, 0): 1},
                                 {(0, 0): 1}, {(-1,): 1}])
def test_forms_reject_lossy_or_noncanonical_input(form):
    """Control: malformed indices and floats cannot become exact coefficients."""
    for op in (lambda: wedge(form, {(): 1}), lambda: inner(form, {}, [1, -1]),
               lambda: hodge(form, [1, -1])):
        with pytest.raises(ValueError):
            op()


def test_metric_and_dimension_guards():
    """Control: Hodge requires +/-1 metric and in-range indices; dimensions are integers."""
    for metric in ([1.0, -1], [1, 0], [1, 2]):
        for op in (lambda: eta_I(metric, ()), lambda: inner({}, {}, metric),
                   lambda: hodge({}, metric)):
            with pytest.raises(ValueError):
                op()
    for op in (lambda: hodge({(2,): 1}, [1, -1]),
               lambda: eta_I([1, -1], (2,)), lambda: vol(2.0),
               lambda: basis(2, 1.0), lambda: basis(-1, 0)):
        with pytest.raises(ValueError):
            op()
