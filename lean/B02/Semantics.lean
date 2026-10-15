import B02.Concrete

/-! Extensional coefficient semantics of the executable sparse-list model. -/
namespace B02.Concrete

@[simp] theorem coefficient_nil {n : ℕ} (f b : Blade n) : coefficient [] f b = 0 := by
  simp [coefficient]

@[simp] theorem coefficient_cons {n : ℕ} (t : Term n) (x : Element n) (f b : Blade n) :
    coefficient (t :: x) f b =
      (if t.form = f ∧ t.blade = b then t.value else 0) + coefficient x f b := by
  simp [coefficient]

/-- Combining a sparse term preserves the sum, including cancellation and duplicates. -/
theorem coefficient_addTerm {n : ℕ} (t : Term n) (x : Element n) (f b : Blade n) :
    coefficient (addTerm t x) f b = coefficient [t] f b + coefficient x f b := by
  induction x with
  | nil =>
    by_cases ht : t.value = 0
    · simp [addTerm, ht]
    · simp [addTerm, ht]
  | cons u us ih =>
    by_cases htu : t.form = u.form ∧ t.blade = u.blade
    · by_cases hz : t.value + u.value = 0
      · simp only [addTerm, if_pos htu, if_pos hz, coefficient_cons, coefficient_nil, add_zero]
        by_cases hm : u.form = f ∧ u.blade = b
        · have htm : t.form = f ∧ t.blade = b := ⟨htu.1.trans hm.1, htu.2.trans hm.2⟩
          simp only [if_pos hm, if_pos htm]
          linear_combination -hz
        · have htm : ¬ (t.form = f ∧ t.blade = b) := by
            intro ht
            exact hm ⟨htu.1.symm.trans ht.1, htu.2.symm.trans ht.2⟩
          simp [hm, htm]
      · simp only [addTerm, if_pos htu, if_neg hz, coefficient_cons, coefficient_nil, add_zero]
        have heq : (t.form = f ∧ t.blade = b) ↔ (u.form = f ∧ u.blade = b) := by
          rw [htu.1, htu.2]
        simp only [heq]
        split_ifs <;> ring
    · simp only [addTerm, if_neg htu, coefficient_cons, ih, coefficient_nil, add_zero]
      ring

private theorem coefficient_fold {n : ℕ} (x acc : Element n) (f b : Blade n) :
    coefficient (x.foldl (fun z t => addTerm t z) acc) f b =
      coefficient acc f b + coefficient x f b := by
  induction x generalizing acc with
  | nil => simp
  | cons t ts ih =>
    simp only [List.foldl_cons, ih, coefficient_addTerm, coefficient_cons,
      coefficient_nil, add_zero]
    ring

@[simp] theorem coefficient_clean {n : ℕ} (x : Element n) (f b : Blade n) :
    coefficient (clean x) f b = coefficient x f b := by
  simpa [clean] using coefficient_fold x [] f b

@[simp] theorem coefficient_plus {n : ℕ} (x y : Element n) (f b : Blade n) :
    coefficient (plus x y) f b = coefficient x f b + coefficient y f b := by
  exact coefficient_fold y x f b

@[simp] theorem coefficient_scale {n : ℕ} (x : Element n) (c : GQ) (f b : Blade n) :
    coefficient (scale x c) f b = coefficient x f b * c := by
  simp only [scale, coefficient_clean]
  induction x with
  | nil => simp
  | cons t ts ih =>
    simp only [List.map_cons, coefficient_cons] at *
    rw [ih]
    split_ifs <;> ring

/-- Star reads the complementary form coefficient and applies the pinned weight. -/
@[simp] theorem coefficient_star {n : ℕ} (eta : Fin n → ℤ) (x : Element n)
    (f b : Blade n) : coefficient (star eta x) f b =
      coefficient x fᶜ b * integer (starSign eta fᶜ) := by
  simp only [star, coefficient_clean]
  induction x with
  | nil => simp
  | cons t ts ih =>
    simp only [List.map_cons, coefficient_cons] at *
    rw [ih]
    have hc : t.formᶜ = f ↔ t.form = fᶜ := by
      constructor
      · intro h
        simpa using congrArg (fun s : Blade n => sᶜ) h
      · intro h
        simp [h]
    simp only [hc]
    by_cases hm : t.form = fᶜ ∧ t.blade = b
    · simp only [hm.1, hm.2, and_self, ite_true]
      ring
    · simp only [if_neg hm, zero_add]

/-- The coefficient of a bracket is its raw finite list sum, independent of normalization. -/
theorem coefficient_bracket_raw {n : ℕ} (eta : Fin n → ℤ) (mode : Mode)
    (x y : Element n) (f b : Blade n) :
    coefficient (bracket eta mode x y) f b =
      coefficient (x.flatMap fun t => y.filterMap fun u =>
        if Disjoint t.form u.form then
          let (out, z) := bladeMul eta t.blade u.blade
          let w := (bladeMul eta u.blade t.blade).2
          let k := match mode with | .C => z - w | .A => z + w
          let c := t.value * u.value * integer (reorderSign t.form u.form * k)
          some ⟨t.form ∪ u.form, out, match mode with | .C => c | .A => c * imaginary⟩
        else none) f b := by
  exact coefficient_clean _ _ _

@[simp] theorem coefficient_append {n : ℕ} (x y : Element n) (f b : Blade n) :
    coefficient (x ++ y) f b = coefficient x f b + coefficient y f b := by
  simp [coefficient]

/-- A single ordered pair's contribution to an output coefficient. -/
def bracketContribution {n : ℕ} (eta : Fin n → ℤ) (mode : Mode)
    (t u : Term n) (f b : Blade n) : GQ :=
  if Disjoint t.form u.form then
    let (out, z) := bladeMul eta t.blade u.blade
    let w := (bladeMul eta u.blade t.blade).2
    let k := match mode with | .C => z - w | .A => z + w
    let c := t.value * u.value * integer (reorderSign t.form u.form * k)
    if t.form ∪ u.form = f ∧ out = b then
      match mode with | .C => c | .A => c * imaginary
    else 0
  else 0

/-- Fully expanded coefficient formula for either executable bracket mode. -/
theorem coefficient_bracket {n : ℕ} (eta : Fin n → ℤ) (mode : Mode)
    (x y : Element n) (f b : Blade n) :
    coefficient (bracket eta mode x y) f b =
      (x.map fun t => (y.map fun u => bracketContribution eta mode t u f b).sum).sum := by
  rw [coefficient_bracket_raw]
  induction x with
  | nil => simp
  | cons t ts ih =>
    simp only [List.flatMap_cons, coefficient_append, List.map_cons, List.sum_cons] at *
    rw [ih]
    congr 1
    clear ih
    induction y with
    | nil => simp
    | cons u us ihu =>
      simp only [List.filterMap_cons, List.map_cons, List.sum_cons]
      by_cases hd : Disjoint t.form u.form
      · simp only [hd, ↓reduceIte, coefficient_cons, bracketContribution]
        rw [ihu]
        rfl
      · simp only [hd, ↓reduceIte, bracketContribution, zero_add]
        exact ihu

end B02.Concrete




#print axioms B02.Concrete.coefficient_addTerm
#print axioms B02.Concrete.coefficient_clean
#print axioms B02.Concrete.coefficient_plus
#print axioms B02.Concrete.coefficient_scale
#print axioms B02.Concrete.coefficient_star
#print axioms B02.Concrete.coefficient_bracket
