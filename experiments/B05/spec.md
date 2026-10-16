# B05 specification sheet: what a covariance test of the fermionic sector needs, and what the draft supplies

Author: Claude (Opus 5.5), 2026-10-15. Plan Task 5, rev 1.2 (`docs/superpowers/plans/2026-10-15-b05-transcription.md`).

**Sources:**
- `transcription.md` rev 1 (`4ea2237`), whose branch IDs B05-* are used below;
- `np_objection.md` (`59c62df`, Codex);
- `pairing.py` and `result.json` (Task 4).

**Scope.** This sheet poses the test. It gives no verdict on any gauge symmetry, anomaly, reality condition or unitarity question.

## 1. Generator families and their action on every field

The draft states actions only on bosonic objects. **It states no transformation law for ν, ζ, ν̄, ζ̄** (looked: pp. 24, 31–47, 50–51, 58, 60–62, 65–66, 68). The only fermionic hint is the decoration ρ(ε) on the barred row and ρ(ε⁻¹) on the column in (9.16), and χ_{ε⁻¹} in (9.17).

### 1.1 Seedhe ℋ: (h, 0) at group level

- **ε.** (5.9) gives (ε, ϖ)·(h, 0) = (εh, h⁻¹ϖh). Right multiplication: ε ↦ εh.
- **ϖ.** ϖ ↦ Aut(h⁻¹, ϖ) = h⁻¹ϖh, from (5.9), p. 33.
- **A₀ / d₀.** The base connection A₀ is fixed (p. 36). Under the Seedhe action, d₀ itself does not transform. Any connection built as A₀·h is a different object.
- **Fermions: not stated.** The branches are:
  - **T1, the decorated reading.** The fields are dressed by ε: ψ ≡ ρ(ε⁻¹)ψ₀ and ψ̄ ≡ ψ̄₀ρ(ε), with ψ₀ transforming by h. The printed decorations would then make the bilinear's ρ-factors cancel under ε ↦ εh. This depends on B05-T′, i.e. whether d₀ acts on ψ₀ or on the dressed field.
  - **T2, the undecorated reading.** ψ ↦ ρ(h⁻¹)ψ and ψ̄ ↦ ψ̄ρ(h). That is consistent with the contragredient law, or with R1 when ρ(h) ∈ U(A).

### 1.2 Tedha ℋ_τ: τ_{A₀}(h) = (h, −h⁻¹(d_{A₀}h)), (6.4) p. 36

- **(ε, ϖ).** By (6.13), (ε, ϖ)·τ(h) = (εh, h⁻¹ϖh − h⁻¹(d_{A₀}h)).
- **A_ω.** (6.20)–(6.22) give A_ω = ∇⁰ + ϖ ↦ A_ω·h, the ordinary gauge transform of the connection.
- **Augmented torsion.** T_g = ϖ − ε⁻¹d_{A₀}ε transforms covariantly, T ↦ h⁻¹Th, by (7.4).
- **Fermions: not stated.** The same branches as 1.1.
- **The obstacle.** (9.16) displays d₀ and ϖ in separate summands. Covariance under ℋ_τ needs the inhomogeneous term of ϖ to combine with d₀, as in d_{A_ω} = d₀ + ϖ. That works only if the summands are read as blocks of d_{A_ω} (transcription, hand derivation 6, and B05-D′).

### 1.3 Translations 𝒩: (1, ϖ′) at group level, (5.9)

- **Bosons.** ε ↦ ε and ϖ ↦ ϖ + ϖ′.
- **Lie-algebra level.** The generator is (0, ϖ′), acting by δϖ = ϖ′. Group- and algebra-level notation must not be mixed.
- **Fermions: not stated.** p. 34 and (12.11) suggest that (ν, ζ) are "square roots" of 𝒩-translations, i.e. a superspace reading. No transformation law, such as δν ∝ ϖ′·(something), is given. Branch **T3**: the fermions are inert under 𝒩. The alternative is supersymmetry-like transformations, which are unspecified.

### 1.4 Constant U(1)-type and chiral generators

These are acting on $ fibrewise, in the global (constant-parameter) form. For any nondegenerate Hermitian A with AC = −CA (`pairing.py`; hand derivations 1–3):

| Generator S | in 𝔲(A)? | Source location |
|---|---|---|
| central phase iI | yes | (8.6) p. 42: degree-0 class among the i-multiplied classes |
| axial phase iC | **no** | (8.6) omits degree 14 |
| chiral boost C (real) | yes | (8.5) p. 42: Λ¹⁴ ⊂ 𝔰𝔬(64,64) |

Membership in 𝔲(A) says only that the transformation preserves A. It is **not** the covariance test (§3). NP's axial transformation is printed as exp(γ̄θ) without an i (`np_objection.md`). Mapping it to C or to iC requires NP's Euclidean conventions and is recorded as a transfer assumption.

### 1.5 Spin(7,7) frame rotations

- **Where they sit.** They lie inside H = U(64,64) via ϱ_D (3.31). The draft does not let them act separately from ℋ.
- **What changes for the fermions.** For local frame changes, the fields of form degree k transform both on the spinor index and on the form index. Because ∗, d₀ and ⊚ (through Φ_r, Definition 8.1) are metric-dependent, the covariance test must vary them too. ⊚ is built from Spin(7,7)-invariant Φ_r, so it is Spin(7,7)-equivariant on ad-valued forms. Its spinor extension is open (B05-Q).

## 1b. A is fixed in R1

In R1 the form A is a fixed algebraic matrix (δA = 0) under internal and axial transformations. It changes only through a connection or frame variation when the geometry on Y is varied.

If A is instead transformed by congruence so that it stays invariant, then δA = −(S†A + AS). Then δ(ψ†Aψ) = 0 for all S, which forces the contragredient law S̄ = −S. That is branch **Rc**, not R1.

## 2. Reality branches (B05-R)

| Branch | Statement | Status in the draft | Which §1 families preserve it |
|---|---|---|---|
| R0 | none: ν, ν̄, ζ, ζ̄ are four independent fields; a complex action; Berezinian integration | the closest to p. 46's "four distinct fields" | everything, since there is no constraint; but the barred law S̄ must then be **specified** separately |
| R1 | ψ̄ = ψ†A, with A one of the two candidate forms (`pairing.forms`; not printed, p. 24) | consistent with U(64,64) = U(A) (3.31) under the candidate identification | S with S♯ = −S, i.e. S ∈ 𝔲(A). For other S the barred field moves by S♯ ≠ −S; §3 decides invariance, not membership |
| Rc | the contragredient law S̄ = −S (an independent bar transforming dually, or a congruence-transformed A, §1b) | not stated | all S, by construction of the pairing. The kinetic operator must still be covariant |
| R2 | Majorana at (7,7): ψ = Jψ with J = B∘conj, J² = +1 (B03, Lean-verified) | not stated | S commuting with J. An explicit fixed-subspace choice is required. The central phase e^{iθ} does **not** preserve Jψ = ψ (J is antilinear: J(e^{iθ}ψ) = e^{−iθ}Jψ), so R2 removes the central U(1) from the symmetry candidates |
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
- Membership in 𝔲(A) is neither necessary nor sufficient for a symmetry of a chirality-flipping kinetic bilinear.
- A test that checks [K, S] = 0 with K frozen would wrongly reject iC under R1, and wrongly accept C.

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
| Seedhe / Tedha / 𝒩 action on bosons | specified | (5.9), (6.4), (6.13), (7.4) |
| Any family's action on the fermions | **unspecified** (B05-T, T′; branches T1–T3 above) | looked: pp. 24, 31–47, 50–51, 58, 60–62, 65–66, 68 |
| Normalization and the physical assignment of entries | **unspecified** (B05-N) | p. 46 |
| NP §3.2 objects → April counterparts | mapped; transfer assumptions listed | `np_objection.md` |

## 5. What the covariance test can run on now, and what it cannot

**Can run now.** The algebraic, constant-parameter part:
- the R1, Rc and R0 laws with the iI, iC and C generators;
- any K assembled from the typed (9.16), under each enumerated label/degree branch, with ⊚ treated as a label-preserving black box of known degree.

That decides which constant generators preserve each branch's printed bilinear. It is a **necessary** condition only.

**Cannot run yet:**
- **Local (gauge) covariance under ℋ_τ.** It needs the fermion transformation law (B05-T, T′) and the spinor action of ⊚ (B05-Q, Y).
- **Covariance under 𝒩.** It needs the fermion law (T3 or a supersymmetry-like law).
- **Any anomaly computation.** It needs a chosen R branch, the physical fermion content after constraints, and the quantum measure. None is in the draft.
