# B07 option C: the T-sector of I₂ and the frozen-metric connection reading. Pre-registration design

**Status:** rev 0, a design for review. Nothing in it has been run. The outcome classes and how each outcome is read are fixed here **before** any code exists. The implementation plan (with smoke-tested code) follows once this design is approved.

**Inputs:**
- Phase 2 H14 (`experiments/B07/phase2/derivations.md`, `second_order.py`): the exact Fourier variation of the quadratic part of I₂, its κ₁⁰/κ₁¹/κ₁² split, ∗^† = (−1)^{k(n−k)}∗, ∗^†∗ = (−1)^q on Ω¹, and the ym_symbol entry ratios.
- Escape E1/E2 (`experiments/B07/escape/`).
- B02's stated limit, "Non-Levi-Civita curvature" (`experiments/B02/README.md:152`).
- A fact-check of another model's (Argon's) proposal, done by Grok and folded below. The rejected parts are listed so they are not re-proposed.

## 1. What is new, and what is not

H14 already compared the quadratic action's variation with (9.12)–(9.13) term by term, recorded its κ orders, and decided ordinary YM at the principal-symbol level. **Option C does not redo any of that.** It asks four questions that H14 did not:
- **Q1.** What is the κ₁¹ cross term as a quadratic form?
- **Q2.** What does each operator do on Lorentz-valued curvature that is not algebraic, that is, curvature with torsion?
- **Q3.** What is the linearized T-sector's characteristic set, its mode count, and the masses of its modes?
- **Q4.** What signs does the action take on those modes?

## 2. Model (the reading being tested)

- **Background.** A 4D point, at signatures (3,1) and (1,3). The background is flat, with B = d. ε and the metric are frozen and δT = δA, which is Phase 2's reading V. The coefficients are constant. Arithmetic is exact over the Gaussian rationals.
- **Operators.** CCC, CAA, CAC and E_OP, taken exactly as in Phase 2 (`phase2/run.py:E_OP`, `escape/run.py`).
- **Pairing.** The pinned pairing ⟨x, y⟩ = Tr(x∧∗y)/2^{n/2} is primary. The prime convention is recorded alongside it wherever a sign is reported. Every sign statement names its convention in the same sentence.
- **Field.** T ∈ Ω¹(u(A)) has a real fiber of dimension 4 × 16 = 64 (`V.one_forms`).
- **Quadratic action.** I₂⁽²⁾[T] = ⟨X(dT) + κ₁∗T, X(dT) + κ₁∗T⟩. Its Fourier matrix is M_X(k; κ₁) = S₀(k) + κ₁S₁(k) + κ₁²S₂, with S₀, S₁, S₂ the κ₁⁰, κ₁¹, κ₁² parts of H14's B(a, t). S₀ is homogeneous of degree 2 in k, S₁ of degree 1, and S₂ of degree 0. For κ₁ ≠ 0, M_X(k; κ₁) = κ₁²M_X(k/κ₁; 1), so κ₁ = 1 loses nothing. κ₁ = 0 is reported separately.
- **This is the R2 reading at linear order, and only that.** At the flat point, with the metric frozen, an independent connection perturbation is exactly T. Metric fluctuations are **not** in the model, so no question about a graviton, an Einstein–Hilbert term, or Newton's constant can be asked of it (see O0).
- **Excluded explicitly.** The following are left out by restriction. Leaving them out avoids nothing in Phase 2's (9.4) result:
  - [T, T] and every cubic or quartic term;
  - every curved background;
  - ε or the metric varying;
  - 14D.

## 3. Pre-registered outcome classes

Each question lists every possible outcome and the reading attached to it. A result outside the listed outcomes is reported as "unanticipated", with no reading.

### O0. Einstein–Hilbert term (closed by construction, stated in advance)
- The model freezes the metric, and I₂ is quadratic in curvature and in T. So **no outcome of Q1–Q4 can show an Einstein–Hilbert term**.
- The term κ₁²S₂ = (−1)^q κ₁² × (the Gram form on Ω¹(u(A))) is a mass term for T, not EH.
- A positive EH claim would need R1 (a varied metric with its Levi-Civita connection) or a model in which ε varies. Both are out of scope.
- This entry exists so that no later sentence reads a T-mass or a cross term as gravity.

### Q1. The κ₁¹ cross term
Compute S₁(k) on the test wavevectors. Because S₁ is linear in k, the n basis vectors e_i decide it.
- **(1a) S₁ ≡ 0.** The cross term 2κ₁⟨X(dT), ∗T⟩ is a total derivative at quadratic order. Then (9.13)'s κ₁ terms 2 + 3, in their repaired and derived forms, cancel in the field equation. They are individually nonzero (H14), but their sum is zero. Reading: in this model, the κ₁ coupling is a mass term plus a boundary term.
- **(1b) S₁ ≢ 0.** Record its rank for each e_i, and which Clifford grade pairs (j, l) of (a, t) it couples. Record whether the pairing form a ↦ B₁(ā, a) vanishes identically, which would mean S₁ is anti-Hermitian, so it enters the action as a total derivative even though the field-equation term is nonzero. Reading: I₂ contains a first-order (Dirac- or BF-like) quadratic term in T. The name is descriptive only. It is not EH and not Palatini recovery.
- **Sign.** By H14, the cross term equals 2κ₁∫Tr(X(dT)∧∗∗T), and ∗∗ = (−1)^{q+1} on Ω¹ in 4D under the pinned star. No reordering to Tr(T∧X(dT)) is used.

### Q2. Lorentz-valued curvature that is not algebraic (torsion channels)
- **Input space.** F = ½R_abcd e^{ab} ⊗ Γ_cΓ_d, with R antisymmetric in ab and in cd and no other symmetry: 36 dimensions. It splits Spin-equivariantly as 36 = 20 ⊕ 1 ⊕ 15:
  - 20 algebraic curvature;
  - 1 totally antisymmetric part R_[abcd];
  - 15 pair-antisymmetric part R_abcd = −R_cdab.
  The first Bianchi identity fails on the 1 and 15 parts, and pair symmetry fails on the 15. The decomposition is exact and its projectors are checked to be idempotent.
- **ξ.** The ξ convention is B02's, extended linearly to the 36 dimensions with the same a<b, c<d and ½ normalization and the same η_cη_d factors. The plan must state this extension explicitly and test that it reduces to `gu.shiab.xi` on the 20 algebraic dimensions.
- **Control.** On the 20 algebraic dimensions, the CCC inner commutator is 0 and the outputs reproduce B02's response. If they do not, the run **stops** as a convention bug.
- **What is computed.** For each operator X: the rank of X∘ξ on the 1 part and on the 15 part. Where nonzero, also its Spin content, read as the output's projection onto the Ricci-type image (B02's E_F, E_F′ span) against the rest. For CCC, the inner-commutator term separately.
- **Outcomes, per operator and part:**
  - **(2a) Zero.** This operator does not see that torsion channel at the point.
  - **(2b) Nonzero, and the inner commutator wakes up.** B02's F1 cancellation does not extend off the algebraic subspace, which is exactly B02's stated limit, now measured.
  - **(2c) Nonzero and outside the Einstein span.** A non-Einstein response channel exists for torsionful curvature. Reading: a candidate non-GR channel of R2, at the algebraic level only. It is not a field equation.
- **What Q2 is not.** It is not a classification of all Spin-invariant quadratic forms on Ω²(u(A)). Only the Lorentz-valued (grade-2 Clifford) part of curvature is tested. Other Clifford grades of F are out of scope and are named as such.

### Q3. Linearized T-sector: characteristic set, mode count, masses
- **Directions.** For each operator, at κ₁ = 1, evaluate M_X(ωu) as a matrix polynomial in the scalar ω along three directions u:
  - a timelike unit vector (the rest frame);
  - a spacelike unit vector;
  - one null vector.
  On (3,1) the timelike axis is index 3 (η₃₃ = −1); on (1,3) it is index 0. M is realified to a 128 × 128 real form if the entries are complex.
- **What is computed exactly:**
  - (i) det M_X(ωu) as a polynomial in ω, computed by linearizing the quadratic eigenproblem with an exact characteristic polynomial (python-flint).
  - (ii) Its roots ω², taken as exact algebraic numbers (factored polynomials). Their real and complex structure is recorded.
  - (iii) The dimension of the kernel of S₀, and how much of that kernel is the exact part {k ⊗ λ}, and how much is ker(X) pulled back.
  - (iv) The κ₁ = 0 case separately: rank of S₀ along each direction.
- **Outcomes:**
  - **(3a) det M ≡ 0 in ω.** There is an identical degeneracy: a redundancy or an undetermined mode survives the mass term. Record its dimension. Reading: this reading of I₂ does not determine T. It is ill-posed as a linear field theory.
  - **(3b) det M is a nonzero constant in ω.** No propagating modes: T is fully algebraic and fixed by its constraint. Reading: T carries no linear degrees of freedom here.
  - **(3c) The roots are real ω² > 0 in the rest frame, consistent across directions.** These are massive modes with m² = ω² × κ₁². Record the multiplicity per root and per Clifford grade block.
  - **(3d) Some root has ω² < 0 at rest, or complex ω².** These are tachyonic or complex modes. Record them. Reading: an instability of this frozen-metric reading. It is not a verdict on GU.
  - Mixed outcomes are recorded per root.
- **Consistency check.** The null direction must agree with the massive and massless counts from the other two directions. A massless mode needs det M(ω u_null) to vanish at the corresponding ω. A mismatch is reported, not tuned away.

### Q4. Sign data on the modes
- **What is computed.** For each root of Q3 and for each operator's ker S₀ block: the inertia (+, −, 0) of the restricted pairing (the residue form on the root's kernel) under the pinned pairing, and under the prime pairing as a check.
- **Reading.** These are algebraic facts about an indefinite pairing (H14; B05 for the 14D spinor form). They are **not** ghost or unitarity theorems, because the draft fixes no positive real form. The word "ghost" is not used.
- **What is not claimed.** The 4D trace pairing's own signature is not assumed. If it is needed, it is computed (`gu.inertia`) and reported as computed.

## 4. Readings of a negative result (fixed in advance)

- **What a negative result closes.** It closes this reading only: flat background, ε and metric frozen, the four named operators, quadratic order. It does not close GU, R1, a curved-background reading, or a model where ε varies.
- **No smuggled conclusions.** "No propagating T" (3b) is a property of this reading, and so is "ill-posed" (3a). Neither is a statement about (9.4). The (9.4) no-go of Phase 2 is about a different action at order T². Nothing here bears on it. The phrase "the obstruction lives in the cubic structure" is not used.

## 5. Rejected inputs (so they are not re-proposed)

From the Argon fact-check (Grok, with Claude spot-checks):
- **"The u(A) trace pairing has neutral signature in 4D."** Unsupported. B05's (64,64) is a 14D spinor Hermitian form, not this pairing.
- **"The cross term is ±2κ₁∫Tr(T∧⊚F)."** Wrong as stated. The sign is fixed, (−1)^{q+1} through ∗∗, and the reordering is not justified.
- **"Einstein–Palatini recovery via the cross term, without the obstructed cubic [T,T]."** Not pre-registerable. It is covered by O0, and it misstates Phase 2.
- **Not used in readings:** "Propagator", "which grades propagate", and "ghost". Q3 and Q4 use characteristic set, modes and inertia instead.
- **"⊚_h(x)=0 ⟺ c_h⁻¹x ∈ ker ⊚" as a new theorem.** It is the covariance identity. It is not part of this design.

## 6. Deliverables (for the implementation plan)

- `experiments/B07/optionc/`:
  - `sector.py`: S₀, S₁, S₂ built from `second_order.fourier_terms`; Q1; the Q3 polynomial assembly.
  - `torsion.py`: the 36 = 20 ⊕ 1 ⊕ 15 split, extended ξ, and Q2.
  - `spectrum.py`: exact determinant, roots and inertia for Q3/Q4.
  - `run.py`: writes `result.json`, with the same dirty-tree guard and `source_commit` as Phase 2.
- Tests in `tests/test_b07_optionc.py`:
  - the H14 reproduction (S₀, S₁, S₂ against `fourier_terms`);
  - the Q2 control (algebraic part equals B02);
  - the projectors;
  - a toy control: X = id in 3D, with a known massive Proca-like determinant;
  - seeded faults, each failing on a test assertion.
- Then the usual route:
  - Codex executes;
  - a fresh Codex session re-derives independently;
  - Grok audits the README;
  - Claude runs P7 on a clean clone.

## 7. Open questions for the reviewers

1. Is "S₁ anti-Hermitian, so it enters the action as a total derivative" the correct test? The Fourier action pairs a e^{−ik·x} with t e^{+ik·x}. Which symmetry of S₁(k) under k → −k and transpose is the right one?
2. The 36-dimensional ξ extension: is a<b, c<d, ½ with η_cη_d unambiguous once pair symmetry is dropped? Or does the index-raising pattern produce a second candidate, which would then become a register reading?
3. Q3 realification and exact charpoly at 128–256 dimensions: is block-diagonalizing by Clifford grade first required for runtime, and is the grade split exact for M (H14 found that S₀ pairs equal grades)?
4. Should Q3 also run at (2,2) and (4,0), as H14 did, as controls for signature dependence?
5. Is anything in O0–Q4 new-theory building rather than the steelman of the draft's (9.11)?
