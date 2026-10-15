"""GU draft data for B03, typed by Claude from the PDF (transcription.md rev 1). Not computed.

Labels are the draft's. The dictionary to abstract irreps lives in branching.py (ansatz rev 1),
never here.
"""

# (11.6): block -> list of (Lorentz label, internal label)
BLOCKS = {
    "F+": [("2-", "16+"), ("2+", "16-")],
    "F-": [("2+", "16+"), ("2-", "16-")],
    "Q+": [("6-", "16+"), ("6+", "16-")],
    "Q-": [("6+", "16+"), ("6-", "16-")],
    "Z+": [("2-", "144+"), ("2+", "144-")],
    "Z-": [("2+", "144+"), ("2-", "144-")],
}

# p. 51: field -> (bundle chirality of the spinor factor, form degree, {printed module: blocks})
DIAGRAM = {
    "zeta-": ("S-", 1, {"832-": ["Z-", "Q+", "F-"], "64-": ["F-"]}),
    "zeta+": ("S+", 1, {"832+": ["F+", "Q-", "Z+"], "64+": ["F+"]}),
    "nu+": ("S+", 0, {"64-": ["F-"]}),
    "nu-": ("S-", 0, {"64+": ["F+"]}),
}

# (12.20): Weyl half of Y -> list of (S^2 label on X, S^16 label on N)
EQ_12_20 = {
    "S_L": [("L", "L"), ("R", "R")],
    "S_R": [("L", "R"), ("R", "L")],
}

# p. 52 first table ("Left" one-generation): (SU3, SU2 dim, n, multiplicity)
TABLE_P52_LEFT = [("3", 2, 1, 1), ("3b", 1, 2, 1), ("3b", 1, -4, 1),
                  ("1", 2, -3, 1), ("1", 1, 6, 1), ("1", 1, 0, 1)]

# p. 52 second table (the Q+_{3/2} "cousin" generation)
TABLE_P52_COUSIN = [("3b", 2, -1, 1), ("3", 1, -2, 1), ("3", 1, 4, 1),
                    ("1", 2, 3, 1), ("1", 1, -6, 1), ("1", 1, 0, 1)]

# p. 53 (25 printed rows, in printed order): (number, multiplicity, SU3, SU2 dim, n, name)
TABLE_P53 = [
    (1, 1, "8", 2, -3, ""), (2, 1, "8", 1, 0, ""), (3, 1, "8", 1, 6, ""),
    (6, 1, "6b", 2, 1, ""), (5, 1, "6", 1, 2, ""), (4, 1, "6", 1, -4, ""),
    (12, 1, "3b", 3, 2, ""), (11, 1, "3b", 3, -4, ""), (8, 1, "3", 2, 7, ""),
    (7, 1, "3", 2, -5, ""), (20, 1, "3", 2, 1, ""),
    (13, 1, "3b", 2, 5, ""), (10, 1, "3", 1, -2, ""), (9, 1, "3", 1, -8, ""),
    (20, 2, "3", 2, 1, "Imposter Quarks"), (18, 2, "3b", 1, 2, "Imposter Anti-Quarks"),
    (19, 2, "3b", 1, -4, "Imposter Anti-Quarks"),
    (15, 1, "1", 3, 6, ""), (16, 1, "1", 2, -9, ""), (23, 1, "1", 1, 0, "Imposter Anti-Neutrino"),
    (14, 1, "1", 3, 0, ""), (21, 1, "1", 2, -3, "Imposter Leptons"),
    (22, 1, "1", 1, 6, "Imposter Anti-Electron"),
    (17, 1, "1", 2, 3, ""), (21, 1, "1", 2, -3, ""),
]
