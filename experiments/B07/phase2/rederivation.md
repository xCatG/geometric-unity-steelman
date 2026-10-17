# Independent B07 Phase 2 re-derivation

The independent calculation agrees with the production result on every required comparison.

Source: [`rederive.py`](rederive.py), committed as `be91369840984b16bc900397ee248544d5a0bd14` before its first execution. Command: `uv run python -m experiments.B07.phase2.rederive`; exit 0.
Production: [`result.json`](result.json), produced from `8a44e8ced16d091d67200ea4b4c5858c364a19ba`. Definitions: [`derivations.md`](derivations.md), H9–H14.

This is an independent implementation, not a blind comparison: the approved smoke values were known. Only `gu.clifford` gamma/Mono matrices are shared with production. The independent Phase 1 matrix/exterior arithmetic is carried forward as source, without importing any B07 module. The real-form construction, Spin matrices, sparse Fraction elimination, curvature tensors, gates, scalar Hodge arithmetic and Fourier matrix calculation are assembled here. No production result is read by `rederive.py`.

Scope: reading V, fixed metric and epsilon, flat model, varpi direction; the universal calculation is at (3,1). The sign table covers all signatures at n=4 and n=14. This does not independently classify the 14D universal space or establish curved/nonlinear equivalence.

## Comparison checklist

| Calculation | Agreement |
|---|---|
| Equivariant dimension | yes |
| Every equivariant grade block | yes |
| Block rank | yes |
| Four zero relations | yes |
| C1 kernel dimension | yes |
| C1 Einstein response dimension | yes |
| C1 curvature response image | yes |
| E_OP curvature response | yes |
| Every star/mass sign row | yes |
| Joint C1+C2 N0 | yes |
| Joint C1+C2 N1 | yes |
| Joint C1+C2 N2 | yes |
| Fourier CAA/pinned | yes |
| Fourier E_OP/pinned | yes |
| Fourier CAA/prime | yes |
| Fourier E_OP/prime | yes |
| YM CAA | yes |
| YM E_OP | yes |

## Equivariant space and gates

| Input grade / output grade | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| 0 | 0 | 2 | 0 | 2 | 0 |
| 1 | 2 | 0 | 6 | 0 | 2 |
| 2 | 0 | 6 | 0 | 6 | 0 |
| 3 | 2 | 0 | 6 | 0 | 2 |
| 4 | 0 | 2 | 0 | 2 | 0 |

Total dimension: **40**, agreeing block by block with production.

| Gate | Independent | Production |
|---|---:|---:|
| C1 | 8 | 8 |
| C1 Einstein response image | 2 | 2 |
| C1+C2, N0 | 0 | 0 |
| C1+C2, N1 | 0 | 0 |
| C1+C2, N2 | 0 | 0 |

The eight C1 basis responses have six zero rows and two nonzero rows: `(-1/2,0,1/4,0)` and `(0,-1/2,0,1/4)`. Their exact row space equals the production response image; basis signs and ordering need not agree. The four response coefficients are `(a,b,c,d)` in H13. Einstein dimension counts the nonzero Ricci response image under `2c+a=2d+b=0`.

E_OP independently gives `(2,0,-1,0)`, equal to production. The C1 Einstein survivors do **not** pass the joint C1+C2 gate under N0, N1 or N2.

## Four block relations

The 20 independently evaluated blocks have rank **16**, agreeing with production. The exact nullspace has these four independent relations (the second blocks exclude the outer −1/2 coefficient):

- `(-1) second[CC](F,B) + (-1) second[CA](F',B') + (-1) second[AC](F',B') + (1) second[AA](F,B) = 0`.
- `(-1) second[CC](F,B') + (1) second[CA](F',B) + (1) second[AC](F',B) + (1) second[AA](F,B') = 0`.
- `(-1) second[CC](F',B) + (-1) second[CA](F,B') + (-1) second[AC](F,B') + (1) second[AA](F',B) = 0`.
- `(-1) second[CC](F',B') + (1) second[CA](F,B) + (1) second[AC](F,B) + (1) second[AA](F',B') = 0`.

## Hodge adjoint and mass signs

All **40** independent rows agree exactly with production: `star_dag_sign_1form = -1 = (-1)^(n-1)` and `mass_sign = (-1)^q`, for both pinned and prime conventions.

| n | q values with mass +1 | q values with mass −1 | Adjoint sign, both conventions |
|---:|---|---|---:|
| 4 | 0, 2, 4 | 1, 3 | −1 |
| 14 | 0, 2, 4, 6, 8, 10, 12, 14 | 1, 3, 5, 7, 9, 11, 13 | −1 |

The independent calculation uses its own scalar exterior/Hodge arithmetic, checking every relevant basis pair. The Clifford trace factor cancels in these signs.

## Fourier variation at (3,1)

For CAA (required) and E_OP (additional), under both conventions, every check and every non-vacuity flag agrees with production. Ten wavevectors determine the homogeneous quadratic, linear and constant coefficients separately. The script factors out the known powers of i and calculates the remaining matrices over the rationals.

| Comparison | Result, both maps and conventions |
|---|---|
| κ⁰ action = printed term 1 | true |
| κ¹ action = repaired term 2 + printed term 3 | false |
| κ¹ action = repaired term 2 + derived term 3 | true |
| derived term 3 = −printed term 3 | true |
| κ² action = printed term 4 | false |
| κ² action = derived term 4 | true |
| derived term 4 = −printed term 4 | true |
| Each printed term nonzero somewhere | true |

“Repaired term 2” inserts the missing star; its literal printed form is ill-typed. At (3,1), q is odd, so printed term 4 has the opposite sign. The action coefficients are formed directly from its two Fourier legs; the comparison operator uses separately assembled metric adjoints and the Hodge codifferential.

## Yang–Mills principal symbol at (3,1)

| Map, pinned convention | Independent ratio set | Entries nonzero where YM vanishes | Production agreement |
|---|---|---:|---|
| CAA | {0, 2, 4, 6, 8} | 576 | yes |
| E_OP | {0, 8, 16, 24, 32} | 648 | yes |

Neither kinetic symbol is a common nonzero multiple of ordinary YM. This conclusion follows from the principal-symbol comparison, independently of whether X*X is scalar.

The script also records the prime-convention YM ratios (CAA: {−8,−6,−4,−2,0}; E_OP: {−32,−24,−16,−8,0}) with the same mismatch counts. The production artifact records YM only for the pinned convention, so these extra prime rows have no production row to compare; no agreement claim is made for them.

## Controls and limits

The independent run passes hand-specified controls for rational row elimination, a large integer, exterior antisymmetry, explicit gamma anticommutation and matrix trace, the Hodge square, and both hand-computed Shiab block terms. No floating-point arithmetic or numerical rank is used.

A read-only source review found no actionable mathematical or executed-path exactness defect. This re-derivation covers the registered Task 4 calculations; the separate production runner supplies the (1,3) survey, SO and 14D witnesses, and the remaining item-2 maps/signatures.

