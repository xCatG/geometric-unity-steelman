# B01 — Signature of the chimeric metric: reconciliation and verdict

Author: Claude (plan Task 4, step 1), 2026-10-15. Inputs:
- `transcription.md` (the draft, pp. 18–22)
- `ansatz.md` (pre-registered criterion)
- `result.json` (exact inertia, `source_commit` 0815385)

Independent re-derivation: `rederivation.md` (Codex), which confirmed every table entry and F1, and corrected N1 and the F1 repair (revised 2026-10-15).

## Verdict

**Match: holds, scope `identity`, under transcription branch R1.**

Every signature the draft enumerates on p. 22 is reproduced exactly, as inertia, by our family s_H·η ⊕ s_V·B_λ under an explicit symbol map. As forms, the match holds under one stated normalization assumption (see N1). The draft's two open choices correspond to two binary parameters of ours.

The one non-cosmetic consequence the draft does not state: mirroring the base metric (1,3) ↔ (3,1), which the draft calls "not meaningfully distinguished", switches the total metric between the (7,7) class and the (5,9)/(9,5) class (finding F1).

## Convention map (draft → ours)

| Draft | Ours | Why |
|---|---|---|
| Frobenius form ⟨A,B⟩_y = double contraction with y (3.8) | tr(ηAηB) = B₀ | Same formula with y = η in an orthonormal frame. |
| Trace component "(0,1)" (discarded) | λ = 0, where the trace direction has norm +4 | B₀ is the unmodified Frobenius form. |
| Trace component "(1,0)" (chosen) | any λ > 1/4; representative λ = 1/2, where the trace norm is −4 | The draft fixes only the trace direction's *sign*. B_{1/2} is the equal-magnitude choice (−Frobenius on the trace line). A trace norm of −4c corresponds to λ = (1+c)/4. See N1. |
| Vertical "(4,6)" or "(6,4)" | s_V = +1 or −1 | overall sign of the vertical summand |
| Base "(1,3), one temporal, three spatial" | s_H = −1 (i.e. −η = mostly plus) | forced by R1, see below |
| Signature "(a,b)" | (n_neg, n_pos) = our inertia read backwards | branch R1 |

**Why R1.** Our exact traceless part of B₀ is (6 positive, 3 negative): the 3 mixed time–space components are negative. This holds for either overall sign of η, because y⁻¹ appears twice in the Frobenius form. The draft writes "(3,6)" with first entry i(n−i) = 3, the mixed count. So on the traceless block the draft's first slot counts negative directions. Extending this to the base and the totals assumes the draft uses one slot order throughout. Under that assumption, R1 is the only reading that needs no unstated sign on the Frobenius form (R2 needs one). Under R1, "(1,3) with one temporal direction" is 1 negative and 3 positive, i.e. −η in our convention, so s_H = −1.

## Reproduction of the draft's enumeration (p. 22)

Rows use s_H = −1. "Ours" is read from `result.json` as (pos, neg); the draft column is (neg, pos) under R1.

| Draft vertical | Our λ, s_V | Ours (pos,neg) | Draft total (neg,pos) | Reproduced |
|---|---|---|---|---|
| (3,7), discarded | 0, +1 | (10,4) | (4,10) | ✓ |
| (7,3), discarded | 0, −1 | (6,8) | (8,6) | ✓ |
| (4,6), chosen | 1/2, +1 | (9,5) | (5,9) | ✓ |
| (6,4), chosen | 1/2, −1 | (7,7) | (7,7) | ✓ |

The vertical signatures reproduce too: B₀ is (7,3) as (pos,neg), i.e. "(3,7)" in R1; B_{1/2} is (6,4), i.e. "(4,6)" ✓. The traceless part is "(3,6)" ✓. The general formula (i(n−i), …) checks arithmetically (transcription, Convention 2).

Evidence: `verified:experiments/B01/result.json` (exact Hermitian congruence; tests in `tests/test_b01.py`).

## The "(9,5)" remark

The draft says to assume "(7,7) (rather than (9,5) …)", but (9,5) is not among its enumerated totals. Our table settles both readings:

- **(9a)** "(9,5)" is the draft's own (5,9) configuration written in the other slot order. Ours prints exactly this as (9,5) (pos,neg).
- **(9b)** "(9,5)" in R1 order means (5 pos, 9 neg) = our (s_H, s_V, λ) = (+1, −1, 1/2). That is the overall negative of the draft's (5,9) metric.

Either way, "(9,5)" and "(5,9)" differ at most by an overall sign of the metric on Y. They share p−q ≡ 4 (mod 8) and Spin(9,5) ≅ Spin(5,9). So the spec's run list {(7,7), (9,5)} covers both of the draft's live options. `[GU-recon]`, scope `identity`.

## Normalization assumption

**N1.** The draft specifies the trace component's signature but not its magnitude. Our exact form-level match uses the equal-magnitude reconstruction (λ = 1/2). Every λ > 1/4 matches the draft's *signatures*; no λ is singled out by the text. Signature-level claims in this README do not depend on N1.

## Findings

**F1. The base mirror is not cosmetic for the total signature** `[GU-recon]`, `verified:experiments/B01/result.json`, scope `identity`.
- The Frobenius form is even in y, so mirroring the base metric g → −g leaves the vertical summand unchanged and flips only the horizontal one. That flips the relative sign s_H·s_V.
- In the table: draft (7,7) = ours (−1,−1,½). Mirroring the base gives ours (+1,−1,½) = (5,9) (pos,neg), which is the (5,9)/(9,5) class.
- Flipping s_H and flipping s_V are distinct operations; their results differ by an overall sign. With the trace sector fixed, though, both toggle between the same two unordered signature classes, {(7,7)} and {(5,9),(9,5)}. So the draft's "cosmetic" choice (1,3) vs (3,1) (p. 19 and p. 22) and its "not yet forced" choice (7,7) vs (5,9) (p. 22) **select the same pair of classes**. The two statements are in tension unless the mirror is meant to act on the whole metric of Y, which the text does not say (transcription: last branch).
- **Repair** `[ext]`: tie s_V to the sign of the base metric, i.e. flip the whole vertical summand with the base. The mirror then negates the whole form, preserving the class. Exactly: η ⊕ B_{1/2} has inertia (7,7). Tying only the *trace* sign to the base does **not** work: η ⊕ (−B₀) has inertia (4,10), because flipping one direction cannot offset the two-unit shift from the horizontal mirror. (Counterexample found by Codex in its re-derivation; confirmed by Claude.)
- Impact: both classes remain live, so the spec's plan to run B02 on (7,7) and (9,5) stands.

**F2. The draft has no DeWitt parameter** `[GU-orig]`, scope `identity`. Its trace-sign choice ("non-forced", footnote 2) is realized exactly by λ = 1/2 and up to inertia by any λ > 1/4. The λ family is our `[ext]` device for that choice. It is not a draft parameter, and the degenerate boundary λ = 1/4 has no counterpart in the draft.

## What this does not establish

- Which of (7,7) and (5,9)/(9,5) is physical. The draft says this is not forced, and our result agrees.
- Anything about a global splitting of TY. This is fibrewise linear algebra on V ⊕ H* (spec §5).
- Branch R1 itself is a reading of the draft; it is the only branch consistent with (3.8) without an unstated sign.
