import B02.Headline
import B02.Volume

/-!
# The B-prime cancellation argument in an associative Clifford model

This proves the complete expanded-basis argument for an associative algebra with a
volume element commuting with the bivector basis. `B02.Concrete.bladeMul_volume_bivector`
separately proves that commutation for the executable Clifford product.
`B02.ConcreteTwistedHeadline` proves the executable B-prime theorem directly from
inversion counts, without requiring an associative-algebra identification.
-/
namespace B02
open scoped BigOperators

/-- Expanded inner bracket with each B bivector right-multiplied by a central twist.
The twist may include any scalar phase, including the phase in B-prime. -/
def expandedTwistedInnerC {n : ℕ} {K A : Type*} [Field K] [Ring A] [Algebra K A]
    (eta : Fin n → ℤ) (R : PairIndex n → PairIndex n → K)
    (G : PairIndex n → A) (z : A) : A :=
  ∑ a, ∑ b, ∑ c,
    ((1/2 : K) * R b c * (metric eta c.val : K) *
      (wedgeStarWeight eta a.val b.val : K)) •
        ((G a * z) * G c - G c * (G a * z))

/-- Centrality moves the B-prime twist through the actual associative commutator. -/
theorem expandedTwistedInnerC_eq {n : ℕ} {K A : Type*}
    [Field K] [Ring A] [Algebra K A]
    (eta : Fin n → ℤ) (R : PairIndex n → PairIndex n → K)
    (G : PairIndex n → A) (z : A) (hz : ∀ a, Commute z (G a)) :
    expandedTwistedInnerC eta R G z =
      expandedInnerC eta R (fun a c => (G a * G c) * z) := by
  unfold expandedTwistedInnerC expandedInnerC
  simp_rw [central_twisted_commutator _ _ z (hz _), sub_mul]

/-- The general B-prime argument: pair symmetry, pinned raising, and central volume
kill the inner commutator. No parity or nondegeneracy assumption is needed here. -/
theorem headline_inner_C_twisted {n : ℕ} {K A : Type*}
    [Field K] [Ring A] [Algebra K A]
    (eta : Fin n → ℤ) (R : PairIndex n → PairIndex n → K)
    (G : PairIndex n → A) (z : A)
    (hR : ∀ a b, R a b = R b a) (hz : ∀ a, Commute z (G a)) :
    expandedTwistedInnerC eta R G z = 0 := by
  rw [expandedTwistedInnerC_eq eta R G z hz]
  exact headline_inner_C eta R (fun a c => (G a * G c) * z) hR

end B02

#print axioms B02.expandedTwistedInnerC_eq
#print axioms B02.headline_inner_C_twisted

