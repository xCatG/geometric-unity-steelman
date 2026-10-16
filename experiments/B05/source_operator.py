"""Claude's typed transcription of GU (9.16), p. 46 (April 1, 2021 draft). Do not edit without a transcription revision.

Fields: (form degree, label). zeta, zetabar in Omega^1(Y, $); nu, nubar in Omega^0(Y, $). d = dim Y = 14.
Row vector (zetabar_-, zetabar_+, nubar_-, nubar_+) decorated rho(epsilon); column vector
(zeta_+, zeta_-, nu_+, nu_-) decorated rho(epsilon^-1). The decorations are carried by transcription.md only.
An entry is a tuple of (sign, summand); a summand is a tuple of primitives, composed right to left.
The printed "*(circledcirc)" is stored as (star, shiab); operator_check branches on whether that star is
an extra Hodge star or the outer *^n of (8.1). The lower-right 2x2 is zero as printed ("other versions" with a
non-trivial lower-right map exist, p. 46, and are not typed here).
"""
D = 14

ROWS = {"zb-": (1, "-"), "zb+": (1, "+"), "nb-": (0, "-"), "nb+": (0, "+")}
COLS = {"z+": (1, "+"), "z-": (1, "-"), "n+": (0, "+"), "n-": (0, "-")}

S, SH, D0, D0S = ("star",), ("shiab",), ("d0",), ("d0star",)


def W(a, b):
    return ("varpi", a, b)


def WS(a, b):
    return ("varpibar_star", a, b)


ENTRIES = {
    ("zb-", "z+"): ((+1, (S, SH, W("+", "+"))),),
    ("zb-", "z-"): ((+1, (S, SH, D0)), (+1, (S, SH, W("+", "-")))),
    ("zb-", "n+"): ((+1, (W("+", "+"),)),),
    ("zb-", "n-"): ((+1, (D0,)), (+1, (W("+", "-"),))),
    ("zb+", "z+"): ((+1, (S, SH, D0)), (+1, (S, SH, W("-", "+")))),
    ("zb+", "z-"): ((+1, (S, SH, W("-", "-"))),),
    ("zb+", "n+"): ((+1, (D0,)), (+1, (W("-", "+"),))),
    ("zb+", "n-"): ((+1, (W("-", "-"),)),),
    ("nb-", "z+"): ((-1, (WS("+", "+"),)),),
    ("nb-", "z-"): ((-1, (D0S,)), (-1, (WS("+", "-"),))),
    ("nb+", "z+"): ((-1, (D0S,)), (-1, (WS("-", "+"),))),
    ("nb+", "z-"): ((-1, (WS("-", "-"),)),),
}
