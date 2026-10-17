import B02.Concrete
import Mathlib

namespace B07Argon.Grades
open B02 B02.Concrete
open scoped BigOperators

theorem blade_scalar_support {n : ℕ} (η : Fin n → ℤ) (I J : Blade n) :
    (bladeMul η I J).1 = ∅ ↔ I = J := by
  simp only [bladeMul, Finset.union_eq_empty, Finset.sdiff_eq_empty_iff_subset]
  exact ⟨fun h => Finset.Subset.antisymm h.1 h.2, fun h => by simp [h]⟩

def scalarBlade {n : ℕ} (η : Fin n → ℤ) (I J : Blade n) : ℤ :=
  if (bladeMul η I J).1 = ∅ then (bladeMul η I J).2 else 0

theorem blade_coefficient_ne_zero {n : ℕ} (η : Fin n → ℤ)
    (hη : ∀ i, η i ≠ 0) (I J : Blade n) : (bladeMul η I J).2 ≠ 0 := by
  apply mul_ne_zero
  · have hh := reorderSign_sq I J
    intro hz; rw [hz, zero_mul] at hh; norm_num at hh
  · exact Finset.prod_ne_zero_iff.mpr (fun i _ => hη i)

theorem scalarBlade_ne_zero_iff {n : ℕ} (η : Fin n → ℤ)
    (hη : ∀ i, η i ≠ 0) (I J : Blade n) : scalarBlade η I J ≠ 0 ↔ I = J := by
  rw [scalarBlade]
  by_cases h : I = J
  · simp [blade_scalar_support, h, blade_coefficient_ne_zero η hη]
  · simp [blade_scalar_support, h]

theorem different_grade_scalar_zero {n : ℕ} (η : Fin n → ℤ) (I J : Blade n)
    (h : I.card ≠ J.card) : scalarBlade η I J = 0 := by
  have hij : I ≠ J := fun hh => h (congrArg Finset.card hh)
  simp [scalarBlade, blade_scalar_support, hij]

/-- Scalar part of the bilinear extension of the actual B02 blade product.
Coefficients rational; the same finite-sum proof works over any characteristic-zero field. -/
def scalarPair {n : ℕ} (η : Fin n → ℤ) (x y : Blade n → ℚ) : ℚ :=
  ∑ I, ∑ J, x I * y J * (scalarBlade η I J : ℚ)

theorem scalarPair_different_grades {n : ℕ} (η : Fin n → ℤ) (x y : Blade n → ℚ)
    (j l : ℕ) (hj : ∀ I, I.card ≠ j → x I = 0) (hl : ∀ I, I.card ≠ l → y I = 0)
    (hjl : j ≠ l) : scalarPair η x y = 0 := by
  apply Finset.sum_eq_zero
  intro I _
  apply Finset.sum_eq_zero
  intro J _
  by_cases hi : I.card = j
  · by_cases hJ : J.card = l
    · rw [different_grade_scalar_zero η I J (by omega)]; simp
    · rw [hl J hJ]; ring
  · rw [hj I hi]; ring

section Blocks
variable {B G : Type*} [DecidableEq G]
/-- B can include every form/blade index. M is the paired symbol matrix for a
fixed covector; C1=M+Mᵀ. Derivative symbols preserve internal grade. -/
def C1 (M : B → B → ℚ) (a b : B) : ℚ := M a b + M b a
def pairBlock (grade : B → G) (p q : G) (M : B → B → ℚ) (a b : B) : ℚ :=
  if (grade a = p ∧ grade b = q) ∨ (grade a = q ∧ grade b = p) then M a b else 0

theorem C1_pairBlock (grade : B → G) (p q : G) (M : B → B → ℚ) (a b : B) :
    C1 (pairBlock grade p q M) a b = pairBlock grade p q (C1 M) a b := by
  unfold C1 pairBlock
  by_cases h : (grade a = p ∧ grade b = q) ∨ (grade a = q ∧ grade b = p)
  · have hs : (grade b = p ∧ grade a = q) ∨ (grade b = q ∧ grade a = p) := by tauto
    simp [h, hs]
  · have hs : ¬ ((grade b = p ∧ grade a = q) ∨ (grade b = q ∧ grade a = p)) := by tauto
    simp [h, hs]

theorem C1_splits (grade : B → G) (M : B → B → ℚ) :
    (∀ a b, C1 M a b = 0) ↔ ∀ p q a b, C1 (pairBlock grade p q M) a b = 0 := by
  constructor
  · intro h p q a b
    rw [C1_pairBlock]
    simp [pairBlock, h]
  · intro h a b
    have hh := h (grade a) (grade b) a b
    simpa [C1_pairBlock, pairBlock] using hh

theorem pairBlock_unordered (grade : B → G) (p q : G) (M : B → B → ℚ) :
    pairBlock grade p q M = pairBlock grade q p M := by
  funext a b; simp [pairBlock, or_comm]
end Blocks

/-- The precise missing hypothesis in a bare blade model: an intertwiner must
respect total tensor parity. In 4D, input parity=(-1)^(2+j), output=(-1)^(3+l).
The model alone does NOT prove this equivariance premise for a concrete X. -/
theorem diagonal_block_zero (j : ℕ) (x : ℚ)
    (h : (-1 : ℚ)^(2+j) * x = (-1 : ℚ)^(3+j) * x) : x = 0 := by
  simp only [pow_add] at h
  norm_num at h
  have hn : (-1 : ℚ)^j ≠ 0 := pow_ne_zero _ (by norm_num)
  have hz : (-1 : ℚ)^j * x = 0 := by linarith
  exact (mul_eq_zero.mp hz).resolve_left hn

end B07Argon.Grades
