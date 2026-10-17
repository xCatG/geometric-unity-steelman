"""14D E2 witnesses runner: writes experiments/B07/escape/result14.json. Run: uv run python -m experiments.B07.escape.run14

witness14.py: bounded Weyl-leak witnesses of the dressed Shiab operator at (7,7) and (9,5), with covariance control.
"""
import json
import subprocess
import time
from pathlib import Path

from experiments.B07.escape import witness14 as W
from experiments.B07.escape.run import jsonable

OUT = Path(__file__).with_name("result14.json")
OUT_REL = "experiments/B07/escape/result14.json"
PRODUCERS = ("gu", "experiments/B02", "experiments/B07", "tests", "pyproject.toml", "uv.lock")
SCOPE = ("counterexample: 14D point, two Ricci-flat algebraic-curvature inputs per signature, eight named "
         "blade-Cayley dressings each (t = 1/2); reading V conventions of experiments/B07/phase2")


def dirty_paths(porcelain_z: str) -> list[str]:
    entries, dirty = iter(porcelain_z.split("\0")), []
    for e in entries:
        if not e:
            continue
        if set(e[:2]) & set("RC"):
            src = next(entries)
            if src != OUT_REL:
                dirty.append(src)
        if e[3:] != OUT_REL:
            dirty.append(e[3:])
    return dirty


def git_commit() -> str:
    out = subprocess.run(["git", "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", *PRODUCERS],
                         capture_output=True, text=True, check=True).stdout
    dirty = dirty_paths(out)
    if dirty:
        raise SystemExit("uncommitted producing code or inputs:\n" + "\n".join(dirty))
    return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()


def main() -> None:
    commit = git_commit()
    json.dumps(jsonable({"smoke": W.entries({(1, 2): W.GQ(1)})}))   # serializer smoke before the run
    t = time.time()
    out = {"scope": SCOPE, "source_commit": commit,
           "E2_14D": [{"signature": [p, q], "rows": W.witnesses(p, q)} for p, q in W.SIGS_14D]}
    out["seconds"] = round(time.time() - t, 1)
    if git_commit() != commit:
        raise SystemExit("HEAD moved during the run")
    OUT.write_text(json.dumps(jsonable(out), indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
