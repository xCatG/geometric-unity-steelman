import B05Sign.Algebra

namespace B05Sign
variable {R : Type*} [Ring R]

/-- Reversing a product in inverse conjugation, with no commutativity assumption. -/
theorem conj_mul_inv (e h : Rˣ) (x : R) :
    conj (e*h)⁻¹ x = conj e⁻¹ (conj h⁻¹ x) := by
  rw [conj_comp, mul_inv_rev]

/-- Exactly (6.15), rearranged using the right logarithmic derivative. -/
def leftAct (D : Diff R) (g : Gauge R) (gamma : R) : R :=
  conj g.unit⁻¹ (g.shift + gamma + logD D g.unit)

theorem leftAct_formula (D : Diff R) (g : Gauge R) (gamma : R) :
    leftAct D g gamma =
      (↑g.unit : R) * (g.shift+gamma) * ↑g.unit⁻¹ + D ↑g.unit * ↑g.unit⁻¹ := by
  simp [leftAct, conj, logD, add_mul, mul_add, ← mul_assoc]

/-- (6.15)-(6.16) does give a left group action for the printed (5.9). -/
theorem leftAct_mul (D : Diff R) (g k : Gauge R) (gamma : R) :
    leftAct D (g*k) gamma = leftAct D g (leftAct D k gamma) := by
  simp only [leftAct, mul_unit, mul_shift, logD_mul, conj_mul_inv, conj_add, conj_cancel]
  abel

theorem leftAct_one (D : Diff R) (gamma : R) : leftAct D 1 gamma = gamma := by
  change conj (1 : Rˣ)⁻¹ (0+gamma+logD D 1) = gamma
  simp

/-- (6.11), the projection used in Lemma 6.3. -/
def projection (D : Diff R) (g : Gauge R) : R := leftAct D g 0

theorem projection_formula (D : Diff R) (g : Gauge R) :
    projection D g = (↑g.unit : R)*g.shift*↑g.unit⁻¹ + D ↑g.unit*↑g.unit⁻¹ := by
  simp [projection, leftAct_formula]

/-- The minus branch is consistent with (6.14). -/
theorem projection_lit (D : Diff R) (g : Gauge R) (h : Rˣ) :
    projection D (g*tauLit D h) = projection D g := by
  simp only [projection, leftAct, mul_unit, mul_shift, tauLit, logD_mul,
    conj_mul_inv, conj_add, conj_neg, conj_cancel, add_zero]
  abel

/-- Changing only the tilted sign breaks (6.14) in general. -/
theorem projection_rec (D : Diff R) (g : Gauge R) (h : Rˣ) :
    projection D (g*tauRec D h) = projection D g +
      2 * conj g.unit⁻¹ (conj h⁻¹ (logD D h)) := by
  simp only [projection, leftAct, mul_unit, mul_shift, tauRec, logD_mul,
    conj_mul_inv, conj_add, conj_cancel, add_zero]
  noncomm_ring

/-- The stabilizer assertion (6.6)-(6.9) uses the minus sign. -/
theorem stabilizer_lit (D : Diff R) (h : Rˣ) : act62 D 0 (tauLit D h) = 0 := by
  simp [act62, tauLit]

theorem stabilizer_rec (D : Diff R) (h : Rˣ) :
    act62 D 0 (tauRec D h) = 2 * logD D h := by
  simp [act62, tauRec]; noncomm_ring

end B05Sign
