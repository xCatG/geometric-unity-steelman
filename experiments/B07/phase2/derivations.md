# B07 Phase 2: derivations H9–H14 and register additions

Plan: `docs/superpowers/plans/2026-10-16-b07-phase2.md` (rev 2, approved 2026-10-16). Phase 1: `experiments/B07/transcription.md` (reading V, H1–H8, readings register) and `experiments/B07/README.md`.

**Scope.** Everything below is under Phase 1's reading B07-V. It varies only the ϖ direction (δT = α), with ε and the metric fixed and the metric trace pairing. Unless a section says otherwise, it works on the **flat model**: B = d, ε = 1, constant coefficients, with Phase 1 H5 removing the dressing.

**Notation.**
- n = p + q, and η = diag(+1 × p, −1 × q).
- pair(x, y) = Tr(x∧y)/2^{n/2}. This is the wedge trace pairing, a positive multiple of Phase 1's Tr(x∧y).
- ⟨x, y⟩ = Tr(x∧∗y)/2^{n/2}. This is the metric pairing.
- X: Ω²(ad) → Ω^{n−1}(ad) is an algebraic (pointwise linear) map; ⊚ is one example. L = X∘d_B.
- e^k is the coframe, K = Σ k_i e^i, and c ranges over Clifford blades.
- C1 and C2 are as in Phase 1 H2 and H3.
- **Scope tags** (P1): *identity* = an exact statement, executed or derived; *hand* = derived here, not computed; *counterexample* = an exact witness.

**Graded cyclicity.** For ad-valued forms x, y of degrees |x|, |y|, Tr(x∧y) = (−1)^{|x||y|} Tr(y∧x). The trace is cyclic on the Clifford coefficients, and swapping the forms gives the sign. Tr commutes with d, and on compactly supported forms ∫Tr(dω) = 0. Every sign below comes from these two facts.

## H9 — the transpose and L† = d∘Xᵗ (identity, executed)

**Definition.** The wedge transpose Xᵗ: Ω¹(ad) → Ω^{n−2}(ad) is the pointwise map with pair(t, Xβ) = pair(Xᵗt, β) for all 1-forms t and 2-forms β. It exists and is unique because pair is nondegenerate between Ω^{n−2} and Ω² (`symmetric.wedge_transpose` builds it from the dual basis).

**L† = d∘Xᵗ.** Let α, T be compactly supported. By definition of Xᵗ, pointwise,

Tr(T∧X(dα)) = Tr(XᵗT∧dα).

Next, d(XᵗT∧α) = d(XᵗT)∧α + (−1)^{n−2} XᵗT∧dα. Integrating and dropping the boundary term gives ∫Tr(XᵗT∧dα) = (−1)^{n−1}∫Tr(d(XᵗT)∧α). Graded cyclicity for an (n−1)-form and a 1-form gives one more factor (−1)^{n−1}. The two signs cancel:

$$\int\mathrm{Tr}(T\wedge X d\alpha)=\int\mathrm{Tr}\big(\alpha\wedge d(X^{t}T)\big).$$

Phase 1 H2 defines L† by ∫Tr(T∧Lα) = ∫Tr(α∧L†T), so L† = d∘Xᵗ on the flat model. With B present, L† = d_B∘Xᵗ follows by the same steps under H11 hypotheses 3–4: the trace is compatible (Tr∘d_B = d∘Tr on the scalar top form), and boundary terms vanish. The graded Leibniz rule for the exterior covariant derivative d_B on ad-valued forms holds for any connection, so torsion is not used here. Torsion-freeness enters only in H11, where d_B is written as Σ_k e^k∧∇_k.

**The symbol of L† − L is −C1.** Let ω be an (n−2)-form. Then

pair(a, e^k∧ω) = Tr(a∧e^k∧ω)/2^{n/2} = −Tr(e^k∧a∧ω)/2^{n/2} = −pair(ω, e^k∧a).

The last step is graded cyclicity for the 2-form e^k∧a and the (n−2)-form ω, which has sign (−1)^{2(n−2)} = +1. Put ω = Xᵗt:

pair(a, e^k∧Xᵗt) = −pair(Xᵗt, e^k∧a) = −pair(t, X(e^k∧a)).

At ∂_k the symbol of L pairs to pair(a, X(e^k∧t)), and the symbol of L† pairs to pair(a, e^k∧Xᵗt). Their difference is

pair(a, σ_k(L† − L)t) = −pair(t, X(e^k∧a)) − pair(a, X(e^k∧t)) = −C1(k; t, a)/2^{n/2}.

So Phase 1's C1 is exactly the symbol of L† − L. The code checks this entry by entry at (3,1) (`test_transpose_symbol_is_minus_c1`, together with `test_wedge_transpose_is_the_transpose`).

## H10 — when L† is algebraic on curvature, and the symmetrized obstruction (identity on the flat model)

**The question.** Varying (9.4) yields the symmetrized operator L_sym = ½(L + L†) (Phase 1 B07-S). L = X∘d is "algebraic on curvature": it is an algebraic map applied to the linearized curvature dT. The question is whether L† = d∘Xᵗ has the same form, X♯∘d.

**Criterion (symbol consistency).** On constant coefficients, L† = Σ_k S_k∂_k, where S_k(t) = e^k∧Xᵗ(t). A factorization L† = X♯∘d requires X♯(e^k∧t) = S_k(t), that is, X♯(e^k∧e^j c) = e^k∧Xᵗ(e^j c). This defines X♯ consistently iff the two writings e^k∧(e^j c) = −e^j∧(e^k c) of the same 2-form give the same value, i.e.

e^k∧Xᵗ(e^j c) + e^j∧Xᵗ(e^k c) = 0 for all k, j and blades c.

The diagonal case k = j says e^k∧Xᵗ(e^k c) = 0, which is needed because e^k∧e^k = 0. The condition is an equality of (n−1)-forms. Pair it with an arbitrary 1-form a and use H9's identity with t = e^j c. It becomes the vanishing of the **symmetrized obstruction**

$$\mathrm{SO}(k,j;c,a)=\mathrm{pair}\big(e^jc,\,X(e^k\wedge a)\big)+\mathrm{pair}\big(e^kc,\,X(e^j\wedge a)\big)$$

for all k ≤ j, all blades c and all 1-forms a. Nondegeneracy of pair makes this equivalent. When SO = 0, X♯ is defined by the formula above and extended linearly, and L† = X♯∘d. Then L_sym = X_sym∘d with X_sym = ½(X + X♯). Implementation: `symmetric.sym_obstruction`, `symmetric.sharp`.

**Equivalent form: P kills exact forms.** Write P = L† = Σ_k S_k∂_k and take f a function and c a constant blade. Then

P(d(f c)) = Σ_{k,j} S_k(e^j c) ∂_k∂_j f.

Hessians ∂_k∂_j f are arbitrary symmetric matrices. So P kills every d(f c) iff S_k(e^j c) + S_j(e^k c) = 0 for k ≠ j and S_k(e^k c) = 0, which is exactly the symbol-consistency condition above. The condition is sufficient for P to factor through d; necessity follows from d² = 0. (The Chern–Simons control P = d itself kills exact forms, so first-order operators can.) This equivalence uses constant coefficients and d² = 0. It is **not** extended to curved d_B, where d_B² = [F_B, ·] ≠ 0 adds zeroth-order terms.

**C1 = 0 implies SO = 0, with X♯ = X.** Suppose C1 = 0, i.e. pair(t, X(e^k∧a)) = −pair(a, X(e^k∧t)) for all k, t, a. Then, using (e^k∧e^j)c + (e^j∧e^k)c = 0,

SO(k, j; c, a) = −pair(a, X(e^k∧e^j c)) − pair(a, X(e^j∧e^k c)) = −pair(a, X(e^k∧e^j c + e^j∧e^k c)) = 0.

Then S_k = σ_k(L†) = σ_k(L) = X(e^k∧·) by H9, so X♯ = X. Executed on the 3D Chern–Simons control (X = id on 2-forms of Cl(3,0), which has C1 = 0, SO = 0 and X♯ = X) and on E_OP at (3,1). The named CAA and CAC branches have SO ≠ 0 (`test_named_branch_does_not_factorize`, and the bounded witnesses in `run.py`).

## H11 — from the symbol to the operator, flat and curved (hand)

**Flat model.** With constant coefficients both L and L† are homogeneous first-order operators. They are determined by their symbols, and C1 = 0 says σ(L) = σ(L†) (H9). So C1 = 0 is exactly L = L†.

**Curved background.** Assume all four of the following:
1. The complete bundle map X is parallel for the induced connection on Λ²⊗ad and Λ^{n−1}⊗ad, acting on form and internal indices together: ∇^B X = 0.
2. The form connection is torsion-free.
3. The trace is compatible with the connection: d Tr(·) = Tr(∇·).
4. Boundary terms vanish (compact support).

Torsion-freeness gives d_B = Σ_k e^k∧∇_k on forms. Parallelism gives Xᵗ∇_k = ∇_kXᵗ, since the transpose of a parallel map is parallel by (3). So L = X∘d_B = Σ_k X(e^k∧∇_k ·) and L† = d_B∘Xᵗ = Σ_k e^k∧Xᵗ(∇_k ·). Both are first order, with no zeroth-order part beyond what ∇_k carries. Their difference is the pointwise operator identity of the flat case applied to ∇_kT. No second covariant derivatives are commuted, so curvature does not enter and there is no remainder. Hence C1 = 0 at a point, together with (1)–(4), gives L = L†.

**What (1) requires.** Write ∇X = dX + ρ_out(ω)X − Xρ_in(ω). The form and internal actions are taken together, and ω is the connection form.
- **Same Spin connection.** If the connections on both bundles (form indices and internal indices) are induced from **one Spin connection ω**, then ρ_out(ω)X − Xρ_in(ω) = 0 for every Spin intertwiner X. That is exactly the equation the universal search solves (H12). So every constant intertwiner is parallel, curved or not, and H11 applies to every vector of the universal C1 kernel.
- **Independent internal connection or variable coefficients.** If the internal connection is independent, as with a general u(A)-valued B, which need not lie in the Spin image, then ∇^B X = 0 is an extra condition and Spin-equivariance does not imply it. The same holds for coefficients that vary in space.

ε fixed under the variation is not enough for (1). Covariantly closed Φ is not the same as parallel Φ.

**Not covered.** Coefficient derivatives (non-parallel Φ, or Φ depending on ϖ: B07-X). Curved d_B in H10's exact-form form.

## H12 — the unreduced Spin-equivariant space (identity, executed in 4D)

**Real basis.** ad = u(A) ⊂ Cl(p,q), with A the Dirac pairing (B02, `gu.clifford.dirac_pairing`). For each blade G_c there is a phase i^{ph(c)} with i^{ph(c)}G_c ∈ u(A). This is B02's `_in_u_A` convention, computed by `universal.phases` from the membership test. The basis is e^I ⊗ i^{ph(c)}G_c, with I a form multi-index. Every u(A)-valued form is a **real** combination of it.

**Generators.** Spin(p,q) acts on Ω^k(Cl) through J_{ab} = ½G_aG_b (a < b), on form indices by the vector representation and on the coefficient by the commutator. This is `gu.shiab.generator_action`, the same simultaneous action as B02. J_{ab} maps a basis element to a rational combination of basis elements. The phase ratios i^{ph(c)−ph(c′)} that appear are real, because the Spin action preserves u(A). So ρ(J_{ab}) is a rational matrix in the phased basis (`universal.rho`).

**Search space.** Let V_in = Ω²(u(A)) and V_out = Ω^{n−1}(u(A)). The search space is every real-linear map M with ρ_out(J)M = Mρ_in(J) for all generators J. The equations are rational. So the real solution space is the rational nullspace tensored with ℝ, and its real dimension equals the complex dimension of the complexified equivariant Hom space (scalar extension). A map preserves u(A)-valued forms iff its matrix in the phased basis is real. The Spin action preserves form degree and Clifford grade, so the space splits into 25 grade blocks (j → l) (`universal.equivariant_block`, solved exactly with python-flint `fmpq_mat`).

**Character count** (fixed before computing, P3). so(4, ℂ) = sl₂ × sl₂, with Λ⁰ = Λ⁴ = (0,0), Λ¹ = Λ³ = (½,½) and Λ² = (1,0) ⊕ (0,1). The Clifford grade-j factor carries Λʲ. The dimension of block (j → l) is the multiplicity pairing between Λ²⊗Λʲ and Λ³⊗Λˡ, using these tensor products:
- Λ²⊗Λ⁰ = Λ²⊗Λ⁴ = (1,0) ⊕ (0,1);
- Λ²⊗Λ¹ = Λ²⊗Λ³ = (3/2,½) ⊕ (½,3/2) ⊕ 2(½,½);
- Λ²⊗Λ² = (2,0) ⊕ (0,2) ⊕ (1,0) ⊕ (0,1) ⊕ 2(1,1) ⊕ 2(0,0);
- Λ³⊗Λ⁰ = Λ³⊗Λ⁴ = (½,½);
- Λ³⊗Λ¹ = Λ³⊗Λ³ = (1,1) ⊕ (1,0) ⊕ (0,1) ⊕ (0,0);
- Λ³⊗Λ² = (3/2,½) ⊕ (½,3/2) ⊕ 2(½,½).

| j \ l | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | 0 | 2 | 0 | 2 | 0 |
| 1 | 2 | 0 | 6 | 0 | 2 |
| 2 | 0 | 6 | 0 | 6 | 0 |
| 3 | 2 | 0 | 6 | 0 | 2 |
| 4 | 0 | 2 | 0 | 2 | 0 |

The total is **40**. The two (j, l) = (2, 1) and (2, 3) entries each include the (1,0) ⊕ (0,1) summand of (1,0)⊗(1,0) and (0,1)⊗(0,1). Parity separates the zero entries: Λ²⊗Λʲ has integral weights iff j is even, and Λ³⊗Λˡ has integral weights iff l is odd. `test_equivariant_dimension_matches_characters` compares this table, block by block, with the computed space at (3,1) and (1,3).

**What the space contains.**
- B02's 20 building blocks across bracket modes (first[m₀](Φ¹) for m₀ ∈ {C, A} and Φ¹ ∈ {F, F′}; second[m₁m₂](Φ¹, Φ²) for the four mode pairs and Φ¹, Φ² ∈ {F, F′} × {B, B′}). They lie in it (`test_blocks_lie_in_the_universal_span`) and span 16 dimensions: four exact zero relations, one of them checked by hand in `test_block_span_has_four_zero_relations`.
- More generally, each undressed (9.3)/(8.1) Shiab with real invariant Φ, and every **real mixed-mode sum** (B07-M), is a real, Spin-equivariant, u(A)-preserving algebraic map. So it lies in the space by the Hom-space argument itself, not only because the 20 blocks were tested.

**What it does not contain: B07-G.** Take the raw ordinary-product reading at (3,1), with Φ¹ = F, Φ² = 0 and β = e^{01}Γ₀ ∈ Ω²(u(A)). The first term gives F∧∗β = e^{023} Id − e^{123} Γ₀₁. The real identity component lies outside u(A): Id needs phase 1. So this map does not preserve u(A) and is not in the real Hom space (finding from Codex's review of rev 0, confirmed by Grok's review of rev 1). Likewise, the expansion ab = (C − iA)/2 has complex coefficients, which do not lie in the real span. B07-G stays deferred until a specific reality-preserving completion is fixed and checked.

**Equivariance group.** The space is Spin(p,q)-equivariant, not equivariant under Pin or under the full U(A) adjoint action (neither is the Shiab family). The pairing is not varied (B07-Q). Both reviews of `argon_b7.md` note that grade-weighted pairings are Spin-invariant but not ad-invariant.

## H13 — the gates, the curvature response and the Einstein condition (identity, executed)

**Gates are linear.** Over a span with basis X₁ … X_N, C1, SO and C2 are linear in the coefficient vector. So each gate is an exact kernel (`variation.kernel`). Kernel dimensions are reported as **operator** dimensions. The 20 blocks are first reduced to an independent subset (`run.independent_blocks`), because their four zero relations would otherwise inflate the coefficient kernels.

**The response space is four-dimensional (4D).** The response ∗X(ξ(R)) of an equivariant X to an algebraic curvature tensor R is an equivariant linear map from algebraic curvature to Ω¹(Cl).
- In 4D, algebraic curvature is Weyl (2,0) ⊕ (0,2), traceless Ricci (1,1) and scalar (0,0): dimensions 10 + 9 + 1 = 20.
- A 1-form with a grade-k Clifford coefficient carries Λ¹⊗Λᵏ:
  - (½,½) for k = 0, 4;
  - (1,1) ⊕ (1,0) ⊕ (0,1) ⊕ (0,0) for k = 1, 3;
  - (3/2,½) ⊕ (½,3/2) ⊕ 2(½,½) for k = 2.
- So (1,1) and (0,0) occur only for k ∈ {1, 3}, each once: the F channel (grade 1) and the F′ channel (grade 3, the volume dual). (2,0) ⊕ (0,2) never occurs.

By Schur, every response is

∗X(ξ(R)) = a E_F(Ric) + b E_{F′}(Ric) + c S E_F(g) + d S E_{F′}(g),

with E_F(H) = Σ e^a H_a{}^b G_b and E_{F′}(H) = Σ e^a H_a{}^b G_b·C, with C the chirality element and B02's phase, (B02's `embed_tensor(·, 1, 0)` and `(·, 0, 1)`). This grade count is the argument; Weyl absence alone would not bound the span. `gates.response` fits (a, b, c, d) exactly on all 55 Kulkarni–Nomizu generators, which span the 20-dimensional curvature space (rank 20, B02). It raises if any generator's response leaves the span, so the computation checks itself.

**Einstein condition.** B02's κ = ½ with a nonzero Ricci term means that the response is a nonzero multiple of the Einstein tensor in each channel: a E_F(Ric − ½Sg) + b E_{F′}(Ric − ½Sg) with (a, b) ≠ 0. Equivalently 2c + a = 0, 2d + b = 0 and (a, b) ≠ 0: a linear condition plus a nonvanishing condition, stated without division (`gates.is_einstein`). The division-free form matters: with a = 2⁶⁰ + 1, a float a/2 rounds and gives a false positive (Codex's review of rev 0; `test_exactness_helpers_reject_floats_and_decide_exactly`). Within a kernel K, the reported Einstein dimension is the rank of (a, b) on the subspace of K where 2c + a = 2d + b = 0. This is the dimension of the response image, not the dimension of the locus of nonzero operators.

**Order T² in general form.** Varying ⅓∫Tr(T∧X b(T,T)) gives ⅓Tr(α∧X b(T,T)) + ⅓Tr(T∧X(b(α,T) + b(T,α))). Subtracting the target's Tr(α∧X(T∧T)) gives, pointwise,

$$C2(\alpha;T)=\tfrac13\mathrm{Tr}\big(\alpha\wedge X b(T,T)\big)+\tfrac13\mathrm{Tr}\big(T\wedge X(b(\alpha,T)+b(T,\alpha))\big)-\mathrm{Tr}\big(\alpha\wedge X(T\wedge T)\big).$$

- **N1 and N2.** b is symmetric on 1-forms, with b(T,T) = T∧T and 2T∧T respectively. This is Phase 1 H3.
- **N0.** b is the ungraded commutator of the form-valued product, b(x, y) = x∧y − y∧x. On the diagonal b(T,T) = 0. Its symmetric cross term is b(α,T) + b(T,α) = (α∧T − T∧α) + (T∧α − α∧T) = 0. So C2 = −Tr(α∧X(T∧T)). The antisymmetric part of b need not vanish off the diagonal, and C2 never uses it.

**Rev 1.1 of Phase 1 is superseded on one point.** Phase 1 recorded N0 but did not execute it. In Phase 2 C2 decides the verdict for operators that pass C1, so N0 is computed alongside N1 and N2 (user decision, 2026-10-16). C2 is polarized (T = tᵢ + tⱼ minus the diagonal parts) into a trilinear form, whose vanishing on basis triples is equivalent (`gates.c2_residual`).

## H14 — the second-order Lagrangian (9.11)–(9.15) (identity, executed by exact Fourier modes)

**Setup.** I₂ = ⟨Υ, Υ⟩ with Υ = X(F_A) + κ₁∗T (9.7). The metric trace pairing ⟨x, y⟩ = ∫Tr(x∧∗y) is symmetric on forms of equal degree. It is indefinite, so ‖·‖² is not a norm. ε and the metric are fixed and δT = δA = α, so δΥ = X d_Aα + κ₁∗α.

**Exact half-gradient.** ½δI₂ = ⟨X d_Aα, Υ⟩ + κ₁⟨∗α, Υ⟩ = ⟨α, d_A^*X^*Υ⟩ + κ₁⟨α, ∗^†Υ⟩. Here X^* is the metric adjoint of X, d_A^* is the formal adjoint of d_A, and ∗^†: Ω^{n−1} → Ω¹ is the metric adjoint of ∗. Expanding:

$$d_A^*X^*XF_A+\kappa_1 d_A^*X^*(*T)+\kappa_1*^\dagger XF_A+\kappa_1^2*^\dagger{*T}.$$

**The adjoint of ∗.** On Ω^k, ∗∗ = (−1)^{k(n−k)+q}, and ∗ is an anti-isometry up to sign: g(∗a, ∗b) = (−1)^q g(a, b). Take a ∈ Ω^k and u = ∗w ∈ Ω^{n−k}. Then

⟨∗a, u⟩ = (−1)^q g(a, w), while ⟨a, ∗u⟩ = g(a, ∗∗w) = (−1)^{k(n−k)+q} g(a, w).

So **∗^† = (−1)^{k(n−k)}∗** from Ω^{n−k} to Ω^k. For k = 1 this is (−1)^{n−1}∗. On Ω¹, ∗^†∗ = (−1)^{n−1}(−1)^{(n−1)+q} = **(−1)^q**.

For the other standard convention ∗′ = (−1)^{deg}∗, with its own pairing ⟨x, y⟩′ = ∫Tr(x∧∗′y) = (−1)^{deg y}⟨x, y⟩, the same computation gives ∗′^† = (−1)^{k(n−k)}∗′ and ∗′^†∗′ = (−1)^{n+q} on Ω¹. For even n, the case here (n = 4, 14), this is again (−1)^q. `test_star_adjoint_and_mass_signs` checks both conventions, every signature and every basis pair at n = 4 and 14.

**Against (9.12)–(9.13)** (even n, both conventions):
1. **Term 1.** d_A^*X^*XF_A **matches**.
2. **Term 2.** (9.13) prints κ₁d_A^*X^*T. X^* maps Ω^{n−1} → Ω², so X^*T is ill-typed; the ∗ is **missing**.
3. **Term 3.** The derived term is κ₁∗^†XF_A = −κ₁∗XF_A. (9.13) prints +κ₁∗XF_A: the **wrong sign** in every signature, under both conventions.
4. **Term 4.** The derived term is κ₁²∗^†∗T = (−1)^q κ₁²T. (9.13) prints +κ₁²T, which is **right iff q is even**.
5. **(9.12).** Its Id stands where ∗^† is needed.

Phase 1 H8 found term 4 wrong at its four signatures, (3,1), (1,3), (7,7) and (9,5). All of those have odd q, so H8 is the odd-q case of this formula.

**Codifferential.** For v ∈ Ω^{m−1} and u ∈ Ω^m, compactly supported,

⟨dv, u⟩ = ∫Tr(dv∧∗u) = (−1)^m∫Tr(v∧d∗u) = ⟨v, (−1)^m∗^{−1}d∗u⟩.

The middle step drops ∫Tr(d(v∧∗u)) = 0 and uses d(v∧∗u) = dv∧∗u + (−1)^{m−1}v∧d∗u. So δu = (−1)^m∗^{−1}d∗u under either convention, using the pairing's own ∗. On e^{ik·x} its symbol is u ↦ (−1)^m∗^{−1}(iK∧∗u).

**Exact Fourier test.** On a flat torus take T = t e^{ik·x} and α = a e^{−ik·x}. The variation of the quadratic part of I₂ is computed from the **action alone**, with no adjoints:

B(a, t) = 2⟨X(−iK∧a) + κ₁∗a, X(iK∧t) + κ₁∗t⟩.

It is compared, order by order in κ₁, with ⟨a, 2P t⟩, where P is the half-gradient operator above. The 2 is the one in δ⟨Υ, Υ⟩ = 2⟨δΥ, Υ⟩, and `fourier_terms` puts it on both sides. P is assembled from:
- the codifferential symbol;
- X^*, built from the diagonal ±1 Gram matrix of basis forms, which `second_order.adjoint` asserts is diagonal;
- ∗^{−1}, from the computed square of ∗ on each basis element;
- ∗^†.

The κ₁⁰, κ₁¹ and κ₁² parts are **homogeneous** in k of degrees 2, 1 and 0. The wavevectors k ∈ {e_i} ∪ {e_i + e_j} (n(n+1)/2 of them) determine homogeneous quadratics, with exact evaluation rank 10/10 in 4D, and linears (4/4). They would not determine a general inhomogeneous polynomial of degree ≤ 2: 1 − Σk_i + Σ_{i<j}k_ik_j vanishes at all of them. Homogeneity is what makes the comparison complete. Every printed term is checked to be non-vacuous, because a zero operator would match anything.

**(9.14), the Yang–Mills reading.**
- **The shortcut.** X^*X ∝ Id would make term 1 ordinary Yang–Mills. It is only **sufficient**:
  - In 4D a topological term λ∗ in X^*X drops out of the field equation, since δ(∗(iK∧a)) = ±∗^{−1}(iK∧iK∧a) = 0 by K∧K = 0. This is an off-shell identity of symbols, not the Bianchi identity.
  - A nonzero scalar multiple of Id is impossible anyway: X maps a 96-dimensional space to a 64-dimensional one (6·16 → 4·16), so X^*X has rank at most 64.
- **The criterion.** The kinetic symbol a ↦ δX^*X(iK∧a) is one common scalar multiple λ of the ordinary YM symbol a ↦ δ(iK∧a) for every k (`second_order.ym_symbol`). Both are homogeneous quadratics in k, so a shared ratio on the test wavevectors holds for all k. With λ ≠ 0, this is **necessary and sufficient** for the flat constant-coefficient kinetic operator to be a multiple of ordinary YM.
- **What the criterion does not show.** It does not establish equal actions, which may differ by the topological density, nor equivalence of curved or nonlinear equations.
- **Packaging.** (9.14)'s generalized packaging D^* = d_A^*X^*X is a different statement from ordinary YM. The README keeps the two apart.

`xstar_x` (the shortcut) and `ym_symbol` (the criterion) are both recorded. Only the criterion supports a conclusion. Controls: the 3D map X = id gives ratio 1 with no mismatch.

## Register additions

These rows extend Phase 1's readings register (`experiments/B07/transcription.md`). Unlisted Phase 1 rows are unchanged.

| ID | Reading | Class | Can change | Executed here |
|---|---|---|---|---|
| B07-U | The unreduced space: every real Spin(p,q)-equivariant u(A)-preserving algebraic map Ω²(u(A)) → Ω^{n−1}(u(A)) (H12) | `[ext]` search space; contains every undressed real (9.3)/(8.1) Shiab and real mixed-mode sum | C1, SO, C2, the response | **yes, in 4D** at (3,1) and (1,3) (dimension 40). The 14D space (≈ 3.4 × 10¹¹ matrix entries) is out of scope; 14D gets bounded witnesses only |
| B07-M | Sums mixing bracket modes (Phase 1 row) | untested in Phase 1 | C1, C2 | **now yes, in 4D**: the 20 blocks across modes (rank 16) and B07-U contain them |
| B07-S | The symmetrized operator ½(L + L†) (Phase 1 row) | different model | C1 | **now analysed** (H10): L† = X♯∘d iff SO = 0, and L_sym = ½(X + X♯)∘d |
| B07-N0 | [T, T] as the ungraded commutator of the form-valued product (Phase 1 row) | source ambiguity | C2 only | **now yes**, at order T², with N1 and N2 (H13). This supersedes Phase 1's record-only decision |
| B07-G | Bracketed products as ordinary products (Phase 1 row) | different completion | C1, C2 | **no, and not in B07-U** (H12 counterexample); deferred until a reality-preserving completion is fixed |
| B07-Q | The trace/reality/pairing convention (Phase 1 row) | convention | C1, C2, H8/H14 signs | unchanged: pairing fixed, not varied. Grade-weighted pairings are Spin- but not ad-invariant |
| B07-P2 | Palatini/BF-type actions with independent fields, or one-leg variations (vary one slot, or ε) | `[ext]` model change | everything | no |
| B07-Bi | A conservation/Bianchi gate on the field equations | undefined until the identity, the fields and the background are specified | — | no |
| B07-YM | (9.14) read as ordinary Yang–Mills | reading of the claim | (9.14) | **yes** (H14): principal-symbol criterion, with X*X ∝ Id recorded as the shortcut |
