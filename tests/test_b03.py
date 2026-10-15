"""B03 tests 5-8: draft identities, Standard-Model tables, imposter data, mirror inventory.

Provenance (P3, plan review finding 3):
- The `*_lie_directly` tests are the expected values. They compare the draft rows
  (source_tables, typed from the PDF) with the external LiE fixture, and import neither
  branching nor reps.
- The other tests are regression checks of branching.py. They agree with the direct tests,
  and the outcomes they pin were first seen in Claude's plan smoke test (ansatz ledger).
"""
from collections import Counter

from experiments.B03 import branching as br
from experiments.B03 import source_tables as src
from experiments.B03.oracle import polynomial

# The ansatz rev 1.1 dictionary, restated here independently of branching.py.
# Keys are LiE D5A1A1 labels (D5 Dynkin, A1_L, A1_R).
_LOR = {"2+": (1, 0), "2-": (0, 1), "6+": (2, 1), "6-": (1, 2)}
_INT = {"16+": (0, 0, 0, 0, 1), "16-": (0, 0, 0, 1, 0), "144+": (1, 0, 0, 1, 0), "144-": (1, 0, 0, 0, 1)}
_MOD = {"64-": "Splus branch", "64+": "Sminus branch", "832+": "RSplus branch", "832-": "RSminus branch"}
_SU3 = {"1": (0, 0), "3": (1, 0), "3b": (0, 1), "6": (2, 0), "6b": (0, 2), "8": (1, 1)}


def _aggregate(rows) -> Counter:
    out = Counter()
    for su3, su2, n, mult in rows:
        out[_SU3[su3] + (su2 - 1, n)] += mult
    return out


def test_source_tables_are_as_transcribed():
    """Control: 25 p.53 rows, 6+6 p.52 rows, total dimension 144 (transcription rev 1)."""
    assert len(src.TABLE_P53) == 25 and len(src.TABLE_P52_LEFT) == len(src.TABLE_P52_COUSIN) == 6
    dims = {"1": 1, "3": 3, "3b": 3, "6": 6, "6b": 6, "8": 8}
    assert sum(mult * dims[s3] * s2 for _, mult, s3, s2, _, _ in src.TABLE_P53) == 144


def test_tables_equal_lie_directly():
    """Claim (identity, test 6; expected values): aggregated draft rows equal LiE's restrictions
    under E: p.52 left = 16, p.52 cousin = 16bar, p.53 = Hbar (23 terms, no missing/extra)."""
    p53 = [(s3, s2, n, m) for _, m, s3, s2, n, _ in src.TABLE_P53]
    assert _aggregate(src.TABLE_P52_LEFT) == polynomial("SM 16")
    assert _aggregate(src.TABLE_P52_COUSIN) == polynomial("SM 16bar")
    assert _aggregate(p53) == polynomial("SM Hbar") and len(_aggregate(p53)) == 23
    assert _aggregate(p53) != polynomial("SM H")


def test_p51_blocks_equal_lie_directly():
    """Claim (identity, test 5; expected values): under the dictionary each printed p.51 module
    equals LiE's branch of the corresponding D7 irrep, block by block."""
    for field, (bundle, degree, modules) in src.DIAGRAM.items():
        for module, names in modules.items():
            printed = Counter()
            for name in names:
                for lor, inn in src.BLOCKS[name]:
                    printed[_INT[inn] + _LOR[lor]] += 1
            assert printed == polynomial(_MOD[module]), (field, module)


def test_p53_aggregation_sums_repeated_rows():
    """Claim (R4): repeated rows are summed, 25 rows -> 23 terms; (3,2)_1 has 3, (1,2)_-3 has 2."""
    agg = br.table_character(br.p53_rows())
    assert len(agg) == 23
    assert agg[((1, 0), (1,), (1,))] == 3  # Imposter quark rows 20 (mult 1) and 20 (mult 2)
    assert agg[((0, 0), (1,), (-3,))] == 2


def test_dictionary_reproduces_every_p51_block():
    """Regression (test 5): branching.check_diagram agrees, including each whole fibre."""
    rows = br.check_diagram()
    assert len(rows) == 10 and all(r["holds"] for r in rows)


def test_full_dirac_identities_are_convention_free():
    """Claim (identity, test 5): (11.2) and (11.3)/(12.22) hold on full modules; the S(TX)xS(N)
    term is contained in the full RS module."""
    assert br.check_full_dirac() == {"11.2": True, "11.3/12.22": True,
                                     "12.22 imposter term S(TX)xS(N)": True}


def test_12_20():
    """Claim (identity, test 5): (12.20) with S_L^64 = S+, 2_L = L, 16_L = 16."""
    assert br.check_12_20() == {"S_L": True, "S_R": True}


def test_tables_regression():
    """Regression (test 6): branching.compare_table agrees with the direct LiE comparison."""
    assert br.compare_table(src.TABLE_P52_LEFT)["equals"] == ["16"]
    assert br.compare_table(src.TABLE_P52_COUSIN)["equals"] == ["16b"]
    p53 = br.compare_table(br.p53_rows())
    assert p53["equals"] == ["Hb"] and p53["dimension"] == 144


def test_su5_parent_labels_match_lie():
    """Claim (identity): SU(5) x U(1)_X labels of 16, 16bar, H, Hbar equal LiE's."""
    for hw, name in br.D5_NAMES.items():
        title = {"16": "SU5 16", "16b": "SU5 16bar", "H": "SU5 H", "Hb": "SU5 Hbar"}[name]
        lie = sorted([list(k[:4]), k[4], m] for k, m in polynomial(title).items())
        assert br.su5_labels(hw) == lie


def test_imposter_records():
    """Data (test 7): per ambient chirality, the four spin-1/2 blocks of RS with carrier, D5
    parent and pattern counts. In RS+ the blocks with one complete pattern are (R;16) [F] and
    (R;Hbar) [Z]; containment does not locate an 'imposter' (ansatz R5)."""
    recs = br.imposter_records()
    assert len(recs) == 8
    full = {(r["ambient"], r["candidate"], r["lorentz"], r["d5"]) for r in recs if r["max_copies"] == 1}
    assert full == {("RS+", "F", "R", "16"), ("RS+", "Z", "R", "Hb"),
                    ("RS-", "F", "L", "16"), ("RS-", "Z", "L", "Hb")}


def test_j_partners_are_conjugate_pairs():
    """Claim (identity, test 8): for each 14D split, J maps (a,b;lambda) to (b,a;lambda-bar),
    an involution preserving multiplicities."""
    from gu.rarita import SPLITS, j_weight_signs
    conj = {"16": "16b", "16b": "16", "H": "Hb", "Hb": "H"}
    swap = {"L": "R", "R": "L", "(3,2)": "(2,3)", "(2,3)": "(3,2)"}
    for key, (p, q, _, _) in SPLITS.items():
        if p + q != 14:
            continue
        for a, b in br.j_partner_map(j_weight_signs(key)).items():
            lor, d5 = br.block_name(a).split(";")
            assert br.block_name(b) == f"{swap[lor]};{conj[d5]}", (key, a, b)


def test_mirror_inventory():
    """Data (test 8): nu + zeta over both chiralities has dimension 1920; each spin-1/2 (L|R) x
    (16|16bar) block 3 times, each RS-type block once; chi = 0 for every D5 irrep."""
    inv = br.fibre_inventory()
    assert sum(m * br.D5.dimension(k[:5]) * (k[5] + 1) * (k[6] + 1) for k, m in inv.items()) == 1920
    for lam in (br.D5_16, br.D5_16B):
        assert inv[lam + (1, 0)] == inv[lam + (0, 1)] == 3
    assert set(br.chirality_index(inv).values()) == {0}
