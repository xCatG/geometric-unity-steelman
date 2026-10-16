"""B05 Task 4: spinor-label and form-degree bookkeeping for the draft's operator (9.16), over an enumerated branch set.

Pure bookkeeping on Claude's typed transcription (`source_operator.py`); no numerics, no verdict on any
symmetry. Each printed summand gets a label status and a degree status under one branch, i.e. one reading of
something the draft leaves open. The statuses describe THIS MODEL: readings that no axis below enumerates
(transcription.md, branches B05-Q and others) can change them. The runner records every branch and asserts none.
"""
from __future__ import annotations

from itertools import product

from experiments.B05 import source_operator as SRC
from gu.cliffform import exact

LABEL = ("chirality", "signature")          # +/- = eigenvalue of C, or of a candidate U(64,64) form A
ORDER = ("target_source", "source_target")  # varpi_{ab}: a is the target label, or the source label
BAR = ("dirac_adjoint", "dual_field")       # pairs opposite labels, or equal labels (see pairs_with)
ADJ = ("a_adjoint", "subscript_swap")       # varpibar*_{ab}: A-adjoint of varpi_{ab}, or varpi with a, b swapped
HOM = ("strict", "extend_by_zero")          # a block outside its domain is a type error, or the zero map there
PAIR = ("wedge", "metric")                  # <psibar, X>: psibar ^ X is top degree, or deg psibar == deg X
D0KIND = ("exterior", "clifford")           # d0: exterior covariant derivative, or Clifford-contracted (Dirac-type)
STARPARSE = ("extra_star", "outer_star")    # printed "*(circledcirc)": a further *, or (8.1)'s own *^n with n = 1
SHIAB_M = (0, 1)                            # (8.1): *^m inside the bracket
SHIAB_N = (0, 1)                            # (8.1): *^n outside it (fixed to 1 under outer_star)
SHIAB_R = tuple(range(15))                  # form degree r of Phi_r; Definition 8.1 / (8.6)-(8.7), pp. 41-42, run to 14

BOTH = frozenset("+-")
STATUSES = ("nonzero", "pairs_to_zero", "extended_zero", "undetermined", "domain_mismatch")


def as_int(x) -> int:
    """P4 boundary: exact integers only (numpy ints accepted, floats and non-integral rationals rejected)."""
    f = exact(x)
    if f.denominator != 1:
        raise ValueError(f"integer required, got {f}")
    return int(f.numerator)


def flip(s: str) -> str:
    return "-" if s == "+" else "+"


def pairs_with(row_label: str, label: str, bar: str) -> str:
    """Label of the vectors a row field pairs nontrivially with.

    Both candidate forms A anticommute with C at (7,7) and (9,5) (`pairing.py`), so under the chirality reading the
    Dirac adjoint of psi_s, labelled by s ("dirac_adjoint"), pairs opposite labels. "dual_field" pairs equal labels;
    combinatorially this also covers the Dirac adjoint labelled by its OWN right C-eigenvalue, zetabar_- :=
    (zeta_+)^dagger A (then zetabar_- C = -zetabar_-), which matches the row/column order of (9.16). A preserves its
    own eigenspaces, so under the signature reading both conventions pair equal labels.
    """
    if bar == "dirac_adjoint" and label == "chirality":
        return flip(row_label)
    return row_label


def varpi_map(op, label: str, order: str, adj: str) -> tuple[str, str]:
    """(source label, target label) of a varpi or varpibar_star block."""
    a, b = op[1], op[2]
    src, tgt = (b, a) if order == "target_source" else (a, b)
    if op[0] == "varpibar_star":
        if adj == "subscript_swap":
            src, tgt = tgt, src
        elif label == "chirality":                   # A-adjoint of src -> tgt is (-tgt) -> (-src) when AC = -CA
            src, tgt = flip(tgt), flip(src)
        else:                                        # A preserves its eigenspaces: tgt -> src
            src, tgt = tgt, src
    return src, tgt


def apply_label(op, support: frozenset, known: bool, br: dict) -> tuple[frozenset, bool]:
    """Possible output labels, and whether that support is established (False = only a possible support)."""
    if not support:
        return support, known                        # zero stays zero
    kind = op[0]
    if kind in ("star", "shiab"):
        return support, known                        # acts on the form factor only (branch B05-Q: assumed)
    if kind in ("d0", "d0star"):
        if br["label"] == "signature":
            return BOTH, False                       # may or may not leave A's eigenspaces; not established
        return (frozenset(map(flip, support)) if br["d0kind"] == "clifford" else support), known
    if kind == "endo":                               # control-only degree-0 block: (target, source)
        return (frozenset({op[1]}) if op[2] in support else frozenset()), known
    if kind in ("varpi", "varpibar_star"):
        src, tgt = varpi_map(op, br["label"], br["order"], br["adj"])
        return (frozenset({tgt}) if src in support else frozenset()), known
    raise ValueError(f"unknown primitive {op!r}")


def degree(op, k, br: dict, n_override=None) -> int:
    k, d = as_int(k), SRC.D
    kind = op[0]
    if kind == "star":
        return d - k
    if kind == "endo":
        return k
    if kind in ("d0", "d0star") and br["d0kind"] == "clifford":
        return k                                     # c(e^i) nabla_i acts on the spinor factor
    if kind in ("d0", "varpi"):
        return k + 1
    if kind in ("d0star", "varpibar_star"):
        return k - 1
    if kind == "shiab":                              # (8.1): *^n [Phi_r ^ *^m eta]
        m, r = as_int(br["m"]), as_int(br["r"])
        n = as_int(br["n"] if n_override is None else n_override)
        k = d - k if m else k
        k += r
        return d - k if n else k
    raise ValueError(f"unknown primitive {op!r}")


def parse(term, br: dict) -> list[tuple]:
    """Apply STARPARSE: under outer_star a star immediately left of shiab is (8.1)'s *^n, not a further star."""
    term = list(term)
    if br["starparse"] == "outer_star":
        out = []
        for op in term:
            if op[0] == "shiab" and out and out[-1][0] == "star":
                out.pop()
                op = ("shiab", "outer")
            out.append(op)
        term = out
    return term


def summand(term, row, col, br, rows=None, cols=None) -> tuple[str, bool]:
    """(label status, degree_ok) for one printed summand; primitives compose right to left."""
    rows, cols = rows or SRC.ROWS, cols or SRC.COLS
    k, support, known = as_int(cols[col][0]), frozenset({cols[col][1]}), True
    for op in reversed(parse(term, br)):
        if not support:
            break
        support, known = apply_label(op, support, known, br)
    k = as_int(cols[col][0])
    for op in reversed(parse(term, br)):
        k = degree(op, k, br, 1 if op == ("shiab", "outer") else None)
    want = pairs_with(rows[row][1], br["label"], br["bar"])
    if not support:
        status = "domain_mismatch" if br["hom"] == "strict" else "extended_zero"
    elif not known:
        status = "undetermined"
    elif want not in support:
        status = "pairs_to_zero"                     # legal, but the printed summand vanishes identically
    elif support == {want}:
        status = "nonzero"
    else:
        status = "undetermined"
    kr = as_int(rows[row][0])
    deg_ok = 0 <= k <= SRC.D and ((kr + k == SRC.D) if br["pair"] == "wedge" else kr == k)
    return status, deg_ok


KEYS = ("label", "order", "bar", "adj", "hom", "pair", "d0kind", "starparse", "m", "n", "r")


def branches() -> list[dict]:
    out = []
    for v in product(LABEL, ORDER, BAR, ADJ, HOM, PAIR, D0KIND, STARPARSE, SHIAB_M, SHIAB_N, SHIAB_R):
        br = dict(zip(KEYS, v))
        if br["starparse"] == "outer_star" and br["n"] != 1:
            continue                                 # n is fixed by the printed star under outer_star
        out.append(br)
    return out


def check(br: dict, entries=None, rows=None, cols=None) -> dict:
    entries = entries or SRC.ENTRIES
    out = []
    for (row, col), terms in entries.items():
        for sign, term in terms:
            sign = as_int(sign)
            if sign not in (1, -1):
                raise ValueError(f"summand sign must be +1 or -1, got {sign}")
            st, d = summand(term, row, col, br, rows, cols)
            out.append({"row": row, "col": col, "sign": sign, "term": term, "status": st, "degree_ok": d})
    return {"branch": br, "summands": out,
            "well_typed": all(x["status"] != "domain_mismatch" for x in out),
            "all_nonzero_under_model": all(x["status"] == "nonzero" for x in out),
            "degree_ok": all(x["degree_ok"] for x in out)}


def survey() -> dict:
    """Every branch, with model-relative predicates; recorded by the runner, never asserted."""
    results = [check(b) for b in branches()]
    return {"n_branches": len(results),
            "well_typed": [r["branch"] for r in results if r["well_typed"]],
            "all_nonzero_under_model": [r["branch"] for r in results if r["all_nonzero_under_model"]],
            "degree_ok": [r["branch"] for r in results if r["degree_ok"]],
            "results": results}
