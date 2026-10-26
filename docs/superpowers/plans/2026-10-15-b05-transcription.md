# B05 Fermionic-Sector Transcription and Specification Plan (rev 1.2)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking. In this project Claude owns transcriptions, specifications and plans; Codex (pane 0:3) owns code, tests and the register (P6). Read `docs/methods.md` (P1–P11) first.

**Goal:** Produce a reviewed, typed specification of GU's fermionic sector that is complete enough to *pose* B05's covariance test: the operator (9.16) with its alternatives, every field's type, the pairing, the candidate reality conditions, and each candidate generator's action on every field. Everything the draft leaves open is either branched or marked `unspecified`. **This plan delivers no verdict on any gauge symmetry, anomaly, or reality condition.**

**Revision 1 (2026-10-15).** This revision folds in the independent reviews by Codex (`notes:b05-plan-review/result.md`, two subagents, verdict *revise*, 7 findings) and Grok (`notes:b05-plan-review-grok/result.md`, verdict *revise*, 5 findings).
- **R1 sign (both reviews, high).** Rev 0 required S̄ = −S♯ for the Dirac-adjoint branch. That is wrong: with ψ̄ = ψ†A and A fixed, δψ̄ = ψ̄S♯, where S♯ = A⁻¹S†A. Rev 0's pre-registered axial control passed only because of the extra minus. The criterion is now S̄ = S♯ for R1. The controls are now executable tests (`test_r1_dirac_adjoint_variation`, `test_r0_independent_bar_variation`, and the (2,2) flip), plus a seeded fault, F8, that reinstates the old minus.
- **Survey semantics (Codex 2, Grok 2).**
  - Statuses now separate `nonzero`, `pairs_to_zero` (a legal zero), `extended_zero`, `undetermined` and `domain_mismatch`.
  - The predicates are renamed to `well_typed` and `all_nonzero_under_model`.
  - New axes: `HOM` (strict versus extend-by-zero) and `STARPARSE` (is the printed ∗ in front of ⊚ an extra star, or (8.1)'s own outer \*ⁿ?).
  - Every survey predicate is labelled model-relative. The README may not report it as a property of GU, and the next plan receives every branch with its status, not a survivor list.
- **The r range (Codex 3).** Φ_r now runs over r = 0…14, per Definition 8.1 and (8.6)–(8.7) on pp. 41–42. The degree-consistent set has 4 members, including r = 11.
- **Adjoint tests (Codex 4, Grok 4).** The A-adjoint rule is now checked against independent 2×2 integer matrices for both label readings, and a new fault, F7, catches its removal. The mass control uses a degree-0 `endo` primitive and asserts degree too. There is a negative degree control.
- **Signature labels (Codex 5).** Under the signature reading, the support of d₀ is `undetermined`, not proven mixed, and empty support stays empty.
- **P4 (Codex 6).** One boundary, `as_int` via `gu.cliffform.exact`, is used for degrees and the branch numbers m, n, r. `signature_of` rejects non-Hermitian input.
- **Faults (Codex 7).** `faults.py` now asserts nonzero exit, an AssertionError, no collection error and the named failing test. It restores the original bytes in `finally`, checks them by SHA-256, and exits 1 on any GREEN.
- **U(64,64) (Grok 3).** The two forms are labelled *candidate* representatives. p. 24 prints no Hermitian form.
- **Signs (Grok 5).** `ENTRIES` now carries the printed sign of every summand.
- **Smaller fixes (Codex).**
  - Step 2's expected error text is corrected.
  - `__init__.py` ownership is fixed.
  - Task 2 needs a fresh reader.
  - The NP ownership exception is now explicit.
  - Translations are written (1, ϖ) at group level.

**Revision 1.1 (2026-10-15).** This revision folds in the confirmation reviews of rev 1 (`notes:b05-plan-review{,-grok}/rev1/result.md`): Grok *accept*, Codex *accept with fixes*. Codex's fixes:
- **A:** the fault anchors are translated to the file's newline convention, and the script is verified on a CRLF checkout.
- **B:** summand signs go through `as_int` and must be ±1, with controls.
- **C:** the degree denominator is 360, not 90.
- **Task 6:** the register is committed only after the audit findings are resolved.
- **Wording:** the stale "survivor list" language in the Global Constraints is replaced.

**Revision 1.2 (2026-10-15).** This revision folds in argon's audit of rev 1.1, which the user relayed. Claude verified each point against the code before adopting it.
- **Bar-label convention.** If ζ̄₋ denotes the Dirac adjoint labelled by its own right C-eigenvalue, ζ̄₋ := (ζ₊)†A, then it pairs equal labels. That matches the row order (ζ̄₋, ζ̄₊, …) against the column order (ζ₊, ζ₋, …) in (9.16). Combinatorially it is the `dual_field` branch, so the code is unchanged apart from the docstring and comment. Branch B05-B must record both conventions.
- **The (ζ̄₋, ζ₋) cell collision becomes a required hand derivation.** ∗⊚(d₀ζ₋ + ϖ₊₋ζ₋) adds two summands. Under every enumerated chirality reading with exterior d₀, they have different target labels or one is outside its domain, so at most one pairs nonzero (Claude's check: `(zb-, z-)` statuses are `[pairs_to_zero, nonzero]`, `[nonzero, pairs_to_zero]`, or one `domain_mismatch`). This is stated as a property of the enumerated readings, not of the draft.
- **R1 with A fixed.** In R1, A is a fixed algebraic matrix (δA = 0) for internal and axial transformations. If A were instead transformed by congruence to stay invariant, δA = −(S†A + AS), and the law reverts to the contragredient S̄ = −S. That is its own named branch, not R1.
- **README framing.** The README must use argon's diagnostic wording for `all_nonzero_under_model = 0` (Task 5, Step 5).

**Why this comes first.** Codex and Grok reviewed independently which register item should come next (`notes:next-item-{codex,grok}/result.md`). Both agreed on these points:
- A covariance or rejection test has nothing to fail against until the kinetic operator is pinned. No B01–B03 output pins one.
- A generator must be tested by transforming barred fields, unbarred fields, connection, Clifford data and dressings together. A commutator with a frozen operator measures a stabilizer, not a gauge symmetry. For example, if K anticommutes with C, the axial phase S = iC leaves ψ̄Kψ invariant under the Dirac-adjoint law even though iC ∉ 𝔲(A). Under an independent bar with S̄ = S = C, it is invariant too, even though [K,C] ≠ 0.
- B03's J is not a default reality condition. At (9,5), J² = −1, so Jψ = ψ has no nonzero solution. At (7,7), choosing a fixed real subspace is extra input. The Dirac pairing A is a different operator from J.
- Removing a classical non-symmetry removes a premise of Nguyen–Polya §3.2. It does not test their anomaly conclusion, which concerns the earlier U(128) setup.

**Architecture.**
- **Documents (Claude):**
  - `experiments/B05/transcription.md`: the verbatim source, a symbol table, the branch register and hand derivations;
  - `experiments/B05/source_operator.py`: the typed (9.16);
  - `experiments/B05/spec.md`: the transformation-law sheet and specification status;
  - `experiments/B05/README.md`.
- **Code (Codex):**
  - `experiments/B05/pairing.py`: exact facts about the two candidate Spin-invariant Hermitian forms, and the bilinear-variation criterion;
  - `experiments/B05/operator_check.py`: label and form-degree bookkeeping of (9.16) over an enumerated branch set;
  - `experiments/B05/run.py`, which writes `result.json`.
- **Second source (Codex):** `experiments/B05/np_objection.md`, a transcription of Nguyen–Polya §3.2 with a map from its objects to those of the April draft.

**Tech Stack:** Python ≥ 3.12 via `uv`; exact monomial matrices from `gu.clifford` (int64 perm/phase); no floats; pytest. Page rendering uses PyMuPDF via `uv run --no-project --with pymupdf` (scratch only, not a project dependency).

**Spec:** `docs/superpowers/specs/2026-10-14-gu-steelman-design.md` (rev 4.1). Register entries are B05 (with B04 and B07 as cross-references) in `docs/gaps/register.md`.

## Global Constraints

- **Source.** The GU draft is the same PDF as in B01–B03: SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, at `notes:b01-task4/evidence/GU-draft.pdf`. Pages are read as rendered images. Text extraction is a cross-check only, because it drops ⊚, ϖ, the bars and the subscripts in (9.16).
- **No verdicts.** The full branch table and its model-relative predicates are recorded, never asserted. An empty predicate list is something to explain in `transcription.md`/`spec.md`; it is neither an implementation failure nor a finding about GU.
- **Exactness (P4).** No floats anywhere. `pairing.py` uses only `gu.clifford.Mono` algebra.
- **Expected values come from outside the code under test (P3).** Every asserted value is either a textbook control (the Weyl kinetic term, a vanishing same-chirality bilinear, the Dirac mass coupling) or a hand derivation written in the test docstring and in `transcription.md` §Hand derivations.
- **Small first (P5).** The pairing facts run on (3,1), (1,3) and the (2,2) control before (7,7) and (9,5).
- **Seeded faults (P2).** F1–F8 below must each fail an **assertion** in the named test, and the original bytes must be restored and SHA-verified. `faults.py` enforces both and exits 1 otherwise. It is a scratch file and is never committed.
- **Model-relative survey.** Every survey predicate (`well_typed`, `all_nonzero_under_model`, `degree_ok`) is a property of the enumerated readings in `operator_check.py`, not of the draft. Readings the code does not enumerate (branch register: B05-Q and any found in Task 2) can change it.
- **Candidate forms.** GU p. 24 embeds complex Dirac Spin(7,7) in U(64,64) without printing a Hermitian form. `pairing.forms` gives two candidate representatives, and every statement using them is labelled as such.
- **Commits.** On master. Run `git add -- <new paths>` first, then `git commit -m … -- <paths>`, never a bare commit. Commit the producing code before `result.json` (P8). Codex's trailer is `Co-Authored-By: Codex <noreply@openai.com>`, Claude's is `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- **Untouchables.** Do not touch the untracked `argon*.md` files or `<lean-worktree>`. No Fable spend.

## Review Focus

These are the failure modes most likely to produce a wrong specification, with the test or step that pins each one:
1. **A reading silently chosen where the draft is open.** The ± on ϖ, the bar, ϖ̄*, d₀ and ⊚ on spinor-valued forms are all ambiguous. Each is an enumerated axis in `operator_check.py` and a numbered branch in `transcription.md`. The second reader (Task 2) must find any axis we missed.
2. **A wrong chirality pairing.** The draft's row and column labels only make sense relative to which chiralities ψ̄ pairs. `test_forms_pair_opposite_chirality_when_q_odd` pins A·C = −C·A at (7,7) and (9,5) for both invariant forms, with the (2,2) impostor where they commute.
3. **The axial U(1) assumed to be in the structure algebra.** `test_u1_membership` pins that iC ∉ 𝔲(A) while C ∈ 𝔲(A) whenever A·C = −C·A. The (2,2) control shows the opposite. Whether GU actually gauges either one is a Task 5 question, not a test.
4. **A wrong or frozen-operator variation criterion.** The variation is δ(ψ̄Kψ) = ψ̄(S̄K + KS + δK)ψ, with S̄ = S♯ for R1, S̄ free for R0, and the contragredient law S̄ = −S as its own named option. `test_r1_dirac_adjoint_variation` pins, for K = Γ₀ and both candidate forms at (3,1), (7,7) and (9,5):
   - S = iC is invariant;
   - S = C is **not** invariant;
   - S = iI is invariant.

   `test_r0_independent_bar_variation` pins S̄ = S = C as invariant and S̄ = −S as not. The (2,2) control flips both, and F8 reinstates rev 0's sign error and turns red.
5. **A survey read as a fact about GU.** A survivor list, or the lack of one, depends on the enumerated axes. The README must say so, and the next plan receives all branches with their statuses.
6. **A transfer of NP's U(128) objects to U(64,64) without justification.** `np_objection.md` maps every NP object to an April-draft object or to `no counterpart`, and no row is filled by analogy alone (Task 3).

## File structure

| Path | Owner | Responsibility |
|---|---|---|
| `experiments/B05/__init__.py` | Claude (created in Task 1 with the typed data) | package marker |
| `experiments/B05/transcription.md` | Claude | verbatim source, symbol table (P11 lookups recorded), branch register, hand derivations |
| `experiments/B05/source_operator.py` | Claude | typed (9.16): rows, columns, entries as summands of primitives |
| `experiments/B05/np_objection.md` | Codex (an explicit exception to P6: a second-source transcription, which Claude reviews in Task 5) | NP §3.2 transcription and object map |
| `experiments/B05/pairing.py` | Codex | candidate invariant Hermitian forms: chirality relation, signature, U(1) membership, S♯, bilinear variation |
| `experiments/B05/operator_check.py` | Codex | label status and degree bookkeeping per summand, branch enumeration, model-relative survey |
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
sha256sum notes:b01-task4/evidence/GU-draft.pdf   # expect 3f28d742…186d4
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
  - **Symbol table.** Record that no Hermitian form is printed on p. 24, so the forms used are candidate representatives. Then list each symbol with its type and the page where it is defined, or `not defined (looked: pp. …)`. It must include at least: ⊚ (the Shiab family of §8, here applied to spinor-valued forms); ϖ, ϖ₊₊, ϖ₊₋, ϖ₋₊, ϖ₋₋; ϖ̄*; d₀ and d₀*; ∗; ρ(ε) and ρ(ε⁻¹); the bar; $; A (not printed in §9.3, so state that); ε; 𝒢, ℋ, 𝒩; τ_{A₀}; ℋ_τ ("Tedha") versus "Seedhe"; 𝒟 and χ in (9.17); ϒ^F.
  - **Branch register:** number each open reading. At minimum, branches B05-L (meaning of ±), B05-O (subscript order), B05-B (bar), B05-J (ϖ̄*), B05-P (pairing), B05-D (d₀), B05-S (⊚ parameters m, n, r), B05-H (strict Hom versus extension by zero), B05-X (printed ∗ in front of ⊚: an extra star, or (8.1)'s outer \*ⁿ), B05-Q (whether ⊚ preserves spinor labels; the code assumes it does), B05-R (reality condition) and B05-T (transformation laws). Codex's review lists further readings to register, none of which is enumerated:
  - Φ acting on the spinor factor;
  - coefficient labels in a different system from field labels;
  - index placement before or after the adjoint;
  - d₀ as d + d\*;
  - row-dependent pairings;
  - sums of Shiab terms. For each, give the readings, the textual evidence, and whether `operator_check.py` enumerates it. B05-Q, B05-R and B05-T are **not** enumerated by code; say so.
  - **Hand derivations (P3):** the expected values that Task 4's tests assert:
    1. AC = (−1)^q CA for A a product of q gammas, in even dimension;
    2. a Hermitian monomial form anticommuting with C has signature (n/2, n/2);
    3. (iC)†A + A(iC) = i(AC − CA), and C†A + AC = CA + AC;
    4. on a 14-dimensional 1-form, ∗(⊚_{m=1,n=0,r=1}(ϖ ∧ ζ)) has degree 1;
    5. the three textbook controls: ψ̄₋ ∂̸ψ₋ is consistent, ψ̄₋ψ₋ vanishes, and ψ̄₋ m ψ₊ is the mass coupling.
  - **The cell collision (hand derivation 6):** derive by hand, for cell (ζ̄₋, ζ₋) = ∗⊚(d₀ζ₋ + ϖ₊₋ζ₋), the target label and form degree of each summand under every enumerated chirality reading, for both bar conventions (B05-B: the label of the unbarred field, or the barred field's own right C-eigenvalue). Show that, with exterior d₀ and a label-preserving ⊚, the two summands cannot both pair nonzero. List which unenumerated readings could reconcile them, without choosing one:
    - ⊚ acting on spinor labels;
    - a frame or Clifford piece in d₀;
    - ϖ labels in a different system from the field labels.
  - **Hand verdicts:** at least four summands of (9.16) under two named branches, derived by hand **before** Task 4 runs. They are pre-registered predictions; the runner's table is compared with them in Task 4, Step 6.

- [ ] **Step 3: Write `source_operator.py`** exactly as below. The entries are read off the p. 46 image. The operator has 12 nonzero entries containing 18 summands, each with its printed sign: + in the upper rows and − in the lower rows. Its lower-right 2×2 is zero. The ρ(ε)/ρ(ε⁻¹) decorations are carried only by `transcription.md`; a covariance plan must read them from there.

```python
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
```

- [ ] **Step 4: Commit** (Claude):

```bash
git add -- experiments/B05/__init__.py experiments/B05/transcription.md experiments/B05/source_operator.py
git commit -m "B05 transcription rev 0 and typed (9.16)" -- experiments/B05/__init__.py experiments/B05/transcription.md experiments/B05/source_operator.py
```

### Task 2: Blind second reading (Codex), then transcription rev 1 (Claude)

**Files:**
- Create (untracked): `notes:b05-transcription/second-reader.md`, `transcription-comparison.md`
- Modify: `experiments/B05/transcription.md` (rev 1), and, if the comparison requires it, `source_operator.py`

- [ ] **Step 1 (Codex, blind, fresh reader):** Assign this to a fresh subagent that has seen neither this plan nor the plan reviews, which contain the typed matrix. Without opening `experiments/B05/transcription.md` or `source_operator.py`, render the same pages and write `second-reader.md` from scratch. Include:
  - (9.16) entry by entry;
  - the symbol table;
  - every reading you think the draft leaves open;
  - for each operator entry, the field types it connects.
- [ ] **Step 2 (Codex):** Now compare against Claude's rev 0. Write `transcription-comparison.md` with one row per disagreement: the item, Claude's text, yours, the page, and which reading the image supports. List every open reading that Claude's branch register does not have.
- [ ] **Step 3 (Claude):** Fold the comparison into rev 1 and record each change in a revision note, as B03 rev 1 did. If an entry of `source_operator.py` changes, Task 4 has not started yet, so the edit is a transcription fix. Commit `transcription.md`, and `source_operator.py` if changed, with an explicit pathspec.

### Task 3: Nguyen–Polya §3.2 and its object map (Codex)

**Files:**
- Create: `experiments/B05/np_objection.md`
- Create (untracked evidence): `notes:b05-np/NP.pdf` and its SHA-256

- [ ] **Step 1:** Download `https://files.timothynguyen.org/geometric_unity.pdf` into `notes:b05-np/` and record the SHA-256 and the access date. Render pp. 6–7 and transcribe §3.2 verbatim.
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
"""B05 transcription-stage checks. Controls validate the tools; branch-survey outcomes are recorded by the runner, not asserted."""
from fractions import Fraction

import numpy as np
import pytest

from experiments.B05 import operator_check as OC
from experiments.B05 import pairing as PR
from experiments.B05 import source_operator as SRC
from gu.clifford import Mono, chirality, gammas

SIGS = [(3, 1), (1, 3), (7, 7), (9, 5)]


# ---- pairing.py: forms and U(1)s ----------------------------------------------------------------------------

@pytest.mark.parametrize("p,q", SIGS + [(2, 2)])
def test_both_forms_are_spin_invariant_hermitian(p, q):
    """Control, identity: products of all timelike (resp. spacelike) gammas give Spin(p,q)-invariant Hermitian forms."""
    for A in PR.forms(p, q).values():
        assert A.dagger() == A
        assert PR.invariant(p, q, A)


@pytest.mark.parametrize("p,q", SIGS)
def test_forms_pair_opposite_chirality_when_q_odd(p, q):
    """Identity: A anticommutes with C for (3,1), (1,3), (7,7), (9,5).

    Hand derivation: A is a product of q (or p) gammas, each anticommuting with C in even dimension, so
    AC = (-1)^q CA, and p, q are odd here.
    """
    for A in PR.forms(p, q).values():
        assert PR.relation_to_chirality(p, q, A) == "anticommute"


def test_forms_commute_with_chirality_at_2_2():
    """Control, identity: q = 2 even, so AC = CA (ambient impostor for the q-odd rule)."""
    for A in PR.forms(2, 2).values():
        assert PR.relation_to_chirality(2, 2, A) == "commute"


@pytest.mark.parametrize("p,q", [(3, 1), (1, 3), (7, 7), (9, 5)])
def test_neutral_signature(p, q):
    """Identity: a Hermitian form anticommuting with the involution C swaps its +-1 eigenspaces, so has signature (n/2, n/2)."""
    for A in PR.forms(p, q).values():
        assert PR.signature_of(A) == (A.n // 2, A.n // 2)


def test_signature_of_rejects_non_hermitian():
    """P4-style boundary: an anti-Hermitian 2-cycle iX is not a form."""
    iX = Mono([1, 0], [1, 1])
    with pytest.raises(ValueError):
        PR.signature_of(iX)


@pytest.mark.parametrize("p,q", SIGS)
def test_u1_membership(p, q):
    """Identity: when AC = -CA, iI and C are in u(A) but the axial phase iC is not.

    Hand derivation: (iC)^dag A + A(iC) = i(AC - CA) = 2iAC != 0; C^dag A + AC = CA + AC = 0.
    """
    for A in PR.forms(p, q).values():
        assert PR.u1_membership(p, q, A) == {"central_iI": True, "axial_iC": False, "chiral_boost_C": True}


def test_u1_membership_flips_at_2_2():
    """Control, identity: when AC = CA (q even), iC is in u(A) and C is not."""
    for A in PR.forms(2, 2).values():
        assert PR.u1_membership(2, 2, A) == {"central_iI": True, "axial_iC": True, "chiral_boost_C": False}


# ---- pairing.py: bilinear variations (Task 5's criterion, pre-registered) ------------------------------------

def _k_c_i(p, q):
    G, C = gammas(p, q), chirality(p, q)
    return G[0], C, Mono.identity(C.n)


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_r1_dirac_adjoint_variation(p, q):
    """Identity, hand-derived. R1: psibar = psi^dag A, A fixed, so delta psibar = psibar S^sharp, S^sharp = A^-1 S^dag A.

    K = Gamma_0 anticommutes with C. With AC = -CA:
      S = iC:  (iC)^sharp = iC,  sum = i{C,K} = 0       -> invariant (axial phase, though iC is not in u(A));
      S = C:   C^sharp = -C,     sum = [K,C] = 2KC != 0  -> NOT invariant;
      S = iI:  (iI)^sharp = -iI, sum = -iK + iK = 0      -> invariant.
    """
    K, C, I = _k_c_i(p, q)
    for A in PR.forms(p, q).values():
        iC, iI = C.times_i_power(1), I.times_i_power(1)
        assert PR.sharp(iC, A) == iC and PR.sharp(C, A) == -C
        assert PR.bilinear_invariant(K, iC, PR.sharp(iC, A))
        assert not PR.bilinear_invariant(K, C, PR.sharp(C, A))
        assert PR.bilinear_invariant(K, iI, PR.sharp(iI, A))


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_r0_independent_bar_variation(p, q):
    """Identity, hand-derived. R0: psibar independent. With Sbar = C and S = C: sum = {C,K} = 0 -> invariant.
    With the contragredient law Sbar = -S = -C: sum = [K,C] != 0 -> not invariant. The law must be specified."""
    K, C, _ = _k_c_i(p, q)
    assert PR.bilinear_invariant(K, C, C)
    assert not PR.bilinear_invariant(K, C, -C)


def test_r1_variation_flips_at_2_2():
    """Control, identity: when AC = CA, C^sharp = C, so S = C gives {C,K} = 0 (invariant) and S = iC gives i[K,C] != 0."""
    K, C, _ = _k_c_i(2, 2)
    for A in PR.forms(2, 2).values():
        iC = C.times_i_power(1)
        assert PR.bilinear_invariant(K, C, PR.sharp(C, A))
        assert not PR.bilinear_invariant(K, iC, PR.sharp(iC, A))


# ---- operator_check.py: the A-adjoint label rule against independent 2x2 matrices ----------------------------

LAB = {"+": 0, "-": 1}


def _support(M):
    """{(source label, target label)} of the nonzero entries of an integer 2x2 matrix in the basis (+, -)."""
    inv = {0: "+", 1: "-"}
    return {(inv[j], inv[i]) for i in range(2) for j in range(2) if M[i, j] != 0}


@pytest.mark.parametrize("label,A", [("chirality", np.array([[0, 1], [1, 0]])),     # anticommutes with C=diag(1,-1)
                                     ("signature", np.array([[1, 0], [0, -1]]))])   # labels = A's own eigenspaces
@pytest.mark.parametrize("order", OC.ORDER)
def test_a_adjoint_rule_matches_matrices(label, A, order):
    """Control: for every elementary block E (source b -> target a), the support of A^-1 E^T A equals varpi_map's
    rule for varpibar*. Independent of the rule's code: plain integer matrices, real entries, so E^dag = E^T,
    and A^-1 = A for both test forms (A^2 = I)."""
    assert (A @ A == np.eye(2, dtype=int)).all()
    for a in "+-":
        for b in "+-":
            src, tgt = OC.varpi_map(("varpi", a, b), label, order, "a_adjoint")
            E = np.zeros((2, 2), dtype=int)
            E[LAB[tgt], LAB[src]] = 1
            assert _support(A @ E.T @ A) == {OC.varpi_map(("varpibar_star", a, b), label, order, "a_adjoint")}


def test_subscript_swap_is_a_different_reading():
    """Control: under chirality labels the two adjoint readings disagree on varpibar*_{+-}."""
    a = OC.varpi_map(("varpibar_star", "+", "-"), "chirality", "target_source", "a_adjoint")
    s = OC.varpi_map(("varpibar_star", "+", "-"), "chirality", "target_source", "subscript_swap")
    assert a != s


# ---- operator_check.py: textbook controls --------------------------------------------------------------------

ROWS_T = {"pb-": (0, "-"), "pb+": (0, "+"), "zb-": (1, "-")}
COLS_T = {"p+": (0, "+"), "p-": (0, "-")}
TEXTBOOK = dict(label="chirality", order="target_source", bar="dirac_adjoint", adj="a_adjoint", hom="strict",
                pair="metric", d0kind="clifford", starparse="extra_star", m=0, n=0, r=0)


def _statuses(entries, br=TEXTBOOK):
    out = OC.check(br, entries, ROWS_T, COLS_T)
    return [x["status"] for x in out["summands"]], [x["degree_ok"] for x in out["summands"]]


def test_textbook_dirac_kinetic_term():
    """Control: psibar_- (dslash psi_-) is the textbook Weyl kinetic term psi_L^dag sigma.d psi_L: nonzero, degree ok."""
    assert _statuses({("pb-", "p-"): ((+1, (SRC.D0,)),), ("pb+", "p+"): ((+1, (SRC.D0,)),)}) == \
        (["nonzero", "nonzero"], [True, True])


def test_same_chirality_scalar_bilinear_is_a_legal_zero():
    """Control: psibar_L psi_L = 0 (a mass term couples L to R). Legal and identically zero, not a type error."""
    e = {("pb-", "p-"): ((+1, (("endo", "-", "-"),)),)}
    assert _statuses(e) == (["pairs_to_zero"], [True])
    assert OC.check(TEXTBOOK, e, ROWS_T, COLS_T)["well_typed"]


def test_mass_term():
    """Control: psibar_- m psi_+ with a degree-0 endomorphism + -> + is the textbook Dirac mass coupling."""
    assert _statuses({("pb-", "p+"): ((+1, (("endo", "+", "+"),)),)}) == (["nonzero"], [True])


def test_degree_mismatch_detected():
    """Negative control: a 1-form-valued block between two 0-form fields fails the metric degree check."""
    assert _statuses({("pb-", "p+"): ((+1, (SRC.W("+", "+"),)),)})[1] == [False]


def test_domain_mismatch_vs_extension_by_zero():
    """Control: varpi_{+-} (target +, source -) on a + field: a type error if strict, the zero map if extended."""
    e = {("pb-", "p+"): ((+1, (SRC.W("+", "-"),)),)}
    assert _statuses(e)[0] == ["domain_mismatch"]
    assert _statuses(e, dict(TEXTBOOK, hom="extend_by_zero"))[0] == ["extended_zero"]


def test_signature_labels_leave_d0_undetermined():
    """Control: under the signature reading the support of d0 psi is not established (a flat d0 preserves an
    A-eigenvector; a boost-valued connection mixes), so the status is 'undetermined', not a proven mix."""
    br = dict(TEXTBOOK, label="signature", d0kind="exterior")
    assert _statuses({("zb-", "p-"): ((+1, (SRC.D0,)),)}, br)[0] == ["undetermined"]


def test_degree_bookkeeping_by_hand():
    """Control: on a 1-form in 14D, *(shiab_{m=1,n=0,r=1}(varpi ^ zeta)) has degree 14 - (14 - 2 + 1) = 1, and the
    outer_star parse of the same printed symbols (shiab with n=1, no extra star) also gives 14 - (12 + 1) = 1."""
    br = dict(TEXTBOOK, d0kind="exterior", m=1, n=0, r=1)
    k = 1
    for op in reversed((SRC.S, SRC.SH, SRC.W("+", "+"))):
        k = OC.degree(op, k, br)
    assert k == 1
    ob = dict(br, starparse="outer_star", n=1)
    k = 1
    for op in reversed(OC.parse((SRC.S, SRC.SH, SRC.W("+", "+")), ob)):
        k = OC.degree(op, k, ob, 1 if op == ("shiab", "outer") else None)
    assert k == 1


# ---- P4 boundary ---------------------------------------------------------------------------------------------

def test_p4_boundary():
    """P4: degrees, branch numbers and summand signs are exact integers (signs +-1); floats and non-integral rationals are rejected."""
    with pytest.raises(TypeError):
        OC.degree(SRC.D0, 1.5, TEXTBOOK)
    with pytest.raises(ValueError):
        OC.degree(SRC.D0, Fraction(3, 2), TEXTBOOK)
    with pytest.raises(TypeError):
        OC.degree(SRC.SH, 1, dict(TEXTBOOK, r=1.0))
    with pytest.raises(TypeError):
        OC.check(TEXTBOOK, {("pb-", "p+"): ((1.5, (("endo", "+", "+"),)),)}, ROWS_T, COLS_T)
    with pytest.raises(ValueError):
        OC.check(TEXTBOOK, {("pb-", "p+"): ((2, (("endo", "+", "+"),)),)}, ROWS_T, COLS_T)
    big = OC.as_int(np.int64(2**62))
    assert type(big) is int and big * 4 == 2**64


# ---- branch space and transcription shape --------------------------------------------------------------------

def test_branch_space_is_complete():
    """Control: 2^7 label/pairing axes x (extra_star: 2*2*15 + outer_star: 2*1*15) = 128 * 90 = 11520 distinct branches."""
    bs = OC.branches()
    assert len(bs) == 11520
    assert len({tuple(b.values()) for b in bs}) == 11520


def test_transcription_shape():
    """Control on Claude's typed data: 12 nonzero entries, 18 summands, lower-right absent, the 6 lower-row summands
    carry the printed minus and the 12 upper-row summands carry plus (p. 46)."""
    assert len(SRC.ENTRIES) == 12
    terms = [(r, s) for (r, _), ts in SRC.ENTRIES.items() for s, _ in ts]
    assert len(terms) == 18
    assert not any(r.startswith("nb") and c.startswith("n") for r, c in SRC.ENTRIES)
    assert all(s == (-1 if r.startswith("nb") else +1) for r, s in terms)


def test_survey_is_recorded_not_asserted():
    """The survey runs on every branch and returns per-summand statuses from the allowed set."""
    s = OC.survey()
    assert s["n_branches"] == 11520
    assert all(x["status"] in OC.STATUSES for r in s["results"] for x in r["summands"])
```

- [ ] **Step 2: Run them; expect an ImportError for `pairing`/`operator_check`.**

Run: `uv run pytest -q tests/test_b05.py`
Expected: a collection error. The test imports `operator_check` first, so the message is `ModuleNotFoundError: No module named 'experiments.B05.operator_check'` (or an ImportError naming it).

- [ ] **Step 3: Write `experiments/B05/pairing.py`** exactly:

```python
"""B05 Task 4: chirality behaviour of Spin(p,q)-invariant Hermitian forms, the U(1)s they admit, and bilinear variations.

Exact facts about the existing monomial gammas (`gu.clifford`). ASSUMPTION (labelled, not recovered from the
source): GU (3.31), p. 24, embeds complex Dirac Spin(7,7) in U(64,64) but prints no Hermitian form. The two
forms below are candidate representatives of that U(64,64); the draft does not say which, if either, it uses.
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
    """Phase times the product of the spacelike gammas, chosen Hermitian (the other candidate form)."""
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


def sharp(S: Mono, A: Mono) -> Mono:
    """S^sharp = A^-1 S^dagger A. Monomials with unit phases are unitary, so A^-1 = A^dagger."""
    if not A @ A.dagger() == Mono.identity(A.n):
        raise AssertionError("A is not unitary")
    return A.dagger() @ S.dagger() @ A


def bilinear_invariant(K: Mono, S: Mono, Sbar: Mono) -> bool:
    """delta(psibar K psi) = psibar (Sbar K + K S) psi vanishes, for fixed K, delta psi = S psi, delta psibar = psibar Sbar.

    For the R1 (Dirac adjoint, fixed A) branch Sbar = sharp(S, A); for R0 (independent bar) Sbar is free.
    Monomial products are monomials, so Sbar K + K S = 0 iff Sbar K = -(K S).
    """
    return Sbar @ K == -(K @ S)


def signature_of(A: Mono) -> tuple[int, int]:
    """(n_plus, n_minus) of a Hermitian monomial form A; exact via its 1- and 2-cycles."""
    if not A.dagger() == A:
        raise ValueError("signature_of requires a Hermitian form")
    plus = minus = 0
    seen = set()
    for j in range(A.n):
        if j in seen:
            continue
        i = int(A.perm[j])
        if i == j:                                   # diagonal entry of a Hermitian form is +1 or -1
            plus, minus = (plus + 1, minus) if int(A.phase[j]) == 0 else (plus, minus + 1)
            seen.add(j)
        else:                                        # Hermitian 2x2 block [[0, conj z], [z, 0]]: one +, one -
            plus, minus = plus + 1, minus + 1
            seen.update((i, j))
    return plus, minus
```

- [ ] **Step 4: Write `experiments/B05/operator_check.py`** exactly:

```python
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
```

- [ ] **Step 5: Run the tests, then the full suite.**

Run: `uv run pytest -q tests/test_b05.py`
Expected: `43 passed`.

Run: `uv run pytest -q`
Expected: `353 passed` (310 before + 43).

- [ ] **Step 6: Seeded faults (P2).** Save the script below as a scratch `faults.py` in the repo root (never committed). Its anchors are newline-agnostic, so it works on LF and on CRLF (native Windows, `core.autocrlf=true`) checkouts, and run `uv run python faults.py`. Expected: eight `RED` lines and exit 0. The script itself checks that each fault fails the named test on an AssertionError, with no collection error, and that the original bytes are restored. Delete `faults.py` before Step 7.

```python
"""B05 seeded faults (P2). Scratch only: never commit. Exit status 1 unless every fault is RED for the intended reason.

Each fault must (a) make pytest exit nonzero, (b) fail with an AssertionError, not a collection/import error,
and (c) fail the named test. The original bytes are restored in `finally` and checked by SHA-256 of the bytes.
Anchors are written with LF and translated to the file's own newline convention (LF or CRLF).
"""
import hashlib
import pathlib
import subprocess
import sys

OC, PRF = "experiments/B05/operator_check.py", "experiments/B05/pairing.py"
FAULTS = [
    ("F1 Dirac adjoint pairs equal chirality", OC,
     '    if bar == "dirac_adjoint" and label == "chirality":\n        return flip(row_label)\n', '',
     "test_textbook_dirac_kinetic_term"),
    ("F2 Clifford d0 keeps chirality", OC,
     '(frozenset(map(flip, support)) if br["d0kind"] == "clifford" else support)', 'support',
     "test_textbook_dirac_kinetic_term"),
    ("F3 star keeps degree", OC,
     '    if kind == "star":\n        return d - k', '    if kind == "star":\n        return k',
     "test_degree_bookkeeping_by_hand"),
    ("F4 invariance sign", PRF,
     '== -(A @ G[a] @ G[b])', '== (A @ G[a] @ G[b])',
     "test_both_forms_are_spin_invariant_hermitian"),
    ("F5 isometry test without dagger", PRF,
     'return X.dagger() @ A == -(A @ X)', 'return X @ A == -(A @ X)',
     "test_u1_membership"),
    ("F6 shiab ignores *^m", OC,
     'k = d - k if m else k', 'k = k',
     "test_degree_bookkeeping_by_hand"),
    ("F7 varpibar* ignores the A-adjoint chirality flip", OC,
     '            src, tgt = flip(tgt), flip(src)', '            src, tgt = tgt, src',
     "test_a_adjoint_rule_matches_matrices"),
    ("F8 R1 barred generator with the old extra minus", PRF,
     '    return A.dagger() @ S.dagger() @ A', '    return -(A.dagger() @ S.dagger() @ A)',
     "test_r1_dirac_adjoint_variation"),
]
CRLF, LF = "\r\n", "\n"

bad = 0
for name, path, old, new, must_fail in FAULTS:
    p = pathlib.Path(path)
    raw = p.read_bytes()
    h = hashlib.sha256(raw).hexdigest()
    src = raw.decode("utf-8")
    nl = CRLF if CRLF in src else LF                 # native Windows checkouts may be CRLF
    old, new = old.replace(LF, nl), new.replace(LF, nl)
    assert src.count(old) == 1, (name, "anchor not unique")
    try:
        p.write_bytes(src.replace(old, new).encode("utf-8"))
        r = subprocess.run(["uv", "run", "pytest", "-q", "-rf", "tests/test_b05.py"], capture_output=True, text=True)
    finally:
        p.write_bytes(raw)
    assert hashlib.sha256(p.read_bytes()).hexdigest() == h, (name, "restore failed")
    failed = [ln for ln in r.stdout.splitlines() if ln.startswith("FAILED")]
    ok = (r.returncode != 0 and "error" not in r.stdout.splitlines()[-1].lower()
          and "AssertionError" in r.stdout and any(must_fail in ln for ln in failed))
    bad += not ok
    print("RED " if ok else "BAD ", name, f"{len(failed)} failing;", "includes", must_fail if ok else "-")
    if not ok:
        print(r.stdout[-2000:], r.stderr[-2000:])
sys.exit(1 if bad else 0)
```

Expected output (smoke-tested):

```text
RED  F1 Dirac adjoint pairs equal chirality 3 failing; includes test_textbook_dirac_kinetic_term
RED  F2 Clifford d0 keeps chirality 1 failing; includes test_textbook_dirac_kinetic_term
RED  F3 star keeps degree 1 failing; includes test_degree_bookkeeping_by_hand
RED  F4 invariance sign 5 failing; includes test_both_forms_are_spin_invariant_hermitian
RED  F5 isometry test without dagger 5 failing; includes test_u1_membership
RED  F6 shiab ignores *^m 1 failing; includes test_degree_bookkeeping_by_hand
RED  F7 varpibar* ignores the A-adjoint chirality flip 3 failing; includes test_a_adjoint_rule_matches_matrices
RED  F8 R1 barred generator with the old extra minus 4 failing; includes test_r1_dirac_adjoint_variation
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
```

- [ ] **Step 8: Compare the label table with Claude's hand verdicts.** Compare the runner's `label_table` with the hand verdicts in `transcription.md` (Task 1, Step 2). Every disagreement goes in `result.md` with both derivations. Do not edit either side (P3, P6).

**Smoke-test observations (recorded so that reviewers can attack the model; these are not expectations, and not facts about GU).** These come from the rev 1 code, smoke-run at master `0f728ae`: 43/43, full suite 353, F1–F8 RED, runner `well_typed=32 all_nonzero=0 degree_ok=4`.
- **Degree.** 4 of the 360 degree branches (pair × d₀ × 90 Shiab/parse choices) are consistent. All four use a metric pairing and exterior d₀:
  - (extra_star, m=1, n=0, r=1);
  - (extra_star, m=0, n=0, r=11);
  - (outer_star, m=1, r=1);
  - (outer_star, m=0, r=11).

  So both parses of the printed ∗ have degree-consistent readings. No branch with Clifford-type d₀ is degree-consistent.
- **Labels.** 32 of the 64 label branches are `well_typed`, meaning no domain mismatch (zeros allowed). None has all 18 summands `nonzero`. The most nonzero summands is 16, reached by (chirality, target_source, Dirac adjoint, Clifford d₀) under both adjoint readings and both Hom readings. That combination needs Clifford d₀, which fails every degree branch.

Whether this tension is the draft's or the model's is decided by Task 1's hand verdicts, Task 2's fresh reader and the unenumerated readings, not by this code.

### Task 5: Transformation-law sheet, reality branches, README (Claude)

**Files:**
- Create: `experiments/B05/spec.md`, `experiments/B05/README.md`

- [ ] **Step 1: The generator families.** Give one section per family:
  - Seedhe ℋ, (ε, 0) at group level;
  - Tedha ℋ_τ, (6.4);
  - translations 𝒩, (1, ϖ) at group level, per (5.9) on p. 33. State the Lie-algebra form separately;
  - the central phase iI;
  - the axial phase iC;
  - the chiral boost C;
  - Spin(7,7) frame rotations, if the draft lets them act separately.

  For each family, state its action on ε, ϖ, A₀/d₀, ζ, ζ̄, ν and ν̄, and on the coefficients ϖ_{±±} and ϖ̄*. Cite the page where the draft states the action. Where it does not, list the branches: the bar transforms by δψ̄ = ψ̄S♯ (R1, with A fixed; if A transforms, add A⁻¹δA), by the contragredient law δψ̄ = −ψ̄S, or independently, as for "four distinct fields". Use `pairing.u1_membership` to state which U(1)s lie in 𝔲(A) for each **candidate** form. Do not conclude anything about whether GU gauges them.
- [ ] **Step 1b: A is fixed in R1.** State that in R1 the form A is a fixed algebraic matrix (δA = 0) under internal and axial transformations, and changes only through a connection or frame variation when the geometry on Y is varied. If A is instead transformed by congruence so that it stays invariant, then δA = −(S†A + AS) and δ(ψ†Aψ) = 0 forces the contragredient law S̄ = −S. Record that as its own named branch, not as R1.
- [ ] **Step 2: Reality branches.**
  - R0: none (four independent fields; Berezinian; complex action).
  - R1: ψ̄ = ψ†A, with A either invariant form.
  - R2: a Majorana condition at (7,7) via J, possible because J² = +1 there. It needs an explicit choice of fixed subspace, and it must say how the central phase acts on it.
  - R2′: at (9,5), J² = −1, so any reality condition needs a doubled (symplectic Majorana) space. It is **not** Jψ = ψ.

  For each branch, say which generator families preserve it, citing `pairing.py` facts or hand derivations.
- [ ] **Step 3: The invariance criterion.**
  - **The variation.** δ(ψ̄Kψ) = ψ̄(S̄K + KS + δK)ψ, with:
    - S̄ = S♯ = A⁻¹S†A for R1 with A fixed (add A⁻¹δA if A transforms);
    - S̄ free for R0;
    - S̄ = −S for the contragredient law.
  - **Cite the executable controls** in `tests/test_b05.py`. These are the pre-registration the later covariance plan must reproduce with its own operator and dressings. With K anticommuting with C and AC = −CA:
    - R1, S = iC: S̄ = iC, the sum is i{C,K} = 0, so invariant. This holds although iC ∉ 𝔲(A), so membership in 𝔲(A) is not the test.
    - R1, S = C: S̄ = −C, the sum is [K,C] ≠ 0, so **not** invariant. The later test must reject this case.
    - R1, S = iI: invariant.
    - R0, S̄ = S = C: invariant.
    - Contragredient, S̄ = −C: not invariant.
    - The (2,2) control flips the R1 cases.
  - **No GU verdict.** None of this is a statement about GU's K, which is (9.16) with its dressings. It is the criterion the covariance plan implements in place of a commutator.
- [ ] **Step 4: Status table.** For every item, mark it `specified (page)`, `branched (IDs)` or `unspecified (looked: pages)`. The items are: field types, operator entries, pairing, the meaning of ±, d₀, ⊚ on spinors, the bar, the reality condition, and each family's transformation law. Add the lower-right "non-trivial map" alternative as `unspecified`.
- [ ] **Step 5: README.**
  - The question.
  - **Framing of `all_nonzero_under_model = 0`** (argon's wording, adopted). Write it diagnostically, never as "(9.16) has no consistent reading". The wording: "Within the 11,520 branches of the minimal decoupled model (`operator_check.py`, where d₀ is either purely exterior and chirality-preserving or purely Clifford and degree-preserving, and ⊚ acts only on form degree), the degree-consistent branches require exterior d₀. Meanwhile, matching the spinor target labels of d₀ζ₋ and ϖ₊₋ζ₋ inside the same cell requires a chirality-flipping action. Reconciling those two summands therefore needs a reading outside this model (for example B05-Q, or a frame/connection term in d₀)."
  - What this stage established: the pairing facts (labelled with the candidate forms) and the survey. Give the survey numbers from `result.json` **only** with the model caveat, never as a property of GU. Do not state any survivor count as a finding until Task 2's added readings have been either enumerated or recorded as unenumerated.
  - What remains open.
  - Exactly what the covariance test needs as input: the full branch table with statuses, not a filtered survivor list. Say which combinations it can run on now, and which need data the draft does not give, and why.
  - Provenance: commits and the hash.
  - Scope, stated exactly: no gauge-symmetry, anomaly or unitarity verdict.
- [ ] **Step 6: Commit** `spec.md` and `README.md` with an explicit pathspec (Claude).

### Task 6: Audit and register (Codex)

- [ ] **Step 1:** Audit every number and claim in `README.md` and `spec.md` against `result.json`, `transcription.md`, `np_objection.md` and the rendered pages. Write `notes:b05-task6/readme-audit.md`. Do not edit Claude's files.
- [ ] **Step 2 (Claude):** Resolve the substantive audit findings in the README/spec, and commit them.
- [ ] **Step 3 (Codex):** Only after Step 2, update the B05 entry in `docs/gaps/register.md`: the status, and the next check as stated in the final README, linking tracked files only. Commit it with its own pathspec.
- [ ] **Step 4 (Claude):** Re-run the decisive checks (P7):
  - `uv run pytest -q`;
  - the runner in a clean clone at the code commit, with `result.json` identical except for `source_commit`;
  - the eight faults RED (F1–F8).

  Then update HANDOFF.

## After this plan

The covariance test (B05 proper) gets its own plan. Its inputs are `spec.md`'s criterion and the **full** branch table with statuses, together with the unenumerated readings. B04 and B07 are re-ranked against what `spec.md` leaves `unspecified`. In particular: if the operator cannot be pinned without the action, B07's one-direction variation comes next (Grok's fallback).
