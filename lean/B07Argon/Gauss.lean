import Mathlib

/-! Pointwise codimension-one Gauss term, positive unit normal convention.
R(a,b,c,d) = h(a,c)h(b,d)-h(a,d)h(b,c) = (h ⊙ h)/2.
Ric(i,j) = Σa ηa R(a,i,a,j). No embedding or field equation is assumed.
Characteristic zero is used for the Einstein half; η²=1 includes all signatures. -/
namespace B07Argon.Gauss
open scoped BigOperators
variable {ι K : Type*} [Fintype ι] [DecidableEq ι] [Field K] [CharZero K]

def metric (η : ι → K) (i j : ι) : K := if i = j then η i else 0
def curvature (h : ι → ι → K) (a b c d : ι) : K :=
  h a c * h b d - h a d * h b c
def kulkarniNomizu (h k : ι → ι → K) (a b c d : ι) : K :=
  h a c * k b d + h b d * k a c - h a d * k b c - h b c * k a d
omit [Fintype ι] [DecidableEq ι] in
theorem gauss_half_KN (h : ι → ι → K) (a b c d : ι) :
    curvature h a b c d = kulkarniNomizu h h a b c d / 2 := by
  unfold curvature kulkarniNomizu; ring
def trace (η : ι → K) (h : ι → ι → K) : K := ∑ i, η i * h i i
def square (η : ι → K) (h : ι → ι → K) (i j : ι) : K :=
  ∑ a, η a * h i a * h a j
def ricci (η : ι → K) (h : ι → ι → K) (i j : ι) : K :=
  ∑ a, η a * curvature h a i a j
def scalar (η : ι → K) (h : ι → ι → K) : K := trace η (ricci η h)
def einstein (η : ι → K) (h : ι → ι → K) (i j : ι) : K :=
  ricci η h i j - scalar η h / 2 * metric η i j

omit [DecidableEq ι] [CharZero K] in
theorem ricci_formula (η : ι → K) (h : ι → ι → K) (i j : ι) :
    ricci η h i j = trace η h * h i j - square η h i j := by
  simp only [ricci, curvature, trace, square, Finset.sum_mul, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro a _
  ring

theorem scalar_formula (η : ι → K) (h : ι → ι → K) :
    scalar η h = (trace η h)^2 - ∑ i, ∑ a, η i * η a * h i a * h a i := by
  unfold scalar trace
  simp_rw [ricci_formula]
  simp only [trace, square, mul_sub, Finset.sum_sub_distrib, Finset.mul_sum]
  rw [show (∑ i, η i * ((∑ a, η a * h a a) * h i i)) =
    (∑ a, η a * h a a) * (∑ i, η i * h i i) by
      rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intros; ring]
  congr 1
  · ring
  · apply Finset.sum_congr rfl; intro i _
    apply Finset.sum_congr rfl; intro a _; ring

omit [CharZero K] in
theorem trace_umbilic (η : ι → K) (hη : ∀ i, η i * η i = 1) (lam : K) :
    trace η (fun i j => lam * metric η i j) = (Fintype.card ι : K) * lam := by
  simp only [trace, metric, ite_true]
  simp_rw [show ∀ i, η i * (lam * η i) = lam by intro i; calc
    _ = lam * (η i * η i) := by ring
    _ = lam := by rw [hη, mul_one]]
  simp

omit [CharZero K] in
theorem square_umbilic (η : ι → K) (hη : ∀ i, η i * η i = 1) (lam : K) (i j : ι) :
    square η (fun i j => lam * metric η i j) i j = lam^2 * metric η i j := by
  classical
  simp only [square, metric]
  by_cases hij : i = j
  · subst j
    simp only [ite_true]
    rw [Finset.sum_eq_single i]
    · simp only [ite_true]
      calc
        η i * (lam * η i) * (lam * η i) = lam^2 * η i * (η i * η i) := by ring
        _ = lam^2 * η i := by rw [hη, mul_one]
    · intro b _ hb; simp [hb, Ne.symm hb]
    · simp
  · simp only [hij, ite_false, mul_zero]
    apply Finset.sum_eq_zero
    intro a _
    by_cases ha : i = a
    · subst a; simp [hij]
    · simp [ha]

theorem ricci_umbilic (η : ι → K) (hη : ∀ i, η i * η i = 1) (lam : K) (i j : ι) :
    ricci η (fun i j => lam * metric η i j) i j =
      ((Fintype.card ι : K) - 1) * lam^2 * metric η i j := by
  rw [ricci_formula, trace_umbilic η hη, square_umbilic η hη]
  ring

theorem scalar_umbilic (η : ι → K) (hη : ∀ i, η i * η i = 1) (lam : K) :
    scalar η (fun i j => lam * metric η i j) =
      (Fintype.card ι : K) * ((Fintype.card ι : K) - 1) * lam^2 := by
  have hr : ricci η (fun i j => lam * metric η i j) =
      fun i j => ((Fintype.card ι : K) - 1) * lam^2 * metric η i j := by
    funext i j; exact ricci_umbilic η hη lam i j
  rw [scalar, hr, trace_umbilic η hη]
  ring

theorem einstein_umbilic (η : ι → K) (hη : ∀ i, η i * η i = 1) (lam : K) (i j : ι) :
    einstein η (fun i j => lam * metric η i j) i j =
      -(((Fintype.card ι : K) - 1) * ((Fintype.card ι : K) - 2) / 2) *
        lam^2 * metric η i j := by
  rw [einstein, ricci_umbilic η hη, scalar_umbilic η hη]
  ring

def PureMetric (η : ι → K) (t : ι → ι → K) : Prop :=
  ∃ c, ∀ i j, t i j = c * metric η i j

/-- In particular n=4; actually no dimension restriction is needed. -/
theorem einstein_pure_iff (η : ι → K) (h : ι → ι → K) :
    PureMetric η (einstein η h) ↔
      PureMetric η (fun i j => square η h i j - trace η h * h i j) := by
  constructor
  · rintro ⟨c, hc⟩
    refine ⟨-c - scalar η h / 2, ?_⟩
    intro i j
    have hh := hc i j
    rw [einstein, ricci_formula] at hh
    linear_combination -hh
  · rintro ⟨c, hc⟩
    refine ⟨-c - scalar η h / 2, ?_⟩
    intro i j
    rw [einstein, ricci_formula]
    linear_combination -(hc i j)

/-- A symmetric non-umbilic Euclidean 4D witness diag(1,2,0,0). -/
def witness : Fin 4 → Fin 4 → ℚ := fun i j => if i = j then (if i = 0 then 1 else if i = 1 then 2 else 0) else 0
theorem witness_symmetric : ∀ i j, witness i j = witness j i := by
  decide
theorem witness_not_umbilic : ¬ ∃ lam : ℚ, ∀ i j : Fin 4,
    witness i j = lam * metric (fun _ => 1) i j := by
  rintro ⟨lam, h⟩
  have h0 := h 0 0
  have h1 := h 1 1
  norm_num [witness, metric] at h0 h1
  linarith
theorem witness_not_pure : ¬ PureMetric (fun _ : Fin 4 => (1 : ℚ))
    (einstein (fun _ => 1) witness) := by
  rintro ⟨c, hc⟩
  have h0 := hc 0 0
  have h2 := hc 2 2
  have e0 : einstein (fun _ => 1) witness 0 0 = 0 := by decide +kernel
  have e2 : einstein (fun _ => 1) witness 2 2 = -2 := by decide +kernel
  rw [e0] at h0
  rw [e2] at h2
  norm_num [metric] at h0 h2
  linarith

end B07Argon.Gauss
