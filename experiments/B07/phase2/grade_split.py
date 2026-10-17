"""Exact grade-pair decomposition of the C1 kernel in the flat 4D algebraic model.

Support means an intersection of subspaces, never the support of a chosen basis vector.
The two directed blocks have disjoint matrix entries, so their concatenated bases
give coordinates in a direct sum. No existing Phase 2 code path is changed.
"""
import json
import subprocess
import time
from pathlib import Path

import sympy as sp

from experiments.B07 import variation as V
from experiments.B07.phase2 import gates as G, universal as U
from experiments.B07.phase2.run import PRODUCERS, SIGS_4D

PAIRS = [(0, 1), (0, 3), (1, 4), (3, 4), (1, 2), (2, 3)]
OUT = Path(__file__).with_name("grade_split.json")
OUT_REL = "experiments/B07/phase2/grade_split.json"


def dirty_paths(porcelain_z: str) -> list[str]:
    """Runner's rename-aware guard, with only this runner's output exempted."""
    entries, dirty = iter(porcelain_z.split("\0")), []
    for entry in entries:
        if not entry:
            continue
        if set(entry[:2]) & set("RC"):
            source = next(entries)
            if source != OUT_REL:
                dirty.append(source)
        if entry[3:] != OUT_REL:
            dirty.append(entry[3:])
    return dirty


def git_commit() -> str:
    status = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", *PRODUCERS],
        capture_output=True, text=True, check=True).stdout
    dirty = dirty_paths(status)
    if dirty:
        raise SystemExit("uncommitted producing code or inputs:\n" + "\n".join(dirty))
    return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()


def subspace_support(columns: sp.Matrix, split: int) -> dict:
    """dim S, dim(S intersect forward), dim(S intersect reverse), for S = im columns.

    Rank-nullity for the projection onto the opposite block gives each intersection.
    This also works with redundant columns and the zero subspace.
    """
    columns = columns.applyfunc(G.exact)
    dim = columns.rank()
    return {"dim": dim, "forward": dim - columns[split:, :].rank(),
            "reverse": dim - columns[:split, :].rank()}


def pair_survey(p: int, q: int, j: int, l: int) -> dict:
    """Survey span(j -> l) + span(l -> j), with canonical K and zero-response Z support."""
    if (p, q) not in SIGS_4D or (j, l) not in PAIRS:
        raise ValueError("expected a registered 4D signature and grade pair")
    ph = U.phases(p, q)
    forward = U.equivariant_block(p, q, j, l, ph)
    reverse = U.equivariant_block(p, q, l, j, ph)
    blocks = forward + reverse
    maps = [U.as_map(matrix, p, q, ph) for matrix in blocks]
    survey = G.gate_survey(maps, p, q)
    # Reconstruct the same ordered kernel as gate_survey without changing its API.
    vectors = V.kernel({i: V.c1_residual(m, p + q, V.eta_of(p, q)) for i, m in enumerate(maps)})
    K = sp.Matrix.hstack(*(sp.Matrix(v) for v in vectors)) if vectors else sp.zeros(len(maps), 0)
    R = sp.Matrix([[G.exact(r[i]) for r in survey["c1_kernel_responses"]] for i in range(4)])
    zero_vectors = R.nullspace()
    Z = K * sp.Matrix.hstack(*zero_vectors) if zero_vectors else sp.zeros(len(maps), 0)
    survey.update(pair=[j, l], block_dims={"forward": len(forward), "reverse": len(reverse)},
                  c1_support=subspace_support(K, len(forward)),
                  zero_response_support=subspace_support(Z, len(forward)))
    return survey


def check_totals(rows: list[dict], universal: dict) -> dict:
    """Raise on any disagreement with Phase 2's universal dimensions, including every norm."""
    fields = ("dim", "c1_kernel_dim", "so_kernel_dim", "c1_kernel_einstein_dim")
    totals = {key: sum(row[key] for row in rows) for key in fields}
    totals["joint"] = {norm: {"dim": sum(row["joint"][norm]["dim"] for row in rows)} for norm in G.NORMS}
    expected = {key: universal[key] for key in fields}
    expected["joint"] = {norm: {"dim": universal["joint"][norm]["dim"]} for norm in G.NORMS}
    if totals != expected:
        raise AssertionError(f"grade-split totals {totals} != universal {expected}")
    return totals


def main() -> None:
    commit = git_commit()
    started = time.monotonic()
    baseline = json.loads(OUT.with_name("result.json").read_text(encoding="utf-8"))
    signatures = []
    for p, q in SIGS_4D:
        rows = []
        for j, l in PAIRS:
            pair_started = time.monotonic()
            row = pair_survey(p, q, j, l)
            row["seconds"] = round(time.monotonic() - pair_started, 1)
            rows.append(row)
            print(f"({p},{q}) {j}<->{l}: " + json.dumps(row, sort_keys=True), flush=True)
        universal = next(entry["universal"] for entry in baseline["item1_4d"] if entry["signature"] == [p, q])
        totals = check_totals(rows, universal)
        totals["zero_response_dim"] = sum(row["zero_response_support"]["dim"] for row in rows)
        signatures.append({"signature": [p, q], "pairs": rows, "totals": totals})
    # Detect concurrent edits or HEAD movement during the long computation.
    if git_commit() != commit:
        raise RuntimeError("source commit changed during grade-split survey")
    result = {"scope": "identity: exact grade-pair subspaces at (3,1)/(1,3), reading V, varpi direction, flat algebraic model",
              "support": "forward = j->l; reverse = l->j; dimensions of subspace intersections, not basis-vector support",
              "signatures": signatures, "source_commit": commit, "seconds": round(time.monotonic() - started, 1)}
    OUT.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({result['seconds']} s)", flush=True)


if __name__ == "__main__":
    main()
