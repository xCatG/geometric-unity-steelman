"""B03 runner: writes experiments/B03/result.json (tests 0, 3, 4 summaries and 5-8 data).

Draft comparisons are recorded, not asserted: a mismatch is a finding (ansatz verdict rules).
Implementation gates (fixture equality, projector algebra) are asserted: a failure is a bug.
"""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

from experiments.B03 import branching as br
from experiments.B03 import source_tables as src
from experiments.B03.oracle import polynomial
from gu import rarita as ra

OUT = Path(__file__).with_name("result.json")


def git_commit() -> str:
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "gu", "experiments/B03", "tests"],
                           capture_output=True, text=True, check=True).stdout.strip()
    dirty = "\n".join(ln for ln in dirty.splitlines() if not ln.endswith("result.json"))
    if dirty:
        raise SystemExit(f"uncommitted producing code:\n{dirty}")
    return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


def matrix_rows() -> list[dict]:
    """The shared implementation gate (gu.rarita.verify_split) on every split's production Q."""
    rows = []
    for key, (p, q, _, _) in ra.SPLITS.items():
        row = ra.verify_split(key)
        if p + q == 14:
            partners = br.j_partner_map(ra.j_weight_signs(key))
            row["J_partners"] = sorted([br.block_name(a), br.block_name(b)] for a, b in partners.items())
        rows.append(row)
    return rows


def main() -> None:
    commit = git_commit()
    for title, hw in [("RSplus branch", br.RS_PLUS), ("RSminus branch", br.RS_MINUS),
                      ("Splus branch", br.S_PLUS), ("Sminus branch", br.S_MINUS)]:
        assert br.restricted(hw) == polynomial(title), title
    inv = br.fibre_inventory()
    result = {
        "scope": "identity (finite characters; explicit matrices on a finite generator set)",
        "dictionary": "ansatz rev 1.1 (GU-recon): 2+=L, 16+=16, 6+=(3,2), 144+=Hbar, 64-=S+, 832+-=RS+-",
        "embedding": "E: n = 6Y via SU(5) (ansatz rev 1.1); E' control",
        "matrix": matrix_rows(),
        "draft_p51": br.check_diagram(),
        "draft_12_20": br.check_12_20(),
        "draft_full_dirac": br.check_full_dirac(),
        "tables": {"p52_left": br.compare_table(src.TABLE_P52_LEFT),
                   "p52_cousin": br.compare_table(src.TABLE_P52_COUSIN),
                   "p53": br.compare_table(br.p53_rows())},
        "e_equals_e_prime": br.e_equals_e_prime(),
        "imposter_data": br.imposter_records(),
        "su5_x_parent_labels": {name: br.su5_labels(hw) for hw, name in br.D5_NAMES.items()},
        "fibre_inventory": sorted([list(k), m] for k, m in inv.items()),
        "fibre_dimension": sum(m * br.D5.dimension(k[:5]) * (k[5] + 1) * (k[6] + 1)
                               for k, m in inv.items()),
        "chirality_index": {str(k): v for k, v in br.chirality_index(inv).items()},
        "versions": {"python": sys.version.split()[0], "lie": "2.2.2+dfsg-3build3 (fixture)"},
        "source_commit": commit,
        "command": "uv run python -m experiments.B03.run",
    }
    OUT.write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
