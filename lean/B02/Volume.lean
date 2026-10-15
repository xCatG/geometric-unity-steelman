import B02.Concrete

/-! Concrete Clifford volume commutation, using exactly the Python inversion-count sign. The result holds in every dimension and for arbitrary metric coefficients. -/

namespace B02
open scoped BigOperators

private theorem volume_count (n : ℕ) (i : Fin n) :
    ((Finset.univ : Blade n).filter (fun j => j < i)).card +
      ((Finset.univ : Blade n).filter (fun j => i < j)).card = n - 1 := by
  have h := Finset.filter_card_add_filter_neg_card_eq_card
    (s := (Finset.univ : Blade n)) (fun j => j < i)
  have hs : ((Finset.univ : Blade n).filter (fun j => ¬ j < i)) =
      insert i ((Finset.univ : Blade n).filter (fun j => i < j)) := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert]
    omega
  rw [hs, Finset.card_insert_of_notMem] at h
  · simp only [Finset.card_univ, Fintype.card_fin] at h
    omega
  · simp

private theorem inversion_volume_sum {n : ℕ} (a : Blade n) :
    (∑ i ∈ a, ((Finset.univ : Blade n).filter (fun j => j < i)).card) +
      (∑ j : Fin n, (a.filter (fun i => i < j)).card) = a.card * (n - 1) := by
  have hswap : (∑ j : Fin n, (a.filter (fun i => i < j)).card) =
      ∑ i ∈ a, ((Finset.univ : Blade n).filter (fun j => i < j)).card := by
    simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
    rw [Finset.sum_comm]
  rw [hswap, ← Finset.sum_add_distrib]
  simp_rw [volume_count]
  simp

/-- Every even-grade blade has equal reordering signs on the two sides of volume. -/
theorem reorderSign_volume_even {n : ℕ} (a : Blade n) (ha : Even a.card) :
    reorderSign a Finset.univ = reorderSign Finset.univ a := by
  have hprod : reorderSign a Finset.univ * reorderSign Finset.univ a = 1 := by
    unfold reorderSign
    rw [← pow_add, inversion_volume_sum]
    exact (ha.mul_right (n - 1)).neg_one_pow
  calc
    reorderSign a Finset.univ = reorderSign a Finset.univ *
        (reorderSign Finset.univ a * reorderSign Finset.univ a) := by rw [reorderSign_sq, mul_one]
    _ = reorderSign Finset.univ a := by rw [← mul_assoc, hprod, one_mul]

theorem reorderSign_volume_pair {n : ℕ} (a : Blade n) (ha : a.card = 2) :
    reorderSign a Finset.univ = reorderSign Finset.univ a :=
  reorderSign_volume_even a (by rw [ha]; decide)

namespace Concrete

/-- The executable Clifford product with volume commutes for every even-grade blade. -/
theorem bladeMul_volume_even {n : ℕ} (eta : Fin n → ℤ) (a : Blade n)
    (ha : Even a.card) : bladeMul eta a Finset.univ = bladeMul eta Finset.univ a := by
  simp only [bladeMul, Finset.inter_univ, Finset.univ_inter,
    Finset.union_comm]
  rw [reorderSign_volume_even a ha]

theorem bladeMul_volume_pair {n : ℕ} (eta : Fin n → ℤ) (a : Blade n)
    (ha : a.card = 2) : bladeMul eta a Finset.univ = bladeMul eta Finset.univ a :=
  bladeMul_volume_even eta a (by rw [ha]; decide)

/-- The actual increasing-pair basis used by phiB commutes with volume. -/
theorem bladeMul_volume_bivector {n : ℕ} (eta : Fin n → ℤ) (a b : Fin n)
    (hab : a ≠ b) : bladeMul eta (pairSet a b) Finset.univ =
      bladeMul eta Finset.univ (pairSet a b) := by
  apply bladeMul_volume_pair
  simp [pairSet, hab]

end Concrete
end B02


#print axioms B02.reorderSign_volume_even
#print axioms B02.Concrete.bladeMul_volume_even
#print axioms B02.Concrete.bladeMul_volume_bivector

