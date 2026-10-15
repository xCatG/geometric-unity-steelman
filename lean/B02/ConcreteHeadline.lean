import B02.Semantics
import B02.Headline

namespace B02.Concrete
open scoped BigOperators

/-- Evaluate a sparse element against an arbitrary coefficient weight. -/
def linearEval {n : ℕ} (x : Element n) (w : Blade n → Blade n → GQ) : GQ :=
  (x.map fun t => t.value * w t.form t.blade).sum

@[simp] theorem linearEval_nil {n : ℕ} (w : Blade n → Blade n → GQ) :
    linearEval [] w = 0 := rfl

@[simp] theorem linearEval_cons {n : ℕ} (t : Term n) (x : Element n)
    (w : Blade n → Blade n → GQ) :
    linearEval (t :: x) w = t.value * w t.form t.blade + linearEval x w := rfl

theorem linearEval_addTerm {n : ℕ} (t : Term n) (x : Element n)
    (w : Blade n → Blade n → GQ) :
    linearEval (addTerm t x) w = t.value * w t.form t.blade + linearEval x w := by
  induction x with
  | nil =>
    by_cases hz : t.value = 0 <;> simp [addTerm, hz]
  | cons u us ih =>
    by_cases he : t.form = u.form ∧ t.blade = u.blade
    · by_cases hz : t.value + u.value = 0
      · simp only [addTerm, if_pos he, if_pos hz, linearEval_cons]
        simp only [he.1, he.2]
        linear_combination -hz * w u.form u.blade
      · simp only [addTerm, if_pos he, if_neg hz, linearEval_cons]
        simp only [he.1, he.2]
        ring
    · simp only [addTerm, if_neg he, linearEval_cons, ih]
      ring

private theorem linearEval_fold {n : ℕ} (x acc : Element n)
    (w : Blade n → Blade n → GQ) :
    linearEval (x.foldl (fun z t => addTerm t z) acc) w = linearEval acc w + linearEval x w := by
  induction x generalizing acc with
  | nil => simp
  | cons t ts ih => simp only [List.foldl_cons, ih, linearEval_addTerm, linearEval_cons]; ring

@[simp] theorem linearEval_clean {n : ℕ} (x : Element n) (w : Blade n → Blade n → GQ) :
    linearEval (clean x) w = linearEval x w := by
  simpa [clean] using linearEval_fold x [] w

@[simp] theorem linearEval_star {n : ℕ} (eta : Fin n → ℤ) (x : Element n)
    (w : Blade n → Blade n → GQ) :
    linearEval (star eta x) w =
      linearEval x (fun f b => integer (starSign eta f) * w fᶜ b) := by
  simp only [star, linearEval_clean]
  simp only [linearEval, List.map_map]
  congr 1
  apply List.map_congr_left
  intro t _
  simp [mul_assoc]

/-- Bilinear kernel of the executable bracket, independent of term values. -/
def bracketWeight {n : ℕ} (eta : Fin n → ℤ) (mode : Mode)
    (tf tb uf ub f b : Blade n) : GQ :=
  if Disjoint tf uf then
    if tf ∪ uf = f ∧ (bladeMul eta tb ub).1 = b then
      let z := (bladeMul eta tb ub).2
      let w := (bladeMul eta ub tb).2
      match mode with
      | .C => integer (reorderSign tf uf * (z - w))
      | .A => integer (reorderSign tf uf * (z + w)) * imaginary
    else 0
  else 0

theorem bracketContribution_factor {n : ℕ} (eta : Fin n → ℤ) (mode : Mode)
    (t u : Term n) (f b : Blade n) : bracketContribution eta mode t u f b =
      t.value * (u.value * bracketWeight eta mode t.form t.blade u.form u.blade f b) := by
  cases mode <;> unfold bracketContribution bracketWeight <;> dsimp <;>
    split_ifs <;> ring

theorem coefficient_bracket_linear {n : ℕ} (eta : Fin n → ℤ) (mode : Mode)
    (x y : Element n) (f b : Blade n) :
    coefficient (bracket eta mode x y) f b =
      linearEval x (fun tf tb => linearEval y (fun uf ub => bracketWeight eta mode tf tb uf ub f b)) := by
  rw [coefficient_bracket]
  simp only [bracketContribution_factor, List.sum_map_mul_left, linearEval]

/-- The executable enumeration contains exactly the increasing pairs. -/
theorem mem_pairs {n : ℕ} (p : Fin n × Fin n) : p ∈ pairs n ↔ p.1 < p.2 := by
  constructor
  · intro h
    obtain ⟨a, _, ha⟩ := List.mem_flatMap.mp h
    obtain ⟨b, _, hab⟩ := List.mem_filterMap.mp ha
    split_ifs at hab with hlt
    · cases Option.some.inj hab
      exact hlt
  · intro h
    apply List.mem_flatMap.mpr
    refine ⟨p.1, List.mem_finRange _, ?_⟩
    apply List.mem_filterMap.mpr
    exact ⟨p.2, List.mem_finRange _, by simp [h]⟩

theorem nodup_pairs (n : ℕ) : (pairs n).Nodup := by
  unfold pairs
  apply List.nodup_flatMap.mpr
  constructor
  · intro a _
    apply List.Nodup.filterMap _ (List.nodup_finRange n)
    intro b c p hb hc
    simp only [Option.mem_def] at hb hc
    split_ifs at hb hc
    simp_all
    exact congrArg Prod.snd (hb.trans hc.symm)
  · apply (List.nodup_finRange n).imp
    intro a b hab p hp hq
    obtain ⟨c, _, hc⟩ := List.mem_filterMap.mp hp
    obtain ⟨d, _, hd⟩ := List.mem_filterMap.mp hq
    split_ifs at hc hd
    simp_all
    exact hab (congrArg Prod.fst (hc.trans hd.symm))

/-- Increasing pairs are determined by their two-element index set. -/
theorem pairSet_injective {n : ℕ} (p q : Fin n × Fin n)
    (hp : p.1 < p.2) (hq : q.1 < q.2)
    (he : pairSet p.1 p.2 = pairSet q.1 q.2) : p = q := by
  have hp1 : p.1 = q.1 ∨ p.1 = q.2 := by
    have := Finset.mem_insert_self p.1 ({p.2} : Blade n)
    rw [← pairSet, he] at this
    simpa [pairSet] using this
  have hp2 : p.2 = q.1 ∨ p.2 = q.2 := by
    have : p.2 ∈ pairSet p.1 p.2 := by simp [pairSet]
    rw [he] at this
    simpa [pairSet] using this
  apply Prod.ext <;> dsimp
  · rcases hp1 with h | h
    · exact h
    · rcases hp2 with h' | h' <;> omega
  · rcases hp2 with h | h
    · rcases hp1 with h' | h' <;> omega
    · exact h

private theorem sum_map_flatMap {α β γ : Type*} [AddMonoid γ]
    (l : List α) (g : α → List β) (h : β → γ) :
    ((l.flatMap g).map h).sum = (l.map fun a => ((g a).map h).sum).sum := by
  induction l with
  | nil => simp
  | cons a as ih => simp [ih]

@[simp] theorem rational_eq_algebraMap (q : ℚ) : rational q = algebraMap ℚ GQ q := rfl
@[simp] theorem integer_eq_cast (z : ℤ) : integer z = (z : GQ) := rfl

/-- The commutator coefficient for one Clifford blade pair. -/
def commKernel {n : ℕ} (eta : Fin n → ℤ) (a c b : Blade n) : GQ :=
  if (bladeMul eta a c).1 = b then
    integer ((bladeMul eta a c).2 - (bladeMul eta c a).2)
  else 0

theorem commKernel_antisymm {n : ℕ} (eta : Fin n → ℤ) (a c b : Blade n) :
    commKernel eta a c b = -commKernel eta c a b := by
  have hout : (bladeMul eta a c).1 = (bladeMul eta c a).1 := by
    simp only [bladeMul, Finset.union_comm]
  unfold commKernel
  rw [hout]
  split_ifs <;> simp [integer_eq_cast]

theorem pair_disjoint_compl_iff {n : ℕ} (p q : Fin n × Fin n)
    (hp : p.1 < p.2) (hq : q.1 < q.2) :
    Disjoint (pairSet p.1 p.2) (pairSet q.1 q.2)ᶜ ↔ p = q := by
  constructor
  · intro hd
    have hs : pairSet p.1 p.2 ⊆ pairSet q.1 q.2 := by
      intro i hi
      by_contra hn
      exact Finset.disjoint_left.mp hd hi (by simpa using hn)
    apply pairSet_injective p q hp hq
    apply Finset.eq_of_subset_of_card_le hs
    simp [pairSet, ne_of_lt hp, ne_of_lt hq]
  · rintro rfl
    exact Finset.disjoint_left.mpr (by intro i hi hn; exact Finset.mem_compl.mp hn hi)

/-- The pinned star contracts the two equal-degree form blades diagonally. -/
theorem diagonal_star_kernel {n : ℕ} (eta : Fin n → ℤ)
    (p q r : Fin n × Fin n) (hp : p.1 < p.2) (hq : q.1 < q.2)
    (f b : Blade n) :
    integer (starSign eta (pairSet q.1 q.2)) *
      bracketWeight eta .C (pairSet p.1 p.2) (pairSet p.1 p.2)
        (pairSet q.1 q.2)ᶜ (pairSet r.1 r.2) f b =
    if p = q then integer (metric eta (pairSet p.1 p.2)) *
      (if Finset.univ = f then commKernel eta (pairSet p.1 p.2) (pairSet r.1 r.2) b else 0)
    else 0 := by
  have hd := pair_disjoint_compl_iff p q hp hq
  by_cases he : p = q
  · subst q
    simp only [bracketWeight, hd, Finset.union_compl,
      integer_eq_cast, Int.cast_mul, commKernel]
    by_cases hf : Finset.univ = f
    · simp only [hf, true_and, ↓reduceIte]
      split_ifs
      · have hw := congrArg (fun z : ℤ => (z : GQ)) (pinned_hodge_weight eta (pairSet p.1 p.2))
        simp only [Int.cast_mul] at hw
        rw [show (starSign eta (pairSet p.1 p.2) : GQ) *
          ((reorderSign (pairSet p.1 p.2) (pairSet p.1 p.2)ᶜ : GQ) *
          (((bladeMul eta (pairSet p.1 p.2) (pairSet r.1 r.2)).2 -
          (bladeMul eta (pairSet r.1 r.2) (pairSet p.1 p.2)).2 : ℤ) : GQ)) =
          ((reorderSign (pairSet p.1 p.2) (pairSet p.1 p.2)ᶜ : GQ) *
          (starSign eta (pairSet p.1 p.2) : GQ)) *
          (((bladeMul eta (pairSet p.1 p.2) (pairSet r.1 r.2)).2 -
          (bladeMul eta (pairSet r.1 r.2) (pairSet p.1 p.2)).2 : ℤ) : GQ) by ring]
        rw [hw]
      · ring
    · simp [hf]
  · simp [bracketWeight, hd, he]

/-- The exact coefficient supplied by executable xi for an increasing pair pair. -/
def raisedPairValue {n : ℕ} (eta : Fin n → ℤ) (R : Curvature n)
    (q r : Fin n × Fin n) : GQ :=
  rational (R q.1 q.2 r.1 r.2 * (eta r.1 * eta r.2 : ℤ) / 2)

/-- Expansion of the actual executable B/xi expression, including both normalizations. -/
theorem coefficient_inner_B_expanded {n : ℕ} (eta : Fin n → ℤ) (R : Curvature n)
    (f b : Blade n) :
    coefficient (bracket eta .C (phiB n) (star eta (xi eta R))) f b =
      ∑ p ∈ (pairs n).toFinset, ∑ q ∈ (pairs n).toFinset, ∑ r ∈ (pairs n).toFinset,
        raisedPairValue eta R q r *
          (integer (starSign eta (pairSet q.1 q.2)) *
            bracketWeight eta .C (pairSet p.1 p.2) (pairSet p.1 p.2)
              (pairSet q.1 q.2)ᶜ (pairSet r.1 r.2) f b) := by
  rw [coefficient_bracket_linear]
  unfold phiB
  rw [linearEval]
  simp only [List.map_map, Function.comp_def, one_mul]
  simp only [linearEval_star, xi, xiWithRaising, if_true, linearEval_clean]
  simp only [linearEval, List.map_map, sum_map_flatMap, Function.comp_def]
  simp_rw [List.sum_toFinset _ (nodup_pairs n)]
  rfl

/-- Diagonal contraction of the actual executable B/xi coefficient. -/
theorem coefficient_inner_B_contracted {n : ℕ} (eta : Fin n → ℤ) (R : Curvature n)
    (f b : Blade n) :
    coefficient (bracket eta .C (phiB n) (star eta (xi eta R))) f b =
      ∑ p ∈ (pairs n).toFinset, ∑ r ∈ (pairs n).toFinset,
        raisedPairValue eta R p r * integer (metric eta (pairSet p.1 p.2)) *
          (if Finset.univ = f then commKernel eta (pairSet p.1 p.2) (pairSet r.1 r.2) b else 0) := by
  rw [coefficient_inner_B_expanded]
  apply Finset.sum_congr rfl
  intro p hp
  have hp' : p.1 < p.2 := (mem_pairs p).mp (List.mem_toFinset.mp hp)
  trans ∑ q ∈ (pairs n).toFinset, ∑ r ∈ (pairs n).toFinset,
    if p = q then raisedPairValue eta R q r * integer (metric eta (pairSet p.1 p.2)) *
      (if Finset.univ = f then commKernel eta (pairSet p.1 p.2) (pairSet r.1 r.2) b else 0)
    else 0
  · apply Finset.sum_congr rfl
    intro q hq
    apply Finset.sum_congr rfl
    intro r _
    rw [diagonal_star_kernel eta p q r hp' ((mem_pairs q).mp (List.mem_toFinset.mp hq))]
    split_ifs <;> ring
  · rw [Finset.sum_eq_single p]
    · simp
    · intro q _ hqp
      simp [Ne.symm hqp]
    · intro hnot
      exact (hnot hp).elim

private theorem antisymmetric_sum_zero {α : Type*} (s : Finset α) (w : α → α → GQ)
    (hw : ∀ a ∈ s, ∀ b ∈ s, w a b = -w b a) :
    (∑ a ∈ s, ∑ b ∈ s, w a b) = 0 := by
  have hn : (∑ a ∈ s, ∑ b ∈ s, w a b) = -(∑ a ∈ s, ∑ b ∈ s, w a b) := by
    calc
      _ = ∑ a ∈ s, ∑ b ∈ s, -w b a := by
        apply Finset.sum_congr rfl
        intro a ha
        apply Finset.sum_congr rfl
        intro b hb
        exact hw a ha b hb
      _ = _ := by rw [Finset.sum_comm]; simp only [Finset.sum_neg_distrib]
  apply QuadraticAlgebra.ext
  · have hr := congrArg QuadraticAlgebra.re hn
    simp only [QuadraticAlgebra.re_neg] at hr
    change (∑ a ∈ s, ∑ b ∈ s, w a b).re = 0
    linarith
  · have hi := congrArg QuadraticAlgebra.im hn
    simp only [QuadraticAlgebra.im_neg] at hi
    change (∑ a ∈ s, ∑ b ∈ s, w a b).im = 0
    linarith

/-- Literal CCC's inner B bracket vanishes in the actual executable model.
Only curvature pair symmetry is required: all dimensions and integer metrics work. -/
theorem headline_inner_B_concrete {n : ℕ} (eta : Fin n → ℤ) (R : Curvature n)
    (hR : ∀ a b c d, R a b c d = R c d a b) (f b : Blade n) :
    coefficient (bracket eta .C (phiB n) (star eta (xi eta R))) f b = 0 := by
  rw [coefficient_inner_B_contracted]
  apply antisymmetric_sum_zero
  intro p hp r hr
  by_cases hf : Finset.univ = f
  · simp only [if_pos hf]
    rw [commKernel_antisymm eta (pairSet p.1 p.2) (pairSet r.1 r.2) b]
    have hp' : p.1 < p.2 := (mem_pairs p).mp (List.mem_toFinset.mp hp)
    have hr' : r.1 < r.2 := (mem_pairs r).mp (List.mem_toFinset.mp hr)
    simp only [raisedPairValue, rational_eq_algebraMap, div_eq_mul_inv, map_mul,
      map_intCast, integer_eq_cast]
    have hmp : metric eta (pairSet p.1 p.2) = eta p.1 * eta p.2 := by
      simp [metric, pairSet, ne_of_lt hp']
    have hmr : metric eta (pairSet r.1 r.2) = eta r.1 * eta r.2 := by
      simp [metric, pairSet, ne_of_lt hr']
    rw [hmp, hmr, hR p.1 p.2 r.1 r.2]
    ring
  · simp [hf]

end B02.Concrete

#print axioms B02.Concrete.headline_inner_B_concrete








