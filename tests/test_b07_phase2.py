"""B07 Phase 2 claims (experiments/B07/phase2/derivations.md). Scope tags per P1; 4D before 14D (P5); exact (P4)."""
import itertools
from collections import Counter
from fractions import Fraction

import numpy as np
import pytest
import sympy as sp

from gu.adjoint import from_mono, is_in_algebra
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import GQ, blade_to_mono, plus, scale
from gu.shiab import generator_action
from experiments.B07 import variation as V
from experiments.B07.phase2 import gates as G, second_order as SO2, symmetric as Sy, universal as U
from experiments.B07.phase2.run import e_op

CAA = "CAA Einstein, Phi1=F, gamma=1, delta=0"


def _ek(k):
    return {(1 << k, 0): GQ(1)}


def test_wedge_transpose_is_the_transpose():
    """H9, identity at (3,1): pair(t, X beta) = pair(X^t t, beta) for every basis 1-form t and 2-form beta."""
    eta, n = V.eta_of(3, 1), 4
    X = V.Linear(V.branch_map(CAA, 3, 1))
    Xt = Sy.wedge_transpose(X, n, eta)
    for t in V.one_forms(n):
        for b in Sy.two_forms(n):
            assert V.pair(t, X(b), eta) == V.pair(Xt(t), b, eta)


def test_transpose_symbol_is_minus_c1():
    """H9, identity at (3,1): <a, e^k ^ X^t t> = -<t, X(e^k ^ a)>, so sigma(L^dag - L) pairs to -C1, entry by entry."""
    eta, n = V.eta_of(3, 1), 4
    X = V.Linear(V.branch_map(CAA, 3, 1))
    Xt = Sy.wedge_transpose(X, n, eta)
    nonzero = 0
    for k in range(n):
        for t in V.one_forms(n):
            for a in V.one_forms(n):
                lhs = V.pair(a, V.wedge_prod(_ek(k), Xt(t), eta), eta) - V.pair(a, X(V.wedge_prod(_ek(k), t, eta)), eta)
                assert lhs == GQ() - V.c1_entry(X, k, t, a, eta)
                nonzero += bool(lhs)
    assert nonzero


def test_chern_simons_control_is_self_adjoint_and_factorizes():
    """H10 control (3D, X = id on 2-forms, Cl(3,0)): C1 = 0, SO = 0 and X# = X."""
    eta = [1, 1, 1]
    ident = lambda x: x
    assert not V.c1_residual(ident, 3, eta)
    assert not Sy.sym_obstruction(ident, 3, eta)
    Xs = Sy.sharp(ident, 3, eta)
    assert all(Xs(b) == b for b in Sy.two_forms(3))


def test_named_branch_does_not_factorize():
    """H10 impostor at (3,1): the CAA Einstein branch has SO != 0, so L^dag is not X# o d for an algebraic X#."""
    assert Sy.sym_obstruction(V.branch_map(CAA, 3, 1), 4, V.eta_of(3, 1))


@pytest.mark.parametrize("p,q", [(3, 1), (1, 3)])
def test_block_span_has_four_zero_relations(p, q):
    """H12 bookkeeping, identity: the 20 blocks span a 16-dimensional operator space; one relation is checked by hand."""
    from experiments.B07.phase2.run import independent_blocks
    _, relations = independent_blocks(p, q)
    assert relations == 4
    rel = [(("second", "CC", ("F", "B")), -1), (("second", "CA", ("F'", "B'")), -1),
           (("second", "AC", ("F'", "B'")), -1), (("second", "AA", ("F", "B")), 1)]
    for x in Sy.two_forms(4):
        assert not plus(*[scale(Sy.block_map(b, p, q)(x), c) for b, c in rel])


def _character_dims():
    half = Fraction(1, 2)
    L = {0: [(0, 0)], 1: [(half, half)], 2: [(1, 0), (0, 1)], 3: [(half, half)], 4: [(0, 0)]}

    def cg(a, b):
        out, j = [], abs(a - b)
        while j <= a + b:
            out.append(j)
            j += 1
        return out

    def tens(A, B):
        c = Counter()
        for a1, b1 in A:
            for a2, b2 in B:
                for a in cg(a1, a2):
                    for b in cg(b1, b2):
                        c[(a, b)] += 1
        return c
    out = {}
    for j in range(5):
        for l in range(5):
            X, Y = tens(L[2], L[j]), tens(L[3], L[l])
            d = sum(X[k] * Y[k] for k in X)
            if d:
                out[f"{j},{l}"] = d
    return out


@pytest.mark.parametrize("p,q", [(3, 1), (1, 3)])
def test_equivariant_dimension_matches_characters(p, q):
    """H12, identity: blockwise dims of the computed equivariant space equal the sl2 x sl2 character count (total 40)."""
    dims = U.block_dims(p, q)
    assert dims == _character_dims()
    assert sum(dims.values()) == 40


def test_equivariant_basis_commutes_with_spin_and_preserves_u_A():
    """H12, identity at (3,1): every basis map commutes with each generator 1/2 G_a G_b on every basis 2-form
    (checked with gu.shiab.generator_action directly, not the assembled matrices), and maps u(A) into u(A)."""
    p, q, n = 3, 1, 4
    eta, ph = V.eta_of(p, q), U.phases(p, q)
    gs, A = gammas(p, q), from_mono(dirac_pairing(p, q))
    basis = U.equivariant_basis(p, q)
    assert len(basis) == 40
    for M in basis:
        X = U.as_map(M, p, q, ph)
        for j in range(n + 1):
            for k in U.basis(n, 2, j):
                x = U.from_phased({k: Fraction(1)}, ph)
                y = X(x)
                for (f, c), v in y.items():
                    assert not (v.re and v.im)
                    mono = blade_to_mono(c, gs).times_i_power(1 if v.im else 0)
                    assert is_in_algebra(from_mono(mono), A)
                for a, b in itertools.combinations(range(n), 2):
                    assert X(generator_action(x, a, b, eta)) == generator_action(y, a, b, eta)


def test_blocks_lie_in_the_universal_span():
    """H12, identity at (3,1): the 20 blocks are among the equivariant maps (rank of basis + blocks stays 40)."""
    from experiments.B07.phase2.run import rank
    ph = U.phases(3, 1)
    basis = U.equivariant_basis(3, 1)
    blocks = [U.matrix_of(Sy.block_map(b, 3, 1), 3, 1, ph) for b in Sy.BLOCKS]
    assert rank(basis) == 40 and rank(basis + blocks) == 40


def test_e_op_is_self_adjoint_and_einstein():
    """H11/H13, identity at (3,1): E_OP has C1 = 0 and response 2 E_F(Ric) - S E_F(g) on every generator."""
    X = e_op(3, 1)  # the production constructor (run.E_OP), not a test-local copy
    assert not V.c1_residual(X, 4, V.eta_of(3, 1))
    r = G.response(X, 3, 1)
    assert [str(x) for x in r] == ["2", "0", "-1", "0"]
    assert G.is_einstein(r)


def test_c2_n0_control_and_e_op_c2():
    """H3/H13: 3D CS control, X = id: C2(N1) = 0 while C2(N0) != 0 (impostor). E_OP at (3,1) has C2 != 0 under all
    three normalizations (a bounded search over alpha in the first 16 basis 1-forms finds an exact nonzero entry)."""
    eta = [1, 1, 1]
    ident = V.Linear(lambda x: x)
    assert not G.c2_residual(ident, 3, eta, "N1")
    assert G.c2_residual(ident, 3, eta, "N0")
    X, eta4 = V.Linear(e_op(3, 1)), V.eta_of(3, 1)
    basis = V.one_forms(4)
    for norm in G.NORMS:
        found = any(G.c2_value(X, al, plus(t, s), norm, eta4) - G.c2_value(X, al, t, norm, eta4)
                    - G.c2_value(X, al, s, norm, eta4)
                    for al in basis[:16] for t, s in itertools.combinations(basis, 2))
        assert found, norm


@pytest.mark.parametrize("n", [4, 14])
@pytest.mark.parametrize("conv", ["pinned", "prime"])
def test_star_adjoint_and_mass_signs(n, conv):
    """H14, identity on every basis pair: *^dag = (-1)^(n-1) * on Omega^(n-1) -> Omega^1 and *^dag * = (-1)^q on
    1-forms, for every signature (p, n - p) and both standard Hodge conventions."""
    for p in range(n + 1):
        assert SO2.star_adjoint_sign(p, n - p, 1, conv) == (-1) ** (n - 1)
        assert SO2.mass_sign(p, n - p, conv) == (-1) ** (n - p)


@pytest.mark.parametrize("p,q", [(3, 1), (2, 2)])
def test_fourier_variation_of_9_11(p, q):
    """H14, identity at degree <= 2 in k: the action's variation matches (9.13) term 1, term 2 with * inserted, and
    *^dag in terms 3-4; printed term 3 has the opposite sign; printed term 4 matches iff q is even. Non-vacuous."""
    r = SO2.compare(V.branch_map(CAA, p, q), p, q, "pinned")
    c = r["checks"]
    assert c["kappa0: action == printed_1"] and c["kappa1: action == printed_2 + derived_3"]
    assert not c["kappa1: action == printed_2 + printed_3"] and c["derived_3 == -printed_3"]
    assert c["kappa2: action == derived_4"]
    assert c["kappa2: action == printed_4"] == (q % 2 == 0)
    assert all(r["nonvacuous"].values())


def test_exactness_helpers_reject_floats_and_decide_exactly():
    """P4 control: gq/combine/is_einstein/_einstein_dim reject floats (including 0.0, sympy Floats and mixed
    expressions) before any simplification, and decide large-integer cases exactly (no float division)."""
    big = 2 ** 60 + 1
    assert G.gq(sp.Rational(big, 3) + sp.I * sp.Rational(1, 7)) == GQ(Fraction(big, 3), Fraction(1, 7))
    assert G.gq(Fraction(-5, 4)) == GQ(Fraction(-5, 4))
    for good in (np.int64(-3), np.uint64(2 ** 63 + 1)):  # fixed-width numpy integers are exact
        assert G.gq(good) == GQ(int(good))
    assert G.is_einstein([np.int64(2), 0, np.int64(-1), 0])
    for bad in (np.float64(0.5), np.complex128(1j)):
        with pytest.raises(TypeError):
            G.gq(bad)
    for bad in (0.1, 0.0, sp.Float("0.1"), sp.Rational(1, 2) + sp.Float("0.5") * sp.I):
        with pytest.raises(TypeError):
            G.gq(bad)
        with pytest.raises(TypeError):
            G.combine([lambda x: x], [bad])
    rejected = []
    for r in ([2.0, 0, -1.0, 0], [2, 0, sp.Float(-1), 0]):
        try:
            G.is_einstein(r)
        except TypeError:
            rejected.append(r)
    assert len(rejected) == 2, "is_einstein accepted a float response"
    assert not G.is_einstein([big, 0, -(2 ** 59), 0])
    assert G.is_einstein([big, 0, sp.Rational(-big, 2), 0])
    assert G._einstein_dim([[big, 0, -(2 ** 59), 0]]) == 0
    assert G._einstein_dim([[big, 0, sp.Rational(-big, 2), 0]]) == 1


def test_provenance_guard_parser():
    """P8 guard: only the exact output path is exempt; staged and worktree renames consume their source record."""
    from experiments.B07.phase2.run import OUT_REL, dirty_paths
    assert dirty_paths("") == []
    assert dirty_paths(f" M {OUT_REL}\0") == []
    assert dirty_paths(" M gu/review-result.json\0?? tests/new.py\0") == ["gu/review-result.json", "tests/new.py"]
    assert dirty_paths(f"R  {OUT_REL}\0gu/cliffform.py\0") == ["gu/cliffform.py"]
    assert dirty_paths(f" R {OUT_REL}\0gu/cliffform.py\0") == ["gu/cliffform.py"]
    assert dirty_paths(f" R {OUT_REL}\0gu/{OUT_REL}\0") == [f"gu/{OUT_REL}"]
    assert dirty_paths("C  gu/a.py\0gu/b.py\0 M uv.lock\0") == ["gu/b.py", "gu/a.py", "uv.lock"]


def test_ym_symbol_control_and_branches():
    """H14 (9.14) at principal-symbol level: 3D control X = id gives ratio 1 everywhere; at (3,1) no named branch and
    not E_OP has a kinetic symbol proportional to ordinary Yang-Mills (unequal nonzero ratios)."""
    r = SO2.ym_symbol(lambda x: x, 3, 0)
    assert r["ym_proportional"] and r["ratios"] == [str(GQ(1))]
    for name in V.BRANCHES:
        assert not SO2.ym_symbol(V.branch_map(name, 3, 1), 3, 1)["ym_proportional"], name
    r = SO2.ym_symbol(e_op(3, 1), 3, 1)
    assert not r["ym_proportional"] and {str(GQ(16)), str(GQ(32))} <= set(r["ratios"])


def test_xstar_x_control_and_branches():
    """H14 (9.14), identity: 3D control X = id gives X*X = Id; no named branch at (3,1) has X*X a multiple of Id."""
    assert SO2.xstar_x(lambda x: x, 3, 0)["multiple_of_identity"]
    for name in V.BRANCHES:
        assert not SO2.xstar_x(V.branch_map(name, 3, 1), 3, 1)["multiple_of_identity"], name
