import B02.Structural
import Mathlib.RingTheory.TensorProduct.Basic

namespace B02.Structural
open scoped TensorProduct
variable {K A B : Type*} [CommRing K] [Ring A] [Ring B]
  [Algebra K A] [Algebra K B]

/-- The sum of the two factor derivations acting on the tensor product. -/
def tensorDerivationMap
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) :
    A ⊗[K] B →ₗ[K] A ⊗[K] B :=
  TensorProduct.map dA.linear LinearMap.id + TensorProduct.map LinearMap.id dB.linear

@[simp] theorem tensorDerivationMap_tmul
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (a : A) (b : B) :
    tensorDerivationMap dA dB (a ⊗ₜ[K] b) =
      dA.linear a ⊗ₜ[K] b + a ⊗ₜ[K] dB.linear b := by
  simp [tensorDerivationMap]

/-- Step 1 on the tensor product, fully proved from the two factor product rules. -/
theorem tensorDerivation_product
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (x y : A ⊗[K] B) :
    tensorDerivationMap dA dB (x * y) =
      tensorDerivationMap dA dB x * y + x * tensorDerivationMap dA dB y := by
  induction x using TensorProduct.induction_on generalizing y with
  | zero => simp
  | tmul a b =>
    induction y using TensorProduct.induction_on with
    | zero => simp
    | tmul c e =>
      simp only [Algebra.TensorProduct.tmul_mul_tmul, tensorDerivationMap_tmul,
        dA.product_rule, dB.product_rule, TensorProduct.add_tmul, TensorProduct.tmul_add,
        add_mul, mul_add]
      abel
    | add y z hy hz =>
      simp only [mul_add, map_add, hy, hz]
      abel
  | add x z hx hz =>
    simp only [add_mul, map_add, hx, hz]
    abel

/-- An actual associative derivation, so both bracket rules apply. The reversed
Clifford product uses the same construction with the opposite Clifford algebra;
the form-factor order is retained exactly as in the source convention. -/
def tensorDerivation
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) :
    AssociativeDerivation (R := K) (A := A ⊗[K] B) where
  linear := tensorDerivationMap dA dB
  product_rule := tensorDerivation_product dA dB



/-- The actual ungraded C bracket on pure form/Clifford factors. -/
def componentC (a : A) (x : B) (b : A) (y : B) : A ⊗[K] B :=
  (a * b) ⊗ₜ[K] (x * y - y * x)

/-- Both terms keep the form order a*b, including the reversed Clifford product. -/
theorem componentC_derivation
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (a b : A) (x y : B) :
    tensorDerivationMap dA dB (componentC a x b y) =
      componentC (dA.linear a) x b y + componentC a (dB.linear x) b y +
      componentC a x (dA.linear b) y + componentC a x b (dB.linear y) := by
  simp only [componentC, tensorDerivationMap_tmul, dA.product_rule,
    dB.commutator_rule, TensorProduct.add_tmul, TensorProduct.tmul_add]
  abel

/-- The i factor is any fixed scalar, so this also works over complex coefficients. -/
def componentA (i : K) (a : A) (x : B) (b : A) (y : B) : A ⊗[K] B :=
  i • ((a * b) ⊗ₜ[K] (x * y + y * x))

theorem componentA_derivation
    (dA : AssociativeDerivation (R := K) (A := A))
    (dB : AssociativeDerivation (R := K) (A := B)) (i : K) (a b : A) (x y : B) :
    tensorDerivationMap dA dB (componentA i a x b y) =
      componentA i (dA.linear a) x b y + componentA i a (dB.linear x) b y +
      componentA i a x (dA.linear b) y + componentA i a x b (dB.linear y) := by
  simp only [componentA, map_smul, tensorDerivationMap_tmul, dA.product_rule,
    map_add, dB.product_rule, TensorProduct.add_tmul, TensorProduct.tmul_add,
    smul_add]
  abel

end B02.Structural
