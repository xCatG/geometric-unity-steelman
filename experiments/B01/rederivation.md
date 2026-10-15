# B01: independent trace/traceless derivation

Author: Codex, 2026-10-15. This is a hand derivation, completed before running
the Task 4 tests. I implemented the original experiment and have seen its
expected values: independence here means a different mathematical route, not
a blinded second author. No execution of `dewitt_family.py` supplies any
expectation below. The second PDF reader's review is reported to the orchestrator.

Provenance: `[ext]` for the family; `[GU-recon]` for its interpretation.
Evidence: `verified:experiments/B01/rederivation.md`, with exact regressions in
`verified:tests/test_b01.py`. Scope: `identity` for the algebra below; the
specific mirror configuration is also a `counterexample` to a universal
claim that a base-only mirror preserves the total signature class.

## Orthogonal decomposition

Let g = eta = diag(1,-1,-1,-1), t(H) = tr(g H), and
F(H,K) = tr(g H g K) on real symmetric 4 by 4 matrices. Since g squared is I,
t(g) = 4 and F(g,H) = t(H). Every H splits uniquely as

    H = H_0 + (t(H)/4) g,   t(H_0) = 0.

For B_lambda = F - lambda t tensor t, the two summands are orthogonal:

    B_lambda(H_0,g) = 0,
    B_lambda(g,g) = 4 - 16 lambda = 4(1 - 4 lambda),
    B_lambda(H_0,K_0) = F(H_0,K_0).

To count signs without diagonalizing the implementation's Gram matrix, write
H in blocks as [[a,b^T],[b,C]], where C is symmetric 3 by 3. Then

    F(H,H) = a^2 + tr(C^2) - 2 b^T b,
    t(H) = a - tr(C).

On t(H)=0, a=tr(C). The six-dimensional C subspace is positive definite,
because (tr C)^2 + tr(C^2) is strictly positive for nonzero real symmetric C.
The three-dimensional b subspace is negative definite. Thus the traceless
inertia is (6,3,0), independently of lambda. Adding the trace line proves
the following table for every real lambda, including the degenerate boundary.

## Vertical and chimeric tables

All tuples below are (positive, negative, zero). For C = s_H eta direct-sum
s_V B_lambda, the horizontal inertia is (1,3,0) for s_H=+1 and (3,1,0) for
s_H=-1. Negating a summand swaps its positive and negative counts.

| lambda | B_lambda | C(+,+) | C(+,-) | C(-,+) | C(-,-) |
|---|---|---|---|---|---|
| < 1/4 | (7,3,0) | (8,6,0) | (4,10,0) | (10,4,0) | (6,8,0) |
| = 1/4 | (6,3,1) | (7,6,1) | (4,9,1) | (9,4,1) | (6,7,1) |
| > 1/4 | (6,4,0) | (7,7,0) | (5,9,0) | (9,5,0) | (7,7,0) |

This matches every case in [result.json](result.json), including -1, 0, 1/8,
1/4, 1/2 and 1. It also explains the registered spectrum: in the elementary
symmetric basis the off-diagonal directions have norms -2 (three) and +2
(three). The diagonal Euclidean orthogonal complement of (1,-1,-1,-1) has
eigenvalue 1 (three); the normalized trace vector g/2 has norm 1-4 lambda.
The trace-vector norm 4(1-4 lambda) is not a conflicting eigenvalue: g has
Euclidean coefficient length 2.

## Base mirror (F1)

Replace g by -g while fixing lambda and both direct-sum signs. Each term of
F contains two inverse-metric factors, and the trace product also contains
two. Therefore B_lambda[-g](H,K) = B_lambda[g](H,K) identically. The same
argument holds for general invertible g using g inverse. The traceless
kernel is unchanged; its defining trace functional only changes sign.
The tangent map H -> -H for the mirror on metric space also contributes
two signs and does not change this conclusion.

The horizontal metric changes sign, so the total does not merely negate.
For the README's split configuration (lambda,s_H,s_V)=(1/2,-1,-1):

| Base supplied | Horizontal | Vertical | Total |
|---|---|---|---|
| eta | (3,1,0) | (4,6,0) | (7,7,0) |
| -eta | (1,3,0) | (4,6,0) | (5,9,0) |

This is the exact expectation for the F1 tests. In draft negative-first
order the latter is (9,5). For the other chosen vertical sign, mirroring
(9,5,0) gives (7,7,0); both chosen branches toggle signature class.
No statement about which signature is physical follows.

## Source audit and limits of reconciliation

I read rendered printed pages 18-22 of the [April 2021 primary draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf),
SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.
The [transcription](transcription.md) agrees on the relevant equations and
signature enumeration. Under a single consistent signature order and the
positive double contraction of (3.8), the traceless count forces the first
slot to count negatives. This is R1; (3.8) alone does not declare a slot
order or exclude a mixed-order reading. With these premises, s_H=-1.

The four rows of the [README](README.md) are correct under R1:

| Draft vertical (neg,pos) | lambda, s_V | Our total (pos,neg) | Draft total (neg,pos) |
|---|---|---|---|
| (3,7) | 0,+1 | (10,4) | (4,10) |
| (7,3) | 0,-1 | (6,8) | (8,6) |
| (4,6) | 1/2,+1 | (9,5) | (5,9) |
| (6,4) | 1/2,-1 | (7,7) | (7,7) |

The match verdict holds as the README's explicit reconstruction: reverse
the trace sign at fixed magnitude, retaining the Frobenius traceless block.
This yields lambda=1/2 exactly. The draft supplies the trace signature but
no separate magnitude formula for the modified trace block. More generally,
if its trace norm is -4c with c>0 and its traceless block is F, the exact map
is lambda=(1+c)/4. Thus the signature match is unconditional within R1,
whereas the specific no-rescaling lambda=1/2 map assumes c=1. An overall
positive rescaling of the vertical summand cannot remove this relative
trace/traceless normalization freedom. These qualifications do not alter
any inertia table.

For the isolated (9,5) remark, the README's two readings both work: changing
slot order describes the same bilinear form; staying in R1 instead gives
the overall negative of its (5,9) configuration. This is an interpretation,
not a uniquely recoverable authorial intent. In fixed positive-first order,
9-5=4 and 5-9=-4 are both 4 modulo 8, so these readings preserve the
signature classes relevant to the planned comparison.

One claimed repair needs correction: changing only the trace sign cannot
make a base-only mirror cosmetic. It changes the positive index by one,
whereas mirroring the horizontal Lorentzian summand changes it by two.
For the split example, mirroring and also undoing the trace flip gives
(4,10,0), not (7,7,0). Correlating the overall vertical sign with the base
sign does work: both summands then negate, preserving the signature class
up to overall sign. Consequently the two operations are equivalent only
on the two-class quotient with the chosen trace sector fixed, not identical
choices of metric. Detailed disagreements and severities are in the task
report; Claude-owned documents are unchanged.
