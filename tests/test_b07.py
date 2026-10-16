"""B07 checks. Controls validate the variation machinery; Shiab-family survey outcomes are recorded by the runner."""
from fractions import Fraction

import pytest

from experiments.B07 import variation as V
from gu.cliffform import GQ, bracket, plus, scale
from gu.shiab import eta_of, phi_basis, shiab

E3 = [1, 1, 1]


def test_pair_is_graded_symmetric_on_one_and_two_forms():
    """Control, identity (3D): Tr(x ^ y) = Tr(y ^ x) for a 1-form x and a 2-form y (degree product even, trace cyclic)."""
    x = {(0b001, 0b011): GQ(1), (0b010, 0b100): GQ(2)}
    y = {(0b110, 0b011): GQ(3), (0b101, 0b110): GQ(Fraction(1, 2))}
    assert V.pair(x, y, E3) == V.pair(y, x, E3)


def test_bracket_is_twice_the_wedge_square():
    """Control, identity: for an ad-valued 1-form T, [T ^ T] = 2 T^T (so N1's b(T,T) = T^T, N2's = 2 T^T)."""
    T = {(0b001, 0b001): GQ(1), (0b010, 0b011): GQ(1), (0b100, 0b110): GQ(2)}
    assert bracket(T, T, "C", E3) == scale(V.wedge_prod(T, T, E3), 2)
    assert V.b_bracket(T, T, "N1", E3) == V.wedge_prod(T, T, E3)


def test_chern_simons_control_c1():
    """Control, identity (hand-derived): in 3D with X = id, I = int Tr(T ^ (1/2 dT + ...)) is 1/2 Chern-Simons, whose
    first variation is Tr(alpha ^ F). The order-T^1 symbol residual must vanish: Tr(t^k^a) + Tr(a^k^t) = 0 by
    trace cyclicity and the sign of swapping two 1-forms past a 1-form."""
    assert V.c1_residual(lambda x: x, 3, E3) == {}


def test_chern_simons_control_c2_n1():
    """Control, identity (hand-derived): with X = id and N1 ([T,T] = T^T), the cubic term 1/3 Tr(T^T^T) varies to
    Tr(alpha^T^T), which matches F_A's T^T term: C2 vanishes."""
    assert V.c2_residual(lambda x: x, 3, E3, "N1") == {}


def test_chern_simons_impostor_n2():
    """Ambient impostor (P2b): with N2 ([T,T] = [T^T] = 2 T^T) the same Chern-Simons action varies to 2 Tr(alpha^T^T),
    so C2 must be nonzero. Hand: residual = (2/3 + 4/3 - 1) Tr(alpha T^2) = Tr(alpha T^2) != 0 for suitable inputs."""
    assert V.c2_residual(lambda x: x, 3, E3, "N2") != {}


def _right_g0(x):
    """X = right multiplication of the Clifford factor by G_0: not symmetric under the trace pairing."""
    from gu.cliffform import blade_mul
    out = {}
    for (f, a), v in x.items():
        c, z = blade_mul(a, 0b001, E3)
        out = plus(out, {(f, c): v * z})
    return out


def test_non_self_adjoint_impostor_c1():
    """Ambient impostor (P2b): X = right multiplication by G_0 breaks trace symmetry, so C1 must be nonzero in 3D."""
    assert V.c1_residual(_right_g0, 3, E3) != {}


def test_c1_entry_matches_residual():
    """Control: the single-entry evaluator used for 14D witnesses agrees with the full residual table on every 3D
    basis entry of the impostor (so a witness is a genuine entry of C1, not of a different expression)."""
    res = V.c1_residual(_right_g0, 3, E3)
    basis = V.one_forms(3)
    for k in range(3):
        for i, t in enumerate(basis):
            for j in range(i, len(basis)):
                assert V.c1_entry(_right_g0, k, t, basis[j], E3) == res.get((k, i, j), GQ())


def test_kernel_of_independent_columns_is_trivial():
    """Control: the exact kernel helper returns [] for independent columns and the dependency for dependent ones."""
    assert V.kernel({"a": {1: GQ(1)}, "b": {2: GQ(1)}}) == []
    assert V.kernel({"a": {1: GQ(1)}, "b": {1: GQ(2)}}) == [[-2, 1]]


def test_survey_shape_small():
    """The survey runs on one mode at (3,1) and records every column and both kernels (outcome not asserted)."""
    s = V.survey(3, 1, "CAA", "N1", with_c2=False)
    assert s["columns"] == [list(c) for c in V.COLUMNS]
    assert set(s["c1_nonzero"]) == {"+".join(c) for c in V.COLUMNS}
    assert isinstance(s["c1_kernel"], list)


def test_b_bracket_rejects_unknown_norm():
    with pytest.raises(ValueError):
        V.b_bracket({}, {}, "N3", E3)


def _family_member(mode, coeffs, p, q):
    """The Shiab-family member sum_col coeff * column, built from the adapter `shiab_column`."""
    cols = {c: V.shiab_column(c, mode, p, q) for c in coeffs}
    return lambda x: plus(*[scale(cols[c](x), v) for c, v in coeffs.items()])


def test_family_columns_assemble_to_b02_shiab():
    """Adapter control (P2 non-vacuity): for every bracket mode and every (Phi1, Phi2) in {F, F'} x {B, B'}, the
    columns weighted by the MONOMIALS coefficients (alpha|beta = 1, gamma|delta = 1) equal B02's verified
    gu.shiab.shiab on all 96 basis ad-valued 2-forms at (3,1), and the output is not identically zero."""
    p, q = 3, 1
    eta, ph = eta_of(p, q), phi_basis(p, q)
    twos = [f for f in range(16) if bin(f).count("1") == 2]
    for mode in V.MODES:
        for f1 in ("F", "F'"):
            for f2 in ("B", "B'"):
                X = _family_member(mode, {(f1,): 1, (f1, f2): Fraction(-1, 2)}, p, q)
                nonzero = False
                for f in twos:
                    for b in range(16):
                        x = {(f, b): GQ(1)}
                        ref = shiab(ph[f1], ph[f2], x, mode, eta)
                        assert X(x) == ref, (mode, f1, f2, f, b)
                        nonzero = nonzero or bool(ref)
                assert nonzero, (mode, f1, f2)


def test_named_branches_match_b02_shiab():
    """Adapter control: each named branch equals gu.shiab.shiab with its declared Phi1, Phi2 on every 4D basis input."""
    p, q = 3, 1
    eta, ph = eta_of(p, q), phi_basis(p, q)
    phis = {"CCC": (ph["F"], ph["B"]), "CAA": (ph["F"], ph["B"]), "CAC": (plus(ph["F"], ph["F'"]), ph["B'"])}
    for name, (mode, _) in V.BRANCHES.items():
        X = V.branch_map(name, p, q)
        for f in (3, 5, 6, 9, 10, 12):
            for b in range(16):
                x = {(f, b): GQ(1)}
                assert X(x) == shiab(*phis[mode], x, mode, eta), (name, f, b)
