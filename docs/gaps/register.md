# GU gap register

Research snapshot: 2026-10-14; B01/A01, B02 and B03 updated 2026-10-15. B01 has an exact fibrewise reconstruction and a base-mirror finding. B02 has an exact algebraic-curvature response: the literal CCC reading is obstructed as an Einstein contraction within the pinned ansatz, while specified reconstructed readings pass. B02 also has a merged, partial [Lean formalization](../../lean/COVERAGE.md); its full closed form and numerical rank computation are not formally certified. B03 has exact branching and reality data within its pinned ansatz; light generations remain unresolved. No physical validation is claimed.

## Priorities

Cost is the effort for the **next check**, not for resolving the whole research question. Importance concerns the proposed theory; H/M/L mean high/medium/low. Dependencies identify shared specifications, not a requirement to solve every foundational problem before exploring a toy model.

| Priority | Entry | Question | Importance | Next-check cost | Immediate deliverable |
|---|---|---|---|---|---|
| 1 | B01 | Signature as a function of the vertical trace coefficient and chimeric metric signs | H | L | Carry the reconciled conventions and F1 into both signature branches |
| 2 | B02 | Shiab response beyond the checked algebraic-curvature ansatz | H | M | Carry the verified convention map into general gauge curvature and dynamics |
| 3 | B03 | Spinor/vector-spinor branching and the claimed third generation | H | M | A specified mass/constraint mechanism tested against the verified full inventory |
| 4 | B05 | Actual gauged symmetry and anomalies in 14D and 4D | H | M | Fully specified covariance branch after the completed specification stage; resolve the tilted-action sign conflict |
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

**Open dressing data (`sampled`).** For F,B with CCC/CAA, two odd Cayley dressings of one undressed Weyl control give nonzero outputs in all three signatures: four terms for the vector dressing and two for the triple-blade dressing. The [recorded data](../../experiments/B02/result.json) refute universal annihilation of that fixed geometric Weyl subspace under arbitrary dressings. They do not classify all dressings or contradict covariance, which transports the Weyl subspace along with the input. The merged [Lean formalization](../../lean/COVERAGE.md), described in the [B02 formal check](../../experiments/B02/README.md#formal-check-lean-4-lean), proves selected sparse-model identities and structural statements under explicit hypotheses. It does not certify the full closed form or the 3185-row computation; the [theorem table](../../lean/THEOREMS.md) records its boundaries. No physical validation is claimed.

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

- **Provenance / evidence / scope:** `[GU-orig]` the transcribed identities and tables; `[GU-recon]` the chirality dictionary and SM embedding E; `[ext]` the (9,5) splits and mirror inventory. `verified:experiments/B03/result.json`, `verified:experiments/B03/rederivation.md`, `verified:tests/test_reps.py`, `verified:tests/test_rarita.py`, `verified:tests/test_b03.py`; `identity` for the finite characters and the explicit matrix checks within the [ansatz](../../experiments/B03/ansatz.md). The [independent re-derivation](../../experiments/B03/rederivation.md) uses fresh direct LiE restrictions and separately constructed Pauli matrices.
- **Draft says:** GU (11.1)–(11.6), pp. 50–52, and (12.20)–(12.22), pp. 61–63, use spinor/vector-spinor branching and an effective third generation.
- **Status:** **Branching identities hold within the pinned dictionary; generation dynamics unresolved.** The full-module forms of (11.1), (11.2), (11.3)/(12.22) hold independently of the draft's sign labels. Both (12.20) halves and all six p.51 module entries plus four whole-fibre comparisons hold under the dictionary, including **144+=Hbar, 144-=H**, with H=omega1+omega5 of D5. The [recorded tables](../../experiments/B03/result.json) give p.52 left=16, p.52 cousin=16bar, and p.53=Hbar under E. The 25 printed p.53 rows sum to 23 terms of total dimension 144. E and the flipped-charge control E' agree on all four complete D5 characters tested.
- **Reality and inventory:** S+ restricts to (L,16)+(R,16bar); V tensor S±=RS±+S∓, with RS± of dimension 832. The full nu+zeta fibre has complex dimension **1920**: each L/R tensor 16/16bar block has multiplicity 3; each six-dimensional Lorentz tensor 16/16bar and L/R tensor H/Hbar block has multiplicity 1. The defined complex-fibre diagnostic chi(lambda)=mult(L,lambda)−mult(R,lambda) is zero for all four D5 parents; it excludes the six-dimensional Lorentz carriers and is not a spectrum or anomaly index. J exchanges conjugate L/R partners in all three 14D splits. J²=+1 in (7,7) permits a Majorana-Weyl condition, relating conjugate coefficients; J²=−1 in (9,5) admits no nonzero J-fixed vector on a single copy. These reality facts do not delete a block or establish decoupling. Matrix characters concern the complexified representation; the recorded real-form diagnostics are J and C=±Pi.
- **Gap / source:** The fibre decomposition, on-shell degrees of freedom and light chiral spectrum remain separate questions. (12.22) locates an imposter candidate in the F-type spinor tensor 16 sector of RS; p.53 names imposter rows in the Z-type Hbar sector. Each candidate contains one complete SM-generation pattern per ambient chirality, but containment and repeated quantum numbers do not allocate a physical generation. Neither the third-family claim, the dashed-line interpretation, VEV decoupling, dark sectors nor (12.21) is established by B03. This is our audit question about GU, not an extra objection attributed to NP.
- **Counterargument / repair:** `[ext]` Retain every verified mirror/exotic carrier and specify an operator, background and mass/constraint mechanism that selects light multiplets. Such a mechanism is additional dynamics unless derived from the proposed action. The SU(5)-based E check does not verify the distinct Pati-Salam/U(3)×U(2) reduction route in section 11.4.
- **Dependencies:** A02, B01, B09; feeds B05 and B11. **Importance / cost:** H / M.
- **Falsifiable next check:** On one specified background, restrict the proposed fermion operator to this complete inventory, impose the stated reality and constraint conditions, and compute which paired sectors acquire mass or remain in its physical kernel. Failure to obtain the claimed light chiral multiplets refutes that mechanism; a successful branching identity alone does not pass this gate. The [reconciliation](../../experiments/B03/README.md) separates the representation verdicts from these dynamical claims.

### B04 — Complex notation, real fields, and physical unitarity are distinct

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; physical consistency unresolved.
- **Draft says:** GU section 3.6, p. 24, uses a noncompact pseudo-unitary group; section 9.1, pp. 43–45, proposes a real action.
- **Gap / source:** NP section 3.1, p. 6, raises nonunitarity/unbounded-energy consequences of complexifying the connections. One must determine whether that enlargement actually occurs in the candidate under review. A real-valued action or an invariant indefinite pairing is not a positive physical Hilbert-space norm. Conversely, writing factors of `i` is not itself a ghost proof. W concerns 2+1D Chern–Simons quantization, so transporting any conclusion to GU requires checking its hypotheses; its abstract alone settles neither side.
- **Counterargument / repair:** `[ext]` Specify a real integration contour/reality involution preserved by gauge transformations and evolution. `[ext]` Identify constraints and test the kinetic form on physical modes, or explicitly propose a reduction to a healthy sector. A projection must be dynamically consistent, not just delete negative directions on paper. **No repair is established.**
- **Dependencies:** B02, B07, B09. **Importance / cost:** H / M.
- **Falsifiable next check:** Linearize one specified real action around a solution, remove gauge/constraint directions, and inspect physical kinetic signs and the evolution operator. A propagating negative-norm/negative-energy mode falsifies that background/realization.

### B05 — Gauged chirality, anomaly cancellation, and the Shiab compatibility tradeoff

- **Provenance / evidence / scope:** `[GU-orig]`, `[GU-recon]`, `[lit]`, `[ext]`; `verified:experiments/B05/pairing.py`, `verified:tests/test_b05.py`, `verified:experiments/B05/result.json`. Scope: `identity` for the exact candidate-pairing algebra and toy variation controls; finite bookkeeping over explicitly enumerated model readings for the survey. Producing code `eb77457`, result `5fb4f4a`, reviewed specification `b133623`. **No gauge-symmetry, anomaly, unitarity or reality verdict about GU; no anomaly coefficient computed.**
- **Status / source:** Specification stage complete; the physical question remains unresolved. The [transcription](../../experiments/B05/transcription.md) and [typed operator](../../experiments/B05/source_operator.py) record (9.16), p. 46: a 4x4 matrix with 12 nonzero entries and 18 signed summands. The [README](../../experiments/B05/README.md) and [specification sheet](../../experiments/B05/spec.md) distinguish located source definitions, reconstruction branches and missing input. The draft supplies partial fermion content, but the inspected pages do not fix all fermion laws, pairings, adjoints or spinor-valued Shiab actions needed for covariance.
- **Established within the model:** The [result](../../experiments/B05/result.json) records 11,520 branches, 64 label projections and 360 degree projections: 32 label branches have no domain mismatch, zero have every summand nonzero, and four degree branches are consistent. All four use metric pairing and exterior d0. Legal zeros and undetermined labels remain distinct; these counts do not exclude unenumerated readings or establish an inconsistency of GU. The exact toy controls show that neither isometry-algebra membership nor a frozen commutator substitutes for the full bilinear variation.
- **New source finding — tilted-action sign conflict:** `[GU-orig]` (6.4), p. 36, and (6.13), p. 37, print `varpi' = h^-1 varpi h - h^-1 d0 h` with `epsilon' = epsilon h`. With `A = A0 + varpi` from (6.22), p. 39, and `T = varpi - epsilon^-1 d0 epsilon` from (7.3), p. 40, this gives `T' = h^-1 T h - 2 h^-1 d0 h`, not the claimed conjugation law. The ordinary right connection action (6.2), p. 36, uses the plus sign; the displayed proofs (6.20), p. 39, and (7.4), p. 40, switch to plus. Footnote 7, p. 36, warns of conflicting conventions. [Spec §1.2](../../experiments/B05/spec.md) records **(6.13-lit)** (literal minus) and **(6.13-rec)** (`[GU-recon]` plus-sign reconstruction); the latter restores these connection/torsion identities, without establishing that every surrounding identity is repaired. Scope: algebraic `identity` under the displayed definitions, with the local central-phase counterexample given in the spec; this is a source-convention finding, not a gauge/anomaly verdict.
- **Lean sign check:** Merge `a134286`, [B05Sign](../../lean/B05Sign/), the [B05Sign coverage section](../../lean/COVERAGE.md#b05-tilted-action-sign-check) and [validation](../../lean/ValidationB05Sign.md) formalize both signs: the literal minus leaves residual −2h⁻¹Dh in (6.20)'s first connection and (7.4)'s torsion; the reconstructed plus leaves a residual in (6.14)'s projection. No single sign of (6.4)/(6.13) preserves all the listed printed formulas. Scope: a directional differential-ring model over an arbitrary possibly noncommutative ring, replacing one-forms by the coefficient algebra; not a global geometric repair or a Lean check of B07.
- **NP transfer / remaining gap:** The [NP object map](../../experiments/B05/np_objection.md) separates NP §3.2, pp. 6–7, on the earlier `U(128)` setup from the April `U(64,64)` operator. Its axial exponential is printed without an `i`; identifying it with C or iC needs a transfer assumption. Central coupling, constrained fermion content and a quantum measure remain needed. NP's Spin-restriction argument addresses its full-adjoint/exterior identification, not every conceivable Spin-equivariant operator. No cancellation mechanism or physically sufficient repair is established.
- **Dependencies:** B02, B03, B04, B09; B07 if an action is needed to pin the operator. **Importance / next-check cost:** H / M for a specified covariance branch; a full anomaly calculation remains H.
- **Next check — (a) executable now:** Use the [toy controls](../../tests/test_b05.py) to validate the variation criterion; they test the tool, not GU.
- **Next check — (b) conditional formal tests:** Following [README: What the covariance test needs](../../experiments/B05/README.md), take the **full** branch table, not a filtered survivor list. Before a binary verdict, specify every tested summand beyond `domain_mismatch`/`undetermined`, the barred law, coefficient and dressing variations, a definite spinor-valued Shiab map, the target (bilinear/density/action), and C's action on coefficient maps under signature labels. Constant parameters can still move coefficients. A frozen-K calculation is a stabilizer test; treating it as a necessary covariance condition requires an explicitly invariant background.
- **Next check — (c) insufficient data today:** Local tilted-gauge covariance needs the missing fermion/Shiab laws and a consistent choice for the (6.13) sign conflict; translation covariance needs its fermion law and the inputs in (b). An anomaly calculation additionally needs a reality branch, constrained fermion content and quantum measure. If the operator cannot be pinned without the action, proceed to [B07](#b07--variational-equations-and-recovery-of-einsteinyangmillsdirac-dynamics)'s one-direction variation. Any eventual rejection is of a specified realization, not all GU readings.

### B06 — What kind of supersymmetry is claimed, and what higher-spin fields follow?

- **Tags / evidence:** `[lit]`, `[GU-orig]`, `[GU-recon]`, `[ext]`; algebra and applicability of no-go assumptions unresolved.
- **Draft says:** GU section 5.5, pp. 33–34, and section 12.8, p. 60, discuss fermionic extensions of affine connection space, distinguished from spacetime supersymmetry.
- **Gap / source:** NP section 3.3, pp. 7–8, gives three linked objections: high-dimensional supersymmetry forces higher spin; interacting higher spin requires further fields under the cited assumptions; their gauge symmetries exceed a finite `U(128)` structure group. An infinite-dimensional group of **local gauge transformations** is not automatically the infinite tower of independent higher-spin species at issue. But standard super-Poincare representation bounds cannot be applied to an unspecified affine-field-space superalgebra solely because both use the word supersymmetry.
- **Counterargument / repair:** `[ext]` Construct the proposed odd bracket into connection translations and test closure and action invariance; state exactly which spacetime assumptions it changes. `[ext]` Alternatively drop the supersymmetry claim and study a purely classical boson/fermion model. If ordinary interacting high-dimensional spacetime supersymmetry is required, **no complete higher-spin repair is proposed** in this register.
- **Dependencies:** B03, B07, B08, B09. **Importance / cost:** H / M.
- **Falsifiable next check:** Write the even/odd brackets, calculate their graded Jacobi identities and action variation, and identify whether translations are spacetime or field-space translations. A failed identity rejects that algebra; a changed algebra requires a fresh theorem-applicability analysis, not an automatic exemption from consistency tests.

### B07 — Variational equations and recovery of Einstein/Yang–Mills/Dirac dynamics

- **Provenance / evidence / scope:** `[GU-orig]` (9.4)/(9.7) and (9.11)–(9.15); `[GU-recon]` reading V and the corrected second-order variation; `[ext]` the B07-U search space. `verified:experiments/B07/result.json`, `verified:experiments/B07/rederivation.md`, `verified:tests/test_b07.py`, `verified:experiments/B07/phase2/result.json`, `verified:experiments/B07/phase2/derivations.md`, `verified:experiments/B07/phase2/rederivation.md`, `verified:tests/test_b07_phase2.py`; `identity` for the exact 4D kernels and flat Fourier comparisons, `counterexample` for bounded 14D witnesses. The [Phase 1 README](../../experiments/B07/README.md), [transcription](../../experiments/B07/transcription.md) and [Phase 2 README](../../experiments/B07/phase2/README.md) pin the conventions and limits.
- **Status / source:** Both phases' results are recorded and independently re-derived; the Phase 2 README is audited. **Phase 1 P7 complete:** clean-clone re-run at `b60bbfc`: 365 tests passed, scientific payload identical to `c7229e9` excluding `seconds`/`source_commit`, and all eight seeded faults RED. **Phase 2 P7 pending.** V repairs (9.4)'s star scope by moving the κ term outside the star, uses the metric trace pairing and compact support, and varies only ϖ at fixed ε and metric. Phase 2 uses B = d, ε = 1 and constant coefficients; H5 removes a fixed dressing. The draft's claimed first variation is (9.7), pp. 44–45.
- **Phase 1 result under V:** The printed (9.7) is **not** the Euler–Lagrange equation of (9.4) for any nonzero member of B02's fixed-mode Shiab family in 4D, nor for the three named 14D branches (CCC literal, CAA Einstein, CAC chiral). The extra order-T¹ term is **½(L†−L)T**, with L = ⊚∘d_B and L† defined through the wedge integral (H2). Its principal-symbol condition C1 is necessary; a nonzero entry rejects the equality. At (3,1)/(1,3), **no nonzero operator** in any fixed-mode family passes C1 or C2 under N1/N2; the named branches have nonzero C1 witnesses at (7,7)/(9,5).
- **Phase 2 first-order result (B07-U, B07-M, B07-N0 executed):** At the two tested Lorentzian signatures (3,1) and (1,3), the unreduced space of real Spin-equivariant u(A)-preserving algebraic maps Ω²(u(A)) → Ω³(u(A)) has dimension 40, matching H12's character count block by block. It contains all 20 mixed-mode building blocks, whose span has dimension 16 with four zero relations. The unreduced C1 kernel has dimension 8: its Einstein response image has rank 2 with κ = ½, and six basis directions annihilate every algebraic curvature ξ(R). The block-span C1 kernel has dimension 2 and Einstein response rank 2; it contains E_OP with response 2E_F(Ric) − S·E_F(g). Thus L = L† with an Einstein response is attainable at order T¹, but **no nonzero operator in the entire C1 kernel passes C2 under N0, N1 or N2**. Among C1 survivors the obstruction is at order T². N0's C2 = −Tr(α∧⊚(T∧T)) is now executed, superseding Phase 1's record-only status. See the [exact results](../../experiments/B07/phase2/result.json) and [independent re-derivation](../../experiments/B07/phase2/rederivation.md).
- **Symmetrized operator (B07-S analysed):** H9–H10 give L† = d∘Xᵗ and, on the flat constant-coefficient model, L† = X♯∘d iff SO = 0. The SO kernels have dimensions 16 (unreduced) and 4 (block span); CAA and CAC have nonzero SO witnesses at all four signatures. Symmetrizing the existing quadratic action leaves its variation unchanged; when SO vanishes its operator is ½(X + X♯)∘d. H11 lifts C1 = 0 to L = L† on curved backgrounds only when X is parallel, the form connection is torsion-free, the trace is compatible, and boundary terms vanish. Spin-equivariance alone does not establish parallelism for an independent internal connection; see the [derivations](../../experiments/B07/phase2/derivations.md).
- **14D limits:** Phase 2's E_OP has exact nonzero C2 witnesses 8, −16/3 and −8 under N0, N1 and N2 respectively at both (7,7) and (9,5). No C1 witness was found in 19,200 checked entries at each signature; that is inconclusive, not a proof of C1 = 0. The 14D unreduced space remains unsearched; neither phase supplies a universal 14D classification.
- **Printed conflicts and second-order variation (H14 executed):** (9.4)'s line 1 and lines 2–4 are degree-inconsistent as printed; V repairs line 1. Line 1's κ₁/2 gives (9.7)'s κ coefficient, while line 4's κ₁ doubles it. For (9.11), the derived half-gradient is `d_A*⊚*⊚F_A + κ₁d_A*⊚*(∗T) + κ₁∗†⊚F_A + κ₁²∗†∗T`, using metric adjoints. Against `[GU-orig]` (9.13), term 1 matches, term 2 is missing ∗, term 3 has the wrong sign (∗† = −∗), and term 4 is (−1)^q κ₁²T, so its printed positive sign is right iff q is even. These `[GU-recon]` signs hold for even n under both Hodge conventions; all signatures at n = 4, 14 were checked for the star signs, with Fourier comparisons for CCC, CAA, CAC and E_OP at (3,1), (1,3), (2,2), (4,0). (9.12)'s Id must be replaced by ∗†.
- **Yang–Mills and swerve-zero scope (B07-YM executed):** At (3,1)/(1,3) under the pinned convention, none of CCC, CAA, CAC or E_OP has a kinetic principal symbol equal to a common nonzero multiple of ordinary Yang–Mills. The failed `⊚*⊚ ∝ Id` test is only a sufficient shortcut; the principal-symbol comparison supplies the verdict. This does not test (9.14)'s generalized packaging `D* = d_A*⊚*⊚`. Configurations with Υ = 0 are stationary for (9.11), but this proves neither equivalence with (9.15)/(9.7) nor minima or stability under the indefinite pairing.
- **Not shown / open readings:** No claim that no reading works. B07-G (ordinary products) remains outside B07-U until a reality-preserving completion is fixed; B07-Q (different pairings), B07-P2 (Palatini/BF or independent-field, one-leg or ε variations), B07-Bi (a specified conservation/Bianchi gate), and B07-X (non-parallel or ϖ-dependent Φ) remain open. So do the 14D universal space and non-flat lower-order terms beyond H11. Per-occurrence ⊚ (B07-Y), restricted variations (B07-R), and the unavailable lost operator (B07-O) remain separate readings; universal coverage is only within the stated real Spin-equivariant algebraic class. The [register additions](../../experiments/B07/phase2/derivations.md#register-additions) record the Phase 2 changes.
- **Fermionic scope:** The fermionic variation (9.16)–(9.22) was not computed; it is blocked on B05-Q's open pairing and adjoint conventions. H7 is a conditional ledger; no C1/C2 result transfers to its different spinor-valued ⊚. See the [B05 inputs](../../experiments/B05/README.md).
- **Dependencies:** B02, B04, B05, B08, B09. **Importance / next-check cost:** H / M.
- **Next checks:** The per-grade-pair C1 probe is **queued and open**: the grade support of the six zero-response directions is undecided, and they are not established operators of a non-gravitational sector. Complete Phase 2 P7. The Phase 2 plan's [After this plan](../superpowers/plans/2026-10-16-b07-phase2.md#after-this-plan) proposes separately planned `[ext]` changes to the cubic term or target, a gauge-invariant pairing change, or a Palatini/BF model with independent fields. Metric/ε variations and Einstein/Yang–Mills/Dirac limits remain separate checks; no first-/second-order equivalence is established.

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

The next checks carry B01's reconciled conventions, B02's verified algebraic operator and B03's full branching inventory into specified operator and dynamics questions. A successful check establishes only its stated claim and assumptions. A failed repair stays in the register with the failed condition and evidence; it does not become a global impossibility result by repetition. No work in this report executes the implementation steps of overview.md.
