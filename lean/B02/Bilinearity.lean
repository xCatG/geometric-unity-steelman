import B02.Semantics

namespace B02.Concrete
open scoped BigOperators

/-- Basis kernel for the executable coefficient bracket. -/
def bracketKernel (eta : Fin n → ℤ) (m : Mode)
    (f1 b1 f2 b2 f b : Blade n) : GQ :=
  bracketContribution eta m ⟨f1,b1,1⟩ ⟨f2,b2,1⟩ f b

theorem bracketContribution_factor (eta : Fin n → ℤ) (m : Mode)
    (t u : Term n) (f b : Blade n) :
    bracketContribution eta m t u f b =
      t.value * u.value * bracketKernel eta m t.form t.blade u.form u.blade f b := by
  by_cases hd : Disjoint t.form u.form
  · by_cases ho : t.form ∪ u.form = f ∧ (bladeMul eta t.blade u.blade).1 = b
    · cases m <;> simp [bracketKernel, bracketContribution, hd, ho] <;> ring
    · cases m <;> simp [bracketKernel, bracketContribution, hd, ho]
  · simp [bracketKernel, bracketContribution, hd]

/-- Regrouping a list of terms by its actual finite basis coefficients. -/
theorem weighted_sum_coefficients (x : Element n) (F : Blade n → Blade n → GQ) :
    (x.map (fun t => t.value * F t.form t.blade)).sum =
      ∑ f, ∑ b, coefficient x f b * F f b := by
  induction x with
  | nil => simp
  | cons t ts ih =>
    simp only [List.map_cons, List.sum_cons, coefficient_cons, add_mul,
      Finset.sum_add_distrib]
    rw [ih]
    congr 1
    classical
    simp [ite_and]

/-- Exact finite coefficient formula, derived from the executable sparse-list code. -/
theorem coefficient_bracket_finite (eta : Fin n → ℤ) (m : Mode)
    (x y : Element n) (f b : Blade n) :
    coefficient (bracket eta m x y) f b =
      ∑ f1, ∑ b1, ∑ f2, ∑ b2,
        coefficient x f1 b1 * coefficient y f2 b2 *
          bracketKernel eta m f1 b1 f2 b2 f b := by
  rw [coefficient_bracket]
  simp_rw [bracketContribution_factor]
  have hinner (t : Term n) :
      (y.map (fun u => t.value * u.value *
        bracketKernel eta m t.form t.blade u.form u.blade f b)).sum =
      t.value * (∑ f2, ∑ b2, coefficient y f2 b2 *
        bracketKernel eta m t.form t.blade f2 b2 f b) := by
    rw [← weighted_sum_coefficients]
    simp_rw [mul_assoc]
    exact List.sum_map_mul_left y (fun u => u.value * bracketKernel eta m t.form t.blade u.form u.blade f b) t.value
  simp_rw [hinner]
  rw [weighted_sum_coefficients x (fun f1 b1 => ∑ f2, ∑ b2,
    coefficient y f2 b2 * bracketKernel eta m f1 b1 f2 b2 f b)]
  simp_rw [Finset.mul_sum]
  simp_rw [mul_assoc]

/-- Brackets depend only on the extensional coefficient values of both inputs. -/
theorem coefficient_bracket_congr (eta : Fin n → ℤ) (m : Mode)
    {x x' y y' : Element n}
    (hx : ∀ f b, coefficient x f b = coefficient x' f b)
    (hy : ∀ f b, coefficient y f b = coefficient y' f b) (f b : Blade n) :
    coefficient (bracket eta m x y) f b = coefficient (bracket eta m x' y') f b := by
  simp only [coefficient_bracket_finite, hx, hy]

theorem coefficient_bracket_scale_right (eta : Fin n → ℤ) (m : Mode)
    (x y : Element n) (c : GQ) (f b : Blade n) :
    coefficient (bracket eta m x (scale y c)) f b =
      coefficient (bracket eta m x y) f b * c := by
  simp only [coefficient_bracket_finite, coefficient_scale, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro f1 _
  apply Finset.sum_congr rfl
  intro b1 _
  apply Finset.sum_congr rfl
  intro f2 _
  apply Finset.sum_congr rfl
  intro b2 _
  ring

theorem coefficient_bracket_scale_left (eta : Fin n → ℤ) (m : Mode)
    (x y : Element n) (c : GQ) (f b : Blade n) :
    coefficient (bracket eta m (scale x c) y) f b =
      coefficient (bracket eta m x y) f b * c := by
  simp only [coefficient_bracket_finite, coefficient_scale, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro f1 _
  apply Finset.sum_congr rfl
  intro b1 _
  apply Finset.sum_congr rfl
  intro f2 _
  apply Finset.sum_congr rfl
  intro b2 _
  ring

end B02.Concrete


