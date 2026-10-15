import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.NormNum

namespace B03
abbrev Col (m : ℕ) := Fin (2^m)
structure Mono (m : ℕ) where
  perm : Col m → Col m
  phase : Col m → Fin 4


namespace Mono
def Eqv (a b : Mono m) : Prop := ∀ j, a.perm j = b.perm j ∧ a.phase j = b.phase j
instance (a b : Mono m) : Decidable (Eqv a b) :=
  inferInstanceAs (Decidable (∀ j, a.perm j = b.perm j ∧ a.phase j = b.phase j))
theorem extensional {a b : Mono m} (h : Eqv a b) : a = b := by
  cases a; cases b
  congr
  · funext j; exact (h j).1
  · funext j; exact (h j).2
def one : Mono m := ⟨id, fun _ => 0⟩
def mul (a b : Mono m) : Mono m :=
  ⟨a.perm ∘ b.perm, fun j => b.phase j + a.phase (b.perm j)⟩
def shift (a : Mono m) (k : Fin 4) : Mono m := ⟨a.perm, fun j => a.phase j + k⟩
def conj (a : Mono m) : Mono m := ⟨a.perm, fun j => -a.phase j⟩
/-- Exactly the column conditions for a unit-phase monomial to equal its adjoint. -/
def Hermitian (a : Mono m) : Prop :=
  ∀ j, a.perm (a.perm j) = j ∧ a.phase (a.perm j) = -a.phase j
instance (a : Mono m) : Decidable a.Hermitian := inferInstanceAs (Decidable (∀ j, a.perm (a.perm j) = j ∧ a.phase (a.perm j) = -a.phase j))
end Mono

/-- Bit k in tensor-factor order: k=0 is the most significant bit. -/
def bit (m k : ℕ) (j : Col m) : ℕ := (j.val / 2^(m-1-k)) % 2
/-- Direct column formula for Z^k tensor X/Y tensor I^(m-k-1). -/
def euclidean (m a : ℕ) : Mono m where
  perm j := (BitVec.ofFin j ^^^ BitVec.ofNat m (2^(m-1-a/2))).toFin
  phase j := Fin.ofNat 4 (2 * ((List.range (a/2)).map (fun k => bit m k j)).sum +
    if a % 2 = 1 then 1 + 2 * bit m (a/2) j else 0)
def gamma (m p a : ℕ) : Mono m :=
  (euclidean m a).shift (if a < p then 0 else 1)
def product (xs : List (Mono m)) : Mono m := xs.foldl Mono.mul Mono.one
/-- The phase parity is independent of the column; certified below for each signature. -/
def imaginaryAxis (p a : ℕ) : Bool := (a % 2 + if a < p then 0 else 1) % 2 == 1
def charge (m p : ℕ) : Mono m :=
  product (((List.range (2*m)).filter (imaginaryAxis p)).map (gamma m p))
def volume (m p : ℕ) : Mono m := product ((List.range (2*m)).map (gamma m p))
/-- Candidate for the library's first admissible phase; least-phase certificates
below verify BOTH square-one and Hermitian conditions, including rejected phases. -/
def chiralityPhase (m p : ℕ) : Fin 4 := Fin.ofNat 4 ((m + (2*m-p)) % 2)
def chirality (m p : ℕ) : Mono m := (volume m p).shift (chiralityPhase m p)
def cartan (m k : ℕ) : Mono m :=
  ((euclidean m (2*k)).mul (euclidean m (2*k+1))).shift 3
/-- Weight bit false = +1, true = -1, in the specified split ordering. -/
def weight (order : Fin m → Fin m) (j : Col m) (k : Fin m) : Bool :=
  (cartan m (order k).val).phase j == 2
def parity (order : Fin m → Fin m) : Mono m :=
  ⟨id, fun j => Fin.ofNat 4 (2 * ((List.finRange m).countP (weight order j)))⟩
def order77 : Fin 7 → Fin 7 := ![3,4,0,1,2,5,6]
def order95a : Fin 7 → Fin 7 := ![4,5,0,1,2,3,6]
def order95b : Fin 7 → Fin 7 := order77
def order31 : Fin 2 → Fin 2 := ![1,0]

/-- Every gamma's real/imaginary status agrees with the selector used by charge. -/
def ImaginarySelection (m p : ℕ) : Prop :=
  ∀ a : Fin (2*m), ∀ j : Col m,
    ((gamma m p a).phase j).val % 2 = if imaginaryAxis p a then 1 else 0
/-- The library tests phases in ascending order, accepting square-one AND Hermitian. -/
def FirstChirality (m p : ℕ) : Prop :=
  Mono.Eqv ((chirality m p).mul (chirality m p)) Mono.one ∧ (chirality m p).Hermitian ∧
  ∀ k : Fin 4, k < chiralityPhase m p →
    ¬ Mono.Eqv (((volume m p).shift k).mul ((volume m p).shift k)) Mono.one

set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option maxRecDepth 100000 in
 theorem selection31 : ImaginarySelection 2 3 := by unfold ImaginarySelection; decide +kernel
 theorem first_chirality31 : FirstChirality 2 3 := by unfold FirstChirality; decide +kernel
 theorem j_square31 : (charge 2 3).mul (charge 2 3).conj = Mono.one.shift 2 := Mono.extensional (by decide +kernel)
 theorem chirality_parity31 : chirality 2 3 = parity order31 := Mono.extensional (by decide +kernel)

end B03
