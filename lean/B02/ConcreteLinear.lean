import B02.Bilinearity
import B02.Structural

namespace B02.Concrete
open scoped BigOperators
abbrev Coefficients (n : ℕ) := Blade n → Blade n → GQ

def denote (x : Element n) : Coefficients n := coefficient x

def starLinear (eta : Fin n → ℤ) : Coefficients n →ₗ[ℚ] Coefficients n where
  toFun x f b := x fᶜ b * integer (starSign eta fᶜ)
  map_add' := by intro x y; funext f b; simp [add_mul]
  map_smul' := by intro r x; funext f b; simp

def coefficientBracket (eta : Fin n → ℤ) (m : Mode) (x y : Coefficients n) : Coefficients n :=
  fun f b => ∑ f1, ∑ b1, ∑ f2, ∑ b2,
    x f1 b1 * y f2 b2 * bracketKernel eta m f1 b1 f2 b2 f b

def bracketLinear (eta : Fin n → ℤ) (m : Mode) :
    Coefficients n →ₗ[ℚ] Coefficients n →ₗ[ℚ] Coefficients n where
  toFun x :=
    { toFun := coefficientBracket eta m x
      map_add' := by
        intro y z; funext f b
        simp [coefficientBracket, mul_add, add_mul, Finset.sum_add_distrib]
      map_smul' := by
        intro r y; funext f b
        simp [coefficientBracket, Finset.smul_sum] }
  map_add' := by
    intro x y; apply LinearMap.ext; intro z; funext f b
    simp [coefficientBracket, add_mul, Finset.sum_add_distrib]
  map_smul' := by
    intro r x; apply LinearMap.ext; intro z; funext f b
    simp [coefficientBracket, Finset.smul_sum]

/-- The structural operator is instantiated with the actual sparse model's
coefficient maps; linearity is proved above rather than hypothesized. -/
def operatorData (eta : Fin n → ℤ) (m0 m1 m2 : Mode) :
    B02.Structural.OperatorData ℚ (Coefficients n) where
  star2 := starLinear eta
  starN := starLinear eta
  star1 := starLinear eta
  bracket0 := bracketLinear eta m0
  bracket1 := bracketLinear eta m1
  bracket2 := bracketLinear eta m2

@[simp] theorem denote_plus (x y : Element n) : denote (plus x y) = denote x + denote y := by
  funext f b; exact coefficient_plus x y f b

@[simp] theorem denote_scale (x : Element n) (r : ℚ) :
    denote (scale x (rational r)) = r • denote x := by
  funext f b
  rw [denote, coefficient_scale]
  change coefficient x f b * rational r = r • coefficient x f b
  ext <;> simp [rational, smul_eq_mul] <;> ring

@[simp] theorem denote_star (eta : Fin n → ℤ) (x : Element n) :
    denote (star eta x) = starLinear eta (denote x) := by
  funext f b; exact coefficient_star eta x f b

@[simp] theorem denote_bracket (eta : Fin n → ℤ) (m : Mode) (x y : Element n) :
    denote (bracket eta m x y) = bracketLinear eta m (denote x) (denote y) := by
  funext f b; exact coefficient_bracket_finite eta m x y f b

/-- Exact interpretation of Python's sparse Shiab in the proved linear/bilinear data. -/
theorem denote_shiab (eta : Fin n → ℤ) (m0 m1 m2 : Mode) (a b x : Element n) :
    denote (shiab eta m0 m1 m2 a b x) =
      (operatorData eta m0 m1 m2).response (denote a) (denote b) (denote x) := by
  simp only [shiab, denote_plus, denote_scale, denote_star, denote_bracket,
    B02.Structural.OperatorData.response_apply, operatorData]
  module

/-- Concrete parameter extension over the executable Gaussian-rational model. -/
theorem concrete_parameter_affine (eta : Fin n → ℤ) (m0 m1 m2 : Mode)
    (a b c x : Element n) (r s : ℚ) :
    denote (shiab eta m0 m1 m2 a (plus (scale b (rational r)) (scale c (rational s))) x) =
      (1-r-s) • denote (shiab eta m0 m1 m2 a [] x) +
      r • denote (shiab eta m0 m1 m2 a b x) +
      s • denote (shiab eta m0 m1 m2 a c x) := by
  simp only [denote_shiab, denote_plus, denote_scale]
  have hz : denote ([] : Element n) = 0 := by funext f b; simp [denote]
  rw [hz]
  exact (operatorData eta m0 m1 m2).response_second_affine _ _ _ _ r s




/-- The six-probe parameter interpolation formula, directly for executable Shiab. -/
theorem concrete_six_probe_formula (eta : Fin n → ℤ) (m0 m1 m2 : Mode)
    (f f' b b' x : Element n) (α β γ δ : ℚ) :
    denote (shiab eta m0 m1 m2
      (plus (scale f (rational α)) (scale f' (rational β)))
      (plus (scale b (rational γ)) (scale b' (rational δ))) x) =
    α • ((1-γ-δ) • denote (shiab eta m0 m1 m2 f [] x) +
      γ • denote (shiab eta m0 m1 m2 f b x) + δ • denote (shiab eta m0 m1 m2 f b' x)) +
    β • ((1-γ-δ) • denote (shiab eta m0 m1 m2 f' [] x) +
      γ • denote (shiab eta m0 m1 m2 f' b x) + δ • denote (shiab eta m0 m1 m2 f' b' x)) := by
  have hz : denote ([] : Element n) = 0 := by funext f b; simp [denote]
  simp only [denote_shiab, denote_plus, denote_scale, hz,
    B02.Structural.OperatorData.response_first_add,
    B02.Structural.OperatorData.response_first_smul,
    B02.Structural.OperatorData.response_second_affine]
  module

/-- Actual input linearity, including the 1/2 normalization of the nested term. -/
theorem concrete_input_linear (eta : Fin n → ℤ) (m0 m1 m2 : Mode)
    (a b x y : Element n) (r s : ℚ) :
    denote (shiab eta m0 m1 m2 a b
      (plus (scale x (rational r)) (scale y (rational s)))) =
    r • denote (shiab eta m0 m1 m2 a b x) +
      s • denote (shiab eta m0 m1 m2 a b y) := by
  simp only [denote_shiab, denote_plus, denote_scale, map_add, map_smul]

end B02.Concrete

