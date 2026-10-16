# B05 Fermionic-Sector Transcription and Specification Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking. In this project Claude owns transcriptions, specifications and plans; Codex (pane 0:3) owns code, tests and the register (P6). Read `docs/methods.md` (P1–P11) first.

**Goal:** Produce a reviewed, typed specification of GU's fermionic sector that is complete enough to *pose* B05's covariance test: the operator (9.16) with its alternatives, every field's type, the pairing, the candidate reality conditions, and each candidate generator's action on every field. Everything the draft leaves open is either branched or marked `unspecified`. **This plan delivers no verdict on any gauge symmetry, anomaly, or reality condition.**

**Why this comes first.** Codex and Grok reviewed independently which register item should come next (`.agent-handoff/next-item-{codex,grok}/result.md`). Both agreed on these points:
- A covariance or rejection test has nothing to fail against until the kinetic operator is pinned. No B01–B03 output pins one.
- A generator must be tested by transforming barred fields, unbarred fields, connection, Clifford data and dressings together. A commutator with a frozen operator measures a stabilizer, not a gauge symmetry. For example, if both ψ̄ and ψ transform with C, then {K,C} = 0 can give invariance even though [K,C] ≠ 0.
- B03's J is not a default reality condition. At (9,5), J² = −1, so Jψ = ψ has no nonzero solution. At (7,7), choosing a fixed real subspace is extra input. The Dirac pairing A is a different operator from J.
- Removing a classical non-symmetry removes a premise of Nguyen–Polya §3.2. It does not test their anomaly conclusion, which concerns the earlier U(128) setup.

**Architecture.**
- **Documents (Claude):**
  - `experiments/B05/transcription.md`: the verbatim source, a symbol table, the branch register and hand derivations;
  - `experiments/B05/source_operator.py`: the typed (9.16);
  - `experiments/B05/spec.md`: the transformation-law sheet and specification status;
  - `experiments/B05/README.md`.
- **Code (Codex):**
  - `experiments/B05/pairing.py`: exact facts about the Spin-invariant Hermitian forms;
  - `experiments/B05/operator_check.py`: label and form-degree bookkeeping of (9.16) over an enumerated branch set;
  - `experiments/B05/run.py`, which writes `result.json`.
- **Second source (Codex):** `experiments/B05/np_objection.md`, a transcription of Nguyen–Polya §3.2 with a map from its objects to those of the April draft.

**Tech Stack:** Python ≥ 3.12 via `uv`; exact monomial matrices from `gu.clifford` (int64 perm/phase); no floats; pytest. Page rendering uses PyMuPDF via `uv run --no-project --with pymupdf` (scratch only, not a project dependency).

**Spec:** `docs/superpowers/specs/2026-10-14-gu-steelman-design.md` (rev 4.1). Register entries are B05 (with B04 and B07 as cross-references) in `docs/gaps/register.md`.

## Global Constraints

- **Source.** The GU draft is the same PDF as in B01–B03: SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, at `.agent-handoff/b01-task4/evidence/GU-draft.pdf`. Pages are read as rendered images. Text extraction is a cross-check only, because it drops ⊚, ϖ, the bars and the subscripts in (9.16).
- **No verdicts.** Survivor lists from the branch survey are recorded, never asserted. An empty survivor list is a finding to be explained in `transcription.md`/`spec.md`; it is not an implementation failure.
- **Exactness (P4).** No floats anywhere. `pairing.py` uses only `gu.clifford.Mono` algebra.
- **Expected values come from outside the code under test (P3).** Every asserted value is either a textbook control (the Weyl kinetic term, a vanishing same-chirality bilinear, the Dirac mass coupling) or a hand derivation written in the test docstring and in `transcription.md` §Hand derivations.
- **Small first (P5).** The pairing facts run on (3,1), (1,3) and the (2,2) control before (7,7) and (9,5).
- **Seeded faults (P2).** F1–F6 below must each fail an **assertion**, with SHA-verified restores. `faults.py` is a scratch file and is never committed.
- **Commits.** On master. Run `git add -- <new paths>` first, then `git commit -m … -- <paths>`, never a bare commit. Commit the producing code before `result.json` (P8). Codex's trailer is `Co-Authored-By: Codex <noreply@openai.com>`, Claude's is `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- **Untouchables.** Do not touch the untracked `argon*.md` files or `C:\work\src\GU-b02-lean`. No Fable spend.

## Review Focus

These are the failure modes most likely to produce a wrong specification, with the test or step that pins each one:
1. **A reading silently chosen where the draft is open.** The ± on ϖ, the bar, ϖ̄*, d₀ and ⊚ on spinor-valued forms are all ambiguous. Each is an enumerated axis in `operator_check.py` and a numbered branch in `transcription.md`. The second reader (Task 2) must find any axis we missed.
2. **A wrong chirality pairing.** The draft's row and column labels only make sense relative to which chiralities ψ̄ pairs. `test_forms_pair_opposite_chirality_when_q_odd` pins A·C = −C·A at (7,7) and (9,5) for both invariant forms, with the (2,2) impostor where they commute.
3. **The axial U(1) assumed to be in the structure algebra.** `test_u1_membership` pins that iC ∉ 𝔲(A) while C ∈ 𝔲(A) whenever A·C = −C·A. The (2,2) control shows the opposite. Whether GU actually gauges either one is a Task 5 question, not a test.
4. **A frozen-operator rejection criterion.** `spec.md` must state the full variation δ(ψ̄Kψ) = ψ̄(S̄K + KS + δK)ψ. It must also include the pre-registered axial example, where both fields transform with C, {K,C} = 0 and [K,C] ≠ 0, so that the later test cannot reject it by commutator alone (Task 5, Step 3).
5. **A transfer of NP's U(128) objects to U(64,64) without justification.** `np_objection.md` maps every NP object to an April-draft object or to `no counterpart`, and no row is filled by analogy alone (Task 3).

## File structure

| Path | Owner | Responsibility |
|---|---|---|
| `experiments/B05/__init__.py` | Codex | package marker |
| `experiments/B05/transcription.md` | Claude | verbatim source, symbol table (P11 lookups recorded), branch register, hand derivations |
| `experiments/B05/source_operator.py` | Claude | typed (9.16): rows, columns, entries as summands of primitives |
| `experiments/B05/np_objection.md` | Codex | NP §3.2 transcription and object map |
| `experiments/B05/pairing.py` | Codex | invariant Hermitian forms: chirality relation, signature, U(1) membership |
| `experiments/B05/operator_check.py` | Codex | label and degree bookkeeping per summand, branch enumeration, survey |
| `experiments/B05/run.py` | Codex | writes `result.json` |
| `experiments/B05/result.json` | Codex | generated record |
| `tests/test_b05.py` | Codex | controls and hand-derived identities |
| `experiments/B05/spec.md` | Claude | transformation-law sheet, reality branches, invariance criterion, status table |
| `experiments/B05/README.md` | Claude | what is specified, what is branched, what is open, what the covariance test will need |
| `docs/gaps/register.md` (B05 entry) | Codex | status update, linking tracked files only |

---

### Task 1: Transcription rev 0 and typed operator (Claude)

**Files:**
- Create: `experiments/B05/transcription.md`, `experiments/B05/source_operator.py`, `experiments/B05/__init__.py` (empty)

**Interfaces:**
- Produces `source_operator.D`, `ROWS`, `COLS`, `ENTRIES`, `S`, `SH`, `D0`, `D0S`, `W(a, b)`, `WS(a, b)`, as in the code below. Task 4 consumes them.

- [ ] **Step 1: Verify the source and render the pages.**

```bash
sha256sum .agent-handoff/b01-task4/evidence/GU-draft.pdf   # expect 3f28d742…186d4
```

Render the pages below at 150 dpi into the scratchpad (not the repo) with PyMuPDF, then read each image:
- 24: (3.29)–(3.36), U(64,64), $, ad;
- 31–34: §5.1–5.5 (field content; 𝒢 = ℋ ⋉ 𝒩 (5.8)–(5.9); the actions (5.10)–(5.11); fermions and SUSY);
- 36–38: §6 (A₀ ≈ ∇⁰ ≈ d₀; (6.2); the tilted map τ (6.3)–(6.5); the stabilizer (6.6)–(6.9); (6.10)–(6.13));
- 39–42: §7 (augmented torsion) and §8 ((8.1), the Shiab family with parameters n, m, Φ_r and ±);
- 43–47: §9, including (9.16)–(9.22);
- 50–51 and 58: the fermionic complex diagram and the field table, for field types;
- 60–62: §12.9 (effective chirality).

- [ ] **Step 2: Write `transcription.md` rev 0.** Use the format of `experiments/B03/transcription.md`. It needs these sections:
  - **Source:** the hash, the pages read, and the cross-references followed (P11).
  - **Verbatim:** (9.16) rendered as a matrix in LaTeX. The row vector is (ζ̄₋, ζ̄₊, ν̄₋, ν̄₊) with subscript ρ(ε); the column vector is (ζ₊, ζ₋, ν₊, ν₋) with subscript ρ(ε⁻¹). Also (9.17)–(9.20), (8.1), (5.8)–(5.11), (6.2), (6.4), (6.13) and (3.31)–(3.36), and the sentences "four distinct fields", "other versions … non-trivial map in the lower right quadrant" and "Berezinian 'integral'".
  - **Symbol table:** each symbol with its type and the page where it is defined, or `not defined (looked: pp. …)`. It must include at least: ⊚ (the Shiab family of §8, here applied to spinor-valued forms); ϖ, ϖ₊₊, ϖ₊₋, ϖ₋₊, ϖ₋₋; ϖ̄*; d₀ and d₀*; ∗; ρ(ε) and ρ(ε⁻¹); the bar; $; A (not printed in §9.3, so state that); ε; 𝒢, ℋ, 𝒩; τ_{A₀}; ℋ_τ ("Tedha") versus "Seedhe"; 𝒟 and χ in (9.17); ϒ^F.
  - **Branch register:** number each open reading. At minimum, branches B05-L (meaning of ±), B05-O (subscript order), B05-B (bar), B05-J (ϖ̄*), B05-P (pairing), B05-D (d₀), B05-S (⊚ parameters m, n, r), B05-Q (whether ⊚ preserves spinor labels; the code assumes it does), B05-R (reality condition) and B05-T (transformation laws). For each, give the readings, the textual evidence, and whether `operator_check.py` enumerates it. B05-Q, B05-R and B05-T are **not** enumerated by code; say so.
  - **Hand derivations (P3):** the expected values that Task 4's tests assert:
    1. AC = (−1)^q CA for A a product of q gammas, in even dimension;
    2. a Hermitian monomial form anticommuting with C has signature (n/2, n/2);
    3. (iC)†A + A(iC) = i(AC − CA), and C†A + AC = CA + AC;
    4. on a 14-dimensional 1-form, ∗(⊚_{m=1,n=0,r=1}(ϖ ∧ ζ)) has degree 1;
    5. the three textbook controls: ψ̄₋ ∂̸ψ₋ is consistent, ψ̄₋ψ₋ vanishes, and ψ̄₋ m ψ₊ is the mass coupling.
  - **Hand verdicts:** at least four summands of (9.16) under two named branches, derived by hand **before** Task 4 runs. They are pre-registered predictions; the runner's table is compared with them in Task 4, Step 6.

- [ ] **Step 3: Write `source_operator.py`** exactly as below. The entries are read off the p. 46 image. The operator has 12 nonzero entries containing 18 summands, and its lower-right 2×2 is zero.

```python
"""Claude's typed transcription of GU (9.16), p. 46 (April 1, 2021 draft). Do not edit without a transcription revision.

Fields: (form degree, label). zeta, zetabar in Omega^1(Y, $); nu, nubar in Omega^0(Y, $). d = dim Y = 14.
Row vector (zetabar_-, zetabar_+, nubar_-, nubar_+); column vector (zeta_+, zeta_-, nu_+, nu_-).
An entry is a tuple of summands; a summand is a tuple of primitives, composed right to left.
The printed "*(circledcirc)" is read as star after shiab; signs and the bar on varpibar are not label data.
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
    ("zb-", "z+"): ((S, SH, W("+", "+")),),
    ("zb-", "z-"): ((S, SH, D0), (S, SH, W("+", "-"))),
    ("zb-", "n+"): ((W("+", "+"),),),
    ("zb-", "n-"): ((D0,), (W("+", "-"),)),
    ("zb+", "z+"): ((S, SH, D0), (S, SH, W("-", "+"))),
    ("zb+", "z-"): ((S, SH, W("-", "-")),),
    ("zb+", "n+"): ((D0,), (W("-", "+"),)),
    ("zb+", "n-"): ((W("-", "-"),),),
    ("nb-", "z+"): ((WS("+", "+"),),),
    ("nb-", "z-"): ((D0S,), (WS("+", "-"),)),
    ("nb+", "z+"): ((D0S,), (WS("-", "+"),)),
    ("nb+", "z-"): ((WS("-", "-"),),),
}
```

- [ ] **Step 4: Commit** (Claude):

```bash
git add -- experiments/B05/__init__.py experiments/B05/transcription.md experiments/B05/source_operator.py
git commit -m "B05 transcription rev 0 and typed (9.16)" -- experiments/B05/__init__.py experiments/B05/transcription.md experiments/B05/source_operator.py
```

### Task 2: Blind second reading (Codex), then transcription rev 1 (Claude)

**Files:**
- Create (untracked): `.agent-handoff/b05-transcription/second-reader.md`, `transcription-comparison.md`
- Modify: `experiments/B05/transcription.md` (rev 1), and, if the comparison requires it, `source_operator.py`

- [ ] **Step 1 (Codex, blind):** Without opening `experiments/B05/transcription.md` or `source_operator.py`, render the same pages and write `second-reader.md` from scratch. Include:
  - (9.16) entry by entry;
  - the symbol table;
  - every reading you think the draft leaves open;
  - for each operator entry, the field types it connects.
- [ ] **Step 2 (Codex):** Now compare against Claude's rev 0. Write `transcription-comparison.md` with one row per disagreement: the item, Claude's text, yours, the page, and which reading the image supports. List every open reading that Claude's branch register does not have.
- [ ] **Step 3 (Claude):** Fold the comparison into rev 1 and record each change in a revision note, as B03 rev 1 did. If an entry of `source_operator.py` changes, Task 4 has not started yet, so the edit is a transcription fix. Commit `transcription.md`, and `source_operator.py` if changed, with an explicit pathspec.

### Task 3: Nguyen–Polya §3.2 and its object map (Codex)

**Files:**
- Create: `experiments/B05/np_objection.md`
- Create (untracked evidence): `.agent-handoff/b05-np/NP.pdf` and its SHA-256

- [ ] **Step 1:** Download `https://files.timothynguyen.org/geometric_unity.pdf` into `.agent-handoff/b05-np/` and record the SHA-256 and the access date. Render pp. 6–7 and transcribe §3.2 verbatim.
- [ ] **Step 2:** Write the object map, one row per NP object:
  - the group (U(128));
  - the "central U(1)";
  - the "gauged axial" transformation;
  - the fermion content;
  - the kinetic operator;
  - the full-adjoint/exterior identification;
  - the Spin-shrinking argument.

  For each, give the April-draft counterpart (page, symbol) or `no counterpart`, and say whether the transfer needs an assumption. Rows that cannot be filled are left open, not guessed.
- [ ] **Step 3:** Commit `experiments/B05/np_objection.md` with an explicit pathspec, with Codex's trailer.

### Task 4: Pairing facts, operator bookkeeping, runner (Codex)

**Files:**
- Create: `experiments/B05/pairing.py`, `experiments/B05/operator_check.py`, `experiments/B05/run.py`, `tests/test_b05.py`, `experiments/B05/result.json`

**Interfaces:**
- Consumes `gu.clifford.{Mono, gammas, dirac_pairing, chirality}`, and `experiments.B05.source_operator` from Task 1.
- Produces, for Task 5 and the later covariance plan:
  - `pairing.forms(p, q) -> dict[str, Mono]`;
  - `pairing.relation_to_chirality(p, q, A) -> str`;
  - `pairing.u1_membership(p, q, A) -> dict[str, bool]`;
  - `pairing.signature_of(A) -> tuple[int, int]`;
  - `operator_check.branches() -> list[dict]`;
  - `operator_check.check(br, entries=None, rows=None, cols=None) -> dict`;
  - `operator_check.survey() -> dict`.

- [ ] **Step 1: Write the failing tests**, `tests/test_b05.py`, exactly:

```python
"""B05 transcription-stage checks. Controls validate the tools; findings are recorded by the runner, not asserted."""
import pytest

from experiments.B05 import operator_check as OC
from experiments.B05 import pairing as PR
from experiments.B05 import source_operator as SRC

SIGS = [(3, 1), (1, 3), (7, 7), (9, 5)]


# ---- pairing.py --------------------------------------------------------------------------------------------

@pytest.mark.parametrize("p,q", SIGS + [(2, 2)])
def test_both_forms_are_spin_invariant_hermitian(p, q):
    """Control, identity: products of all timelike (resp. spacelike) gammas give Spin(p,q)-invariant Hermitian forms."""
    for A in PR.forms(p, q).values():
        assert A.dagger() == A
        assert PR.invariant(p, q, A)


@pytest.mark.parametrize("p,q", SIGS)
def test_forms_pair_opposite_chirality_when_q_odd(p, q):
    """Finding input, identity: A anticommutes with C for (3,1), (1,3), (7,7), (9,5) (q odd, p odd).

    Hand derivation: A = product of q gammas; each anticommutes with C in even dimension, so AC = (-1)^q CA.
    """
    for A in PR.forms(p, q).values():
        assert PR.relation_to_chirality(p, q, A) == "anticommute"


def test_forms_commute_with_chirality_at_2_2():
    """Control, identity: q = 2 even, so AC = CA (ambient impostor for the q-odd rule)."""
    for A in PR.forms(2, 2).values():
        assert PR.relation_to_chirality(2, 2, A) == "commute"


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_neutral_signature(p, q):
    """Control, identity: an invariant form anticommuting with C has signature (n/2, n/2); at (7,7) that is U(64,64)."""
    for A in PR.forms(p, q).values():
        n = A.n
        assert PR.signature_of(A) == (n // 2, n // 2)


@pytest.mark.parametrize("p,q", SIGS)
def test_u1_membership(p, q):
    """Finding input, identity: when AC = -CA, iI and C are in u(A) but the axial phase iC is not.

    Hand derivation: (iC)^dag A + A(iC) = i(AC - CA) = 2iAC != 0; C^dag A + AC = CA + AC = 0.
    """
    for A in PR.forms(p, q).values():
        assert PR.u1_membership(p, q, A) == {"central_iI": True, "axial_iC": False, "chiral_boost_C": True}


def test_u1_membership_flips_at_2_2():
    """Control, identity: when AC = CA (q even), iC is in u(A) and C is not."""
    for A in PR.forms(2, 2).values():
        assert PR.u1_membership(2, 2, A) == {"central_iI": True, "axial_iC": True, "chiral_boost_C": False}


# ---- operator_check.py --------------------------------------------------------------------------------------

ROWS_T = {"pb-": (0, "-"), "pb+": (0, "+")}
COLS_T = {"p+": (0, "+"), "p-": (0, "-")}
TEXTBOOK = dict(label="chirality", order="target_source", bar="dirac_adjoint", adj="a_adjoint",
                pair="metric", d0kind="clifford", m=0, n=0, r=0)


def test_textbook_dirac_kinetic_term_is_consistent():
    """Control: psibar_- (dslash psi_-) is the textbook Weyl kinetic term psi_L^dag sigma.d psi_L; it must be 'ok'."""
    entries = {("pb-", "p-"): ((SRC.D0,),), ("pb+", "p+"): ((SRC.D0,),)}
    out = OC.check(TEXTBOOK, entries, ROWS_T, COLS_T)
    assert [x["label"] for x in out["summands"]] == ["ok", "ok"]
    assert out["label_ok"] and out["degree_ok"]


def test_same_chirality_scalar_bilinear_vanishes():
    """Control: psibar_L psi_L = 0 (a mass term couples L to R); with no Clifford factor it must pair to zero."""
    entries = {("pb-", "p-"): ((SRC.W("-", "-"),),)}
    out = OC.check(TEXTBOOK, entries, ROWS_T, COLS_T)
    assert [x["label"] for x in out["summands"]] == ["pairs_to_zero"]
    assert not out["label_ok"]


def test_mass_term_is_consistent():
    """Control: psibar_- m psi_+ with an endomorphism + -> + is the textbook Dirac mass coupling; 'ok'."""
    entries = {("pb-", "p+"): ((SRC.W("+", "+"),),)}
    assert OC.check(TEXTBOOK, entries, ROWS_T, COLS_T)["summands"][0]["label"] == "ok"


def test_ill_typed_when_domain_label_missing():
    """Control: varpi_{+-} (target +, source -) applied to a + field is outside its domain."""
    entries = {("pb-", "p+"): ((SRC.W("+", "-"),),)}
    assert OC.check(TEXTBOOK, entries, ROWS_T, COLS_T)["summands"][0]["label"] == "ill_typed"


def test_degree_bookkeeping_by_hand():
    """Control: on a 1-form in 14D, *(shiab_{m=1,n=0,r=1}(varpi ^ zeta)) has degree 14 - (14 - 2 + 1) = 1."""
    br = dict(TEXTBOOK, d0kind="exterior", m=1, n=0, r=1)
    k = 1
    for op in reversed((SRC.S, SRC.SH, SRC.W("+", "+"))):
        k = OC.degree(op, k, br)
    assert k == 1


def test_branch_space_is_complete():
    """Control: 2^8 * 5 = 1280 (eight binary axes, five values of r) branches, each distinct."""
    bs = OC.branches()
    assert len(bs) == 1280
    assert len({tuple(b.values()) for b in bs}) == 1280


def test_transcription_shape():
    """Control on Claude's typed data: 12 nonzero entries, 18 summands, the 4 lower-right entries absent."""
    assert len(SRC.ENTRIES) == 12
    assert sum(len(t) for t in SRC.ENTRIES.values()) == 18
    assert not any(r.startswith("nb") and c.startswith("n") for r, c in SRC.ENTRIES)


def test_survey_is_recorded_not_asserted():
    """The survey runs on every branch and returns per-summand verdicts from the allowed set."""
    s = OC.survey()
    assert s["n_branches"] == 1280
    assert all(x["label"] in OC.VERDICTS for r in s["results"] for x in r["summands"])
```

- [ ] **Step 2: Run them; expect an ImportError for `pairing`/`operator_check`.**

Run: `uv run pytest -q tests/test_b05.py`
Expected: collection error, `ModuleNotFoundError: No module named 'experiments.B05.pairing'`.

- [ ] **Step 3: Write `experiments/B05/pairing.py`** exactly:

```python
"""B05 Task 3: chirality behaviour of the Spin(p,q)-invariant Hermitian forms, and which U(1)s they admit.

Facts about the existing monomial gammas (`gu.clifford`), exact. The U(64,64) of GU (3.31)-(3.36) is the
isometry group of such a form A on the 128-dimensional Dirac spinors at (7,7).
"""
from __future__ import annotations

from gu.clifford import Mono, chirality, dirac_pairing, gammas


def _hermitian_phase(m: Mono) -> Mono:
    for k in range(4):
        c = m.times_i_power(k)
        if c.dagger() == c:
            return c
    raise AssertionError("no Hermitian phase")


def spacelike_pairing(p: int, q: int) -> Mono:
    """Phase times the product of the spacelike gammas, chosen Hermitian (the other invariant form)."""
    G = gammas(p, q)
    out = Mono.identity(G[0].n)
    for g in G[:p]:
        out = out @ g
    return _hermitian_phase(out)


def forms(p: int, q: int) -> dict[str, Mono]:
    return {"timelike": dirac_pairing(p, q), "spacelike": spacelike_pairing(p, q)}


def invariant(p: int, q: int, A: Mono) -> bool:
    """Sigma^dagger A + A Sigma = 0 for every Sigma = G_a G_b, a < b."""
    G = gammas(p, q)
    return all((G[a] @ G[b]).dagger() @ A == -(A @ G[a] @ G[b])
               for a in range(p + q) for b in range(a + 1, p + q))


def relation_to_chirality(p: int, q: int, A: Mono) -> str:
    C = chirality(p, q)
    if A @ C == C @ A:
        return "commute"
    if A @ C == -(C @ A):
        return "anticommute"
    return "neither"


def in_isometry_algebra(X: Mono, A: Mono) -> bool:
    """X in u(A) iff X^dagger A + A X = 0."""
    return X.dagger() @ A == -(A @ X)


def u1_membership(p: int, q: int, A: Mono) -> dict[str, bool]:
    """Which of the central phase iI, the axial phase iC and the real chiral boost C lie in u(A)."""
    C = chirality(p, q)
    iI = Mono.identity(C.n).times_i_power(1)
    return {"central_iI": in_isometry_algebra(iI, A),
            "axial_iC": in_isometry_algebra(C.times_i_power(1), A),
            "chiral_boost_C": in_isometry_algebra(C, A)}


def signature_of(A: Mono) -> tuple[int, int]:
    """(n_plus, n_minus) of the Hermitian monomial form A; exact via its 1- and 2-cycles."""
    plus = minus = 0
    seen = set()
    for j in range(A.n):
        if j in seen:
            continue
        i = int(A.perm[j])
        if i == j:                                   # diagonal entry i^phase is real: phase 0 or 2
            ph = int(A.phase[j])
            if ph not in (0, 2):
                raise AssertionError("non-real diagonal entry of a Hermitian form")
            plus, minus = (plus + 1, minus) if ph == 0 else (plus, minus + 1)
            seen.add(j)
        else:                                        # Hermitian 2x2 block [[0, z̄], [z, 0]]: one +, one -
            if int(A.perm[i]) != j:
                raise AssertionError("Hermitian monomial with a cycle longer than 2")
            plus, minus = plus + 1, minus + 1
            seen.update((i, j))
    return plus, minus
```

- [ ] **Step 4: Write `experiments/B05/operator_check.py`** exactly:

```python
"""B05 Task 4: spinor-label and form-degree bookkeeping for the draft's operator (9.16), under every branch.

Pure bookkeeping on Claude's typed transcription (`source_operator.py`); no numerics, no verdict on any
symmetry. Each printed summand is checked against (a) the spinor label its column field supplies and the
label its row field pairs with, and (b) the form degree the pairing requires. A branch is one reading of
something the draft leaves open; the runner records every branch, it asserts none.
"""
from __future__ import annotations

from itertools import product

from experiments.B05 import source_operator as SRC

LABEL = ("chirality", "signature")        # +/- = eigenvalue of C, or of the U(64,64) form A
ORDER = ("target_source", "source_target")  # varpi_{ab}: a is the target label, or the source label
BAR = ("dirac_adjoint", "dual_field")     # psibar_s = psi_s^dagger A, or an independent field in S_s^*
ADJ = ("a_adjoint", "subscript_swap")     # varpibar*_{ab}: A-adjoint of varpi_{ab}, or varpi with a, b swapped
PAIR = ("wedge", "metric")                # <psibar, X>: psibar ^ X is top degree, or deg psibar == deg X
D0KIND = ("exterior", "clifford")         # d0: exterior covariant derivative, or Clifford-contracted (Dirac-type)
SHIAB_M = (0, 1)                          # (8.1): *^m inside the bracket
SHIAB_N = (0, 1)                          # (8.1): *^n outside it
SHIAB_R = (0, 1, 2, 3, 4)                 # form degree r of Phi_r

BOTH = frozenset("+-")
VERDICTS = ("ok", "mixed", "pairs_to_zero", "ill_typed")


def flip(s: str) -> str:
    return "-" if s == "+" else "+"


def pairs_with(row_label: str, label: str, bar: str) -> str:
    """Label of the vectors a row field pairs nontrivially with.

    A anticommutes with C at (7,7) and (9,5) (`pairing.py`), so under the chirality reading a Dirac
    adjoint pairs opposite labels. A preserves its own eigenspaces, and a dual field pairs its own label.
    """
    if bar == "dirac_adjoint" and label == "chirality":
        return flip(row_label)
    return row_label


def _varpi_map(op, label, order, adj):
    a, b = op[1], op[2]
    src, tgt = (b, a) if order == "target_source" else (a, b)
    if op[0] == "varpibar_star":
        if adj == "subscript_swap":
            src, tgt = tgt, src
        elif label == "chirality":                   # A-adjoint of src -> tgt is (-tgt) -> (-src)
            src, tgt = flip(tgt), flip(src)
        else:                                        # A preserves its eigenspaces: tgt -> src
            src, tgt = tgt, src
    return src, tgt


def apply_label(op, s_in: frozenset, br: dict) -> frozenset:
    kind = op[0]
    if kind in ("star", "shiab"):
        return s_in                                  # act on the form factor only
    if kind in ("d0", "d0star"):
        if br["label"] == "signature":
            return BOTH                              # neither nabla nor c(e) preserves A's eigenspaces
        return frozenset(map(flip, s_in)) if br["d0kind"] == "clifford" else s_in
    if kind in ("varpi", "varpibar_star"):
        src, tgt = _varpi_map(op, br["label"], br["order"], br["adj"])
        return frozenset({tgt}) if src in s_in else frozenset()
    raise ValueError(f"unknown primitive {op!r}")


def degree(op, k: int, br: dict) -> int:
    kind, d = op[0], SRC.D
    if kind == "star":
        return d - k
    if kind in ("d0", "d0star") and br["d0kind"] == "clifford":
        return k                                     # c(e^i) nabla_i acts on the spinor factor
    if kind in ("d0", "varpi"):
        return k + 1
    if kind in ("d0star", "varpibar_star"):
        return k - 1
    if kind == "shiab":                              # (8.1): *^n [Phi_r ^ *^m eta]
        k = d - k if br["m"] else k
        k += br["r"]
        return d - k if br["n"] else k
    raise ValueError(f"unknown primitive {op!r}")


def summand(term, row, col, br, rows=None, cols=None) -> tuple[str, bool]:
    """(label verdict, degree_ok) for one printed summand; primitives compose right to left."""
    rows, cols = rows or SRC.ROWS, cols or SRC.COLS
    k, s = cols[col][0], frozenset({cols[col][1]})
    for op in reversed(term):
        s, k = apply_label(op, s, br), degree(op, k, br)
    want = pairs_with(rows[row][1], br["label"], br["bar"])
    if not s:
        verdict = "ill_typed"                        # the column's label is not in the first map's domain
    elif want not in s:
        verdict = "pairs_to_zero"                    # the printed summand vanishes identically
    elif s == {want}:
        verdict = "ok"
    else:
        verdict = "mixed"                            # output spans both labels; the row projects one out
    kr = rows[row][0]
    deg_ok = 0 <= k <= SRC.D and ((kr + k == SRC.D) if br["pair"] == "wedge" else kr == k)
    return verdict, deg_ok


KEYS = ("label", "order", "bar", "adj", "pair", "d0kind", "m", "n", "r")


def branches() -> list[dict]:
    return [dict(zip(KEYS, v)) for v in
            product(LABEL, ORDER, BAR, ADJ, PAIR, D0KIND, SHIAB_M, SHIAB_N, SHIAB_R)]


def check(br: dict, entries=None, rows=None, cols=None) -> dict:
    entries = entries or SRC.ENTRIES
    out = []
    for (row, col), terms in entries.items():
        for term in terms:
            v, d = summand(term, row, col, br, rows, cols)
            out.append({"row": row, "col": col, "term": term, "label": v, "degree_ok": d})
    return {"branch": br, "summands": out,
            "label_ok": all(x["label"] in ("ok", "mixed") for x in out),
            "degree_ok": all(x["degree_ok"] for x in out)}


def survey() -> dict:
    """Every branch, with the per-field survivor lists; recorded by the runner, never asserted."""
    results = [check(b) for b in branches()]
    return {"n_branches": len(results),
            "label_ok": [r["branch"] for r in results if r["label_ok"]],
            "degree_ok": [r["branch"] for r in results if r["degree_ok"]],
            "both": [r["branch"] for r in results if r["label_ok"] and r["degree_ok"]],
            "results": results}
```

- [ ] **Step 5: Run the tests, then the full suite.**

Run: `uv run pytest -q tests/test_b05.py`
Expected: `26 passed`.

Run: `uv run pytest -q`
Expected: `336 passed` (310 before + 26).

- [ ] **Step 6: Seeded faults (P2).** Save the script below as a scratch `faults.py` (not committed) and run `uv run python faults.py`. Expected: six `RED` lines, each failing on an `AssertionError`. Every restore is hash-verified.

```python
import hashlib, pathlib, subprocess, sys
F = [
 ("F1 Dirac adjoint pairs equal chirality", "experiments/B05/operator_check.py",
  '    if bar == "dirac_adjoint" and label == "chirality":\n        return flip(row_label)\n', ''),
 ("F2 Clifford d0 keeps chirality", "experiments/B05/operator_check.py",
  'frozenset(map(flip, s_in)) if br["d0kind"] == "clifford" else s_in', 's_in'),
 ("F3 star keeps degree", "experiments/B05/operator_check.py",
  '    if kind == "star":\n        return d - k', '    if kind == "star":\n        return k'),
 ("F4 invariance sign", "experiments/B05/pairing.py",
  '== -(A @ G[a] @ G[b])', '== (A @ G[a] @ G[b])'),
 ("F5 isometry test without dagger", "experiments/B05/pairing.py",
  'return X.dagger() @ A == -(A @ X)', 'return X @ A == -(A @ X)'),
 ("F6 shiab ignores *^m", "experiments/B05/operator_check.py",
  'k = d - k if br["m"] else k', 'k = k'),
]
for name, path, old, new in F:
    p = pathlib.Path(path); src = p.read_text(encoding="utf-8"); h = hashlib.sha256(src.encode()).hexdigest()
    assert src.count(old) == 1, (name, "anchor")
    p.write_text(src.replace(old, new), encoding="utf-8")
    r = subprocess.run(["uv", "run", "pytest", "-q", "tests/test_b05.py"], capture_output=True, text=True)
    p.write_text(src, encoding="utf-8")
    assert hashlib.sha256(p.read_text(encoding="utf-8").encode()).hexdigest() == h
    fails = [l for l in r.stdout.splitlines() if l.startswith("FAILED")]
    print("RED " if r.returncode else "GREEN", name, len(fails), "failing;", "AssertionError" in r.stdout)
```

Expected output (smoke-tested):

```text
RED  F1 Dirac adjoint pairs equal chirality 3 failing; True
RED  F2 Clifford d0 keeps chirality 1 failing; True
RED  F3 star keeps degree 1 failing; True
RED  F4 invariance sign 5 failing; True
RED  F5 isometry test without dagger 5 failing; True
RED  F6 shiab ignores *^m 1 failing; True
```

- [ ] **Step 7: Commit the code, then generate and commit the result (P8).**

```bash
git add -- experiments/B05/pairing.py experiments/B05/operator_check.py experiments/B05/run.py tests/test_b05.py
git commit -m "B05: invariant-pairing facts and (9.16) branch bookkeeping" -- experiments/B05/pairing.py experiments/B05/operator_check.py experiments/B05/run.py tests/test_b05.py
uv run python -m experiments.B05.run
git add -- experiments/B05/result.json
git commit -m "B05: result.json" -- experiments/B05/result.json
```

`run.py`:

```python
"""B05 transcription-stage runner: writes experiments/B05/result.json.

Records the pairing facts and the (9.16) branch survey. Nothing about the draft is asserted here:
survivor lists, including empty ones, are findings to be read against the transcription's hand derivation.
"""
import json
import subprocess
from collections import Counter
from pathlib import Path

from experiments.B05 import operator_check as OC
from experiments.B05 import pairing as PR

OUT = Path(__file__).with_name("result.json")
LABEL_KEYS = ("label", "order", "bar", "adj", "d0kind")   # label verdicts depend on these only
DEGREE_KEYS = ("pair", "d0kind", "m", "n", "r")           # degree verdicts depend on these only


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
        for name, A in PR.forms(p, q).items():
            rows.append({"signature": [p, q], "form": name, "invariant": PR.invariant(p, q, A),
                         "hermitian": A.dagger() == A, "vs_chirality": PR.relation_to_chirality(p, q, A),
                         "form_signature": list(PR.signature_of(A)), "u1": PR.u1_membership(p, q, A)})
    return rows


def project(branches, keys) -> list[dict]:
    seen = {tuple(b[k] for k in keys) for b in branches}
    return [dict(zip(keys, v)) for v in sorted(seen)]


def label_table(results) -> list[dict]:
    """One row per label branch: the verdict of every printed summand (identical across m, n, r, pair)."""
    rows, seen = [], set()
    for r in results:
        key = tuple(r["branch"][k] for k in LABEL_KEYS)
        if key in seen:
            continue
        seen.add(key)
        rows.append({"branch": dict(zip(LABEL_KEYS, key)),
                     "counts": dict(Counter(x["label"] for x in r["summands"])),
                     "summands": [{"row": x["row"], "col": x["col"],
                                   "term": [list(op) for op in x["term"]], "label": x["label"]}
                                  for x in r["summands"]]})
    return rows


def main() -> None:
    commit = git_commit()
    s = OC.survey()
    result = {
        "scope": "identity (exact monomial algebra; finite bookkeeping over an enumerated branch set)",
        "source": "GU April 1 2021 draft, (9.16) p. 46; typed in experiments/B05/source_operator.py",
        "pairing": pairing_rows(),
        "survey": {"n_branches": s["n_branches"],
                   "label_ok": project(s["label_ok"], LABEL_KEYS),
                   "degree_ok": project(s["degree_ok"], DEGREE_KEYS),
                   "both": s["both"],
                   "label_table": label_table(s["results"])},
        "source_commit": commit,
    }
    OUT.write_text(json.dumps(result, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT}: label_ok={len(result['survey']['label_ok'])} "
          f"degree_ok={len(result['survey']['degree_ok'])} both={len(s['both'])}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 8: Compare the label table with Claude's hand verdicts.** Compare the runner's `label_table` with the hand verdicts in `transcription.md` (Task 1, Step 2). Every disagreement goes in `result.md` with both derivations. Do not edit either side (P3, P6).

**Smoke-test observations (recorded so that reviewers can attack the model; these are not expectations).** On the smoke run of this exact code at master `0f728ae`:
- **Degree:** of the 1280 branches, only those with a metric pairing, exterior d₀ and ⊚ = (m=1, n=0, r=1) make every summand's degree consistent.
- **Labels:** no label branch makes every printed summand `ok` or `mixed`.
- **The nearest label branch** is (chirality, target_source, Dirac adjoint, A-adjoint, Clifford d₀): 16 `ok` and 2 `ill_typed`, the two diagonal ϖ̄* summands. But Clifford d₀ fails the degree check.

The likely culprits are a missing branch (B05-Q, or ⊚ acting on the spinor factor) or the model of ϖ̄*. Task 1's hand verdicts and Task 2's second reader are what decide this. The code does not.

### Task 5: Transformation-law sheet, reality branches, README (Claude)

**Files:**
- Create: `experiments/B05/spec.md`, `experiments/B05/README.md`

- [ ] **Step 1: The generator families.** Give one section per family:
  - Seedhe ℋ, (ε, 0);
  - Tedha ℋ_τ, (6.4);
  - translations 𝒩, (0, ϖ);
  - the central phase iI;
  - the axial phase iC;
  - the chiral boost C;
  - Spin(7,7) frame rotations, if the draft lets them act separately.

  For each family, state its action on ε, ϖ, A₀/d₀, ζ, ζ̄, ν and ν̄, and on the coefficients ϖ_{±±} and ϖ̄*. Cite the page where the draft states the action. Where it does not, list the branches: the bar transforms by the A-adjoint (−S^♯), or independently, as for "four distinct fields". Use `pairing.u1_membership` to state which U(1)s lie in 𝔲(64,64) under each invariant form. Do not conclude anything about whether GU gauges them.
- [ ] **Step 2: Reality branches.**
  - R0: none (four independent fields; Berezinian; complex action).
  - R1: ψ̄ = ψ†A, with A either invariant form.
  - R2: a Majorana condition at (7,7) via J, possible because J² = +1 there. It needs an explicit choice of fixed subspace, and it must say how the central phase acts on it.
  - R2′: at (9,5), J² = −1, so any reality condition needs a doubled (symplectic Majorana) space. It is **not** Jψ = ψ.

  For each branch, say which generator families preserve it, citing `pairing.py` facts or hand derivations.
- [ ] **Step 3: The invariance criterion.** Write down the full variation for a bilinear ψ̄Kψ under each bar branch: δ(ψ̄Kψ) = ψ̄(S̄K + KS + δK)ψ, with S̄ = −S^♯ (R1) or free (R0). Pre-register the control the later covariance test must pass: K anticommuting with C, both fields transforming with C, so S̄ = −C^♯. It must come out invariant while [K,C] ≠ 0. Compute S̄ by hand for both invariant forms, and record whether the example is invariant under R1 (it depends on A·C = −C·A). This criterion, not a commutator, is what the later plan implements.
- [ ] **Step 4: Status table.** For every item, mark it `specified (page)`, `branched (IDs)` or `unspecified (looked: pages)`. The items are: field types, operator entries, pairing, the meaning of ±, d₀, ⊚ on spinors, the bar, the reality condition, and each family's transformation law. Add the lower-right "non-trivial map" alternative as `unspecified`.
- [ ] **Step 5: README.**
  - The question.
  - What this stage established: the pairing facts and the survey, with numbers from `result.json`.
  - What remains open.
  - Exactly what the covariance test needs as input. List which branch combinations it will run on, and which it cannot yet run on and why.
  - Provenance: commits and the hash.
  - Scope, stated exactly: no gauge-symmetry, anomaly or unitarity verdict.
- [ ] **Step 6: Commit** `spec.md` and `README.md` with an explicit pathspec (Claude).

### Task 6: Audit and register (Codex)

- [ ] **Step 1:** Audit every number and claim in `README.md` and `spec.md` against `result.json`, `transcription.md`, `np_objection.md` and the rendered pages. Write `.agent-handoff/b05-task6/readme-audit.md`. Do not edit Claude's files.
- [ ] **Step 2:** Update the B05 entry in `docs/gaps/register.md`: the status, and the next check as stated in the README, linking tracked files only. Commit it with its own pathspec.
- [ ] **Step 3 (Claude):** Resolve the audit findings in the README/spec, then re-run the decisive checks (P7):
  - `uv run pytest -q`;
  - the runner in a clean clone at the code commit, with `result.json` identical except for `source_commit`;
  - the six faults RED.

  Then update HANDOFF.

## After this plan

The covariance test (B05 proper) gets its own plan. Its inputs are `spec.md`'s criterion and the surviving branch set. B04 and B07 are re-ranked against what `spec.md` leaves `unspecified`. In particular: if the operator cannot be pinned without the action, B07's one-direction variation comes next (Grok's fallback).
