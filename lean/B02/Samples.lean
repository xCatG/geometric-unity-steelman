import B02.Concrete

/-! Concrete certificates only. These do not promote the signature-parity
observation in proofs.md from sampled scope to an all-curvature theorem.
These five certificates use native_decide: Lean.ofReduceBool and Lean.trustCompiler
are explicitly included in their trust boundary. Kernel decide was attempted
and stopped at the executable sparse-list equality computations. -/
namespace B02.Samples
open B02.Concrete

/-- Constant sectional curvature +1 in the Python R_abcd convention. -/
def constantCurvature (eta : Fin n → ℤ) : Curvature n := fun a b c d =>
  (eta a * eta b : ℤ) *
    ((if a = c ∧ b = d then 1 else 0) - (if a = d ∧ b = c then 1 else 0) : ℚ)

def eta22 : Fin 4 → ℤ := fun a => if a.val < 2 then 1 else -1
def eta40 : Fin 4 → ℤ := fun _ => 1
def eta11 : Fin 2 → ℤ := fun a => if a.val < 1 then 1 else -1

/-- Canonical order only; coefficients are untouched. This avoids equating
sparse representations by accidental insertion order. -/
def canonical (x : Element n) : Element n :=
  (clean x).mergeSort fun a b =>
    if toMask a.form == toMask b.form then toMask a.blade ≤ toMask b.blade
    else toMask a.form < toMask b.form

def response (eta : Fin n → ℤ) (m0 m1 m2 : Mode) : Element n :=
  star eta (shiab eta m0 m1 m2 (phiF n) (phiB n) (xi eta (constantCurvature eta)))

set_option maxRecDepth 100000
set_option maxHeartbeats 8000000

/-- Ric=3g, S=12; even signature parity gives +3F for literal CCC. -/
theorem split_CCC :
    canonical (response eta22 .C .C .C) = canonical (scale (phiF 4) (integer 3)) := by
  native_decide

/-- The sampled (2,2) CAA response is +3F+6F=9F. -/
theorem split_CAA :
    canonical (response eta22 .C .A .A) = canonical (scale (phiF 4) (integer 9)) := by
  native_decide

/-- Same sampled relative sign for Euclidean (4,0). -/
theorem euclidean_CCC :
    canonical (response eta40 .C .C .C) = canonical (scale (phiF 4) (integer 3)) := by
  native_decide

theorem euclidean_CAA :
    canonical (response eta40 .C .A .A) = canonical (scale (phiF 4) (integer 9)) := by
  native_decide

/-- In dimension two the literal CCC response is -F on curvature +1.
This is a concrete response certificate, not a uniqueness statement about kappa. -/
theorem dimension_two_CCC :
    canonical (response eta11 .C .C .C) = canonical (scale (phiF 2) (integer (-1))) := by
  native_decide

end B02.Samples

