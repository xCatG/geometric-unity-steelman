import B02.Samples
open B02 B02.Concrete B02.Samples

private def emit (label : String) (x : Element n) : IO Unit := do
  let raw := String.intercalate ";" ((canonical x).map fun t =>
    s!"{toMask t.form},{toMask t.blade},{t.value.re.num}/{t.value.re.den},{t.value.im.num}/{t.value.im.den}")
  IO.println s!"{label}|{raw}"

def main : IO Unit := do
  for (label, eta) in [("22", eta22), ("40", eta40), ("31", eta31)] do
    emit s!"{label}_CCC" (response eta .C .C .C)
    emit s!"{label}_CAA" (response eta .C .A .A)
  emit "11_CCC" (response eta11 .C .C .C)
  emit "11_CAA" (response eta11 .C .A .A)
