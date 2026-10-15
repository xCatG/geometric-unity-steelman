# GU gap register

Research snapshot: 2026-10-14; B01/A01 and B02 updated 2026-10-15. B01 has an exact fibrewise reconstruction and a base-mirror finding. B02 has an exact algebraic-curvature response: the literal CCC reading is obstructed as an Einstein contraction within the pinned ansatz, while specified reconstructed readings pass. No Lean proof or physical validation is claimed.

## Priorities

Cost is the effort for the **next check**, not for resolving the whole research question. Importance concerns the proposed theory; H/M/L mean high/medium/low. Dependencies identify shared specifications, not a requirement to solve every foundational problem before exploring a toy model.

| Priority | Entry | Question | Importance | Next-check cost | Immediate deliverable |
|---|---|---|---|---|---|
| 1 | B01 | Signature as a function of the vertical trace coefficient and chimeric metric signs | H | L | Carry the reconciled conventions and F1 into both signature branches |
| 2 | B02 | Shiab response beyond the checked algebraic-curvature ansatz | H | M | Carry the verified convention map into general gauge curvature and dynamics |
| 3 | B03 | Spinor/vector-spinor branching and the claimed third generation | H | M | Branching table with chirality, reality, and unwanted sectors |
| 4 | B05 | Actual gauged symmetry and anomalies in 14D and 4D | H | M | Fermion/generator inventory before computing an anomaly |
| 5 | B04 | Reality conditions, positive physical states, and kinetic signs | H | M | Quadratic-action diagnostic for one specified background |
| 6 | B07 | Does the proposed action yield the stated equations? | H | M | One independent variation with all dependencies retained |
| 7 | B08 | Exactness, sign conventions, and deformation-complex closure | H | M | Convention sheet and one explicit operator composition |
| 8 | B09 | Does observation yield closed four-dimensional dynamics? | H | M | Counterexample or closure criterion for a toy restriction |
| 9 | B10 | Chimeric spinors versus tangent spinors and global choices | M | M | Bundle/connection dependency diagram |
| 10 | B06 | Affine fermionic symmetry versus spacetime supersymmetry | H | M | Candidate superbrackets and applicable hypotheses |
| 11 | B11 | Higgs representation and potential | H | H | Identify a scalar candidate before deriving its action |
| 12 | B12 | Quantum completion | H | H | Record the required quantum data; no completion proposed |

Section A corrects the implementation blueprint. Section B investigates the theory. Fixing an A-entry is not evidence that the corresponding B-entry is solved.

## Sources, chronology, and labels

- **GU:** Eric Weinstein, *Geometric Unity: Author's Working Draft, v1.0*, April 1, 2021, [primary PDF](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf). Page citations use the document's printed pages, which agree with one-based PDF pages in this copy.
- **NP:** Timothy Nguyen and Theo Polya, *A Response to Geometric Unity*, February 23, 2021, [author-hosted PDF](https://files.timothynguyen.org/geometric_unity.pdf), 10 pages. **NP critiques the 2013/2020 lecture presentation, not the subsequently published April draft.** Its Euclidean `U(128)` reconstruction must not silently replace GU's later `U(64,64)` setup.
- **T:** David Tong, *Gauge Theory*, chapter 3, [author's notes](https://davidtong.org/pdfs/teaching/gauge-theory/gauge3.pdf), especially sections 3.4.2–3.4.3, printed pp. 161–167, for the four-dimensional anomaly criteria.
- **W:** Edward Witten, *Quantization of Chern-Simons Gauge Theory with Complex Gauge Group*, CMP 137 (1991), 29–66, [publisher record and abstract](https://doi.org/10.1007/BF02099116). This handoff checked the abstract and bibliographic scope, not the full paper's unitarity arguments. NP cites it as reference 15.
- **O:** the repository's [overview.md](../../overview.md), tasks 1–4; an implementation proposal, not a primary definition of GU.

Access date: 2026-10-14. The parallel source collector owns `sources/`; local S-ids will be used if its index is available before handoff. URLs and page/section locators above remain the fallback.

**Provenance and evidence are separate.** `[GU-orig]` identifies a draft claim, `[GU-recon]` an interpretation, `[lit]` a literature claim, and `[ext]` a proposed repair or explicit new assumption. Each checked claim states `verified:<tracked path>` and its scope (`identity`, `sampled` or `counterexample`); verification does not erase its provenance. “Unresolved” does not mean false. Short source statements below identify mathematical facts to audit; the repair proposals and next checks are our own analysis.

## A. Defects in overview.md

### A01 — A selected signature is presented as the foundation without its choices

- **Provenance / evidence / scope:** `[GU-recon]`; `verified:experiments/B01/rederivation.md`, `verified:experiments/B01/result.json`, `verified:tests/test_b01.py`; `identity` for the fibrewise signature map under R1. The physical selection remains `unverified`.
- **Draft says:** `[GU-orig]` GU sections 3.1–3.5, pp. 19–22, permit trace/sign choices and adopt `(7,7)`; the isolated `(9,5)` alternative admits the readings recorded in the [reconciliation](../../experiments/B01/README.md).
- **Status / gap:** The [exact experiment](../../experiments/B01/result.json) and [independent derivation](../../experiments/B01/rederivation.md) reproduce both live signature classes. O tasks 1 and 4 fix `(9,5)` without specifying those choices; neither class is physically selected by this algebra.
- **Counterargument / repair:** `[ext]` Retain both `(7,7)` and `(9,5)` as explicit configurations, recording slot order, base sign, vertical sign and trace normalization. F1 shows that mirroring the base alone can change the total class; it is not merely a notation change.
- **Dependencies:** B01 and B10. **Importance / cost:** H / L.
- **Next check:** Carry this convention map into the downstream representation tests. A claimed physical preference needs further evidence beyond the signature computation.

### A02 — Dirac, Weyl, real, and complex spinors are conflated

- **Tags / evidence:** `[GU-orig]`, `[GU-recon]`, `[ext]`; no Clifford implementation checked here.
- **Draft says:** GU section 3.5, equations (3.18)–(3.28), pp. 22–23, distinguishes 128-component Dirac and 64-component Weyl modules in its split construction.
- **Gap / source:** O task 4 calls its space “128-dimensional chiral” without a base field, while task 1 specifies 128-square gamma matrices. Over the complex numbers the full 14D Dirac module has dimension 128 and each Weyl half 64. Odd Clifford multiplication exchanges chirality. A real dimension count, a complex dimension count, and a reality constraint cannot be interchanged. The matrix `A` in Dirac conjugation also needs its invariant pairing convention.
- **Counterargument / repair:** `[ext]` Declare the coefficient field, Clifford sign, chirality operator, any reality condition, and the invariance identity for `A`. Begin with the complex Dirac module; establish real forms separately. Formalizing a Clifford algebra alone is not formalizing a global spinor bundle or a physical inner product.
- **Dependencies:** B01, B03, B10. **Importance / cost:** H / L.
- **Falsifiable next check:** Check all Clifford relations, chirality eigenspace dimensions, and `rho(g)^dagger A rho(g)=A` for the stated Spin representation. A failed identity rejects the proposed representation/pairing, not GU in general.

### A03 — The Shiab codomain and component count are wrong for the intended bosonic equation

- **Tags / evidence:** `[GU-orig]`, `[GU-recon]`, `[ext]`; typing analysis, no operator implementation.
- **Draft says:** GU equation (9.2), p. 43, specifies an adjoint-valued 2-form to adjoint-valued 13-form operator.
- **Gap / source:** O task 2 substitutes a spinor-valued target. Its “91 versus 14” compares an internal Lie-algebra dimension with an exterior-form dimension; it omits coefficient-bundle factors. The enlarged GU adjoint is also not simply `so(9,5)`. Under full Spin equivariance, central `-1` fixes tensor inputs but negates a lone spinor output; therefore a tensor-only map of that specified type must vanish. This is a short representation-theoretic argument about **O's typing**, not a no-go theorem for adjoint-valued Shiab maps.
- **Counterargument / repair:** `[ext]` Restore `Omega^2(Y,ad P) -> Omega^13(Y,ad P)` and distinguish matrix-valued Clifford multiplication from a spinor section. An unpaired spinor input changes the parity argument; a spinor bilinear alone does not.
- **Dependencies:** B02. **Importance / cost:** H / L.
- **Falsifiable next check:** Type every contraction, including all coefficient spaces. Reject any candidate whose free indices or central-character action disagree with the declared target.

### A04 — Neither a canonical torsion 3-form nor an exhaustive search is specified

- **Tags / evidence:** `[GU-orig]`, `[GU-recon]`, `[ext]`; unresolved search specification.
- **Draft says:** GU section 7, pp. 39–40, uses an augmented torsion in `Omega^1(Y,ad P)`; section 8, pp. 41–42, gives an operator family.
- **Gap / source:** O task 2 inserts a “canonical” ordinary 3-form without defining its origin, transformation law, or skew-torsion assumption. Arbitrary torsion is not automatically a totally antisymmetric 3-form. “All non-vanishing combinations” is unbounded without polynomial degree, derivatives, allowed invariant tensors, and equivalence relations.
- **Counterargument / repair:** `[ext]` Start from the draft's fields and candidate operator. If a 3-form is added, label it additional structure. Specify a finite ansatz and quotient by known tensor identities before searching.
- **Dependencies:** A03, B02. **Importance / cost:** H / L.
- **Falsifiable next check:** Publish a finite basis and its equivariance equations; solve for its invariant subspace. A zero-dimensional result excludes only that declared basis/ansatz.

### A05 — Curvature restriction is confused with a metric decomposition and Higgs derivation

- **Tags / evidence:** `[GU-orig]`, `[GU-recon]`, `[ext]`; no pullback or Higgs computation performed.
- **Draft says:** GU section 3.6, pp. 24–26, treats observation by a section; section 11, p. 49, distinguishes bundle pullbacks from jets of fields.
- **Gap / source:** O task 3 lists extrinsic curvature as a part of the metric. It is derivative embedding data. Gauss–Codazzi controls tangential ambient curvature; it does not determine the entire 14D scalar curvature from a slice without normal/mixed curvature and further geometric data. A scalar expression in extrinsic curvature has not thereby acquired Higgs quantum numbers or the required potential.
- **Counterargument / repair:** `[ext]` Specify the section, ambient metric, tangent/normal splitting and normal connection. Derive the induced metric and curvature identities first, then identify a scalar representation and its effective action. Do not substitute an arbitrary 14D embedding for the metric-bundle construction without labeling the change.
- **Dependencies:** B01, B09, B11. **Importance / cost:** H / M.
- **Falsifiable next check:** Compare the direct ambient/slice curvature calculation with the proposed decomposition for one nontrivial explicit embedding. Missing mixed or normal terms refute that formula.

### A06 — Traceless generators are not the anomaly-cancellation criterion

- **Tags / evidence:** `[lit]`, `[ext]`; criteria sourced, GU spectrum not checked.
- **Draft says:** GU section 9.3, pp. 46–47, supplies a fermionic ansatz; sections 11 and 12.9–12.10, pp. 49–53 and 60–63, discuss emergent chirality.
- **Gap / source:** O task 4 asks only for vanishing single-generator traces. Four-dimensional local non-Abelian anomalies instead depend on chirality-weighted cubic traces, and global anomalies require separate checks; see T sections 3.4.2–3.4.3. The representation content and the embedding of `SU(4) x SU(2) x SU(2)` are prerequisites. A 4D check also cannot answer NP section 3.2's 14D objection.
- **Counterargument / repair:** `[ext]` Specify each effective Weyl multiplet, multiplicity, chirality, charges, and the global gauge group. Check local and relevant global anomalies at each dimension where the theory is intended to be quantized. Lean should certify the correct finite statement, with assumptions explicit.
- **Dependencies:** B03, B05, B09. **Importance / cost:** H / M.
- **Falsifiable next check:** Compute the complete signed anomaly coefficients for a specified proposed 4D spectrum and count relevant `SU(2)` global-anomaly contributions. Any uncancelled coefficient rejects that spectrum.

## B. Gaps and research questions in GU

### B01 — Signature choices and their geometric meaning

- **Provenance / evidence / scope:** `[GU-recon]`; `verified:experiments/B01/rederivation.md`, `verified:experiments/B01/result.json`, `verified:tests/test_b01.py`; `identity` for the fibrewise reconstruction and F1 under the conventions below. The lambda family itself remains `[ext]`.
- **Verdict:** **Match: holds under R1**, as in the [README](../../experiments/B01/README.md): all four draft totals and both live signature classes are reproduced. R1 assumes a uniform negative-first signature order and the literal positive double contraction. The exact lambda=1/2 representative additionally preserves the trace magnitude while reversing its sign. The [independent derivation](../../experiments/B01/rederivation.md#source-audit-and-limits-of-reconciliation) records these qualifications; an unstated trace magnitude does not affect the inertia verdict.
- **Draft says:** `[GU-orig]` Equations (3.8)–(3.10), p. 19, and section 3.5, p. 22, leave trace and relative direct-sum signs open. The [transcription](../../experiments/B01/transcription.md) preserves the alternative readings. The draft supplies no DeWitt parameter or counterpart of the degenerate lambda=1/4 boundary.
- **Remaining gap:** The signature calculation selects no physical sector and establishes no global splitting of TY. Physical selection remains `unverified`.
- **Dependencies:** B10 for global interpretation; A01 for blueprint correction. **Importance / cost:** H / L for convention checks; physical selection is outside this algebraic check.
- **Next check:** Keep both signature classes in downstream B02 work with explicit conventions. Resolve the meaning of the base mirror before treating it as a physical equivalence.

**Family and exact evidence.** Set `eta=diag(1,-1,-1,-1)`, take real symmetric 4-square matrices, and define

`B_lambda(H,K) = tr(eta H eta K) - lambda tr(eta H) tr(eta K)`.

The [hand trace/traceless split](../../experiments/B01/rederivation.md) proves traceless inertia `(6,3,0)` and trace norm `4(1-4 lambda)`. The symbolic eigenvalues in the elementary symmetric basis are `-2` (three), `+2` (three), `+1` (three), and `1-4 lambda` (one). Here and below inertia means **(positive, negative, zero)**:

| Parameter | Vertical inertia | Character |
|---|---|---|
| `lambda < 1/4` | `(7,3,0)` | Nondegenerate |
| `lambda = 1/4` | `(6,3,1)` | Degenerate; unsuitable for an ordinary nondegenerate Hodge star |
| `lambda > 1/4` | `(6,4,0)` | Nondegenerate with reversed trace-direction sign |

For `lambda=1/2` (and every `lambda>1/4`), exact direct-sum counts of `s_H eta direct-sum s_V B_lambda` give:

| `s_H` | `s_V` | Total inertia |
|---|---|---|
| `+1` | `+1` | `(7,7,0)` |
| `+1` | `-1` | `(5,9,0)` |
| `-1` | `+1` | `(9,5,0)` |
| `-1` | `-1` | `(7,7,0)` |

**F1 — A base-only mirror changes the total signature class.** `[GU-recon]`; `verified:experiments/B01/rederivation.md`, `verified:tests/test_b01.py`; `identity` for vertical evenness and `counterexample` for a universal cosmetic-mirror claim. The two inverse-metric factors make B_lambda unchanged by eta -> -eta, while the horizontal summand negates. The draft split configuration `(lambda,s_H,s_V)=(1/2,-1,-1)` therefore changes from `(7,7,0)` to `(5,9,0)`. Symbolic Gram equality and this exact case are pinned in the tests. This note belongs inside B01 because it concerns the same relative-sign choice and evidence, rather than a new independent obstruction. Reversing the whole vertical summand as well would preserve the class up to overall sign; reversing only the trace line cannot do so. That correlated-sign rule would be an `[ext]` assumption.

Evidence: [implementation](../../experiments/B01/dewitt_family.py), [pre-registration](../../experiments/B01/ansatz.md), [exact recorded results](../../experiments/B01/result.json), [tests](../../tests/test_b01.py), [independent proof and source audit](../../experiments/B01/rederivation.md). The original results record their generating source commit and command; they are retained unchanged. Run the current checks with `uv run --no-sync pytest tests/test_b01.py -q`. These are exact algebraic results and tests, not a Lean proof or physical validation.

### B02 — Shiab typing, dressing, and closure in a real adjoint algebra

- **Provenance / evidence / scope:** `[GU-orig]` displayed operator (9.3); `[GU-recon]` its pinned input, invariant forms, bracket readings and Einstein target; `[ext]` the (9,5) signature extension. `verified:experiments/B02/response.py`, `verified:experiments/B02/result.json`, `verified:experiments/B02/proofs.md`, `verified:tests/test_shiab.py`, `verified:tests/test_dressing.py`; `identity` for the algebraic-curvature response in (3,1), (7,7), (9,5), degree, real-form closure, dressed covariance and Spin₀ equivariance as specified below; `sampled` for Cayley regression and open dressing data.
- **Draft says:** `[GU-orig]` GU (8.1) and (8.7), pp. 41–42, dress invariant adjoint-valued forms by conjugation. Equations (9.2)–(9.3), p. 43, give an Ω²(ad) → Ω¹³(ad) candidate, label its terms Ricci-like and Ricci-scalar-like, and state Weyl annihilation. Appendix (12.26)–(12.27), pp. 65–66, defines the commutator and i·anticommutator. The [transcription](../../experiments/B02/transcription.md) records the unresolved Φ choice, norm and relative scale, and the unavailable preferred operator in section 8.2 / footnote 10.
- **Status / gap:** **Literal CCC: `obstructed-within-literal` as an Einstein contraction, `identity`.** On algebraic curvature, its inner commutator vanishes by pair symmetry with the pinned index-raising factors. Thus the −½ term is zero and the pinned response is −E_T(Ric), κ = 0 for nonzero T. Vanishing of that term survives global rescalings, either standard Hodge convention and either global generator normalization; a nonzero scale is required to retain the nonzero-response gate. It is not invariant under arbitrary changes to the ξ index convention. This does not obstruct every reconstructed reading of the displayed candidate.
- **Reconstructed verdicts:** **`holds-Einstein`**, under N-a, the pinned star, and nonzero T=(α,β): CAA iff γ=1 (any δ); CAC iff β=sα and sδ=1, s=±1 (any γ). H0 fixes Φ¹=F, Φ²=B and has CAA as its unique passing bracket assignment. These are algebraic statements within the [amended ansatz](../../experiments/B02/ansatz.md), not a physical selection of Φ or a verdict on the lost preferred operator.
- **Remaining gap:** The source does not choose the unit/sign or norm of Φ. The trace-norm exclusion, if imposed on both forms, requires α²≠β² and γ²≠δ²; it removes the chiral CAC family and restricts CAA Einstein to δ≠±1. It filters admissible forms without changing their computed κ. General gauge curvature need not have pair symmetry or the algebraic first Bianchi identity, so the curvature classification does not extend to it. NP section 3.1, pp. 5–6, concerns the earlier real-Clifford identification; checking this April candidate's real form does not settle the physical objections in B04/B05.
- **Dependencies:** B01, B10; informs B04, B05, B07, B08. **Importance / next-check cost:** H / M.
- **Next check:** Use the explicit conventions in a stated general-gauge-curvature or variational problem, retaining the dependence on the metric and dressed Φ. Do not use undressed Weyl annihilation alone as an Einstein gate or infer full-gauge behavior from Levi-Civita inputs.

**Response and normalization.** Write Φ¹=αF+βF′, Φ²=γB+δB′, T′=(β,α), and use the branch's own embedding E_T. The [checker](../../experiments/B02/response.py) verifies

`*Shiab(xi(R)) = -[m0=C] E_T(Ric) + (S/2)([m1m2=AA] gamma E_T(g) + [m1m2=AC] delta E_T'(g))`.

For T≠0, the first-bracket-C modes have c=r_T=−1. CCC/CCA have κ=0. CAA has κ=γ/2 and fails gate 5a when γ=2/n because its scalar response vanishes. CAC has κ=0 for δ=0; for δ≠0 it fits the same embedding only on β=sα, with κ=sδ/2, and fails 5a at sδ=2/n. Nonchiral CAC with δ≠0 has no scalar ratio in E_T. Every first-bracket-A mode has r_T=0 and fails 5a; κ is undefined. T=0 is the zero embedding/operator and fails the nonzero gate; its response ratios are not identifiable.

N-b is available only with inner A, δ=0 and γ≠0: the whole inner contraction `(S/2)(i gamma I - delta C)` can then be rescaled to `iS I`. Under the pinned star this gives CAA κ=1 and CAC κ=0, with no Einstein branch. Under the alternative star `*' = (-1)^{k(n-k)} *`, the operator is the pinned one with Φ² negated; the final read-off star also reverses c. Thus CAA Einstein moves to γ=−1 and CAC to sδ=−1. Using the unit spin generator `sigma_ab=(1/2)Gamma_aGamma_b` instead gives ordinary CAA κ=1/4, still passing 5a at n=14. These coefficient claims use the three verified odd-q signatures; even-q observations remain sampled. The [reconciliation](../../experiments/B02/README.md) gives the branch discussion.

**Evidence.** [result.json](../../experiments/B02/result.json) records producing source commit `d66cd8f7c3ac4f2f5b0aaa7eb0f5c9dc831cac6b`: ranks 20/20 at n=4 and 3185/3185 at n=14, with 2640, 267120 and 267120 response cases respectively and positive nonzero-output counts. It records no κ field: the classification follows algebraically from the verified formula. The [proofs](../../experiments/B02/proofs.md) extend the rational spanning checks to real algebraic curvature and real Φ parameters by linearity in R and Φ¹ and affinity in Φ². They also establish degree, real-form closure, dressed covariance and Spin₀ equivariance by composition; no Pin/O claim is made. [Small response controls](../../tests/test_b02_response.py), [operator tests](../../tests/test_shiab.py) and [dressing tests](../../tests/test_dressing.py) exercise these paths. Reproduce the response evidence with `uv run python -m experiments.B02.run`; run the tests with `uv run pytest -q`.

**Open dressing data (`sampled`).** For F,B with CCC/CAA, two odd Cayley dressings of one undressed Weyl control give nonzero outputs in all three signatures: four terms for the vector dressing and two for the triple-blade dressing. The [recorded data](../../experiments/B02/result.json) refute universal annihilation of that fixed geometric Weyl subspace under arbitrary dressings. They do not classify all dressings or contradict covariance, which transports the Weyl subspace along with the input. No Lean proof or physical validation is claimed.

**Working type dictionary.** GU section 3.6, equations (3.31)–(3.36), p. 24, supplies the finite structure group and bundles. NP uses different `Ad(P)` notation for its Lie-algebra bundle; here `ad P` always denotes the Lie-algebra bundle, and `Ad P` the group bundle.

| Symbol | Working type | Source / unresolved point |
|---|---|---|
| `H_fin` | `U(64,64)` in the April setup | GU section 3.6; not NP's compact `U(128)` |
| `H_gauge` | Sections of the associated group bundle | Distinct from the finite group and from the horizontal bundle also called H |
| `A0` | Distinguished reference connection | Depends on the observation metric via the Zorro construction |
| `epsilon` | Gauge-group section | Acts by conjugation on coefficient fibers |
| `varpi` | `Omega^1(Y,ad P)` | Displacement from the reference connection |
| `T` | `varpi - epsilon^-1 d_A0 epsilon` | Augmented torsion, not an assumed ordinary 3-form |
| `F` | `Omega^2(Y,ad P)` | Enlarged connection curvature; distinguish its geometric subspace |
| `Phi_r` | Adjoint-valued r-form with specified Clifford origin | Which intertwiner, phase and normalization? |
| `Shiab_epsilon` | `Omega^2(Y,ad P) -> Omega^13(Y,ad P)` | GU (9.2), with candidate (9.3) |
| `star` | `Omega^k -> Omega^(14-k)` on the form factor | Depends on oriented pseudo-metric, conventions, and observation |

For a fixed spacetime metric, the desired dressed covariance has the form

`Shiab_(epsilon h)(h^-1 eta h) = h^-1 Shiab_epsilon(eta) h`.

This is now an **identity** for the implemented dressed operator, by the [conjugation proof](../../experiments/B02/proofs.md#test-3a-dressed-covariance), with exact Cayley regressions in all three signatures. Here ε,h are in the internal gauge group and the metric/Hodge star is fixed. Internal gauge transformations act on coefficient fibers; the geometric Spin action and the enlarged internal gauge action remain distinct. Dressed covariance does not make the undressed contraction invariant under the full enlarged group. The adjoint-valued bosonic map is also distinct from the spinor-valued fermionic maps of section 9.3.

### B03 — Branching is not yet a three-generation dynamical explanation

- **Tags / evidence:** `[GU-orig]`, `[GU-recon]`, `[ext]`; branching claims located, not independently computed.
- **Draft says:** GU (11.1)–(11.6), pp. 50–52, and (12.20)–(12.22), pp. 61–63, use spinor/vector-spinor branching and an effective third generation.
- **Gap / source:** The fiber representation decomposition, the field's on-shell degrees of freedom, and the light chiral spectrum are separate questions. The gamma-traceless vector-spinor sector cannot be dropped when counting generations. Nor can mirror sectors be declared absent merely because a block decouples in a special background. This is our audit question about GU, not an extra objection attributed to NP.
- **Counterargument / repair:** `[ext]` Verify complexified branching first, then separately impose the chosen real structures and Lorentz interpretation. `[ext]` Preserve every mirror/exotic sector and test a concrete mass/constraint mechanism that leaves the desired light multiplets. Such a mechanism is additional dynamics unless already derived from the action.
- **Dependencies:** A02, B01, B09; feeds B05 and B11. **Importance / cost:** H / M.
- **Falsifiable next check:** Reproduce the restriction of both chiral spinors and gamma-traceless vector-spinors to the specified 4+10 subgroup, with dimensions and chirality tracked. Compare every multiplicity with GU (11.6)/(12.22). A character mismatch refutes that branching claim; matching characters do not establish light generations or mass hierarchies.

### B04 — Complex notation, real fields, and physical unitarity are distinct

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; physical consistency unresolved.
- **Draft says:** GU section 3.6, p. 24, uses a noncompact pseudo-unitary group; section 9.1, pp. 43–45, proposes a real action.
- **Gap / source:** NP section 3.1, p. 6, raises nonunitarity/unbounded-energy consequences of complexifying the connections. One must determine whether that enlargement actually occurs in the candidate under review. A real-valued action or an invariant indefinite pairing is not a positive physical Hilbert-space norm. Conversely, writing factors of `i` is not itself a ghost proof. W concerns 2+1D Chern–Simons quantization, so transporting any conclusion to GU requires checking its hypotheses; its abstract alone settles neither side.
- **Counterargument / repair:** `[ext]` Specify a real integration contour/reality involution preserved by gauge transformations and evolution. `[ext]` Identify constraints and test the kinetic form on physical modes, or explicitly propose a reduction to a healthy sector. A projection must be dynamically consistent, not just delete negative directions on paper. **No repair is established.**
- **Dependencies:** B02, B07, B09. **Importance / cost:** H / M.
- **Falsifiable next check:** Linearize one specified real action around a solution, remove gauge/constraint directions, and inspect physical kinetic signs and the evolution operator. A propagating negative-norm/negative-energy mode falsifies that background/realization.

### B05 — Gauged chirality, anomaly cancellation, and the Shiab compatibility tradeoff

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; no anomaly coefficient computed.
- **Draft says:** GU sections 3.6 and 9.3, pp. 24 and 46–47, specify enlarged gauge and fermionic ingredients; section 12.9, pp. 60–62, discusses effective chirality.
- **Gap / source:** NP section 3.2, pp. 6–7, objects to gauged axial transformations together with the central `U(1)`, and argues that shrinking to Spin destroys its full-adjoint/exterior identification. The objection is genuinely about 14D, not merely a 4D Pati–Salam trace. Its exact transfer to the later indefinite real form and mixed fermionic operator must be established. “Fundamentally non-chiral” does not automatically cure an anomalous gauged axial symmetry. Conversely, NP's dimensional argument addresses its identification-based construction, not every conceivable Spin-equivariant operator.
- **Counterargument / repair:** `[ext]` First identify which transformations actually preserve the kinetic operator, including its Clifford action and dressed fields. `[ext]` Test anomaly cancellation by a fully specified spectrum/mechanism, or a restricted gauge group with a newly defined Shiab construction. Adding fields, inflow, or counterterms creates a new proposal and must satisfy its own conditions. **No repair proposed at a sufficient level to assert cancellation.**
- **Dependencies:** B02, B03, B04, B09. **Importance / cost:** H / M for the inventory; full calculation H.
- **Falsifiable next check:** Give the generators, their action on every fermion sector, and the kinetic symbol; reject any claimed gauge generator that is not a classical symmetry. For genuine chiral gauge symmetries, compute the applicable 14D anomaly polynomial/descent and the separate 4D effective anomaly data. An uncancelled gauged variation rejects that realization. Do not import the ordinary Weyl-fermion formula blindly for the constrained vector-spinor operator.

### B06 — What kind of supersymmetry is claimed, and what higher-spin fields follow?

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; algebra and applicability of no-go assumptions unresolved.
- **Draft says:** GU section 5.5, pp. 33–34, and section 12.8, p. 60, discuss fermionic extensions of affine connection space, distinguished from spacetime supersymmetry.
- **Gap / source:** NP section 3.3, pp. 7–8, gives three linked objections: high-dimensional supersymmetry forces higher spin; interacting higher spin requires further fields under the cited assumptions; their gauge symmetries exceed a finite `U(128)` structure group. An infinite-dimensional group of **local gauge transformations** is not automatically the infinite tower of independent higher-spin species at issue. But standard super-Poincare representation bounds cannot be applied to an unspecified affine-field-space superalgebra solely because both use the word supersymmetry.
- **Counterargument / repair:** `[ext]` Construct the proposed odd bracket into connection translations and test closure and action invariance; state exactly which spacetime assumptions it changes. `[ext]` Alternatively drop the supersymmetry claim and study a purely classical boson/fermion model. If ordinary interacting high-dimensional spacetime supersymmetry is required, **no complete higher-spin repair is proposed** in this register.
- **Dependencies:** B03, B07, B08, B09. **Importance / cost:** H / M.
- **Falsifiable next check:** Write the even/odd brackets, calculate their graded Jacobi identities and action variation, and identify whether translations are spacetime or field-space translations. A failed identity rejects that algebra; a changed algebra requires a fresh theorem-applicability analysis, not an automatic exemption from consistency tests.

### B07 — Variational equations and recovery of Einstein/Yang–Mills/Dirac dynamics

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; equations available, equivalence not established.
- **Draft says:** GU section 9, pp. 43–47, gives first/second-order bosonic and fermionic expressions; section 12.5, pp. 57–58, discusses paired equations.
- **Gap / source:** NP section 3.4, p. 8, requests the missing unification computations. The April draft supplies more formulas, but notation resembling familiar equations is weaker than deriving them. Varying an action must track the dependence of `A0`, Hodge star, pairings, and Shiab tensors on the observation metric. Squaring a first-order equation can introduce additional solutions and is not an equivalence theorem.
- **Counterargument / repair:** `[ext]` Freeze a background metric for the first restricted check and label that assumption. Then restore its variation and boundary terms. `[ext]` Prove a precise implication between the first- and second-order systems before claiming equivalence or a Standard Model limit.
- **Dependencies:** B02, B04, B08, B09. **Importance / cost:** H / M.
- **Falsifiable next check:** Independently vary the stated bosonic action in one allowed field direction with compact support, and compare to (9.7)/(9.12). An extra surviving term invalidates the advertised equality under those assumptions. Separate checks must then address the Einstein, Yang–Mills, and Dirac limits.

### B08 — Exactness, signs, and the deformation-complex claim

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; no differential identity verified.
- **Draft says:** GU section 10, pp. 47–49, proposes a deformation complex and flags possible inconsistencies in (10.10).
- **Gap / source:** NP section 3.4, p. 8, singles out exact forms and sign computations; its appendix, p. 10, points to lecture times 1:45:40 and 2:03:32. These particular lecture claims have not been rewatched in this handoff and cannot safely be identified with a specific April equation. Independently, an operator diagram needs valid types and zero composition on the claimed solution locus. Being closed is weaker than being globally exact.
- **Counterargument / repair:** `[ext]` Fix the orientation, signature, Hodge-square, graded-bracket, integration-by-parts and adjoint conventions before checking signs. `[ext]` Supply a primitive for the relevant form, or state a local/contractible-domain hypothesis; preserve the global cohomological question.
- **Dependencies:** B01, B02, B07, B10. **Importance / cost:** H / M.
- **Falsifiable next check:** Locate the exact lecture assertion using NP's timestamps and compare it with the later draft; separately compute `delta_2 delta_1` from (10.7)–(10.9) on a stated solution. A nonzero residual or a nonzero period of a purported exact form rejects that claim in its specified domain.

### B09 — Pullback of fields versus closed four-dimensional dynamics

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; reduction prescription unresolved.
- **Draft says:** GU sections 3.6, 11 and 12.6, pp. 24–26, 49 and 58–59, discuss observation/pullback and jets.
- **Gap / source:** NP section 3.4, p. 8, asks how a 14D theory becomes applicable in 4D. Pulling back coefficient bundles is well-defined, but two ambient fields can agree on a slice and have different normal derivatives. Thus restricted values alone need not determine their dynamics. Direct pullback of a degree-13 differential form to a four-manifold vanishes; it cannot itself be the desired four-dimensional field equation. An operator/restriction rule, constraints, or reduction procedure is needed. The noncompact metric fibers also make naive fiber integration a separate problem.
- **Counterargument / repair:** `[ext]` Specify jet data or a closed consistent truncation, using Hodge/contraction and observation in a declared order. `[ext]` If integrating fibers instead, define measure, boundary behavior, and which modes survive. These alternatives must not be silently interchanged.
- **Dependencies:** B01, B02, B07, B10. **Importance / cost:** H / M.
- **Falsifiable next check:** Find two admissible ambient configurations with identical pulled-back fields but different proposed 4D evolution. Such a pair disproves closure on that field set; a repair must add data or constraints sufficient to exclude it.

### B10 — Topological spinor claims, metric dependence, and global bundle data

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; local construction plausible, global/naturality assertions unproved here.
- **Draft says:** GU sections 3.2–3.4, pp. 19–22, distinguish chimeric and metric spinors; section 1, p. 4, assumes a spin structure on X.
- **Gap / source:** NP section 2.1 and footnotes a–b, p. 3, question the metric-independence claim and note the spin obstruction. Distinguish a spinor bundle for the rank-14 bundle `C -> Y` from a spinor bundle of the tangent bundle of the **28-dimensional total space** C. The former is the relevant charitable reading; silently changing base spaces would create a false objection. Transferring spinors and Dirac operators to `TY` still needs the stated identification, connections, and compatible spin lifts. The connection-to-metric lemma alone is not a uniqueness or physical-selection theorem.
- **Counterargument / repair:** `[ext]` Formalize a universal metric-parameterized spinor family and its observation-dependent identification. `[ext]` State orientability, time-orientation/component, spin-lift, and gluing assumptions explicitly; prove any asserted canonical maps rather than treating all splittings as canonical.
- **Dependencies:** B01; supports B02, B03, B09. **Importance / cost:** M / M.
- **Falsifiable next check:** Construct transition functions and compatible lifts for C and TY under the declared hypotheses, and vary the chosen horizontal splitting. Failure to intertwine Clifford multiplication/connection under the claimed natural identification disproves that naturality assertion, without disproving existence of some spinor bundle.

### B11 — A geometric scalar must still reproduce Higgs quantum numbers and dynamics

- **Tags / evidence:** `[GU-orig]`, `[GU-recon]`, `[ext]`; no Higgs identification or potential established.
- **Draft says:** GU section 9.3, p. 46, associates subfields with Higgs-like masses/Yukawa couplings; section 12.9, p. 62, links a scalar gauge component and masses.
- **Gap / source:** O's extrinsic-curvature target (A05) is not supplied by those statements. Lorentz scalar behavior alone does not imply a complex electroweak doublet, the right hypercharge, a stable potential, or correct Yukawa couplings. A claimed mass-generating scalar and a Standard Model Higgs field must be distinguished.
- **Counterargument / repair:** `[ext]` Identify a candidate in the actual bosonic branching, derive its kinetic and interaction terms, and check its vacuum and couplings. `[ext]` An extrinsic-curvature construction may be explored as a separate geometric extension after a map to the gauge representation is given. **No completed repair proposed.**
- **Dependencies:** B03, B07, B09. **Importance / cost:** H / H.
- **Falsifiable next check:** Determine the proposed scalar's representation under the surviving electroweak group. Wrong charges or no doublet exclude that candidate before any potential fitting.

### B12 — Quantum completion remains outside the present deliverable

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[ext]`; open, no completion proposed.
- **Draft says:** GU section 9.3, p. 46, discusses a future fermionic functional integral.
- **Gap / source:** NP introduction, p. 1, explicitly evaluates a pre-quantum presentation. A classical identity, exact matrix check, or Lean theorem about it cannot by itself define a quantum measure, renormalized dynamics, a physical state space, or predictions.
- **Counterargument / repair:** `[ext]` Treat a well-defined classical sector as a legitimate intermediate research goal with an explicit quantum-obligation list. **No repair proposed** for a full quantum completion in this report.
- **Dependencies:** B04–B09, especially the actual degrees of freedom and gauge symmetries. **Importance / cost:** H / H.
- **Falsifiable next check:** For any claimed quantum candidate, specify its quadratic physical propagator and actual gauge symmetry, then test norm/energy and anomalous Ward identities. Failure rejects that candidate; passing does not establish a full quantum theory.

## Nguyen–Polya coverage and version crosswalk

This table covers the substantive mathematical/physical objections, including technical footnotes. Commentary about publicity, credit, and scientific discourse is not a mathematical gap and receives no repair proposal.

| NP location | Objection or prerequisite | Register entry | Treatment of the later draft / repair status |
|---|---|---|---|
| Introduction, p. 1 | Pre-quantum status | B12 | Classical intermediate goal; no quantum completion proposed |
| Section 2.1, p. 3 | Connection-to-metric lemma's significance | B10, B01 | Separate existence from canonical selection |
| Footnote a, p. 3 | Alleged metric-independent spinor construction | B10 | Distinguish C-over-Y spinors from spinors of total space C; audit transfer to TY |
| Footnote b, p. 3 | Existence of spin structure | B10 | State and verify global hypotheses |
| Section 3.1, pp. 5–6 | Real Clifford/adjoint identification | B02 | April draft includes complexification; test real closure and the dressed map |
| Section 3.1, p. 6 | Nonunitarity or unbounded energy | B04 | Separate representation from field-space complexification; no established repair |
| Section 3.2, pp. 6–7 | Gauged axial symmetry and central U(1) anomaly | B05 | Verify actual symmetry/spectrum of the later operator; no cancellation asserted |
| Section 3.2, p. 7 | Restricting to Spin breaks the identification | B05, B02 | Restricted-group operator is a new candidate, not automatically impossible or successful |
| Section 3.3 point 1, p. 7 | High-D spacetime supersymmetry requires higher spin | B06 | State the algebra before transferring the representation bound |
| Section 3.3 point 2, p. 7 | Interacting higher-spin tower | B06 | Audit hypotheses; no completed tower supplied |
| Section 3.3 point 3, pp. 7–8 | Gauge structure for the extra higher-spin fields | B06 | Distinguish local gauge-function dimension from species/content |
| Section 3.4, p. 8; appendix notes 20–22 | Einstein/Yang–Mills/Dirac recovery omitted | B07 | Later formulas need independent derivations and limit checks |
| Section 3.4, p. 8; appendix note 23 | Claimed exact forms | B08 | Timestamp identified; precise lecture claim not yet transcribed |
| Section 3.4, p. 8; appendix note 24 | Unexplained sign calculations | B08 | Timestamp identified; convention and formula audit still required |
| Section 3.4, p. 8; appendix note 25 | 14D to 4D recovery | B09 | Pullbacks/jets are discussed later; closed effective dynamics still needs a test |

## What would constitute progress

The next checks carry B01's reconciled conventions and B02's verified algebraic operator into downstream questions, beginning with B03's full branching inventory. A successful check establishes only its stated claim and assumptions. A failed repair stays in the register with the failed condition and evidence; it does not become a global impossibility result by repetition. No work in this report executes the implementation steps of overview.md.
