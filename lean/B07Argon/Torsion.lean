import Mathlib

/-! Cartan torsion, NOT GU augmented torsion. All indices are lowered;
K a b c = g((nabla-LC)_a e_b,e_c), antisymmetric in b,c.
The trace convention is t_b = Σa ηa torsion(a,b,a). -/
namespace B07Argon.Cartan
open scoped BigOperators
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
abbrev Tensor (ι : Type*) := ι → ι → ι → ℚ
def torsion (K : Tensor ι) (a b c : ι) : ℚ := K a b c - K b a c
def trace (η : ι → ℚ) (t : Tensor ι) (b : ι) : ℚ := ∑ a, η a * t a b a
def divergence (η : ι → ℚ) (K : Tensor ι) (dV : ι → ι → ℚ) (V : ι → ℚ) : ℚ :=
  ∑ a, (dV a a + ∑ b, η a * K a b a * V b)

omit [Fintype ι] [DecidableEq ι] in
theorem metric_diagonal_zero (K : Tensor ι)
    (hK : ∀ a b c, K a b c = -K a c b) (a b : ι) : K a b b = 0 := by
  have := hK a b b; linarith

theorem contorsion_trace (η : ι → ℚ) (K : Tensor ι)
    (hK : ∀ a b c, K a b c = -K a c b) (b : ι) :
    trace η (torsion K) b = ∑ a, η a * K a b a := by
  simp [trace, torsion, metric_diagonal_zero K hK]

theorem divergence_difference (η : ι → ℚ) (K : Tensor ι)
    (hK : ∀ a b c, K a b c = -K a c b) (dV : ι → ι → ℚ) (V : ι → ℚ) :
    divergence η K dV V - (∑ a, dV a a) = ∑ b, trace η (torsion K) b * V b := by
  simp only [divergence, Finset.sum_add_distrib, add_sub_cancel_left,
    contorsion_trace η K hK, Finset.sum_mul]
  exact Finset.sum_comm

def g (η : ι → ℚ) (a b : ι) : ℚ := if a = b then η a else 0
def tracePart (η v : ι → ℚ) (a b c : ι) : ℚ :=
  (g η a c * v b - g η b c * v a) / ((Fintype.card ι : ℚ) - 1)
def axialPart (t : Tensor ι) (a b c : ι) : ℚ :=
  (t a b c + t b c a + t c a b) / 3
def tensorPart (η : ι → ℚ) (t : Tensor ι) (a b c : ι) : ℚ :=
  t a b c - tracePart η (trace η t) a b c - axialPart t a b c

theorem trace_tracePart (η v : ι → ℚ) (hη : ∀ a, η a * η a = 1)
    (hn : (Fintype.card ι : ℚ) - 1 ≠ 0) (b : ι) : trace η (tracePart η v) b = v b := by
  simp only [trace, tracePart, ← mul_div_assoc, ← Finset.sum_div, mul_sub, Finset.sum_sub_distrib]
  have hfirst : (∑ a, η a * (g η a a * v b)) = (Fintype.card ι : ℚ) * v b := by
    simp only [g, ite_true, ← mul_assoc, hη, one_mul, Finset.sum_const,
      Finset.card_univ, nsmul_eq_mul]
  have hsecond : (∑ a, η a * (g η b a * v a)) = v b := by
    rw [Finset.sum_eq_single b]
    · simp [g, ← mul_assoc, hη]
    · intro a _ ha; simp [g, Ne.symm ha]
    · simp
  rw [hfirst, hsecond]
  apply (div_eq_iff hn).2
  ring

omit [Fintype ι] [DecidableEq ι] in
theorem axial_antisymm_first (t : Tensor ι) (ht : ∀ a b c, t a b c = -t b a c)
    (a b c : ι) : axialPart t a b c = -axialPart t b a c := by
  unfold axialPart
  rw [ht a b c, ht b c a, ht c a b]
  ring

omit [Fintype ι] [DecidableEq ι] in
theorem axial_antisymm_last (t : Tensor ι) (ht : ∀ a b c, t a b c = -t b a c)
    (a b c : ι) : axialPart t a b c = -axialPart t a c b := by
  unfold axialPart
  rw [ht a b c, ht b c a, ht c a b]
  ring

theorem axial_trace_zero (η : ι → ℚ) (t : Tensor ι)
    (ht : ∀ a b c, t a b c = -t b a c) (b : ι) : trace η (axialPart t) b = 0 := by
  apply Finset.sum_eq_zero
  intro a _
  have h1 := axial_antisymm_first t ht a b a
  have h2 := axial_antisymm_last t ht b a a
  have hz : axialPart t a b a = 0 := by linarith
  rw [hz, mul_zero]

theorem tensor_trace_zero (η : ι → ℚ) (t : Tensor ι)
    (hη : ∀ a, η a * η a = 1) (hn : (Fintype.card ι : ℚ) - 1 ≠ 0)
    (ht : ∀ a b c, t a b c = -t b a c) (b : ι) : trace η (tensorPart η t) b = 0 := by
  change (∑ a, η a * (t a b a - tracePart η (trace η t) a b a - axialPart t a b a)) = 0
  simp only [mul_sub, Finset.sum_sub_distrib]
  change trace η t b - trace η (tracePart η (trace η t)) b - trace η (axialPart t) b = 0
  rw [trace_tracePart η _ hη hn, axial_trace_zero η t ht]; ring

theorem decomposition (η : ι → ℚ) (t : Tensor ι) (a b c : ι) :
    t a b c = tracePart η (trace η t) a b c + axialPart t a b c + tensorPart η t a b c := by
  unfold tensorPart; ring

omit [Fintype ι] in
theorem g_symmetric (η : ι → ℚ) (a b : ι) : g η a b = g η b a := by
  by_cases h : a = b
  · subst b; rfl
  · simp [g, h, Ne.symm h]

theorem tracePart_cyclic_zero (η v : ι → ℚ) (a b c : ι) :
    tracePart η v a b c + tracePart η v b c a + tracePart η v c a b = 0 := by
  unfold tracePart
  rw [g_symmetric η c a, g_symmetric η b a, g_symmetric η c b]
  ring

theorem tensor_cyclic_zero (η : ι → ℚ) (t : Tensor ι) (a b c : ι) :
    tensorPart η t a b c + tensorPart η t b c a + tensorPart η t c a b = 0 := by
  have hh := tracePart_cyclic_zero η (trace η t) a b c
  unfold tensorPart axialPart
  linear_combination -hh

theorem tracePart_antisymm (η v : ι → ℚ) (a b c : ι) :
    tracePart η v a b c = -tracePart η v b a c := by unfold tracePart; ring

theorem tensor_antisymm (η : ι → ℚ) (t : Tensor ι)
    (ht : ∀ a b c, t a b c = -t b a c) (a b c : ι) :
    tensorPart η t a b c = -tensorPart η t b a c := by
  unfold tensorPart
  rw [ht a b c, tracePart_antisymm η (trace η t) a b c, axial_antisymm_first t ht a b c]
  ring

/-- Coordinate one-form derivative. d is connection independent. -/
def covDerivative (η : ι → ℚ) (K : Tensor ι) (dw : ι → ι → ℚ)
    (w : ι → ℚ) (a b : ι) : ℚ := dw a b - ∑ c, η c * K a b c * w c

omit [DecidableEq ι] in
theorem exterior_one_form (η : ι → ℚ) (K : Tensor ι) (dw : ι → ι → ℚ)
    (w : ι → ℚ) (a b : ι) :
    dw a b - dw b a = covDerivative η K dw w a b - covDerivative η K dw w b a +
      ∑ c, η c * torsion K a b c * w c := by
  simp only [covDerivative, torsion, mul_sub, sub_mul, Finset.sum_sub_distrib]
  ring

def epsilon3 (a b c : Fin 3) : ℚ :=
  if (a,b,c) = (0,1,2) ∨ (a,b,c) = (1,2,0) ∨ (a,b,c) = (2,0,1) then 1
  else if (a,b,c) = (1,0,2) ∨ (a,b,c) = (0,2,1) ∨ (a,b,c) = (2,1,0) then -1 else 0
theorem epsilon3_metric : ∀ a b c, epsilon3 a b c = -epsilon3 a c b := by decide
theorem epsilon3_axial : ∀ a b c, epsilon3 a b c = -epsilon3 b a c := by decide
theorem epsilon3_trace_zero : ∀ b, trace (fun _ => 1) (torsion epsilon3) b = 0 := by
  decide +kernel
theorem axial_exterior_nonzero :
    (∑ c : Fin 3, torsion epsilon3 0 1 c * (if c = 2 then 1 else 0)) = 2 := by
  decide +kernel

end B07Argon.Cartan
