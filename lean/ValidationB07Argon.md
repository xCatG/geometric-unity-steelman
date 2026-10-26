# B07 Argon validation

- Lean 4.24.0, Windows x86_64, compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
- Mathlib v4.24.0, lockfile commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
- Clean whole-project `lake build`: **passed, 206.944256 seconds, 8786 jobs**.
- Only the resolved `<lean-worktree>/lean/.lake/build` was removed;
  dependency caches were retained. Existing B02, B03, B05Sign and bridge targets
  were rebuilt together with B07Argon.
- `lake env lean Audit.lean`: **passed, 83.5472351 seconds**, 368 records.
- All **308 previous axiom records unchanged**, compared with AxiomAudit.txt
  using case-sensitive declaration names (e.g. B03.j_chirality31 and
  B03.J_chirality31 are different declarations).
- **60 new audit entries**: every one of the 57 new theorems, plus dualD,
  constantUnit and infinitesimalUnit. Every dependency set is a subset of
  `{propext, Classical.choice, Quot.sound}`. None uses sorryAx, native-decision
  axioms, compiler trust, or custom axioms.
- Exact new output: `AxiomAuditB07Argon.txt`. Reproduce with
  `lake env lean B07Audit.lean`; `Audit.lean` includes both old and new checks.
- Finite rational witnesses use kernel proofs, including `decide +kernel`.
  This is distinct from native_decide.
- No edits to existing B02/B03/B05Sign proof modules or dependency versions.

The comparison script and full clean-build/audit logs are in the assigned
`notes:b07-argon-lean/` directory of the main checkout. Coverage and
all model boundaries are recorded in COVERAGE.md and THEOREMS.md.
