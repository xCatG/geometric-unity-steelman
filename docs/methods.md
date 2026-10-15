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

### P3. Expected values come from outside the code under test

Expected values come from one of: textbook formulas, hand derivations written in the test or in `rederivation.md`, an oracle, or a different algorithm. Expected values are never pasted from the code's own output. When an expected value fails, stop and report it; do not edit the expectation.

### P4. Exact or explicit

Use no floats in any claim path. Any API that takes numbers rejects floats loudly.

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
