# Handoff notes: GU steelman (resume here)

Last updated: 2026-10-15, by Claude (orchestrator, pane 0:2). Read this file first after any context reset, then `.agent-handoff/auto-snapshot.md` (written by a local PreCompact hook; git and agent state that may be newer than this file), then `docs/methods.md`.

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
- **Agents:** the pi coding agent is now in pane 0:4 (GPT-6-Astra medium, web access) and available for lookups and side checks. agy is retired.

**Next**
1. ~~Resolve Codex's review~~ (done, `f75bb66`). ~~Retro~~ (done). ~~Write the B02 plan~~ (done).
2. **Wait for the user's approval of B02 plan revision 2.** Then dispatch Tasks 1–4 to Codex (one brief; the plan is self-contained). Claude does Task 5 (`proofs.md`) in parallel.
3. (Superseded; kept for the record.) Write the follow-up plan `docs/superpowers/plans/<date>-b02-direct-check.md` (writing-plans skill), from the reviewed transcription. Include the symbolic covariance derivation (Claude), the branch enumeration (brackets 2³ × Φ choices × signatures), tests 1–5 and 5′, and the H0 line item. Smoke-test the plan's code, and list the ambient impostors (P2b).
4. Get the user's approval of that plan, then dispatch it to Codex.
5. Later: P3 (B03 branching), P4 repairs, the write-up.

## Facts that are easy to get wrong

- The GU adjoint is u(64,64), dim 16384, not so(14). A = a phase times the product of the timelike gammas, with A Hermitian and A² = I. AΓ_aA⁻¹ = (−1)^q Γ_a†.
- γ_sγ_t (one spacelike, one timelike gamma) is **not** in U(A): h†Ah = −A.
- Weyl annihilation is automatic for undressed equivariant maps (D7 highest weight). The B02 exit gate is a **nonzero** Ricci and scalar response.
- (9.3) is explicitly not the author's preferred Shiab operator: that one is lost (footnote 10). A failure refutes only the displayed candidate.
- The draft PDF has SHA-256 `3f28d742…186d4`. Render pages with `uv run --no-project --with pymupdf python -I` plus `sys.stdout.reconfigure(encoding='utf-8')`; `Read` cannot open PDFs here because pdftoppm is missing.
