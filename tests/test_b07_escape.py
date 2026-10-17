"""Non-GR channels E1/E2 (experiments/B07/escape/derivations.md). Exact (P4); 4D point; identity on stated bases."""
import itertools
from fractions import Fraction

import numpy as np
import pytest

from gu.curvature import kulkarni_nomizu
from gu.shiab import eta_of
from experiments.B02.run import weyl_control
from experiments.B07 import variation as V
from experiments.B07.escape import quadratic as Q, weyl_dressing as WD
from experiments.B07.phase2 import gates as G
from experiments.B07.phase2.run import e_op

SIGS = [(3, 1), (1, 3)]
ZERO = ["0", "0", "0", "0"]


def test_bases_have_the_right_dimensions():
    """20 = dim algebraic curvature in 4D; 10 = dim Weyl (gu.curvature.dims)."""
    assert len(Q.curvature_basis(4)) == 20
    assert WD.rank(WD.weyl_basis(3, 1)) == 10


def test_invariant_controls():
    """KN(g, g): Ric = 2(n-1) g, S = 24, W = 0. The B02 Weyl control: Ric = 0, W != 0."""
    eta = eta_of(3, 1)
    g = np.diag(eta).astype(np.int64)
    K = kulkarni_nomizu(g, g)
    assert Q.invariant_bilinears(K, K, eta) == [0, 0, 0, 576]
    W = weyl_control(3, 1)
    ww, _, rr, ss = Q.invariant_bilinears(W, W, eta)
    assert ww != 0 and rr == 0 and ss == 0


def test_floats_are_rejected():
    """P4 at every new entry: curvature inputs, the greedy basis adapter, and the dressing parameter."""
    with pytest.raises((TypeError, ValueError)):  # gu.curvature raises ValueError first
        Q.invariant_bilinears(weyl_control(3, 1).astype(float), weyl_control(3, 1), eta_of(3, 1))
    with pytest.raises(TypeError):
        Q.independent([np.array([0.5])])
    assert Q.independent([np.array([Fraction(1, 2)], dtype=object)]) == [0]   # exact rational kept, not truncated
    assert Q.independent([np.array([2**70 + 1], dtype=object)]) == [0]
    with pytest.raises(TypeError):
        WD.family_report(3, 1, 0.5)


def test_weyl_dual_normalization():
    """W.*W uses (*W)_abcd = (1/2) eps_cd^fg W_abfg: for the dual D = *W, W.*D = -W.W (** = -1 on Lorentzian
    2-forms) and W.D = W.*W. Independent of the fit: D is built here by hand."""
    eta = eta_of(3, 1)
    for R in Q.curvature_basis(4)[:8]:
        W = Q.decompose(R, eta).weyl
        if not W.any():
            continue
        D = np.zeros((4, 4, 4, 4), dtype=object)
        for a, b, c, d in itertools.product(range(4), repeat=4):
            D[a, b, c, d] = Fraction(sum(Q._levi((c, d, f, g)) * eta[f] * eta[g] * W[a, b, f, g]
                                         for f, g in itertools.product(range(4), repeat=2)), 2)
        assert all(x.denominator == 1 for x in D.flat)
        D = D.astype(np.int64)
        ww, wsw, _, _ = Q.invariant_bilinears(W, W, eta)
        wd, wsd, _, _ = Q.invariant_bilinears(W, D, eta)
        assert ww != 0 and wsd == -ww and wd == wsw


def test_dressing_family_records_skips_and_lies_in_u_a():
    """Review Focus 2: singular Cayley members are skipped and listed; every member at t = 1/2 is in U(A)."""
    rep = WD.family_report(3, 1, Fraction(1))
    assert len(rep["skipped"]) == 8 and len(rep["members"]) + len(rep["skipped"]) == len(rep["attempted"]) == 15
    assert all(WD.in_group(e, 3, 1) for _, _, e, _ in WD.family(3, 1))


@pytest.mark.parametrize("p,q", SIGS)
def test_curvature_quadratic_form(p, q):
    """E1: Q has no Weyl or Weyl-dual part; E_OP gives -(4 Ric0^2 + S^2) = -4 Ric.Ric; CCC/CAA -Ric.Ric; CAC 0."""
    def fit(X, conv="pinned"):
        return Q.quadratic_form(X, p, q, conv)
    assert fit(e_op(p, q)) == {"re": ["0", "0", "-4", "-1"], "im": ZERO}
    assert fit(e_op(p, q), "prime") == {"re": ["0", "0", "4", "1"], "im": ZERO}
    for name, want in (("CCC", ["0", "0", "-1", "-1/4"]), ("CAA", ["0", "0", "-1", "-1/4"]), ("CAC", ZERO)):
        key = next(k for k in V.BRANCHES if k.startswith(name))
        assert fit(V.branch_map(key, p, q)) == {"re": want, "im": ZERO}, name


def _from_gram(Gm, r):
    tot = [Fraction(0)] * 4
    for i in range(4):
        for j in range(4):
            assert Gm[i][j]["im"] == ZERO
            for k in range(4):
                tot[k] += Fraction(r[i]) * Fraction(r[j]) * Fraction(Gm[i][j]["re"][k])
    return [str(x) for x in tot]


def test_response_gram_reproduces_q_and_the_einstein_identity():
    """Q_X = r^T G r for X with response r; on the Einstein ratio (c = -a/2, d = -b/2) Q = (b^2 - a^2) Ric.Ric."""
    p, q = 3, 1
    Gm = Q.response_gram(p, q)
    for X in (e_op(p, q), V.branch_map(next(k for k in V.BRANCHES if k.startswith("CCC")), p, q)):
        assert _from_gram(Gm, G.response(X, p, q)) == Q.quadratic_form(X, p, q)["re"]
    for a, b in ((1, 0), (0, 1), (2, 3), (Fraction(1, 2), -5)):
        a, b = Fraction(a), Fraction(b)
        k = b * b - a * a
        assert _from_gram(Gm, [a, b, -a / 2, -b / 2]) == [str(x) for x in (0, 0, k, k / 4)]


def test_dressed_weyl_response():
    """E2 at (3,1), CCC: undressed 0; leak ranks 10/6/5/0 for grades 1/2/3/4; covariance defect 0; residual 3/2/3/6."""
    p, q = 3, 1
    eta = eta_of(p, q)
    weyl = WD.weyl_basis(p, q)
    from gu.shiab import xi
    curv = [xi(R, eta) for R in Q.curvature_basis(4)]
    fam = {b: (e, ei) for b, _, e, ei in WD.family(p, q)}
    for blade, leak, res in ((0b0001, 10, 3), (0b0011, 6, 2), (0b0111, 5, 3), (0b1111, 0, 6)):
        e, ei = fam[blade]
        row = WD.survey_one("CCC", p, q, e, ei, weyl, curv)
        assert (row["leak_rank"], row["cov_defect"], row["residual"]) == (leak, 0, res), blade
        if blade == 0b0001:
            assert row["dressed_Q"]["re"] is None          # not Spin-invariant: recorded, not raised
        if blade == 0b1111:
            assert row["dressed_Q"] == Q.quadratic_form(V.branch_map(next(k for k in V.BRANCHES if k.startswith("CCC")), p, q), p, q)
    assert len(fam) == 15                                    # no blade skipped as singular at (3,1)
    s = WD.survey(p, q, ("CCC",))
    assert s["modes"]["CCC"]["undressed_leak_rank"] == 0 and s["weyl_dim"] == 10
