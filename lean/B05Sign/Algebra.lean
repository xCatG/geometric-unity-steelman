import Mathlib

/-!
Directional algebraic model for GU pp.33,36-40. R need not commute. A
covariant derivative of endomorphism-valued functions, evaluated in one
vector direction, obeys these rules. Replacing the module of one-forms by
R preserves the order of every coefficient product; no wedge products,
bundles, smoothness, evaluation homomorphism, or gauge-group restriction
are asserted. In particular h=1 in R implies D h=0, unlike h(p)=1.
-/
namespace B05Sign
variable {R : Type*} [Ring R]

structure Diff (R : Type*) [Ring R] where
  toAdd : R →+ R
  leibniz : ∀ x y, toAdd (x * y) = toAdd x * y + x * toAdd y

instance : CoeFun (Diff R) (fun _ => R → R) := ⟨fun D => D.toAdd⟩

namespace Diff
variable (D : Diff R)

@[simp] theorem one : D 1 = 0 := by
  have h := D.leibniz 1 1
  simp only [one_mul, mul_one] at h
  exact (add_eq_left.mp h.symm)

@[simp] theorem zero : D 0 = 0 := D.toAdd.map_zero

theorem inverse (h : Rˣ) : D (↑h⁻¹ : R) = -(↑h⁻¹ : R) * D (↑h) * ↑h⁻¹ := by
  have he := D.leibniz (↑h : R) (↑h⁻¹ : R)
  simp only [Units.mul_inv, one] at he
  have ht := congrArg (fun x : R => (↑h⁻¹ : R) * x) he
  simp only [mul_zero, mul_add, ← mul_assoc, Units.inv_mul, one_mul] at ht
  simpa only [neg_mul] using eq_neg_of_add_eq_zero_right ht.symm
end Diff

/-- Right conjugation; the order matches Aut(h⁻¹, x) in (5.9). -/
def conj (h : Rˣ) (x : R) : R := (↑h⁻¹ : R) * x * ↑h

@[simp] theorem conj_one (x : R) : conj (1 : Rˣ) x = x := by simp [conj]
@[simp] theorem conj_zero (h : Rˣ) : conj h 0 = 0 := by simp [conj]
@[simp] theorem conj_add (h : Rˣ) (x y : R) : conj h (x+y) = conj h x + conj h y := by
  simp [conj, mul_add, add_mul]
@[simp] theorem conj_neg (h : Rˣ) (x : R) : conj h (-x) = -conj h x := by simp [conj]
@[simp] theorem conj_sub (h : Rˣ) (x y : R) : conj h (x-y) = conj h x - conj h y := by
  simp [sub_eq_add_neg]

theorem conj_comp (e h : Rˣ) (x : R) : conj h (conj e x) = conj (e*h) x := by
  simp [conj, mul_assoc]

@[simp] theorem conj_cancel (h : Rˣ) (x : R) : conj h⁻¹ (conj h x) = x := by
  rw [conj_comp]; simp

/-- The logarithmic derivative appearing in (6.2), (6.4), (7.3). -/
def logD (D : Diff R) (h : Rˣ) : R := (↑h⁻¹ : R) * D ↑h

@[simp] theorem logD_one (D : Diff R) : logD D 1 = 0 := by simp [logD]

theorem logD_mul (D : Diff R) (e h : Rˣ) :
    logD D (e*h) = conj h (logD D e) + logD D h := by
  simp [logD, conj, D.leibniz, mul_add, ← mul_assoc]

/-- (5.9), with actual group laws verified below. -/
structure Gauge (R : Type*) [Ring R] where
  unit : Rˣ
  shift : R
  deriving DecidableEq

@[ext] theorem Gauge.ext {g k : Gauge R} (hu : g.unit = k.unit) (hs : g.shift = k.shift) : g = k := by
  cases g; cases k; simp_all

instance gaugeGroup : Group (Gauge R) where
  mul g k := ⟨g.unit * k.unit, conj k.unit g.shift + k.shift⟩
  one := ⟨1, 0⟩
  inv g := ⟨g.unit⁻¹, -conj g.unit⁻¹ g.shift⟩
  mul_assoc g h k := by
    apply Gauge.ext
    · exact mul_assoc _ _ _
    · change conj k.unit (conj h.unit g.shift + h.shift) + k.shift =
        conj (h.unit*k.unit) g.shift + (conj k.unit h.shift + k.shift)
      simp only [conj_add, conj_comp]; exact add_assoc _ _ _
  one_mul g := by
    apply Gauge.ext
    · exact one_mul _
    · change conj g.unit 0 + g.shift = g.shift
      simp
  mul_one g := by
    apply Gauge.ext
    · exact mul_one _
    · change conj 1 g.shift + 0 = g.shift
      simp
  inv_mul_cancel g := by
    apply Gauge.ext
    · exact inv_mul_cancel _
    · change conj g.unit (-conj g.unit⁻¹ g.shift) + g.shift = 0
      simp only [conj_neg, conj_comp, inv_mul_cancel, conj_one, neg_add_cancel]

@[simp] theorem mul_unit (g k : Gauge R) : (g*k).unit = g.unit*k.unit := rfl
@[simp] theorem mul_shift (g k : Gauge R) : (g*k).shift = conj k.unit g.shift + k.shift := rfl

/-- (6.4) literal and reconstruction are kept as distinct definitions. -/
def tauLit (D : Diff R) (h : Rˣ) : Gauge R := ⟨h, -logD D h⟩
def tauRec (D : Diff R) (h : Rˣ) : Gauge R := ⟨h, logD D h⟩

theorem tauLit_mul (D : Diff R) (e h : Rˣ) : tauLit D (e*h) = tauLit D e * tauLit D h := by
  apply Gauge.ext
  · rfl
  · simp [tauLit, logD_mul, add_comm]

theorem tauRec_mul (D : Diff R) (e h : Rˣ) : tauRec D (e*h) = tauRec D e * tauRec D h := by
  apply Gauge.ext
  · rfl
  · simp [tauRec, logD_mul]

def tauLitHom (D : Diff R) : Rˣ →* Gauge R where
  toFun := tauLit D
  map_one' := by
    apply Gauge.ext
    · rfl
    · change -logD D 1 = 0
      simp
  map_mul' := tauLit_mul D

def tauRecHom (D : Diff R) : Rˣ →* Gauge R where
  toFun := tauRec D
  map_one' := by
    apply Gauge.ext
    · rfl
    · change logD D 1 = 0
      simp
  map_mul' := tauRec_mul D

theorem tauLit_injective (D : Diff R) : Function.Injective (tauLitHom D) := by
  intro a b he; exact congrArg Gauge.unit he

theorem tauRec_injective (D : Diff R) : Function.Injective (tauRecHom D) := by
  intro a b he; exact congrArg Gauge.unit he

/-- (6.13), with the printed negative inhomogeneous term. -/
theorem tilted_action_lit (D : Diff R) (g : Gauge R) (h : Rˣ) :
    g * tauLit D h = ⟨g.unit*h, conj h g.shift - logD D h⟩ := by
  apply Gauge.ext
  · rfl
  · exact (sub_eq_add_neg _ _).symm

/-- The explicit plus-sign reconstruction of (6.13). -/
theorem tilted_action_rec (D : Diff R) (g : Gauge R) (h : Rˣ) :
    g * tauRec D h = ⟨g.unit*h, conj h g.shift + logD D h⟩ := rfl

/-- (6.2) is an action on alpha=A-A0, not on A itself. -/
def act62 (D : Diff R) (alpha : R) (g : Gauge R) : R :=
  conj g.unit alpha + logD D g.unit + g.shift

theorem act62_mul (D : Diff R) (alpha : R) (g k : Gauge R) :
    act62 D alpha (g*k) = act62 D (act62 D alpha g) k := by
  simp only [act62, mul_unit, mul_shift, logD_mul, conj_add, conj_comp]
  abel

theorem act62_one (D : Diff R) (alpha : R) : act62 D alpha 1 = alpha := by
  change conj 1 alpha + logD D 1 + 0 = alpha
  simp

/-- (7.3). -/
def torsion (D : Diff R) (g : Gauge R) : R := g.shift - logD D g.unit

theorem torsion_lit (D : Diff R) (g : Gauge R) (h : Rˣ) :
    torsion D (g * tauLit D h) = conj h (torsion D g) - 2 * logD D h := by
  simp [torsion, tauLit, logD_mul]
  noncomm_ring

theorem torsion_rec (D : Diff R) (g : Gauge R) (h : Rˣ) :
    torsion D (g * tauRec D h) = conj h (torsion D g) := by
  simp [torsion, tauRec, logD_mul]

/-- Full affine connection action with fixed coordinate origin A0 and D=d_A0. -/
def connectionAct (D : Diff R) (A0 A : R) (h : Rˣ) : R :=
  A0 + act62 D (A-A0) ⟨h, 0⟩

/-- The two connections (6.19)/(6.22), expressed with an explicit affine origin. -/
def biConnection (D : Diff R) (A0 : R) (g : Gauge R) : R × R :=
  (A0 + g.shift, A0 + logD D g.unit)

theorem connection_lit (D : Diff R) (A0 : R) (g : Gauge R) (h : Rˣ) :
    (biConnection D A0 (g * tauLit D h)).1 =
      connectionAct D A0 (A0+g.shift) h - 2 * logD D h := by
  simp [biConnection, connectionAct, act62, tauLit]
  noncomm_ring

theorem connection_rec (D : Diff R) (A0 : R) (g : Gauge R) (h : Rˣ) :
    (biConnection D A0 (g * tauRec D h)).1 =
      connectionAct D A0 (A0+g.shift) h := by
  simp [biConnection, connectionAct, act62, tauRec]

theorem second_connection (D : Diff R) (A0 : R) (g k : Gauge R) :
    (biConnection D A0 (g*k)).2 =
      connectionAct D A0 (A0+logD D g.unit) k.unit := by
  simp [biConnection, connectionAct, act62, logD_mul]

theorem biConnection_rec (D : Diff R) (A0 : R) (g : Gauge R) (h : Rˣ) :
    biConnection D A0 (g * tauRec D h) =
      (connectionAct D A0 (A0+g.shift) h,
       connectionAct D A0 (A0+logD D g.unit) h) := by
  apply Prod.ext
  · exact connection_rec D A0 g h
  · exact second_connection D A0 g (tauRec D h)

end B05Sign
