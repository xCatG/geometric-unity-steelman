import B03.Model

namespace B03
set_option maxRecDepth 100000
set_option maxHeartbeats 0

 theorem selection77 : ImaginarySelection 7 7 := by unfold ImaginarySelection; decide +kernel
 theorem selection95 : ImaginarySelection 7 9 := by unfold ImaginarySelection; decide +kernel
 theorem first_chirality77 : FirstChirality 7 7 := by unfold FirstChirality; decide +kernel
 theorem first_chirality95 : FirstChirality 7 9 := by unfold FirstChirality; decide +kernel
 theorem j_square77 : (charge 7 7).mul (charge 7 7).conj = Mono.one :=
  Mono.extensional (by decide +kernel)
 theorem j_square95 : (charge 7 9).mul (charge 7 9).conj = Mono.one.shift 2 :=
  Mono.extensional (by decide +kernel)
 theorem chirality_parity77 : chirality 7 7 = (parity order77).shift 2 :=
  Mono.extensional (by decide +kernel)
 theorem chirality_parity95a : chirality 7 9 = parity order95a :=
  Mono.extensional (by decide +kernel)
 theorem chirality_parity95b : chirality 7 9 = parity order95b :=
  Mono.extensional (by decide +kernel)

/-- Clifford relations in multiplicative form: squares eta_a, distinct products anticommute. -/
def Clifford (m p : ℕ) : Prop :=
  (∀ a : Fin (2*m), Mono.Eqv ((gamma m p a).mul (gamma m p a))
    (Mono.one.shift (if a.val < p then 0 else 2))) ∧
  (∀ a b : Fin (2*m), a < b → Mono.Eqv ((gamma m p a).mul (gamma m p b))
    (((gamma m p b).mul (gamma m p a)).shift 2))
 theorem clifford31 : Clifford 2 3 := by unfold Clifford; decide +kernel
 theorem clifford77 : Clifford 7 7 := by unfold Clifford; decide +kernel
 theorem clifford95 : Clifford 7 9 := by unfold Clifford; decide +kernel

/-- A single common sign suffices for every bivector, not only adjacent generators. -/
def JGamma (m p : ℕ) (s : Fin 4) : Prop :=
  ∀ a : Fin (2*m), Mono.Eqv ((charge m p).mul (gamma m p a).conj)
    (((gamma m p a).mul (charge m p)).shift s)
 theorem j_gamma31 : JGamma 2 3 2 := by unfold JGamma; decide +kernel
 theorem j_gamma77 : JGamma 7 7 0 := by unfold JGamma; decide +kernel
 theorem j_gamma95 : JGamma 7 9 0 := by unfold JGamma; decide +kernel
 theorem j_chirality31 : (charge 2 3).mul (chirality 2 3).conj =
    ((chirality 2 3).mul (charge 2 3)).shift 2 := Mono.extensional (by decide +kernel)
 theorem j_chirality77 : (charge 7 7).mul (chirality 7 7).conj =
    (chirality 7 7).mul (charge 7 7) := Mono.extensional (by decide +kernel)
 theorem j_chirality95 : (charge 7 9).mul (chirality 7 9).conj =
    (chirality 7 9).mul (charge 7 9) := Mono.extensional (by decide +kernel)

end B03
