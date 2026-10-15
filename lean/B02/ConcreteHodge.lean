import B02.Semantics
import B02.Bilinearity
import B02.Degree
import B02.Hodge
import Mathlib

/-! The alternate Hodge convention for the executable sparse model.
All statements use the actual list operations and extensional coefficients. -/
namespace B02.Concrete

/-- Same sparse normalization as `star`, with the opposite convention's sign. -/
def otherStar (eta : Fin n → ℤ) (x : Element n) : Element n :=
  clean (x.map fun t => ⟨t.formᶜ, t.blade,
    t.value * integer (oppositeStarSign eta t.form)⟩)

/-- Equation (9.3) with every Hodge star changed to the opposite convention. -/
def otherShiab (eta : Fin n → ℤ) (m0 m1 m2 : Mode)
    (phi1 phi2 x : Element n) : Element n :=
  let sx := otherStar eta x
  let first := bracket eta m0 phi1 sx
  let second := otherStar eta
    (bracket eta m2 phi1 (otherStar eta (bracket eta m1 phi2 sx)))
  plus first (scale second (rational (-1 / 2)))

theorem integer_negation (z : ℤ) : integer (-z) = -integer z := by
  ext <;> simp [integer, rational]

/-- Coefficient formula including normalization of the opposite star. -/
theorem coefficient_otherStar (eta : Fin n → ℤ) (x : Element n) (f b : Blade n) :
    coefficient (otherStar eta x) f b =
      coefficient x fᶜ b * integer (oppositeStarSign eta fᶜ) := by
  simp only [otherStar, coefficient_clean]
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

/-- A homogeneous sparse list has no coefficient in any other form degree. -/
theorem homogeneous_coefficient_zero {k : ℕ} {x : Element n}
    (hx : Homogeneous k x) (f b : Blade n) (hf : f.card ≠ k) :
    coefficient x f b = 0 := by
  unfold coefficient
  apply List.sum_eq_zero
  intro v hv
  obtain ⟨t, ht, rfl⟩ := List.mem_map.mp hv
  have htf : t.form ≠ f := by
    intro h
    exact hf (h ▸ hx t ht)
  simp [htf]

/-- Input degree two is unchanged, as literal normalized-list equality. -/
theorem otherStar_two (eta : Fin n → ℤ) {x : Element n}
    (hx : Homogeneous 2 x) : otherStar eta x = star eta x := by
  unfold otherStar star
  congr 1
  apply List.map_congr_left
  intro t ht
  rw [oppositeStarSign_two eta t.form (hx t ht)]

/-- Top degree is unchanged, as literal normalized-list equality. -/
theorem otherStar_top (eta : Fin n → ℤ) {x : Element n}
    (hx : Homogeneous n x) : otherStar eta x = star eta x := by
  unfold otherStar star
  congr 1
  apply List.map_congr_left
  intro t ht
  rw [oppositeStarSign_top eta t.form (hx t ht)]

/-- Actual coefficient sign change on degree one, for every even dimension. -/
theorem coefficient_otherStar_one (eta : Fin n → ℤ) (hn : Even n)
    {x : Element n} (hx : Homogeneous 1 x) (f b : Blade n) :
    coefficient (otherStar eta x) f b = -coefficient (star eta x) f b := by
  rw [coefficient_otherStar, coefficient_star]
  by_cases hf : fᶜ.card = 1
  · rw [oppositeStarSign_one eta hn fᶜ hf, integer_negation]
    ring
  · rw [homogeneous_coefficient_zero hx fᶜ b hf]
    simp

/-- The opposite star has the same degree as the pinned star, independently
of all signature and parity assumptions. -/
theorem homogeneous_otherStar (eta : Fin n → ℤ) {k : ℕ} {x : Element n}
    (hx : Homogeneous k x) : Homogeneous (n - k) (otherStar eta x) := by
  apply clean_form_property (fun f => f.card = n - k)
  intro t ht
  obtain ⟨u, hu, rfl⟩ := List.mem_map.mp ht
  simp [Finset.card_compl, hx u hu]

/-- Coefficient equivalence with a scalar factor passes through the actual star. -/
theorem coefficient_star_scaled (eta : Fin n → ℤ) {x y : Element n} (c : GQ)
    (h : ∀ f b, coefficient x f b = coefficient y f b * c) (f b : Blade n) :
    coefficient (star eta x) f b = coefficient (star eta y) f b * c := by
  rw [coefficient_star, coefficient_star, h]
  ring

/-- The final readout star on degree n-1 changes the entire response's sign. -/
theorem coefficient_otherStar_output (eta : Fin n → ℤ) (hn : Even n) (hn2 : 2 ≤ n)
    {x : Element n} (hx : Homogeneous (n - 1) x) (f b : Blade n) :
    coefficient (otherStar eta x) f b = -coefficient (star eta x) f b := by
  rw [coefficient_otherStar, coefficient_star]
  by_cases hf : fᶜ.card = n - 1
  · rw [oppositeStarSign_output eta hn hn2 fᶜ hf, integer_negation]
    ring
  · rw [homogeneous_coefficient_zero hx fᶜ b hf]
    simp

/-- Concrete all-dimension/all-eight-mode composition: precisely the nested
term changes sign when every Hodge star in equation (9.3) is replaced. -/
theorem otherShiab_coefficient (eta : Fin n → ℤ) (hn : Even n) (hn2 : 2 ≤ n)
    (m0 m1 m2 : Mode) {phi1 phi2 x : Element n}
    (h1 : Homogeneous 1 phi1) (h2 : Homogeneous 2 phi2) (hx : Homogeneous 2 x)
    (f b : Blade n) :
    coefficient (otherShiab eta m0 m1 m2 phi1 phi2 x) f b =
      coefficient (bracket eta m0 phi1 (star eta x)) f b +
      coefficient (star eta (bracket eta m2 phi1
        (star eta (bracket eta m1 phi2 (star eta x))))) f b * rational (1 / 2) := by
  have hsx := otherStar_two eta hx
  have hi := homogeneous_bracket eta m1 h2 (homogeneous_star eta hx)
  have hdeg : 2 + (n - 2) = n := by omega
  rw [hdeg] at hi
  have hinner := otherStar_top eta hi
  have ho := homogeneous_bracket eta m2 h1 (homogeneous_star eta hi)
  simp only [Nat.sub_self, Nat.add_zero] at ho
  simp only [otherShiab, hsx, hinner, coefficient_plus, coefficient_scale]
  rw [coefficient_otherStar_one eta hn ho]
  have hc : rational (-1 / 2) = -rational (1 / 2) := by
    ext <;> norm_num [rational, QuadraticAlgebra.re_one, QuadraticAlgebra.im_one]
  rw [hc]
  ring


/-- The degree theorem also holds with the opposite Hodge convention. -/
theorem otherShiab_degree (eta : Fin n → ℤ) (hn : 2 ≤ n) (m0 m1 m2 : Mode)
    {phi1 phi2 x : Element n} (h1 : Homogeneous 1 phi1)
    (h2 : Homogeneous 2 phi2) (hx : Homogeneous 2 x) :
    Homogeneous (n - 1) (otherShiab eta m0 m1 m2 phi1 phi2 x) := by
  have hsx := homogeneous_otherStar eta hx
  have hf := homogeneous_bracket eta m0 h1 hsx
  have hi := homogeneous_bracket eta m1 h2 hsx
  have heq : 2 + (n - 2) = n := by omega
  rw [heq] at hi
  have hsi := homogeneous_otherStar eta hi
  simp only [Nat.sub_self] at hsi
  have ho := homogeneous_bracket eta m2 h1 hsi
  simp only [Nat.add_zero] at ho
  have hso := homogeneous_otherStar eta ho
  have heq' : 1 + (n - 2) = n - 1 := by omega
  rw [heq'] at hf
  exact homogeneous_plus hf (homogeneous_scale hso _)


/-- Extensional scalar compatibility passes through the second bracket input,
including all sparse normalization steps. -/
theorem coefficient_bracket_scaled_right (eta : Fin n → ℤ) (m : Mode)
    (x : Element n) {y' y : Element n} (c : GQ)
    (hy : ∀ f b, coefficient y' f b = coefficient y f b * c) (f b : Blade n) :
    coefficient (bracket eta m x y') f b = coefficient (bracket eta m x y) f b * c := by
  calc
    coefficient (bracket eta m x y') f b =
        coefficient (bracket eta m x (scale y c)) f b :=
      coefficient_bracket_congr eta m (fun _ _ => rfl)
        (fun f b => by rw [coefficient_scale]; exact hy f b) f b
    _ = coefficient (bracket eta m x y) f b * c :=
      coefficient_bracket_scale_right eta m x y c f b

/-- Full concrete Hodge-convention reparametrization, for every even n>=2,
every metric diagonal, all eight bracket assignments, and arbitrary homogeneous
sparse inputs. This is coefficient equality of the actual executable model;
no abstract linearity or bracket-compatibility hypotheses are assumed. -/
theorem otherShiab_reparametrization (eta : Fin n → ℤ) (hn : Even n) (hn2 : 2 ≤ n)
    (m0 m1 m2 : Mode) {phi1 phi2 x : Element n}
    (h1 : Homogeneous 1 phi1) (h2 : Homogeneous 2 phi2) (hx : Homogeneous 2 x)
    (f b : Blade n) :
    coefficient (otherShiab eta m0 m1 m2 phi1 phi2 x) f b =
      coefficient (shiab eta m0 m1 m2 phi1 (scale phi2 (rational (-1))) x) f b := by
  have hinner0 := coefficient_bracket_scale_left eta m1 phi2 (star eta x) (rational (-1))
  have hinner := coefficient_star_scaled eta (rational (-1)) hinner0
  have houter := coefficient_bracket_scaled_right eta m2 phi1 (rational (-1)) hinner
  have hsecond := coefficient_star_scaled eta (rational (-1)) houter
  rw [otherShiab_coefficient eta hn hn2 m0 m1 m2 h1 h2 hx]
  simp only [shiab, coefficient_plus, coefficient_scale]
  rw [hsecond]
  have hc : rational (-1) = (-1 : GQ) := by
    ext <;> norm_num [rational, QuadraticAlgebra.re_one, QuadraticAlgebra.im_one]
  have hh : rational (-1 / 2) = -rational (1 / 2) := by
    ext <;> norm_num [rational, QuadraticAlgebra.re_one, QuadraticAlgebra.im_one]
  rw [hc, hh]
  ring

/-- Including the final readout star introduces one overall minus sign,
while the internal convention change is precisely Phi2 ↦ -Phi2. -/
theorem otherShiab_readout_reparametrization
    (eta : Fin n → ℤ) (hn : Even n) (hn2 : 2 ≤ n)
    (m0 m1 m2 : Mode) {phi1 phi2 x : Element n}
    (h1 : Homogeneous 1 phi1) (h2 : Homogeneous 2 phi2) (hx : Homogeneous 2 x)
    (f b : Blade n) :
    coefficient (otherStar eta (otherShiab eta m0 m1 m2 phi1 phi2 x)) f b =
      -coefficient (star eta
        (shiab eta m0 m1 m2 phi1 (scale phi2 (rational (-1))) x)) f b := by
  rw [coefficient_otherStar_output eta hn hn2
    (otherShiab_degree eta hn2 m0 m1 m2 h1 h2 hx)]
  simp only [coefficient_star]
  rw [otherShiab_reparametrization eta hn hn2 m0 m1 m2 h1 h2 hx]

end B02.Concrete



#print axioms B02.Concrete.otherShiab_reparametrization
#print axioms B02.Concrete.otherShiab_readout_reparametrization

