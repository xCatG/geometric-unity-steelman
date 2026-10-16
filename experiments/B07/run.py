"""B07 runner: writes experiments/B07/result.json.

Records, under reading V (transcription.md), the order-T^1 (C1) and order-T^2 (C2) residuals of the first variation of
(9.4) in the varpi direction against (9.7), for the whole Shiab family in 4D and for named branches in 14D. Draft
comparisons are recorded, not asserted: a nonzero residual is a finding about reading V, not a verdict on every reading.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

from experiments.B07 import variation as V

OUT = Path(__file__).with_name("result.json")
SIGS_4D = [(3, 1), (1, 3)]
SIGS_14D = [(7, 7), (9, 5)]


def git_commit() -> str:
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "gu", "experiments/B07", "tests"],
                           capture_output=True, text=True, check=True).stdout.strip()
    dirty = "\n".join(ln for ln in dirty.splitlines() if not ln.endswith("result.json"))
    if dirty:
        raise SystemExit(f"uncommitted producing code:\n{dirty}")
    return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


def main() -> None:
    commit = git_commit()
    t0 = time.time()
    family = []
    for p, q in SIGS_4D:
        for mode in V.MODES:
            row = V.survey(p, q, mode, with_c2=False)
            for norm in V.NORMS:
                c2 = V.survey(p, q, mode, norm, with_c2=True)
                row.setdefault("c2", {})[norm] = {k: c2[k] for k in ("c2_nonzero", "c2_kernel", "joint_kernel")}
            family.append(row)
            print(f"{p},{q} {mode}: C1 kernel dim {len(row['c1_kernel'])}", flush=True)
    witnesses = [V.c1_witness(name, p, q) for name in V.BRANCHES for p, q in SIGS_4D + SIGS_14D]
    result = {
        "scope": "identity (4D: exact kernels over the six Shiab-family monomials, every bracket mode); "
                 "counterexample (14D: one exact nonzero C1 entry per named branch)",
        "reading": "V (experiments/B07/transcription.md): eps, metric fixed; I1 = int Tr(T ^ X(F_B + 1/2 d_B T + "
                   "1/3 b(T,T))) + kappa/2 int Tr(T ^ *T); compared with (9.7)",
        "monomials": {"+".join(c): m for c, m in V.MONOMIALS.items()},
        "family_4d": family,
        "witnesses_c1": witnesses,
        "seconds": round(time.time() - t0, 1),
        "source_commit": commit,
    }
    OUT.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT}: {len(family)} family rows, {sum(w is not None for w in witnesses)} witnesses")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
