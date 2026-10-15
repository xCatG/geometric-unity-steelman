import B02.Concrete

open B02 B02.Concrete

private def ratText (q : ℚ) : String := s!"{q.num}/{q.den}"

/-- Stable text protocol: label|formMask,bladeMask,reNum/reDen,imNum/imDen;...
Terms are sorted by the two masks; zero terms and duplicates are removed. -/
private def emit (label : String) (x : Element 4) : IO Unit := do
  let ts := (clean x).mergeSort fun a b =>
    if toMask a.form == toMask b.form then toMask a.blade ≤ toMask b.blade
    else toMask a.form < toMask b.form
  let raw := String.intercalate ";" (ts.map fun t =>
    s!"{toMask t.form},{toMask t.blade},{ratText t.value.re},{ratText t.value.im}")
  IO.println s!"{label}|{raw}"

private def modeName : Mode → String | .C => "C" | .A => "A"

/-- Enumerations deliberately match `bridge/check.py`; expected algebra values
come exclusively from the repository's `gu.cliffform` and `gu.shiab` functions. -/
def main : IO Unit := do
  let eta := eta31
  let phase := imaginary
  emit "phase" (basis 4 0 0 phase)
  for f in List.range 16 do
    for b in List.range 16 do
      emit s!"star_{f}_{b}" (star eta (basis 4 f b ⟨2, -3⟩))
  for (f, g) in [(0, 0), (1, 2), (2, 1), (3, 1)] do
    for a in List.range 16 do
      for b in List.range 16 do
        for m in [Mode.C, Mode.A] do
          emit s!"bracket_{f}_{g}_{a}_{b}_{modeName m}"
            (bracket eta m (basis 4 f a ⟨2 / 3, -1⟩) (basis 4 g b ⟨-2, 1 / 5⟩))
  let fs := [("F", phiF 4), ("F'", phiFPrime eta phase)]
  let bs := [("B", phiB 4), ("B'", phiBPrime eta phase)]
  for (label, p) in fs ++ bs do
    emit s!"phi_{label}" p
  let x := xi eta witnessR
  let dropped := xiWithRaising eta witnessR false
  emit "xi" x
  emit "xi_dropped" dropped
  for (label, p) in bs do
    emit s!"inner_pinned_{label}" (bracket eta .C p (star eta x))
    emit s!"inner_dropped_{label}" (bracket eta .C p (star eta dropped))
  for (p1, f) in fs do
    for (p2, b) in bs do
      for m0 in [Mode.C, Mode.A] do
        for m1 in [Mode.C, Mode.A] do
          for m2 in [Mode.C, Mode.A] do
            emit s!"shiab_{p1}_{p2}_{modeName m0}{modeName m1}{modeName m2}"
              (shiab eta m0 m1 m2 f b x)
  for a in List.finRange 3 do
    let aa : Fin 4 := ⟨a.val, by omega⟩
    let bb : Fin 4 := ⟨a.val + 1, by omega⟩
    for f in List.range 16 do
      for b in List.range 16 do
        emit s!"action_{a.val}_{f}_{b}"
          (generatorAction eta aa bb (by change a.val < a.val + 1; omega) (basis 4 f b ⟨1, 2⟩))


