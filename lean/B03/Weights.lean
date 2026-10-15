import B03.Model

namespace B03
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def CartanSpec (m : ℕ) : Prop := ∀ k : Fin m, ∀ j : Col m,
  (cartan m k).perm j = j ∧ ((cartan m k).phase j = 0 ∨ (cartan m k).phase j = 2)
 theorem cartan2 : CartanSpec 2 := by unfold CartanSpec; decide +kernel
 theorem cartan7 : CartanSpec 7 := by unfold CartanSpec; decide +kernel

/-- Inverse of the split-ordered weight map, interpreting minus signs as binary 1. -/
def encode (order : Fin m → Fin m) (w : Fin m → Bool) : Col m :=
  ⟨((List.finRange m).map (fun k => if w k then 2^(m-1-(order k).val) else 0)).sum % 2^m,
   Nat.mod_lt _ (Nat.two_pow_pos m)⟩
def WeightInverse (order : Fin m → Fin m) : Prop :=
  (∀ j, encode order (weight order j) = j) ∧
  (∀ w k, weight order (encode order w) k = w k)
 theorem weight_inverse31 : WeightInverse order31 := by unfold WeightInverse; decide +kernel
 theorem weight_inverse77 : WeightInverse order77 := by unfold WeightInverse; decide +kernel
 theorem weight_inverse95a : WeightInverse order95a := by unfold WeightInverse; decide +kernel
 theorem weight_inverse95b : WeightInverse order95b := weight_inverse77
/-- Every sign pattern has exactly one column, not merely a distinctness/count check. -/
 theorem weight_exactly_once (order : Fin m → Fin m) (h : WeightInverse order) :
    ∀ w : Fin m → Bool, ∃! j : Col m, weight order j = w := by
  intro w
  refine ⟨encode order w, funext (h.2 w), ?_⟩
  intro j hj
  rw [← h.1 j, hj]

/-- A true bit records a minus sign in the J weight-sign tuple. -/
def JWeight (p : ℕ) (order : Fin m → Fin m) (flips : Fin m → Bool) : Prop :=
  ∀ j k, weight order ((charge m p).perm j) k = (weight order j k ^^ flips k)
 theorem j_weight31 : JWeight 3 order31 ![false,true] := by unfold JWeight; decide +kernel
 theorem j_weight77 : JWeight 7 order77 ![false,true,true,true,true,true,true] := by
  unfold JWeight; decide +kernel
 theorem j_weight95a : JWeight 9 order95a ![false,true,true,true,true,true,true] := by
  unfold JWeight; decide +kernel
 theorem j_weight95b : JWeight 9 order95b ![true,false,true,true,true,true,true] := by
  unfold JWeight; decide +kernel
end B03
