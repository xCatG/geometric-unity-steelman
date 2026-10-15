# B02 Lean formalization

Lean is pinned to `leanprover/lean4:v4.24.0`; Mathlib is pinned by
`lake-manifest.json` to `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (tag `v4.24.0`).
Install elan, then from this directory:

```powershell
lake exe cache get
lake build
```

From the repository root, compare the executable model with the actual Python implementation:

```powershell
$env:UV_PROJECT_ENVIRONMENT = "$PWD/lean/.tools/python-env"
$env:PYTHONDONTWRITEBYTECODE = "1"
uv run python lean/bridge/check.py
```

`--lean-run` uses Lean's interpreter instead of the compiled bridge executable.
The bridge checks 3,115 exact cases in signature (3,1), including every form/blade
basis input for star, every Clifford blade pair for both brackets with four wedge
contexts, and every basis input for the adjacent generator actions. It also checks
xi, all four Phi bases, all eight Shiab modes, and the missing-index-factor witness.
It calls the repository's `gu` functions; expectations are not copied Lean output.

The model uses finite subsets of `Fin n`, exact Gaussian rationals represented by
`QuadraticAlgebra ℚ (-1) 0`, and normalized sparse term lists. `coefficient` is the
extensional interpretation; list order is not mathematical equality. The Hodge
and Clifford operations share the general sign definitions in `B02/Signs.lean`.
Chirality phase is an explicit argument and is cross-checked against Python.

Formal proof coverage and outstanding instantiation obligations are recorded in
`COVERAGE.md`, with every theorem mapped in `THEOREMS.md`. An abstract theorem
with uninstantiated operation laws is not a proof of those laws for the executable model.

The negative-scope B-prime witness currently uses `native_decide`; in Lean 4.24
its axioms include `Lean.ofReduceBool` and `Lean.trustCompiler`. The B witness,
its Bianchi identity, and the pinned-B witness use kernel reduction.


Additional exact checks, from the repository root with the environment above:

```powershell
uv run python lean/bridge/samples.py
uv run python lean/bridge/dimension_two.py
uv run python lean/bridge/mutations.py
uv run python lean/bridge/inventory.py
cd lean
lake env lean Audit.lean
```

The sample and dimension-two certificates also use `native_decide`. All native
axiom dependencies, including downstream theorems, appear in `AxiomAudit.txt`.
The mutation check uses disposable copies, reverses the star sign, drops xi's
raising factors, and removes the A-bracket imaginary factor. It requires each
fault to disagree with unchanged expectations from the actual Python functions.

`Validation.md` records the final clean-project build timing and bridge output.
A clean-project build removes only this project's `.lake/build`; Mathlib and
other dependency caches remain populated by `lake exe cache get`.
