# B07 option C: the T-sector of I₂ and the frozen-metric connection reading

**Status:** results recorded (`complete`; every applicable hard gate held) and independently re-derived by a fresh Codex session (1,444/1,444 compared records agree, 0 disagreements; written without opening the Task 1 code). README audited by Grok (7 findings, all folded: ready with fixes). P7 clean-clone reproduction pending.

**Result, in one paragraph.** At a 4D point, at (3,1) and (1,3), on the flat background with ε = 1 and the metric frozen (reading V, δT = δA), the quadratic part of I₂ = ‖Υ‖² was computed exactly for CCC, CAA, CAC and E_OP. Every applicable hard gate held, including Lorentz covariance for all four operators; real u(A)-closure fails at the auxiliary signatures (2,2) and (4,0), which is the design's declared exception (b).
- **Q1.** The κ₁¹ cross term is nonzero for CCC, CAA and CAC (outcome 1b): I₂ contains a first-order quadratic term in T that contributes to the field equation. For E_OP, C1 = 0, so its nonzero S₁ is a control (control 9), not an outcome.
- **Q2.** On the 15-dimensional pair-antisymmetric part of non-algebraic curvature, every operator has rank 6, landing entirely in 𝓔ᵃ: an antisymmetric-tensor response channel. On the 1-part every operator gives zero.
- **Q3.** CAC's N(u) is nilpotent (3b): no finite dispersion roots. For CCC and E_OP every root is massive-type at (3,1) and tachyonic-type at (1,3); CAA is mixed at both. In every case χ₍₁,₃₎(ν) = χ₍₃,₁₎(iν), and the exchange between massive-type and tachyonic-type is not absorbed by the (3c) m² convention.
- **Q4.** Sign data are recorded at every rational massive-type root; the derivative form vanishes on ker U everywhere, as control 4 predicts.

None of this is an Einstein–Hilbert term, a field-equation claim about (9.4), a stability statement or a degree-of-freedom count (O0, §5 of the design).

Design (pre-registration): `docs/superpowers/specs/2026-10-17-b07-optionc-design.md`, rev 3.1 (`562370e`), frozen before any outcome existed. Plan: `docs/superpowers/plans/2026-10-17-b07-optionc.md`, rev 2 (`e93bee6`), approved by the user. Code and tests: `aac4e42`. Result: `result.json` (`27be011`, status `complete`, canonical payload SHA-256 `5bf868be…4248`). Independent re-derivation: `rederivation_codex.md` (`850c4d0`, `2627696`, `866bb80`).

## The question

H14 (Phase 2) already compared the quadratic action's variation with (9.12)–(9.13) and decided ordinary YM at the principal-symbol level. Option C asks four questions that H14 did not:
- **Q1:** is the κ₁¹ cross term zero in the field equation?
- **Q2:** what does each operator do on pointwise Lorentz-valued curvature values that are not algebraic?
- **Q3:** what are the dispersion roots and kernel structure of the linearized first-order system Υ_lin = 0, and of the field equation?
- **Q4:** what sign data do the named forms take on those kernels?

The outcome classes and their readings were fixed in the design before any code ran. The readings below are the design's §4–§5 readings, with one stated exception for (3f) (see Q3).

## Model and scope

- **Scope tag (P1):** `identity` at a 4D point, signatures (3,1) and (1,3), for the four named operators, with the metric frozen, at quadratic order. Exact arithmetic over Q, Q(i), Q[ν]/f and Q(√−d) only (P4).
- **Background:** flat, B = d, ε = 1, δT = δA. T ∈ Ω¹(u(A)), real fiber dimension 64, in the phased basis e^a ⊗ i^{ph(C)}Γ_C.
- **Operators:** CCC, CAA, CAC from `variation.branch_map`; E_OP from `phase2/run.py:e_op`. All undressed.
- **Objects.** U(k) = X∘(iK∧·) + κ₁∗ is the square 64 × 64 first-order symbol of Υ_lin; U = ∗(iN(k) + κ₁) with N(k) rational. M(k; κ₁) = S₀ + κ₁S₁ + κ₁²S₂ is H14's Hessian matrix, and M(k) = 2U(−k)ᵀG₃U(k). So ker U ⊆ ker M. κ₁ = 1 (scaling covers every real κ₁ ≠ 0).
- **Pairing:** the pinned ⟨x, y⟩ = Tr(x∧∗y)/2^{n/2}; the fixed-X prime convention is a control only (M′(k; κ₁) = −M(k; −κ₁)).
- **Excluded:** [T, T] and higher terms, curved backgrounds, varying ε or metric, dressings ε ≠ 1, 14D.

## Results (`result.json`)

**Q1 and Q2.** Per operator; identical at (3,1) and (1,3) unless a second value is shown.

| Operator | C1 nonzero entries | S₁ ≡ 0? | rank S₁(e_m), m = 0..3 | Q2 15-part rank | in 𝓔 / in 𝓔ᵃ | 1-part rank | CCC inner rank (15) |
|---|---|---|---|---|---|---|---|
| CCC | 192 | no | 38, 38, 38, 38 | 6 | 0 / 6 | 0 | 6 |
| CAA | 144 | no | 38, 38, 38, 38 | 6 | 0 / 6 | 0 | — |
| CAC | 192 | no | 24, 24, 24, 24 | 6 | 0 / 6 | 0 | — |
| E_OP | 0 | no | 30, 30, 30, 30 | 6 | 0 / 6 | 0 | — |

**Q3 (i): χ of N(u) on the timelike ray.** Factor and exponent; m = massive-type (w² > 0), t = tachyonic-type (w² < 0). No factor has non-real squared frequencies w².

| Operator | (3,1) | (1,3) |
|---|---|---|
| CCC | ν³⁴ · (ν²+16)¹ m · (ν²+12)³ m · (ν²+4)⁵ m · (ν²+8)⁶ m | ν³⁴ · (ν-4)¹ t · (ν+4)¹ t · (ν²-12)³ t · (ν-2)⁵ t · (ν+2)⁵ t · (ν²-8)⁶ t |
| CAA | ν⁴⁰ · (ν²-8)¹ t · (ν-2)³ t · (ν+2)³ t · (ν²+8)³ m · (ν²+4)⁵ m | ν⁴⁰ · (ν²+8)¹ m · (ν²-8)³ t · (ν²+4)³ m · (ν-2)⁵ t · (ν+2)⁵ t |
| CAC | ν⁶⁴ (nilpotent) | ν⁶⁴ (nilpotent) |
| E_OP | ν³⁴ · (ν²+64)¹ m · (ν²+32)⁶ m · (ν²+16)⁸ m | ν³⁴ · (ν-8)¹ t · (ν+8)¹ t · (ν²-32)⁶ t · (ν-4)⁸ t · (ν+4)⁸ t |

**Q3 (ii): kernels at every root** (over Q[ν]/f; the record holds for each root of the factor). dim ker U always equals the exponent and U is always semisimple (partial multiplicities all 1). Where M is non-semisimple, its partial multiplicities are `not computed` (design (3f): "partial multiplicities wherever they are computed"); at the three semisimple CAA factors they are six 1s.

| Sig | Operator | Factor | Type | dim ker U / ker M | gap (reading) | M semisimple |
|---|---|---|---|---|---|---|
| (3,1) | CCC | (ν²+16)¹ | massive | 1 / 1 | 0 (hermitian radical) | no (forced) |
| (3,1) | CCC | (ν²+12)³ | massive | 3 / 3 | 0 (hermitian radical) | no (forced) |
| (3,1) | CCC | (ν²+4)⁵ | massive | 5 / 5 | 0 (hermitian radical) | no (forced) |
| (3,1) | CCC | (ν²+8)⁶ | massive | 6 / 6 | 0 (hermitian radical) | no (forced) |
| (3,1) | CAA | (ν²-8)¹ | tachyonic | 1 / 1 | 0 (cross annihilator) | no (forced) |
| (3,1) | CAA | (ν-2)³ | tachyonic | 3 / 6 | 3 (cross annihilator) | yes |
| (3,1) | CAA | (ν+2)³ | tachyonic | 3 / 6 | 3 (cross annihilator) | yes |
| (3,1) | CAA | (ν²+8)³ | massive | 3 / 3 | 0 (hermitian radical) | no (forced) |
| (3,1) | CAA | (ν²+4)⁵ | massive | 5 / 5 | 0 (hermitian radical) | no (forced) |
| (3,1) | E_OP | (ν²+64)¹ | massive | 1 / 1 | 0 (hermitian radical) | no (forced) |
| (3,1) | E_OP | (ν²+32)⁶ | massive | 6 / 6 | 0 (hermitian radical) | no (forced) |
| (3,1) | E_OP | (ν²+16)⁸ | massive | 8 / 8 | 0 (hermitian radical) | no (forced) |
| (1,3) | CCC | (ν-4)¹ | tachyonic | 1 / 1 | 0 (cross annihilator) | no (forced) |
| (1,3) | CCC | (ν+4)¹ | tachyonic | 1 / 1 | 0 (cross annihilator) | no (forced) |
| (1,3) | CCC | (ν²-12)³ | tachyonic | 3 / 3 | 0 (cross annihilator) | no (forced) |
| (1,3) | CCC | (ν-2)⁵ | tachyonic | 5 / 5 | 0 (cross annihilator) | no (forced) |
| (1,3) | CCC | (ν+2)⁵ | tachyonic | 5 / 5 | 0 (cross annihilator) | no (forced) |
| (1,3) | CCC | (ν²-8)⁶ | tachyonic | 6 / 6 | 0 (cross annihilator) | no (forced) |
| (1,3) | CAA | (ν²+8)¹ | massive | 1 / 1 | 0 (hermitian radical) | no (forced) |
| (1,3) | CAA | (ν²-8)³ | tachyonic | 3 / 3 | 0 (cross annihilator) | no (forced) |
| (1,3) | CAA | (ν²+4)³ | massive | 3 / 6 | 3 (hermitian radical) | yes |
| (1,3) | CAA | (ν-2)⁵ | tachyonic | 5 / 5 | 0 (cross annihilator) | no (forced) |
| (1,3) | CAA | (ν+2)⁵ | tachyonic | 5 / 5 | 0 (cross annihilator) | no (forced) |
| (1,3) | E_OP | (ν-8)¹ | tachyonic | 1 / 1 | 0 (cross annihilator) | no (forced) |
| (1,3) | E_OP | (ν+8)¹ | tachyonic | 1 / 1 | 0 (cross annihilator) | no (forced) |
| (1,3) | E_OP | (ν²-32)⁶ | tachyonic | 6 / 6 | 0 (cross annihilator) | no (forced) |
| (1,3) | E_OP | (ν-4)⁸ | tachyonic | 8 / 8 | 0 (cross annihilator) | no (forced) |
| (1,3) | E_OP | (ν+4)⁸ | tachyonic | 8 / 8 | 0 (cross annihilator) | no (forced) |

**Q4 (i)–(ii) at the rational massive-type roots** (both signs ±w₀ agree). Inertias are (n₊, n₋, n₀) on the stated kernel; (0,0,k) is the zero form on a k-dimensional kernel.

| Sig | Operator | w₀² | (i) derivative form on ker M: inertia, rank | (ii) Q_U on ker U: inertia, rank |
|---|---|---|---|---|
| (3,1) | CCC | 1/16 | (0,0,1), 0 | (0,1,0), 1 |
| (3,1) | CCC | 1/12 | (0,0,3), 0 | (0,3,0), 3 |
| (3,1) | CCC | 1/4 | (0,0,5), 0 | (0,5,0), 5 |
| (3,1) | CCC | 1/8 | (0,0,6), 0 | (3,3,0), 6 |
| (3,1) | CAA | 1/8 | (0,0,3), 0 | (3,0,0), 3 |
| (3,1) | CAA | 1/4 | (0,0,5), 0 | (0,5,0), 5 |
| (3,1) | E_OP | 1/64 | (0,0,1), 0 | (0,1,0), 1 |
| (3,1) | E_OP | 1/32 | (0,0,6), 0 | (6,0,0), 6 |
| (3,1) | E_OP | 1/16 | (0,0,8), 0 | (0,8,0), 8 |
| (1,3) | CAA | 1/8 | (0,0,1), 0 | (0,1,0), 1 |
| (1,3) | CAA | 1/4 | (3,3,0), 6 | (0,0,3), 0 |

All other factors are tachyonic-type: their Q4 (i)–(ii) entry is `not_applicable` (complex ω₀).

**Q4 (iii): nested S₀ kernels on the three pinned rays** (κ₁ = 1 pencil data; dimensions over the Gaussian rationals; restricted inertias (n₊, n₋, n₀)). The two quotients are the successive differences; the second is the radical of the pairing on im(X∘(u∧·)). The rays differ, so no row stands for another.

| Sig | Operator | Ray | exact ⊆ ker A ⊆ ker S₀ | quotients | G₁ on ker S₀ | S₁ on ker S₀ |
|---|---|---|---|---|---|---|
| (3,1) | CCC | timelike | 16 ⊆ 33 ⊆ 33 | 17, 0 | (8,25,0) | (0,0,33) |
| (3,1) | CCC | spacelike | 16 ⊆ 33 ⊆ 33 | 17, 0 | (17,16,0) | (0,0,33) |
| (3,1) | CCC | null | 16 ⊆ 33 ⊆ 44 | 17, 11 | (15,13,16) | (3,3,38) |
| (3,1) | CAA | timelike | 16 ⊆ 30 ⊆ 30 | 14, 0 | (11,19,0) | (0,0,30) |
| (3,1) | CAA | spacelike | 16 ⊆ 30 ⊆ 30 | 14, 0 | (16,14,0) | (0,0,30) |
| (3,1) | CAA | null | 16 ⊆ 30 ⊆ 45 | 14, 15 | (16,13,16) | (3,3,39) |
| (3,1) | CAC | timelike | 16 ⊆ 40 ⊆ 52 | 24, 12 | (20,20,12) | (3,3,46) |
| (3,1) | CAC | spacelike | 16 ⊆ 40 ⊆ 52 | 24, 12 | (20,20,12) | (3,3,46) |
| (3,1) | CAC | null | 16 ⊆ 40 ⊆ 58 | 24, 18 | (26,26,6) | (7,7,44) |
| (3,1) | E_OP | timelike | 16 ⊆ 34 ⊆ 34 | 18, 0 | (14,20,0) | (0,0,34) |
| (3,1) | E_OP | spacelike | 16 ⊆ 34 ⊆ 34 | 18, 0 | (17,17,0) | (0,0,34) |
| (3,1) | E_OP | null | 16 ⊆ 34 ⊆ 47 | 18, 13 | (17,16,14) | (1,1,45) |
| (1,3) | CCC | timelike | 16 ⊆ 33 ⊆ 33 | 17, 0 | (17,16,0) | (0,0,33) |
| (1,3) | CCC | spacelike | 16 ⊆ 33 ⊆ 33 | 17, 0 | (16,17,0) | (0,0,33) |
| (1,3) | CCC | null | 16 ⊆ 33 ⊆ 44 | 17, 11 | (13,15,16) | (3,3,38) |
| (1,3) | CAA | timelike | 16 ⊆ 30 ⊆ 30 | 14, 0 | (14,16,0) | (0,0,30) |
| (1,3) | CAA | spacelike | 16 ⊆ 30 ⊆ 30 | 14, 0 | (13,17,0) | (0,0,30) |
| (1,3) | CAA | null | 16 ⊆ 30 ⊆ 45 | 14, 15 | (14,15,16) | (3,3,39) |
| (1,3) | CAC | timelike | 16 ⊆ 40 ⊆ 52 | 24, 12 | (20,20,12) | (3,3,46) |
| (1,3) | CAC | spacelike | 16 ⊆ 40 ⊆ 52 | 24, 12 | (20,20,12) | (3,3,46) |
| (1,3) | CAC | null | 16 ⊆ 40 ⊆ 58 | 24, 18 | (26,26,6) | (7,7,44) |
| (1,3) | E_OP | timelike | 16 ⊆ 34 ⊆ 34 | 18, 0 | (17,17,0) | (0,0,34) |
| (1,3) | E_OP | spacelike | 16 ⊆ 34 ⊆ 34 | 18, 0 | (14,20,0) | (0,0,34) |
| (1,3) | E_OP | null | 16 ⊆ 34 ⊆ 47 | 18, 13 | (15,18,14) | (1,1,45) |

**Auxiliary signatures.** Real closure fails for {'(2,2)': ['CAA', 'CAC', 'CCC', 'E_OP'], '(4,0)': ['CAA', 'CAC', 'CCC', 'E_OP']}; the raw transpose, S₂, prime and reconstruction controls and the backend toys hold there.

**κ₁ = 0** (Q3 (iv), `rank_S0_kappa0`). Rank of S₀ on the timelike / spacelike / null rays, identical at both signatures: CCC 31 / 31 / 20, CAA 34 / 34 / 19, CAC 12 / 12 / 6, E_OP 30 / 30 / 17. det S₀ ≡ 0 with nullity ≥ 16 (the exact directions), as control 9 requires.

## Readings (design §4, applied)

**Q1: outcome (1b) for all four operators.**
- S₁ ≢ 0 for every operator. Its rank at each e_m is recorded above (for M); its grade-block support and the Clifford-grade pairs it couples are in `result.json` (`Q1.grade_pairs_coupled`).
- Reading: I₂ contains a first-order quadratic term in T that contributes to the field equation. The reading is descriptive only. The term is not named Einstein–Hilbert, Palatini or Chern–Simons.
- For E_OP, C1 = 0 at both signatures, so S₁ ≢ 0 is a control, not an outcome (control 9). Q1 was open only for CCC, CAA and CAC, whose C1 is nonzero (192, 144, 192 entries).
- The repaired κ₁ term 2 and the derived term 3 are each nonzero at e₀ for every operator; with S₁ ≢ 0 they do not cancel.

**Q2: nonzero on 𝓔ᵃ for all four operators.**
- On the 15-part, every operator has rank 6, with dim(image ∩ 𝓔) = 0 and dim(image ∩ 𝓔ᵃ) = 6. Reading: there is an antisymmetric-tensor response channel. This is the algebraic shape of the antisymmetric part of the Einstein tensor of a connection with torsion, as in Einstein–Cartan. It is a pointwise algebraic fact of the R2 reading only. It is not a field equation and not by itself non-GR.
- On the 1-part, every operator gives zero (rank 0, coefficients (0, 0) in the E_F(g), E_F′(g) basis after ∗).
- For CCC, the inner term on the 15-part has rank 6. Reading: B02's F1 cancellation, which is sufficient under pair symmetry, does not extend there.
- The 1 and 15 parts are non-algebraic, torsion-sensitive components; they neither exhaust nor measure torsion. Only the grade-2 part of F is tested.

**Q3: dispersion roots (covariance verified for every operator at both signatures).**
- **CAC: (3b) N(u) nilpotent** at both signatures (χ = ν⁶⁴). det U is a nonzero constant and there are no finite dispersion roots: U(k) and M(k) are polynomially invertible. This does not mean the equations contain no derivatives.
- **CCC and E_OP:** every root is **(3c) massive-type** at (3,1) and **(3e1) tachyonic-type** at (1,3), under the (3c) m² convention. No stability or instability claim is made: no time-evolution setup is stated.
- **CAA:** mixed at both signatures, recorded per root.
- No root has non-real ω² (no (3e2)).
- **The signature map.** In every case χ₍₁,₃₎(ν) = χ₍₃,₁₎(iν), with no residual sign, and the kernel data map with it. The (3c) convention gives m² = −k² on (3,1) and m² = +k² on (1,3); on the timelike unit ray k² = −w² at (3,1) and k² = +w² at (1,3), so both give m² = w². The exchange between massive-type and tachyonic-type is therefore **not** absorbed by the m² convention. It is a recorded signature dependence of this frozen-metric reading, not an equivalence of the two readings and not an instability.
- **(3f) non-semisimple roots.** At every root except the two CAA families below, ker M = ker U, and M is non-semisimple there. Where this holds the reading is the design's: "a root of the first-order symbol U, doubled by I₂ = ‖Υ‖²", and nothing further. U itself is semisimple at every root.
- **The two unforced CAA families**, exchanged by the signature map:
  - (1,3), w² = 1/4 (massive-type, real ω₀ = ±½): dim ker M = 6 > dim ker U = 3, a Hermitian radical of dimension 3; M is semisimple there. The derivative form on ker M has inertia (3,3,0), with ker U maximal isotropic; Q_U is the zero form on ker U, (0,0,3).
  - (3,1), factors (ν∓2)³ (tachyonic-type, ω₀ = ±i/2): dim ker M = 6 > dim ker U = 3, a cross-annihilator of dimension 3, with no radical or inertia reading; M is semisimple there. Q4 is `not_applicable`.

  These are polarization-space and algebraic data only.
- **A note on the design's (3f) sentence.** The design says that at complex roots, non-semisimplicity "is forced by the doubled multiplicity: dim ker U ≤ mult(det U) < 2 mult(det U) = mult(det M)". That inequality forces a non-semisimple M only where ker M = ker U, a hypothesis the sentence leaves implicit. The CAA (3,1) roots are complex, have ker M ≠ ker U, and M is semisimple there. The frozen design is not changed; this README applies the sentence with its needed hypothesis, as the plan pre-stated, and records every root individually ("Mixed outcomes are recorded per root").
- Nullities throughout are **polarization-space dimensions**, not physical degree-of-freedom counts. Constraint and gauge analysis is not part of option C.

**Q4: sign data (named forms only).**
- (i) The derivative form V_M^†M′(ω₀)V_M vanishes on ker U at every rational real root (control 4), so it is the zero form wherever ker M = ker U. Its one nonzero instance is the CAA (1,3) w² = 1/4 family above.
- (ii) Q_U is recorded at every rational massive-type root; its inertia varies by operator and root (table above). Q_U is an algebraic restricted form only; no inverse-pole coefficient of M⁻¹ is inferred from it.
- (iii) The nested S₀ kernels and the restricted G₁, S₁ inertias on ker S₀ are recorded on every pinned ray (table above). The rays differ: ker S₀ is larger on the null ray for every operator, and except for CAC the G₁ inertia differs between the timelike and spacelike rays. They are the infinite-eigenvalue data of the M pencil, not residue forms.
- Reading: these are algebraic sign facts about an indefinite pairing (H14). They are not unitarity theorems; the draft fixes no positive real form.
- Tachyonic-type roots have complex ω₀ and give `not_applicable` for Hermitian inertia. No root required an algebraic extension beyond Q(√−d) with d rational.

## Controls (design §3; every applicable hard gate held, and real closure at (2,2)/(4,0) took declared exception (b))

- **Backend toys (control 7)**, 20 pinned toys, run before any named operator: scalar wave operators (massless timelike and null, massive), a Jordan chain (also realified), a singular leading coefficient, the Gram-of-square-symbol toys (G = I and G = diag(1, −1), also over the field), root classification (massive, tachyonic, non-real), an algebraic nilpotent multiplicity, a real-eigenvalue root, and the Q(√−d) fixtures (d = 1 against `gu.inertia`, a hand-checked d = 2, the second-order forms, the conjugation convention). The design's 3D toy (X = id at (2,1)) was not pinned and did not run; by control 7 it is then not a stop condition.
- **Fourier symmetry and reality (1), homogeneous reconstruction (2)**, and the Gram identity M = 2U(−k)ᵀG₃U(k) at every determining wavevector.
- **Direct small action (3):** Hessian entries (2, 4i, −4i, −4i, 0) by polarization of the action, without `fourier_terms`; S₁ against the Q1 closed form.
- **Conventions (4):** S₂ = 2(−1)^qG₁; M′(k; κ₁) = −M(k; −κ₁); det M(ω) = det(2G₃)·u(ω)·u(−ω) on all three rays at 129 points, with u = det U computed independently; the derivative form vanishing on ker U; Q_U = ¼V^†M″V.
- **Lorentz covariance (5)** for all four operators at both signatures: intertwining of U, pairing invariance, Hessian covariance, tracelessness. So the timelike unit ray determines g and F as polynomials in s = k², the spacelike ray matches at the opposite sign of s, and the null ray gives det M constant.
- **Q2 controls (6):** the 20 ⊕ 1 ⊕ 15 projectors; the algebraic-part responses reproduce the recorded vectors (CCC (−1, 0, 0, 0), CAA (−1, 0, ½, 0), CAC (−1, −1, ½, ½), E_OP (2, 0, −1, 0)); the hand ξ entry; the Schur bounds; the CCC inner cancellation on the 20- and 1-parts.
- **Auxiliary signatures (8):** at (2,2) and (4,0), real u(A)-closure fails for all four operators (declared exception (b)). The raw complex-bilinear controls hold there: transpose symmetry over Q(i), S₂, the prime identity, reconstruction, and the backend toys. Nothing from Q1–Q4 runs at those signatures, and no reading is attached.
- **Pre-decided facts (9):** det M(0) ≠ 0 at κ₁ ≠ 0, no root with ω² = 0, E_OP C1 = 0 matching Phase 2, S₁ ≢ 0 where C1 = 0.
- **Nested-kernel gates:** {u⊗λ} ⊆ ker(X∘(u∧·)) ⊆ ker S₀(u) on every ray, with exactly 16 exact directions; ker U ⊆ ker M at every root, over the field.

**Tests and faults.** `tests/test_b07_optionc.py`: 14 tests (controls only; outcomes are recorded, never asserted). Task 1 run (Codex, at `aac4e42`): the 14 new tests passed, the full suite gave 421 passed, and 27 seeded faults C-F1..C-F27 (factor 2, phases, transpose/conjugation, G₃ vs G₁, projector sign, η_cη_d in ξ, realification conventions, the w² map, covariance index order, gates, routing, the deadline, late provenance, misreported ranks) were all RED, each on a test assertion or a designed control exception. P7 reproduction: see the status line.

## Independent re-derivation

A fresh Codex session rebuilt every Q1–Q4 quantity from exact gamma matrices (`gu.clifford` only, with its own wedge, Hodge and exact linear algebra in SymPy), from the design, Phase 2's derivations and README, B02's README, transcription and proofs, and the escape derivations. It did not open the Task 1 code or any other producer module. `result.json` was used as comparison data only, read after the computation.
- **1,444 compared records agree, 0 disagree**, with no extra records. This covers the C1 counts, S₁ ranks and grade pairs, every Q2 quantity, the charpoly of N(u) and its factorization, at every nonzero factor the U and M kernel dimensions, inclusion, multiplicities, kernel gap and its reading, semisimplicity and U's partial multiplicities, Q4 (i)–(ii) at both signs of every rational real root, the nested S₀ kernels and Q4 (iii) on all three rays, and the κ₁ = 0 ranks. Claude re-ran the script at `866bb80` and got the same tally (1,444 agree, 0 disagree, 12 not reconstructed).
- **Findings, all resolved without touching Tasks 1–2:**
  - its first E_OP build used the wrong block normalization (the Shiab coefficient −½ inside the second block); it failed the documented response and C1 = 0, and was fixed from the formula sources (`2627696`);
  - three factor records first said "not computed" for M's partial multiplicities where M is semisimple; they were derived as six 1s;
  - empty `not_applicable` Q4 arrays were dropped to match the schema (no value changed).
- **Not reconstructed (12 groups):** the auxiliary (2,2)/(4,0) records, the producer backend-toy suite, the signature-level direct-Hessian / hand-ξ / projector aggregates (their underlying identities were checked independently), runtime and provenance metadata, and M's partial multiplicities at non-semisimple roots (also "not computed" in `result.json`; agreement on that placeholder certifies nothing).

Full table: `rederivation_codex.md`. Script: `rederive_codex.py` (`uv run python -m experiments.B07.optionc.rederive_codex`, about 70 s).

## What this does not establish (design §5)

- **A negative result closes this reading only:** the flat background, ε = 1 with the metric frozen, the four named operators, at quadratic order. It does not close GU, R1, a curved-background reading, or a model where ε or the metric varies.
- **No Einstein–Hilbert term** can appear in this model (O0): the metric is frozen and every term is quadratic in T. S₂ is a mass term for T. Nothing here is read as gravity or Newton's constant.
- **Q3 and Q4 say nothing about (9.4).** Phase 2's (9.4) result concerns a different action, at order T².
- **No dynamics.** Dispersion roots are not a spectrum of a stated time evolution; massive-type and tachyonic-type are labels under the (3c) convention, not stability statements. Nullities are polarization-space dimensions, not degree-of-freedom counts. Q4 inertias are algebraic sign facts of an indefinite pairing, not unitarity statements.
- **Q2 is pointwise.** An antisymmetric-tensor response channel on the 15-part is an algebraic shape, not a torsion field equation.

## Files

- `sector.py`: phased-basis U, N, G₁, G₃, S₀, S₁, S₂; controls 1–5; Q1.
- `spectrum.py`: charpoly and factor classification, kernels over Q[ν]/f, the Q(√−d) forms, control 4's determinant identity, the backend toys.
- `torsion.py`: the 36 = 20 ⊕ 1 ⊕ 15 projectors and Q2.
- `run.py`: the runner (provenance gate, atomic checkpoints, 2 h per-signature limit, exit 0 / 2 / 3).
- `result.json`: the recorded run.
- `rederive_codex.py`, `rederivation_codex.md`: the independent re-derivation.
