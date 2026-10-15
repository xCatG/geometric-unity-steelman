import B02.Structural

namespace B02
open scoped BigOperators

/-- The finite-rank sandwich in the prose. The modular-to-rational lower bound
is an input certificate, not an unverified call to a modular rank program. -/
theorem rank_sandwich (modularRank rationalRank ambientDimension : ℕ)
    (modular_le_rational : modularRank ≤ rationalRank)
    (rational_le_ambient : rationalRank ≤ ambientDimension)
    (outer_equal : modularRank = ambientDimension) :
    rationalRank = ambientDimension := by omega

/-- Once the lower rank certificate reaches ambient dimension, spanning follows.
For B02 at n=14, use r=3185 and explicitly supply the recorded rank certificate
and the dimension of the algebraic-curvature space. Row membership is enforced
by typing each member of s in V, the algebraic-curvature space itself. -/
theorem span_eq_top_of_rank_certificate {K V : Type*} [Field K]
    [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    (s : Set V) (r : ℕ)
    (modular_rank_lower_bound : r ≤ Module.finrank K (Submodule.span K s))
    (algebraic_curvature_dimension : Module.finrank K V = r) :
    Submodule.span K s = ⊤ := by
  apply Submodule.eq_top_of_finrank_eq
  exact le_antisymm (Submodule.finrank_le _) (by
    rw [algebraic_curvature_dimension]; exact modular_rank_lower_bound)

/-- Conditional extension from a rank-certified spanning family. Neither the
3185 computation nor scalar extension Q→R is silently assumed to be proved. -/
theorem curvature_extension {K V W : Type*} [Field K]
    [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    [AddCommGroup W] [Module K W]
    (s : Set V) (r : ℕ)
    (modular_rank_lower_bound : r ≤ Module.finrank K (Submodule.span K s))
    (algebraic_curvature_dimension : Module.finrank K V = r)
    (lhs rhs : V →ₗ[K] W) (basis_checks : ∀ x ∈ s, lhs x = rhs x) :
    lhs = rhs := by
  apply B02.Structural.linear_eq_of_spanning s
    (span_eq_top_of_rank_certificate s r modular_rank_lower_bound algebraic_curvature_dimension)
  exact basis_checks

/-- Dimension arithmetic, NOT a proof that the curvature space has this dimension. -/
theorem curvature_dimension_numerals :
    4^2 * (4^2 - 1) / 12 = (20 : ℕ) ∧
    14^2 * (14^2 - 1) / 12 = (3185 : ℕ) := by norm_num



/-- Rational spanning extends to real spanning in the genuine tensor scalar extension. -/
theorem rational_span_extends_to_real {V : Type*} [AddCommGroup V] [Module ℚ V]
    (s : Set V) (hs : Submodule.span ℚ s = ⊤) :
    Submodule.span ℝ (TensorProduct.mk ℚ ℝ V 1 '' s) = ⊤ := by
  have h := congrArg (fun p : Submodule ℚ V => p.baseChange ℝ) hs
  simpa using h

/-- The rational rank certificate carries the identity to scalar-extended real
curvature. An identification with a concrete real curvature coordinate space
must still be supplied separately; this is not asserted by the theorem. -/
theorem real_scalar_extension_identity {V W : Type*} [AddCommGroup V] [Module ℚ V]
    [FiniteDimensional ℚ V] [AddCommGroup W] [Module ℝ W]
    (s : Set V) (r : ℕ)
    (modular_rank_lower_bound : r ≤ Module.finrank ℚ (Submodule.span ℚ s))
    (algebraic_curvature_dimension : Module.finrank ℚ V = r)
    (lhs rhs : TensorProduct ℚ ℝ V →ₗ[ℝ] W)
    (basis_checks : ∀ x ∈ s, lhs (TensorProduct.mk ℚ ℝ V 1 x) =
      rhs (TensorProduct.mk ℚ ℝ V 1 x)) : lhs = rhs := by
  apply B02.Structural.linear_eq_of_spanning (TensorProduct.mk ℚ ℝ V 1 '' s)
    (rational_span_extends_to_real s
      (span_eq_top_of_rank_certificate s r modular_rank_lower_bound algebraic_curvature_dimension))
  intro y hy
  obtain ⟨x, hx, rfl⟩ := hy
  exact basis_checks x hx

end B02
