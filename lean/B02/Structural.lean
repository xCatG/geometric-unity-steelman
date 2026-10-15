import Mathlib

/-! Structural identities over vector spaces over any field. Three named linear
Hodge maps correspond to input degrees 2, n, and 1. Instantiating these maps
and bilinear brackets with the concrete exterior/Clifford model is separate. -/
namespace B02.Structural
universe u
variable (K : Type*) [Field K] (M : Type u) [AddCommGroup M] [Module K M]
structure OperatorData where
  star2 : M →ₗ[K] M
  starN : M →ₗ[K] M
  star1 : M →ₗ[K] M
  bracket0 : M →ₗ[K] M →ₗ[K] M
  bracket1 : M →ₗ[K] M →ₗ[K] M
  bracket2 : M →ₗ[K] M →ₗ[K] M
variable {K M}
namespace OperatorData
variable (D : OperatorData K M)
def response (a b : M) : M →ₗ[K] M :=
  (D.bracket0 a).comp D.star2 - (1 / 2 : K) •
    D.star1.comp ((D.bracket2 a).comp (D.starN.comp ((D.bracket1 b).comp D.star2)))
theorem response_apply (a b x : M) :
    D.response a b x = D.bracket0 a (D.star2 x) - (1 / 2 : K) •
      D.star1 (D.bracket2 a (D.starN (D.bracket1 b (D.star2 x)))) := rfl
/-- Input linearity is derived, not assumed. -/
theorem response_input_add (a b x y : M) :
    D.response a b (x + y) = D.response a b x + D.response a b y :=
  (D.response a b).map_add x y
theorem response_input_smul (a b x : M) (r : K) :
    D.response a b (r • x) = r • D.response a b x :=
  (D.response a b).map_smul r x
theorem response_first_add (a a' b x : M) :
    D.response (a + a') b x = D.response a b x + D.response a' b x := by
  simp only [response_apply, map_add, LinearMap.add_apply]
  module
theorem response_first_smul (a b x : M) (r : K) :
    D.response (r • a) b x = r • D.response a b x := by
  simp only [response_apply, map_smul, LinearMap.smul_apply]
  module
/-- The second parameter is affine; the zero-parameter term is essential. -/
theorem response_second_affine (a b c x : M) (r s : K) :
    D.response a (r • b + s • c) x =
      (1 - r - s) • D.response a 0 x +
        r • D.response a b x + s • D.response a c x := by
  simp only [response_apply, map_add, map_smul, map_zero,
    LinearMap.add_apply, LinearMap.smul_apply, LinearMap.zero_apply]
  module
/-- Six parameter probes extend to the generated parameter family. -/
theorem response_parameter_extension (E : OperatorData K M) (f f' b b' x : M)
    (h00 : D.response f 0 x = E.response f 0 x)
    (h01 : D.response f b x = E.response f b x)
    (h02 : D.response f b' x = E.response f b' x)
    (h10 : D.response f' 0 x = E.response f' 0 x)
    (h11 : D.response f' b x = E.response f' b x)
    (h12 : D.response f' b' x = E.response f' b' x)
    (α β γ δ : K) :
    D.response (α • f + β • f') (γ • b + δ • b') x =
      E.response (α • f + β • f') (γ • b + δ • b') x := by
  simp only [response_first_add, response_first_smul, response_second_affine,
    h00, h01, h02, h10, h11, h12]
/-- Conditional on the actual degree-specific Hodge signs. Geometric parity
and the validity of these hypotheses are not asserted here. -/
theorem hodge_reparametrization (E : OperatorData K M)
    (h2 : E.star2 = D.star2) (hN : E.starN = D.starN)
    (h1 : E.star1 = -D.star1)
    (hb0 : E.bracket0 = D.bracket0) (hb1 : E.bracket1 = D.bracket1)
    (hb2 : E.bracket2 = D.bracket2) (a b x : M) :
    E.response a b x = D.response a (-b) x := by
  simp [response_apply, h2, hN, h1, hb0, hb1, hb2]
/-- Closure under the three stars and brackets implies response closure. -/
theorem response_mem (S : Submodule K M)
    (hs2 : ∀ x ∈ S, D.star2 x ∈ S)
    (hsN : ∀ x ∈ S, D.starN x ∈ S)
    (hs1 : ∀ x ∈ S, D.star1 x ∈ S)
    (hb0 : ∀ a ∈ S, ∀ b ∈ S, D.bracket0 a b ∈ S)
    (hb1 : ∀ a ∈ S, ∀ b ∈ S, D.bracket1 a b ∈ S)
    (hb2 : ∀ a ∈ S, ∀ b ∈ S, D.bracket2 a b ∈ S)
    {a b x : M} (ha : a ∈ S) (hb : b ∈ S) (hx : x ∈ S) :
    D.response a b x ∈ S := by
  rw [response_apply]
  exact S.sub_mem (hb0 a ha _ (hs2 x hx))
    (S.smul_mem _ (hs1 _ (hb2 a ha _ (hsN _ (hb1 b hb _ (hs2 x hx))))))
/-- In the application f is Clifford conjugation. Its compatibility with all
operations still needs a concrete proof. -/
theorem response_covariant (f : M →ₗ[K] M)
    (hs2 : ∀ x, f (D.star2 x) = D.star2 (f x))
    (hsN : ∀ x, f (D.starN x) = D.starN (f x))
    (hs1 : ∀ x, f (D.star1 x) = D.star1 (f x))
    (hb0 : ∀ a b, f (D.bracket0 a b) = D.bracket0 (f a) (f b))
    (hb1 : ∀ a b, f (D.bracket1 a b) = D.bracket1 (f a) (f b))
    (hb2 : ∀ a b, f (D.bracket2 a b) = D.bracket2 (f a) (f b))
    (a b x : M) : f (D.response a b x) = D.response (f a) (f b) (f x) := by
  simp only [response_apply, map_sub, map_smul, hs1, hs2, hsN, hb0, hb1, hb2]
/-- Infinitesimal equivariance by composition; no group integration claim. -/
theorem response_derivation (d : M →ₗ[K] M)
    (hs2 : ∀ x, d (D.star2 x) = D.star2 (d x))
    (hsN : ∀ x, d (D.starN x) = D.starN (d x))
    (hs1 : ∀ x, d (D.star1 x) = D.star1 (d x))
    (hb0 : ∀ a b, d (D.bracket0 a b) =
      D.bracket0 (d a) b + D.bracket0 a (d b))
    (hb1 : ∀ a b, d (D.bracket1 a b) =
      D.bracket1 (d a) b + D.bracket1 a (d b))
    (hb2 : ∀ a b, d (D.bracket2 a b) =
      D.bracket2 (d a) b + D.bracket2 a (d b))
    {a b : M} (ha : d a = 0) (hb : d b = 0) (x : M) :
    d (D.response a b x) = D.response a b (d x) := by
  simp only [response_apply, map_sub, map_smul, hs1, hs2, hsN, hb0, hb1, hb2,
    ha, hb, map_zero, LinearMap.zero_apply, zero_add]
end OperatorData
/-- Does not certify the spanning property of a particular KN family. -/
theorem linear_eq_of_spanning {N : Type*} [AddCommGroup N] [Module K N] (s : Set M) (hspan : Submodule.span K s = ⊤)
    (f g : M →ₗ[K] N) (h : ∀ x ∈ s, f x = g x) : f = g := by
  apply LinearMap.ext
  intro x
  have hx : x ∈ Submodule.span K s := by rw [hspan]; trivial
  induction hx using Submodule.span_induction with
  | mem x hx => exact h x hx
  | zero => simp
  | add x y hx hy ihx ihy => simp [ihx, ihy]
  | smul a x hx ih => simp [ih]

section AdjointAlgebra
variable {A : Type*} [Ring A] [StarRing A]

/-- The skew-adjoint elements are closed under the coefficient commutator.
The abstract star must be instantiated as X ↦ A⁻¹ X† A in the application. -/
theorem commutator_skew {x y : A} (hx : star x = -x) (hy : star y = -y) :
    star (x * y - y * x) = -(x * y - y * x) := by
  simp only [star_sub, star_mul, hx, hy]
  noncomm_ring

/-- Closure under i times the anticommutator uses a central skew-adjoint i.
The equation i² = -1 is unnecessary for this closure statement. -/
theorem imaginary_anticommutator_skew {i x y : A}
    (hi : star i = -i) (hic : ∀ z : A, i * z = z * i)
    (hx : star x = -x) (hy : star y = -y) :
    star (i * (x * y + y * x)) = -(i * (x * y + y * x)) := by
  calc
    star (i * (x * y + y * x)) = (y * x + x * y) * (-i) := by
      simp only [star_mul, star_add, hi, hx, hy, neg_mul_neg]
    _ = -(i * (x * y + y * x)) := by
      rw [mul_neg, ← hic]
      noncomm_ring

omit [StarRing A] in
/-- The inner commutator is a derivation of the associative product. -/
theorem inner_derivation_product (d x y : A) :
    d * (x * y) - (x * y) * d =
      (d * x - x * d) * y + x * (d * y - y * d) := by
  noncomm_ring

end AdjointAlgebra

section Conjugation
variable {A : Type*} [Ring A]

/-- Right-convention conjugation, matching c_h(x) = h⁻¹ x h. -/
def unitConjugate (h : Aˣ) (x : A) : A := (↑h⁻¹ : A) * x * ↑h

theorem unitConjugate_mul (h : Aˣ) (x y : A) :
    unitConjugate h (x * y) = unitConjugate h x * unitConjugate h y := by
  simp [unitConjugate, mul_assoc]

theorem unitConjugate_add (h : Aˣ) (x y : A) :
    unitConjugate h (x + y) = unitConjugate h x + unitConjugate h y := by
  simp [unitConjugate, mul_add, add_mul]

theorem unitConjugate_sub (h : Aˣ) (x y : A) :
    unitConjugate h (x - y) = unitConjugate h x - unitConjugate h y := by
  simp [unitConjugate, mul_sub, sub_mul]

/-- This is precisely the dressing composition (εh)⁻¹ x (εh). -/
theorem unitConjugate_composition (ε h : Aˣ) (x : A) :
    unitConjugate (ε * h) x = unitConjugate h (unitConjugate ε x) := by
  simp [unitConjugate, mul_assoc]

theorem unitConjugate_commutator (h : Aˣ) (x y : A) :
    unitConjugate h (x * y - y * x) =
      unitConjugate h x * unitConjugate h y -
        unitConjugate h y * unitConjugate h x := by
  rw [unitConjugate_sub, unitConjugate_mul, unitConjugate_mul]

theorem unitConjugate_central (h : Aˣ) (i : A) (hi : ∀ z : A, i * z = z * i) :
    unitConjugate h i = i := by
  dsimp [unitConjugate]
  rw [mul_assoc, hi]
  simp [← mul_assoc]

theorem unitConjugate_imaginary_anticommutator (h : Aˣ) (i x y : A)
    (hi : ∀ z : A, i * z = z * i) :
    unitConjugate h (i * (x * y + y * x)) =
      i * (unitConjugate h x * unitConjugate h y +
        unitConjugate h y * unitConjugate h x) := by
  rw [unitConjugate_mul, unitConjugate_central h i hi,
    unitConjugate_add, unitConjugate_mul, unitConjugate_mul]
end Conjugation

section NoncommutativeDerivations
variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Actual scalar-linear Clifford-factor conjugation; tensoring with the
identity on forms and verifying star compatibility are separate steps. -/
def unitConjugateLinear (h : Aˣ) : A →ₗ[R] A where
  toFun := unitConjugate h
  map_add' := unitConjugate_add h
  map_smul' := by
    intro r x
    simp [unitConjugate]

/-- An associative derivation for a possibly noncommutative algebra.
Mathlib v4.24.0 `RingTheory/Derivation/Basic.lean` requires `CommSemiring A`
for its `Derivation`; its documented future work is bimodule generalization.
This small structure states the actual noncommutative product rule, and does
not assume either of the bracket derivation rules proved below. -/
structure AssociativeDerivation where
  linear : A →ₗ[R] A
  product_rule : ∀ x y, linear (x * y) = linear x * y + x * linear y

namespace AssociativeDerivation
variable (d : AssociativeDerivation (R := R) (A := A))

theorem commutator_rule (x y : A) :
    d.linear (x * y - y * x) =
      (d.linear x * y - y * d.linear x) + (x * d.linear y - d.linear y * x) := by
  rw [map_sub, d.product_rule, d.product_rule]
  noncomm_ring

/-- Centrality of i is not needed for this Leibniz consequence; d(i)=0 suffices. -/
theorem imaginary_anticommutator_rule (i x y : A) (hi : d.linear i = 0) :
    d.linear (i * (x * y + y * x)) =
      i * (d.linear x * y + y * d.linear x) +
        i * (x * d.linear y + d.linear y * x) := by
  rw [d.product_rule, hi, zero_mul, zero_add, map_add,
    d.product_rule, d.product_rule]
  noncomm_ring

/-- Scalar linearity makes every scalar imaginary unit constant for d. -/
theorem scalar_killed (r : R) : d.linear (algebraMap R A r) = 0 := by
  have h := d.product_rule 1 1
  have h1 : d.linear 1 = 0 := by
    simp only [one_mul, mul_one] at h
    exact (add_eq_right).mp h.symm
  rw [Algebra.algebraMap_eq_smul_one, map_smul, h1, smul_zero]

/-- The Clifford commutator d_X(a) = Xa-aX is an actual associative derivation. -/
def inner (z : A) : AssociativeDerivation (R := R) (A := A) where
  linear :=
    { toFun := fun x => z * x - x * z
      map_add' := by intro x y; noncomm_ring
      map_smul' := by
        intro r x
        simp only [RingHom.id_apply, mul_smul_comm, smul_mul_assoc, smul_sub] }
  product_rule := by intro x y; exact inner_derivation_product z x y

/-- A central coefficient is constant under every inner derivation. -/
theorem inner_kills_central (z i : A) (hi : ∀ x : A, i * x = x * i) :
    (inner (R := R) z).linear i = 0 := by
  change z * i - i * z = 0
  rw [hi, sub_self]
end AssociativeDerivation
end NoncommutativeDerivations

section GeneratedGroup
variable {G : Type*} [Group G]

/-- The elements intertwining a fixed linear response form a subgroup.
This proves the algebraic subgroup step of `experiments/B02/proofs.md`,
"From the generators to the group", without a Lie-theory assumption. -/
def equivariantSubgroup (ρ : G →* (M ≃ₗ[K] M)) (L : M →ₗ[K] M) : Subgroup G where
  carrier := {g | ∀ x, L (ρ g x) = ρ g (L x)}
  one_mem' := by intro x; simp
  mul_mem' := by
    intro a b ha hb x
    simp only [map_mul, LinearEquiv.mul_apply]
    rw [ha, hb]
  inv_mem' := by
    intro a ha x
    have hinv (y : M) : ρ a (ρ a⁻¹ y) = y := by
      calc
        ρ a (ρ a⁻¹ y) = (ρ a * ρ a⁻¹) y := rfl
        _ = ρ (a * a⁻¹) y := by rw [map_mul]
        _ = y := by simp
    apply (ρ a).injective
    rw [hinv]
    have h := ha (ρ a⁻¹ x)
    rw [hinv] at h
    exact h.symm

/-- Conditional group-level extension via `Subgroup.closure_le` from
Mathlib/Algebra/Group/Subgroup/Lattice.lean. For the Spin₀ application,
`exponential_generators` denotes the chosen exponentials. BOTH Lie-theoretic
inputs from `experiments/B02/proofs.md`, "From the generators to the group",
remain explicit hypotheses: they generate the group, and infinitesimal
commutation integrates to commutation with each chosen exponential. Neither
analytic integration nor exponential generation of Spin₀ is proved here. -/
theorem equivariant_of_exponential_generators
    (ρ : G →* (M ≃ₗ[K] M)) (L : M →ₗ[K] M) (exponential_generators : Set G)
    (exponentials_generate : Subgroup.closure exponential_generators = ⊤)
    (commutes_with_exponentials : ∀ g ∈ exponential_generators,
      ∀ x, L (ρ g x) = ρ g (L x)) (g : G) (x : M) :
    L (ρ g x) = ρ g (L x) := by
  have hle : Subgroup.closure exponential_generators ≤ equivariantSubgroup ρ L :=
    (Subgroup.closure_le (equivariantSubgroup ρ L)).2 commutes_with_exponentials
  have hg : g ∈ Subgroup.closure exponential_generators := by
    rw [exponentials_generate]
    trivial
  exact hle hg x
end GeneratedGroup
end B02.Structural








