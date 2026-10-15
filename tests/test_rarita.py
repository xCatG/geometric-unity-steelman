"""gu.rarita: Cartan adapter, RS projector, charge conjugation (B03 tests 0, 3, 4)."""
from collections import Counter
from itertools import product

import numpy as np
import pytest
from scipy import sparse as sp

from gu.rarita import (SPLITS, chirality_on_vs, chirality_vs_parity, contraction,
                       euclidean_conjugation_ok, generator, j_commutes_with_generators,
                       j_on_vs, j_preserves_chirality, j_square, j_weight_signs, projector_Q,
                       projector_controls,
                       rs_character, spin_weights, spinor_character, split_signatures,
                       verify_split)
from gu.clifford import gammas
from gu.reps import Simple, split_14, d7_to_d5a1a1

ALL = list(SPLITS)
D14 = [k for k in ALL if sum(SPLITS[k][:2]) == 14]
D7 = Simple("D", 7)
RS_HW = {1: (1, 0, 0, 0, 0, 0, 1), -1: (1, 0, 0, 0, 0, 1, 0)}
S_HW = {1: (0, 0, 0, 0, 0, 0, 1), -1: (0, 0, 0, 0, 0, 1, 0)}


def sig(key):
    return SPLITS[key][:2]


@pytest.mark.parametrize("key,expected", [
    ("7,7|1,3+6,4", ((1, 3), (6, 4))), ("9,5|1,3+8,2", ((1, 3), (8, 2))),
    ("9,5|3,1+6,4", ((3, 1), (6, 4))), ("3,1|1,1+2,0", ((1, 1), (2, 0)))])
def test_split_signatures(key, expected):
    """Control (ansatz rev 1.1 split table): the axis lists have the stated signatures."""
    assert split_signatures(key) == expected


@pytest.mark.parametrize("key", ALL)
def test_adapter_weights_are_the_dirac_character(key):
    """Claim (identity, test 0): JW-pair Cartans give every +-1 weight exactly once."""
    ws = spin_weights(key)
    assert Counter(ws) == Counter(product((1, -1), repeat=len(ws[0])))


@pytest.mark.parametrize("key,s", [("7,7|1,3+6,4", -1), ("9,5|1,3+8,2", 1),
                                   ("9,5|3,1+6,4", 1), ("3,1|1,1+2,0", 1)])
def test_library_chirality_versus_weight_parity(key, s):
    """Claim (identity, test 0): gu.clifford.chirality = s * Pi; s is signature-dependent."""
    assert chirality_vs_parity(key) == s


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_projector_algebra(p, q):
    """Claim (identity, test 3): Q^2 = dQ, gamma.Q = 0, tr Q = d(d-1) dim S, covariance."""
    d = p + q
    Q = projector_Q(p, q)
    assert (Q @ Q - d * Q).count_nonzero() == 0
    assert (contraction(p, q) @ Q).count_nonzero() == 0
    n = gammas(p, q)[0].n
    assert int(Q.diagonal().sum()) // 2 == d * (d - 1) * n           # realified: real part twice
    assert {(3, 1): 48, (7, 7): 23296, (9, 5): 23296}[(p, q)] == d * (d - 1) * n
    for a in range(d - 1):
        X = generator(p, q, a, a + 1)
        assert (Q @ X - X @ Q).count_nonzero() == 0


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_projector_per_chirality_trace(p, q):
    """Claim (identity, test 3): tr Q on each chirality is half: 11648 at d=14, 24 at d=4 (tr P = 832, 6)."""
    d, Q, C = p + q, projector_Q(p, q), chirality_on_vs(p, q)
    assert (Q @ C - C @ Q).count_nonzero() == 0
    total = int(Q.diagonal().sum()) // 2
    twisted = int((Q @ C).diagonal().sum()) // 2
    plus, minus = (total + twisted) // 2, (total - twisted) // 2
    assert plus == minus == {14: 11648, 4: 24}[d]
    assert plus // d == {14: 832, 4: 6}[d]


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_projector_is_not_vacuous(p, q):
    """Control (P2): P fixes a nonzero gamma-traceless vector and kills a gamma-inserted spinor."""
    d = p + q
    Q = projector_Q(p, q)
    T, W = projector_controls(p, q)  # built from the gammas, not from Q
    assert T.count_nonzero() and (contraction(p, q) @ T).count_nonzero() == 0
    assert (Q @ T - d * T).count_nonzero() == 0
    assert W.count_nonzero() and (Q @ W).count_nonzero() == 0


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_euclidean_frame_conjugation(p, q):
    """Claim (identity): c Q c^-1 = d - E_a E_b, which licenses reading characters in the E frame."""
    assert euclidean_conjugation_ok(p, q)


@pytest.mark.parametrize("key", D14)
@pytest.mark.parametrize("chir", [1, -1])
def test_matrix_characters_equal_abstract(key, chir):
    """Claim (identity, test 3): weight characters of S_chir and im Q on V x S_chir, read from the
    actual matrices through the adapter, equal reps.py's S and RS restricted to D2 x D5."""
    def restrict(ch):
        out = Counter()
        for w, m in ch.items():
            out[split_14(w)] += m
        return out
    assert restrict(spinor_character(key, chir)) == d7_to_d5a1a1(D7.character(S_HW[chir]))
    assert restrict(rs_character(key, chir)) == d7_to_d5a1a1(D7.character(RS_HW[chir]))
    assert sum(rs_character(key, chir).values()) == 832


@pytest.mark.parametrize("key", ALL)
def test_verify_split_gate(key):
    """Claim (identity, tests 0/3/4): the shared runner gate passes on the production Q."""
    row = verify_split(key)
    assert row["trace_Q"] == {14: 23296, 4: 48}[sum(SPLITS[key][:2])]


def _realified(complex_blocks: dict, dn: int):
    """Sparse realified matrix from {(row, col): (re, im)} plus 14 * identity."""
    re = sp.lil_matrix((dn, dn), dtype=np.int64)
    im = sp.lil_matrix((dn, dn), dtype=np.int64)
    for (r, c), (x, y) in complex_blocks.items():
        re[r, c] += x
        im[r, c] += y
    return sp.bmat([[re.tocsr(), -im.tocsr()], [im.tocsr(), re.tocsr()]], format="csr")


def test_character_gate_rejects_wrong_rank_832_projector():
    """Control (P2, review finding 1): W = 14 (I - P_u (x) I) with u = e_0 + i e_1 (an orthogonal
    projector, Euclidean pair (0,1) at (7,7)) satisfies W^2 = 14 W and has the RS trace, but its
    weight character is wrong; rs_character must read W and differ, and verify_split must fail."""
    key, (p, q) = "7,7|1,3+6,4", (7, 7)
    d, n = 14, 128
    blocks = {}
    for j in range(n):
        for a in range(d):
            blocks[(a * n + j, a * n + j)] = (14, 0)
        # -14 * P_u (x) I, P_u = (1/2) [[1, -i], [i, 1]] on vector indices (0, 1)
        blocks[(0 * n + j, 0 * n + j)] = (14 - 7, 0)
        blocks[(1 * n + j, 1 * n + j)] = (14 - 7, 0)
        blocks[(0 * n + j, 1 * n + j)] = (0, 7)
        blocks[(1 * n + j, 0 * n + j)] = (0, -7)
    W = _realified(blocks, d * n)
    assert (W @ W - d * W).count_nonzero() == 0
    assert int(W.diagonal().sum()) // 2 == 23296
    def restrict(ch):
        out = Counter()
        for w, m in ch.items():
            out[split_14(w)] += m
        return out
    assert restrict(rs_character(key, 1, W)) != d7_to_d5a1a1(D7.character(RS_HW[1]))
    with pytest.raises(AssertionError):
        verify_split(key, W)


def test_verify_split_rejects_zero_q():
    """Control (P2, review finding 1): the runner gate rejects Q = 0."""
    p, q = 7, 7
    with pytest.raises(AssertionError):
        verify_split("7,7|1,3+6,4", 0 * projector_Q(p, q))


def test_four_dimensional_rs_character():
    """Control (P5): at (3,1) each chirality's RS space has dimension 6 = 4*2 - 2."""
    assert [sum(rs_character("3,1|1,1+2,0", c).values()) for c in (1, -1)] == [6, 6]


@pytest.mark.parametrize("p,q,square", [(7, 7, 1), (9, 5, -1), (3, 1, -1)])
def test_charge_conjugation(p, q, square):
    """Claim (identity, test 4): J = B conj commutes with all Spin generators; J^2 = +1 (7,7),
    -1 (9,5) [lit: Figueroa-O'Farrill Table 2]; at d=14 J preserves chirality; JQ = QJ."""
    assert j_square(p, q) == square
    assert j_commutes_with_generators(p, q)
    assert j_preserves_chirality(p, q) == (p + q == 14)
    J, Q = j_on_vs(p, q), projector_Q(p, q)
    assert (J @ Q - Q @ J).count_nonzero() == 0


@pytest.mark.parametrize("key,sigma", [
    ("7,7|1,3+6,4", (1, -1, -1, -1, -1, -1, -1)), ("9,5|1,3+8,2", (1, -1, -1, -1, -1, -1, -1)),
    ("9,5|3,1+6,4", (-1, 1, -1, -1, -1, -1, -1))])
def test_j_exchanges_conjugate_pairs(key, sigma):
    """Claim (identity, test 4): J flips one horizontal coordinate (L <-> R on X) and all five
    normal coordinates (16 <-> 16bar), an even number of flips (ambient chirality kept)."""
    assert j_weight_signs(key) == sigma
