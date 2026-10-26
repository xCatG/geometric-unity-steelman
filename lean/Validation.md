# Final validation

Lean 4.24.0, x86_64-w64-windows-gnu, Release, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b.
Mathlib v4.24.0, exact manifest revision f897ebcf72cd16f89ab4577d0c826cd14afaafc7.
`lake exe cache get` completed successfully during setup.

## Clean-project build

Only the resolved `<lean-worktree>/lean/.lake/build` directory was removed.
Mathlib/dependency caches were retained. Command: `lake build` (default B02 and bridge targets).
This measures a clean build of this project, not compilation of Mathlib from source or download time.

```text
Exit=0; elapsed_seconds=114.932
info: B02/ConcreteHodge.lean:221:0: 'B02.Concrete.otherShiab_reparametrization' depends on axioms: [propext, Classical.choice, Quot.sound]
info: B02/ConcreteHodge.lean:222:0: 'B02.Concrete.otherShiab_readout_reparametrization' depends on axioms: [propext, Classical.choice, Quot.sound]
✔ [8764/8767] Built B02.ConcreteLinear (30s)
ℹ [8765/8767] Built B02.TensorCovariance (30s)
info: B02/TensorCovariance.lean:254:0: 'B02.Structural.tensor_dressed_covariance' depends on axioms: [propext, Classical.choice, Quot.sound]
info: B02/TensorCovariance.lean:257:0: 'B02.Structural.tensor_response_derivation' depends on axioms: [propext, Classical.choice, Quot.sound]
✔ [8766/8767] Built B02 (18s)
Build completed successfully (8767 jobs).
```

Two existing tactic-style linter warnings (`unnecessarySeqFocus`) in Headline and Bilinearity;
no errors. All 20 B02 source modules are imported by the root library.

## Actual Python comparisons

Executed from the worktree root with `UV_PROJECT_ENVIRONMENT=lean/.tools/python-env`
and `PYTHONDONTWRITEBYTECODE=1`. Each maintained bridge rebuilds its required Lean target.
Expectations call the actual `gu` functions and use exact arithmetic.

### uv run python lean/bridge/check.py

```text
Build completed successfully (2802 jobs).
PASS: 3115 exact Lean/Python cases
Dropped-index witness R_0103=R_0301=1, eta=(1,1,1,-1):
  pinned [B,*xi]_C = ()
  dropped [B,*xi]_C = ((15, 10, Fraction(-2, 1), Fraction(0, 1)),)
  dropped [B',*xi]_C = ((15, 5, Fraction(-2, 1), Fraction(0, 1)),)
```

### uv run python lean/bridge/samples.py

```text
Build completed successfully (1408 jobs).
PASS 22_CCC: ((1, 1, Fraction(3, 1), Fraction(0, 1)), (2, 2, Fraction(3, 1), Fraction(0, 1)), (4, 4, Fraction(3, 1), Fraction(0, 1)), (8, 8, Fraction(3, 1), Fraction(0, 1)))
PASS 22_CAA: ((1, 1, Fraction(9, 1), Fraction(0, 1)), (2, 2, Fraction(9, 1), Fraction(0, 1)), (4, 4, Fraction(9, 1), Fraction(0, 1)), (8, 8, Fraction(9, 1), Fraction(0, 1)))
PASS 40_CCC: ((1, 1, Fraction(3, 1), Fraction(0, 1)), (2, 2, Fraction(3, 1), Fraction(0, 1)), (4, 4, Fraction(3, 1), Fraction(0, 1)), (8, 8, Fraction(3, 1), Fraction(0, 1)))
PASS 40_CAA: ((1, 1, Fraction(9, 1), Fraction(0, 1)), (2, 2, Fraction(9, 1), Fraction(0, 1)), (4, 4, Fraction(9, 1), Fraction(0, 1)), (8, 8, Fraction(9, 1), Fraction(0, 1)))
PASS 31_CCC: ((1, 1, Fraction(-3, 1), Fraction(0, 1)), (2, 2, Fraction(-3, 1), Fraction(0, 1)), (4, 4, Fraction(-3, 1), Fraction(0, 1)), (8, 8, Fraction(-3, 1), Fraction(0, 1)))
PASS 31_CAA: ((1, 1, Fraction(3, 1), Fraction(0, 1)), (2, 2, Fraction(3, 1), Fraction(0, 1)), (4, 4, Fraction(3, 1), Fraction(0, 1)), (8, 8, Fraction(3, 1), Fraction(0, 1)))
PASS 11_CCC: ((1, 1, Fraction(-1, 1), Fraction(0, 1)), (2, 2, Fraction(-1, 1), Fraction(0, 1)))
PASS 11_CAA: ()
PASS: 8 additional exact signature sample cases
```

### uv run python lean/bridge/dimension_two.py

```text
Build completed successfully (1409 jobs).
PASS: 6 exact dimension-two contraction/embedding/response cases
Ric=g, S=2; nonzero response -F has (c,kappa)=(-1,0) and (1,1)
```

### uv run python lean/bridge/mutations.py

```text
Running reverse_star_sign
DETECTED reverse_star_sign: 274 mismatches; first star_0_0: Lean=((15, 0, Fraction(-2, 1), Fraction(3, 1)),), Python=((15, 0, Fraction(2, 1), Fraction(-3, 1)),)
Running drop_xi_raising
DETECTED drop_xi_raising: 35 mismatches; first xi: Lean=((3, 9, Fraction(1, 2), Fraction(0, 1)), (9, 3, Fraction(1, 2), Fraction(0, 1))), Python=((3, 9, Fraction(-1, 2), Fraction(0, 1)), (9, 3, Fraction(1, 2), Fraction(0, 1)))
Running remove_A_imaginary
DETECTED remove_A_imaginary: 408 mismatches; first bracket_0_0_0_0_A: Lean=((0, 0, Fraction(-34, 15), Fraction(64, 15)),), Python=((0, 0, Fraction(-64, 15), Fraction(-34, 15)),)
UNCHANGED SHA256 Concrete.lean: 648457949121ff22ce8e62d6364c535cb575a4519f9e0a2a2828209d12822152
UNCHANGED SHA256 Bridge.lean: 4adc076c9b254aa380053f4417942328ff3b4e5a71c16a3274a9fdf866e2d8e2
```

The 3,115 core comparisons use the freshly built native executable. The 8 signature
samples and 6 dimension-two cases use Lean's interpreter. The seeded fault run uses
disposable source copies, unchanged Python expectations and verifies maintained-source hashes.
The bridge is finite executable evidence, not a formal semantics equivalence proof for Python.

## Axiom and source audit

After the clean build: `lake env lean Audit.lean` exited 0. All public entries matched
`bridge/inventory.py`'s generated inventory. Full output is in `AxiomAudit.txt`.

```text
PASS: 179 public axiom outputs matched inventory; no sorryAx or undeclared axioms
Native compiler trust: 11 theorem dependencies:
B02.Concrete.dropped_witness_inner_BPrime
B02.DimensionTwo.embedded_metric
B02.DimensionTwo.description_kappa_zero
B02.DimensionTwo.description_kappa_one
B02.DimensionTwo.response_nonzero
B02.DimensionTwo.nonunique_parameter_descriptions
B02.Samples.split_CCC
B02.Samples.split_CAA
B02.Samples.euclidean_CCC
B02.Samples.euclidean_CAA
B02.Samples.dimension_two_CCC
```

The source scan found no `sorry`, `admit`, or custom axiom declarations in maintained Lean sources.
`git diff --check` passed. All changes relative to base 36add8f are under `lean/`.

## Independent review

The read-only reviewer checked concrete semantics, witness symmetries, tensor covariance/derivation,
scalar extension and final documentation. Fixed the stale-bridge risk by requiring builds, added
both curvature antisymmetry certificates, replaced an arithmetic-only dimension-two witness with
actual contractions/embedding, and imported every audited module. Final review reported no material
scope overclaims in COVERAGE.md or THEOREMS.md. Remaining mathematical gaps are explicitly listed.
