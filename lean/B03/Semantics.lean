import B03.Model
import Mathlib.Algebra.Group.Fin.Basic
import Mathlib.LinearAlgebra.Pi
import Mathlib.Data.Complex.Basic
import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.Tactic.FinCases

namespace B03
namespace Mono
 theorem mul_assoc (a b c : Mono m) : (a.mul b).mul c = a.mul (b.mul c) := by
  apply extensional; intro j; constructor
  · rfl
  · simp [mul, add_assoc]
 theorem conj_mul (a b : Mono m) : (a.mul b).conj = a.conj.mul b.conj := by
  apply extensional; intro j; constructor
  · rfl
  · simp [conj, mul, add_comm]
 theorem shift_mul (a b : Mono m) (k : Fin 4) : (a.shift k).mul b = (a.mul b).shift k := by
  apply extensional; intro j; constructor
  · rfl
  · simp [shift, mul, add_assoc]
 theorem mul_shift (a b : Mono m) (k : Fin 4) : a.mul (b.shift k) = (a.mul b).shift k := by
  apply extensional; intro j; constructor
  · rfl
  · simp [shift, mul]; omega
 theorem shift_shift (a : Mono m) (k l : Fin 4) : (a.shift k).shift l = a.shift (k+l) := by
  apply extensional; intro j; constructor
  · rfl
  · simp [shift, add_assoc]
 @[simp] theorem shift_zero (a : Mono m) : a.shift 0 = a := by
  apply extensional; intro j; simp [shift]
 theorem diagonal_commute (a b : Mono m) (ha : ∀ j, a.perm j = j) (hb : ∀ j, b.perm j = j) :
    a.mul b = b.mul a := by
  apply extensional; intro j; simp [mul, ha, hb, add_comm]
end Mono

noncomputable section
abbrev Spinor (m : ℕ) := Col m → ℂ
def phaseValue (k : Fin 4) : ℂ := Complex.I ^ k.val
 theorem phaseValue_add (k l : Fin 4) : phaseValue (k+l) = phaseValue k * phaseValue l := by
  fin_cases k <;> fin_cases l <;> norm_num [phaseValue, Fin.val_add, Fin.neg_def, pow_succ]
 theorem phaseValue_neg (k : Fin 4) : phaseValue (-k) = star (phaseValue k) := by
  fin_cases k <;> norm_num [phaseValue, Fin.val_add, Fin.neg_def, pow_succ]

def act (a : Mono m) : Spinor m →ₗ[ℂ] Spinor m :=
  Fintype.linearCombination ℂ (fun j => Pi.single (a.perm j) (phaseValue (a.phase j)))
@[simp] theorem act_single (a : Mono m) (j : Col m) (z : ℂ) :
    act a (Pi.single j z) = Pi.single (a.perm j) (z * phaseValue (a.phase j)) := by
  rw [act, Fintype.linearCombination_apply_single]
  ext i; by_cases h : i = a.perm j <;> simp [Pi.single_apply, h, smul_eq_mul]
 theorem act_mul (a b : Mono m) (v : Spinor m) : act (a.mul b) v = act a (act b v) := by
  have h : act (a.mul b) = (act a).comp (act b) := by
    apply LinearMap.pi_ext; intro j z
    simp [Mono.mul, phaseValue_add, mul_assoc]
  exact congrArg (fun f => f v) h
 @[simp] theorem act_one (v : Spinor m) : act Mono.one v = v := by
  have h : act (Mono.one : Mono m) = LinearMap.id := by
    apply LinearMap.pi_ext; intro j z; simp [Mono.one, phaseValue]
  exact congrArg (fun f => f v) h
 theorem act_shift (a : Mono m) (k : Fin 4) (v : Spinor m) :
    act (a.shift k) v = phaseValue k • act a v := by
  have h : act (a.shift k) = phaseValue k • act a := by
    apply LinearMap.pi_ext; intro j z
    ext r; by_cases hr : r = a.perm j <;>
      simp [Mono.shift, phaseValue_add, hr, smul_eq_mul, mul_left_comm, mul_comm]
  exact congrArg (fun f => f v) h
 @[simp] theorem act_shift_two (a : Mono m) (v : Spinor m) : act (a.shift 2) v = -act a v := by
  rw [act_shift]; norm_num [phaseValue]

def conjugation : Spinor m →ₛₗ[starRingEnd ℂ] Spinor m where
  toFun v j := star (v j)
  map_add' v w := by ext j; simp
  map_smul' z v := by ext j; simp [smul_eq_mul]
@[simp] theorem conjugation_single (j : Col m) (z : ℂ) :
    conjugation (Pi.single j z) = Pi.single j (star z) := by
  ext k; by_cases h : k = j <;> simp [conjugation, Pi.single_apply, h]
@[simp] theorem conjugation_involutive (v : Spinor m) : conjugation (conjugation v) = v := by
  ext j; simp [conjugation]
 theorem conjugation_act (a : Mono m) (v : Spinor m) :
    conjugation (act a v) = act a.conj (conjugation v) := by
  have h : conjugation.comp (act a) = (act a.conj).comp conjugation := by
    apply LinearMap.toAddMonoidHom_injective
    apply AddMonoidHom.functions_ext; intro j z
    simp [Mono.conj, phaseValue_neg]
  exact congrArg (fun f => f v) h
/-- Genuine complex-antilinear operator on the full complex spinor space. -/
def J (b : Mono m) : Spinor m →ₛₗ[starRingEnd ℂ] Spinor m := (act b).comp conjugation
 theorem J_antilinear (b : Mono m) (z : ℂ) (v w : Spinor m) :
    J b (z • v + w) = star z • J b v + J b w := by simp
 theorem J_squared (b : Mono m) (v : Spinor m) : J b (J b v) = act (b.mul b.conj) v := by
  simp only [J, LinearMap.comp_apply, conjugation_act, conjugation_involutive, act_mul]
 theorem J_intertwines (b a c : Mono m) (h : b.mul a.conj = c.mul b) (v : Spinor m) :
    J b (act a v) = act c (J b v) := by
  simp only [J, LinearMap.comp_apply, conjugation_act]
  rw [← act_mul, h, act_mul]
/-- Dense complex entries in the same COLUMN convention as Python Mono. -/
def matrix (a : Mono m) (i j : Col m) : ℂ :=
  if i = a.perm j then phaseValue (a.phase j) else 0
 theorem act_column_entry (a : Mono m) (i j : Col m) :
    act a (Pi.single j 1) i = matrix a i j := by
  simp [matrix, Pi.single_apply]
 theorem hermitian_entries (a : Mono m) (h : a.Hermitian) (i j : Col m) :
    matrix a i j = star (matrix a j i) := by
  by_cases hp : i = a.perm j
  · subst i
    simp [matrix, (h j).1, (h j).2, phaseValue_neg]
  · have hq : j ≠ a.perm i := by
      intro hq; apply hp
      rw [hq, (h i).1]
    simp [matrix, hp, hq]
end
end B03
