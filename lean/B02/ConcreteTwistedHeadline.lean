import B02.TwistedHeadline
import B02.ConcreteHeadline

namespace B02
open scoped BigOperators

private theorem inversion_transpose {n : ℕ} (a b : Blade n) :
    (∑ i ∈ a, (b.filter (fun j => j < i)).card) =
      ∑ j ∈ b, (a.filter (fun i => j < i)).card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]

/-- Complementing a first input removes its inversions from the full volume count. -/
theorem reorderSign_compl_left {n : ℕ} (a b : Blade n) :
    reorderSign aᶜ b = reorderSign Finset.univ b * reorderSign a b := by
  have h : reorderSign aᶜ b * reorderSign a b = reorderSign Finset.univ b := by
    unfold reorderSign
    rw [← pow_add, Finset.sum_compl_add_sum]
  calc
    _ = reorderSign aᶜ b * (reorderSign a b * reorderSign a b) := by rw [reorderSign_sq, mul_one]
    _ = _ := by rw [← mul_assoc, h]

/-- The analogous complement identity in the second input. -/
theorem reorderSign_compl_right {n : ℕ} (a b : Blade n) :
    reorderSign a bᶜ = reorderSign a Finset.univ * reorderSign a b := by
  have h : reorderSign a bᶜ * reorderSign a b = reorderSign a Finset.univ := by
    unfold reorderSign
    rw [inversion_transpose a bᶜ, inversion_transpose a b,
      inversion_transpose a Finset.univ, ← pow_add, Finset.sum_compl_add_sum]
  calc
    _ = reorderSign a bᶜ * (reorderSign a b * reorderSign a b) := by rw [reorderSign_sq, mul_one]
    _ = _ := by rw [← mul_assoc, h]

/-- The metric factors in the volume-twisted commutator cover a union once. -/
theorem metric_union_compl_inter {n : ℕ} (eta : Fin n → ℤ) (a b : Blade n) :
    metric eta a * metric eta (aᶜ ∩ b) = metric eta (a ∪ b) := by
  have hd : Disjoint a (aᶜ ∩ b) := Finset.disjoint_left.mpr (by
    intro i hi hn
    exact Finset.mem_compl.mp (Finset.mem_inter.mp hn).1 hi)
  have hu : a ∪ (aᶜ ∩ b) = a ∪ b := by
    ext i
    simp only [Finset.mem_union, Finset.mem_inter, Finset.mem_compl]
    tauto
  unfold metric
  rw [← Finset.prod_union hd, hu]

namespace Concrete

/-- Coefficient from right-multiplying an increasing blade by volume. -/
def volumeFactor {n : ℕ} (eta : Fin n → ℤ) (a : Blade n) : ℤ :=
  reorderSign a Finset.univ * metric eta a

/-- The twisted commutator factors through a manifestly symmetric metric weight. -/
theorem twisted_coefficient_normal_form {n : ℕ} (eta : Fin n → ℤ)
    (a b : Blade n) (hb : Even b.card) :
    volumeFactor eta a * ((bladeMul eta aᶜ b).2 - (bladeMul eta b aᶜ).2) =
      reorderSign a Finset.univ * reorderSign b Finset.univ *
        (reorderSign a b - reorderSign b a) * metric eta (a ∪ b) := by
  simp only [volumeFactor, bladeMul]
  rw [reorderSign_compl_left, reorderSign_compl_right,
    ← reorderSign_volume_even b hb, Finset.inter_comm b aᶜ]
  calc
    _ = reorderSign a Finset.univ * reorderSign b Finset.univ *
        (reorderSign a b - reorderSign b a) * (metric eta a * metric eta (aᶜ ∩ b)) := by ring
    _ = _ := by rw [metric_union_compl_inter]

/-- Actual sparse twisted commutator coefficients are antisymmetric on even blades. -/
theorem twisted_coefficient_antisymm {n : ℕ} (eta : Fin n → ℤ)
    (a b : Blade n) (ha : Even a.card) (hb : Even b.card) :
    volumeFactor eta a * ((bladeMul eta aᶜ b).2 - (bladeMul eta b aᶜ).2) =
      -(volumeFactor eta b * ((bladeMul eta bᶜ a).2 - (bladeMul eta a bᶜ).2)) := by
  rw [twisted_coefficient_normal_form eta a b hb, twisted_coefficient_normal_form eta b a ha,
    Finset.union_comm b a]
  ring

/-- The output blade of the swapped twisted products agrees. -/
theorem twisted_output_symm {n : ℕ} (eta : Fin n → ℤ) (a b : Blade n) :
    (bladeMul eta aᶜ b).1 = (bladeMul eta bᶜ a).1 := by
  ext i
  simp only [bladeMul, Finset.mem_union, Finset.mem_sdiff, Finset.mem_compl]
  tauto

def twistedCommKernel {n : ℕ} (eta : Fin n → ℤ) (a c b : Blade n) : GQ :=
  integer (volumeFactor eta a) * commKernel eta aᶜ c b

theorem twistedCommKernel_antisymm {n : ℕ} (eta : Fin n → ℤ) (a c b : Blade n)
    (ha : Even a.card) (hc : Even c.card) :
    twistedCommKernel eta a c b = -twistedCommKernel eta c a b := by
  unfold twistedCommKernel commKernel
  rw [twisted_output_symm eta a c]
  split_ifs
  · simpa only [integer_eq_cast, Int.cast_mul, Int.cast_neg] using
      congrArg (fun z : ℤ => (z : GQ)) (twisted_coefficient_antisymm eta a c ha hc)
  · ring

/-- The exact volume product exposes the complement blade and its coefficient. -/
theorem bladeMul_volume_exact {n : ℕ} (eta : Fin n → ℤ) (a : Blade n) :
    bladeMul eta a Finset.univ = (aᶜ, volumeFactor eta a) := by
  apply Prod.ext
  · ext i
    simp [bladeMul]
  · simp [bladeMul, volumeFactor]

@[simp] theorem linearEval_rightMulVolume {n : ℕ} (eta : Fin n → ℤ) (phase : GQ)
    (x : Element n) (w : Blade n → Blade n → GQ) :
    linearEval (rightMulVolume eta phase x) w =
      linearEval x (fun f a => phase * integer (volumeFactor eta a) * w f aᶜ) := by
  simp only [rightMulVolume, linearEval_clean]
  simp only [linearEval, List.map_map, bladeMul_volume_exact]
  congr 1
  apply List.map_congr_left
  intro t _
  simp only [Function.comp_def]
  ring

/-- Pinned star contraction, allowing an arbitrary Clifford blade in the B slot. -/
theorem diagonal_star_kernel_general {n : ℕ} (eta : Fin n → ℤ)
    (p q r : Fin n × Fin n) (a : Blade n)
    (hp : p.1 < p.2) (hq : q.1 < q.2) (f b : Blade n) :
    integer (starSign eta (pairSet q.1 q.2)) *
      bracketWeight eta .C (pairSet p.1 p.2) a
        (pairSet q.1 q.2)ᶜ (pairSet r.1 r.2) f b =
    if p = q then integer (metric eta (pairSet p.1 p.2)) *
      (if Finset.univ = f then commKernel eta a (pairSet r.1 r.2) b else 0)
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
        linear_combination (((bladeMul eta a (pairSet r.1 r.2)).2 -
          (bladeMul eta (pairSet r.1 r.2) a).2 : ℤ) : GQ) * hw
      · ring
    · simp [hf]
  · simp [bracketWeight, hd, he]

private theorem twisted_sum_map_flatMap {α β γ : Type*} [AddMonoid γ]
    (l : List α) (g : α → List β) (h : β → γ) :
    ((l.flatMap g).map h).sum = (l.map fun a => ((g a).map h).sum).sum := by
  induction l with
  | nil => simp
  | cons a as ih => simp [ih]

/-- Full expansion of executable B-prime with its arbitrary chirality phase. -/
theorem coefficient_inner_BPrime_expanded {n : ℕ} (eta : Fin n → ℤ) (R : Curvature n)
    (phase : GQ) (f b : Blade n) :
    coefficient (bracket eta .C (phiBPrime eta phase) (star eta (xi eta R))) f b =
      ∑ p ∈ (pairs n).toFinset,
        (imaginary * phase) * integer (volumeFactor eta (pairSet p.1 p.2)) *
          (∑ q ∈ (pairs n).toFinset, ∑ r ∈ (pairs n).toFinset,
            raisedPairValue eta R q r *
              (integer (starSign eta (pairSet q.1 q.2)) *
                bracketWeight eta .C (pairSet p.1 p.2) (pairSet p.1 p.2)ᶜ
                  (pairSet q.1 q.2)ᶜ (pairSet r.1 r.2) f b)) := by
  rw [coefficient_bracket_linear]
  unfold phiBPrime
  rw [linearEval_rightMulVolume]
  unfold phiB
  rw [linearEval]
  simp only [List.map_map, Function.comp_def, one_mul]
  simp only [linearEval_star, xi, xiWithRaising, if_true, linearEval_clean]
  simp only [linearEval, List.map_map, twisted_sum_map_flatMap, Function.comp_def]
  simp_rw [List.sum_toFinset _ (nodup_pairs n)]
  rfl

/-- Exact diagonal contraction of the executable B-prime coefficient. -/
theorem coefficient_inner_BPrime_contracted {n : ℕ} (eta : Fin n → ℤ) (R : Curvature n)
    (phase : GQ) (f b : Blade n) :
    coefficient (bracket eta .C (phiBPrime eta phase) (star eta (xi eta R))) f b =
      ∑ p ∈ (pairs n).toFinset, ∑ r ∈ (pairs n).toFinset,
        (imaginary * phase) * raisedPairValue eta R p r * integer (metric eta (pairSet p.1 p.2)) *
          (if Finset.univ = f then twistedCommKernel eta (pairSet p.1 p.2) (pairSet r.1 r.2) b else 0) := by
  rw [coefficient_inner_BPrime_expanded]
  apply Finset.sum_congr rfl
  intro p hp
  have hp' : p.1 < p.2 := (mem_pairs p).mp (List.mem_toFinset.mp hp)
  rw [Finset.sum_eq_single p]
  · rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro r _
    rw [diagonal_star_kernel_general eta p p r (pairSet p.1 p.2)ᶜ hp' hp']
    simp only [ite_true]
    by_cases hf : Finset.univ = f
    · simp only [if_pos hf, twistedCommKernel]
      ring
    · simp [hf]
  · intro q hq hqp
    apply Finset.sum_eq_zero
    intro r _
    rw [diagonal_star_kernel_general eta p q r (pairSet p.1 p.2)ᶜ hp'
      ((mem_pairs q).mp (List.mem_toFinset.mp hq))]
    simp [Ne.symm hqp]
  · intro hnot
    exact (hnot hp).elim

private theorem twisted_antisymmetric_sum_zero {α : Type*} (s : Finset α) (w : α → α → GQ)
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

/-- Literal CCC's inner B-prime bracket vanishes in the actual executable model.
This is stronger than the even-dimensional claim: all dimensions, arbitrary integer
metrics, and every chirality phase work. Only curvature pair symmetry is required.
No associativity of the sparse product is assumed. -/
theorem headline_inner_BPrime_concrete {n : ℕ} (eta : Fin n → ℤ) (R : Curvature n)
    (hR : ∀ a b c d, R a b c d = R c d a b) (phase : GQ) (f b : Blade n) :
    coefficient (bracket eta .C (phiBPrime eta phase) (star eta (xi eta R))) f b = 0 := by
  rw [coefficient_inner_BPrime_contracted]
  apply twisted_antisymmetric_sum_zero
  intro p hp r hr
  by_cases hf : Finset.univ = f
  · simp only [if_pos hf]
    have hp' : p.1 < p.2 := (mem_pairs p).mp (List.mem_toFinset.mp hp)
    have hr' : r.1 < r.2 := (mem_pairs r).mp (List.mem_toFinset.mp hr)
    have hpEven : Even (pairSet p.1 p.2).card := by simp [pairSet, ne_of_lt hp']
    have hrEven : Even (pairSet r.1 r.2).card := by simp [pairSet, ne_of_lt hr']
    rw [twistedCommKernel_antisymm eta (pairSet p.1 p.2) (pairSet r.1 r.2) b hpEven hrEven]
    simp only [raisedPairValue, rational_eq_algebraMap, div_eq_mul_inv, map_mul,
      map_intCast, integer_eq_cast]
    have hmp : metric eta (pairSet p.1 p.2) = eta p.1 * eta p.2 := by
      simp [metric, pairSet, ne_of_lt hp']
    have hmr : metric eta (pairSet r.1 r.2) = eta r.1 * eta r.2 := by
      simp [metric, pairSet, ne_of_lt hr']
    rw [hmp, hmr, hR p.1 p.2 r.1 r.2]
    ring
  · simp [hf]

end Concrete
end B02



#print axioms B02.reorderSign_compl_left
#print axioms B02.reorderSign_compl_right
#print axioms B02.Concrete.twisted_coefficient_antisymm
#print axioms B02.Concrete.headline_inner_BPrime_concrete
