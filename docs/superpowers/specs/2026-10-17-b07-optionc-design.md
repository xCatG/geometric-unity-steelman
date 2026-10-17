# B07 option C: the T-sector of I₂ and the frozen-metric connection reading. Pre-registration design

**Status:** rev 1. It folds in Codex's adversarial review of rev 0 (`c6564f2`), whose verdict was "revise", with 11 findings, all accepted.

Nothing in this design has been run. Codex's feasibility probes reported sizes, timings and block support only. They reported no Q1–Q4 ranks, roots, inertias or classifications. The outcome classes, and the reading attached to each outcome, are fixed **before** any experiment code exists. The implementation plan, with smoke-tested code, comes after this design is approved.

**Inputs:**
- Phase 2 H14 (`experiments/B07/phase2/derivations.md`, `second_order.py`): the exact Fourier variation of the quadratic part of I₂, its κ₁⁰/κ₁¹/κ₁² split, ∗^† = (−1)^{k(n−k)}∗, ∗^†∗ = (−1)^q on Ω¹, and the ym_symbol entry ratios.
- Phase 2 H12 (`universal.py:phases`): the real basis of u(A).
- Escape E1/E2 (`experiments/B07/escape/`).
- B02's stated limit, "Non-Levi-Civita curvature" (`experiments/B02/README.md:152`).
- A fact-check of another model's (Argon's) proposal, by Grok. Its rejected parts are listed in §6.

## 1. What is new, and what is not

H14 already did three things for the quadratic action:
- compared its variation with (9.12)–(9.13), term by term;
- recorded its κ orders;
- decided the ordinary-YM question at the principal-symbol level.

**Option C does not redo any of that.** It asks what H14 did not:
- **Q1:** is the κ₁¹ cross term zero in the field equation?
- **Q2:** what does each operator do on pointwise Lorentz-valued curvature values that are not algebraic?
- **Q3:** what is the dispersion zero set of the linearized T-sector, and what kernel structure does it have?
- **Q4:** what is the fiber-pairing sign data on those kernels?

## 2. Model (the reading being tested)

**Background and method**
- A 4D point, at signatures (3,1) and (1,3). The background is flat, B = d and **ε = 1**. The metric is frozen and δT = δA (Phase 2 reading V).
- Coefficients are constant. Arithmetic is exact over Q(i). No floating-point or modular result becomes an outcome.

**Operators**
- CCC, CAA, CAC and E_OP, exactly as in Phase 2 (`phase2/run.py:E_OP`, `escape/run.py`). These are undressed.
- The plan asserts that each operator maps u(A)-valued 2-forms to u(A)-valued 3-forms at the signature in use. If that closure fails, the run stops (see (2,2) and (4,0) below).

**Real field basis**
- T ∈ Ω¹(u(A)). Its real fiber dimension is 4 × 16 = 64.
- The basis is the **phased** one, e^a ⊗ i^{ph(C)}Γ_C, with ph from `universal.phases`. `variation.one_forms` is the unphased basis.
- With D the diagonal phase matrix, the bilinear matrices transform as M = Dᵀ M_raw D.
- The Fourier coefficients satisfy t(−k) = conj t(k). They are not 128 independent fields.

**Pairing and normalization**
- The pinned pairing is ⟨x, y⟩ = Tr(x∧∗y)/2^{n/2}, where Tr/2^{n/2} is the normalized trace.
- **M is H14's first-variation (Hessian) matrix:** M(k; κ₁) = S₀(k) + κ₁S₁(k) + κ₁²S₂, the κ-parts of B(a, t) = 2⟨X(−iK∧a) + κ₁∗a, X(iK∧t) + κ₁∗t⟩.
- Hence **S₂ = 2(−1)^q G₁**, with G₁ the one-form Gram matrix.
- The half-gradient operator is P = ½G₁⁻¹M. Its mass part is (−1)^q Id.
- Every reported number names which of M or P it refers to.

**Prime convention.** The primary model is H14's **fixed-X** policy: X is held fixed while the external star and its pairing change. Under that policy, at n = 4:
- the identity M′(k; κ₁) = −M(k; −κ₁) is asserted as a test;
- so S₀ and S₂ change sign and S₁ does not.

Rebuilding X with the prime star would be a separately named reading. It is not run.

**Scaling.** For real κ₁ ≠ 0, M(k; κ₁) = κ₁²M(k/κ₁; 1). So κ₁ = 1 is used, with the orientation map for κ₁ < 0 stated. κ₁ = 0 is reported separately.

**This is the R2 reading at linear order, and only that.** With B and ε fixed, T = A − B is the connection perturbation, not an extra field. Metric fluctuations are not in the model (see O0).

**Excluded explicitly.** The following are left out by restriction. None of them is avoided "in favor of" anything, and the exclusion bears on nothing in Phase 2's (9.4) result.
- [T, T] and every cubic or quartic term.
- Curved backgrounds.
- ε or the metric varying.
- Dressings ε ≠ 1.
- 14D.

## 3. Identities and controls (stop conditions)

A failure of any item below stops the run, and is reported as a failed control, never as an outcome.

1. **Fourier symmetry.**
   - M(k) = M(−k)ᵀ, and conj M(k) = M(−k) in the phased basis, so M(k) is Hermitian for real k.
   - In particular S₁(k)ᵀ = −S₁(k), with S₁ purely imaginary.
2. **Homogeneous reconstruction.**
   - Determining sets: S₀ from k ∈ {e_i} ∪ {e_i + e_j}, S₁ from {e_i}, and S₂ at k = 0.
   - Each is then checked at exact wavevectors outside its determining set.
3. **Direct small-action control.** For one operator and a few basis pairs, the Hessian entry is computed directly from the action ⟨X(dT) + κ₁∗T, ·⟩ by polarization, independently of `fourier_terms`.
4. **Convention identities.**
   - S₂ = 2(−1)^q G₁.
   - The prime identity M′(k; κ₁) = −M(k; −κ₁).
5. **Lorentz covariance** of the frozen-background operator, checked on the polynomial coefficients S₀, S₁, S₂ for ε = 1:
   - infinitesimal Spin(p,q) generators act on the field basis, and the coefficients transform by congruence;
   - the determinant representation weight is 1.
   - Then det M(k) = F(k²), a polynomial in k², and the orbit reduction of Q3 is justified. Without this check, Q3 reports ray data only.
6. **Q2 controls.**
   - The projectors P₁₅ = (I − τ)/2, P₁ = Alt and P₂₀ = (I + τ)/2 − Alt are idempotent, mutually annihilating, sum to the identity, have dimensions 20/1/15, and are equivariant.
   - On the 20-dimensional algebraic part, every operator reproduces B02's response, and the CCC inner term is 0.
   - Off the algebraic part, one elementary-tensor ξ entry is checked against the hand formula.
7. **Spectral backend controls (toys with known answers):**
   - a scalar massless and a scalar massive wave operator, as null-ray controls;
   - a small Hermitian matrix polynomial with a known repeated root and a known Jordan chain;
   - a matrix with a singular leading coefficient, for degree-deficit reconstruction;
   - the 3D toy X = id, i.e. ‖dT + κ∗T‖², whose Maxwell–Chern–Simons–mass determinant is derived and pinned by hand first. It is not Proca, because the ⟨dT, ∗T⟩ term is Chern–Simons-type.
8. **(2,2) and (4,0).**
   - These are convention controls only: star squares and adjoints, the even-q mass sign, the Hessian factor, the Fourier identities, reconstruction, the projectors and the pencil backend.
   - With the documented Dirac adjoint Γ_a^♯ = (−1)^qΓ_a, the unphased F is not u(A)-valued at even q. So whether the operators close on u(A) at these signatures is **checked**.
   - If closure fails, these are run as complexified formal calculations, labeled as such.
   - No mass or stability reading is attached at these signatures: Euclidean space has no real null vector, and split signature has no single time direction.

## 4. Pre-registered outcome classes

A result outside the listed outcomes is reported as "unanticipated", with no reading.

### O0. Einstein–Hilbert term (closed by construction)
- The metric is frozen and every term is quadratic. So **no outcome of Q1–Q4 can exhibit an Einstein–Hilbert term**.
- S₂ is a mass term for T.
- An EH claim needs two things: a separately specified enlarged model, and an exhibited density that is linear in curvature. Neither is part of option C.
- Nothing below is read as gravity, Palatini recovery or Newton's constant.

### Q1. The κ₁¹ cross term
S₁ is H14's **first-variation** matrix, so the test is direct: is S₁(e_i) = 0 for the four basis covectors?

- **(1a) S₁ ≡ 0.** The cross term 2κ₁⟨X(dT), ∗T⟩ contributes nothing to the quadratic field equation, so in this model it is a boundary term. (9.13)'s κ₁ terms 2 (repaired) and 3 (derived) are each nonzero (H14), and they cancel.
- **(1b) S₁ ≢ 0.** Record the following:
  - its rank at each e_i, for M (not P);
  - its support on the safe grade blocks (see Q3);
  - which Clifford-grade components it couples.

  Reading: I₂ contains a first-order quadratic term in T that contributes to the field equation.
  - This is a descriptive statement only. It is not EH, Palatini or Chern–Simons by name.
  - If an explicit boundary density is wanted, it is derived from the symmetric part of the coefficient Cᵘ in Tᵀ Cᵘ ∂_μT, with periodic or compact boundary conditions.
- **Sign** (pinned, fixed-X):
  - The cross density is 2κ₁ Tr_norm(X(dT)∧∗∗T), with ∗∗ = (−1)^{q+1} on Ω¹.
  - Graded cyclicity, with degrees 3 and 1, gives Tr_norm(X(dT)∧T) = −Tr_norm(T∧X(dT)).
  - So the reordered coefficient is 2κ₁(−1)^q/2^{n/2}.

### Q2. Pointwise Lorentz-valued curvature that is not algebraic
**Domain**
- These are off-shell **pointwise curvature values**, F = ξ(R).
- The ξ formula is ξ(R) = ½Σ_{a<b, c<d} R_abcd η_cη_d e^{ab} ⊗ Γ_cΓ_d, with R ∈ Λ²⊗Λ² (36 dimensions) and no further symmetry.
- The formula needs no pair symmetry, and `gu.shiab.xi` already evaluates it. Raising a different pair, or transposing slots, would be a different convention and is not run.
- The space splits Spin-equivariantly as 36 = 20 ⊕ 1 ⊕ 15:
  - 20 algebraic dimensions;
  - 1 totally antisymmetric dimension;
  - 15 pair-antisymmetric dimensions.
- The 1 and 15 parts are **non-algebraic, torsion-sensitive components**. They do not exhaust torsion and do not measure it. The GU field T has all Clifford grades, and only the grade-2 (Lorentz) part of F is tested here.
- **Not the Q3 domain.** A single Fourier curvature iK∧T satisfies K∧F = 0, and its Lorentz-valued image has dimension 18 for k ≠ 0. If Q2 is later related to Q3, that Bianchi condition is imposed separately.

**Fixed output subspace**
- 𝓔 = ∗⁻¹{E_F(H) + E_F′(K) : H, K symmetric}, a subspace of 3-form values.
- Membership in 𝓔 is reported relative to 𝓔. It is not a Spin decomposition.

**Reported, independently per operator and per part (1 and 15)**
- (i) Output: zero or nonzero, with the rank of X∘ξ on the part.
- (ii) For CCC only, the inner-commutator contribution: zero or nonzero, with its rank.
- (iii) dim(image ∩ 𝓔) and the rank of the image modulo 𝓔. No arbitrary complement is chosen.

**Readings**
- **Output 0.** This operator gives zero on that non-algebraic part.
- **Nonzero, with the image in 𝓔.** The response stays inside the Einstein-type value space.
- **Nonzero, with the image modulo 𝓔 nonzero.** A pointwise value outside 𝓔 exists. This is a candidate non-GR channel of the R2 reading, at the algebraic level only. It is not a field equation, and by itself it is not a non-GR theory.
- **CCC inner term nonzero off the algebraic part.** B02's F1 cancellation was proved under pair symmetry as a sufficient condition, and it does not extend to these inputs. If the inner term is 0, that is recorded with no converse claim.

### Q3. Linearized T-sector: dispersion zero set and kernel structure
"Characteristic set" is reserved for the principal symbol S₀. Roots of the full M form the **dispersion zero set**.

**Directions**
- With control 5 passed, det M(k) = F(k²), so the following rays decide F:
  - a timelike unit ray (both signs of k²);
  - a spacelike unit ray;
  - one nonzero null ray, which probes **F(0) only** and not the massive frequencies;
  - k = 0 separately.
- On (3,1) the timelike axis is index 3 (η₃₃ = −1). On (1,3) it is index 0.
- If control 5 fails, the rays are reported as ray data, with no orbit claims.

**Algebra**
- In the phased basis, M(ω) = Aω² + iCω + D, with A, C, D rational.
- The substitution ω = −iz gives a rational polynomial matrix, so no realification is needed. The roots are mapped back before any real or imaginary label is attached.
- Computation is on the **native 64 × 64** matrix, or on Codex's safe grade-support blocks:
  - CCC {0}, {1,2}, {3,4};
  - CAA {0,3,4}, {1,2};
  - CAC {0,1,2,3}, {4};
  - E_OP {0,3}, {1,2}, {4}.
  These are support blocks, not Spin modules, and the plan re-checks the support.
- **Primary algorithm:** an exact polynomial determinant over Q[z], by fraction-free elimination, or by interpolation at more exact points than the degree bound with verification at extra points.
- **Fallback:** the reversed companion L = [[0, I], [−C₀⁻¹A₀, −C₀⁻¹B₀]] after checking that C₀ = M(0) is invertible. Then det M(ω) = det C₀ · ω^{2N} · χ_L(1/ω). Zero eigenvalues of L account for the degree deficit. They are not modes.
- A singular leading coefficient is expected, since d(k)(k⊗λ) = 0 makes S₀ singular for every k. The degree deficit is recorded exactly.
- Runtime limit: 2 h per signature. If it is exceeded, the result is reported as **partial**, never as a numerical fallback.

**Recorded per operator, signature and ray**
- (i) det M as an exact polynomial: its degree, leading coefficient, constant term and factorization over Q.
- (ii) Each root ω₀: its algebraic multiplicity, its exact nullity dim ker M(ω₀), and its elementary-divisor data where computed (otherwise "not computed").
- (iii) Nested kernels of S₀ at the ray's k: {k⊗λ} ⊆ ker(X∘d(k)) ⊆ ker S₀. Their three dimensions and two quotient dimensions are recorded. The second quotient is the radical of the pairing restricted to im(X∘d(k)), not "a kernel of X".
- (iv) The κ₁ = 0 case: rank of S₀ on each ray.

**Outcomes, each with its reading.** Nullity is called a **polarization-space dimension**, not a physical degree-of-freedom count, because constraint and gauge analysis is not part of option C.
- **(3a) det M ≡ 0 on every ray.** This is a polynomial degeneracy, with its generic nullity recorded. It may be a redundancy or an undetermined direction. That is not decided here, and "ill-posed" is not concluded.
- **(3b) det M is a nonzero constant on every ray.** There are no finite dispersion roots, so M(k) is polynomially invertible. This does not mean the equations contain no derivatives, and "no propagating modes" is not concluded.
- **(3c) Real roots with ω² > 0 on the timelike ray**, consistent with F(k²). Record each k²-root, its multiplicity and its nullity. The reading is "massive-type dispersion root", with m² = −k² in the stated signature convention. No stability claim is made.
- **(3d) A root with ω² = 0.** This is a massless-type root, cross-checked against F(0) from the null ray.
- **(3e) Some ω² < 0 on the timelike ray, or complex ω².** Record it. The reading is "a non-real or tachyonic-type root of this frozen-metric reading". No instability claim is made without a stated time-evolution setup, and nothing is concluded about GU.
- **(3f) A repeated root whose nullity is less than its multiplicity (non-semisimple).** Record the Jordan data. No reading is attached.
- Mixed outcomes are recorded per root.

### Q4. Fiber-pairing sign data
**What is computed.** For each real semisimple root ω₀ with exact basis V of ker M(ω₀), compute the **derivative form** V^†(∂_ωM)(ω₀)V, and its inertia (+, −, 0) when it is nondegenerate. This form controls the residue of the inverse pencil at a simple or semisimple root. For roots with nonzero nullity in ker S₀ blocks, compute the fiber-pairing inertia of G₁ restricted to the block, named as such.
- **Supported cases:** roots in Q, and roots in quadratic fields, using exact sign isolation of a + b√d.
- **Higher-degree, complex or non-semisimple roots:** the output is "not applicable" or "requires an algebraic extension". No inertia is invented.
- `gu.inertia` covers Q(i) only. Any extension is a pre-registered implementation with its own controls.

**Reading.** These are algebraic sign facts about an indefinite pairing (H14). They are **not** ghost or unitarity theorems, because the draft fixes no positive real form, and the word "ghost" is not used. The 4D trace pairing's own signature is computed where it is needed, never assumed.

## 5. Readings of a negative result

**What a negative result closes:** this reading only. That is the flat background, ε = 1 with the metric frozen, the four named operators, at quadratic order. It does not close GU, R1, a curved-background reading, or a model where ε varies.

**What Q3 and Q4 do not say:** nothing in them is a statement about (9.4). Phase 2's (9.4) no-go concerns a different action, at order T².

## 6. Rejected inputs (so they are not re-proposed)

From the Argon fact-check (Grok, with Claude spot-checks):
- **"The u(A) trace pairing has neutral signature in 4D."** Unsupported. B05's (64,64) is a 14D spinor Hermitian form, not this pairing.
- **"The cross term is ±2κ₁∫Tr(T∧⊚F)" with a free sign.** The sign is fixed (§4, Q1).
- **"Einstein–Palatini recovery via the cross term, without the obstructed cubic [T,T]."** Covered by O0. It also misstates Phase 2.
- **"Propagator", "which grades propagate", "ghost".** Q3 and Q4 use dispersion zero set, polarization space and inertia instead.
- **"⊚_h(x)=0 ⟺ c_h⁻¹x ∈ ker ⊚" as a new theorem.** It is the covariance identity.

From Codex's review of rev 0 (folded):
- the anti-Hermitian "boundary" subcase;
- realification without a multiplicity correction;
- S₂ without its factor 2;
- the unphased basis;
- "ill-posed" and "no propagating modes" read from ray determinants;
- restricted Gram used as a residue form;
- the "Proca" toy;
- ker S₀ described as "exact part plus ker X";
- non-exhaustive Q2 classes;
- an unspecified "Einstein span".

## 7. Deliverables (for the implementation plan)

**Code, in `experiments/B07/optionc/`:**
- `sector.py`: the phased-basis S₀, S₁, S₂ built from `second_order.fourier_terms`; controls 1–5; Q1; the polynomial assembly.
- `torsion.py`: the projectors, the ξ extension and its control, and Q2.
- `spectrum.py`: the exact determinant, roots, multiplicities, nullities, nested kernels and Q4 derivative forms; control 7.
- `run.py`: writes `result.json`, with Phase 2's dirty-tree guard and `source_commit`.

**Tests, in `tests/test_b07_optionc.py`:**
- one test per control in §3;
- seeded faults, each failing on a test assertion and each seeded independently. They cover the factor 2, the phases, the transpose and conjugation, a dropped η_cη_d, the reconstruction and the degree deficit.

**Route after implementation:**
1. Codex executes.
2. A fresh Codex session re-derives independently.
3. Grok audits the README.
4. Claude runs P7 on a clean clone.

## 8. Remaining open questions for reviewers

1. Is the Q4 derivative form the right sign datum to pre-register? Or should Q4 be limited to fiber-pairing inertia on the ker S₀ blocks, which is more modest?
2. For Q3, is a 2 h per-signature limit with "partial" status acceptable? Should the plan cap root-field degree at 2 up front?
3. Is control 5 (covariance) cheap enough to be mandatory? Or should Q3 report ray data only and leave orbit reduction as a stated assumption?
