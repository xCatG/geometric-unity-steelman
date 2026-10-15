import B02.Signs
import Mathlib.Algebra.QuadraticAlgebra

/-!
# Executable finite-dimensional model of `gu.cliffform` and `gu.shiab`

All basis sets are subsets of `Fin n`; out-of-dimension indices cannot be represented.
Coefficients are exact Gaussian rationals. Sparse lists are normalized by `addTerm`.
`coefficient` gives their extensional meaning, independent of list order.
The metric and reordering convention are the SAME definitions as `B02.Signs`.
Chirality phase is an explicit argument; no unproved identification with a matrix
representation is built into the model. The executable bridge checks Python's phase.
-/
namespace B02.Concrete

abbrev GQ := QuadraticAlgebra ℚ (-1) 0

def imaginary : GQ := ⟨0, 1⟩
def rational (q : ℚ) : GQ := ⟨q, 0⟩
def integer (z : ℤ) : GQ := rational z

structure Term (n : ℕ) where
  form : Blade n
  blade : Blade n
  value : GQ
  deriving DecidableEq

abbrev Element (n : ℕ) := List (Term n)

def addTerm (t : Term n) : Element n → Element n
  | [] => if t.value = 0 then [] else [t]
  | u :: us =>
    if t.form = u.form ∧ t.blade = u.blade then
      if t.value + u.value = 0 then us
      else { u with value := t.value + u.value } :: us
    else u :: addTerm t us

def clean (x : Element n) : Element n := x.foldl (fun acc t => addTerm t acc) []
def plus (x y : Element n) : Element n := y.foldl (fun acc t => addTerm t acc) x
def scale (x : Element n) (c : GQ) : Element n :=
  clean (x.map fun t => { t with value := t.value * c })

def coefficient (x : Element n) (f b : Blade n) : GQ :=
  (x.map fun t => if t.form = f ∧ t.blade = b then t.value else 0).sum

/-- Clifford multiplication, including repeated-index metric factors. -/
def bladeMul (eta : Fin n → ℤ) (a b : Blade n) : Blade n × ℤ :=
  ((a \ b) ∪ (b \ a), reorderSign a b * metric eta (a ∩ b))

/-- Pinned Hodge star, acting solely on the form index. -/
def star (eta : Fin n → ℤ) (x : Element n) : Element n :=
  clean (x.map fun t => ⟨t.formᶜ, t.blade, t.value * integer (starSign eta t.form)⟩)

inductive Mode where
  | C | A
  deriving DecidableEq, Repr

/-- The reversed Clifford product retains the SAME form order: this is the
ungraded coefficient bracket used by Python, not a graded tensor commutator. -/
def bracket (eta : Fin n → ℤ) (mode : Mode) (x y : Element n) : Element n :=
  clean (x.flatMap fun t => y.filterMap fun u =>
    if Disjoint t.form u.form then
      let (b, z) := bladeMul eta t.blade u.blade
      let w := (bladeMul eta u.blade t.blade).2
      let k := match mode with | .C => z - w | .A => z + w
      let c := t.value * u.value * integer (reorderSign t.form u.form * k)
      some ⟨t.form ∪ u.form, b, match mode with | .C => c | .A => c * imaginary⟩
    else none)

def rightMulVolume (eta : Fin n → ℤ) (phase : GQ) (x : Element n) : Element n :=
  clean (x.map fun t =>
    let (b, z) := bladeMul eta t.blade Finset.univ
    ⟨t.form, b, t.value * phase * integer z⟩)

/-- Enumerate only increasing pairs, precisely as `itertools.combinations`. -/
def pairs (n : ℕ) : List (Fin n × Fin n) :=
  (List.finRange n).flatMap fun a => (List.finRange n).filterMap fun b =>
    if a < b then some (a, b) else none

def pairSet (a b : Fin n) : Blade n := {a, b}

def phiF (n : ℕ) : Element n := (List.finRange n).map fun a => ⟨{a}, {a}, 1⟩
def phiB (n : ℕ) : Element n := (pairs n).map fun (a, b) => ⟨pairSet a b, pairSet a b, 1⟩
def phiFPrime (eta : Fin n → ℤ) (phase : GQ) : Element n :=
  rightMulVolume eta phase (phiF n)
def phiBPrime (eta : Fin n → ℤ) (phase : GQ) : Element n :=
  rightMulVolume eta (imaginary * phase) (phiB n)

abbrev Curvature (n : ℕ) := Fin n → Fin n → Fin n → Fin n → ℚ

/-- `raiseLastPair = false` is explicitly a DIFFERENT index convention used
only to witness the negative scope claim. The pinned `xi` always raises. -/
def xiWithRaising (eta : Fin n → ℤ) (R : Curvature n) (raiseLastPair : Bool) : Element n :=
  clean ((pairs n).flatMap fun (a, b) => (pairs n).map fun (c, d) =>
    let weight : ℚ := if raiseLastPair then (eta c * eta d : ℤ) else 1
    ⟨pairSet a b, pairSet c d, rational (R a b c d * weight / 2)⟩)

def xi (eta : Fin n → ℤ) (R : Curvature n) : Element n := xiWithRaising eta R true

/-- All eight assignments are represented by three independent `Mode`s. -/
def shiab (eta : Fin n → ℤ) (m0 m1 m2 : Mode)
    (phi1 phi2 x : Element n) : Element n :=
  let sx := star eta x
  let first := bracket eta m0 phi1 sx
  let second := star eta (bracket eta m2 phi1 (star eta (bracket eta m1 phi2 sx)))
  plus first (scale second (rational (-1 / 2)))

/-- Infinitesimal generator with normalization `X = (1/2) G_a G_b`.
The proof argument `hab` excludes the repeated or reversed generator cases. -/
def generatorAction (eta : Fin n → ℤ) (a b : Fin n) (_hab : a < b)
    (x : Element n) : Element n :=
  let cl := bracket eta .C [⟨∅, pairSet a b, rational (1 / 2)⟩] x
  let fm := x.flatMap fun t => [(a, b, -eta b), (b, a, eta a)].filterMap fun (src, dst, s) =>
    if src ∈ t.form ∧ dst ∉ t.form then
      let g := t.form.erase src
      let sign := s * reorderSign {src} g * reorderSign {dst} g
      some ⟨insert dst g, t.blade, t.value * integer sign⟩
    else none
  plus cl (clean fm)

/-- Bounded conversion for the bridge's bitmask interchange format. Bits >= n
are discarded at this external adapter; the algebra itself has no unbounded masks. -/
def fromMask (n mask : ℕ) : Blade n := Finset.univ.filter fun i => mask.testBit i.val

def toMask (s : Blade n) : ℕ := ∑ i ∈ s, 2 ^ i.val

def basis (n f b : ℕ) (c : GQ) : Element n := [⟨fromMask n f, fromMask n b, c⟩]

def eta31 : Fin 4 → ℤ := fun i => if i.val < 3 then 1 else -1

/-- Pair-symmetric witness: the (01,03) and (03,01) entries are one.
All remaining increasing-pair entries are zero. Full antisymmetry is supplied
below so this also defines an algebraic curvature tensor, not just a pair table. -/
def witnessR : Curvature 4 := fun a b c d =>
  let oriented (u v i j : Fin 4) : ℚ :=
    if u = i ∧ v = j then 1 else if u = j ∧ v = i then -1 else 0
  oriented a b 0 1 * oriented c d 0 3 + oriented a b 0 3 * oriented c d 0 1

/-- The witness really has the pair symmetry used by the headline. -/
theorem witness_pair_symmetric (a b c d : Fin 4) : witnessR a b c d = witnessR c d a b := by
  unfold witnessR
  ac_rfl

section ConcreteWitnesses
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

/-- Full first Bianchi identity: the counterexample is algebraic curvature. -/
theorem witness_bianchi : ∀ a b c d : Fin 4,
    witnessR a b c d + witnessR a c d b + witnessR a d b c = 0 := by decide +kernel

/-- Direct kernel-checked evaluation, with pinned raising factors. -/
theorem pinned_witness_inner_B :
    bracket eta31 .C (phiB 4) (star eta31 (xi eta31 witnessR)) = [] := by decide +kernel

/-- Dropping eta_c eta_d gives exactly -2 vol ⊗ G_1 G_3. -/
theorem dropped_witness_inner_B :
    bracket eta31 .C (phiB 4) (star eta31 (xiWithRaising eta31 witnessR false)) =
      basis 4 15 10 (integer (-2)) := by decide +kernel

/-- B-prime also fails under the dropped-index convention, for phase i. -/
theorem dropped_witness_inner_BPrime :
    bracket eta31 .C (phiBPrime eta31 imaginary)
      (star eta31 (xiWithRaising eta31 witnessR false)) =
      basis 4 15 5 (integer (-2)) := by native_decide

end ConcreteWitnesses

end B02.Concrete



