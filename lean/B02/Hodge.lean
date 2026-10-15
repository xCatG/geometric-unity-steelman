import B02.Signs
import Mathlib.Algebra.Group.Nat.Even

namespace B02

/-- The opposite convention differs by (-1)^k on k-forms in every even dimension. -/
theorem even_dimension_star_parity (n k : ℕ) (hn : Even n) (hk : k ≤ n) :
    (-1 : ℤ) ^ (k * (n - k)) = (-1) ^ k := by
  apply neg_one_pow_congr
  simp [Nat.even_mul, Nat.even_sub hk, hn]

def oppositeStarSign {n : ℕ} (eta : Fin n → ℤ) (a : Blade n) : ℤ :=
  (-1) ^ (a.card * (n - a.card)) * starSign eta a

theorem oppositeStarSign_degree {n : ℕ} (eta : Fin n → ℤ)
    (hn : Even n) (a : Blade n) :
    oppositeStarSign eta a = (-1) ^ a.card * starSign eta a := by
  unfold oppositeStarSign
  rw [even_dimension_star_parity n a.card hn (by simpa using a.card_le_univ)]

/-- Input star is unchanged, even without the even-n assumption. -/
theorem oppositeStarSign_two {n : ℕ} (eta : Fin n → ℤ)
    (a : Blade n) (ha : a.card = 2) : oppositeStarSign eta a = starSign eta a := by
  unfold oppositeStarSign
  rw [ha, (show Even (2 * (n - 2)) from even_two.mul_right _).neg_one_pow, one_mul]

theorem oppositeStarSign_top {n : ℕ} (eta : Fin n → ℤ)
    (a : Blade n) (ha : a.card = n) : oppositeStarSign eta a = starSign eta a := by
  simp [oppositeStarSign, ha]

theorem oppositeStarSign_one {n : ℕ} (eta : Fin n → ℤ) (hn : Even n)
    (a : Blade n) (ha : a.card = 1) : oppositeStarSign eta a = -starSign eta a := by
  rw [oppositeStarSign_degree eta hn a, ha]
  simp

/-- Reading off the (n-1)-form introduces one further global minus sign. -/
theorem oppositeStarSign_output {n : ℕ} (eta : Fin n → ℤ)
    (hn : Even n) (hn2 : 2 ≤ n) (a : Blade n) (ha : a.card = n - 1) :
    oppositeStarSign eta a = -starSign eta a := by
  have ho : Odd (n - 1) := by
    obtain ⟨k,hk⟩ := hn
    exact ⟨k - 1, by omega⟩
  rw [oppositeStarSign_degree eta (by exact hn) a, ha, ho.neg_one_pow]
  simp

end B02
