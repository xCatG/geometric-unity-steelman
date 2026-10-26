# B03 validation

Toolchain unchanged: Lean 4.24.0, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b,
x86_64-w64-windows-gnu Release. Mathlib v4.24.0, exact manifest revision
f897ebcf72cd16f89ab4577d0c826cd14afaafc7. Existing dependency caches were reused.

## Clean combined build

Removed only the verified project output directory
`<lean-worktree>/lean/.lake/build`, retaining `.lake/packages` caches.
Command from lean/: `lake build`, default targets B02, B03, bridge.
This is project-rebuild time, excluding dependency download/recompilation.

```text
Exit=0; elapsed_seconds=225.082
info: B02/ConcreteHodge.lean:221:0: 'B02.Concrete.otherShiab_reparametrization' depends on axioms: [propext, Classical.choice, Quot.sound]
info: B02/ConcreteHodge.lean:222:0: 'B02.Concrete.otherShiab_readout_reparametrization' depends on axioms: [propext, Classical.choice, Quot.sound]
✔ [8766/8774] Built B02.ConcreteLinear (35s)
ℹ [8767/8774] Built B02.TensorCovariance (33s)
info: B02/TensorCovariance.lean:254:0: 'B02.Structural.tensor_dressed_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
info: B02/TensorCovariance.lean:257:0: 'B02.Structural.tensor_response_derivation' depends on axioms: [propext, Classical.choice, Quot.sound]
✔ [8768/8774] Built B02 (26s)
✔ [8770/8774] Built B03.Weights (185s)
✔ [8771/8774] Built B03.Certificates (185s)
✔ [8772/8774] Built B03.Operators (10s)
✔ [8773/8774] Built B03 (10s)
Build completed successfully (8774 jobs).
```

## Fresh exact bridges

Commands run from the worktree root with `UV_PROJECT_ENVIRONMENT=lean/.tools/python-env`
and `PYTHONDONTWRITEBYTECODE=1`. The bridge scripts build their required Lean targets
before reading an executable or interpreted model. Expectations call the actual Python
functions; they are never copied from Lean output.

### uv run python lean/bridge/b03_check.py

```text
Build completed successfully (844 jobs).
RECORDED 7,7|1,3+6,4: {"J_preserves_chirality": true, "J_square": 1, "J_weight_signs": [1, -1, -1, -1, -1, -1, -1], "chirality_vs_parity": -1}
RECORDED 9,5|1,3+8,2: {"J_preserves_chirality": true, "J_square": -1, "J_weight_signs": [1, -1, -1, -1, -1, -1, -1], "chirality_vs_parity": 1}
RECORDED 9,5|3,1+6,4: {"J_preserves_chirality": true, "J_square": -1, "J_weight_signs": [-1, 1, -1, -1, -1, -1, -1], "chirality_vs_parity": 1}
RECORDED 3,1|1,1+2,0: {"J_preserves_chirality": false, "J_square": -1, "J_weight_signs": [1, -1], "chirality_vs_parity": 1}
PASS: 127 monomial matrices; 14644 column (perm,phase) pairs; all four splits
PASS: all 16 recorded matrix-row real-structure/adapter fields match actual Python
```

### uv run python lean/bridge/check.py

```text
Build completed successfully (2802 jobs).
PASS: 3115 exact Lean/Python cases
Dropped-index witness R_0103=R_0301=1, eta=(1,1,1,-1):
  pinned [B,*xi]_C = ()
  dropped [B,*xi]_C = ((15, 10, Fraction(-2, 1), Fraction(0, 1)),)
  dropped [B',*xi]_C = ((15, 5, Fraction(-2, 1), Fraction(0, 1)),)
```

### uv run python lean/bridge/b03_mutations.py

```text
RECORDED 7,7|1,3+6,4: {"J_preserves_chirality": true, "J_square": 1, "J_weight_signs": [1, -1, -1, -1, -1, -1, -1], "chirality_vs_parity": -1}
RECORDED 9,5|1,3+8,2: {"J_preserves_chirality": true, "J_square": -1, "J_weight_signs": [1, -1, -1, -1, -1, -1, -1], "chirality_vs_parity": 1}
RECORDED 9,5|3,1+6,4: {"J_preserves_chirality": true, "J_square": -1, "J_weight_signs": [-1, 1, -1, -1, -1, -1, -1], "chirality_vs_parity": 1}
RECORDED 3,1|1,1+2,0: {"J_preserves_chirality": false, "J_square": -1, "J_weight_signs": [1, -1], "chirality_vs_parity": 1}
DETECTED reverse_Y_phase: 77 matrices, 8988 columns; first 7,7|1,3+6,4/G1[0]: Lean=[64, 3], Python=[64, 1]
DETECTED omit_timelike_i: 25 matrices, 2952 columns; first 7,7|1,3+6,4/G7[0]: Lean=[8, 1], Python=[8, 2]
DETECTED reverse_chirality_sign: 4 matrices, 388 columns; first 7,7|1,3+6,4/C[0]: Lean=[0, 0], Python=[0, 2]
UNCHANGED SHA256 Model.lean: f3951e7f91855783caca0221b35b31f63576327274c99d3ea15ccefb6f4442db
UNCHANGED SHA256 B03Bridge.lean: 6befd3ef378d9fe3f8ffa6eee879f4b9e3b92f3c028eba085be167e09e4b40b9
```

The B03 bridge retains ignored JSON dumps of every Python and Lean perm/phase column.
The 127 matrices include physical/Euclidean gammas, B, C, Pi and each ordered Cartan
matrix for all four splits. It checks every entry and all 16 recorded matrix-row
real-structure/adapter fields. The bridge is executable evidence tying the finite
formal model to production code, not a formal semantics proof for Python.

Mutation failures are numerical mismatches against unchanged expectations, not import
or parse failures. Source copies are disposable and maintained-source hashes are checked.

## Trust audit

After the clean build, `lake env lean Audit.lean` exited 0. The generated inventory
contains 269 theorem declarations (260 public), including all 81 B03 declarations.
Full combined output: AxiomAudit.txt; B03 output: AxiomAuditB03.txt.

```text
PASS: 260 public theorem audit outputs match the combined inventory
PASS: all 81 B03 theorems use only propext, Classical.choice, Quot.sound (or fewer)
PASS: no B03 Lean.ofReduceBool, Lean.trustCompiler, sorryAx or custom axiom dependencies
```

All B03 finite certificates, including J-square and C/Pi at dimension 128, use
`decide +kernel`. No B03 `native_decide`, `sorry`, `admit`, or custom axiom declarations.
The preexisting B02 native-computation boundary is unchanged. `git diff --check` passed.
No Python/project/experiment code outside lean/ was changed.

## Independent review

A read-only reviewer compared the five B03 modules and both bridge scripts against
gu/clifford.py, gu/rarita.py and the README Reality table. No actionable code/fidelity
defects were found. The final documentation review confirmed fixed-instance completeness
and caught four theorem-inventory rows with an erroneously shared (9,5) qualifier;
those labels were corrected. No source expectations or mathematical signs were changed.
