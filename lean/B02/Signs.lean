import Mathlib.Algebra.QuadraticAlgebra
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fintype.Powerset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.NormNum

namespace B02
open scoped BigOperators
abbrev Blade (n : ℕ) := Finset (Fin n)

def reorderSign {n : ℕ} (a b : Blade n) : ℤ :=
  (-1) ^ (∑ i ∈ a, (b.filter (fun j => j < i)).card)

def metric {n : ℕ} (eta : Fin n → ℤ) (a : Blade n) : ℤ :=
  ∏ i ∈ a, eta i

def starSign {n : ℕ} (eta : Fin n → ℤ) (a : Blade n) : ℤ :=
  reorderSign a aᶜ * metric eta a

/-- The sorting sign has square one, at every dimension. -/
theorem reorderSign_sq {n : ℕ} (a b : Blade n) :
    reorderSign a b * reorderSign a b = 1 := by
  unfold reorderSign
  rw [← mul_pow]
  norm_num

/-- Coefficient of e^a wedge star(e^a). No signature or parity restriction. -/
theorem pinned_hodge_weight {n : ℕ} (eta : Fin n → ℤ) (a : Blade n) :
    reorderSign a aᶜ * starSign eta a = metric eta a := by
  unfold starSign
  rw [← mul_assoc, reorderSign_sq, one_mul]

/-- The claimed w_ab=+eta_a eta_b, uniformly in dimension. -/
theorem pinned_pair_weight {n : ℕ} (eta : Fin n → ℤ)
    (a b : Fin n) (hab : a ≠ b) :
    reorderSign {a,b} ({a,b} : Blade n)ᶜ * starSign eta {a,b} = eta a * eta b := by
  rw [pinned_hodge_weight]
  simp [metric, hab]

/-- The opening prose's total-degree claim is false already in dimension four. -/
theorem wedge_total_degree_counterexample : ¬ Even (1 + (4 - 2) : ℕ) := by decide

/-- Correct statement: the operand-degree product governing the graded sign is even. -/
theorem bracket_degree_products_even (n : ℕ) (hn : Even n) (h : 2 ≤ n) :
    Even (1 * (n - 2)) ∧ Even (2 * (n - 2)) ∧ Even (1 * 0 : ℕ) := by
  obtain ⟨k, hk⟩ := hn
  constructor
  · refine ⟨k - 1, ?_⟩
    omega
  constructor
  · exact ⟨n - 2, by omega⟩
  · exact ⟨0, rfl⟩

/-- In 2D the same scalar response admits two different (c,kappa) pairs. -/
theorem dimension_two_kappa_nonunique :
    (-1 : ℚ) = (-1) * (1 - 2 * 0) ∧
    (-1 : ℚ) = 1 * (1 - 2 * 1) ∧ (0 : ℚ) ≠ 1 := by norm_num

end B02

