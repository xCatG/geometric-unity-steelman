import B03.Model
open B03
private def emit (label : String) (a : Mono m) : IO Unit := do
  let xs := (List.finRange (2^m)).map fun j => s!"[{(a.perm j).val},{(a.phase j).val}]"
  IO.println s!"{label}|[{String.intercalate "," xs}]"
private def split (label : String) (m p : ℕ) (order : Fin m → Fin m) : IO Unit := do
  for a in List.range (2*m) do
    emit s!"{label}/G{a}" (gamma m p a)
    emit s!"{label}/E{a}" (euclidean m a)
  emit s!"{label}/B" (charge m p)
  emit s!"{label}/C" (chirality m p)
  emit s!"{label}/Pi" (parity order)
  for k in List.finRange m do
    emit s!"{label}/h{k.val}" (cartan m (order k).val)
def main : IO Unit := do
  split "3,1|1,1+2,0" 2 3 order31
  split "7,7|1,3+6,4" 7 7 order77
  split "9,5|1,3+8,2" 7 9 order95a
  split "9,5|3,1+6,4" 7 9 order95b
