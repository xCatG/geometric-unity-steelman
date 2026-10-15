import B03.Certificates
import B03.Weights
import B03.Semantics

namespace B03
/-- The common sign cancels twice, so every bivector commutes with J. -/
theorem bivector_intertwining (b g h : Mono m) (s : Fin 4) (hs : s+s=0)
    (hg : b.mul g.conj = (g.mul b).shift s)
    (hh : b.mul h.conj = (h.mul b).shift s) :
    b.mul (g.mul h).conj = (g.mul h).mul b := by
  calc
    b.mul (g.mul h).conj = (b.mul g.conj).mul h.conj := by
      rw [Mono.conj_mul, Mono.mul_assoc]
    _ = ((g.mul b).mul h.conj).shift s := by rw [hg, Mono.shift_mul]
    _ = (g.mul (h.mul b)).shift (s+s) := by
      rw [Mono.mul_assoc, hh, Mono.mul_shift, Mono.shift_shift]
    _ = (g.mul h).mul b := by rw [hs, Mono.shift_zero, Mono.mul_assoc]
 theorem all_bivectors (h : JGamma m p s) (hs : s+s=0) (a b : Fin (2*m)) :
    (charge m p).mul ((gamma m p a).mul (gamma m p b)).conj =
      ((gamma m p a).mul (gamma m p b)).mul (charge m p) :=
  bivector_intertwining _ _ _ s hs (Mono.extensional (h a)) (Mono.extensional (h b))

/-- The optimized selector is exactly the Python all-imaginary-entry predicate. -/
theorem imaginary_selector_iff (h : ImaginarySelection m p) (a : Fin (2*m)) :
    imaginaryAxis p a = true ↔ ∀ j : Col m, ((gamma m p a).phase j).val % 2 = 1 := by
  constructor
  · intro ha j; rw [h a j, ha]; rfl
  · intro hj
    cases hs : imaginaryAxis p a with
    | true => rfl
    | false =>
      have hz := hj ⟨0, Nat.two_pow_pos m⟩
      rw [h a _, hs] at hz
      contradiction

noncomputable section
 theorem real_structure_square77 (v : Spinor 7) : J (charge 7 7) (J (charge 7 7) v) = v := by
  rw [J_squared, j_square77, act_one]
 theorem real_structure_square95 (v : Spinor 7) : J (charge 7 9) (J (charge 7 9) v) = -v := by
  rw [J_squared, j_square95, act_shift_two, act_one]
 theorem real_structure_square31 (v : Spinor 2) : J (charge 2 3) (J (charge 2 3) v) = -v := by
  rw [J_squared, j_square31, act_shift_two, act_one]

 theorem J_all_generators77 (a b : Fin 14) (v : Spinor 7) :
    J (charge 7 7) (act ((gamma 7 7 a).mul (gamma 7 7 b)) v) =
      act ((gamma 7 7 a).mul (gamma 7 7 b)) (J (charge 7 7) v) :=
  J_intertwines _ _ _ (all_bivectors j_gamma77 (by decide) a b) v
 theorem J_all_generators95 (a b : Fin 14) (v : Spinor 7) :
    J (charge 7 9) (act ((gamma 7 9 a).mul (gamma 7 9 b)) v) =
      act ((gamma 7 9 a).mul (gamma 7 9 b)) (J (charge 7 9) v) :=
  J_intertwines _ _ _ (all_bivectors j_gamma95 (by decide) a b) v
 theorem J_all_generators31 (a b : Fin 4) (v : Spinor 2) :
    J (charge 2 3) (act ((gamma 2 3 a).mul (gamma 2 3 b)) v) =
      act ((gamma 2 3 a).mul (gamma 2 3 b)) (J (charge 2 3) v) :=
  J_intertwines _ _ _ (all_bivectors j_gamma31 (by decide) a b) v
 theorem J_chirality77 (v : Spinor 7) :
    J (charge 7 7) (act (chirality 7 7) v) = act (chirality 7 7) (J (charge 7 7) v) :=
  J_intertwines _ _ _ j_chirality77 v
 theorem J_chirality95 (v : Spinor 7) :
    J (charge 7 9) (act (chirality 7 9) v) = act (chirality 7 9) (J (charge 7 9) v) :=
  J_intertwines _ _ _ j_chirality95 v
 theorem J_chirality31 (v : Spinor 2) :
    J (charge 2 3) (act (chirality 2 3) v) = -act (chirality 2 3) (J (charge 2 3) v) := by
  have h := J_intertwines (charge 2 3) (chirality 2 3) ((chirality 2 3).shift 2)
    (by rw [Mono.shift_mul]; exact j_chirality31) v
  simpa using h

 theorem clifford_operators (h : Clifford m p) (a b : Fin (2*m)) (v : Spinor m) :
    act (gamma m p a) (act (gamma m p b) v) + act (gamma m p b) (act (gamma m p a) v) =
    (if a = b then (if a.val < p then (2 : ℂ) else -2) else 0) • v := by
  by_cases he : a = b
  · subst b
    have hs := congrArg (fun g => act g v) (Mono.extensional (h.1 a))
    by_cases ha : a.val < p
    · simp [ha, act_mul] at hs
      simp [hs, ha, two_smul]
    · simp [ha, act_mul] at hs
      simp [hs, ha, two_smul, neg_smul]
  · simp only [if_neg he, zero_smul]
    by_cases hab : a < b
    · have hs := congrArg (fun g => act g v) (Mono.extensional (h.2 a b hab))
      simp only [act_mul, act_shift_two] at hs
      rw [hs]; simp
    · have hba : b < a := by omega
      have hs := congrArg (fun g => act g v) (Mono.extensional (h.2 b a hba))
      simp only [act_mul, act_shift_two] at hs
      rw [hs]; simp

 theorem clifford_relations77 (a b : Fin 14) (v : Spinor 7) :
    act (gamma 7 7 a) (act (gamma 7 7 b) v) + act (gamma 7 7 b) (act (gamma 7 7 a) v) =
      (if a = b then (if a.val < 7 then (2 : ℂ) else -2) else 0) • v :=
  clifford_operators clifford77 a b v
 theorem clifford_relations95 (a b : Fin 14) (v : Spinor 7) :
    act (gamma 7 9 a) (act (gamma 7 9 b) v) + act (gamma 7 9 b) (act (gamma 7 9 a) v) =
      (if a = b then (if a.val < 9 then (2 : ℂ) else -2) else 0) • v :=
  clifford_operators clifford95 a b v
 theorem clifford_relations31 (a b : Fin 4) (v : Spinor 2) :
    act (gamma 2 3 a) (act (gamma 2 3 b) v) + act (gamma 2 3 b) (act (gamma 2 3 a) v) =
      (if a = b then (if a.val < 3 then (2 : ℂ) else -2) else 0) • v :=
  clifford_operators clifford31 a b v

 theorem chirality_preserves77 (v : Spinor 7) (s : ℝ)
    (hv : act (chirality 7 7) v = (s : ℂ) • v) :
    act (chirality 7 7) (J (charge 7 7) v) = (s : ℂ) • J (charge 7 7) v := by
  rw [← J_chirality77, hv]; simp
 theorem chirality_preserves95 (v : Spinor 7) (s : ℝ)
    (hv : act (chirality 7 9) v = (s : ℂ) • v) :
    act (chirality 7 9) (J (charge 7 9) v) = (s : ℂ) • J (charge 7 9) v := by
  rw [← J_chirality95, hv]; simp
 theorem chirality_exchanges31 (v : Spinor 2) (s : ℝ)
    (hv : act (chirality 2 3) v = (s : ℂ) • v) :
    act (chirality 2 3) (J (charge 2 3) v) = (-s : ℂ) • J (charge 2 3) v := by
  have h := J_chirality31 v
  rw [hv] at h
  have h' := congrArg Neg.neg h
  simpa using h'.symm

 theorem cartan_commutes (h : CartanSpec m) (k l : Fin m) (v : Spinor m) :
    act (cartan m k) (act (cartan m l) v) = act (cartan m l) (act (cartan m k) v) := by
  rw [← act_mul, ← act_mul, Mono.diagonal_commute _ _ (fun j => (h k j).1) (fun j => (h l j).1)]
 theorem cartan_eigenvalues (h : CartanSpec m) (k : Fin m) (j : Col m) :
    act (cartan m k) (Pi.single j 1) = Pi.single j 1 ∨
    act (cartan m k) (Pi.single j 1) = -Pi.single j 1 := by
  obtain ⟨hp,hz|hz⟩ := h k j
  · left; simp [act_single, hp, hz, phaseValue]
  · right; simp [act_single, hp, hz, phaseValue, Pi.single_neg]

 theorem every_weight31 : ∀ w : Fin 2 → Bool, ∃! j : Col 2, weight order31 j = w :=
  weight_exactly_once _ weight_inverse31
 theorem every_weight77 : ∀ w : Fin 7 → Bool, ∃! j : Col 7, weight order77 j = w :=
  weight_exactly_once _ weight_inverse77
 theorem every_weight95a : ∀ w : Fin 7 → Bool, ∃! j : Col 7, weight order95a j = w :=
  weight_exactly_once _ weight_inverse95a
 theorem every_weight95b : ∀ w : Fin 7 → Bool, ∃! j : Col 7, weight order95b j = w :=
  weight_exactly_once _ weight_inverse95b
end
end B03
