# B02 ansatz: direct check of GU (9.3) (pre-registered)

Provenance: the operator is `[GU-orig]` (9.3); everything branch-dependent is `[GU-recon]` per `transcription.md`. Committed before any B02 code exists. Results go in a later commit.

**Signatures:** (7,7) and (9,5), as runtime parameters. The (9,5) case is `[ext]`, because the draft computes only (7,7).

## Pre-analysis (Claude, by hand; to be checked, not assumed)

Take ξ to be the Levi-Civita-type input ξ = ½ R_{abcd} e^{ab} ⊗ ¼Γ^{cd}, take Φ¹ = e^a ⊗ Γ_a and Φ² = e^{ab} ⊗ Γ_{ab}, and set ε = 1. Then the Clifford grade rules predict:
- **Ricci-like term:** the commutator [Γ_a, Γ^{cd}] is grade 1, so the commutator branch contracts R to Ric. The anticommutator gives grade 3, which is not Ricci-like.
- **Inner scalar term:** the anticommutator {Γ_{ab}, Γ^{cd}} contains grade 0, so the i·anticommutator branch extracts S. The commutator has no grade-0 part.
- **Outer term:** the inner result is ∝ i·S·I, which is central. A commutator with it vanishes, so only the i·anticommutator branch survives.

**Prediction H0:** the only "Einstein-like" bracket assignment is (commutator, i·anticommutator, i·anticommutator) for (Ricci term, inner, outer). Every other assignment drops the scalar term or produces non-Ricci grades. Scope once run: `identity` for the enumerated branches.

## Tests and pass criteria

Each test is run for every branch combination: brackets (2³) × Φ choices (Γ-type, Γ·Γ_*-type) × signature. Each result is recorded with its scope.

| # | Test | Pass criterion | Scope target |
|---|---|---|---|
| 1 | Degree | output in Ω¹³ for every Ω² basis input | identity (by linearity, checked on a basis) |
| 2 | Real form | output in 𝔲(A) for inputs in Ω² ⊗ 𝔲(A), on a basis of Ω² ⊗ (a spanning set of 𝔲 grades) | identity on the checked basis; sampled otherwise |
| 3 | Dressed covariance Shiab_{εh}(h⁻¹ξh) = h⁻¹Shiab_ε(ξ)h | (a) symbolic derivation from the conjugation structure (Claude writes it, Codex checks it); (b) exact Cayley regression samples for ≥3 h and ≥2 ε | (a) identity; (b) sampled |
| 4 | Geometric Spin(p,q) equivariance of the undressed map (ε = 1) | exact commutation with the 13 adjacent generators J_{a,a+1}, on a basis of the inputs used | identity (identity component) |
| 5 | Curvature response (exit gate) on certified pure-sector inputs from `gu/curvature.py` | **scalar** and **traceless-Ricci** inputs give nonzero outputs; after ∗ to Λ¹ ⊗ 𝔲, the outputs lie in span{e^a ⊗ Γ_b} and equal c·(Ric − κ S g)_a{}^b for constants c ≠ 0 and κ, the same for both inputs; **Weyl** inputs give 0 | identity on a basis of each pure sector |
| 5′ | Open data: Shiab_ε(W) for ε ∈ U(A) outside the image of Spin(p,q) | record zero or nonzero; no expectation | sampled |

**Reporting κ.** κ depends on how Φ¹ and Φ² are normalized relative to each other (transcription branch 3). Report κ for two normalizations:
- (N-a) Φ¹ and Φ² with unit coefficients as written above;
- (N-b) Φ² rescaled so that the Riemannian contraction gives S exactly.

"Einstein-like" `[GU-recon]` means κ = ½ under some stated normalization. Report the value under N-a as it is, without tuning.

## Verdict rules (fixed in advance)

- `holds (displayed candidate)`: tests 1, 2, 4 and 5 pass for at least one branch combination, with 3(a) proved. Name that combination.
- `obstructed-within-X`: no branch combination passes test 5 with c ≠ 0. That is a counterexample family for the displayed (9.3) **only**. It says nothing about the author's lost preferred operator (transcription P6).
- Test 3(b) failing while 3(a) is proved means an implementation bug, not a finding.
- H0 is confirmed or refuted as its own line item.

## Inputs fixed now

- Clifford: `gu.clifford.gammas`, `dirac_pairing`, `chirality`, with A as in spec §4.
- Forms and Hodge star: `gu.forms` (pinned convention).
- Curvature sectors: `gu.curvature.decompose` and its controls.
- Group elements: `gu.adjoint.cayley`; a singular Cayley denominator is logged and resampled, never counted as an operator failure.
