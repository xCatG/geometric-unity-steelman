import B02.Signs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NoncommRing

namespace B02
open scoped BigOperators
abbrev PairIndex (n : ℕ) := {a : Blade n // a.card = 2}

def wedgeStarWeight {n : ℕ} (eta : Fin n → ℤ) (a b : Blade n) : ℤ :=
  if Disjoint a bᶜ then reorderSign a bᶜ * starSign eta b else 0

/-- Equal-degree basis forms pair diagonally under wedge-star. -/
theorem wedgeStarWeight_diagonal {n : ℕ} (eta : Fin n → ℤ)
    (a b : PairIndex n) :
    wedgeStarWeight eta a.val b.val = if a = b then metric eta a.val else 0 := by
  by_cases h : a = b
  · subst b
    have hd : Disjoint a.val a.valᶜ := Finset.disjoint_left.mpr (by
      intro i hi hci; exact (Finset.mem_compl.mp hci) hi)
    simp [wedgeStarWeight, hd, pinned_hodge_weight]
  · have hd : ¬ Disjoint a.val b.valᶜ := by
      intro hd
      have hs : a.val ⊆ b.val := by
        intro i hi
        by_contra hn
        exact Finset.disjoint_left.mp hd hi (by simpa using hn)
      have he : a.val = b.val := Finset.eq_of_subset_of_card_le hs (by simp [a.property, b.property])
      exact h (Subtype.ext he)
    simp [wedgeStarWeight, hd, h]

/-- Symmetric scalar weights kill an antisymmetric double sum, without any division. -/
theorem symmetric_commutator_sum {ι K A : Type*} [Fintype ι]
    [CommRing K] [AddCommGroup A] [Module K A]
    (R : ι → ι → K) (w : ι → K) (P : ι → ι → A)
    (hR : ∀ a b, R a b = R b a) :
    (∑ a, ∑ b, (R a b * w a * w b) • (P a b - P b a)) = 0 := by
  simp_rw [smul_sub]
  simp_rw [Finset.sum_sub_distrib]
  apply sub_eq_zero.mpr
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro a _
  apply Finset.sum_congr rfl
  intro b _
  congr 1
  rw [hR]
  ring

/-- The full basis expansion of [B wedge star xi]_C, before diagonal contraction.
`P a c` is the Clifford product of the increasing blades, with arbitrary target module.
This definition includes the pinned 1/2 and the raised second curvature index pair. -/
def expandedInnerC {n : ℕ} {K A : Type*} [Field K] [AddCommGroup A] [Module K A]
    (eta : Fin n → ℤ) (R : PairIndex n → PairIndex n → K)
    (P : PairIndex n → PairIndex n → A) : A :=
  ∑ a, ∑ b, ∑ c,
    ((1/2 : K) * R b c * (metric eta c.val : K) *
      (wedgeStarWeight eta a.val b.val : K)) • (P a c - P c a)

/-- General-dimensional headline at the expanded-basis level. No Bianchi identity,
nondegeneracy, dimension parity, or signature restriction is needed for B. -/
theorem headline_inner_C {n : ℕ} {K A : Type*} [Field K] [AddCommGroup A] [Module K A]
    (eta : Fin n → ℤ) (R : PairIndex n → PairIndex n → K)
    (P : PairIndex n → PairIndex n → A)
    (hR : ∀ a b, R a b = R b a) : expandedInnerC eta R P = 0 := by
  unfold expandedInnerC
  simp_rw [wedgeStarWeight_diagonal]
  classical
  simp only [Int.cast_ite, Int.cast_zero]
  have hc : ∀ a : PairIndex n,
      (∑ b, ∑ c, ((1 / 2 : K) * R b c * (metric eta c.val : K) *
        (if a = b then (metric eta a.val : K) else 0)) • (P a c - P c a)) =
      ∑ c, ((1 / 2 : K) * R a c * (metric eta c.val : K) *
        (metric eta a.val : K)) • (P a c - P c a) := by
    intro a
    rw [Finset.sum_eq_single a]
    · simp
    · intro b _ hba
      simp [Ne.symm hba]
    · simp
  simp_rw [hc]
  have h := symmetric_commutator_sum (fun a b => (1/2 : K) * R a b)
    (fun a => (metric eta a.val : K)) P (by intro a b; dsimp; rw [hR])
  convert h using 1 <;> congr 1
  funext a
  congr 1
  funext b
  congr 1
  ring

/-- Multiplying the first blade by a central chirality factor commutes through C. -/
theorem central_twisted_commutator {A : Type*} [Ring A]
    (a b z : A) (hz : Commute z b) :
    (a * z) * b - b * (a * z) = (a * b - b * a) * z := by
  rw [mul_assoc a z b, hz.eq, ← mul_assoc a b z]
  noncomm_ring

end B02


