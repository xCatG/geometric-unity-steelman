# B05 sign-check validation

## Source and model

The source is Eric Weinstein's *Geometric Unity: Author's Working Draft,
v1.0*, April 1, 2021, SHA-256
`3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.
Printed pages equal one-based PDF pages in this copy. Pages 33 and 36-40
were rendered with PyMuPDF 1.28.2 and visually inspected, including
(5.9), (6.2), (6.4)-(6.5), (6.11)-(6.16), (6.19)-(6.22), (7.3)-(7.4),
and footnote 7 on page 36. Intermediate images are in the ignored
`.tools/b05-source/` directory.

The printed (6.13) uses a minus sign. Both (6.20) and (7.4) switch it to
plus during the displayed calculation. The printed (6.14) genuinely
cancels with the minus sign. See `COVERAGE.md` for the affine-coordinate
interpretation, directional-model limitation, all branch outcomes, and
the distinction between a ring identity and a value at a point.

Read against `experiments/B05/spec.md` section 1.2,
`docs/gaps/register.md` B05 sign-conflict entry, and the prior
`notes:b05-task6/readme-audit.md` Finding 1 plus its
`evidence/checks.json` central-phase jet. No disagreement with that
correctly interpreted jet was found.

## Reproduction

From `lean/` in the designated worktree:

```powershell
lake build
& .tools/python-env/Scripts/python.exe bridge/inventory.py
lake env lean Audit.lean
```

The toolchain and dependency revisions are unchanged: Lean 4.24.0
(commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`), mathlib v4.24.0
(revision `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`).

## Verified results

- Clean `lake build` exited 0 in **211.495 seconds**, rebuilding the
  entire project output directory (B02, B03, B05Sign and bridge). Only the
  resolved `<lean-worktree>/lean/.lake/build` was removed; installed
  dependency packages and their cached builds were retained.
- **44 new public theorems**, plus the group instance, both homomorphism
  structures and the concrete derivation, audited with `#print axioms`.
  The B05 output contains only `propext`, `Classical.choice`, `Quot.sound`,
  or no axioms. No `sorryAx`, `Lean.ofReduceBool`, or `Lean.trustCompiler`.
- The full inventory has 313 theorem declarations, 304 public theorem
  audits, and four additional B05 proof-bearing definition audits.
- Source scan found no `sorry`, `admit`, `axiom` declaration or
  `native_decide` in B05Sign. Proofs use ring/group identities and
  kernel-checked tactics, including explicit matrix-entry normalization.
- B02/B03 source files were unchanged. The combined axiom audit preserves
  their prior dependencies, including the documented native finite
  certificates in B02; those dependencies do not occur in B05Sign.
- Independent read-only review inspected all six page images and the
  complete implementation/fidelity inventory: no actionable findings.
  No extra numerical bridge run was required: this change adds an
  independent Lean library and the combined build rebuilt the bridge.

The raw build log and metadata are retained in the handoff directory;
`AxiomAudit.txt` is the complete combined audit and
`AxiomAuditB05Sign.txt` is the full B05 extract. The appendix below is the
actual output for every new theorem and the four proof-bearing definitions.

```text
'B05Sign.Diff.one' depends on axioms: [propext, Quot.sound]
'B05Sign.Diff.zero' does not depend on any axioms
'B05Sign.Diff.inverse' depends on axioms: [propext, Quot.sound]
'B05Sign.conj_one' depends on axioms: [propext]
'B05Sign.conj_zero' depends on axioms: [propext]
'B05Sign.conj_add' depends on axioms: [propext]
'B05Sign.conj_neg' depends on axioms: [propext, Quot.sound]
'B05Sign.conj_sub' depends on axioms: [propext, Quot.sound]
'B05Sign.conj_comp' depends on axioms: [propext]
'B05Sign.conj_cancel' depends on axioms: [propext]
'B05Sign.logD_one' depends on axioms: [propext, Quot.sound]
'B05Sign.logD_mul' depends on axioms: [propext]
'B05Sign.Gauge.ext' depends on axioms: [propext]
'B05Sign.mul_unit' depends on axioms: [propext, Quot.sound]
'B05Sign.mul_shift' depends on axioms: [propext, Quot.sound]
'B05Sign.tauLit_mul' depends on axioms: [propext, Quot.sound]
'B05Sign.tauRec_mul' depends on axioms: [propext, Quot.sound]
'B05Sign.tauLit_injective' depends on axioms: [propext, Quot.sound]
'B05Sign.tauRec_injective' depends on axioms: [propext, Quot.sound]
'B05Sign.tilted_action_lit' depends on axioms: [propext, Quot.sound]
'B05Sign.tilted_action_rec' depends on axioms: [propext, Quot.sound]
'B05Sign.act62_mul' depends on axioms: [propext, Quot.sound]
'B05Sign.act62_one' depends on axioms: [propext, Quot.sound]
'B05Sign.torsion_lit' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.torsion_rec' depends on axioms: [propext, Quot.sound]
'B05Sign.connection_lit' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.connection_rec' depends on axioms: [propext, Quot.sound]
'B05Sign.second_connection' depends on axioms: [propext, Quot.sound]
'B05Sign.biConnection_rec' depends on axioms: [propext, Quot.sound]
'B05Sign.conj_mul_inv' depends on axioms: [propext]
'B05Sign.leftAct_formula' depends on axioms: [propext]
'B05Sign.leftAct_mul' depends on axioms: [propext, Quot.sound]
'B05Sign.leftAct_one' depends on axioms: [propext, Quot.sound]
'B05Sign.projection_formula' depends on axioms: [propext]
'B05Sign.projection_lit' depends on axioms: [propext, Quot.sound]
'B05Sign.projection_rec' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.stabilizer_lit' depends on axioms: [propext, Quot.sound]
'B05Sign.stabilizer_rec' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.Witness.swap_squared' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.Witness.logarithm' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.Witness.residual_nonzero' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.Witness.torsion_not_covariant' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.Witness.connection_not_covariant' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.Witness.reconstructed_projection_not_invariant' depends on axioms: [propext, Classical.choice, Quot.sound]
'B05Sign.gaugeGroup' depends on axioms: [propext, Quot.sound]
'B05Sign.tauLitHom' depends on axioms: [propext, Quot.sound]
'B05Sign.tauRecHom' depends on axioms: [propext, Quot.sound]
'B05Sign.innerDiff' depends on axioms: [propext, Quot.sound]
```
