import B02.DimensionTwo
open B02 B02.Concrete B02.Samples B02.DimensionTwo

private def emit (label : String) (x : Element 2) : IO Unit := do
  let raw := String.intercalate ";" ((canonical x).map fun t =>
    s!"{toMask t.form},{toMask t.blade},{t.value.re.num}/{t.value.re.den},{t.value.im.num}/{t.value.im.den}")
  IO.println s!"{label}|{raw}"

def main : IO Unit := do
  emit "Ricci" (clean ((List.finRange 2).flatMap fun a => (List.finRange 2).map fun b =>
    ⟨{a}, {b}, rational (ricci eta11 curvature a b)⟩))
  emit "scalar" (basis 2 0 0 (rational (scalar eta11 curvature)))
  emit "embed_metric" (embedF eta11 (metricTensor eta11))
  emit "response" (response eta11 .C .C .C)
  emit "kappa_zero" (predicted (-1) 0)
  emit "kappa_one" (predicted 1 1)
