# B02: the Shiab operator (9.3), direct check, reconciliation and verdict

Author: Claude (plan Task 6, steps 1–2), 2026-10-15.

Inputs:
- `transcription.md` (revision 2; draft pp. 23–24, 32–33, 41–43, 65–66)
- `ansatz.md` (pre-registered, amendment 1)
- `proofs.md` (Task 5; checked by Grok)
- `result.json` (exact identity check; `source_commit` d66cd8f)
- plan `docs/superpowers/plans/2026-10-15-b02-direct-check.md` (revision 3)

Independent re-derivation of the classification: Codex (Task 6, step 3). A Lean 4 formalization of `proofs.md` is in progress on branch `b02-lean`. Neither is claimed here until it is merged.

## The closed form everything below follows from

For ξ = ξ(R) with R an algebraic (Levi-Civita-type) curvature tensor, Φ¹ = αF + βF′ and Φ² = γB + δB′:

∗Shiab(ξ) = −[m₀=C]·E_T(Ric) + (S/2)·([m₁m₂=AA]·γ·E_T(g) + [m₁m₂=AC]·δ·E_{T′}(g)),

where T = (α, β) and T′ = (β, α). The bracket string m₀m₁m₂ names (Ricci term, inner, outer), with C the commutator and A i·anticommutator.

- **Scope `identity`, in (3,1), (7,7) and (9,5).** `experiments/B02/response.py` asserts this formula exactly, in Gaussian-rational arithmetic. It checks every bracket assignment × {F, F′} × {B, B′, 0} on every Kulkarni–Nomizu product KN(s, t) of the symmetric basis. There are 2640 cases at n = 4 and 267120 at n = 14. The KN products span the algebraic curvature tensors (certified rank 20/20 and 3185/3185; `result.json`, `spanning_rank`). Linearity in R and affinity in (γ, δ) extend the identity to every algebraic R and all real (α, β, γ, δ) (`proofs.md`, §§ "Parameter extension" and "Extension to all algebraic curvature").
- **Not in `result.json`.** κ is derived below from the asserted formula, not read from a field (review G3).
- **Signatures.** All three have odd q. At even q (sampled at (2,2) and (4,0)) the relative sign of the two terms flips. Every signature this project uses has odd q.

Response coefficients follow the ansatz: the output is c·E_T(Ric − κSg). κ = ½ is "Einstein-like". This requires r_T ≠ 0 (test 5a), and a nonzero traceless-Ricci sector (n ≥ 3; at n = 2, (c, κ) is not identifiable). Every κ here is for n = 4 and n = 14.

## Verdict

**1. Literal reading CCC: `obstructed-within-literal`, scope `identity`.**

The "Ricci-scalar-like" −½ term of (9.3) is identically zero on Levi-Civita curvature. So ∗Shiab(ξ) = −E_T(Ric): κ = 0, for every Φ¹ ≠ 0 and every Φ². This is the consequence of the literal reading that does not depend on any convention. It holds:
- at any scale of ξ, Φ¹ or Φ²;
- under either standard Hodge star;
- with either generator normalization (Γ_aΓ_b or ½Γ_aΓ_b).

**Mechanism** (`proofs.md`, § "Literal CCC has no scalar term"): with inner bracket C, the inner term pairs R_abcd (symmetric under (ab) ↔ (cd)) with [Γ_aΓ_b, Γ_cΓ_d] (antisymmetric). The weight that the pinned ξ and the Hodge star put on each term is η_aη_bη_cη_d up to one global sign, which is symmetric. So the sum vanishes. CCA behaves the same way.

**Scope of the claim:**
- even n;
- the pinned ξ, including its η_cη_d index-raising factors;
- curvature with pair symmetry R_abcd = R_cdab.

It is **not** a statement about general gauge curvature (see "What this does not establish").

**2. Reconstructed readings: `holds-Einstein` (reconstructed), scope `identity`, odd q, pinned star.**

Every listed branch passes tests 1, 2, 4 and 5b with 3(a) proved:

| Branch | Φ | κ | Einstein iff | Norm status |
|---|---|---|---|---|
| CAA, N-a | Φ¹ = αF + βF′ with T ≠ 0; any δ | γ/2 | **γ = 1** | Under the trace norm, admissible iff α² ≠ β² and δ ≠ ±1 |
| CAC, N-a, chiral | Φ¹ = α(F ± F′), i.e. β = sα with s = ±1; any γ | sδ/2 | **sδ = 1** | Φ¹ is null under the trace norm. Excluded if null directions are excluded. Not a headline. |

- **Undefined or zero branches.** All other branches either have κ = 0 (CCC, CCA, and CAC with δ = 0) or κ undefined. κ is undefined for m₀ = A and for T = 0, because there r_T = 0 and 5a fails; undefined is not the same as 0.
- **Branches where 5a fails.** CAA at γ = 2/n and CAC at sδ = 2/n have no scalar response, so 5a fails there too.
- **N-b.** N-b is defined only when the inner bracket is A, δ = 0 and γ ≠ 0. It gives CAA κ = 1 and CAC κ = 0, so **N-b has no Einstein branch**.

**3. H0: confirmed, scope `identity`.**

For Φ¹ = F, Φ² = B under N-a, with the pinned Hodge star and odd q, CAA is the unique bracket assignment with κ = ½. All four qualifiers are required:
- **(F, B):** other Φ change κ (table above).
- **N-a:** N-b gives κ = 1.
- **Pinned star:** under ∗′, CAA with B gives κ = −½.
- **Odd q:** even q flips κ (sampled).

The response is c = −1, κ = ½. The hand control KN(g,g) gives −2(n−1)F under CCC and (n−1)(n−2)F under CAA (`run.hand_control`).

**4. Displayed (9.3) as a whole: not obstructed.**

Some reconstructed branch passes 5b, so (9.3) is not a counterexample family. Its Einstein point is set by a choice of the unit and sign of Φ², which the draft does not make. See finding F2.

## Convention map (P9: formula, normalization, consequence)

| Convention (draft is silent unless noted) | Our choice | What changes if it is changed |
|---|---|---|
| Bracket in each of the three slots | All 8 assignments; literal = CCC. Square brackets mean commutator per (12.26). | Verdict lines 1 and 2 |
| Φ¹, Φ² ("a basis element per degree"; the invariant spaces are 2-dimensional) | Φ¹ = αF + βF′, Φ² = γB + δB′, all real | κ, through γ, δ and s |
| Hodge star (convention unstated) | Pinned: α∧∗β = ⟨α,β⟩vol | Under ∗′ = (−1)^k∗ (even n), Shiab′(Φ¹, Φ²) = Shiab(Φ¹, −Φ²) exactly. So γ, δ → −γ, −δ: CAA Einstein iff γ = −1, CAC iff sδ = −1. The final read-off ∗ flips c, not κ (`proofs.md`). CCC unaffected. |
| Unit 2-form in Φ² ("normed", no norm) | N-a: Γ_aΓ_b, unit coefficients | With the spin generator σ_ab = ½Γ_aΓ_b, γ = ½ gives κ = ¼. This still passes 5a at n = 14, since ½ ≠ 2/14. CCC unaffected. |
| Normalization to Einstein's S | N-b: inner contraction exactly iS·I | CAA κ = 1; no Einstein branch |
| Norm used to exclude null Φ | Reported both ways | Trace norm N(X) = Σ_I η_I Tr(X_I X_I)/dim S. This is complex-bilinear, Ad-invariant and indefinite. It gives N(αF + βF′) = n(α² − β²) and N(γB + δB′) = C(n,2)(δ² − γ²). F ± F′ and B ± B′ are null for one shared reason: the dual copies carry the opposite-sign norm. A positive-definite norm (Re Tr X†Y) has no null directions but is not Ad-invariant for U(64,64). |
| ξ index convention | ξ(R) = ½ Σ R_abcd η_cη_d e^{ab} ⊗ Γ_cΓ_d | Dropping η_cη_d breaks the CCC cancellation (nonzero in (3,1)). This convention is pinned, not optional. |
| Signature parity | Odd q: (3,1), (7,7), (9,5); the project's (1,3) and (5,9) also have odd q | Even q flips κ (sampled), CCC stays 0 |
| Graded vs ungraded bracket | Ungraded | Moot: every bracket in (9.3) has an even product of form degrees (transcription, branch 1) |

## Findings

**F1. The literal operator has no scalar curvature term** `[GU-orig]` operator, `identity`.
- With the draft's own bracket notation (12.26), the term it labels "Ricci Scalar Like" vanishes on every Levi-Civita curvature, under every convention we could vary.
- The literal (9.3) therefore contracts curvature to −E_T(Ric), which is Ricci, not Einstein.
- The −½ coefficient the text draws attention to multiplies zero.
- This is the result of B02 that is stable under every convention.

**F2. Einstein requires a reconstructed bracket and a chosen unit and sign for Φ²** `[GU-recon]`, `identity`.
- The reconstructed CAA (inner and outer i·anticommutators) is Einstein-like exactly at γ = 1 under N-a and the pinned star. It is at γ = −1 under ∗′.
- κ = ¼ under the spin-generator unit, and κ = 1 under N-b.
- The draft fixes none of these, so "the operator is Einstein-like" is a statement about a choice, not about (9.3) as printed.
- The ansatz pre-registered H0 as a sampled observation (κ = ½ for CAA, F, B, N-a). It is now `identity` scope, with the qualifiers stated.

**F3. The Ricci term needs the commutator** `identity`.
- With m₀ = A, the Ricci term vanishes on algebraic curvature: its Clifford grade-3 coefficient is killed by the first Bianchi identity.
- r_T = 0, so 5a fails and κ is undefined.
- This uses the Bianchi identity, so it does not carry over to general gauge curvature.

**F4. Φ is not unique, and the second Einstein family is chiral and null** `identity`.
- The invariant spaces are 2-dimensional (transcription, branch 2). This produces the CAC family Φ¹ = α(F ± F′) = Σ eᵃ ⊗ αΓₐ(1 ± C), which is a chirally projected soldering form.
- It is null under the natural trace norm, as are B ± B′.
- Whether it counts depends on a norm the draft does not name. Both families are reported.

**F5. Weyl annihilation holds undressed, but not after an odd dressing** `sampled`.
- Undressed: Weyl curvature is annihilated in every branch. This is automatic for an equivariant map, and the closed form has no Weyl dependence.
- Open data 5′ (`result.json`, `open_data_5prime`): for F, B under CCC and CAA, dressing by two odd Cayley elements gives Shiab_ε(W) ≠ 0 on the sampled Weyl input, in all three signatures. The vector dressing gives 4 terms and the triple-blade dressing 2.
- The draft's "the Weyl curvature tensor is annihilated" therefore holds for ε in the stabilizer, not for a general gauge dressing.
- This is sampled open data with no expectation. It covers only F, B with CCC and CAA, and two odd dressings.

**F6. Signature parity** `sampled`. At even q (2,2) and (4,0), the relative sign between the two terms flips, so CAA has κ = −½, while CCC stays at κ = 0. No project signature is affected.

## Supporting checks

- **Test 1 (degree), test 2 (real form), test 3(a) (dressed covariance), test 4(iii) (Spin₀ equivariance):** proved in `proofs.md`.
- **Tests 2(b) and 4(i)/(ii):** `identity` checks in `tests/test_shiab.py`.
- **Test 3(b), Cayley-dressed covariance:** exact samples in `tests/test_dressing.py`. They pass in (3,1), (7,7) and (9,5), with sparse Cayley matching the library Cayley.
- **Seeded faults** (P2): eleven, all red, including −½ → +½ in `assemble` turning the standalone verifier red at `(3,1,0,4,F,B,CAA)`. Claude independently seeded −½ → −1 and got the same verifier failure. See `.agent-handoff/b02-impl/result.md`; it is an untracked working note, cited for provenance only.
- **Test suite:** 222 passed.

## What this does not establish

- **Non-Levi-Civita curvature.** For a general gauge curvature, pair symmetry R_abcd = R_cdab and the first Bianchi identity both fail. Then the CCC cancellation (F1) and the vanishing of the A-type Ricci term (F3) need not hold, so the classification above is specific to algebraic curvature.
- **The author's preferred operator.** The draft says its preferred Shiab operator was "chosen for its properties relative to the Bianchi identity" and lost (footnote 10; transcription P6). B02 tests the displayed candidate (9.3) only. Nothing here is a statement about that operator.
- **Pin or O equivariance.** Equivariance is proved for Spin₀ only.
- **Even q.** Even-q signatures are sampled, not proved.
- **Dressed behavior beyond the 5′ samples.**
- **A physical choice of norm, star convention or unit for Φ.** The draft makes none, and the Einstein point moves with each.
