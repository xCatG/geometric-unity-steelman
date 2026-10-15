import B02.Structural
import Mathlib.Analysis.Normed.Algebra.Exponential

namespace B02

/-- Commutation with a fixed response is closed under the Lie bracket. -/
theorem commutation_lie_closed {A : Type*} [Ring A] (L X Y : A)
    (hX : Commute L X) (hY : Commute L Y) :
    Commute L (X * Y - Y * X) :=
  (hX.mul_right hY).sub_right (hY.mul_right hX)

/-- The analytic integration step, using Mathlib's proved power-series theorem.
This can be instantiated in the finite-dimensional algebra of continuous
endomorphisms. Identification of rho(exp X) with exp(d rho X) is still a
representation-theoretic hypothesis; it is NOT silently asserted here. -/
theorem commutation_exponential {A : Type*} [Ring A] [Algebra ℝ A]
    [TopologicalSpace A] [IsTopologicalRing A] [T2Space A]
    (L X : A) (h : Commute L X) : Commute L (NormedSpace.exp ℝ X) :=
  h.exp_right ℝ

/-- Invariants are closed under commutators of infinitesimal operators. -/
theorem invariant_lie_closed {K M : Type*} [Field K] [AddCommGroup M] [Module K M]
    (X Y : M →ₗ[K] M) (p : M) (hX : X p = 0) (hY : Y p = 0) :
    (X.comp Y - Y.comp X) p = 0 := by
  simp [hX, hY]

end B02
