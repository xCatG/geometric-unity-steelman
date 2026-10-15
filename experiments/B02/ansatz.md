# B02 ansatz: direct check of GU (9.3) (pre-registered, amendment 1)

Provenance: the operator is `[GU-orig]` (9.3); everything branch-dependent is `[GU-recon]` per `transcription.md` (revision 2).

**Amendment 1 (2026-10-15), and what it does and does not pre-register.** Revision 0 (`ecdf966`) was committed before any B02 code. Codex's adversarial review then found the gate unsound (findings F2–F7, below) and, in doing so, computed the response on **sampled** curvature controls for every pure-basis branch. This amendment is made *after* those sampled outcomes are known, so it does not pre-register them. What it pre-registers, before any production B02 code exists, is: the pinned conventions, the identity-scope tests, the gates, and the verdict rules. The sampled outcomes are listed under "Known before the run" so that nobody mistakes them for predictions.

**Signatures:** (7,7) and (9,5), as runtime parameters; (3,1) as the small control (P5). (9,5) is `[ext]`: the draft computes only (7,7).

## Pinned conventions (review F6)

- e^{ab} = e^a ∧ e^b, Γ_{ab} = Γ_aΓ_b for a < b; **every sum runs over increasing index sets**.
- Curvature input: ξ(R) = ½ Σ_{a<b, c<d} R_{abcd} η_cη_d e^{ab} ⊗ Γ_cΓ_d, with R from `gu.curvature` (its Ricci convention: Ric_bd = η^{ac}R_abcd).
- Hodge star: `gu.forms.hodge` (α∧∗β = ⟨α,β⟩vol). ∗∗ = +1 on degrees 1 and 13 in both signatures.
- Brackets: C = commutator (12.26), A = i·anticommutator (12.27). A string such as CAA lists (Ricci term, inner, outer).
- Φ¹ = αF + βF′, Φ² = γB + δB′ with real α, β, γ, δ, using the real bases of transcription branch 2.
- Output embedding: Φ¹ fixes T_a = αΓ_a + βΓ_aC. For a symmetric tensor H, E_T(H) = Σ e^a ⊗ H_a{}^b T_b (second index raised with η). After the final ∗, each output is compared with E_T of the **same** branch, never with a fixed grade-1 copy (review F3).
- Response coefficients: r_T is the ratio to E_T(Ric) on traceless-Ricci inputs, r_S the ratio on pure-scalar inputs. Then c = r_T and κ = (1 − r_S/r_T)/14, so that the output is c·E_T(Ric − κSg). Both ratios must hold on the **whole** sector, not on single samples.

## Normalizations (reported, never tuned)

- **N-a:** the pinned conventions above, with unit coefficients.
- **N-b:** Φ² rescaled so that the inner contraction is exactly S on the central line iℝ·I identified with ℝ. Review F6 shows this is *not* automatically Einstein's normalization, because the outer symmetric product contributes its own factor of 2.

Report κ under both. "Einstein-like" `[GU-recon]` means κ = ½ under N-a or N-b, stated which.

## Tests and pass criteria

Branch space: 8 bracket assignments × (α, β, γ, δ) × signature. The four pure choices (F or F′) × (B or B′) are run exhaustively. General combinations follow exactly by linearity (the Ricci term is linear in Φ¹, the scalar term bilinear in Φ¹, Φ²), so the full four-parameter family is solved symbolically, not sampled (review F4). Results are then reported both with and without the null directions excluded (e.g. F ± F′), since "normed" names no norm.

| # | Test | Pass criterion | Scope |
|---|---|---|---|
| 1 | Degree | output in Ω¹³ for every Ω² basis input | identity (linearity, basis) |
| 2 | Real form | (a) proof that C and A preserve 𝔲(A) (closure under ♯); (b) exact check that F, F′, B, B′ are 𝔲(A)-valued; (c) real Hodge coefficients. One blade per grade is **not** a spanning set and is not used as one (review F7). | identity |
| 3 | Dressed covariance Shiab_{εh}(h⁻¹ξh) = h⁻¹Shiab_ε(ξ)h | (a) symbolic derivation (Claude writes, Codex checks); (b) exact Cayley samples, ≥3 h and ≥2 ε | (a) identity; (b) sampled |
| 4 | Spin(p,q) equivariance of the undressed map | exact commutation with the 13 adjacent generators J_{a,a+1} on the named input basis | identity (identity component, named basis) |
| 5a | Nonzero equivariant contraction | on certified pure sectors from `gu.curvature`: Weyl → 0; scalar and traceless-Ricci → nonzero multiples of E_T(g) and E_T(Ric₀); r_T ≠ 0 | identity on a basis of each pure sector |
| 5b | **Einstein gate** | 5a passes **and** κ = ½ under N-a or N-b (named) | identity |
| 5′ | Open data: Shiab_ε(W) for ε ∈ U(A) outside the image of Spin(p,q) | record zero or nonzero; no expectation | sampled |

Passing 5a alone is labeled "nonzero Ricci/scalar contraction", **never** "Einstein-like": any equivariant map has some c and κ (review F2).

## H0 (restricted, review F4/F8)

For Φ¹ = F, Φ² = B (pure, ordinary copies) under N-a: CAA is the unique bracket assignment with κ = ½. Mechanism (hand-derived in the review, to be made identity-scope):
- Ricci term: C gives −2E_F(Ric) on 2ξ. The A-branch Clifford grade is 3, and its coefficient vanishes on algebraic curvature by the first Bianchi identity (not on general gauge curvature).
- Inner bracket: C vanishes (antisymmetric under pair exchange, while R_abcd = R_cdab). A gives a multiple of iS·I.
- Outer bracket on the central term: only A survives.

H0 is confirmed or refuted as its own line item. It makes no claim about general (α, β, γ, δ): e.g. Φ¹ = F + F′, Φ² = B′ reaches κ = ½ with CAC.

## Known before the run (sampled, from the review; not predictions)

Exact, on scalar, diagonal-Ricci, off-diagonal-Ricci and Weyl controls in (3,1), (7,7), (9,5):
- **Literal reading CCC with F, B:** output −E_F(Ric) on ξ, so κ = 0. The second term of (9.3), the "−½" Ricci-scalar term, vanishes on these inputs.
- CAA with F, B: κ = ½ under N-a (r_T = −2, r_S = 12 on 2ξ in both 14-dimensional signatures). Under N-b, κ = 1.
- CAA with F′, B: the same Einstein response, in the grade-13 embedding E_{F′}.
- Weyl → 0 for every branch.

## Verdict rules (fixed now)

Each reading gets its own line in the result. The verdict never merges readings.
- **Literal reading (CCC).** `holds-Einstein` if 5b passes for some admissible (α, β, γ, δ) with CCC; otherwise `obstructed-within-literal` with the identity-scope reason (e.g. "the scalar term vanishes on Levi-Civita curvature").
- **Reconstructed readings.** `holds-Einstein (reconstructed: <brackets>, <Φ>, <N>)` for every branch passing 1, 2, 4, 5b with 3(a) proved; list them all.
- `obstructed-within-X` for the displayed (9.3) only if no branch passes 5b. That is a counterexample family for (9.3) **only**, not for the author's lost preferred operator (transcription P6).
- 3(b) failing while 3(a) is proved means an implementation bug, not a finding.
- H0 is confirmed or refuted as its own line item.

## Inputs fixed now

- Clifford: `gu.clifford.gammas`, `dirac_pairing`, `chirality`, with A as in spec §4.
- Forms and Hodge star: `gu.forms` (pinned convention).
- Curvature sectors: `gu.curvature.decompose` and its controls.
- Group elements: `gu.adjoint.cayley`; a singular Cayley denominator is logged and resampled, never counted as an operator failure.
