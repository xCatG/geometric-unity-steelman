# B02 transcription: the Shiab operator, GU (8.1)–(8.7) and (9.2)–(9.3)

Transcriber: Claude (Opus 5.5), 2026-10-15. Plan Task 9, step 1. Reviewer: Codex (step 3), verdict *revise*. Revision 2 (this file) applies every review finding; the review's decisive claims (grade-1 real form in both signatures; the appendix bracket definitions) were re-checked by Claude independently.

## Source

- Same PDF as `experiments/B01/transcription.md`: SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, 69 pages.
- Pages read as rendered images: 23–24 (§3.5–3.6), 32–33 (§5.2–5.3), 41–43 (§8–9.1), and the end matter 64–69 (read by Codex's independent second reader; p. 66 re-read by Claude). Eqs. (8.1) and (9.3) were also read at 300 dpi.

## Verbatim

**p. 23, (3.27)** (text extraction checked against the page):
$$\mathfrak u(64,64)\ \text{“=”}\ \bigoplus_{i=0}^{3}\Lambda^{4i+2}\ \oplus\ \bigoplus_{i=0}^{3} i\Lambda^{4i}\ \oplus\ \bigoplus_{i=0}^{3}\Lambda^{4i+1}\ \oplus\ \bigoplus_{i=0}^{2} i\Lambda^{4i+3}\ \subset\ \mathrm{Cl}_\mathbb{R}(7,7)\otimes\mathbb C$$
"corresponding to the Lie Group H = U(64,64), where the 'adjoint' operation in the Clifford Algebra is given by the operation of composing the canonical automorphism with the reversal of order of all basis vectors." Footnote 3: "This decomposition was taken from a decades old file and should be checked by someone…" (The three ⊕ separators between the big sums above are editorial; the print sets the sums adjacent.)

**p. 24, (3.31)–(3.35).** ϱ_D: Spin(7,7) → U(64,64) "on complex Dirac Spinors using the notation H = U(64,64)". The main bundle is P_H = P_{F̃r(C^{7,7})} ×_{ϱ_D} H, with ad = P_H ×_ad 𝔲(64,64) (3.34) and Ad = P_H ×_Ad U(64,64) (3.35).

**p. 32–33, (5.3), (5.8).** The gauge group is ℋ = Γ^∞(P_H ×_Ad H). The inhomogeneous gauge group is 𝒢 = ℋ ⋉ 𝒩, with 𝒩 = Ω¹(Y, ad(P_H)).

**p. 41, (8.1).** "By incorporating the gauge group into the contraction operator, the gauge group rotates only the bundle valued portion of a collection contracting forms {Φ_i} in which these special invariant differential forms are valued in such a way that it exactly compensates for the a symmetry of treatment in the form being contracted. Suppose for example that η is a gauge covariant ad−valued differential form. Then a Shiab contraction operator might look like:"
$$\circledcirc_\varepsilon\eta = *^{\,n}\, i^{\frac{1\pm1}{2}}\,\big[(\varepsilon^{-1}\Phi_r\varepsilon)\wedge *^{\,m}\eta\big]_\pm \tag{8.1}$$
"or perhaps a sum of such terms, where typically Φ_r is a normed Lie Algebra Valued r-form valued in an invariant subspace of the structure group of the tangent bundle and the bracket is either a commutator or an anti-commutator with a factor of i out front in the case of the latter."

**p. 42, (8.3)–(8.7).**
- ϑ: Λ*(T*Y) → Cl(T*X) = ℝ(128) (8.3). [Sic: "Cl(T*X)". The (7,7) context implies Cl(T*Y).]
- 𝔰𝔬(64,64) "=" (Λ² ⊕ Λ⁶ ⊕ Λ¹⁰ ⊕ Λ¹⁴) ⊕ (Λ¹ ⊕ Λ⁵ ⊕ Λ⁹ ⊕ Λ¹³) ⊂ Cl_ℝ(7,7) (8.5).
- 𝔲(64,64)/𝔰𝔬(64,64) "=" k₀Λ⁰ ⊕ k₃Λ³ ⊕ k₄Λ⁴ ⊕ k₇Λ⁷ ⊕ k₈Λ⁸ ⊕ k₁₁Λ¹¹ ⊕ k₁₂Λ¹² (8.6), "which must be multiplied by various factors of i inside the complexification".
- **Definition 8.1.** "Let {Φ_i}_{i=0}^{14} be a basis for the invariant subspaces of"
$$[\Lambda^i(\mathbb R^{7,7})\otimes\mathfrak u(64,64)]_{Spin(7,7)} \tag{8.7}$$
"seen as a Spin(7,7) representation."

**p. 42, §8.2.** "… some aspect of conjugation by the gauge group element ε ∈ ℋ ⊂ 𝒢 living inside the inhomogeneous gauge group 𝒢 as a non-linear sigma-field of sorts." "… the Bianchi identity was able to pick the best and most appropriate operator … the author … has been unable to locate the notes … that originally picked out the operator of choice."

**p. 43, (9.2)–(9.3).**
$$\circledcirc_\varepsilon:\ \Omega^2(Y^{7,7},\mathrm{ad})\longrightarrow\Omega^{d-1}(Y^{7,7},\mathrm{ad}) \tag{9.2}$$
"we will begin with one¹⁰ which makes the parallel to Einstein's contraction of the full Riemannian curvature explicit:"
$$\circledcirc_\varepsilon\xi=\underbrace{\big[(\varepsilon^{-1}\Phi^1\varepsilon)\wedge(*\xi)\big]}_{\text{Ricci Like}}-\frac{*}{2}\big[\underbrace{(\varepsilon^{-1}\Phi^1\varepsilon)}_{g_{\mu\nu}\text{-like}}\wedge *\underbrace{\big[(\varepsilon^{-1}\Phi^2\varepsilon)\wedge(*\xi)\big]}_{\text{Ricci Scalar Like}}\big] \tag{9.3}$$
"for a gauge covariant ad-valued 2-form ξ ∈ Ω²(Y, ad). Here, as in Einstein's case, the Weyl curvature tensor is annihilated by the contraction operator above so the operator preserves and mixes only the analogues of the Ricci and Scalar curvature components." Footnote 10: "The Shiab operator that he settled on (but cannot yet now locate) was chosen for its properties relative to the Bianchi identity."

**pp. 65–66, appendix "Other Elements of Shiab Constructions"** (missed in revision 1; found by Codex's second reader):
- Contraction: "Various forms of contraction can be defined either with co-variant against contravariant tensors in the obvious way or via the wedge and star operations between forms as in: φ ∨ μ = ∗(φ ∧ ∗μ)" (12.25).
- Bracket: "As with any Lie Group, U(64,64) carries a Lie Bracket structure. Given that it lives embedded within the Clifford Algebra Cl_ℂ(7,7) = ℂ(128), it can be constructed from the matrix algebra product in the usual fashion: [a,b] = a·b − b·a" (12.26).
- Symmetric product: "Unlike most Lie Algebras, there is a second symmetric product on 𝔲(n) gotten from taking: {a,b} = i(a·b + b·a)" (12.27).
- Volume form: "The analog of the Hodge Star operator is multiplication with the Clifford Volume form λ."

The appendix does not select Φ, its norm, its relative scale, or the lost preferred operator. pp. 66–69 contain no further such definitions.

## Symbol table

| Symbol | Type | Source |
|---|---|---|
| ξ | Ω²(Y, ad), i.e. a 𝔲(64,64)-valued 2-form on the 14-manifold Y | (9.3) |
| ∗ | Hodge star on Y^{7,7} (convention unstated) | (8.1), (9.3) |
| ε | section of P_H ×_Ad H, i.e. pointwise an element of U(64,64) | (5.3), §8.2 |
| Φ¹, Φ² | Spin(7,7)-invariant elements of Λ^i ⊗ 𝔲(64,64) for i = 1, 2: a "basis" element per degree | (8.7) |
| ε⁻¹Φ^iε | conjugation acting on the 𝔲 factor only | (8.1) text |
| [α ∧ β] | wedge on form parts with the commutator on the 𝔲 parts, per the appendix notation (12.26); the braces {·,·} = i·anticommutator (12.27) do not appear in (9.3) | (8.1) text, (12.26)–(12.27) |

**Degree check** (n = 14):
- Ricci-like term: Φ¹ is a 1-form and ∗ξ a 12-form, so [Φ¹ ∧ ∗ξ] is a 13-form ✓.
- Second term: [Φ² ∧ ∗ξ] is a 14-form; ∗ makes it a 0-form; [Φ¹ ∧ 0-form] is a 1-form; ∗ makes it a 13-form ✓.

So (9.3) is consistent with (9.2) under the reading "−½ ∗[…]".

## `[GU-recon]` branches

1. **The brackets in (9.3).** (9.3) contains **three** square-bracket operations: the Ricci-like term, the inner bracket of the second term, and its outer bracket. That gives 2³ = 8 assignments, written as strings such as CAA for (Ricci term, inner, outer), with C = commutator and A = i·anticommutator.
   - **Literal reading (ranked first):** all three are commutators (CCC). The appendix defines square brackets as the commutator (12.26) and reserves braces for i·anticommutator (12.27), and (9.3) prints only square brackets. Notation is evidence of intent, not proof of it.
   - **Reconstructed readings** `[GU-recon]`: the other seven assignments, licensed by (8.1)'s "either a commutator or an anti-commutator with a factor of i".
   - The graded sign is moot: for ad-valued forms α ∈ Ω^p, β ∈ Ω^q the graded commutator is α∧β − (−1)^{pq} β∧α, and pq is even for every bracket in (9.3) (12, 24, 0). So graded and ungraded agree.
2. **Φ¹ and Φ² are not unique** — confirmed by Codex's review, scope `identity` (representation-theoretic argument plus exact all-entry commutant ranks, both signatures):
   - dim_ℝ [Λ¹ ⊗ 𝔲(A)]^{Spin} = dim_ℝ [Λ² ⊗ 𝔲(A)]^{Spin} = **2** in both (7,7) and (9,5). Only Clifford grades 1/13 (resp. 2/12) can contain Λ¹ (resp. Λ²), each once.
   - Real bases, with C = Γ_* the chirality and real coefficients α, β, γ, δ:
     - Φ¹ = αF + βF′, with F = Σ_a e^a ⊗ Γ_a and F′ = Σ_a e^a ⊗ Γ_aC;
     - Φ² = γB + δB′, with B = Σ_{a<b} e^{ab} ⊗ Γ_aΓ_b and B′ = Σ_{a<b} e^{ab} ⊗ iΓ_aΓ_bC (B·C without the i is outside 𝔲(A)).
   - The draft's "{Φ_i}_{i=0}^{14}" indexing suggests one per degree, which contradicts this count. Which element or combination is meant is unresolved. "Normed" names no norm, and some combinations (e.g. F + F′) are null for the natural trace form, so admissibility depends on that unstated norm.
3. **Normalization.** The draft says "normed" but gives no norm. The relative coefficient −½ in (9.3) assumes a normalization of Φ¹ and Φ² (as with g and Einstein's ½). Branch: each Φ normalized so that its contraction reproduces Riemannian Ric and S in the Levi-Civita case (the reading that makes "Einstein-like" literal), or unresolved.
4. **Hodge-star convention.** Unstated. Use the spec's pinned convention (α∧∗β = ⟨α,β⟩vol). Under another convention the result can differ by signs per degree; record that as a branch if it matters.
5. **The real form (3.27) is the same in both signatures** (revision 1 claimed otherwise; that was wrong, since 5 and 7 are both odd). With X^♯ = A⁻¹X†A, every Clifford blade of degree k satisfies Γ_I^♯ = (−1)^{qk + k(k−1)/2} Γ_I. For odd q this depends only on k, so in both (7,7) and (9,5):
   - real coefficients in 𝔲(A): grades 1, 2, 5, 6, 9, 10, 13, 14;
   - imaginary coefficients: grades 0, 3, 4, 7, 8, 11, 12.

   This matches (3.27) exactly, so the draft's footnote-3 request to check it is answered: correct for both pairings. The phase that makes A Hermitian cancels under conjugation; it should not be confused with the phase of an element of 𝔲(A). Evidence: Codex's sharp-identity proof plus `adjoint.is_in_algebra` on one blade per grade; Claude re-checked grade 1 independently (Γ_a ∈ 𝔲(A), iΓ_a ∉ 𝔲(A), both signatures).
6. **The domain of ε.** Pointwise ε ∈ U(64,64) (from ℋ). Our tests use h with h†Ah = A (spec §4). The draft never uses geometric Spin elements as dressings, which is consistent with the spec's separation.

## The draft's stated properties (to test)

- (P1) **Degree:** Ω² → Ω¹³ `[GU-orig]` (9.2).
- (P2) **Real form:** the values stay in ad, i.e. 𝔲(64,64) `[GU-orig]` (9.2). Both brackets preserve 𝔲(A) (if X, Y are ♯-skew, so are [X,Y] and i(XY+YX)), so this reduces to Φ ∈ 𝔲(A)-valued forms and real Hodge coefficients.
- (P3) **Gauge covariance via dressing:** "rotates only the bundle valued portion … exactly compensates" (p. 41) `[GU-orig]`, stated qualitatively. Spec §5 test 3 makes it precise.
- (P4) **Weyl annihilation:** "the Weyl curvature tensor is annihilated" (p. 43) `[GU-orig]`. For undressed equivariant maps this holds automatically (spec §5).
- (P5) **The response is Einstein-like:** "preserves and mixes only the analogues of the Ricci and Scalar curvature components" (p. 43), with Ricci-like and Ricci-scalar-like labels and a −½ coefficient `[GU-orig]`. **No explicit numerical response is given.** The expected scalar and traceless-Ricci outputs are therefore `[GU-recon]` (branch 3): the "Einstein-like" reading is G_ab = Ric_ab − ½ S g_ab, with relative coefficient −½.
- (P6) The operator is **not the author's preferred one**. That one is "chosen for … Bianchi identity" and lost (footnote 10, §8.2) `[GU-orig]`. So a failure of (9.3) is a failure of the displayed candidate, not of "GU's Shiab".
