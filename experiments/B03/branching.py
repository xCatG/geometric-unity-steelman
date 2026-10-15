"""B03 tests 5-8: draft identities, Standard-Model tables, imposter data, mirror inventory.

Abstract irreps are reps.py characters; restricted blocks are keys (D5 labels, A1_L, A1_R).
The dictionary from draft labels to irreps is ansatz rev 1 and appears only here.
"""
from collections import Counter

from gu.reps import Product, Simple, d7_to_d5a1a1, dn_doubled, sm_weight, sm_weight_flipped
from experiments.B03 import source_tables as src

D7, D5, A1, A2 = Simple("D", 7), Simple("D", 5), Simple("A", 1), Simple("A", 2)
TARGET = Product([D5, A1, A1])
SM = Product([A2, A1], u1=1)

V14, S_PLUS, S_MINUS = (1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1, 0)
RS_PLUS, RS_MINUS = (1, 0, 0, 0, 0, 0, 1), (1, 0, 0, 0, 0, 1, 0)
D5_16, D5_16B, D5_H, D5_HB = (0, 0, 0, 0, 1), (0, 0, 0, 1, 0), (1, 0, 0, 0, 1), (1, 0, 0, 1, 0)

# Ansatz rev 1 dictionary (GU-recon): draft label -> abstract label
LORENTZ = {"2+": (1, 0), "2-": (0, 1), "6+": (2, 1), "6-": (1, 2)}      # (A1_L, A1_R) Dynkin
INTERNAL = {"16+": D5_16, "16-": D5_16B, "144+": D5_HB, "144-": D5_H}
MODULE = {"64-": S_PLUS, "64+": S_MINUS, "832+": RS_PLUS, "832-": RS_MINUS}
BUNDLE = {"S+": S_PLUS, "S-": S_MINUS}
HALF_12_20 = {"S_L": S_PLUS, "S_R": S_MINUS}
X_12_20 = {"L": (1, 0), "R": (0, 1)}
N_12_20 = {"L": D5_16, "R": D5_16B}


def restricted(hw) -> Counter:
    """Multiplicities of (D5 labels, A1_L, A1_R) blocks in the D7 irrep hw."""
    return Counter({k[0][0] + k[0][1] + k[0][2]: m
                    for k, m in TARGET.decompose(d7_to_d5a1a1(D7.character(hw))).items()})


def block_key(lorentz: tuple[int, int], internal) -> tuple:
    return tuple(internal) + lorentz


def draft_blocks(names) -> Counter:
    out = Counter()
    for name in names:
        for lor, inn in src.BLOCKS[name]:
            out[block_key(LORENTZ[lor], INTERNAL[inn])] += 1
    return out


def check_diagram() -> list[dict]:
    """Test 5, p. 51 and (11.1): each printed module equals its blocks; trace has opposite chirality."""
    rows = []
    vs = {k: Counter() for k in BUNDLE}
    for b, hw in BUNDLE.items():
        vs[b] = TARGET.decompose(d7_to_d5a1a1(_tensor_d7(V14, hw)))
    for field, (bundle, degree, modules) in src.DIAGRAM.items():
        total = Counter()
        for module, names in modules.items():
            computed = restricted(MODULE[module])
            printed = draft_blocks(names)
            rows.append({"field": field, "module": module, "blocks": names,
                         "holds": computed == printed})
            total += computed
        expected = restricted(BUNDLE[bundle]) if degree == 0 else _flatten(vs[bundle])
        rows.append({"field": field, "module": "whole fibre", "holds": total == expected})
    return rows


def _tensor_d7(a, b) -> Counter:
    from gu.reps import tensor
    return tensor(D7.character(a), D7.character(b))


def _flatten(decomp) -> Counter:
    return Counter({k[0][0] + k[0][1] + k[0][2]: m for k, m in decomp.items()})


def check_12_20() -> dict:
    out = {}
    for half, pairs in src.EQ_12_20.items():
        printed = Counter(block_key(X_12_20[x], N_12_20[n]) for x, n in pairs)
        out[half] = restricted(HALF_12_20[half]) == printed
    return out


def check_full_dirac() -> dict:
    """(11.2) and (11.3)/(12.22) on full (non-chiral) modules: convention-free."""
    s_x = [(1, 0), (0, 1)]
    r_x = [(2, 1), (1, 2)]
    s_n, r_n = [D5_16, D5_16B], [D5_H, D5_HB]
    prod = lambda xs, ns: Counter(block_key(x, n) for x in xs for n in ns)
    full_s = restricted(S_PLUS) + restricted(S_MINUS)
    full_rs = restricted(RS_PLUS) + restricted(RS_MINUS)
    rhs = prod(r_x, s_n) + prod(s_x, r_n) + prod(s_x, s_n)
    return {"11.2": full_s == prod(s_x, s_n), "11.3/12.22": full_rs == rhs,
            "12.22 imposter term S(TX)xS(N)": prod(s_x, s_n) <= full_rs}


# ---- Standard-Model tables (test 6)

SU3 = {"1": (0, 0), "3": (1, 0), "3b": (0, 1), "6": (2, 0), "6b": (0, 2), "8": (1, 1)}


def sm_character(d5_hw, embed=sm_weight) -> Counter:
    ch = Counter()
    for w, m in D5.character(d5_hw).items():
        ch[embed(dn_doubled(w))] += m
    return Counter({(k[0][0], k[0][1], k[1]): m for k, m in SM.decompose(ch).items()})


def table_character(rows) -> Counter:
    """Aggregate source rows by (SU3, SU2, n); rows are (su3, su2dim, n, mult)."""
    out = Counter()
    for su3, su2, n, mult in rows:
        out[(SU3[su3], (su2 - 1,), (n,))] += mult
    return out


def p53_rows():
    return [(su3, su2, n, mult) for _, mult, su3, su2, n, _ in src.TABLE_P53]


def compare_table(rows) -> dict:
    printed = table_character(rows)
    result = {"aggregated_terms": len(printed), "dimension": _sm_dim(printed), "equals": []}
    for name, hw in [("16", D5_16), ("16b", D5_16B), ("H", D5_H), ("Hb", D5_HB)]:
        c = sm_character(hw)
        if c == printed:
            result["equals"].append(name)
        result[f"vs_{name}"] = {"missing": _fmt(printed - c), "extra": _fmt(c - printed)}
    return result


def _sm_dim(ch) -> int:
    return sum(m * A2.dimension(k[0]) * A1.dimension(k[1]) for k, m in ch.items())


def _fmt(ch) -> list:
    return sorted([list(k[0]), k[1][0], k[2][0], m] for k, m in ch.items())


def e_equals_e_prime() -> bool:
    return all(sm_character(hw) == sm_character(hw, sm_weight_flipped)
               for hw in (D5_16, D5_16B, D5_H, D5_HB))


# ---- imposter data (test 7)

GENERATION = {"Q": ((1, 0), (1,), (1,)), "dc": ((0, 1), (0,), (2,)), "uc": ((0, 1), (0,), (-4,)),
              "L": ((0, 0), (1,), (-3,)), "ec": ((0, 0), (0,), (6,)), "nuc": ((0, 0), (0,), (0,))}


def generation_counts(d5_hw) -> dict:
    c = sm_character(d5_hw)
    mult = {k: c[v] for k, v in GENERATION.items()}
    return {"multiplicities": mult, "max_copies": min(mult.values())}


# SU(5) x U(1)_X parent labels: LiE's reversed-A4 restriction matrix (oracle.lie, "r");
# its charge column equals X = sum of doubled D5 coordinates on every fundamental weight.
R_SU5 = [[0, 0, 0, 1, 2], [0, 0, 1, 0, 4], [0, 1, 0, 0, 6], [1, 0, 0, 0, 3], [0, 0, 0, 0, 5]]
A4 = Simple("A", 4)
D5_NAMES = {D5_16: "16", D5_16B: "16b", D5_H: "H", D5_HB: "Hb"}
LORENTZ_NAMES = {(1, 0): "L", (0, 1): "R", (2, 1): "(3,2)", (1, 2): "(2,3)"}


def block_name(key) -> str:
    """'(A1_L x A1_R carrier; D5 name)', e.g. 'L;16' or '(3,2);Hb'."""
    return f"{LORENTZ_NAMES[key[5:]]};{D5_NAMES[key[:5]]}"


def su5_labels(d5_hw) -> list:
    from gu.reps import restrict
    dec = Product([A4], u1=1).decompose(restrict(D5.character(d5_hw), R_SU5))
    return sorted([list(parts[0]), q[0], m] for (parts, q), m in dec.items())


def imposter_records() -> list[dict]:
    """Test 7 (data only): every spin-1/2 block of RS_+- (F: D5 in 16/16bar; Z: D5 in H/Hbar),
    keyed by ambient chirality, candidate, Lorentz carrier and D5 parent. Complex data are the
    same for all three 14D splits."""
    rows = []
    for amb, hw in (("RS+", RS_PLUS), ("RS-", RS_MINUS)):
        for key, m in sorted(restricted(hw).items()):
            lam, lor = key[:5], key[5:]
            if lor not in ((1, 0), (0, 1)):
                continue
            cand = "F" if lam in (D5_16, D5_16B) else "Z" if lam in (D5_H, D5_HB) else None
            assert cand is not None, key
            rows.append({"ambient": amb, "candidate": cand, "lorentz": LORENTZ_NAMES[lor],
                         "d5": D5_NAMES[lam], "multiplicity": m, **generation_counts(lam)})
    return rows


def _block_doubled_character(key) -> Counter:
    """Character of the D2 x D5 block (D5 labels, A1_L, A1_R) in doubled D7 coordinates."""
    lam, (l, r) = key[:5], key[5:]
    out = Counter()
    for w5, m5 in D5.character(lam).items():
        y5 = dn_doubled(w5)
        for (a,), ma in A1.character((l,)).items():
            for (b,), mb in A1.character((r,)).items():
                out[(a + b, a - b) + y5] += m5 * ma * mb
    return out


def j_partner_map(sigma) -> dict:
    """Test 8: image of every fibre block under J, whose weight action is sigma (gu.rarita)."""
    from gu.reps import split_14
    inv = fibre_inventory()
    partner = {}
    for key in inv:
        moved = Counter()
        for y, m in _block_doubled_character(key).items():
            moved[split_14(tuple(s * x for s, x in zip(sigma, y)))] += m
        dec = TARGET.decompose(moved)
        assert len(dec) == 1 and sum(dec.values()) == 1, (key, dec)
        (parts, _), = dec
        partner[key] = parts[0] + parts[1] + parts[2]
    assert all(partner[partner[k]] == k for k in partner), "J partner map is not an involution"
    assert all(inv[k] == inv[partner[k]] for k in partner), "J does not preserve multiplicities"
    return partner


# ---- mirror inventory (test 8)

def fibre_inventory() -> Counter:
    """nu (S+ + S-) plus zeta (V x (S+ + S-)), restricted to D2 x D5."""
    inv = restricted(S_PLUS) + restricted(S_MINUS)
    for hw in (S_PLUS, S_MINUS):
        inv += _flatten(TARGET.decompose(d7_to_d5a1a1(_tensor_d7(V14, hw))))
    return inv


def chirality_index(inv: Counter) -> dict:
    """chi(lambda) = mult(L, lambda) - mult(R, lambda): a complex-fibre diagnostic only."""
    out = {}
    for key, m in inv.items():
        lam, lor = key[:5], key[5:]
        if lor == (1, 0):
            out[lam] = out.get(lam, 0) + m
        elif lor == (0, 1):
            out[lam] = out.get(lam, 0) - m
    return out
