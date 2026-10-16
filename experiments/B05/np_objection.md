# B05: Nguyen–Polya objection and April-draft object map

Author: Codex. Source check: 2026-10-15 America/Los_Angeles (2026-10-16 UTC).

## Sources and scope

Nguyen and Polya, *A Response to Geometric Unity*, February 23, 2021, §3.2, printed pp. 6–7; adjacent §3.1 supplies its identification premise. [Original PDF](https://files.timothynguyen.org/geometric_unity.pdf). Download SHA-256: `66c7caafce188744c7c7e6e085b40f849e0d1218a07ae675f8add187e82fc71f`. Access recorded at `2026-10-16T01:46:54.851220+00:00`. Both pages were rendered at 170 dpi and read as images; p.5 was additionally read at 150 dpi to follow (3.1). Text extraction was a cross-check.

The comparison source is Weinstein's April 1, 2021 working draft, SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, especially pp. 24, 31–42, 46, 50–51 and 60–62, with appendix checks on pp.65–66 and 68. Equation references below refer to that draft unless prefixed NP. See [the B05 transcription](transcription.md) for the local source record; this map checks the underlying images independently.

This file supplies a short excerpt and summary, **not a verbatim reproduction of the whole externally sourced §3.2**. It records a historical objection and the assumptions needed to transfer it. It does not compute an anomaly or decide a gauge symmetry.

## Short excerpt and summary of §3.2

> “a subgroup of the gauge group consists of axial transformations”

The accompanying printed formulas are \(\psi\mapsto\exp(\bar\gamma\theta)\psi\) and \(\bar\gamma\psi_{L/R}=\pm\psi_{L/R}\). No explicit i appears in the exponential. Preserve that convention; identifying a real generator with an imaginary multiple requires additional input.

NP argues that gauging the full unitary spinor group includes an anomalous axial direction coupled to the central connection. They identify no cancellation mechanism. Restricting to Spin would remove that problem, they argue, but would destroy the identification needed for their Shiab construction. This concerns the earlier presentation, rather than an analysis of the later April operator. [NP, §3.2, pp. 6–7](https://files.timothynguyen.org/geometric_unity.pdf).

## Object-by-object map

“Counterpart” means a located April-draft object, not equivalence of theories or proof that the objection transfers.

| Object | NP object/premise | April-draft counterpart and evidence | Transfer condition / open item |
|---|---|---|---|
| Group | U(128), with a tilted construction. | H=U(64,64) and complex Dirac representation, (3.31), p.24; gauge transformations ℋ in (5.3), p.32; ℋ⋉𝒩 in (5.8), p.33; tilted map τ in (6.4), p.36. | Same-sized complex spinor fiber does not identify the compact and indefinite real forms. The action and conventions must be supplied for the chosen group. |
| Central U(1) | Central phase connection; claimed anomaly source. | Scalar phases belong to U(64,64); (3.34) gives its adjoint bundle and (5.5) the adjoint-valued 1-forms. (8.6), p.42 includes the degree-zero class among the classes requiring complex phases. | Algebraic availability of iI follows from any Hermitian A: (iI)†A+A(iI)=0. A separately specified central coupling and its fermion charges are **not located** in the checked pages. |
| Gauged axial transformation | The displayed chirality exponential. | The chirality/volume direction has a candidate counterpart in Λ¹⁴⊂so(64,64), (8.5), p.42; chiral spinor bundles also occur on pp.51,61. | No explicit axial transformation law for all four fields and dressings was located. Distinguish C from iC and distinguish Lie-algebra membership from covariance of the action; see below. |
| Fermion content | Fourteen-dimensional spinors with Weyl halves. | ν,ζ in (5.1)–(5.2), p.31; four independent classical barred/unbarred fields with ν,ν̄∈Ω⁰(Y,$), ζ,ζ̄∈Ω¹(Y,$), p.46; decomposition/RS discussion, pp.50–51; chirality discussion, pp.60–62. | The anomaly-relevant independent fields, reality constraints, representation charges, kinetic complex and cancellation contributions must be established. Fiber branching alone is insufficient. |
| Kinetic operator | No explicit kinetic matrix in §3.2. | Candidate matrix \(\not{\mathcal D}_\omega\) in (9.16), its dressed equation (9.17), and variations (9.18)–(9.19), p.46. The source permits a different lower-right quadrant. | **No counterpart in NP §3.2 to this particular matrix is specified.** Bar, adjoint, contraction and Shiab-on-spinor conventions remain needed before a covariance test. |
| Full-adjoint/exterior identification | Complexified identification (3.1), discussed in §3.1. | (8.3)–(8.7), p.42 use the split real Clifford setting and grade-dependent placement in so(64,64) and its complement in u(64,64). (8.1), p.41 supplies a family of invariant-form operations. | Compare real forms, complexifications, module actions and phase choices explicitly. A dimension match alone does not identify brackets, pairings or a particular Shiab operator. |
| Shrinking to Spin | Spin(14) removes the stated problem but dimensionally breaks (3.1). | Spin(7,7) embeds into H on p.24; p.42 uses Spin(7,7)-invariant tensors inside the enlarged algebra. | **No source prescription found** that replaces H by Spin(7,7) while retaining the same action. A reduced full-adjoint identification has a dimension obstruction; whether some specified Shiab construction survives is a different question. |

## What (8.5)–(8.6) establish about the axial direction

The p.42 image places Λ¹⁴ in the real so(64,64) part of (8.5). The classes displayed in (8.6), which require factors of i in the complexification, have degrees 0,3,4,7,8,11,12; degree 14 is absent. This is source evidence for distinguishing the real volume direction from its imaginary multiple.

For the real Cl(7,7) volume element Ω, the Clifford relations give

\[
\Omega^2=(-1)^{14\cdot13/2+7}=1.
\]

Thus a normalized real chirality C can be chosen as ±Ω. With a candidate nondegenerate Hermitian form satisfying C†=C and AC=−CA,

\[
C^\dagger A+AC=0,\qquad
(iC)^\dagger A+A(iC)=2iAC\ne0.
\]

Consequently C lies in the candidate isometry algebra whereas iC does not. For real parameter t, exp(tC) is a noncompact chiral scaling, distinct from exp(itC). The identification of a particular A is still a reconstruction choice: p.24 does not print its matrix. These facts do not specify which transformations GU gauges or prove that its fermionic action is covariant.

In particular, for a bilinear with ψ̄=ψ†A and A fixed, δψ=Sψ induces δψ̄=ψ̄A⁻¹S†A. Covariance tests must include this barred action and variations of K and its coefficients/dressings. Merely dropping an algebra generator, or testing a commutator with frozen K, is not an anomaly calculation.

## The precise dimensional obstruction and its limit

In fourteen dimensions, the full exterior algebra has dimension 2¹⁴=16,384; u(64,64) has the same real dimension. By contrast, spin(7,7) has dimension 14·13/2=91. After complexification these numerical dimensions are unchanged as complex dimensions. Thus the full adjoint of the reduced Spin group cannot be isomorphic to the full exterior algebra. This arithmetic does not rule out maps involving selected degrees, projections or invariant tensors: such a claim requires the actual proposed operator and its equivariance law.

The open transfer questions are therefore concrete: identify the gauge action on all four fermions and coefficients; pin the pairing, reality condition and kinetic operator; then establish the quantum representation/measure and any anomaly or cancellation. This map supplies none of those missing choices by analogy.
