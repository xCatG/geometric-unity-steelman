"""Non-GR channels runner: writes experiments/B07/escape/result.json. Run: uv run python -m experiments.B07.escape.run

E1 (quadratic.py): the T = 0 curvature quadratic form of (9.11) for E_OP, the named branches, and the response Gram.
E2 (weyl_dressing.py): exact Weyl response of Shiab_eps over the blade-Cayley family, with covariance control.
"""
import json
import subprocess
import time
from fractions import Fraction
from pathlib import Path

from experiments.B07 import variation as V
from experiments.B07.escape import quadratic as Q, weyl_dressing as WD
from experiments.B07.phase2.run import e_op

OUT = Path(__file__).with_name("result.json")
OUT_REL = "experiments/B07/escape/result.json"
PRODUCERS = ("gu", "experiments/B02", "experiments/B07", "tests", "pyproject.toml", "uv.lock")
SIGS = [(3, 1), (1, 3)]
SCOPE = ("identity: 4D point, flat model, T = 0 (E1); finite blade-Cayley dressing family (E2); "
         "reading V conventions of experiments/B07/phase2")


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


def jsonable(x):
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    return x


def e1(p: int, q: int) -> dict:
    maps = {"E_OP": e_op(p, q), **{k.split(",")[0]: V.branch_map(k, p, q) for k in V.BRANCHES}}
    return {"signature": [p, q], "invariants": list(Q.INVARIANTS), "basis_dim": len(Q.curvature_basis(p + q)),
            "Q": {conv: {name: Q.quadratic_form(X, p, q, conv) for name, X in maps.items()}
                  for conv in ("pinned", "prime")},
            "response_gram": Q.response_gram(p, q)}


def main() -> None:
    commit = git_commit()
    json.dumps(jsonable({"smoke": Fraction(1, 2)}))          # serializer smoke before the long run
    t = time.time()
    out = {"scope": SCOPE, "source_commit": commit,
           "E1": [e1(p, q) for p, q in SIGS],
           "E2": [WD.survey(p, q) for p, q in SIGS]}
    out["seconds"] = round(time.time() - t, 1)
    if git_commit() != commit:
        raise SystemExit("HEAD moved during the run")
    OUT.write_text(json.dumps(jsonable(out), indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
