# Handoff notes: GU steelman (resume here)

Last updated: 2026-10-16 before compaction, by Claude (orchestrator, pane 0:2). **B01–B03 and B05-specification complete; B05 sign-conflict Lean check merged (a134286); B07 plan rev 0 drafted + smoke-tested, NOT yet committed** — see **Current work** below first. Read this file first after any context reset, then `.agent-handoff/auto-snapshot.md`, then `docs/methods.md`.

## Current work (resume here) — B07 one-direction variation, COMPLETE

**Plan:** `docs/superpowers/plans/2026-10-16-b07-variation.md` **rev 1.1 be2ae34, APPROVED by user 2026-10-16** ("approved, please continue"). History: rev 0 7b07e50 → Codex `revise` (7) + Grok `accept with fixes` (2) → rev 1 7d89105 → confirmation round (Grok accept; Codex 2 text items) → rev 1.1. Reviews: `.agent-handoff/b07-plan-review{,-grok}/` (+ `rev1/`).

**Task status:**
1. **Task 1 DONE** — `experiments/B07/transcription.md` rev 0 0912d4c (+ empty `__init__.py`).
2. **Task 2 DONE** — Codex blind reader + comparison `.agent-handoff/b07-transcription/{second-reader,transcription-comparison}.md`; **transcription rev 1 564ed4a** folds it.
3. **Task 3 DONE** — code b60bbfc (variation.py, run.py, tests/test_b07.py), result.json c7229e9 (runner 5293.6 s). 12 passed / suite 365; 8 faults RED. All 4D kernels 0 (C1, C2 N1/N2, joint; 8 modes × (3,1),(1,3)); 12 C1 witnesses as smoke. Orchestrator check: result.json minus seconds/source_commit **identical** to smoke clone. Worker report `.agent-handoff/b07-impl/result.md`.
4. **Task 4 DONE** — Codex `rederive.py` de8ab67, `rederivation.md` dccc0a4: 13/13 results agree with result.json (8 C1 kernels, 2 C2/N1, 3 14D witnesses). Claude re-checked the 10 kernel rows.
5. **Grok review DONE** (`.agent-handoff/b07-impl-review-grok/result.md`): Task 3 accepted, no defect; N0: rescue claim and H3's N0 C2 correct, ranking N1 > N2 ≫ N0, record-only adequate if no N0 number is stated. One finding: N0 is **not** the wedge extension of (12.26) (that is N2 = `gu.cliffform.bracket` C); verified and fixed in transcription rev 1.1 (4994078).
6. **Task 5 DONE** — README 4994078; Codex audit `.agent-handoff/b07-audit/readme-audit.md` (revise, 4 wording findings, no numeric disagreement) all fixed 01c328c (+ same fixes in transcription N0 note and B07-S row); Codex register cf90b4c (B07 entry + B05 Lean citation; says "P7 re-run pending"); **P7 DONE** (evidence `.agent-handoff/b07-p7/`): 365 passed, runner payload identical to c7229e9 (seconds 5322.6 vs 5293.6, source_commit b60bbfc both), 8 faults RED from plan block at be2ae34. README status + P7 lines and `methods.md` B07 retro committed with this HANDOFF. Register P7 flip 93a595a (Codex). **Next decision for user:** the plan's "After this plan" — `[ext]` constructive search (symmetrized ⊚ or different Φ), the second-order Lagrangian (9.11)–(9.15), metric/ε directions, or another register item.

**Key findings so far (transcription rev 1):**
- (9.4) is degree-inconsistent as printed in both line 1 (∗ over ⊚(…) + κT) and lines 2–4 (2-form integrand); V repairs line 1.
- [T,T] readings: **N0** (appendix (12.26) commutator extended to forms ungraded ⇒ [T,T] = 0; extension, not forced; C2 = −Tr(α∧⊚(T∧T)); cannot rescue (9.7) since C1 is bracket-free), **N1** (CS-consistent), **N2** (graded). p. 47's [F_A∧φ] does not select any (F has even degree). Codex's matrix check: N0/N1/N2 residuals 4, 0, −4 on one example.
- H8: under pinned convention ∗ is an anti-isometry on 1-forms (q odd), ∗† = −∗ between Ω¹ and Ω^{d−1}; correct gradient of I₂/2 is d\*⊚\*⊚F + κ₁d\*⊚\*(∗T) − κ₁∗⊚F − κ₁²T. (9.13) drops a ∗ in term 2 and has wrong signs in terms 3, 4; (9.12)'s Id should be ∗\* = −∗.
- H7 ledger: (9.18) lacks the barred-field (ν-, ζ-variation) equations; ⊚ζ̄ζ does not follow as printed (variation gives a transpose of ⊚; degree conflict); other components conditional on B05-Q.
- Register rows: V, L1, L2, P, S, T, Y, R, O, M, N0/N1/N2, K½/K1, G (ordinary products = mixed modes; unexecuted, outside approved scope — told user), D, F, S0, E, Q, Bd, X.

**Smoke expectations (for comparing Task 3 output):** C1, C2 (N1, N2) and joint kernels [] for all 8 modes at (3,1), (1,3); all six columns nonzero; 12 witnesses: CCC t=[0,1], a=[1,3], −2 at all four signatures; CAA and CAC t=[0,4], a=[1,6], value 2 at (3,1), (7,7), (9,5) and −2 at (1,3). Smoke runtime 7460 s.

**Lean sign check — DONE, merged a134286** (`lean/B05Sign/`): no single sign of (6.4)/(6.13) repairs §6. TODO (Codex, with B07 register task): cite it in the register B05 entry.

**tmux notes:** from Git Bash, `export MSYS_NO_PATHCONV=1` before `tmux send-keys ... "/new"`. Codex `/new` asks worktree (Enter = current) and resets model to GPT-6-Luna medium: `/model` → 2 → 3 for GPT-6-Astra high. Wait with a background `until grep -qE '^(DONE|BLOCKED|FAILED)' <dir>/status; do sleep 60; done`.

**Rules learned (B05 retro):** don't write under `experiments/B07/` while a worker's runner is pending; compose/differentiate printed formulas before citing; one degree chain per occurrence; Claude-authored derivations get an independent check.

**Scratch (session-local, may be gone):** `…/scratchpad/b07smoke/` (plan skeleton, rev scripts, smoke clone `repo/` with result.json), `…/scratchpad/b07pages/` (pp. 41–47 PNG).

## What this project is

A personal deep-dive (the user's choice "(b)": curiosity, not polish). We give Weinstein's *Geometric Unity* April 2021 draft the benefit of the doubt: find its gaps, try charitable repairs, and test them with exact-arithmetic programs. The deliverable is `docs/gaps/register.md`, with verdicts backed by tracked code.

## Key documents

| File | Owner | Role |
|---|---|---|
| `docs/superpowers/specs/2026-10-14-gu-steelman-design.md` | Claude | Spec rev 4.1, **approved by the user** |
| `docs/superpowers/plans/2026-10-15-p1-b01-and-p2-library.md` | Claude | Current plan, Tasks 1–9. **Approved; the user chose "keep the plan as written"** |
| `docs/methods.md` | Claude (Codex proposes) | Working methods P1–P9 and P2b, plus the retro log. The user asked us to iterate on these. |
| `docs/gaps/register.md` | Codex | Gap register A01–A06, B01–B12 |
| `experiments/<id>/` | mixed | transcription.md, README.md, (rederivation.md) by Claude; ansatz.md, code, result.json by Codex |

## Agents and rules

- **Codex** (GPT-6-Astra, Full Access) is in tmux **pane 0:3**. It is the *only* worker; **agy is not used**. Codex may spawn its own subagents.
- **Handoff:** write `.agent-handoff/<task>/task.md`, then send a one-line pointer: `tmux send-keys -t 0:3 -l "— Claude: new task. Read …/task.md …"`, then Enter, then a second Enter. Watch `status` with a background loop. `.agent-handoff/` is git-excluded.
- **Slash commands to Codex** need `MSYS_NO_PATHCONV=1` (Git Bash mangles `/compact`). Compact Codex when its context drops below about 60%. Done means idle at about 96–100% left; don't wait for exactly 100%.
- **Commits** go on master, always with a pathspec (`git commit -m … -- <paths>`), because we share one git index. Claude's trailer is `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; Codex's is `Co-Authored-By: Codex <noreply@openai.com>`.
- **Fable 5.1 budget:** hard cap $20, about $2 per call, reserved before dispatch. Announce each call to the user first. Ledger: `docs/fable-ledger.md`. **Spent: $0.** The user asked about a Fable review; Claude advised waiting for the B02 symbolic-covariance derivation or a stuck repair.
- The user pastes reviews from **argon** (another LLM). Treat them as input to verify, not as authority. Its claims have been about half right.
- The untracked `argon*.md` files in the repo root are the user's. Leave them alone.

## State (as of `4111a1b` and later)

**Done**
- **P0:** the register.
- **P1 / B01 closed.** Verdict: *match, holds, under R1*: the draft writes signatures as (#neg, #pos). See `experiments/B01/README.md`.
  - **F1:** the base mirror (1,3)↔(3,1) toggles between the (7,7) and (5,9)/(9,5) classes. The draft calls this choice cosmetic, but it is the same as the choice the draft calls "not yet forced".
  - **N1:** the trace magnitude is unspecified in the draft.
  - **Repair:** tie s_V (not the trace sign) to the base sign.
- **P2 library, Tasks 5–8:** `gu/{inertia,clifford,forms,curvature,adjoint}.py`, 164 tests passing (`uv run pytest -q`, about 30 s).
- **Task 9 steps 1–3:** B02 transcription rev 2 and ansatz amendment 1 (`f75bb66`), after Codex's review (verdict *revise*, 9 findings; evidence in `.agent-handoff/b02-transcription/`, reproduced by Claude). Key facts:
  - The appendix (pp. 65–66, (12.26)–(12.27)) defines [·,·] = commutator and {·,·} = i·anticommutator. (9.3) has 3 square brackets, so the **literal reading is CCC**.
  - Sampled (not yet identity): under CCC the "−½" scalar term of (9.3) vanishes on Levi-Civita curvature (κ = 0). CAA gives κ = ½ under N-a (κ = 1 under N-b). This is the likely headline B02 finding; the plan must make it identity-scope.
  - Real-form grade pattern of (3.27) is identical in (7,7) and (9,5). Invariant Φ spaces are real-2-dimensional each: Φ¹ = αF + βF′, Φ² = γB + δB′.
- Retro and new practices P10, P11 in `docs/methods.md`.

- **B02 plan written:** `docs/superpowers/plans/2026-10-15-b02-direct-check.md`, **awaiting the user's approval** (not yet dispatched).
  - Every code block was smoke-tested in scratch: 209 tests pass, the full 14D identity response check passes (~4 min per signature), and a rebuild from the plan text alone passes.
  - The smoke test found two issues, both fixed in the plan:
    - The checker had bypassed `shiab` (a −½ fault stayed green); it is now routed through `assemble`.
    - A wrong control assumed a Spin-image dressing is a no-op; replaced by a central dressing.
  - Sampled 5′ observation: odd dressings do **not** annihilate Weyl.
  - Predicted classification (README task): κ = γ/2 for CAA. So κ = ½ is exactly the unit normalization of B (N-a), while CCC gives κ = 0 for every Φ.

- **B02 plan revision 2** (`docs/superpowers/plans/2026-10-15-b02-direct-check.md`) folds in Codex's two-subagent review (verdict *revise*, R1–R8; `.agent-handoff/b02-plan-review/`) and argon's three test additions:
  - exactness via `exact()`;
  - the corrected Task 6 classification: κ undefined for m₀ = A; CAC κ = sδ/2 for β = sα; no N-b Einstein branch; scalar boundary at κ = 1/n; null Φ² directions B ± B′;
  - `git add` before every new-file commit;
  - (9,5) covariance samples;
  - runner guards plus a hand control;
  - a nonzero dressing sample.
  It was smoke-tested by rebuilding from the plan text: 222 tests pass, and the full run passes. **Awaiting the user's re-review and approval.**
- **Rev 2.1** (`70fa6ce`): Task 6 now names the trace norm, answering argon's clarification request. Both formulas were verified exactly in all three signatures:
  - N(X) = Σ_I η_I Tr(X_I X_I)/dim S (complex-bilinear, Ad-invariant, indefinite);
  - N(αF + βF′) = n(α² − β²) and N(γB + δB′) = C(n,2)(δ² − γ²).

  Argon reviewed rev 2: zero blockers.
- **B02 plan rev 3** folds in the independent Grok review (pi; `.agent-handoff/b02-plan-review-grok/`; verdict *revise*, findings G1–G5, all reproduced by Claude) and argon's docstring nit (the chart has C(n,4) extra coordinates).
  - **G1:** the other Hodge convention is exactly Φ² → −Φ², so the Einstein point moves to γ = −1.
  - **G2:** the README leads with the convention-stable result (literal CCC has no scalar term). κ = ½ requires N-a plus the pinned star; it is ¼ under σ = ½ΓΓ and 1 under N-b.
  - **Claude:** even q flips κ. All of this project's signatures have odd q.

  Rebuilt from the plan text: 222 tests pass, and the full run passes (about 10 min). **The user approved rev 3** and asked to be told if anything changes.
- **Tasks 1–4 verified by Claude (P7).** Codex commits: `30c87d0` (cliffform), `d63c7c5` (shiab), `14f4c65` (dressing), `d66cd8f` (response/run), `806b2e2` (result.json).
  - All 8 code files are identical to Claude's rebuild from the plan, with CRLF stripped.
  - 222 tests pass.
  - result.json: ranks 20/20 and 3185/3185; 912 / 57512 / 57512 nonzero out of 2640 / 267120 / 267120; `source_commit` d66cd8f.
  - Codex's 11 seeded faults were all red, including −½ → +½, which turned the verifier red.
  - Claude seeded −½ → −1 in a scratch copy, and the verifier went red at `(3,1,0,4,F,B,CAA)`.
  - No change from the plan.
- **Task 5 done:** `experiments/B02/proofs.md` (`93cf975`, revised `1c89d5b` after Grok's adversarial check, `.agent-handoff/b02-proofs-check-grok/`). Every argument holds. Wording fixes:
  - narrow scope for the CCC headline (even n, pinned ξ with η_cη_d, global scale, either standard star; *not* any ξ index convention or pair-dependent star);
  - κ = 0 also needs the first-term multiple;
  - Spin₀ is generated by exponentials;
  - even-q is sampled only.

  Claude also ran the full n = 4 identity check at (1,3) in scratch: it passes; it is not in `result.json`.
- **Task 6 done, except for the Lean unification.**
  - README `a70c6d4`, revised `88c99b2`, `723593b` and `fc7d5e6`.
  - Codex re-derived the classification independently and confirmed it (`.agent-handoff/b02-verdict/result.md`, 70 exact checks).
  - Codex's README audit R1–R4 is applied:
    - the headline is "stable under the conventions varied, with ξ pinned";
    - T = 0 is unidentifiable, not r_T = 0;
    - the Bianchi kill covers both grade 3 and grade n−3;
    - the norm filters admissibility rather than moving κ.
  - New fact: the σ unit fails 5a at n = 4.
  - Register B02 entry: `109eab5` (Codex).
  - Lean FINDINGs folded in: `482b73d` (pq is even, not the total degree) and `88c99b2` (κ needs n ≥ 3).
  - Retro: `fc7d5e6`.
- **Lean side task (the user's request, 2026-10-15).**
  - The user started a second GPT-6-Astra in **pane 0:5** to formalize all of `proofs.md` in Lean 4 + Mathlib.
  - It works in the worktree `C:\work\src\GU-b02-lean`, branch `b02-lean`, created from 36add8f. Brief and status are in `.agent-handoff/b02-lean/`. `progress.md` gets `FINDING:` lines.
  - Extra dependencies (elan, Mathlib) are approved by the user.
  - **On Lean DONE, the user asked for a Grok review (pi, 0:4).** The brief is ready at `.agent-handoff/b02-lean-review-grok/task.md`. It covers definition fidelity against the Python, statement fidelity, the hypotheses and axioms audit, and reproducing the build and bridge. A background waiter auto-sends the pointer to pi on `DONE`. If the waiter is gone after a reset, send it by hand.
  - **Unify at the end of Task 6:** review its `result.md`, covering the claim-to-theorem fidelity table, `#print axioms` and the Python bridge cross-check. Fold any FINDING into proofs.md and the README, merge `b02-lean`, then update the register's "no Lean proof claimed" line.
- **B03 (P3) started 2026-10-15 (the user's request, while the Lean worker runs).**
  - Claude: transcription rev 0 at `experiments/B03/transcription.md` (`8c83fc5`). It covers pp. 50–53 and 61–62, with 7 `[GU-recon]` branches and properties B1–B6. Key open items:
    - the chirality dictionary (11.6) vs (12.20);
    - the location of the "imposter" generation: ℱ ⊂ 832 in (12.22), vs the p. 53 names on rows of a 144;
    - the U(1) embedding (n = 6Y fits all 25 rows of the p. 53 table).
  - Codex: `.agent-handoff/b03-oracle/`. It installs LiE in WSL (or a fallback), runs the positive controls (Spin(10) 16 → SU(5)) and the D7 ⊃ D2 × D5 tables for S±, RS± and V⊗S±, gives an independent second reading of the pages, and proposes a `reps.py` interface. It must not commit.
  - **Codex oracle: DONE** (`.agent-handoff/b03-oracle/result.md`).
    - LiE 2.2.2 is installed in WSL Ubuntu-24.04 (apt).
    - The Spin(10) 16 → 10₁ + 5̄₋₃ + 1₅ control passes.
    - The full D7 → D2 × D5 tables cover S±, RS± and V⊗S±. The gamma trace has the **opposite** chirality. RS keeps its own spinor-shaped 64: 832 = 576 + 192 + 64.
    - ν ⊕ ζ inventory: each (2,1)/(1,2) × 16/16̄ block appears 3 times, and each RS-type block once.
    - Spinors are Majorana–Weyl in (7,7) and quaternionic in (9,5).
  - **Claude verified (P7).**
    - Reran LiE: byte-identical output.
    - Independent route by explicit weight multisets: `.agent-handoff/b03-transcription/weights_check.py`, all True.
  - **Transcription rev 1** (`58e275d`) applies Codex's 5 corrections, including a declared chirality dictionary (144₊ = H̄, mixed relative to 16₊ = 16).
  - **Still open for the ansatz:**
    - where the "imposter" generation sits: ℱ ⊂ 832 per (12.22) and pp. 65 and 68, vs the p. 53 names on rows of a 144;
    - the SM embedding for the §11.3 tables;
    - J for RS, to be checked with explicit matrices.
  - **Ansatz.**
    - rev 0: `a0bc8e0`.
    - Codex two-subagent review: *revise*, R1–R5, in `.agent-handoff/b03-ansatz-review/`.
    - rev 1 applies it:
      - pinned real-axis splits plus a Cartan adapter (test 0); library C vs S± flips with signature;
      - tr Q = d·tr P targets;
      - E pinned by explicit maps, with E′ as a conjugacy control (identical on complete characters);
      - p. 53 aggregated to 23 terms;
      - test 7 is data only.
    - Outcomes the review already computed are declared as known.
  - **Claude's scratch `reps.py`** (`scratchpad/b03/reps.py`, exact Freudenthal for A_n/D_n) reproduces every LiE output in 0.6 s.
  - **Ansatz rev 1.1** (`fcc408f`): JW-pair axis lists and the Euclidean-frame adapter. **`source_tables.py`** (Claude's draft data): `65b9d2c`.
  - **Plan rev 0:** `docs/superpowers/plans/2026-10-15-b03-branching.md` (`06a5f3b`, 1627 lines).
    - Smoke test, in scratch `b03smoke/`:
      - 286 tests pass;
      - all 11 seeded faults are red (`faults.py`);
      - a fresh rebuild from the plan text is green;
      - the LiE fixture now also includes the A1 controls and the SM restriction under E.
    - Smoke outcomes (not evidence):
      - every draft identity holds under the dictionary;
      - p. 52 = 16 / 16̄, and p. 53 = H̄ = 144₊ exactly;
      - J² = +1 (7,7) / −1 (9,5);
      - χ = 0.
    - **Codex two-subagent plan review dispatched:** `.agent-handoff/b03-plan-review/`. Claude expects one finding: `rs_character` uses the Q″ formula, not the `projector_Q` matrix.
  - **Plan review:** Codex said *revise*, with findings 1–4 (`.agent-handoff/b03-plan-review/`). **Plan rev 1 applies all four:**
    1. The character gate reads the production Q, through a shared `verify_split`; wrong-projector and zero-Q controls added.
    2. A P4 exactness layer in reps.
    3. Expected values come from LiE compared directly with the draft rows; the ansatz ledger is corrected (rev 1.2, `a70337e`).
    4. Imposter records, J partners and SU(5) × U(1)_X labels.
  - Smoke test: 297 pass; 13/13 seeded faults red; a fresh rebuild from the plan text plus a fresh LiE run matches the fixture hash `576888f2…`.
  - **Plan rev 1.1** (`7e4ea9c`, 2008 lines) folds in **argon's review** (no blockers):
    - the parser rejects an unfinished polynomial;
    - `faults.py` prints the failing test names (F12 includes `test_verify_split_gate`);
    - a Layer-1 scope note on `rs_character`: c-conjugation is a GL(14, ℂ) similarity, real-form data are only J and `chirality_vs_parity`, and only the Cartan-pair blocks are read, so call it through `verify_split`.
  - **Task 5 README must:**
    - state that J² = +1 (7,7) admits Majorana–Weyl Jψ = ψ, so (R;16̄) is the conjugate of (L;16), while J² = −1 (9,5) has no nonzero Jψ = ψ; the J pairing never removes a block by itself;
    - include the Layer-1 scope note;
    - give no location verdict on "imposter";
    - say that generations and decoupling need dynamics.
  - **Plan rev 1.2 + ansatz rev 1.3** (`a5a3b99`, 2023 lines) fold in **Grok's review** (`.agent-handoff/b03-plan-review-grok/`; *accept with fixes*, 3 findings, all reproduced):
    - `projector_controls` builds a traceless map T and a gamma-inserted map W from the gammas; `verify_split` and the test assert Q T = d T, γ·T = 0, Q W = 0 (the old assert was implied by Q² = dQ);
    - F10 keys by (SU3, SU2, n), so it fails at the Imposter quark sum `2 == 3` (checked);
    - E′ is the charge formula, not the y₄, y₅ flip (ansatz wording).
    - Fresh rebuild (`scratchpad/b03fresh3`): 297 pass, 13/13 faults RED.
  - **Tasks 1–4 DONE** (user approved dispatch; Codex, `.agent-handoff/b03-impl/result.md`). Commits `5b85fd9`, `ee6c59f`, `71409f3`, `895fc08` (code, = `source_commit`), `2cf2c71` (result.json).
    - **Claude P7:** all 9 committed code files equal the plan's blocks (newline-normalized); fixture SHA `576888f2…`; `result.json` regenerated from a clone at `895fc08` is identical; full suite at `2cf2c71` = 297 passed.
    - Results: p51 10/10 blocks hold, (12.20) both hold, full Dirac holds, p52 = 16 / 16̄, p53 = H̄ (23 terms); fibre 1920; J² = +1 (7,7), −1 (9,5); 8 imposter records, 6 J-partner pairs.
    - **Open (Codex P6, reproduced by Claude):** two P4 holes in the frozen `gu/reps.py`, neither touching the pinned run: `sm_weight_flipped` sums the raw argument (NumPy int64 overflow → spurious ValueError); `Simple.to_dynkin_root`/`ip` skip `weight()` coercion (overflow; float accepted). Fix = coerce via `weight(...)` at each public entry, add controls. User approved bundling it with Codex's Task 5.
  - **Task 5 DONE.** Codex: `835d7c8` (reps.py P4 fix: every public numeric entry coerced; 310 tests; 13/13 faults RED; clean-clone result.json equal except source_commit), `9bfaf04` (`experiments/B03/rederivation.md`: fresh LiE + own Pauli gammas, 44/44 entries agree), `dda3bd5` (register: B03 entry, partial-Lean wording). Claude: README `d91fa21`/`de24f31`/`df64ed9` (audit's 3 wording fixes applied), retro `01c58ff`. Claude P7 log: `.agent-handoff/b03-task5/claude-p7.log` (runner at 835d7c8 equal except source_commit; suite 310 at dda3bd5).
  - **B03 verdict (README):** all branching identities hold (full-module forms convention-free; chiral forms under the declared dictionary, 144+ = H̄); p.52 = 16/16̄, p.53 = H̄ under E; J² = +1 (7,7) / −1 (9,5); both imposter candidates (ℱ⊗16, 𝒵⊗H̄) contain one generation pattern per chirality, no location verdict; fibre 1920, χ = 0; generations/decoupling need dynamics.
  - **B03 Lean (user-requested), DONE, Grok ACCEPTED (no findings):** GPT-6-Astra, branch `b03-lean` (4fc432a, c8980cb, 8e62882 on 736dd77) in worktree `C:\work\src\GU-b02-lean`; report `.agent-handoff/b03-lean/result.md`. 81 public B03 theorems; all four splits; all kernel `decide +kernel` (no `native_decide`, no sorry, standard axioms only); J commutation proved for every bivector (stronger than brief); no FINDING. Claude verified: `lake build` OK, Audit 81/81 standard axioms, `b03_check.py` PASS (127 matrices, 14644 columns, 16 fields). Grok review: `.agent-handoff/b03-lean-review-grok/task.md` (pi 0:4). Grok verdict `accept`, no findings (`.agent-handoff/b03-lean-review-grok/result.md`; Claude spot-checked order95b = order77 against `SPLITS`). MERGED to master as c22e8ac (user OK).
  - **Next item = B05, transcription/specification stage (user-approved direction):** Codex and Grok second opinions (`.agent-handoff/next-item-{codex,grok}/result.md`) both said: pin the fermionic operator (9.16) and every field's transformation law before any covariance/rejection test; B03's J is not a reality condition (J²=−1 at (9,5)). Plan rev 0 `docs/superpowers/plans/2026-10-15-b05-transcription.md` (443a16a): Task 1 transcription + typed (9.16) (Claude), Task 2 blind second reader (Codex), Task 3 NP §3.2 object map (Codex), Task 4 `pairing.py` + `operator_check.py` + runner (Codex), Task 5 `spec.md` transformation laws/reality branches/invariance criterion (Claude), Task 6 audit + register (Codex). Smoke: fresh rebuild from plan text 26/26, full suite 336, faults F1–F6 RED. Smoke observation (not a finding): no label branch of (9.16) fully consistent; only (metric, exterior d₀, ⊚ m=1 n=0 r=1) degree-consistent. Rev 0 reviews: both *revise* (`.agent-handoff/b05-plan-review/result.md` 7 findings, `.agent-handoff/b05-plan-review-grok/result.md` 5). Key: rev 0's R1 criterion had a sign error (δψ̄ = ψ̄S♯, not −ψ̄S♯). Rev 1 (89fd065) folds all in: 43 B05 tests, full 353, faults F1–F8 RED, survey well_typed=32/64 all_nonzero=0 degree_ok=4/90 (model-relative). Rev 1 confirmation: Grok accept; Codex accept with fixes A (CRLF fault anchors), B (sign ±1 validation), C (4 of 360 degree branches), Task 6 order — all applied in rev 1.1 (c43aa3e); fresh rebuild 43/43, faults 8 RED on LF and CRLF. Argon audit (pasted by user) verified by Claude and folded into rev 1.2 (32d654d): bar-label convention (ζ̄₋ := (ζ₊)†A ≡ dual_field combinatorics), (ζ̄₋,ζ₋) cell-collision as hand derivation 6 (checked: no enumerated chirality reading makes d₀ζ₋ and ϖ₊₋ζ₋ both nonzero with exterior d₀), R1 has δA=0 (congruence-transformed A = contragredient branch), README diagnostic framing. User approved rev 1.2. Task 1 committed 68559dd (`experiments/B05/transcription.md` rev 0, `source_operator.py`). Source cross-check found: (9.18)–(9.19) type ⊚ on spinor 2-forms → 13-forms (metric-pairing sense), (8.5)/(8.6) consistent with C∈𝔲, iC∉𝔲; (6.22) A_ω=∇⁰+ϖ. Tasks 2 (fresh blind reader) + 3 (NP §3.2 map) dispatched to Codex 0:3 (`.agent-handoff/b05-transcription/task.md`). Then: Claude transcription rev 1 from the comparison, then Task 4 (Codex code), Task 5 (Claude spec/README), Task 6.
  - (Superseded: user chose B05 specification, then B07 + Lean; see **Current work**.)
  - **Smoke-copy caveat:** files in `b03smoke/` are CRLF. Python edits there must keep newlines (read and write bytes); `faults.py` matches either newline style.
- **Lean (B02): merged** (`e48a0e3`, from `b02-lean`).
  - Grok's review: *accept*, with two minor findings (`otherStar` is not in the bridge; `native_decide` theorems are outside the kernel).
  - The B02 README has a "Formal check" section (`f8cf6b5`). The headline holds for all n with pair symmetry only.
  - **Pending:**
    - Codex updates the register's "No Lean proof … claimed" line, in its next register task (the B03 Task 5 brief).
    - **Keep the worktree** `C:\work\src\GU-b02-lean` (6.8 GB of Mathlib build cache). The user wants Lean validation in later steps too. To reuse it, check out a fresh branch from current master there (`lean/` is merged) before briefing a Lean worker.
- **Agents:** Codex is in pane 0:3. A second GPT-6-Astra (the Lean worker) is in pane 0:5. pi is in pane 0:4, running Grok, a different model family, which makes it useful as a third independent reviewer and for web lookups. agy is retired. Scratchpad: `C:/Users/yenchi/AppData/Local/Temp/claude/C--work-src-GU/3062a13c-f3b7-47e3-935c-cd657b34eb26/scratchpad/`.

**Next**
1. ~~Resolve Codex's review~~ (done, `f75bb66`). ~~Retro~~ (done). ~~Write the B02 plan~~ (done).
2. ~~Approval~~ (rev 3 approved). Codex: Tasks 1–4 (code and result.json committed; final suite and result.md in flight). ~~Task 5~~ (done). Then verify, report to the user, and do Task 6.
3. (Superseded; kept for the record.) Write the follow-up plan `docs/superpowers/plans/<date>-b02-direct-check.md` (writing-plans skill), from the reviewed transcription. Include the symbolic covariance derivation (Claude), the branch enumeration (brackets 2³ × Φ choices × signatures), tests 1–5 and 5′, and the H0 line item. Smoke-test the plan's code, and list the ambient impostors (P2b).
4. Get the user's approval of that plan, then dispatch it to Codex.
5. ~~P3 (B03)~~ done; ~~B05 specification~~ done. **Now: B07** — see **Current work** at the top.

## Facts that are easy to get wrong

- The GU adjoint is u(64,64), dim 16384, not so(14). A = a phase times the product of the timelike gammas, with A Hermitian and A² = I. AΓ_aA⁻¹ = (−1)^q Γ_a†.
- γ_sγ_t (one spacelike, one timelike gamma) is **not** in U(A): h†Ah = −A.
- Weyl annihilation is automatic for undressed equivariant maps (D7 highest weight). The B02 exit gate is a **nonzero** Ricci and scalar response.
- (9.3) is explicitly not the author's preferred Shiab operator: that one is lost (footnote 10). A failure refutes only the displayed candidate.
- The draft PDF has SHA-256 `3f28d742…186d4`. Render pages with `uv run --no-project --with pymupdf python -I` plus `sys.stdout.reconfigure(encoding='utf-8')`; `Read` cannot open PDFs here because pdftoppm is missing.
