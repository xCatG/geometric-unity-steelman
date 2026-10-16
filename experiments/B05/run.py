"""B05 transcription-stage runner: writes experiments/B05/result.json.

Records the pairing facts, the pre-registered bilinear-variation controls, and the (9.16) branch survey. Nothing about
the draft is asserted here. Every survey predicate is relative to the enumerated model in operator_check.py; an
empty list is a property of that model, to be read against transcription.md, not a property of GU.
"""
import json
import subprocess
from collections import Counter
from pathlib import Path

from experiments.B05 import operator_check as OC
from experiments.B05 import pairing as PR
from gu.clifford import Mono, chirality, gammas

OUT = Path(__file__).with_name("result.json")
LABEL_KEYS = ("label", "order", "bar", "adj", "hom", "d0kind")   # label statuses depend on these only
DEGREE_KEYS = ("pair", "d0kind", "starparse", "m", "n", "r")    # degree verdicts depend on these only


def git_commit() -> str:
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "gu", "experiments/B05", "tests"],
                           capture_output=True, text=True, check=True).stdout.strip()
    dirty = "\n".join(ln for ln in dirty.splitlines() if not ln.endswith("result.json"))
    if dirty:
        raise SystemExit(f"uncommitted producing code:\n{dirty}")
    return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()


def pairing_rows() -> list[dict]:
    rows = []
    for p, q in [(3, 1), (1, 3), (7, 7), (9, 5), (2, 2)]:
        G, C = gammas(p, q), chirality(p, q)
        K, I = G[0], Mono.identity(C.n)
        for name, A in PR.forms(p, q).items():
            S = {"iC": C.times_i_power(1), "C": C, "iI": I.times_i_power(1)}
            rows.append({"signature": [p, q], "form": name, "candidate_not_source": True,
                         "invariant": PR.invariant(p, q, A), "hermitian": A.dagger() == A,
                         "vs_chirality": PR.relation_to_chirality(p, q, A),
                         "form_signature": list(PR.signature_of(A)), "u1_in_u(A)": PR.u1_membership(p, q, A),
                         "R1_invariant_K_Gamma0": {k: PR.bilinear_invariant(K, s, PR.sharp(s, A))
                                                   for k, s in S.items()}})
    return rows


def project(branches, keys) -> list[dict]:
    seen = {tuple(b[k] for k in keys) for b in branches}
    return [dict(zip(keys, v)) for v in sorted(seen, key=str)]


def label_table(results) -> list[dict]:
    """One row per label branch: every printed summand's status (identical across pair, starparse, m, n, r)."""
    rows, seen = [], set()
    for r in results:
        key = tuple(r["branch"][k] for k in LABEL_KEYS)
        if key in seen:
            continue
        seen.add(key)
        rows.append({"branch": dict(zip(LABEL_KEYS, key)),
                     "counts": dict(Counter(x["status"] for x in r["summands"])),
                     "summands": [{"row": x["row"], "col": x["col"], "sign": x["sign"],
                                   "term": [list(op) for op in x["term"]], "status": x["status"]}
                                  for x in r["summands"]]})
    return rows


def main() -> None:
    commit = git_commit()
    s = OC.survey()
    result = {
        "scope": "identity (exact monomial algebra); finite bookkeeping over an enumerated, model-relative branch set",
        "source": "GU April 1 2021 draft, (9.16) p. 46; typed in experiments/B05/source_operator.py",
        "model_caveat": "survey predicates are relative to operator_check.py's axes; unenumerated readings "
                        "(transcription.md branch register) can change them",
        "pairing": pairing_rows(),
        "survey": {"n_branches": s["n_branches"],
                   "well_typed": project(s["well_typed"], LABEL_KEYS),
                   "all_nonzero_under_model": project(s["all_nonzero_under_model"], LABEL_KEYS),
                   "degree_ok": project(s["degree_ok"], DEGREE_KEYS),
                   "label_table": label_table(s["results"])},
        "source_commit": commit,
    }
    OUT.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    sv = result["survey"]
    print(f"wrote {OUT}: well_typed={len(sv['well_typed'])} all_nonzero={len(sv['all_nonzero_under_model'])} "
          f"degree_ok={len(sv['degree_ok'])} (label branches / degree branches, model-relative)")


if __name__ == "__main__":
    main()
