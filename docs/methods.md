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
- **2026-10-15 · B02 plan (rev 2.1 → rev 3) · Grok via pi (independent review), Claude (author).**
  - *Worked:* a reviewer from a third model family found five issues that Codex and argon had both missed. The decisive one: an unstated Hodge convention moves the Einstein point. Grok wrote its findings before reading Codex's review, then marked each one NEW or DUPLICATE, which kept the comparison honest. Claude reproduced every finding with its own code. Doing so sharpened finding 1: the other star is *exactly* the pinned operator with Φ² → −Φ², a reparametrization rather than a new branch. It also turned up a related fact: the q-parity of the signature flips κ.
  - *Didn't:* (1) The transcription had flagged the star as "record a branch if it matters", but the plan never tested whether it matters. (2) The plan told the README author to confirm κ "against `result.json`", which contains no κ; that check could never be carried out. (3) The runner's only hand control skipped the term under test.
  - *Changes:* for every convention a transcription leaves open, the plan either tests it or proves it irrelevant (an extension of P9/P11). Every "confirm against X" instruction names a field that X actually contains. Hand controls must exercise each term of the formula under test.
- **2026-10-15 · B02 execution (Tasks 1–6) · Codex (worker, re-derivation), Claude (proofs, README), GPT-6-Astra (Lean side task).**
  - *Worked:*
    - The plan-equals-tested-code discipline paid off. Codex's 8 code files were byte-identical (modulo CRLF) to Claude's rebuild, there was no deviation, and verification took minutes.
    - Codex wrote its classification **before** reading the README table. That separated two cases the README had blurred: "measured r_T = 0" versus "zero reference embedding", and "the norm moves κ" versus "the norm filters admissibility". Its cheap exact controls also found that the σ unit fails 5a at n = 4 (γ = ½ = 2/n), which the plan had stated only for n = 14.
    - Formalizing in Lean found two real wording errors within its first milestone, before any proofs were written. proofs.md said "even total degree" where it should say "even product of degrees", and it gave κ for "all even n" when n ≥ 3 is needed for identifiability.
  - *Didn't:*
    - Claude's README overstated the headline as "independent of every convention". It is stable under the conventions varied, with ξ pinned; the signed equation depends on the star.
    - Two Grok passes and Codex's review did not catch the "total degree" slip, because each reader checked the conclusion, not the stated reason.
    - Claude's extra seeded-fault run was cited without saved output until the audit asked for it.
  - *Changes:*
    - Headline claims list the conventions they were tested under, never "every convention".
    - When a rationale sentence carries a claim, review checks it like a claim.
    - Every orchestrator-run check saves its command and output to a file before it is cited.
    - Formalization is a cheap first-pass auditor of stated hypotheses. Starting it early, in parallel, works.
- **2026-10-15 · B03 (ansatz → plan rev 1.2 → Tasks 1–5) · Claude (plan, README), Codex (reviews, execution, re-derivation, audit), Grok via pi and argon (plan reviews).**
  - *Worked:*
    - An external oracle (LiE, fixture hashed and tracked) gave every expected value without trusting our code (P3). Tests compared the draft rows to LiE directly, without importing the B03 code.
    - Three review families each found something the others had missed:
      - Codex: the runner accepted Q = 0 while still reporting a matching RS character.
      - argon: J² = +1 and J² = −1 license different statements, which became a README requirement.
      - Grok: a fixed-vector gate that Q² = dQ already implied; a seeded fault keyed so that it missed the row it named; a sentence calling two different maps the same.
    - Plan code equalled tested code again: Codex's 9 files were byte-identical modulo CRLF.
    - Codex's final review then found P4 holes *in the approved code*, and reported them under P6 instead of silently fixing them. The user approved a separate fix, and a clean-clone rerun showed the fix changes no result.
    - Codex's README audit caught three wording errors with no numerical disagreement.
  - *Didn't:*
    - Claude ran the plan's extraction script from the repo root, and it wrote 11 untracked files there. They were removed by exact path.
    - Claude cited its first clean-clone rerun (`895fc08`) without saving the output. This repeats the B02 "save before citing" slip; the audit flagged it, and the rerun at `835d7c8` is now logged.
    - Claude's README wording errors:
      - it wrote "Q fixes T" where QT = dT;
      - it attributed the n = X impostor to F4, which is n → n + X;
      - it called ten comparisons "ten printed rows".
      Each sentence was right in spirit and wrong in its stated object.
    - Literal plan fidelity is not an API contract: the approved code promised exactness at entries it did not guard.
  - *Changes:*
    - Scratch scripts that write files take an explicit output directory, never the working directory.
    - A seeded fault's description must name the assertion it is expected to trip, and the fault run checks that assertion's message.
    - Before a README is committed, every gate or fault it cites is checked against the code's exact expression, normalization included.
    - P4 reviews cover every public entry, not only the functions the plan exercises.
- **2026-10-15 · B05 transcription/specification stage (plan rev 1.2 → Tasks 1–6) · Claude (plan, transcription, spec, README), Codex (blind second reading via a fresh subagent, NP map, code, audits, register), Grok via pi and argon (plan reviews).**
  - *Worked:*
    - Asking Codex and Grok *before* planning which item comes next changed the plan from a rejection test into a specification stage. Both said a covariance test has nothing to fail against until the operator is pinned.
    - A fresh, blind subagent reproduced every entry of (9.16) independently. Its comparison caught an arithmetic error in Claude's source cross-check (an outer ∗ dropped in (9.18)), which had been used to claim the source fixes the pairing.
    - Pre-registered controls as executable tests (R1/R0/Rc variations) plus a fault reinstating the old error (F8) made the corrected criterion durable.
    - Differentiating the printed transformation formulas, rather than citing them, exposed a sign conflict *in the source*: (6.13) against (6.2)/(6.20)/(7.4). Codex's audit found it; Claude re-derived it.
  - *Didn't:*
    - Claude's criterion had S̄ = −S♯. Two reviewers caught it, and the "pre-registered control" had passed only because of the error.
    - Claude's spec also contained three more local errors, all found by audit:
      - "frozen commutator wrongly accepts C" (it rejects both C and iC);
      - a T1 dressing cancellation that fails for noncommuting factors;
      - the (2,2) "flips each" claim.
    - Claude's untracked `spec.md` draft under `experiments/B05/` tripped the runner's clean-tree guard and blocked Codex's result generation. The guard worked as designed.
    - The hand verdicts were not blind, because their author wrote the smoke code. This was disclosed, and the blind reading was supplied separately.
  - *Changes:*
    - Before citing a printed transformation law, compose and differentiate it against the neighbouring definitions. Record conflicts as branches (first occurrence; promote if repeated).
    - One degree chain per occurrence: never reuse a degree map across two occurrences of an overloaded operator without re-deriving each.
    - The orchestrator does not write under a producing directory while a worker's runner is pending. Drafts go to the scratchpad until the result is committed.
    - Claude-authored derivations used as evidence get an independent check before they constrain a spec. This is the third experiment in a row where Claude's own prose carried the residual errors; reviewers found them every time.
- **2026-10-16 · B07 one-direction variation (plan rev 1.1 → Tasks 1–5) · Claude (plan, transcription, README, P7: payload identical, 365 passed, 8 faults RED), Codex (blind second reading, code, runner, independent re-derivation, audit, register), Grok via pi (plan and implementation reviews).**
  - *Worked:*
    - The orchestrator ran the plan's code in a scratch smoke clone before the plan was reviewed. That fixed the expected numbers ahead of time (all 4D kernels trivial; twelve 14D witnesses with their signs), and the committed `result.json` matched the smoke payload byte for byte, minus `seconds` and `source_commit`.
    - Reducing (9.7) to a necessary pointwise condition (C1, the principal symbol of ½(L†−L)T) turned "does the variation match?" into a finite exact-kernel question with a one-entry counterexample form for 14D.
    - The family adapter was tested against B02's `shiab` on all 96 basis 2-forms for all eight modes, with two seeded faults (F6, F6b) keyed to that test. The survey therefore ran on the same operator B02 validated.
    - Codex's independent re-derivation shared only `gu.clifford`'s gamma matrices, used the actual matrix trace and its own Hodge star, and agreed on all 13 results.
    - Grok's review, asked a direct question the user posed (N0), found that the transcription's stated mechanism for N0 was wrong: the coefficient-wise extension of (12.26) is N2, not 0. The conclusion was unaffected, but the stated derivation was false.
    - Codex's README audit found four wording/hypothesis errors and no numerical disagreement.
  - *Didn't:*
    - Claude's N0 mechanism ("(12.26) extended with wedge and no grading sign") was asserted, not computed; one line of index relabelling or a call to `gu.cliffform.bracket` would have shown [T,T] = 2T∧T. The rev 1 comparison caught that N0 is not forced but not that the stated extension gives N2.
    - Claude then overstated Grok's N0 finding in two places ("the braced C-S terms vanish"; the brace includes ½d_BT). The audit caught it. This is again Claude's prose carrying the residual errors (fourth experiment in a row).
    - Claude's README wrote a C2 shortcut valid only for symmetric b without restricting it, used the metric pairing for a complementary-degree identity, and shortened H7's hypothesis lists. Each was right in substance and wrong in its stated domain.
  - *Changes:*
    - A registered reading that claims to come from a printed definition must be evaluated against the code's existing implementation of that definition (here `gu.cliffform.bracket`) before it is written down.
    - When summarizing a reviewer's or a ledger's conditions, copy the full hypothesis list or link the row; never abbreviate a hypothesis list.
    - Formulas specialized under an assumption (symmetric b, N1/N2) carry that assumption in the same sentence.
- **2026-10-16 · B07 Phase 2: actual ½(L+L†) and the second-order Lagrangian (plan rev 2 → Tasks 1–5) · Claude (plan, derivations H9–H14, README, P7: payload identical, 387 passed, 13 faults RED), Codex (code, runner, independent re-derivation, README audit, register), Grok via pi (derivation review, Argon discussion), GPT-6-Astra (Lean formalization of Argon's generous readings, squash-merged as a1c5701).**
  - *Worked:*
    - The smoke clone fixed every expected number before execution again: 40/8/2/16/0/0/0 at both signatures, three 14D C2 witnesses. The committed `result.json` equalled the smoke payload apart from `scope`, and the P7 clean-clone run equalled master apart from `seconds` and `source_commit`.
    - Codex's independent re-derivation imported only `gu.clifford` and agreed on all 18 comparisons.
    - Checking a reviewer's objection before adopting it paid off. Grok's H9 torsion objection was wrong on the maths (the graded Leibniz rule for d_B holds for any connection), but checking it improved the wording and placed torsion where it actually enters (H11).
    - The Lean pass on the most generous reading of Argon's notes produced a real finding: a trace-free torsion counterexample showing that H11's torsion-free hypothesis cannot be weakened to trace-free. Two reviewers checked it independently.
    - Codex's README audit found six wording errors and no numerical disagreement.
  - *Didn't:*
    - Coefficient-kernel dimensions were first counted as operator dimensions.
    - A background import clobbered a log.
    - The JSON dump crashed on `Fraction` after the full computation and cost 75 minutes.
    - Reviewer maths was adopted unchecked once (Grok's H10 point) before the H9 lesson above.
    - Claude misread Hom-space dimensions (up to 6) as isotypic multiplicities (at most 2). Grok caught it.
    - Claude's README dropped "nonzero" twice ("no operator" where X = 0 passes both gates); the audit caught it. This is Claude's prose carrying the residual errors for the fifth experiment in a row.
    - Claude reported b05-sign-lean as "awaiting merge" without checking ancestry; it was already on master.
  - *Changes:*
    - Smoke the result serializer on a tiny payload before any long run.
    - Kernel dimensions are reported with their space named (coefficient space, Hom space or operator space). Multiplicities come from an isotypic decomposition, never from a Hom dimension.
    - Every negative existence claim keeps its trivial-solution caveat ("no nonzero …").
    - Before reporting branch status, run `git merge-base --is-ancestor`.
    - Background jobs write to their own log files; never share a log with another process.
- **2026-10-17 · B07 non-GR channels (escape plan rev 1.1 → Tasks 1–5) · Claude (plan, derivations, Tasks 2–3 verbatim from the plan, README, register, P7: payload identical, 401 passed, 8 faults RED), Grok via pi (plan and derivation reviews), fresh Claude subagents (independent re-derivation, README audit). Codex out of quota and Grok out of OpenRouter credits for Tasks 4–5.**
  - *Worked:*
    - Embedding smoke-tested code verbatim in the plan let the orchestrator execute Tasks 2–3 mechanically (byte-compared against the smoke clone) and kept worker quota for the independent check. `result.json` equalled the smoke payload.
    - The re-derivation (gamma matrices only) agreed on 709/709 comparisons. Its first run disagreed by a uniform factor 16, which exposed an unstated summation range in B02's documented ξ formula; scale-free results agreed from the start.
    - The adversarial README audit found 11 wording/scope issues and no numerical disagreement.
  - *Didn't:*
    - Claude's README prose again carried the residual errors: R1 shortened (its hypothesis b² ≠ a² dropped), a Lovelock sentence that misattributed what representation theory forces, an Argon-exit sentence citing an argument Phase 2 does not contain. Sixth experiment in a row.
    - The register paragraph was first inserted mid-explanation; caught by re-reading the context.
    - Line endings: the smoke clone checked out CRLF, which silently broke multi-line fault patterns; the harness had to be made line-ending-aware.
    - From Git Bash, a pi slash command was path-converted (`/new` → `C:/Program Files/Git/new`) and sent as a prompt.
    - A watcher keyed on the status file's existence fired on a worker's `WORKING` marker.
  - *Changes:*
    - Name the documented normalization (summation ranges, ½ factors) for every formula a re-deriver must rebuild; record a scale disagreement as a documentation note in the README even when resolved.
    - Before the README is drafted, list each hypothesis of every consequence and check the summary paragraph keeps all of them.
    - Fault harnesses normalize line endings; watchers wait for the `DONE` token, not the file.
    - Send pi slash commands with `MSYS_NO_PATHCONV=1`; pi's `/new` resets the model, so re-set it.
    - When no non-Claude reviewer is available, say so in the README status line.
- **2026-10-17 · B07 escape: non-Claude retry of Tasks 4–5 · Codex (second independent re-derivation, exact SymPy), Grok via pi (audit of the README, the Claude re-derivation and the register), Claude (verification, re-runs, rederive revision, folds).**
  - *Worked:*
    - A second re-derivation by a different model, under a stricter import and reading list, agreed on 192/192 and independently hit the same unstated ξ summation range.
    - The worker refused to synthesize E_OP from its expected Q when the defining formula was outside its allowed sources, and reported the rows as unavailable rather than passed.
    - The non-Claude audit found what the Claude audit missed: 90 agree rows that compared a different predicate, zero by construction, under the production field's name.
  - *Didn't:*
    - Claude's brief for the re-derivation omitted the file that defines E_OP; four rows needed an extension.
    - The earlier Claude-only audit counted rows without checking that each compared the quantity its label names; the register again shortened README hypotheses.
  - *Changes:*
    - For each comparison row, check that both sides compute the same predicate, and mark rows that are entailed by other rows or zero by construction; do not count them as independent.
    - Pin observed counts (not just `> 0`) and every branch the prose mentions as rows.
    - Build a re-derivation brief's allowed-source list from where each object the worker must rebuild is defined (grep its name), not from memory.
- **2026-10-17 · B07 escape 14D E2 witnesses · Claude (plan, smoke, README, P7), Codex (Tasks 1–2 verbatim; independent matrix re-derivation in a fresh session), Grok via pi (plan review, README audit).**
  - *Worked:*
    - Smoke-testing the plan's code before writing it let the run be a confirmation: Codex's payload equalled the smoke payload, and P7 equalled both.
    - Stating the ξ summation range and the Hodge-star rule in the plan's mathematics section made the independent matrix re-derivation agree on its first run (the escape re-derivations had each tripped on the ξ range).
    - A new exact check (is the transported input ξ of a Weyl tensor?) explained an unexpected zero: two in-plane bivectors give no leak because they move W_P to another Weyl tensor.
  - *Didn't:*
    - Smoke development wrote `GQ(1, 2)` (= 1 + 2i) for ½; the U(A) gate caught it. `dressing` now rejects a non-Fraction t.
    - Claude edited the smoke clone twice while its full suite was running, which invalidated those runs.
    - Claude's plan stated a hand argument wrongly ("anticommutes" for a commuting bivector), and its README overstated two things: that the output maps are the same across signatures, and "the same leak" in 14D. Grok's reviews caught all three.
    - A seeded fault (W-F6) was caught only by the constructor's own assert. It now removes that assert too and fails on a pinned entry.
  - *Changes:*
    - Never edit a checkout while a suite or runner is running in it.
    - Every seeded fault must fail on a test assertion, not on an assert inside the code under test.
    - When a table summarizes counts, say whether the underlying maps also agree.
- **2026-10-21 · B07 option C (T-sector of I₂, frozen-metric R2 reading; pre-registered) · Codex (Tasks 1–2 verbatim; independent re-derivation in a fresh session), Grok via pi (README audit), Claude (design, plan, smoke, README, register, P7).**
  - *Worked:*
    - Pre-registering outcome classes before any code ran kept the README to the design's readings. The one place the design was too strong (the (3f) complex-root forcing sentence needs ker M = ker U) was found in the smoke run, stated in the plan, and handled as a README note without editing the frozen design.
    - Smoke-testing the plan's code made the run a confirmation: Codex's payload, the smoke payload and P7's payload have the same canonical SHA.
    - Three plan revisions under Codex review (10, then 6, then 0 findings) left the executor with one question (pre-existing untracked files), and no code fix.
    - The fresh-session re-derivation agreed on 1,444/1,444 records after fixing its own E_OP block normalization from the formula sources.
  - *Didn't:*
    - Sending `/new` to Codex through Git Bash without `MSYS_NO_PATHCONV=1` turned it into a file path, and the re-derivation brief reached the session that had written the Task 1 code. It was interrupted before writing anything and resent to a real fresh session.
    - The README draft said "every control held" (real closure fails at the auxiliary signatures, a declared exception), listed an unpinned 3D toy as run, showed one ray's Q4 (iii) data as if ray-independent, and called E_OP's nonzero S₁ an outcome. Grok's audit caught all four.
  - *Changes:*
    - Send every slash command to any pane with `MSYS_NO_PATHCONV=1`, and confirm the fresh session from the context meter (100% left) before sending a brief that requires independence.
    - Mention a declared exception wherever the README makes a "held" claim; list only fixtures that appear in the recorded control keys.
    - When a datum is recorded per ray or per root, tabulate every ray or root, or say which one is shown.
