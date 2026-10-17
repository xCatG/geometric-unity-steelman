import B05Sign.Algebra

namespace B07Argon.Variation
open B05Sign
variable {R : Type*} [Ring R]

/-- Extend D coefficientwise to genuine central dual numbers s²=0. -/
def dualD (D : Diff R) : Diff (DualNumber R) where
  toAdd :=
    { toFun := fun x => ⟨D x.fst, D x.snd⟩
      map_zero' := by ext <;> simp
      map_add' := by intro x y; ext <;> simp [map_add] }
  leibniz x y := by
    apply TrivSqZeroExt.ext
    · exact D.leibniz _ _
    · change D (x.fst * y.snd + x.snd * y.fst) =
        (D x.fst * y.snd + D x.snd * y.fst) + (x.fst * D y.snd + x.snd * D y.fst)
      rw [map_add, D.leibniz, D.leibniz]
      abel

def constantUnit (e : Rˣ) : (DualNumber R)ˣ where
  val := ⟨e, 0⟩
  inv := ⟨↑e⁻¹, 0⟩
  val_inv := by ext <;> simp
  inv_val := by ext <;> simp

def infinitesimalUnit (β : R) : (DualNumber R)ˣ where
  val := ⟨1, β⟩
  inv := ⟨1, -β⟩
  val_inv := by ext <;> simp
  inv_val := by ext <;> simp

/-- ε(s)=ε(1+sβ); δ means the s coefficient, not an analytic limit. -/
theorem logD_variation (D : Diff R) (e : Rˣ) (β : R) :
    (logD (dualD D) (constantUnit e * infinitesimalUnit β)).snd =
      D β + (logD D e * β - β * logD D e) := by
  rw [logD_mul]
  simp [logD, conj, dualD, constantUnit, infinitesimalUnit]
  noncomm_ring

theorem augmentedT_variation (D : Diff R) (e : Rˣ) (varpi β : R) :
    ((TrivSqZeroExt.inl varpi : DualNumber R) -
      logD (dualD D) (constantUnit e * infinitesimalUnit β)).snd =
        -(D β + (logD D e * β - β * logD D e)) := by
  simpa only [TrivSqZeroExt.snd_sub, TrivSqZeroExt.snd_inl, zero_sub] using
    congrArg (fun x : R => -x) (logD_variation D e β)

def dress (e : Rˣ) (X : R → R) (x : R) : R := conj e (X (conj e⁻¹ x))

theorem dress_apply (e : Rˣ) (X : R → R) (x : R) :
    dress e X (conj e x) = conj e (X x) := by simp [dress]

theorem conj_mul (e : Rˣ) (x y : R) : conj e (x*y) = conj e x * conj e y := by
  simp [conj, mul_assoc]

/-- D_B becomes D after undressing, with B=ε⁻¹Dε. This is the
directional coefficient version of exterior covariant differentiation. -/
theorem derivative_undress (D : Diff R) (e : Rˣ) (x : R) :
    D (conj e⁻¹ x) = conj e⁻¹ (D x + (logD D e * x - x * logD D e)) := by
  simp only [conj, inv_inv, D.leibniz, D.inverse, logD]
  simp only [mul_add, add_mul, mul_sub, sub_mul, neg_mul, mul_neg, mul_assoc,
    Units.mul_inv_cancel_left]
  noncomm_ring

/-- All three backgrounds X,Q,F are conjugated together. This is the exact
algebraic factorization behind S_ε(T)=S_1(Ad(ε)T), NOT an assumption that
varying ε keeps X or B fixed. Fixed numerical cubic weights may be absorbed
in Q and the product argument. -/
theorem action_conjugation {S : Type*} (P : R → R → S)
    (hP : ∀ (e : Rˣ) x y, P (conj e x) (conj e y) = P x y)
    (e : Rˣ) (X Q : R → R) (F t : R) :
    P (conj e t) (dress e X (conj e F + dress e Q (conj e t) + conj e t * conj e t)) =
      P t (X (F + Q t + t*t)) := by
  simp only [dress_apply, ← conj_mul, ← conj_add, hP]

/-- H5 for a C1-shaped residual. P is the explicitly supplied invariant pairing;
Q is the (conjugation-compatible) symbol insertion, not a derivative of ε. -/
theorem c1_conjugation {S : Type*} [Add S] (P : R → R → S)
    (hP : ∀ (e : Rˣ) x y, P (conj e x) (conj e y) = P x y)
    (e : Rˣ) (X Q : R → R) (a t : R) :
    P (conj e t) (dress e X (dress e Q (conj e a))) +
      P (conj e a) (dress e X (dress e Q (conj e t))) =
      P t (X (Q a)) + P a (X (Q t)) := by
  simp only [dress_apply, hP]

/-- A polarized cubic residual built from product, X and trace pairing. All
three summands are separately invariant, hence any fixed scalar weights are too. -/
theorem cubic_conjugation {S : Type*} [Ring S] (P : R → R → S)
    (hP : ∀ (e : Rˣ) x y, P (conj e x) (conj e y) = P x y)
    (e : Rˣ) (X : R → R) (a t : R) (c0 c1 c2 : S) :
    c0 * P (conj e a) (dress e X (conj e t * conj e t)) +
      c1 * P (conj e t) (dress e X (conj e a * conj e t + conj e t * conj e a)) -
      c2 * P (conj e a) (dress e X (conj e t * conj e t)) =
    c0 * P a (X (t*t)) + c1 * P t (X (a*t+t*a)) - c2 * P a (X (t*t)) := by
  simp only [← conj_mul, ← conj_add, dress_apply, hP]

/-- The full undressed variable U=Ad(ε)T has an extra [β,T] variation.
After combining it with δT the derivative is D+[varpi,·], not D+[B,·]. -/
theorem undressed_variation (D : Diff R) (varpi B β : R) :
    β * (varpi-B) - (varpi-B) * β - (D β + (B*β-β*B)) =
      -(D β + (varpi*β-β*varpi)) := by noncomm_ring

theorem full_undressed_variation (D : Diff R) (e : Rˣ) (varpi β : R) :
    (conj (constantUnit e * infinitesimalUnit β)⁻¹
      ((TrivSqZeroExt.inl varpi : DualNumber R) -
        logD (dualD D) (constantUnit e * infinitesimalUnit β))).snd =
      conj e⁻¹ (-(D β + (varpi*β-β*varpi))) := by
  rw [logD_mul]
  simp [conj, logD, dualD, constantUnit, infinitesimalUnit, mul_add, add_mul,
    mul_sub, sub_mul, mul_assoc]
  noncomm_ring

/-- Formal chain rule: when the ENTIRE action is S(U), stationarity for all
varpi-directions implies stationarity for ε-directions. No pairing or integration
axiom is hidden here: E is the supplied first variation in U. -/
theorem epsilon_no_independent_equation {S : Type*} [Zero S]
    (E : R → S) (e : Rˣ) (D : Diff R) (varpi : R)
    (hvarpi : ∀ a, E (conj e⁻¹ a) = 0) (β : R) :
    E ((conj (constantUnit e * infinitesimalUnit β)⁻¹
      ((TrivSqZeroExt.inl varpi : DualNumber R) -
        logD (dualD D) (constantUnit e * infinitesimalUnit β))).snd) = 0 := by
  rw [full_undressed_variation]
  exact hvarpi _

end B07Argon.Variation
