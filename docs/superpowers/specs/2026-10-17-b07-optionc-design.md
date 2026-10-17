# B07 option C: the T-sector of I₂ and the frozen-metric connection reading. Pre-registration design

**Status:** rev 3. Nothing has been run. Codex's and the reviewers' probes used sizes, timings, block support and toy maps only. No Q1–Q4 rank, root, inertia or classification of a named operator has been computed. The outcome classes and their readings are fixed **before** any experiment code exists. The implementation plan, with smoke-tested code, comes after this design is approved.

**History:**
- rev 0 (`c6564f2`), then Codex's review (11 findings);
- rev 1 (`a85c1a4`), then Grok's co-revision (5 corrections);
- rev 2 (`7be737c`), then a three-way review:
  - Codex: accept with fixes, 3 blocking findings;
  - Grok: accept with fixes, 1 blocking;
  - a fresh Claude subagent: revise, 2 blocking.
- rev 3, this revision. It folds all three reviews. The main change comes from the Claude review: the second-order matrix M is the Gram matrix of the draft's own square first-order symbol Υ_lin = U(k), so Q3 and Q4 are rebuilt around U.

**Inputs:**
- Phase 2 H9/H10 (L and L†, C1) and H14 (`experiments/B07/phase2/derivations.md`, `second_order.py`). H14 supplies the exact Fourier variation of the quadratic part of I₂, its κ₁⁰/κ₁¹/κ₁² split, ∗^† = (−1)^{k(n−k)}∗, ∗^†∗ = (−1)^q on Ω¹, and the ym_symbol entry ratios.
- Phase 2 H12/H13 (`universal.py`): the real basis of u(A), and the grade count of invariants.
- `phase2/result.json`: the recorded C1 and response data.
- Escape E1/E2 (`experiments/B07/escape/`).
- B02's stated limits (`experiments/B02/README.md:134,152`).
- Grok's fact-check of another model's (Argon's) proposal. The rejected parts are in §6.

## 1. What is new, and what is not

H14 already compared the quadratic action's variation with (9.12)–(9.13), recorded its κ orders, and decided ordinary YM at the principal-symbol level. **Option C does not redo any of that.** It asks four new questions:

- **Q1:** Is the κ₁¹ cross term zero in the field equation?
- **Q2:** What does each operator do on pointwise Lorentz-valued curvature values that are not algebraic?
- **Q3:** What are the dispersion roots and kernel structure of the linearized first-order system Υ_lin = 0, and of the field equation?
- **Q4:** What sign data do the named forms take on those kernels?

## 2. Model (the reading being tested)

**Background and method.**
- A 4D point, at signatures (3,1) and (1,3).
- The background is flat, B = d, and **ε = 1**. The metric is frozen and δT = δA (Phase 2 reading V).
- Coefficients are constant, and arithmetic is exact over Q(i) and its declared extensions. No floating-point or modular result becomes an outcome.

**Operators.**
- CCC, CAA and CAC are `variation.branch_map(name, p, q)` for the three `variation.BRANCHES` keys.
- E_OP is `phase2/run.py:e_op(p, q)`, the callable built from the spec tuple `E_OP`.
- All four are undressed.

**Real field basis.**
- T ∈ Ω¹(u(A)), with real fiber dimension 4 × 16 = 64.
- The basis is the **phased** one, e^a ⊗ i^{ph(C)}Γ_C, with ph from `universal.phases`, `to_phased` and `from_phased`. (`variation.one_forms` is the unphased basis.)
- With Π the diagonal phase matrix, the bilinear matrices are M = Πᵀ M_raw Π.
- Fourier coefficients satisfy t(−k) = conj t(k). They do not form 128 independent fields.

**Pairing, Hessian and the first-order symbol.**
- The pinned pairing is ⟨x, y⟩ = Tr(x∧∗y)/2^{n/2}, with Tr/2^{n/2} the normalized trace.
- **The first-order symbol.** U(k) = X∘(iK∧·) + κ₁∗ maps Ω¹(u(A)) → Ω³(u(A)). It is the Fourier symbol of the draft's linearized Υ = X(dT) + κ₁∗T (9.7). It is a **square** 64 × 64 matrix, linear in k.
  - In the phased basis, U(k) = ∗(iN(k) + κ₁), where N(k) = ∗⁻¹∘X∘(K∧·) is a **rational** 64 × 64 matrix, linear in k. Rationality is checked: X preserves u(A), and K and ∗ are real.
- **M is H14's first-variation (Hessian) matrix:**
  - M(k; κ₁) = S₀(k) + κ₁S₁(k) + κ₁²S₂, the κ-parts of B(a, t) = 2⟨X(−iK∧a) + κ₁∗a, X(iK∧t) + κ₁∗t⟩;
  - S₂ = 2(−1)^q G₁, with G₁ the one-form Gram matrix;
  - the half-gradient operator is P = ½G₁⁻¹M, whose mass term is (−1)^qκ₁² Id;
  - every reported number names which object (M, P, U or N) it refers to.
- **Gram structure.** M(k) = 2U(−k)ᵀG₃U(k), with G₃ the diagonal ±1 Gram matrix on 3-forms (`second_order.adjoint` asserts that it is diagonal). Consequences:
  - det M = det(2G₃)·|det U|² on real k;
  - **ker U(k) ⊆ ker M(k)**: the solutions of the linearized Υ = 0 are a subset of the field-equation solutions;
  - the radical of G₃ on im U(k) measures the gap between ker U and ker M.

**Prime convention.**
- The primary model is H14's **fixed-X** policy: X is held fixed while the external star and its pairing change.
- At n = 4 this gives M′(k; κ₁) = −M(k; −κ₁), which is asserted as a test. So S₀ and S₂ change sign and S₁ does not.
- Rebuilding X with the prime star is a separately named reading. It is not run.

**Scaling.**
- For real κ₁ ≠ 0, M(k; κ₁) = κ₁²M(k/κ₁; 1).
- For κ₁ < 0, M(k; κ₁) = κ₁²M(k/|κ₁|; 1)ᵀ. The zero sets coincide and the kernels are complex-conjugated, so no separate run is needed.
- κ₁ = 1 is used. κ₁ = 0 is reported separately.

**Scope.**
- **This is the R2 reading at linear order, and only that.** With B and ε fixed, T = A − B is the connection perturbation, not an extra field. Metric fluctuations are not in the model (O0).
- **Excluded explicitly**, by restriction, with no bearing on Phase 2's (9.4) result:
  - [T, T] and every cubic or quartic term;
  - curved backgrounds;
  - ε or the metric varying;
  - dressings ε ≠ 1;
  - 14D.

## 3. Controls and stop policy

**Stop policy.**
- **Hard gates.** Every algebraic, normalization, reconstruction, backend, Fourier-reality and real-u(A)-closure control at (3,1) and (1,3) is a hard gate. If one fails, the affected run stops and is recorded as `failed_control`, never as an outcome.
- **Exactly two declared exceptions:**
  - **(a)** If control 5 (covariance) fails, the run sets `covariance_verified=false`. Only the explicitly labelled ray diagnostics of Q3 may continue.
  - **(b)** If real closure fails at the auxiliary signatures (2,2) or (4,0), the run selects the complexified-control branch of control 8 and records `real_closure=false`. It never alters X.
- **Runtime exhaustion** is recorded as `partial`. It is neither a failed control nor an outcome, and it is written from checkpointed work.

**Controls.**

1. **Fourier symmetry and reality.**
   - M(k) = M(−k)ᵀ.
   - In the phased basis, conj M(k) = M(−k), so M(k) is Hermitian for real k.
   - S₁(k)ᵀ = −S₁(k), with S₁ purely imaginary.
   - N(k) is rational.
2. **Homogeneous reconstruction.**
   - S₀ is determined from k ∈ {e_i} ∪ {e_i + e_j}, S₁ from {e_i}, and S₂ and N(0) = 0 at k = 0.
   - Each is checked at exact wavevectors outside its determining set.
3. **Direct small-action control.**
   - **What is fixed.** The operator, the basis pairs, κ₁ and the covectors are named in the plan. They include at least one pair with a nonzero Hessian entry, and a toy map that exercises the odd (S₁) coefficient.
   - **The check.** The Hessian entries are computed from the action ⟨X(dT) + κ₁∗T, ·⟩ by polarization, without calling `fourier_terms`. S₁ is also checked against the Q1 closed form.
4. **Conventions and Gram structure.**
   - S₂ = 2(−1)^q G₁.
   - M′(k; κ₁) = −M(k; −κ₁).
   - M(k) = 2U(−k)ᵀG₃U(k), entrywise at every determining wavevector.
   - det M on each ray equals det(2G₃)·u(ω)·conj u(ω), where u = det U is computed independently.
   - On ker U(ω₀) at a real root, the derivative form V^†M′(ω₀)V restricts to 0.
5. **Lorentz covariance.**
   - **Generators.** For each J_ab = ½Γ_aΓ_b (a < b), let ρ(J) = ⊕_grades `universal.rho(p, q, 1, g, ph)`, real on the phased one-form basis. Let ρ₃(J) be the same on 3-forms, and Λ_J the action on covectors (as in `gu.shiab.generator_action`).
   - **Equations.** ρ(J)ᵀS(k) + S(k)ρ(J) + (d/ds)S(k + sΛ_Jk)|₀ = 0 for S ∈ {S₀, S₁, S₂}. The analogous intertwining equation holds for U(k), with ρ₃ on the output.
   - **Trace condition.** tr ρ(J) = tr ρ₃(J) = 0, so det ρ = 1 on the identity component.
   - **What it buys.** If control 5 passes, then det U(k) = g(k²) and det M(k) = F(k²) = det(2G₃)·g², and the orbit reduction of Q3 holds.
6. **Q2 controls.**
   - **Projectors.** P₁₅ = (I − τ)/2, P₁ = Alt and P₂₀ = (I + τ)/2 − Alt. They are idempotent, mutually annihilating, sum to I, have dimensions 15/1/20 respectively, and are equivariant.
   - **Algebraic-part responses.** On the 20-dimensional algebraic part, `phase2/gates.py:response(X, p, q)` reproduces the response vectors already recorded for each operator:
     - CCC, CAA and CAC as in `escape/result.json` and B02;
     - E_OP as `phase2/result.json` `e_op_response`, which is 2E_F(Ric) − S·E_F(g).
     A mismatch with the recorded vector is a stop.
   - **Hand ξ entry.** One elementary off-algebraic ξ entry is checked against the hand formula.
   - **Schur predictions (controls).** For every operator:
     - on the 1-part, ∗X∘ξ ∈ span{E_F(g), E_F′(g)} ⊂ ∗𝓔 (rank ≤ 1, image mod 𝓔 = 0);
     - on the 15-part, the image lies in 𝓔 ⊕ 𝓔ᵃ.
   - **CCC inner term.** It is 0 on the 20-part and on the 1-part, since both are pair-symmetric (B02 README:134).
7. **Spectral backend controls (toys with pinned answers, all pinned in the plan before any named operator is run):**
   - scalar massless and massive wave operators;
   - a small Hermitian polynomial with a known repeated root and a known Jordan chain;
   - a singular-leading-coefficient matrix;
   - a small Gram-of-square-symbol toy, U = [[1, iω], [iω, −1]] with G = I and with G = diag(1, −1). These exercise, respectively, the forced non-semisimple root and the neutral derivative form.
   - **The 3D toy.** X = id at signature (2,1), i.e. ‖dT + κ∗T‖². This is Maxwell–Chern–Simons plus mass, not Proca, and it is itself a Gram of a square symbol. Its determinant is pinned in the plan, including the factor 2. Until that pin exists, it is not a stop condition.
8. **(2,2) and (4,0): convention controls only.** At these signatures only the following run:
   - `second_order.star_adjoint_sign` and `mass_sign`;
   - S₂ = 2(−1)^qG₁;
   - the prime identity;
   - homogeneous reconstruction;
   - the backend toys.

   **Closure.** u(A)-closure is checked and reported as a fact. The grade-1 phases differ there, so F is not u(A)-valued with the documented Dirac adjoint. If closure fails (exception (b)), control 1 is reduced to M(k) = M(−k)ᵀ over Q(i). Conjugation, Hermiticity and a real-field reading are not asserted, and nothing from Q1–Q4 runs at these signatures. No mass or stability reading is attached at these signatures either way.
9. **Pre-decided facts, recorded as controls rather than outcomes.**
   - **κ₁ ≠ 0.** det M(0) = det(2(−1)^qκ₁²G₁) ≠ 0. So:
     - the null ray must give det M ≡ det M(0);
     - no root has ω² = 0;
     - det M is never identically zero on a ray.
   - **κ₁ = 0.** det S₀(k) ≡ 0, with nullity ≥ 16 for k ≠ 0 (the exact directions {k⊗λ}).
   - **Q1 for E_OP.** S₁ ≢ 0 is forced: E_OP has C1 = 0 at both signatures (`phase2/result.json` `e_op_c1_nonzero`), and C1 = S₁ = 0 would force X = 0 (Q1 closed form).

   Any violation is a failed control.

## 4. Pre-registered outcome classes

A result outside the listed outcomes is reported as "unanticipated", with no reading.

### O0. Einstein–Hilbert term (closed by construction)

No outcome of Q1–Q4 can exhibit an Einstein–Hilbert term, because the metric is frozen and every term is quadratic. S₂ is a mass term for T. An EH claim needs a separately specified enlarged model and an exhibited density that is linear in curvature. Neither is part of option C. Nothing below is read as gravity, Palatini recovery or Newton's constant.

### Q1. The κ₁¹ cross term

**Closed form.**
- S₁(k)(a, t) = 2(−1)^{q+1} i [pair(t, X(K∧a)) − pair(a, X(K∧t))].
- So S₁ ≡ 0 ⟺ L† = −L (H9).
- Phase 2's C1 is the symmetric companion of this expression, and C1 = S₁ = 0 forces X = 0. So E_OP's S₁ ≢ 0 is a control (control 9).
- **Q1 is open for CCC, CAA and CAC only.** These are named operators outside the C1 kernel.

**Test.** S₁(e_i) = 0 for the four basis covectors?

**Outcomes.**
- **(1a) S₁ ≡ 0.** The cross term contributes nothing to the quadratic field equation, so it is a boundary term in this model. If the repaired κ₁ term 2 and the derived term 3 are each nonzero for this operator, they cancel in the sum. That both are nonzero is not assumed beforehand.
- **(1b) S₁ ≢ 0.** Record its rank at each e_i (for M), its support on the grade blocks (Q3), and which Clifford-grade components it couples.
  - Reading: I₂ contains a first-order quadratic term in T that contributes to the field equation.
  - The reading is descriptive only. The term is not named EH, Palatini or Chern–Simons.

**Sign (pinned, fixed-X).** 2κ₁⟨X(dT), ∗T⟩ = [2κ₁(−1)^q/2^{n/2}] Tr(T∧X(dT)). Here Tr is the un-normalized matrix trace, using ∗∗ = (−1)^{q+1} on Ω¹ and graded cyclicity for degrees 3 and 1. The factor 2^{n/2} is not applied twice.

### Q2. Pointwise Lorentz-valued curvature that is not algebraic

**Domain.**
- **Values.** Off-shell **pointwise curvature values** F = ξ(R), with ξ(R) = ½Σ_{a<b, c<d} R_abcd η_cη_d e^{ab} ⊗ Γ_cΓ_d. Here R ∈ Λ²⊗Λ² (36 dimensions) carries no further symmetry, and is supplied in `gu.shiab.xi`'s n⁴ slot layout (read only at a < b, c < d).
- **Uniqueness.** The formula needs no pair symmetry. Raising a different pair, or transposing slots, would be a different convention and is not run.
- **Split.** 36 = 20 ⊕ 1 ⊕ 15 (algebraic, totally antisymmetric, pair-antisymmetric). The 1 and 15 parts are **non-algebraic, torsion-sensitive components**. They neither exhaust nor measure torsion.
- **Grade.** The GU field T has all Clifford grades. Only the grade-2 (Lorentz) part of F is tested here.
- **Not the Q3 domain.** A single Fourier curvature iK∧T satisfies K∧F = 0, and its Lorentz-valued image has dimension 18 for k ≠ 0. If Q2 is later related to Q3, that condition is imposed separately.

**Fixed output subspaces.**
- 𝓔 = ∗⁻¹{E_F(H) + E_F′(K) : H, K symmetric}. It is 20-dimensional and holds symmetric-tensor responses, B02's value space.
- 𝓔ᵃ = ∗⁻¹{E_F(H) + E_F′(K) : H, K antisymmetric}.
- By Schur, the 15-part can land only in 𝓔 ⊕ 𝓔ᵃ (control 6).

**Reported per operator, on the 15-part.** The 1-part is decided by control 6 and is reported only as that control.
- (i) Output zero or nonzero, and the rank of X∘ξ.
- (ii) For CCC, the inner term: the inner bracket `bracket(B, ∗x, 'C')` of `gu.shiab.shiab_parts(F, B, ξ(R))`, taken before the outer bracket. Record zero or nonzero, and its rank.
- (iii) dim(image ∩ 𝓔) and dim(image ∩ 𝓔ᵃ), checked to sum to the rank.

**Readings.**
- **Output 0.** This operator gives zero on the 15-part.
- **Nonzero, with the image in 𝓔.** The response is symmetric-tensor-valued. It is not an Einstein claim and not a field equation.
- **Nonzero on 𝓔ᵃ.** There is an antisymmetric-tensor response channel. This is the algebraic shape of the antisymmetric part of the Einstein tensor of a connection with torsion, as in Einstein–Cartan. It is a pointwise algebraic fact of the R2 reading only. It is not a field equation and not by itself non-GR.
- **CCC inner term nonzero on the 15-part.** B02's F1 cancellation, which is sufficient under pair symmetry, does not extend there. A zero is recorded with no converse claim.

### Q3. Linearized system: dispersion roots and kernel structure

"Characteristic set" is reserved for the principal symbol. The roots of U and M are the **dispersion roots**.

**Primary object.**
- On a ray k = ωu: det U(ωu) = det(∗)·det(iωN(u) + κ₁).
- So the dispersion roots of Υ_lin are **ω = iκ₁/ν** for the nonzero eigenvalues ν of the rational matrix N(u).
  - A real ω corresponds to a purely imaginary ν, i.e. ν² < 0, with ω² = −κ₁²/ν².
  - ν = 0 (the nilpotent part) gives no finite root. It is the degree deficit.
- The exact characteristic polynomial of N(u), a 64 × 64 rational matrix (python-flint `fmpq_mat.charpoly`), is the primary computation. It is factored over Q.
- det M then follows as a check: det M = det(2G₃)·|det U|² (control 4). Every root of det M has even multiplicity.

**Grade blocks.**
- These are the safe support blocks from Codex's probe:
  - CCC: {0}, {1,2}, {3,4};
  - CAA: {0,3,4}, {1,2};
  - CAC: {0,1,2,3}, {4};
  - E_OP: {0,3}, {1,2}, {4}.
- They are Spin-invariant subspaces, since Spin preserves Clifford grade, but are not claimed to be irreducible. The plan re-checks their support for N and for M.
- If blocks are used, every formula uses the block dimension d, not 64.

**Rays.**
- With `covariance_verified=true` (control 5):
  - the **timelike unit ray determines** g and F as polynomials in s = k². This is index 3 on (3,1) (η₃₃ = −1) and index 0 on (1,3).
  - The spacelike ray is a control. Its determinant must equal the same polynomial at the opposite sign of s. Pinned representatives: e₀ on (3,1) and e₁ on (1,3).
  - The null ray is control 9. Pinned: e₀ + e₃ on (3,1) and e₀ + e₁ on (1,3).
- With `covariance_verified=false`, only ray diagnostics are reported, for those pinned covectors. They are labelled `zero_on_sampled_ray`, `constant_on_sampled_ray` or `nonconstant_on_sampled_ray`. No global, massive-type or tachyonic-type classification is made.

**Recorded per operator and signature (timelike ray, κ₁ = 1).**
- (i) The characteristic polynomial of N(u) and its factorization: the nilpotent dimension, and each nonzero eigenvalue factor.
- (ii) For each root ω₀:
  - its multiplicity in det U;
  - dim ker U(ω₀) and dim ker M(ω₀) (their difference is the radical dimension of G₃ on im U(ω₀));
  - partial multiplicities wherever they are computed. Otherwise the entry reads "not computed".
- (iii) **Nested kernels of S₀(u):** {u⊗λ} ⊆ ker(X∘(u∧·)) ⊆ ker S₀(u). Record the three dimensions and the two quotient dimensions. The second quotient is the radical of the pairing on im(X∘(u∧·)).
- (iv) κ₁ = 0: rank of S₀ on each pinned ray.

**Outcomes** (valid with `covariance_verified=true`). Nullities are **polarization-space dimensions**, not physical degree-of-freedom counts. Constraint and gauge analysis is not part of option C.
- **(3b) N(u) nilpotent.** Then det U is a nonzero constant, and there are no finite dispersion roots: U(k) and M(k) are polynomially invertible. This does not mean the equations contain no derivatives, and "no propagating modes" is not concluded.
- **(3c) Real roots with ω² > 0 on the timelike ray** (ν² < 0). These are massive-type dispersion roots. With k² = η^{μν}k_μk_ν and η = diag(+1 × p, −1 × q), record m² = −k² on (3,1) and m² = +k² on (1,3). Also record the multiplicities and the nullities of U and of M. No stability claim is made.
- **(3e1) ω² < 0 on the timelike ray** (ν² > 0). This is a tachyonic-type root of this frozen-metric reading, under the (3c) m² convention. No instability claim is made, because no time-evolution setup is stated.
- **(3e2) Complex ω²** (ν² ∉ R). This is a non-real root, and it is not called tachyonic.
- **(3f) Non-semisimple root.** Record its partial multiplicities. It is forced wherever ker M(ω₀) = ker U(ω₀) (control 4). Where forced, the reading is "a root of the first-order symbol U, doubled by I₂ = ‖Υ‖²", and nothing further. A non-semisimple root of U itself is recorded with no reading.
- Mixed outcomes are recorded per root.

### Q4. Sign data on the kernels (named forms only)

For each real root ω₀ of Q3 with ω₀² = d ∈ Q, take exact bases V_U of ker U(ω₀) and V_M of ker M(ω₀). Kernels and forms are computed over Q(√−d), and Hermitian elimination uses rational pivots.

**Data, each named and reported separately:**
- **(i) Derivative form on ker M.** V_M^†M′(ω₀)V_M, scaled by |ω₀| so that its entries lie in Q(√−d). Record its rank and its inertia. By control 4 it vanishes on ker U, so when it is nondegenerate n₊, n₋ ≥ dim ker U.
- **(ii) Second-order form on ker U.** (U′(ω₀)V_U)^†G₃(U′(ω₀)V_U) = ½V_U^†M″(ω₀)V_U, and its inertia. It governs the leading (ω − ω₀)⁻² coefficient of M⁻¹ on ker U.
- **(iii) Restricted forms on ker S₀(u)** (the infinite-eigenvalue data of the M pencil). With V₀ an exact basis of ker S₀(u), record dim ker S₀(u) and the inertias of V₀^†S₁(u)V₀ and of V₀^†G₁V₀. This datum needs no dispersion root. It is not an intersection with ker M(ω₀), and it is not a residue form.

**Unsupported cases.** Roots with irrational ω₀², complex roots and non-semisimple roots give `not_applicable` or `requires_algebraic_extension` for (i). No inertia is invented. An unexpected zero direction in (i) at a root certified semisimple is an internal consistency failure.

**Implementation.** `gu.inertia` accepts Q(i) only. The Q(√−d) Hermitian elimination is new code with its own controls:
- d = −1, where it must agree with `gu.inertia`;
- one hand-checked d;
- off-diagonal pivots;
- the conjugation convention.

**Reading.** These are algebraic sign facts about an indefinite pairing (H14). They are **not** ghost or unitarity theorems: the draft fixes no positive real form, and the word "ghost" is not used. The signature of the 4D trace pairing is computed where it is needed, never assumed.

## 5. Readings of a negative result

**What a negative result closes:** this reading only. That is the flat background, ε = 1 with the metric frozen, the four named operators, at quadratic order. It does not close GU, R1, a curved-background reading, or a model where ε varies.

**What Q3 and Q4 do not say:** nothing in them is a statement about (9.4). Phase 2's (9.4) no-go concerns a different action, at order T².

## 6. Rejected inputs (so they are not re-proposed)

Do not re-propose any of the following:
- a neutral 4D u(A) trace pairing;
- a free ± on the cross term;
- Palatini recovery, or an EH term, from this quadratic model;
- "propagator" or "ghost";
- the covariance identity presented as a new theorem;
- an anti-Hermitian boundary subcase;
- realification without a multiplicity correction;
- S₂ without its factor 2;
- the unphased basis;
- "ill-posed" or "no propagating modes" read from a determinant;
- a restricted Gram used as a residue form;
- a Proca toy;
- ker S₀ described as "exact part plus ker X";
- an unspecified Einstein span, or 𝓔 called "Einstein-type";
- outcomes that the algebra pre-decides, listed as open: (3a) identically zero and (3d) ω² = 0 at κ₁ ≠ 0, and (1a) for E_OP.

Sources: the Argon fact-check (Grok), Codex's rev 0 and rev 2 reviews, Grok's rev 1 co-revision and rev 2 review, and the fresh Claude rev 2 review.

## 7. Deliverables (for the implementation plan)

**Code**, in `experiments/B07/optionc/`:
- `sector.py`:
  - the phased-basis S₀, S₁, S₂, from `fourier_terms`' `action_k0/k1/k2` and Πᵀ·Π;
  - U(k), N(k) and G₃;
  - controls 1–5 and 9;
  - Q1 and its closed form.
- `torsion.py`: the projectors, ξ on Λ²⊗Λ², 𝓔 and 𝓔ᵃ, the Schur controls, and Q2.
- `spectrum.py`:
  - the charpoly of N(u) and its factorization;
  - roots, kernels of U and M, partial multiplicities, nested kernels;
  - Q4 (i)–(iii), with the Q(√−d) Hermitian elimination;
  - control 7.
- `run.py`: writes `result.json`, using `phase2/run.py:git_commit` and `dirty_paths` adapted to the new output path.

**Reuse.** `second_order.{fourier_terms, mpair, star_c, star_inv, adjoint, star_adjoint_sign, mass_sign, wavevectors}`, `variation.{BRANCHES, branch_map, Linear, pair, wedge_prod, one_forms}`, `universal.{phases, to_phased, from_phased, rho, matrix_of}`, `phase2/run.py:e_op`, `phase2/gates.py:response`, `gu.shiab.{xi, shiab_parts, embed_tensor, generator_action}`, `escape/quadratic.curvature_basis`, `gu.inertia.inertia`.

**New code:**
- the polynomial and charpoly pipeline;
- algebraic-root kernels;
- the Q(√−d) elimination;
- the 36-dimensional projectors.

**Tests**, in `tests/test_b07_optionc.py`:
- one test per control;
- seeded faults, each failing on a test assertion and seeded independently. They cover the factor 2, the phases, the transpose and conjugation, the Gram identity, a dropped η_cη_d, reconstruction, the degree deficit and the Q(√−d) conjugation.

**Route:** Codex executes; a fresh Codex session re-derives independently; Grok audits the README; Claude runs P7 on a clean clone.

## 8. Decisions

1. **Q4.** Data (i) and (ii) are both primary. (i) is predicted to vanish on ker U (control 4). (iii) is separately named. Sign work is limited to rational ω₀².
2. **Runtime.** The limit is 2 h per signature, with status `partial`. `partial` is not an outcome and not a negative result. The charpoly degree is not capped; with the first-order reduction it is at most 64.
3. **Control 5** is mandatory for any orbit or global claim. If it fails, only labelled ray diagnostics are reported (exception (a)). Orbit reduction is never assumed.
