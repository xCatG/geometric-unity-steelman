import B02.Samples

/-!
# Two-dimensional nonuniqueness with the actual contractions and embedding

This exhibits one nonzero algebraic-curvature response with two distinct
(c,kappa) descriptions. It does not assert failure of uniqueness in dimension
four, or extend a one-curvature test to arbitrary curvature tensors.
The sparse canonical-equality certificates use native_decide (Lean.ofReduceBool
and Lean.trustCompiler); the contractions and curvature symmetries use kernel
decide. The response theorem imported from Samples has the same native boundary.
-/
namespace B02.DimensionTwo
open B02.Concrete B02.Samples

abbrev Tensor (n : ℕ) := Fin n → Fin n → ℚ

/-- Covariant metric components in the diagonal orthonormal basis. -/
def metricTensor (eta : Fin n → ℤ) : Tensor n :=
  fun a b => if a = b then eta a else 0

/-- The exact contraction Ric_bd = sum_a eta_a R_ab ad. -/
def ricci (eta : Fin n → ℤ) (R : Curvature n) : Tensor n :=
  fun b d => ∑ a : Fin n, (eta a : ℚ) * R a b a d

/-- Scalar curvature S = sum_b eta_b Ric_bb. -/
def scalar (eta : Fin n → ℤ) (R : Curvature n) : ℚ :=
  ∑ b : Fin n, (eta b : ℚ) * ricci eta R b b

/-- The `embed_tensor` formula in gu/shiab.py at alpha=1, beta=0:
E_F(H) = sum_ab e^a ⊗ eta_b H_ab G_b. -/
def embedF (eta : Fin n → ℤ) (H : Tensor n) : Element n :=
  clean ((List.finRange n).flatMap fun a => (List.finRange n).map fun b =>
    ⟨{a}, {b}, rational ((eta b : ℚ) * H a b)⟩)

def curvature : Curvature 2 := constantCurvature eta11

def predicted (c kappa : ℚ) : Element 2 :=
  scale (embedF eta11 fun a b =>
    ricci eta11 curvature a b - kappa * scalar eta11 curvature * metricTensor eta11 a b)
    (rational c)

set_option maxRecDepth 100000
set_option maxHeartbeats 8000000

/-- The nonzero sectional component fixes the curvature convention. -/
theorem sectional_component : curvature 0 1 0 1 = -1 := by decide +kernel

/-- All algebraic-curvature symmetries hold for the actual witness. -/
theorem curvature_is_algebraic : ∀ a b c d : Fin 2,
    curvature a b c d = -curvature b a c d ∧
    curvature a b c d = -curvature a b d c ∧
    curvature a b c d = curvature c d a b ∧
    curvature a b c d + curvature a c d b + curvature a d b c = 0 := by decide +kernel

/-- For this exact tensor, Ric is the covariant metric, not an assumed matrix. -/
theorem ricci_is_metric : ∀ b d : Fin 2,
    ricci eta11 curvature b d = metricTensor eta11 b d := by decide +kernel

theorem scalar_is_two : scalar eta11 curvature = 2 := by decide +kernel

/-- Explicitly checks the index-raising factor in the embedding. -/
theorem embedded_metric :
    canonical (embedF eta11 (metricTensor eta11)) = canonical (phiF 2) := by native_decide

theorem description_kappa_zero :
    canonical (response eta11 .C .C .C) = canonical (predicted (-1) 0) := by
  rw [dimension_two_CCC]
  native_decide

theorem description_kappa_one :
    canonical (response eta11 .C .C .C) = canonical (predicted 1 1) := by
  rw [dimension_two_CCC]
  native_decide

theorem response_nonzero : canonical (response eta11 .C .C .C) ≠ [] := by
  rw [dimension_two_CCC]
  native_decide

/-- The same nonzero concrete response admits kappa=0 with c=-1 AND kappa=1
with c=1, using actual Ric, S and E_F. Both scale factors are nonzero. -/
theorem nonunique_parameter_descriptions :
    canonical (response eta11 .C .C .C) = canonical (predicted (-1) 0) ∧
    canonical (response eta11 .C .C .C) = canonical (predicted 1 1) ∧
    (0 : ℚ) ≠ 1 ∧ (-1 : ℚ) ≠ 0 ∧ (1 : ℚ) ≠ 0 ∧
    canonical (response eta11 .C .C .C) ≠ [] := by
  exact ⟨description_kappa_zero, description_kappa_one, by decide,
    by decide, by decide, response_nonzero⟩

end B02.DimensionTwo

