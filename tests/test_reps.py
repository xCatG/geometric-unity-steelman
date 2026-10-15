"""gu.reps: exact characters, checked against the tracked LiE fixture (B03 tests 1 and 2)."""
from collections import Counter

import pytest

from experiments.B03.oracle import polynomial, sections
from gu.reps import (Product, Simple, d2_as_a1a1, d7_to_d5a1a1, dn_doubled, dn_dynkin, restrict,
                     sm_weight, sm_weight_flipped, tensor)

D7, D5, A1, A2, A4 = (Simple("D", 7), Simple("D", 5), Simple("A", 1), Simple("A", 2),
                      Simple("A", 4))
V, SP, SM_, RSP, RSM = ((1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1, 0),
                        (1, 0, 0, 0, 0, 0, 1), (1, 0, 0, 0, 0, 1, 0))
TARGET = Product([D5, A1, A1])
SM = Product([A2, A1], u1=1)


def flat(decomp: Counter) -> Counter:
    """Product.decompose keys ((labels per factor), charges) -> flat label tuples (LiE order)."""
    return Counter({sum(parts, ()) + q: m for (parts, q), m in decomp.items()})


def test_a1_controls_match_lie_and_clebsch_gordan():
    """Control: 1/2 x 1/2 = 1 + 0 and 1 x 1/2 = 3/2 + 1/2 (textbook; also the LiE fixture)."""
    P = Product([A1])
    assert flat(P.decompose(tensor(A1.character((1,)), A1.character((1,))))) == Counter({(0,): 1, (2,): 1})
    assert flat(P.decompose(tensor(A1.character((2,)), A1.character((1,))))) == Counter({(1,): 1, (3,): 1})
    lie = sections()["A1 controls: 1/2 x 1/2 and 1 x 1/2"]
    assert lie[0] == Counter({(0,): 1, (2,): 1}) and lie[1] == Counter({(1,): 1, (3,): 1})


def test_d7_dimensions_and_character_sizes():
    """Claim (identity): Weyl dimensions 14, 64, 64, 832, 832 equal LiE's and each character's total."""
    lie = sections()["D7 dimensions V Splus Sminus RSplus RSminus"]
    for hw, dim in zip((V, SP, SM_, RSP, RSM), lie):
        assert D7.dimension(hw) == dim == sum(D7.character(hw).values())


def test_gamma_trace_has_opposite_chirality():
    """Claim (identity): V x S+ = RS+ + S- and V x S- = RS- + S+ (LiE fixture)."""
    P = Product([D7])
    tp, tm = sections()["D7 tensor V*Splus and V*Sminus: gamma trace has opposite chirality"][:2]
    assert flat(P.decompose(tensor(D7.character(V), D7.character(SP)))) == tp == Counter({RSP: 1, SM_: 1})
    assert flat(P.decompose(tensor(D7.character(V), D7.character(SM_)))) == tm == Counter({RSM: 1, SP: 1})


@pytest.mark.parametrize("title,hw", [
    ("Vector branch", V), ("Splus branch", SP), ("Sminus branch", SM_),
    ("RSplus branch", RSP), ("RSminus branch", RSM)])
def test_d7_to_d5a1a1_branching_matches_lie(title, hw):
    """Claim (identity, finite character): orthonormal-split restriction equals LiE's branch."""
    assert flat(TARGET.decompose(d7_to_d5a1a1(D7.character(hw)))) == polynomial(title)


@pytest.mark.parametrize("title,hw", [("V*Splus branch", SP), ("V*Sminus branch", SM_)])
def test_vector_spinor_branching_matches_lie(title, hw):
    """Claim (identity): V x S restricted, with multiplicities (two spinor-shaped 64s)."""
    ch = tensor(D7.character(V), D7.character(hw))
    assert flat(TARGET.decompose(d7_to_d5a1a1(ch))) == polynomial(title)


def test_spin10_sixteen_positive_control():
    """Control (spec 3.2): 16 = 10_1 + 5bar_-3 + 1_5 under SU(5) x U(1), LiE's reversed-A4 matrix."""
    r = [[0, 0, 0, 1, 2], [0, 0, 1, 0, 4], [0, 1, 0, 0, 6], [1, 0, 0, 0, 3], [0, 0, 0, 0, 5]]
    got = flat(Product([A4], u1=1).decompose(restrict(D5.character((0, 0, 0, 0, 1)), r)))
    assert got == polynomial("D5 Splus omega5: 16 = 10_1 + 5bar_-3 + 1_5")
    assert got == Counter({(0, 1, 0, 0, 1): 1, (0, 0, 0, 1, -3): 1, (0, 0, 0, 0, 5): 1})


@pytest.mark.parametrize("title,hw", [("SM 16", (0, 0, 0, 0, 1)), ("SM 16bar", (0, 0, 0, 1, 0)),
                                      ("SM H", (1, 0, 0, 0, 1)), ("SM Hbar", (1, 0, 0, 1, 0))])
def test_standard_model_restriction_matches_lie(title, hw):
    """Claim (identity): embedding E restricts 16, 16bar, H, Hbar exactly as LiE does."""
    ch = Counter()
    for w, m in D5.character(hw).items():
        ch[sm_weight(dn_doubled(w))] += m
    assert flat(SM.decompose(ch)) == polynomial(title)


def test_flipped_embedding_gives_identical_characters():
    """Control (ansatz rev 1, R2): E' is conjugate to E, so complete characters agree."""
    for hw in [(0, 0, 0, 0, 1), (0, 0, 0, 1, 0), (1, 0, 0, 0, 1), (1, 0, 0, 1, 0)]:
        a, b = Counter(), Counter()
        for w, m in D5.character(hw).items():
            a[sm_weight(dn_doubled(w))] += m
            b[sm_weight_flipped(dn_doubled(w))] += m
        assert SM.decompose(a) == SM.decompose(b)


def test_wrong_hypercharge_with_right_quark_doublet_is_rejected():
    """Ambient impostor (P2b): n = X also gives (3,2)_1 but not the 16 of the fixture."""
    def x_charge(y):
        a, b, k, _ = sm_weight(y)
        return a, b, k, sum(y)
    ch = Counter()
    for w, m in D5.character((0, 0, 0, 0, 1)).items():
        ch[x_charge(dn_doubled(w))] += m
    got = flat(SM.decompose(ch))
    assert got[(1, 0, 1, 1)] == 1 and got != polynomial("SM 16")


def test_coordinates_round_trip_and_spinor_parity():
    """Control: Dynkin <-> doubled coordinates; S+ highest weight is all +1 (even minus count)."""
    for hw in [V, SP, SM_, RSP, RSM, (0, 1, 0, 0, 0, 0, 0), (2, 0, 1, 0, 0, 1, 1)]:
        assert dn_dynkin(dn_doubled(hw)) == hw
    assert dn_doubled(SP) == (1,) * 7 and dn_doubled(SM_) == (1,) * 6 + (-1,)
    assert d2_as_a1a1((1, 1)) == (1, 0) and d2_as_a1a1((1, -1)) == (0, 1)


def test_exactness_contract_p4():
    """Control (P4, review finding 2): floats, nonintegral rationals, negative multiplicities,
    mixed widths and missing factors are rejected; numpy integers are converted, never overflow."""
    from fractions import Fraction
    import numpy as np
    from gu.reps import character, exact_int
    for bad in (1.0, True, Fraction(1, 2)):
        with pytest.raises(ValueError):
            exact_int(bad)
    with pytest.raises(ValueError):
        dn_dynkin((0.0, 0, 0, 0, 1))
    with pytest.raises(ValueError):
        sm_weight((1.0, 1, 1, 1, 1))
    with pytest.raises(ValueError):
        restrict(Counter({(1,): 1}), [[1.0]])
    with pytest.raises(ValueError):
        Product([A1]).decompose(Counter({(0,): Fraction(1, 2)}))
    with pytest.raises(ValueError):
        Product([A1]).decompose(Counter({(0,): -1, (2,): 1}))
    with pytest.raises(ValueError):
        character({(0,): 1, (0, 0): 1})
    with pytest.raises(ValueError):
        tensor(Counter({(0,): 1}), Counter({(0, 0): 1}))
    with pytest.raises(ValueError):
        Product([A1, A1]).character([(1,)])
    big = tensor(Counter({(0,): np.int64(2**62)}), Counter({(0,): np.int64(4)}))
    assert big == Counter({(0,): 2**64}) and type(big[(0,)]) is int
    assert exact_int(np.int64(7)) == 7 and exact_int(Fraction(6, 3)) == 2


def test_rejects_bad_input():
    """Control: no float or negative highest weights; a non-character cannot be decomposed."""
    with pytest.raises(ValueError):
        D5.character((0, 0, 0, 0, -1))
    with pytest.raises(ValueError):
        D5.dimension((0.0, 0, 0, 0, 1))
    with pytest.raises(ValueError):
        Product([A1]).decompose(Counter({(1,): 1}))


def test_flipped_embedding_large_exact_integers():
    """P4 control: n5=0 and X=5t give n'=6t, without int64 overflow."""
    import numpy as np
    expected = (0, 0, 0, 6 * 2**60)
    assert sm_weight_flipped((2**60,) * 5) == expected
    got = sm_weight_flipped((np.int64(2**60),) * 5)
    assert got == expected and all(type(x) is int for x in got)


@pytest.mark.parametrize("method", ["to_dynkin_root", "ip_left", "ip_right", "dominant", "orbit", "split"])
def test_public_coordinate_methods_reject_inexact(method):
    """P4 control: every coordinate operand rejects floats and nonintegral rationals."""
    from fractions import Fraction
    from gu.reps import weight
    calls = {
        "to_dynkin_root": A1.to_dynkin_root,
        "ip_left": lambda w: A1.ip(w, (1,)),
        "ip_right": lambda w: A1.ip((1,), w),
        "dominant": A1.dominant, "orbit": A1.orbit,
        "split": Product([A1]).split,
    }
    for bad in (1.0, Fraction(1, 2), True):
        with pytest.raises(ValueError) as expected:
            weight((bad,))
        with pytest.raises(type(expected.value)):
            calls[method]((bad,))
    with pytest.raises(ValueError):
        calls[method]((1, 2))


def test_public_coordinate_methods_normalize_large_numpy_integers():
    """P4 control: A1 Cartan=[2], inverse=[1/2]; convert before multiplication."""
    from fractions import Fraction
    import numpy as np
    for t in (2**62, np.int64(2**62)):
        got = A1.to_dynkin_root((t,))
        assert got == (2**63,) and type(got[0]) is int
        got_ip = A1.ip((t,), (t,))
        assert got_ip == Fraction(2**124, 2) and isinstance(got_ip, Fraction)
        assert A1.dominant((-t,)) == (2**62,)
        assert A1.orbit((t,)) == {(2**62,), (-2**62,)}
        parts, charges = Product([A1], u1=1).split((t, t))
        assert parts == [(2**62,)] and charges == (2**62,)
        assert type(parts[0][0]) is int and type(charges[0]) is int


@pytest.mark.parametrize("entry", ["cartan", "simple", "u1", "width", "empty_character_width"])
def test_public_numeric_sizes_use_exact_integer_contract(entry):
    """P4 control: numeric sizes reject inexact values and accept integral Fractions."""
    from fractions import Fraction
    from gu.reps import cartan, character, weight
    calls = {"cartan": lambda n: cartan("A", n), "simple": lambda n: Simple("A", n),
             "u1": lambda n: Product([A1], u1=n), "width": lambda n: weight((1,), n),
             "empty_character_width": lambda n: character({}, n)}
    for bad in (1.0, Fraction(1, 2), True):
        with pytest.raises(ValueError):
            calls[entry](bad)
    calls[entry](Fraction(1))
