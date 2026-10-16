import B05Sign.Surrounding

namespace B05Sign
variable {R : Type*} [Ring R]

/-- Inner derivations give a concrete endoderivation without differential geometry. -/
def innerDiff (z : R) : Diff R where
  toAdd :=
    { toFun := fun x => z*x-x*z
      map_zero' := by simp
      map_add' := by intros; noncomm_ring }
  leibniz := by
    intro x y
    change z*(x*y)-(x*y)*z = (z*x-x*z)*y+x*(z*y-y*z)
    noncomm_ring

namespace Witness
abbrev M := Matrix (Fin 2) (Fin 2) ℤ

def swap : M := !![0, 1; 1, 0]
def origin : M := !![1, 0; 0, 0]

theorem swap_squared : swap * swap = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    norm_num [swap, Matrix.mul_apply, Fin.sum_univ_two]

def h : Mˣ := ⟨swap, swap, swap_squared, swap_squared⟩
def D : Diff M := innerDiff origin
def g : Gauge M := ⟨1, 0⟩

/-- The logarithmic derivative is nonzero in a fully specified noncommutative ring. -/
theorem logarithm : logD D h = !![-1, 0; 0, 1] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    norm_num [logD, D, innerDiff, origin, h, swap, Matrix.mul_apply, Fin.sum_univ_two]

theorem residual_nonzero : -(2 : M) * logD D h ≠ 0 := by
  intro he
  rw [neg_mul, neg_eq_zero, two_mul] at he
  have he00 := congrArg (fun m : M => m 0 0) he
  norm_num [logarithm, Matrix.add_apply] at he00

/-- Literal (7.4) fails at this explicit algebraic input. -/
theorem torsion_not_covariant : torsion D (g*tauLit D h) ≠ conj h (torsion D g) := by
  rw [torsion_lit]
  intro he
  have hz : 2 * logD D h = 0 := sub_eq_self.mp he
  exact residual_nonzero (by rw [neg_mul, hz, neg_zero])

/-- Literal first component of (6.20) fails with A0=0. -/
theorem connection_not_covariant :
    (biConnection D 0 (g*tauLit D h)).1 ≠ connectionAct D 0 (0+g.shift) h := by
  rw [connection_lit]
  intro he
  have hz : 2 * logD D h = 0 := sub_eq_self.mp he
  exact residual_nonzero (by rw [neg_mul, hz, neg_zero])

/-- The plus reconstruction cannot retain the printed projection claim (6.14). -/
theorem reconstructed_projection_not_invariant :
    projection D (g*tauRec D h) ≠ projection D g := by
  rw [projection_rec]
  intro he
  have hz := add_eq_left.mp he
  have hz' : 2 * logD D h = 0 := by
    have ht := congrArg (conj h) hz
    simp only [g, inv_one, conj_one, two_mul, conj_add, conj_comp,
      mul_one, inv_mul_cancel, conj_zero] at ht
    simpa only [two_mul] using ht
  exact residual_nonzero (by rw [neg_mul, hz', neg_zero])

end Witness
end B05Sign
