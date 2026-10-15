# B02 transcription: the Shiab operator, GU (8.1)–(8.7) and (9.2)–(9.3)

Transcriber: Claude (Opus 5.5), 2026-10-15. Plan Task 9, step 1. Reviewer: Codex (step 3).

## Source

- Same PDF as `experiments/B01/transcription.md`: SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.
- Pages read as rendered images: 23–24 (§3.5–3.6), 32–33 (§5.2–5.3), 41–43 (§8–9.1). Eqs. (8.1) and (9.3) were also read at 300 dpi.

## Verbatim

**p. 23, (3.27)** (text extraction checked against the page):
$$\mathfrak u(64,64)\ \text{“=”}\ \bigoplus_{i=0}^{3}\Lambda^{4i+2}\ \oplus\ \bigoplus_{i=0}^{3} i\Lambda^{4i}\ \oplus\ \bigoplus_{i=0}^{3}\Lambda^{4i+1}\ \oplus\ \bigoplus_{i=0}^{2} i\Lambda^{4i+3}\ \subset\ \mathrm{Cl}_\mathbb{R}(7,7)\otimes\mathbb C$$
"corresponding to the Lie Group H = U(64,64), where the 'adjoint' operation in the Clifford Algebra is given by the operation of composing the canonical automorphism with the reversal of order of all basis vectors." Footnote 3: "This decomposition was taken from a decades old file and should be checked by s[omeone]…"

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

## Symbol table

| Symbol | Type | Source |
|---|---|---|
| ξ | Ω²(Y, ad), i.e. a 𝔲(64,64)-valued 2-form on the 14-manifold Y | (9.3) |
| ∗ | Hodge star on Y^{7,7} (convention unstated) | (8.1), (9.3) |
| ε | section of P_H ×_Ad H, i.e. pointwise an element of U(64,64) | (5.3), §8.2 |
| Φ¹, Φ² | Spin(7,7)-invariant elements of Λ^i ⊗ 𝔲(64,64) for i = 1, 2: a "basis" element per degree | (8.7) |
| ε⁻¹Φ^iε | conjugation acting on the 𝔲 factor only | (8.1) text |
| [α ∧ β] | wedge on form parts with a bracket on the 𝔲 parts: commutator or i·anticommutator | (8.1) text |

**Degree check** (n = 14):
- Ricci-like term: Φ¹ is a 1-form and ∗ξ a 12-form, so [Φ¹ ∧ ∗ξ] is a 13-form ✓.
- Second term: [Φ² ∧ ∗ξ] is a 14-form; ∗ makes it a 0-form; [Φ¹ ∧ 0-form] is a 1-form; ∗ makes it a 13-form ✓.

So (9.3) is consistent with (9.2) under the reading "−½ ∗[…]".

## `[GU-recon]` branches

1. **The bracket in (9.3).** It is unsubscripted, and (8.1) allows either:
   - (b−) a commutator [·,·] (factor i⁰);
   - (b+) i × anticommutator (factor i¹).

   The two brackets in (9.3) may differ, which gives 4 combinations. The graded sign is also unstated: for ad-valued forms α ∈ Ω^p, β ∈ Ω^q the natural graded commutator is α∧β − (−1)^{pq} β∧α. In the Ricci-like term pq = 12 (even). In the inner bracket of the second term pq = 24 (even); in the outer one pq = 0. So graded and ungraded agree for every bracket in (9.3).
2. **Φ¹ and Φ² are not unique** `[GU-recon]`, a claim we must check.
   - Under SO, Λ¹ ≅ Λ¹³ and Λ² ≅ Λ¹², and both of each pair sit in 𝔲(64,64) ≅ ⊕Λᵏ. So the invariant spaces [Λ¹ ⊗ 𝔲]^{Spin} and [Λ² ⊗ 𝔲]^{Spin} are expected to be **2-dimensional each** over the complex span. Candidates:
     - Φ¹ ∈ span{e^a ⊗ Γ_a, e^a ⊗ Γ_aΓ_*}
     - Φ² ∈ span{e^{ab} ⊗ Γ_{ab}, e^{ab} ⊗ Γ_{ab}Γ_*}

     with i-phases needed to land in 𝔲(64,64).
   - The draft's "{Φ_i}_{i=0}^{14}" indexing suggests one per degree, which contradicts this count. Which element (or combination) is meant is unresolved.
   - The real dimension of the invariant subspace inside 𝔲(64,64), as opposed to its complexification, must be computed per signature.
   - Branch set Φ¹ ∈ {Γ-type, Γ·Γ_*-type, general combination}, likewise for Φ².
3. **Normalization.** The draft says "normed" but gives no norm. The relative coefficient −½ in (9.3) assumes a normalization of Φ¹ and Φ² (as with g and Einstein's ½). Branch: each Φ normalized so that its contraction reproduces Riemannian Ric and S in the Levi-Civita case (the reading that makes "Einstein-like" literal), or unresolved.
4. **Hodge-star convention.** Unstated. Use the spec's pinned convention (α∧∗β = ⟨α,β⟩vol). Under another convention the result can differ by signs per degree; record that as a branch if it matters.
5. **The real form (3.27) is signature-dependent.** In our Mono model with A = phase·(product of timelike gammas):
   - AΓ_aA⁻¹ = (−1)^q Γ_a†. So the grade-1 elements Γ_a are A-skew (real coefficient) for q = 7 but need a factor i for q = 5.
   - (3.27) (q = 7) puts Λ¹ at real coefficient, consistent with our A for (7,7). For (9,5) the i-pattern of (3.27) must be recomputed, not copied.
   - The draft's footnote 3 itself asks for (3.27) to be checked. Test candidate: a direct membership check of each grade in our `adjoint.is_in_algebra`, for both signatures.
6. **The domain of ε.** Pointwise ε ∈ U(64,64) (from ℋ). Our tests use h with h†Ah = A (spec §4). The draft never uses geometric Spin elements as dressings, which is consistent with the spec's separation.

## The draft's stated properties (to test)

- (P1) **Degree:** Ω² → Ω¹³ `[GU-orig]` (9.2).
- (P2) **Real form:** the values stay in ad, i.e. 𝔲(64,64) `[GU-orig]` (9.2). Depends on branches 1 and 5.
- (P3) **Gauge covariance via dressing:** "rotates only the bundle valued portion … exactly compensates" (p. 41) `[GU-orig]`, stated qualitatively. Spec §5 test 3 makes it precise.
- (P4) **Weyl annihilation:** "the Weyl curvature tensor is annihilated" (p. 43) `[GU-orig]`. For undressed equivariant maps this holds automatically (spec §5).
- (P5) **The response is Einstein-like:** "preserves and mixes only the analogues of the Ricci and Scalar curvature components" (p. 43), with Ricci-like and Ricci-scalar-like labels and a −½ coefficient `[GU-orig]`. **No explicit numerical response is given.** The expected scalar and traceless-Ricci outputs are therefore `[GU-recon]` (branch 3): the "Einstein-like" reading is G_ab = Ric_ab − ½ S g_ab, with relative coefficient −½.
- (P6) The operator is **not the author's preferred one**. That one is "chosen for … Bianchi identity" and lost (footnote 10, §8.2) `[GU-orig]`. So a failure of (9.3) is a failure of the displayed candidate, not of "GU's Shiab".
