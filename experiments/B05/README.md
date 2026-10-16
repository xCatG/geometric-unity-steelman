# B05, transcription and specification stage: the fermionic operator (9.16)

**Status:** specification stage complete, pending the Task 6 audit. This stage reaches **no verdict** on any gauge symmetry, anomaly, reality condition or unitarity question.

## The question

Register entry B05 asks whether the gauged symmetries of GU survive anomaly cancellation. That includes the Nguyen–Polya §3.2 objection: the axial transformations together with the central U(1).

A covariance or anomaly test needs the fermionic kinetic operator and every field's transformation law first. Neither B01–B03 nor, as it turns out, the draft supplies all of them. This stage therefore asks a narrower question. What does the April 2021 draft actually fix about its fermionic operator (9.16), what does it leave open, and what exactly would a covariance test need?

Plan: `docs/superpowers/plans/2026-10-15-b05-transcription.md`, rev 1.2. It was reviewed twice each by Codex and Grok, then by argon, and approved by the user.

## What this stage established

### 1. The operator, transcribed twice

`transcription.md`, rev 1:
- (9.16) is a 4×4 block operator 𝒟̸_ω between the row (ζ̄₋, ζ̄₊, ν̄₋, ν̄₊)_{ρ(ε)} and the column (ζ₊, ζ₋, ν₊, ν₋)_{ρ(ε⁻¹)}.
- It has 12 nonzero entries, made of 18 signed summands, and the lower-right 2×2 is zero.
- Claude's reading and Codex's fresh, blind second reading agree on every entry, sign and decoration.
- The typed form is `source_operator.py`.

### 2. What the draft leaves undefined

None of these was located in the pages read (pp. 24, 31–47, 50–51, 58, 60–62 and the appendix pp. 65–66, 68; a bounded search):
- the bar on ν, ζ;
- the ± on ϖ;
- ϖ̄\*;
- the Hermitian form on $;
- **any transformation law for the fermions** under ℋ, its tilted version ℋ_τ, or 𝒩.

The branch register records 25 open readings:
- 9 are enumerated in `operator_check.py`, as its 11 axes;
- the other 16 are recorded as unenumerated, for example whether ⊚ acts on the spinor factor (B05-Q), how ϖ acts on spinor forms (B05-A), and the transformation laws (B05-T, T′).

### 3. Pairing facts (exact; `pairing.py`; `result.json` `pairing`)

Both candidate Spin(p,q)-invariant Hermitian forms A (timelike and spacelike gamma products) satisfy the following at (3,1), (1,3), (7,7) and (9,5). **The draft prints no form** (p. 24), so these are candidates, not recovered from the source.
- AC = −CA, where C is the chirality.
- The form has neutral signature: (64,64) at (7,7) and (9,5).
- iI ∈ 𝔲(A) and C ∈ 𝔲(A), but the axial phase iC ∉ 𝔲(A).

The (2,2) control, where AC = CA, flips the C relation (commute instead of anticommute) and swaps the membership of C and iC. It keeps neutral inertia (2,2) and iI ∈ 𝔲(A). The R1 toy invariances of C and iC flip too.

The draft agrees independently. (8.5) on p. 42 places Λ¹⁴ (∝ C) in 𝔰𝔬(64,64), and (8.6) omits it from the i-multiplied classes.

### 4. The invariance criterion, corrected and pinned (`spec.md` §3; tests)

The variation is δ(ψ̄Kψ) = ψ̄(S̄K + KS + δK)ψ, with:
- **R1** (Dirac adjoint, A fixed): S̄ = S♯ = A⁻¹S†A;
- **Rc** (contragredient): S̄ = −S;
- **R0** (independent bar): S̄ free.

Rev 0 of the plan had S̄ = −S♯ for R1. Both reviewers caught it; it is now fault F8.

For the toy operator K = Γ₀, under R1:
- the axial phase iC is invariant, although iC ∉ 𝔲(A);
- the chiral boost C is **not** invariant, although C ∈ 𝔲(A).

So membership in 𝔲(A) gets both toy cases wrong. A frozen commutator [K, S] = 0 rejects both: it incorrectly rejects iC and correctly rejects C. Neither substitutes for the full variation. **This is about the toy K, not GU's.**

### 5. The branch survey (`result.json` `survey`; a property of the model, not of GU)

Within the 11,520 branches of the minimal decoupled model in `operator_check.py`:
- d₀ is either purely exterior and chirality-preserving, or purely Clifford and degree-preserving;
- ⊚ acts only on form degree;
- ϖ acts by wedge.

Four of the 360 degree branches are degree-consistent. All use a metric pairing and exterior d₀, with ⊚ parameters (m, r) = (1, 1) or (0, 11), under either parse of the printed ∗.

Under the enumerated chirality readings, making both d₀ζ₋ and ϖ₊₋ζ₋ in the same cell contribute nontrivially, while satisfying the degree conditions, requires an extension of this model (transcription, hand derivation 6). This assumes common chirality labels, label-preserving ∗ and ⊚, exterior d₀ and the chosen Hom and index reading. Legal zero summands are allowed: a well-typed expression need not have both summands nonzero. In the signature-label branches the support of d₀ is `undetermined`. In the enumerated set, `all_nonzero_under_model` is empty and 32 of the 64 label branches are `well_typed`. **Making both summands contribute needs a reading outside this model**, for example:
- B05-Q, ⊚ acting on spinor labels;
- a frame or connection term in d₀ (B05-D′);
- ϖ's labels in a different system from the fields' (B05-L′).

Codex compared the 12 pre-registered hand verdicts with the generated label table and found 12 agreements. They were written by the code's author, so this checks the code against its stated rules, not the model against the source.

### 6. Corrected in review: the source does not fix the pairing

Rev 0 of the transcription claimed that (9.18)–(9.19) fix the metric pairing. The blind comparison showed this was wrong, and Claude re-derived the correction. **Under ordinary wedge products and exterior covariant derivatives** (B05-P, A, V, M remain open):
- in the first component, ⊚ sends spinor 2-forms to 13-forms;
- in the third component, it sends 2-forms to 1-forms.

Those are different degree maps for the two occurrences, or an inconsistency in the source (B05-Y). No reading of the printed outer star is fixed.

### 7. Nguyen–Polya §3.2 mapped to the April draft (`np_objection.md`, Codex)

- The NP group U(128) is not the April H = U(64,64).
- NP's axial transformation is printed as exp(γ̄θ), without an i, so mapping it to C or to iC is a transfer assumption.
- No central coupling or fermion charge assignment is located in the April draft.
- No prescription is found that shrinks H to Spin(7,7) while keeping the action.

## What remains open (`spec.md` §4)

The following are unspecified in the draft:
- the Hermitian form;
- the pairing;
- the meaning of ± and of the bar;
- how ϖ and ⊚ act on spinor forms;
- the lower-right "non-trivial map" version;
- **every fermion transformation law**;
- **the bosonic tilted-gauge (ℋ_τ) law, which is printed inconsistently** (Codex audit Finding 1, re-derived by Claude). (6.4)/(6.13) put a minus sign on h⁻¹dh, while (6.2), (6.20) and (7.4) need a plus. Taken literally, A_ω and the augmented torsion are not covariant. Footnote 7 on p. 36 warns of conflicting conventions. It is branched as (6.13-lit) and (6.13-rec) (`spec.md` §1.2).

The reality condition is branched as R0, R1, Rc, R2 and R2′:
- R2, Majorana at (7,7) via B03's J (J² = +1), breaks the central U(1).
- R2′ at (9,5) needs a doubled space, because J² = −1 there.

## What the covariance test needs (`spec.md` §5)

- **(a) Executable now.** Only the toy controls, which test the criterion and not GU.
- **(b) Conditional formal tests.** A branch of the typed (9.16) can get a binary verdict only once it is fully specified:
  - every tested summand has a status other than `domain_mismatch` or `undetermined`;
  - the barred law S̄;
  - the coefficient and dressing variations. Constant parameters still move noncommuting coefficients, so a frozen-K test is a stabilizer test unless δK = 0 is stated;
  - a definite spinor-valued ⊚;
  - the target: bilinear, density or action;
  - under signature labels, how C acts on the coefficients.

  The next plan takes the **full** branch table with statuses, not a filtered survivor list.
- **(c) Returns "insufficient data" today:**
  - local covariance under ℋ_τ: fermion laws, the spinor action of ⊚, and the (6.13) sign conflict;
  - covariance under 𝒩;
  - any anomaly computation: a reality branch, the constrained fermion content and a quantum measure. The draft gives partial fermion content but no measure.

If the operator cannot be pinned without the action, the next step is B07's one-direction variation, as Grok suggested.

## Provenance

| Item | Commit | Author |
|---|---|---|
| Plan rev 1.2 (its Revision notes summarize the Codex, Grok and argon reviews) | `32d654d` | Claude |
| Transcription rev 0 / rev 1 (rev 1 records the blind second reading and comparison), `source_operator.py` | `68559dd` / `4ea2237` | Claude |
| `np_objection.md` | `59c62df` | Codex |
| `pairing.py`, `operator_check.py`, `run.py`, `tests/test_b05.py` | `eb77457` | Codex (written verbatim from the plan's code) |
| `result.json` (`source_commit` `eb77457`) | `5fb4f4a` | Codex |
| `spec.md`, this README | this commit | Claude |

Source PDF SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`. NP PDF SHA-256 `66c7caafce188744c7c7e6e085b40f849e0d1218a07ae675f8add187e82fc71f`.

Test results:
- 43 B05 tests;
- full suite 353 passed;
- seeded faults F1–F8, defined in the plan's Task 4 Step 6, all fail on an assertion, with byte-verified restores. Claude re-ran them in a clean checkout at `eb77457`.
- `result.json` regenerated in that clean checkout is identical to `5fb4f4a`, including `source_commit`.
- The 12 pre-registered hand verdicts in `transcription.md` agree with the committed `label_table`. The plan's Task 4 Step 8 compared them; anyone can re-check them from the two tracked files.

## Scope

The scope tags are `identity` (exact monomial algebra) and finite bookkeeping over an enumerated set of readings that depends on the model. This stage establishes no gauge-symmetry, anomaly, unitarity or reality verdict about GU, and none about Nguyen–Polya's conclusion.
