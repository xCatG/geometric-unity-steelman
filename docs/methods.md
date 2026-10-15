# Working methods: proof-carrying programs

A living document. Claude and Codex append to the **Retro log** after every task, and fold recurring lessons into **Practices**. The spec (`docs/superpowers/specs/2026-10-14-gu-steelman-design.md`) defines *what* counts as evidence. This file is about *how* we write programs that deserve that status.

## Practices (v1, 2026-10-15)

### P1. Every test states the claim it carries

A test's docstring or name says which claim it supports and at what scope: `identity`, `sampled` or `counterexample`. Two kinds of test must be kept apart:
- **Controls:** known textbook facts that validate the tool.
- **Findings:** claims about GU.

A test that has no scope is a control.

### P2. Show that tests can fail (seeded faults)

A passing test is evidence only if a plausible bug would have made it fail. For each new module, the implementer seeds 2–3 realistic faults by hand: a flipped sign, a wrong contraction slot, a dropped phase or an off-by-one index. They confirm that at least one test fails for each fault, then revert. The seeded faults and the tests that caught them are recorded in the task's `result.md`. A fault that no test catches means a test is missing; add it.

Check *why* each seeded fault fails. A fault that only raises `NameError` or `ImportError` tests nothing. Read the failure message, and keep only faults that fail an assertion.

**Non-vacuity.** Assert that every sample input is nonzero, and that every batch of outputs contains at least one nonzero output. A verifier must call the production entry point, never re-implement it. Seed a fault in the production code and confirm that the *verifier* (not just the unit tests) turns red. (Promoted 2026-10-15 after a zero curvature sample, and a response checker that bypassed `shiab` and stayed green with the −½ flipped.)

### P2b. Representation adapters get a positive example and an ambient impostor

Every adapter between representations (e.g. the ℂ → ℝ 2×2-block embedding) gets two tests:
- one independently specified positive example;
- one input that satisfies the ambient representation's equations but lies outside the intended domain, and must be rejected.

Example: a real orthogonal matrix that is not complex-linear passes the block-form unitarity equation, but it is not in U(A). (Proposed by Codex, who caught exactly this hole in the plan's `adjoint.py`.)

### P3. Expected values come from outside the code under test

Expected values come from one of: textbook formulas, hand derivations written in the test or in `rederivation.md`, an oracle, or a different algorithm. Expected values are never pasted from the code's own output. When an expected value fails, stop and report it; do not edit the expectation.

### P4. Exact or explicit

Use no floats in any claim path. Any API that takes numbers rejects floats loudly.

Route every numeric input through **one** coercion helper (e.g. `gu.cliffform.exact`). It converts numpy fixed-width integers to Python `int` and raises on floats. Never cast with a bare `int(...)` on a claim path, because it truncates rationals and floats silently. Before handoff, grep new code for `int(`, `float(` and arithmetic on numpy scalars. Add a large-integer control (e.g. 2⁶² · 4) and a rational-input control for each adapter. (Promoted 2026-10-15: the bare-`int()` bug class appeared twice, in `adjoint.embed` and then in B02 `xi`/`embed_tensor`.)

### P5. Small, then big

Run every check on a small signature first, where it can be confirmed by hand (e.g. (1,1), (3,1), d = 4), and then on (7,7) and (9,5). The small case goes in the test suite permanently.

### P6. One writer per file, and disagreements go in writing

Codex owns code, tests and the register. Claude owns transcriptions, reconciliations, specs and plans. A worker who disagrees with the plan's code or math writes the disagreement in `result.md`, with a counterexample if possible, and does not silently "fix" the plan.

### P7. Handoff hygiene

- Briefs live at `.agent-handoff/<task>/task.md`.
- The worker writes `status`: `ACK`, `WORKING: <step>`, `BLOCKED: <why>`, `DONE` or `FAILED`.
- The worker writes `result.md` with the commands run and their output, the seeded-fault table, any deviations from the plan, and retro notes.
- The orchestrator reruns the decisive checks itself before accepting the work.

### P9. Reconciliations separate formula, normalization and consequence

A reconciliation of a source formula with our code states three things separately:
1. the literal source formula;
2. the normalization we chose where the source is silent;
3. the consequence that holds independently of that choice (e.g. signature only).

A match of invariants such as inertia does not show that the source chose our representative.

### P10. Gates name their target value, not just its shape

A pass criterion that fits free parameters ("c ≠ 0 and some κ") admits any map of the right shape. Pre-register the specific target value (κ = ½), the embedding the output is compared in, and every summation and normalization convention it depends on. A gate that passes a known-wrong candidate (e.g. the pure −Ric contraction for an Einstein claim) is an ambient impostor at the level of the experiment (compare P2b). Conversely, do not fix a target copy that silently rejects an equally valid embedding.

### P11. Follow the source's own cross-references before calling something unspecified

Before marking notation as an open branch, read the source's appendix, glossary and end matter for a definition. Record where you looked.

### P8. Commits mirror the evidence

Commit the pre-registration first and the results second. One task produces one or more commits, and a commit never mixes authors' files.

- Both agents share one working tree and one git index, so always commit with an explicit pathspec (`git commit -m … -- <paths>` or `git commit --only`). A bare `git commit` can sweep up the other agent's staged files.
- When a generated result records `source_commit`, commit the producing code and inputs first and check they have no uncommitted changes. Then run, and commit the result separately. A revision that lacks the producing code is not a valid source.

## Review checklist (orchestrator, per task)

- [ ] Ran `uv run pytest -q` myself and got the same results as the worker reported.
- [ ] Read the seeded-fault table. Reproduced one fault myself.
- [ ] Every new expected value has a source outside the code under test (P3).
- [ ] No float on any claim path; no `.agent-handoff/` link in tracked files.
- [ ] Deviations from the plan are justified, and the plan is updated if a deviation sticks.
- [ ] Retro notes merged into the log below.

## Retro log

Each entry: date, task, who, what worked, what didn't, what to change. Promote a lesson to **Practices** once it has come up twice.

- **2026-10-15 · plan writing · Claude.** Smoke-testing the plan's code blocks in a scratch copy before handoff (101 → 102 tests) caught nothing structural. An outside review found a real false rejection (unexpanded ℚ(i) expressions in `inertia`), which none of my tests exercised. **Change:** add P2 (seeded faults) so that false negatives and false positives in a tool get looked for deliberately, not by luck.
- **2026-10-15 · Tasks 1–2 · Codex (worker) and Claude (review).**
  - *Worked:* 4 seeded faults, all caught; Claude reproduced an extra fault (transpose instead of conjugate in the Schur step), caught by 3 complex-path tests. Narrow file ownership let Task 3 run in parallel. Codex added float guards at the public API (P4) and split the code and results commits, so `source_commit` is accurate.
  - *Didn't:* the plan's basis shorthand `{E_ij+E_ji}` was ambiguous on the diagonal. The generic skill's worktree/wrapper assumptions clashed with the shared-master setup.
  - *Changes:* P8 now requires pathspec commits and code-before-result for `source_commit` (both promoted immediately, because each fixes a provenance hazard rather than a style choice). Plans must define bases explicitly.
- **2026-10-15 · Tasks 3–4 · Claude.** Transcribing from rendered page images (pymupdf at 110 dpi) worked well; text extraction alone would have lost the fractions in (3.9). The reconciliation produced a finding the plan didn't anticipate (B01 F1, the base mirror). *Change:* reconciliation READMEs end with a "What this does not establish" section.
- **2026-10-15 · Task 4 · Codex (worker) and Claude (review).**
  - *Worked:* the adversarial re-derivation earned its keep. It confirmed all the arithmetic, and it found two errors in Claude's README that a passing signature table could not detect: an exact-form overclaim (λ = 1/2 "no rescaling") and a false repair (tie the trace sign to the base, which gives (4,10), not (7,7)). Claude reproduced the counterexample exactly. Codex's second subagent read the PDF independently.
  - *Didn't:* Claude's brief asked for `git grep agent-handoff` over all of `docs/`, which legitimately matches the methods and spec text. Codex recorded the exception rather than editing protected files, which was the right call.
  - *Changes:* new P9 (proposed by Codex). Acceptance checks in briefs must be scoped to exactly the files they police.
- **2026-10-15 · Tasks 5–8 · Codex (worker) and Claude (review).**
  - *Worked:* 10 seeded faults, all caught, each restoration verified by SHA-256. Every expected value has a one-line outside source (P3). Codex caught two plan bugs no test had exercised: (1) `is_in_algebra`/`is_in_group` admitted real-orthogonal, non-complex-linear matrices; (2) `int(x)` casts in `embed` silently truncated rationals and could overflow int64 in `curvature`.
  - *Didn't:* Claude's first reproduced fault died with a `NameError`, so it tested nothing; noticed only by reading the failure. A system-Python vs uv runtime clash cost Codex a rerun.
  - *Changes:* P2 now requires reading why a fault fails; new P2b for adapters. **Lesson for plan-writing:** code smoke-tested by its own author missed both bugs. Plans should list the ambient-impostor input for every adapter.
- **2026-10-15 · Task 9 (B02 transcription review) · Codex (reviewer) and Claude (author).**
  - *Worked:* the adversarial review again earned its keep: verdict *revise*, 9 findings, 3 high. Codex used an independent second reader on the PDF, all-entry commutant ranks rather than a diagonal ansatz, and a representation-theoretic argument for completeness. It separated hand-derived identities from sampled executions. Claude reproduced the runs (exit 0, identical output) and re-checked the two decisive claims with independent code and the page image.
  - *Didn't:* (1) Claude wrote a parity claim (q = 5 vs q = 7 differ) without checking that both are odd: a one-line arithmetic slip that a membership check would have caught. (2) Claude missed the appendix that defines the brackets. (3) Claude's exit gate (fit c, κ) admitted the literal −Ric contraction as "Einstein-like", and fixed a grade-1 target that rejected the equally valid grade-13 embedding. (4) The review's sampled computations now precede the amended pre-registration; the amendment says so explicitly.
  - *Changes:* new P10 (gates name their target value and embedding) and P11 (follow cross-references before declaring a branch), both promoted immediately because each guards evidence validity. **For transcriptions:** any claim checkable by an existing library predicate gets checked before it is written down.
- **2026-10-15 · B02 plan (rev 1 → rev 2) · Claude (author), Codex (two-subagent review), argon (review).**
  - *Worked:* smoke-testing the plan in scratch caught a verifier that bypassed `shiab` and a wrong "Spin dressing is a no-op" control before anyone else saw them. Codex's practical subagent replayed the plan literally (all Expected lines, 9 seeded faults, a full 541 s run). Its adversarial subagent confirmed the spanning, affine-extension and equivariance arguments and found real classification errors with exact counterexamples. Argon's three test additions were cheap and are now in. Inlining the tested scratch files into the plan by script, then rebuilding from the plan text, guarantees that the plan code equals the tested code.
  - *Didn't:*
    - Claude repeated the bare-`int()` cast bug class (R1/R2).
    - Claude mis-stated κ as 0 where it is undefined, used the wrong CAC locus, and gave N-b a domain where it is unavailable (R3–R5).
    - New-file commits lacked `git add` (R6; Claude hit this itself on the plan commit).
    - One dressing sample was identically zero.
    - Claude presented the plan for approval before any outside review. The user had to ask.
  - *Changes:* P4 now requires one coercion helper and large-integer/rational controls. P2 now has a non-vacuity rule. Memory: an adversarial + practical Codex review always precedes asking the user for plan approval. Plans include `git add` before every new-file pathspec commit.
