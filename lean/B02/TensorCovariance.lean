import B02.TensorDerivation

/-! Tensor-factor covariance for actual algebraic conjugation.
The constructions use arbitrary associative algebras, with no commutativity
assumption on either factor. Identifying these tensor algebras with the executable
sparse exterior/Clifford model is a separate connection obligation. -/
namespace B02.Structural
open scoped TensorProduct

section TensorAlgebras
variable {K A B : Type*} [CommRing K] [Ring A] [Ring B]
  [Algebra K A] [Algebra K B]

/-- Conjugation acts solely on the Clifford/algebra factor. -/
def tensorConjugate (h : Bˣ) : A ⊗[K] B →ₗ[K] A ⊗[K] B :=
  TensorProduct.map LinearMap.id (unitConjugateLinear h)

/-- A form-only operation, including any linear Hodge map. -/
def tensorFormMap (H : A →ₗ[K] A) : A ⊗[K] B →ₗ[K] A ⊗[K] B :=
  TensorProduct.map H LinearMap.id

@[simp] theorem tensorConjugate_tmul (h : Bˣ) (a : A) (b : B) :
    tensorConjugate h (a ⊗ₜ[K] b) = a ⊗ₜ[K] unitConjugate h b := by
  simp [tensorConjugate, unitConjugateLinear]

@[simp] theorem tensorFormMap_tmul (H : A →ₗ[K] A) (a : A) (b : B) :
    tensorFormMap H (a ⊗ₜ[K] b) = H a ⊗ₜ[K] b := by
  simp [tensorFormMap]

/-- Actual factor separation proves star/conjugation commutation on ALL tensors. -/
theorem tensorConjugate_formMap (h : Bˣ) (H : A →ₗ[K] A) (x : A ⊗[K] B) :
    tensorConjugate h (tensorFormMap H x) = tensorFormMap H (tensorConjugate h x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp
  | add x y hx hy => simp [hx, hy]

/-- Dressing composition on all tensors, with the right-convention order. -/
theorem tensorConjugate_composition (ε h : Bˣ) (x : A ⊗[K] B) :
    tensorConjugate (ε * h) x = tensorConjugate h (tensorConjugate ε x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp [unitConjugate_composition]
  | add x y hx hy => simp [hx, hy]

theorem componentC_covariance (h : Bˣ) (a b : A) (x y : B) :
    tensorConjugate h (componentC (K := K) a x b y) =
      componentC (K := K) a (unitConjugate h x) b (unitConjugate h y) := by
  simp only [componentC, tensorConjugate_tmul, unitConjugate_commutator]

theorem componentA_covariance (h : Bˣ) (i : K) (a b : A) (x y : B) :
    tensorConjugate h (componentA i a x b y) =
      componentA i a (unitConjugate h x) b (unitConjugate h y) := by
  simp only [componentA, map_smul, tensorConjugate_tmul,
    unitConjugate_add, unitConjugate_mul]

/-- Full bilinear coefficient commutator: the form order is always a*b,
even in the reversed Clifford product. -/
def tensorBracketC : A ⊗[K] B →ₗ[K] A ⊗[K] B →ₗ[K] A ⊗[K] B :=
  TensorProduct.map₂ (LinearMap.mul K A)
    (LinearMap.mul K B - (LinearMap.mul K B).flip)

/-- Full bilinear scalar-i anticommutator with the same ungraded form order. -/
def tensorBracketA (i : K) : A ⊗[K] B →ₗ[K] A ⊗[K] B →ₗ[K] A ⊗[K] B :=
  i • TensorProduct.map₂ (LinearMap.mul K A)
    (LinearMap.mul K B + (LinearMap.mul K B).flip)

@[simp] theorem tensorBracketC_tmul (a b : A) (x y : B) :
    tensorBracketC (a ⊗ₜ[K] x) (b ⊗ₜ[K] y) = componentC (K := K) a x b y := by
  simp [tensorBracketC, componentC]

@[simp] theorem tensorBracketA_tmul (i : K) (a b : A) (x y : B) :
    tensorBracketA i (a ⊗ₜ[K] x) (b ⊗ₜ[K] y) = componentA i a x b y := by
  simp [tensorBracketA, componentA]

/-- Pure tensor covariance extends to every tensor by actual bilinearity. -/
theorem tensorBracketC_covariance (h : Bˣ) (x y : A ⊗[K] B) :
    tensorConjugate h (tensorBracketC x y) =
      tensorBracketC (tensorConjugate h x) (tensorConjugate h y) := by
  induction x using TensorProduct.induction_on generalizing y with
  | zero => simp
  | tmul a b =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul c e => simp [componentC_covariance]
    | add y z hy hz => simp only [map_add, hy, hz]
  | add x z hx hz => simp only [map_add, LinearMap.add_apply, hx, hz]

theorem tensorBracketA_covariance (h : Bˣ) (i : K) (x y : A ⊗[K] B) :
    tensorConjugate h (tensorBracketA i x y) =
      tensorBracketA i (tensorConjugate h x) (tensorConjugate h y) := by
  induction x using TensorProduct.induction_on generalizing y with
  | zero => simp
  | tmul a b =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul c e => simp [componentA_covariance]
    | add y z hy hz => simp only [map_add, hy, hz]
  | add x z hx hz => simp only [map_add, LinearMap.add_apply, hx, hz]

/-- false selects C, true selects scalar-i A. Three independent booleans
therefore represent exactly the eight bracket assignments of equation (9.3). -/
def tensorBracket (i : K) (symmetric : Bool) :
    A ⊗[K] B →ₗ[K] A ⊗[K] B →ₗ[K] A ⊗[K] B :=
  if symmetric then tensorBracketA i else tensorBracketC

theorem tensorBracket_covariance (h : Bˣ) (i : K) (symmetric : Bool)
    (x y : A ⊗[K] B) :
    tensorConjugate h (tensorBracket i symmetric x y) =
      tensorBracket i symmetric (tensorConjugate h x) (tensorConjugate h y) := by
  cases symmetric
  · exact tensorBracketC_covariance h x y
  · exact tensorBracketA_covariance h i x y


/-- Full ungraded C derivation rule, extended from the proved pure components. -/
theorem tensorBracketC_derivation
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (x y : A ⊗[K] B) :
    tensorDerivationMap dA dB (tensorBracketC x y) =
      tensorBracketC (tensorDerivationMap dA dB x) y +
        tensorBracketC x (tensorDerivationMap dA dB y) := by
  induction x using TensorProduct.induction_on generalizing y with
  | zero => simp
  | tmul a b =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul c e =>
      simp only [tensorBracketC_tmul, componentC_derivation, tensorDerivationMap_tmul,
        map_add, LinearMap.add_apply, tensorBracketC_tmul]
      abel
    | add y z hy hz =>
      simp only [map_add, hy, hz]
      abel
  | add x z hx hz =>
    simp only [map_add, LinearMap.add_apply, hx, hz]
    abel

/-- Full scalar-i A derivation rule with the same form order on both products. -/
theorem tensorBracketA_derivation
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (i : K) (x y : A ⊗[K] B) :
    tensorDerivationMap dA dB (tensorBracketA i x y) =
      tensorBracketA i (tensorDerivationMap dA dB x) y +
        tensorBracketA i x (tensorDerivationMap dA dB y) := by
  induction x using TensorProduct.induction_on generalizing y with
  | zero => simp
  | tmul a b =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul c e =>
      simp only [tensorBracketA_tmul, componentA_derivation, tensorDerivationMap_tmul,
        map_add, LinearMap.add_apply, tensorBracketA_tmul]
      abel
    | add y z hy hz =>
      simp only [map_add, hy, hz]
      abel
  | add x z hx hz =>
    simp only [map_add, LinearMap.add_apply, hx, hz]
    abel

theorem tensorBracket_derivation
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (i : K) (symmetric : Bool)
    (x y : A ⊗[K] B) :
    tensorDerivationMap dA dB (tensorBracket i symmetric x y) =
      tensorBracket i symmetric (tensorDerivationMap dA dB x) y +
        tensorBracket i symmetric x (tensorDerivationMap dA dB y) := by
  cases symmetric
  · exact tensorBracketC_derivation dA dB x y
  · exact tensorBracketA_derivation dA dB i x y

/-- Form-factor commutation lifts to the sum of both actual factor derivations.
Only the geometric form-star commutation is a hypothesis; the Clifford-factor
part follows automatically from factor separation. -/
theorem tensorDerivation_formMap
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (H : A →ₗ[K] A)
    (hH : ∀ a, dA.linear (H a) = H (dA.linear a)) (x : A ⊗[K] B) :
    tensorDerivationMap dA dB (tensorFormMap H x) =
      tensorFormMap H (tensorDerivationMap dA dB x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp [hH]
  | add x y hx hy => simp [hx, hy]

end TensorAlgebras

section TensorResponse
variable {K A B : Type*} [Field K] [Ring A] [Ring B]
  [Algebra K A] [Algebra K B]

/-- Equation (9.3) instantiated with proved tensor brackets and form-only stars. -/
def tensorOperatorData (i : K) (H2 HN H1 : A →ₗ[K] A) (s0 s1 s2 : Bool) :
    OperatorData K (A ⊗[K] B) where
  star2 := tensorFormMap H2
  starN := tensorFormMap HN
  star1 := tensorFormMap H1
  bracket0 := tensorBracket i s0
  bracket1 := tensorBracket i s1
  bracket2 := tensorBracket i s2

/-- Full tensor covariance: no bracket-preservation or star-compatibility
hypotheses are assumed; they are proved from the factor constructions. -/
theorem tensor_response_covariance (i : K) (H2 HN H1 : A →ₗ[K] A)
    (s0 s1 s2 : Bool) (h : Bˣ) (a b x : A ⊗[K] B) :
    tensorConjugate h ((tensorOperatorData i H2 HN H1 s0 s1 s2).response a b x) =
      (tensorOperatorData i H2 HN H1 s0 s1 s2).response
        (tensorConjugate h a) (tensorConjugate h b) (tensorConjugate h x) := by
  exact (tensorOperatorData i H2 HN H1 s0 s1 s2).response_covariant
    (tensorConjugate h) (tensorConjugate_formMap h H2)
    (tensorConjugate_formMap h HN) (tensorConjugate_formMap h H1)
    (tensorBracket_covariance h i s0) (tensorBracket_covariance h i s1)
    (tensorBracket_covariance h i s2) a b x

/-- The full dressed identity Shiab_(εh)(c_h x)=c_h(Shiab_ε x),
for arbitrary units ε,h, arbitrary tensor inputs and all eight assignments.
No equivariance hypotheses on the undressed parameters are required. -/
theorem tensor_dressed_covariance (i : K) (H2 HN H1 : A →ₗ[K] A)
    (s0 s1 s2 : Bool) (ε h : Bˣ) (a b x : A ⊗[K] B) :
    (tensorOperatorData i H2 HN H1 s0 s1 s2).response
        (tensorConjugate (ε * h) a) (tensorConjugate (ε * h) b) (tensorConjugate h x) =
      tensorConjugate h ((tensorOperatorData i H2 HN H1 s0 s1 s2).response
        (tensorConjugate ε a) (tensorConjugate ε b) x) := by
  rw [tensorConjugate_composition, tensorConjugate_composition]
  exact (tensor_response_covariance i H2 HN H1 s0 s1 s2 h
    (tensorConjugate ε a) (tensorConjugate ε b) x).symm


/-- Steps 1 and 4 for the actual tensor algebra and all eight assignments.
The remaining geometric hypotheses are explicit: the form derivation commutes
with the three chosen Hodge maps and both parameter tensors are invariant.
No bracket-derivation or full-response-equivariance hypothesis is assumed. -/
theorem tensor_response_derivation
    (i : K) (H2 HN H1 : A →ₗ[K] A) (s0 s1 s2 : Bool)
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B))
    (hH2 : ∀ a, dA.linear (H2 a) = H2 (dA.linear a))
    (hHN : ∀ a, dA.linear (HN a) = HN (dA.linear a))
    (hH1 : ∀ a, dA.linear (H1 a) = H1 (dA.linear a))
    {a b : A ⊗[K] B} (ha : tensorDerivationMap dA dB a = 0)
    (hb : tensorDerivationMap dA dB b = 0) (x : A ⊗[K] B) :
    tensorDerivationMap dA dB ((tensorOperatorData i H2 HN H1 s0 s1 s2).response a b x) =
      (tensorOperatorData i H2 HN H1 s0 s1 s2).response a b (tensorDerivationMap dA dB x) := by
  exact (tensorOperatorData i H2 HN H1 s0 s1 s2).response_derivation
    (tensorDerivationMap dA dB) (tensorDerivation_formMap dA dB H2 hH2)
    (tensorDerivation_formMap dA dB HN hHN) (tensorDerivation_formMap dA dB H1 hH1)
    (tensorBracket_derivation dA dB i s0) (tensorBracket_derivation dA dB i s1)
    (tensorBracket_derivation dA dB i s2) ha hb x

end TensorResponse
end B02.Structural

#print axioms B02.Structural.tensor_dressed_covariance


#print axioms B02.Structural.tensor_response_derivation


