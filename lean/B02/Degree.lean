import B02.Concrete

namespace B02.Concrete

/-- Every stored term has the indicated form degree. The zero element is homogeneous
in every degree, as required for wedges that vanish. -/
def Homogeneous (k : ℕ) (x : Element n) : Prop := ∀ t ∈ x, t.form.card = k

theorem addTerm_form_property (P : Blade n → Prop) (t : Term n) (x : Element n)
    (ht : P t.form) (hx : ∀ u ∈ x, P u.form) : ∀ u ∈ addTerm t x, P u.form := by
  induction x with
  | nil => simp only [addTerm]; split <;> simp_all
  | cons u us ih =>
    simp only [addTerm]
    split
    · split <;> simp_all
    · simp_all

theorem fold_addTerm_form_property (P : Blade n → Prop) (x acc : Element n)
    (hx : ∀ u ∈ x, P u.form) (ha : ∀ u ∈ acc, P u.form) :
    ∀ u ∈ x.foldl (fun a t => addTerm t a) acc, P u.form := by
  induction x generalizing acc with
  | nil => simpa using ha
  | cons t ts ih =>
    apply ih
    · intro u hu; exact hx u (by simp [hu])
    · exact addTerm_form_property P t acc (hx t (by simp)) ha

theorem clean_form_property (P : Blade n → Prop) (x : Element n)
    (hx : ∀ t ∈ x, P t.form) : ∀ t ∈ clean x, P t.form :=
  fold_addTerm_form_property P x [] hx (by simp)

theorem homogeneous_plus {k : ℕ} {x y : Element n}
    (hx : Homogeneous k x) (hy : Homogeneous k y) : Homogeneous k (plus x y) :=
  fold_addTerm_form_property (fun f => f.card = k) y x hy hx

theorem homogeneous_scale {k : ℕ} {x : Element n}
    (hx : Homogeneous k x) (c : GQ) : Homogeneous k (scale x c) := by
  apply clean_form_property (fun f => f.card = k)
  intro t ht
  obtain ⟨u, hu, rfl⟩ := List.mem_map.mp ht
  exact hx u hu

theorem homogeneous_star (eta : Fin n → ℤ) {k : ℕ} {x : Element n}
    (hx : Homogeneous k x) : Homogeneous (n - k) (star eta x) := by
  apply clean_form_property (fun f => f.card = n - k)
  intro t ht
  obtain ⟨u, hu, rfl⟩ := List.mem_map.mp ht
  simp [Finset.card_compl, hx u hu]

theorem homogeneous_bracket (eta : Fin n → ℤ) (m : Mode) {k l : ℕ}
    {x y : Element n} (hx : Homogeneous k x) (hy : Homogeneous l y) :
    Homogeneous (k + l) (bracket eta m x y) := by
  apply clean_form_property (fun f => f.card = k + l)
  intro v hv
  obtain ⟨t, ht, hv⟩ := List.mem_flatMap.mp hv
  obtain ⟨u, hu, he⟩ := List.mem_filterMap.mp hv
  split at he
  next hd =>
    simp only [Option.some.injEq] at he
    subst v
    simp only
    rw [Finset.card_union_of_disjoint hd, hx t ht, hy u hu]
  next => simp at he

/-- Test 1, for the executable model itself, all dimensions n>=2 and all eight modes. -/
theorem shiab_degree (eta : Fin n → ℤ) (hn : 2 ≤ n) (m0 m1 m2 : Mode)
    {phi1 phi2 x : Element n} (h1 : Homogeneous 1 phi1)
    (h2 : Homogeneous 2 phi2) (hx : Homogeneous 2 x) :
    Homogeneous (n - 1) (shiab eta m0 m1 m2 phi1 phi2 x) := by
  have hsx := homogeneous_star eta hx
  have hf := homogeneous_bracket eta m0 h1 hsx
  have hi := homogeneous_bracket eta m1 h2 hsx
  have heq : 2 + (n - 2) = n := by omega
  rw [heq] at hi
  have hsi := homogeneous_star eta hi
  simp only [Nat.sub_self] at hsi
  have ho := homogeneous_bracket eta m2 h1 hsi
  simp only [Nat.add_zero] at ho
  have hso := homogeneous_star eta ho
  have heq' : 1 + (n - 2) = n - 1 := by omega
  rw [heq'] at hf
  exact homogeneous_plus hf (homogeneous_scale hso _)

end B02.Concrete

