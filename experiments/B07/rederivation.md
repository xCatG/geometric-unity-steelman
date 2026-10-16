# B07 independent matrix re-derivation

All 13 requested results agree with `result.json`: eight C1 kernels, two C2/N1 kernels and their nonzero-entry counts, and three named-branch C1 witnesses. C1 counts were also compared and agree.

Producer: `experiments/B07/rederive.py`, committed before this run at `de8ab674b3414374b9dcec621886aa0d039ac97a`. Comparison target: `experiments/B07/result.json` at `c7229e967fab4b87d1e254e712fc54c6e3b17ac5`. The producer, shared `gu/clifford.py`, and comparison target had no uncommitted changes when the comparison was made.

Exact command, from the repository root (exit 0):

```text
uv run python -m experiments.B07.rederive
```

## Conventions and independence

This is an independent algorithm, not a blind derivation: the B02 transcription, B07 plan's column/residual definitions, and the reference witness inputs were read. The script does not load `result.json` or import `gu.shiab`, `gu.cliffform`, `gu.forms`, or any B07 module. It shares only explicit `gu.clifford.Mono` matrices and gamma generation; multiplication and traces are matrix operations, with its own tuple-based exterior algebra and metric Hodge star. The script's docstring pins all chirality, generator, bracket, Hodge, family-coefficient, and trace conventions.

`Tr` is the actual matrix trace: the factor relative to the scalar-coefficient trace in `result.json` is `2^(n/2)`, hence 4 at (3,1) and 128 at (7,7). The C2 calculation stores `3*C2` to avoid thirds; its coefficients are therefore 12 times the reference C2 coefficients at (3,1). Both factors are nonzero and preserve kernels and entry counts. Off-diagonal C2 entries are polynomial cross coefficients, while diagonal entries are unpolarized values; the script accounts for their factor of two. The named-branch operator includes the printed -1/2.

Column order for every count vector is `F, F+B, F+B', F', F'+B, F'+B'`. The labels with `+` denote second-term columns without -1/2, not sums of columns. Their coefficients are `alpha, -alpha*gamma/2, -alpha*delta/2, beta, -beta*gamma/2, -beta*delta/2`.

## Result-by-result comparison

| Result | Independent output | Comparison with result.json |
|---|---|---|
| C1, CCC, (3,1) | kernel {0}, dimension 0; counts `[96, 144, 144, 96, 144, 144]` | agrees |
| C2_N1, CCC, (3,1) | kernel {0}, dimension 0; counts `[1776, 1716, 1824, 1776, 1716, 1824]` | agrees |
| C1, CCA, (3,1) | kernel {0}, dimension 0; counts `[96, 168, 96, 96, 168, 96]` | agrees |
| C1, CAC, (3,1) | kernel {0}, dimension 0; counts `[96, 168, 96, 96, 168, 96]` | agrees |
| C1, CAA, (3,1) | kernel {0}, dimension 0; counts `[96, 144, 144, 96, 144, 144]` | agrees |
| C2_N1, CAA, (3,1) | kernel {0}, dimension 0; counts `[1776, 1716, 1728, 1776, 1716, 1728]` | agrees |
| C1, ACC, (3,1) | kernel {0}, dimension 0; counts `[144, 144, 144, 144, 144, 144]` | agrees |
| C1, ACA, (3,1) | kernel {0}, dimension 0; counts `[144, 168, 96, 144, 168, 96]` | agrees |
| C1, AAC, (3,1) | kernel {0}, dimension 0; counts `[144, 168, 96, 144, 168, 96]` | agrees |
| C1, AAA, (3,1) | kernel {0}, dimension 0; counts `[144, 144, 144, 144, 144, 144]` | agrees |
| C1 witness, CCC literal, (7,7) | actual Tr `['-256', '0']`; Tr/128 `['-2', '0']` | agrees |
| C1 witness, CAA Einstein, (7,7) | actual Tr `['256', '0']`; Tr/128 `['2', '0']` | agrees |
| C1 witness, CAC chiral, (7,7) | actual Tr `['256', '0']`; Tr/128 `['2', '0']` | agrees |

The 4D enumeration covers the complex basis of 64 adjoint-valued one-forms: 8,320 symmetric C1 entries per column and 133,120 polarized C2 entries per column, including diagonal values. Exact complex nullspaces are computed after removing duplicate constraint rows. This proves the stated kernels in the dimension-4 analogue. The 14D results are three counterexamples at the recorded inputs; they are not an exhaustive 14D family classification. These statements concern the bosonic variation under reading V; no fermionic variation is computed here.

## Complete command output

```text
CONTROLS: PASS
COLUMNS: ["F", "F+B", "F+B'", "F'", "F'+B", "F'+B'"]
C1: {"mode": "CCC", "kernel_dimension": 0, "kernel": [], "nonzero": [96, 144, 144, 96, 144, 144]}
C2_N1: {"mode": "CCC", "kernel_dimension": 0, "kernel": [], "nonzero": [1776, 1716, 1824, 1776, 1716, 1824]}
C1: {"mode": "CCA", "kernel_dimension": 0, "kernel": [], "nonzero": [96, 168, 96, 96, 168, 96]}
C1: {"mode": "CAC", "kernel_dimension": 0, "kernel": [], "nonzero": [96, 168, 96, 96, 168, 96]}
C1: {"mode": "CAA", "kernel_dimension": 0, "kernel": [], "nonzero": [96, 144, 144, 96, 144, 144]}
C2_N1: {"mode": "CAA", "kernel_dimension": 0, "kernel": [], "nonzero": [1776, 1716, 1728, 1776, 1716, 1728]}
C1: {"mode": "ACC", "kernel_dimension": 0, "kernel": [], "nonzero": [144, 144, 144, 144, 144, 144]}
C1: {"mode": "ACA", "kernel_dimension": 0, "kernel": [], "nonzero": [144, 168, 96, 144, 168, 96]}
C1: {"mode": "AAC", "kernel_dimension": 0, "kernel": [], "nonzero": [144, 168, 96, 144, 168, 96]}
C1: {"mode": "AAA", "kernel_dimension": 0, "kernel": [], "nonzero": [144, 144, 144, 144, 144, 144]}
WITNESS_7_7: {"branch": "literal", "mode": "CCC", "k": 0, "t": [0, [0]], "a": [1, [0, 1]], "matrix_trace": ["-256", "0"], "normalized_trace": ["-2", "0"]}
WITNESS_7_7: {"branch": "Einstein", "mode": "CAA", "k": 0, "t": [0, [2]], "a": [1, [1, 2]], "matrix_trace": ["256", "0"], "normalized_trace": ["2", "0"]}
WITNESS_7_7: {"branch": "chiral", "mode": "CAC", "k": 0, "t": [0, [2]], "a": [1, [1, 2]], "matrix_trace": ["256", "0"], "normalized_trace": ["2", "0"]}
```

## Validation

`uv run python -m experiments.B07.rederive --controls-only` prints `CONTROLS: PASS`. The same controls run before every full survey. They check the Clifford relations, real and imaginary actual trace, all 4D basis Hodge identities, exterior orientation/repeated indices, hand-expanded first and second terms of (9.3), its -1/2 coefficient, nonzero diagonal/off-diagonal C2 entries, a known complex nullspace, rational/large-integer arithmetic, fixed-width integer and rational normalization, and rejection of float coefficients.

The C2 control uses `u=e^0 Gamma_0`, `v=e^1 Gamma_1` and the first CCC column. Since `uv+vu=2 e^01 Gamma_01`, its image is `4 e^023 Gamma_1 - 4 e^123 Gamma_0`. Therefore `D(u,u,v)=-16`, `D(v,u,u)=0`, and `D(v,u,v)=-16`, giving the tested off-diagonal `3*C2(u;u,v)=16` and diagonal `3*C2(u;v)=-16`.

Three deliberate faults were applied separately before committing, each failed an assertion, and each restoration was byte-verified by SHA-256:

| Fault | Assertion that caught it |
|---|---|
| Remove the metric factor in the Hodge star | `Hodge square` |
| Drop i from the A-bracket | `hand second term` |
| Change -1/2 to +1/2 in (9.3) | `hand minus half` |

A fresh code review found an accepted NumPy scalar could retain fixed-width arithmetic inside `Fraction`. Integer and NumPy-backed Fraction regressions were reproduced failing, then fixed by normalizing their integer components to Python integers. All three scratch regression tests passed after the fix; persistent controls for both cases are included in the committed producer.
