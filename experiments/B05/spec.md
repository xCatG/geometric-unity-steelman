# B05 specification sheet: what a covariance test of the fermionic sector needs, and what the draft supplies

Author: Claude (Opus 5.5), 2026-10-15. Plan Task 5, rev 1.2 (`docs/superpowers/plans/2026-10-15-b05-transcription.md`).

**Revision 1.** This revision resolves Codex's Task 6 audit (9 findings, all accepted, and the two high-severity ones re-derived by Claude):
- **The source's own sign conflict.** (6.4)/(6.13) carry a minus sign on h⁻¹dh, while (6.2), (6.20) and (7.4) need a plus. This is now recorded as a conflict, §1.2.
- **§5 split three ways.** "Can run now" is now: toy controls; conditional formal tests that need a full specification; and branches that return insufficient data.
- **The frozen-commutator statement** is corrected.
- **The T1 dressing claim** is withdrawn.
- **The R1 preservation column** now separates three different conditions.
- **Absence claims** are bounded to the pages that were read.

**Sources:**
- `transcription.md` rev 1 (`4ea2237`), whose branch IDs B05-* are used below;
- `np_objection.md` (`59c62df`, Codex);
- `pairing.py` and `result.json` (Task 4).

**Scope.** This sheet poses the test. It gives no verdict on any gauge symmetry, anomaly, reality condition or unitarity question.

## 1. Generator families and their action on every field

The draft states actions only on bosonic objects. **No transformation law for ν, ζ, ν̄, ζ̄ was located** in the pages read (pp. 24, 31–47, 50–51, 58, 60–62, 65–66, 68). That is a bounded search, not an exhaustive reread of the whole draft. The only fermionic hint is the decoration ρ(ε) on the barred row and ρ(ε⁻¹) on the column in (9.16), and χ_{ε⁻¹} in (9.17).

### 1.1 Seedhe ℋ: (h, 0) at group level

- **ε.** (5.9) gives (ε, ϖ)·(h, 0) = (εh, h⁻¹ϖh). Right multiplication: ε ↦ εh.
- **ϖ.** ϖ ↦ Aut(h⁻¹, ϖ) = h⁻¹ϖh, from (5.9), p. 33.
- **A₀ / d₀.** Holding A₀ as a fixed origin (p. 36) is a reconstruction choice. It is not a claim that A₀ is invariant under the natural action A₀ ↦ A₀·h on connection space.
- **Fermions: not stated.** The branches are:
  - **T1, the decorated reading.** The fields are dressed by ε: ψ ≡ ρ(ε⁻¹)ψ₀ and ψ̄ ≡ ψ̄₀ρ(ε). The raw laws for ψ₀ and ψ̄₀ are **not** given, and the order of the factors matters. For example, with ψ₀ ↦ hψ₀ and ε ↦ εh, ψ′ = h⁻¹ε⁻¹hψ₀, which does not cancel for noncommuting ε and h. Codex's exact 2×2 counterexample has ε = diag(1, i) and h = K = [[0,1],[1,0]]. One reconstruction is raw fields inert under right multiplication, which gives the dressed laws ψ′ = h⁻¹ψ and ψ̄′ = ψ̄h. Invariance would then still need the matching K law. **The printed decorations alone promise no cancellation.** This also depends on B05-T′: does d₀ act on ψ₀ or on the dressed field?
  - **T2, the undecorated reading.** ψ ↦ ρ(h⁻¹)ψ and ψ̄ ↦ ψ̄ρ(h). That is consistent with the contragredient law, or with R1 when ρ(h) ∈ U(A).

### 1.2 Tedha ℋ_τ: τ_{A₀}(h) = (h, −h⁻¹(d_{A₀}h)), (6.4) p. 36

- **(ε, ϖ), as printed.** By (6.13), (ε, ϖ)·τ(h) = (εh, h⁻¹ϖh − h⁻¹(d_{A₀}h)).
- **A source sign conflict (Codex audit, Finding 1; re-derived by Claude).** The ordinary right connection action (6.2) carries **+**ε⁻¹(d_{A₀}ε). With A_ω = A₀ + ϖ (6.22), the literal (6.13) gives A_ω ↦ A₀ + h⁻¹ϖh − h⁻¹dh, which has the wrong sign for A_ω·h. For the torsion T = ϖ − ε⁻¹d_{A₀}ε, the product rule gives a = ε⁻¹dε ↦ h⁻¹ah + h⁻¹dh, so the literal law yields T′ = h⁻¹Th − 2h⁻¹dh, not h⁻¹Th.
- **The printed proofs switch sign.** The displayed calculations in (6.20) and (7.4) (pp. 39–40) change the sign of the h⁻¹dh term to plus partway through. Footnote 7 on p. 36 warns of "2 or more conflicting conventions in this section". A local central-phase jet shows the conflict: A₀ = 0, ε = h = 1, ϖ = 0 and h⁻¹dh = i give A′ = −i instead of +i, and T′ = −2i instead of 0.
- **Status: branched.**
  - **(6.13-lit)** is the minus sign as printed, under which the covariance identities (6.20) and (7.4) fail.
  - **(6.13-rec)** is a plus-sign reconstruction, under which A_ω ↦ A_ω·h and T ↦ h⁻¹Th hold.

  Neither replaces the printed formula. Whether one repair makes every surrounding identity consistent is not checked here.
- **Fermions: not stated.** The same branches as 1.1.
- **The obstacle.** (9.16) displays d₀ and ϖ in separate summands. Under (6.13-rec), covariance under ℋ_τ needs the inhomogeneous term of ϖ to combine with d₀, as in d_{A_ω} = d₀ + ϖ. That works only if the summands are read as blocks of d_{A_ω} (transcription, hand derivation 6, and B05-D′). Under (6.13-lit), even the bosonic laws are not mutually consistent.

### 1.3 Translations 𝒩: (1, ϖ′) at group level, (5.9)

- **Bosons.** ε ↦ ε and ϖ ↦ ϖ + ϖ′.
- **Lie-algebra level.** The generator is (0, ϖ′), acting by δϖ = ϖ′. Group- and algebra-level notation must not be mixed.
- **Fermions: not located.** p. 34 and (12.11) suggest that (ν, ζ) are "square roots" of 𝒩-translations, i.e. a superspace reading. No transformation law, such as δν ∝ ϖ′·(something), was located in the pages read. Branch **T3**: the fermions are inert under 𝒩. The alternative is supersymmetry-like transformations, which are unspecified.

### 1.4 Constant U(1)-type and chiral generators

These are acting on $ fibrewise, in the global (constant-parameter) form. For any nondegenerate Hermitian A with AC = −CA (`pairing.py`; hand derivations 1–3):

| Generator S | in 𝔲(A)? | Source location |
|---|---|---|
| central phase iI | yes | (8.6) p. 42: degree-0 class among the i-multiplied classes |
| axial phase iC | **no** | (8.6) omits degree 14 |
| chiral boost C (real) | yes | (8.5) p. 42: Λ¹⁴ ⊂ 𝔰𝔬(64,64) |

Membership in 𝔲(A) says only that the transformation preserves A. It is **not** the covariance test (§3). NP's axial transformation is printed as exp(γ̄θ) without an i (`np_objection.md`). Mapping it to C or to iC requires NP's Euclidean conventions and is recorded as a transfer assumption.

### 1.5 Spin(7,7) frame rotations

- **Where they sit.** They lie inside H = U(64,64) via ϱ_D (3.31). No separate frame-action law was located.
- **What changes for the fermions.** For local frame changes, the fields of form degree k transform both on the spinor index and on the form index. Because ∗, d₀ and ⊚ (through Φ_r, Definition 8.1) are metric-dependent, the covariance test must vary them too. ⊚ is built from Spin(7,7)-invariant Φ_r, so it is Spin(7,7)-equivariant on ad-valued forms. Its spinor extension is open (B05-Q).

## 1b. A is fixed in R1

In R1 the form A is a fixed algebraic matrix (δA = 0) under internal and axial transformations. It changes only through a connection or frame variation when the geometry on Y is varied.

If A is instead transformed by congruence so that it stays invariant, then δA = −(S†A + AS). Then δ(ψ†Aψ) = 0 for all S, which forces the contragredient law S̄ = −S. That is branch **Rc**, not R1.

## 2. Reality branches (B05-R)

| Branch | Statement | Status in the draft | Which §1 families preserve it |
|---|---|---|---|
| R0 | none: ν, ν̄, ζ, ζ̄ are four independent fields; a complex action; Berezinian integration | the closest to p. 46's "four distinct fields" | everything, since there is no constraint; but the barred law S̄ must then be **specified** separately |
| R1 | ψ̄ = ψ†A, with A one of the two candidate forms (`pairing.forms`; not printed, p. 24) | consistent with U(64,64) = U(A) (3.31) under the candidate identification | Three distinct conditions apply. (a) **Every** S preserves the R1 relation, provided A is fixed and the induced barred law δψ̄ = ψ̄S♯ is used. (b) Those S with S ∈ 𝔲(A) additionally have S♯ = −S, so the induced law equals the contragredient one. (c) Invariance of the kinetic bilinear is a separate test (§3). Under R1 the toy iC passes (c) without satisfying (b) |
| Rc | the contragredient law S̄ = −S (an independent bar transforming dually, or a congruence-transformed A, §1b) | not stated | all S, by construction of the pairing. The kinetic operator must still be covariant |
| R2 | Majorana at (7,7): ψ = Jψ with J = B∘conj, J² = +1 (B03, Lean-verified) | not stated | With J fixed, real-linear S commuting with J. An explicit choice of fixed subspace is required. J commutes with C and with the spin generators, so the real C and Spin(7,7) preserve it. The axial iC and the central phase do not: J(e^{iθ}ψ) = e^{−iθ}Jψ, so only θ ∈ πℤ (the ±1 subgroup) survives. Under R2 the continuous central U(1) is not a symmetry candidate. This is a conditional branch statement, not a claim about what GU removes |
| R2′ | (9,5): J² = −1, so Jψ = ψ has no nonzero solution. A reality condition needs a doubled (symplectic Majorana) space | not stated | requires new fields (a new proposal) |

## 3. The invariance criterion (pre-registered; executable controls in `tests/test_b05.py`)

**The variation.** For a bilinear ψ̄Kψ, with δψ = Sψ, δψ̄ = ψ̄S̄ and δK the variation of the operator's coefficients and dressings:

$$\delta(\bar\psi K\psi)=\bar\psi\,(\bar S K + K S + \delta K)\,\psi .$$

- **R1 (A fixed):** S̄ = S♯ = A⁻¹S†A.
- **Rc:** S̄ = −S.
- **R0:** S̄ is free and must be specified.

**Controls.** These are pinned by tests with K = Γ₀ (anticommutes with C), both candidate forms, at (3,1), (7,7) and (9,5), with AC = −CA:

| Case | S̄ | Sum | Verdict on the toy K | Test |
|---|---|---|---|---|
| R1, S = iC | iC | i{C,K} = 0 | invariant, **although iC ∉ 𝔲(A)** | `test_r1_dirac_adjoint_variation` |
| R1, S = C | −C | [K,C] = 2KC ≠ 0 | **not invariant**, although C ∈ 𝔲(A) | same |
| R1, S = iI | −iI | 0 | invariant | same |
| R0, S̄ = S = C | C | {C,K} = 0 | invariant | `test_r0_independent_bar_variation` |
| Rc, S̄ = −C | −C | [K,C] ≠ 0 | not invariant | same |
| (2,2) control, AC = CA | — | the R1 C and iC cases flip | — | `test_r1_variation_flips_at_2_2` |

**Two consequences for the later covariance plan.** Neither is about GU's K.
- In the fixed-A R1 toy setup, membership in 𝔲(A) is neither necessary nor sufficient for a symmetry of a chirality-flipping kinetic bilinear: iC lies outside 𝔲(A) and is invariant, while C lies inside and is not. Membership gets both toy cases wrong.
- A frozen commutator test, [K, S] = 0, rejects **both**. It incorrectly rejects iC and correctly rejects C. Neither membership nor the frozen commutator substitutes for the full variation. A frozen-K test is a **stabilizer** test. It is a necessary covariance condition only under an explicit hypothesis that the background is invariant, i.e. δK = 0. For example, in Rc a frozen variation −SK + KS is cancelled identically by δK = SK − KS.

**GU's actual K.** It is 𝒟̸_ω of (9.16), with its dressings ρ(ε), ρ(ε⁻¹), the metric-dependent ∗ and ⊚, and ϖ itself transforming (δK ≠ 0 under ℋ_τ and 𝒩). The later plan implements this criterion on that K, branch by branch.

## 4. Specification status

| Item | Status | Where |
|---|---|---|
| Field types: ν, ν̄ ∈ Ω⁰(Y,$); ζ, ζ̄ ∈ Ω¹(Y,$) | specified | p. 46; (5.2) p. 31; p. 51 |
| $, H = U(64,64), ad | specified | (3.31)–(3.36) p. 24 |
| The Hermitian form A | **unspecified**. Two candidates (`pairing.py`) agree on every fact computed here | looked: pp. 22–24, 41–42, 46 |
| Operator entries, signs, layout of (9.16) | specified (two independent readings agree) | p. 46; `source_operator.py` |
| The lower-right "non-trivial map" version | **unspecified** (B05-Z) | p. 46 |
| What the display is: bilinear, density, action or equation | branched (B05-M), unenumerated | p. 46 |
| Pairing ⟨ψ̄, X⟩ | branched (B05-P); the source does **not** fix it (transcription rev 1, hand derivation 4 correction) | (9.18)–(9.19) |
| Meaning of ± (fields, ϖ) | branched (B05-L, L′, O); p. 51 labels the fields' bundles S± | pp. 46, 51, 61 |
| The bar on fermions | branched (B05-B, R) | p. 46 |
| The bar and star on ϖ | branched (B05-J enumerated; B05-V unenumerated) | p. 46 |
| How ϖ acts on spinor forms | branched (B05-A), unenumerated (the code assumes wedge) | pp. 31–33, 46 |
| d₀ | branched (B05-D enumerated; B05-D′ unenumerated) | p. 36 |
| ⊚ on spinor-valued forms | branched (B05-S, X enumerated; S′, Q, Y unenumerated) | (8.1) p. 41, Definition 8.1 p. 42 |
| Domain convention for blocks | branched (B05-H) | — |
| Whole-block adjoint relation | **unspecified** (B05-K) | p. 46 |
| Reality condition | branched (R0, R1, Rc, R2, R2′; §2) | p. 46 |
| Seedhe and 𝒩 action on bosons | specified | (5.9) |
| Tedha (ℋ_τ) action on bosons | **conflicting as printed.** (6.13-lit) and (6.13-rec) are branched; §1.2 | (6.2), (6.4), (6.13), (6.20), (7.3), (7.4); footnote 7, p. 36 |
| Any family's action on the fermions | **not located** (B05-T, T′; branches T1–T3 above, none of which yields cancellation without further laws) | looked: pp. 24, 31–47, 50–51, 58, 60–62, 65–66, 68 |
| Normalization and the physical assignment of entries | **unspecified** (B05-N) | p. 46 |
| NP §3.2 objects → April counterparts | mapped; transfer assumptions listed | `np_objection.md` |

## 5. What the covariance test can run on now, and what it cannot

**(a) Already executable: the toy controls (§3).** These are exact and tested. They test the criterion, not GU.

**(b) Conditional formal tests.** These need a full specification per branch first. A binary symmetry verdict for one printed bilinear of (9.16) needs all of the following. The typed (9.16) records only primitive names, signs, degrees and label support. It does not supply matrices.
- one choice from each enumerated axis, with a status other than `domain_mismatch` or `undetermined` for every summand that is to be tested;
- the barred law S̄: R1, Rc or a specified R0 law;
- the coefficient and dressing variations δϖ, δε, δρ(ε^{±1}) and δΦ. Even for constant parameters, conjugation moves noncommuting coefficients, so δK = 0 is a stated background hypothesis, not a default;
- a definite spinor-valued ⊚ (B05-Q, S′, Y): the code's "label-preserving black box of known degree" is not enough to compute S̄K + KS + δK;
- the target: a local bilinear, a density or an action (B05-M);
- under signature labels, the explicit action of C on the coefficient maps, because A-signature support is not a C-eigenvalue.

Only with all of these can the test return invariant or not invariant for that branch. A frozen-K result is reported as a stabilizer result.

**(c) Returns "insufficient data" today:**
- local covariance under ℋ_τ: the fermion laws (B05-T, T′), the spinor action of ⊚ (B05-Q, Y), and the resolution of the (6.13) sign conflict (§1.2);
- covariance under 𝒩: a fermion law, inert or supersymmetry-like, plus the items in (b);
- any anomaly computation: a chosen reality branch, the constrained fermion content, and a quantum measure. The draft supplies partial fermion content (pp. 31, 46, 50–51, 60–62) but no measure.
