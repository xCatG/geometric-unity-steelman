"""B05 transcription-stage checks. Controls validate the tools; branch-survey outcomes are recorded by the runner, not asserted."""
from fractions import Fraction

import numpy as np
import pytest

from experiments.B05 import operator_check as OC
from experiments.B05 import pairing as PR
from experiments.B05 import source_operator as SRC
from gu.clifford import Mono, chirality, gammas

SIGS = [(3, 1), (1, 3), (7, 7), (9, 5)]


# ---- pairing.py: forms and U(1)s ----------------------------------------------------------------------------

@pytest.mark.parametrize("p,q", SIGS + [(2, 2)])
def test_both_forms_are_spin_invariant_hermitian(p, q):
    """Control, identity: products of all timelike (resp. spacelike) gammas give Spin(p,q)-invariant Hermitian forms."""
    for A in PR.forms(p, q).values():
        assert A.dagger() == A
        assert PR.invariant(p, q, A)


@pytest.mark.parametrize("p,q", SIGS)
def test_forms_pair_opposite_chirality_when_q_odd(p, q):
    """Identity: A anticommutes with C for (3,1), (1,3), (7,7), (9,5).

    Hand derivation: A is a product of q (or p) gammas, each anticommuting with C in even dimension, so
    AC = (-1)^q CA, and p, q are odd here.
    """
    for A in PR.forms(p, q).values():
        assert PR.relation_to_chirality(p, q, A) == "anticommute"


def test_forms_commute_with_chirality_at_2_2():
    """Control, identity: q = 2 even, so AC = CA (ambient impostor for the q-odd rule)."""
    for A in PR.forms(2, 2).values():
        assert PR.relation_to_chirality(2, 2, A) == "commute"


@pytest.mark.parametrize("p,q", [(3, 1), (1, 3), (7, 7), (9, 5)])
def test_neutral_signature(p, q):
    """Identity: a Hermitian form anticommuting with the involution C swaps its +-1 eigenspaces, so has signature (n/2, n/2)."""
    for A in PR.forms(p, q).values():
        assert PR.signature_of(A) == (A.n // 2, A.n // 2)


def test_signature_of_rejects_non_hermitian():
    """P4-style boundary: an anti-Hermitian 2-cycle iX is not a form."""
    iX = Mono([1, 0], [1, 1])
    with pytest.raises(ValueError):
        PR.signature_of(iX)


@pytest.mark.parametrize("p,q", SIGS)
def test_u1_membership(p, q):
    """Identity: when AC = -CA, iI and C are in u(A) but the axial phase iC is not.

    Hand derivation: (iC)^dag A + A(iC) = i(AC - CA) = 2iAC != 0; C^dag A + AC = CA + AC = 0.
    """
    for A in PR.forms(p, q).values():
        assert PR.u1_membership(p, q, A) == {"central_iI": True, "axial_iC": False, "chiral_boost_C": True}


def test_u1_membership_flips_at_2_2():
    """Control, identity: when AC = CA (q even), iC is in u(A) and C is not."""
    for A in PR.forms(2, 2).values():
        assert PR.u1_membership(2, 2, A) == {"central_iI": True, "axial_iC": True, "chiral_boost_C": False}


# ---- pairing.py: bilinear variations (Task 5's criterion, pre-registered) ------------------------------------

def _k_c_i(p, q):
    G, C = gammas(p, q), chirality(p, q)
    return G[0], C, Mono.identity(C.n)


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_r1_dirac_adjoint_variation(p, q):
    """Identity, hand-derived. R1: psibar = psi^dag A, A fixed, so delta psibar = psibar S^sharp, S^sharp = A^-1 S^dag A.

    K = Gamma_0 anticommutes with C. With AC = -CA:
      S = iC:  (iC)^sharp = iC,  sum = i{C,K} = 0       -> invariant (axial phase, though iC is not in u(A));
      S = C:   C^sharp = -C,     sum = [K,C] = 2KC != 0  -> NOT invariant;
      S = iI:  (iI)^sharp = -iI, sum = -iK + iK = 0      -> invariant.
    """
    K, C, I = _k_c_i(p, q)
    for A in PR.forms(p, q).values():
        iC, iI = C.times_i_power(1), I.times_i_power(1)
        assert PR.sharp(iC, A) == iC and PR.sharp(C, A) == -C
        assert PR.bilinear_invariant(K, iC, PR.sharp(iC, A))
        assert not PR.bilinear_invariant(K, C, PR.sharp(C, A))
        assert PR.bilinear_invariant(K, iI, PR.sharp(iI, A))


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_r0_independent_bar_variation(p, q):
    """Identity, hand-derived. R0: psibar independent. With Sbar = C and S = C: sum = {C,K} = 0 -> invariant.
    With the contragredient law Sbar = -S = -C: sum = [K,C] != 0 -> not invariant. The law must be specified."""
    K, C, _ = _k_c_i(p, q)
    assert PR.bilinear_invariant(K, C, C)
    assert not PR.bilinear_invariant(K, C, -C)


def test_r1_variation_flips_at_2_2():
    """Control, identity: when AC = CA, C^sharp = C, so S = C gives {C,K} = 0 (invariant) and S = iC gives i[K,C] != 0."""
    K, C, _ = _k_c_i(2, 2)
    for A in PR.forms(2, 2).values():
        iC = C.times_i_power(1)
        assert PR.bilinear_invariant(K, C, PR.sharp(C, A))
        assert not PR.bilinear_invariant(K, iC, PR.sharp(iC, A))


# ---- operator_check.py: the A-adjoint label rule against independent 2x2 matrices ----------------------------

LAB = {"+": 0, "-": 1}


def _support(M):
    """{(source label, target label)} of the nonzero entries of an integer 2x2 matrix in the basis (+, -)."""
    inv = {0: "+", 1: "-"}
    return {(inv[j], inv[i]) for i in range(2) for j in range(2) if M[i, j] != 0}


@pytest.mark.parametrize("label,A", [("chirality", np.array([[0, 1], [1, 0]])),     # anticommutes with C=diag(1,-1)
                                     ("signature", np.array([[1, 0], [0, -1]]))])   # labels = A's own eigenspaces
@pytest.mark.parametrize("order", OC.ORDER)
def test_a_adjoint_rule_matches_matrices(label, A, order):
    """Control: for every elementary block E (source b -> target a), the support of A^-1 E^T A equals varpi_map's
    rule for varpibar*. Independent of the rule's code: plain integer matrices, real entries, so E^dag = E^T,
    and A^-1 = A for both test forms (A^2 = I)."""
    assert (A @ A == np.eye(2, dtype=int)).all()
    for a in "+-":
        for b in "+-":
            src, tgt = OC.varpi_map(("varpi", a, b), label, order, "a_adjoint")
            E = np.zeros((2, 2), dtype=int)
            E[LAB[tgt], LAB[src]] = 1
            assert _support(A @ E.T @ A) == {OC.varpi_map(("varpibar_star", a, b), label, order, "a_adjoint")}


def test_subscript_swap_is_a_different_reading():
    """Control: under chirality labels the two adjoint readings disagree on varpibar*_{+-}."""
    a = OC.varpi_map(("varpibar_star", "+", "-"), "chirality", "target_source", "a_adjoint")
    s = OC.varpi_map(("varpibar_star", "+", "-"), "chirality", "target_source", "subscript_swap")
    assert a != s


# ---- operator_check.py: textbook controls --------------------------------------------------------------------

ROWS_T = {"pb-": (0, "-"), "pb+": (0, "+"), "zb-": (1, "-")}
COLS_T = {"p+": (0, "+"), "p-": (0, "-")}
TEXTBOOK = dict(label="chirality", order="target_source", bar="dirac_adjoint", adj="a_adjoint", hom="strict",
                pair="metric", d0kind="clifford", starparse="extra_star", m=0, n=0, r=0)


def _statuses(entries, br=TEXTBOOK):
    out = OC.check(br, entries, ROWS_T, COLS_T)
    return [x["status"] for x in out["summands"]], [x["degree_ok"] for x in out["summands"]]


def test_textbook_dirac_kinetic_term():
    """Control: psibar_- (dslash psi_-) is the textbook Weyl kinetic term psi_L^dag sigma.d psi_L: nonzero, degree ok."""
    assert _statuses({("pb-", "p-"): ((+1, (SRC.D0,)),), ("pb+", "p+"): ((+1, (SRC.D0,)),)}) == \
        (["nonzero", "nonzero"], [True, True])


def test_same_chirality_scalar_bilinear_is_a_legal_zero():
    """Control: psibar_L psi_L = 0 (a mass term couples L to R). Legal and identically zero, not a type error."""
    e = {("pb-", "p-"): ((+1, (("endo", "-", "-"),)),)}
    assert _statuses(e) == (["pairs_to_zero"], [True])
    assert OC.check(TEXTBOOK, e, ROWS_T, COLS_T)["well_typed"]


def test_mass_term():
    """Control: psibar_- m psi_+ with a degree-0 endomorphism + -> + is the textbook Dirac mass coupling."""
    assert _statuses({("pb-", "p+"): ((+1, (("endo", "+", "+"),)),)}) == (["nonzero"], [True])


def test_degree_mismatch_detected():
    """Negative control: a 1-form-valued block between two 0-form fields fails the metric degree check."""
    assert _statuses({("pb-", "p+"): ((+1, (SRC.W("+", "+"),)),)})[1] == [False]


def test_domain_mismatch_vs_extension_by_zero():
    """Control: varpi_{+-} (target +, source -) on a + field: a type error if strict, the zero map if extended."""
    e = {("pb-", "p+"): ((+1, (SRC.W("+", "-"),)),)}
    assert _statuses(e)[0] == ["domain_mismatch"]
    assert _statuses(e, dict(TEXTBOOK, hom="extend_by_zero"))[0] == ["extended_zero"]


def test_signature_labels_leave_d0_undetermined():
    """Control: under the signature reading the support of d0 psi is not established (a flat d0 preserves an
    A-eigenvector; a boost-valued connection mixes), so the status is 'undetermined', not a proven mix."""
    br = dict(TEXTBOOK, label="signature", d0kind="exterior")
    assert _statuses({("zb-", "p-"): ((+1, (SRC.D0,)),)}, br)[0] == ["undetermined"]


def test_degree_bookkeeping_by_hand():
    """Control: on a 1-form in 14D, *(shiab_{m=1,n=0,r=1}(varpi ^ zeta)) has degree 14 - (14 - 2 + 1) = 1, and the
    outer_star parse of the same printed symbols (shiab with n=1, no extra star) also gives 14 - (12 + 1) = 1."""
    br = dict(TEXTBOOK, d0kind="exterior", m=1, n=0, r=1)
    k = 1
    for op in reversed((SRC.S, SRC.SH, SRC.W("+", "+"))):
        k = OC.degree(op, k, br)
    assert k == 1
    ob = dict(br, starparse="outer_star", n=1)
    k = 1
    for op in reversed(OC.parse((SRC.S, SRC.SH, SRC.W("+", "+")), ob)):
        k = OC.degree(op, k, ob, 1 if op == ("shiab", "outer") else None)
    assert k == 1


# ---- P4 boundary ---------------------------------------------------------------------------------------------

def test_p4_boundary():
    """P4: degrees, branch numbers and summand signs are exact integers (signs +-1); floats and non-integral rationals are rejected."""
    with pytest.raises(TypeError):
        OC.degree(SRC.D0, 1.5, TEXTBOOK)
    with pytest.raises(ValueError):
        OC.degree(SRC.D0, Fraction(3, 2), TEXTBOOK)
    with pytest.raises(TypeError):
        OC.degree(SRC.SH, 1, dict(TEXTBOOK, r=1.0))
    with pytest.raises(TypeError):
        OC.check(TEXTBOOK, {("pb-", "p+"): ((1.5, (("endo", "+", "+"),)),)}, ROWS_T, COLS_T)
    with pytest.raises(ValueError):
        OC.check(TEXTBOOK, {("pb-", "p+"): ((2, (("endo", "+", "+"),)),)}, ROWS_T, COLS_T)
    big = OC.as_int(np.int64(2**62))
    assert type(big) is int and big * 4 == 2**64


# ---- branch space and transcription shape --------------------------------------------------------------------

def test_branch_space_is_complete():
    """Control: 2^7 label/pairing axes x (extra_star: 2*2*15 + outer_star: 2*1*15) = 128 * 90 = 11520 distinct branches."""
    bs = OC.branches()
    assert len(bs) == 11520
    assert len({tuple(b.values()) for b in bs}) == 11520


def test_transcription_shape():
    """Control on Claude's typed data: 12 nonzero entries, 18 summands, lower-right absent, the 6 lower-row summands
    carry the printed minus and the 12 upper-row summands carry plus (p. 46)."""
    assert len(SRC.ENTRIES) == 12
    terms = [(r, s) for (r, _), ts in SRC.ENTRIES.items() for s, _ in ts]
    assert len(terms) == 18
    assert not any(r.startswith("nb") and c.startswith("n") for r, c in SRC.ENTRIES)
    assert all(s == (-1 if r.startswith("nb") else +1) for r, s in terms)


def test_survey_is_recorded_not_asserted():
    """The survey runs on every branch and returns per-summand statuses from the allowed set."""
    s = OC.survey()
    assert s["n_branches"] == 11520
    assert all(x["status"] in OC.STATUSES for r in s["results"] for x in r["summands"])
