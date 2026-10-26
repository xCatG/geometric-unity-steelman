# B05 transcription: the fermionic operator (9.16) and the data needed to pose a covariance test

Transcriber: Claude (Opus 5.5), 2026-10-15. **Revision 1.**

- **Revision 0** (`68559dd`) was written before the blind second reading.
- **Revision 1** applies Codex's comparison (`notes:b05-transcription/transcription-comparison.md`). A fresh subagent produced the blind reading in `second-reader.md` in the same directory, without seeing the plan, the reviews or rev 0. All 16 matrix positions, 18 summands, signs and decorations agree with rev 0, and `source_operator.py` needs no change. The corrections are:
  1. **The operator label.** It is a slashed calligraphic 𝒟̸_ω, not 𝒟_ω. Claude checked this on the enlarged image.
  2. **Hand derivation 4's third-component cross-check was wrong.** Claude verified the arithmetic. The claim that the source fixes the metric pairing is withdrawn. A new branch, B05-Y, records a per-occurrence degree conflict for ⊚ in (9.18)–(9.19).
  3. **p. 51 evidence for the field ±.** Added.
  4. **d₀ as exterior** is marked as a reconstruction, conditional wherever it is used.
  5. **New unenumerated branches:** B05-A (how ϖ acts), B05-V (the barred potential and the star), B05-T′ (where derivatives act relative to the ρ decorations), B05-K (a whole-block adjoint relation), B05-M (what the display is) and B05-N (normalization and physical assignments).
  6. **Hand derivation 2** now assumes nondegeneracy explicitly.
  7. **Hand derivation 5** now says what "nonzero" means.
  8. **Hand derivation 6's degree statement** is conditional on ϖ acting by wedge.
  9. **The hand-verdict table** covers the first **two** columns.
  10. **Appendix pages 65–66 and 68** are added to the source record.

  The NP object map is `experiments/B05/np_objection.md` (`59c62df`, Codex).

**Independence caveat.** The transcriber also wrote the smoke version of `operator_check.py`. While the plan was under review, they saw its aggregate counts and the eight-reading status check of cell (ζ̄₋, ζ₋). The hand verdicts below are derived from the stated rules and were not copied from runner output. They are therefore a check of the code against its own stated rules, not a blind prediction. The fresh reader in Task 2 supplies the blind reading.

Plan: `docs/superpowers/plans/2026-10-15-b05-transcription.md`, rev 1.2.

## Source

- **The PDF.** Same as B01–B03: GU, *Author's Working Draft v1.0*, April 1, 2021. SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, re-verified 2026-10-15. Printed page numbers equal one-based PDF pages.
- **How the pages were read.** Each was rendered at 130–150 dpi with PyMuPDF and read as an image. `pdftotext` was used only as a cross-check; it drops ⊚, ϖ, the bars, the subscripts and the matrix layout of (9.16).
- **Pages read:**
  - 24 (§3.6);
  - 31–34 (§5.1–5.5);
  - 36–40 (§6–7);
  - 41–42 (§8);
  - 43–47 (§9);
  - 58 (§12.5 table);
  - 60–62 (§12.8–12.10).

  Pages 50–51 are covered by `experiments/B03/transcription.md`. Rev 1 adds pp. 65–66 and 68 (the technical appendix and the locations table, which the p. 42 pointer leads to), inspected by Codex. They define the wedge product, the bundle-valued Hodge degree rule (12.24), contraction (12.25), the matrix bracket, the i-weighted symmetric product, and a Clifford-volume analogue of the Hodge star. They do **not** define the bar, the star, or the spinor conventions of (9.16).
- **Cross-references followed (P11):**
  - ⊚ → §8 (8.1), Definition 8.1, and (9.2)–(9.3);
  - d₀ → §6 p. 36, "A₀ ≈ ∇⁰ ≈ d₀";
  - ϖ → (5.1)–(5.2), (6.22);
  - $ → (3.36);
  - the inhomogeneous group → (5.8)–(5.11);
  - the tilted map → (6.3)–(6.13).

  Looked for, and **not found** anywhere in pp. 24–62:
  - a definition of the bar on ν, ζ;
  - a definition of the subscripts ± on ϖ;
  - a definition of ϖ̄\*;
  - an explicit Hermitian form on $;
  - a transformation law for ν, ζ under ℋ or 𝒢.

## Verbatim

### The operator, p. 46

"In the case of the Fermionic content we can at the classical level take fields ν̄, ζ̄, ν, ζ on Y to be four distinct fields when ultimately we will wish to integrate out the Dirac like operator to take a Berezinian 'integral' in the quantum theory. For ν, ν̄ ∈ Ω⁰(Y, $) and ζ, ζ̄ ∈ Ω¹(Y, $) we can begin with operators like:"

$$
\begin{pmatrix}\bar\zeta_- & \bar\zeta_+ & \bar\nu_- & \bar\nu_+\end{pmatrix}_{\rho(\varepsilon)}\cdot
\underbrace{\begin{pmatrix}
*\circledcirc\varpi_{++} & *\circledcirc(d_0+\varpi_{+-}) & \varpi_{++} & d_0+\varpi_{+-}\\
*\circledcirc(d_0+\varpi_{-+}) & *\circledcirc\varpi_{--} & d_0+\varpi_{-+} & \varpi_{--}\\
-\bar\varpi^*_{++} & -d_0^*-\bar\varpi^*_{+-} & 0 & 0\\
-d_0^*-\bar\varpi^*_{-+} & -\bar\varpi^*_{--} & 0 & 0
\end{pmatrix}}_{\not{\mathcal D}_\omega}\cdot
\begin{pmatrix}\zeta_+\\ \zeta_-\\ \nu_+\\ \nu_-\end{pmatrix}_{\rho(\varepsilon^{-1})}
\tag{9.16}
$$

"noting that other versions of the theory exist including one with a non-trivial map in the lower right quadrant of the operator. This two can be made to look closer to the Dirac Theory of Spinorial Fermions:"

$$\not{\mathcal D}^F_\omega\begin{pmatrix}\zeta\\ \nu\end{pmatrix}_{\rho(\varepsilon^{-1})}=\not{\mathcal D}_\omega\chi_{\varepsilon^{-1}}=0 \tag{9.17}$$

"where χ contains three generations of observed Fermions as well as Looking-Glass matter, dark Spinorial Matter, Rarita-Schwinger matter and more while 𝒟 subsumes the Dirac Operators, and the various subfields of ω accomodate the functionings of the CKM matrix, the Higgs-Like soft mass fields, the Yukawa couplings, Gauge Potentials and the like. Let us compile the Bosonic and Fermionic variations of the Spinorial Lagrangian terms in a single term:"

$$\Upsilon^F=*\begin{pmatrix} d_{A_\omega}\nu+*\circledcirc d_{A_\omega}\zeta\\ \oplus\\ d^*_{A_\omega}\zeta\\ \oplus\\ \bar\nu\zeta+\bar\zeta\nu+\circledcirc\bar\zeta\zeta\end{pmatrix}\tag{9.18}
\qquad
\Upsilon^F_\omega\in\begin{pmatrix}\Omega^{d-1}(Y,\$)\\ \oplus\\ \Omega^{d}(Y,\$)\\ \oplus\\ \Omega^{d-1}(Y,\mathrm{ad})\end{pmatrix}\tag{9.19}$$

"as a kind of 1-form on some SuperSpace-like structure over 𝒜", then (9.20): $\Upsilon_\omega=\Upsilon^B_\omega+\Upsilon^F_\omega=0$ or $\mathcal D\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega$.

**Layout facts read from the image.** These are the facts the typed data encodes.
- The row vector is (ζ̄₋, ζ̄₊, ν̄₋, ν̄₊), with subscript ρ(ε). The column vector is (ζ₊, ζ₋, ν₊, ν₋), with subscript ρ(ε⁻¹).
- In each position the row field carries the opposite subscript sign to the column field.
- The upper two rows have no printed sign.
- In the lower two rows every summand is printed with a minus, and the ϖ there carry a bar and a star: ϖ̄\*.
- The lower-right 2×2 is printed as zeros.
- The operator is labelled with a **slashed** calligraphic D, 𝒟̸_ω (rev 1). The slash does not by itself decide whether each d₀ is Clifford-contracted (B05-D).
- (9.16) has no "= 0", no integral and no outer star. (9.18) has an outer star.

### The Shiab family and the Clifford decomposition, pp. 41–42 and 43

$$\circledcirc_\varepsilon\eta=*^n\, i^{\frac{1\pm1}{2}}\big[(\varepsilon^{-1}\Phi_r\varepsilon)\wedge *^m\eta\big]_\pm\tag{8.1}$$

"or perhaps a sum of such terms, where typically Φ_r is a normed Lie Algebra Valued r-form valued in an invariant subspace of the structure group of the tangent bundle and the bracket is either a commutator or an anti-commutator with a factor of i out front in the case of the latter."

$$\mathfrak{so}(64,64)\ \text{“=”}\ \underbrace{(\Lambda^2\oplus\Lambda^6\oplus\Lambda^{10}\oplus\Lambda^{14})}_{\$_L\otimes\$_R=\$_L\otimes\$_L^*=\$_R^*\otimes\$_R}\oplus\underbrace{(\Lambda^1\oplus\Lambda^5\oplus\Lambda^9\oplus\Lambda^{13})}_{\Lambda^2(\$_L)\oplus\Lambda^2(\$_R)}\subset \mathrm{Cl}_{\mathbb R(7,7)}\tag{8.5}$$

$$\mathfrak u(64,64)/\mathfrak{so}(64,64)\ \text{“=”}\ k_0\Lambda^0\oplus k_3\Lambda^3\oplus k_4\Lambda^4\oplus k_7\Lambda^7\oplus k_8\Lambda^8\oplus k_{11}\Lambda^{11}\oplus k_{12}\Lambda^{12}\tag{8.6}$$

"which must be multiplied by various factors of i inside the complexification."

**Definition 8.1.** "Let {Φ_i}, i = 0, …, 14, be a basis for the invariant subspaces of [Λ^i(ℝ^{7,7}) ⊗ 𝔲(64,64)]_{Spin(7,7)} (8.7) seen as a Spin(7,7) representation."

(9.2) is ⊚: Ω²(Y^{7,7}, ad) → Ω^{d−1}(Y^{7,7}, ad). (9.3) is ⊚ξ = [(ε⁻¹Φ¹ε) ∧ (∗ξ)] − (∗/2)[(ε⁻¹Φ¹ε) ∧ ∗[(ε⁻¹Φ²ε) ∧ (∗ξ)]], the Ricci-like and Ricci-scalar-like terms. That transcription is `experiments/B02/transcription.md`.

### The structure group and bundles, p. 24

(3.30): Spin(7,7) → SL(64,ℝ) → SO(64,64) → U(64,64) → GL(128,ℂ).
(3.31): ϱ_Dirac = ϱ_D : Spin(7,7) → U(64,64), "on complex Dirac Spinors using the notation H = U(64,64)".
(3.32): P_H = P_{F̃r(C^{7,7})} ×_{ϱ_D} H.
(3.34): ad = P_H ×_ad 𝔲(64,64).
(3.35): Ad = P_H ×_Ad U(64,64).
(3.36): $ = P_H ×_{ϱ_D} ℂ^{64,64}.
**No Hermitian form is printed.** ℂ^{64,64} names a signature only.

### Field content and the inhomogeneous group, pp. 31–33

- **(5.1):** ω = (β, χ) = ((ε, ϖ), (ν, ζ)), with "Bosons β" and "Fermions χ". The naive spins are 0, 1, ½ and (½, 3/2).
- **(5.2), a table:**
  - Ω⁰_Y ⊗ ad = ε̄ (the linearization of ε);
  - Ω⁰_Y ⊗ $ = ν;
  - Ω¹_Y ⊗ ad = ϖ;
  - Ω¹_Y ⊗ $ = ζ.
- **The spaces:**
  - (5.3): ℋ = Γ^∞(P_H ×_Ad H);
  - (5.4): 𝒜 = Conn(P_H);
  - (5.5): 𝒩 = Ω¹(Y, ad(P_H)).
- **Definition 5.1, (5.8)–(5.9):**
  - 𝒢 = ℋ ⋉ 𝒩;
  - g₁·g₂ = (ε₁,ϖ₁)·(ε₂,ϖ₂) = (ε₁·ε₂, Aut(ε₂⁻¹, ϖ₁) + ϖ₂).
  - The identity is (1, 0), so a pure translation is (1, ϖ) at group level.
- **The actions:**
  - (5.10): A·g = A·(ε, ϖ) = A·ε + ϖ;
  - (5.11): g·A = (A + ϖ)·ε⁻¹.
- **p. 34:** "expressions like (ν̄ · ζ) can be given meaning directly as elements of 𝒩 while expressions like ζ̄_a · ζ_b are harder to directly interpret as translations".

### The distinguished connection and the tilted maps, pp. 36–39

- **p. 36:** "we will refer to the connection as A₀ ≈ ∇⁰ ≈ d₀ as needed". Here ∇⁰ is the Levi-Civita connection of g_ℵ on TY, "which, by abuse of notation, we will consider as determining a spin connection on the structure bundle P_H of Dirac spinors over Y".
- **The actions and maps, with formulas:**
  - (6.2): α·(ε, ϖ) = ε⁻¹(α)ε + ε⁻¹(d_{A₀}ε) + ϖ.
  - (6.4): τ_{A₀}(h) = (h, −h⁻¹(d_{A₀}h)), called the "Tedha" gauge group ℋ_τ. The plain inclusion (h, 0) is "Seedhe".
  - (6.9): τ̂₀(h) = (h, −h⁻¹d₀h).
  - (6.13): g·τ_{A₀}(h) = (ε·h, h⁻¹ϖh − h⁻¹(d_{A₀}h)).
  - (6.22): A_ω = ∇⁰ + ϖ_ω, B_ω = ∇⁰ + ε_ω⁻¹(∇⁰ε_ω).
  - (7.3): T_g = ϖ − ε⁻¹(d_{A₀}ε).
- **Footnote 7, p. 36:** "There appears to have been multiple sign conventions and some notational shifts within the files from which this section was reassembled … there may be 2 or more conflicting convetions in this section."

### Chirality and mass, pp. 60–62

- **(12.12):** a toy non-chiral system on (ψ_L, ψ_R): the matrix [[−Λ, ∂̸_A], [∂̸_A, −Λ]] annihilates (ψ_L, ψ_R)ᵀ, with R(y) = 4Λ(y).
- **(12.21):** "the field playing the role of the fundamental mass for the generalized Dirac equations is actually part of the gauge potential". Specifically, it is an invariant subspace Λ¹ ⊗ Λ¹ ⊂ Λ¹ ⊗ Λ\* of Ω¹(Y, ad).
- **p. 62:** "part of the field ζ ∈ Ω¹(Y, $_R) is an ordinary second generation spinor in Ω⁰(Y, $_L) via the Dirac gamma matrix contraction".
- **(12.9) table:** ν, ζ are 'Dirac–Rarita–Schwinger' fields of order 1; ϖ is Yang–Mills of order 2; T_ω is 'Chern–Simons–Einstein' of order 1.

## Symbol table

| Symbol | Type | Where defined |
|---|---|---|
| $ | the complex rank-128 bundle P_H ×_{ϱ_D} ℂ^{64,64} | (3.36), p. 24 |
| A (Hermitian form on $) | **not printed.** Only the signature (64,64) via U(64,64). B05 uses two *candidate* Spin(7,7)-invariant forms (`pairing.forms`), which are not recovered from the source | looked: pp. 22–24, 41–42, 46 |
| ε | a section of P_H ×_Ad U(64,64), in ℋ | (5.1), (5.3) |
| ϖ | ad-valued 1-form, in 𝒩 = Ω¹(Y, ad) | (5.1), (5.2), (5.5) |
| ϖ₊₊, ϖ₊₋, ϖ₋₊, ϖ₋₋ | **not defined.** Presumably blocks of ϖ for some ± splitting of $. Which splitting, and which index is the source, are open (B05-L, B05-O) | looked: pp. 24–47 |
| ϖ̄\*_{ab} | **not defined.** "Bar" and "star" on a block of ϖ (B05-J) | looked: pp. 24–47 |
| d₀ | p. 36 prints only "A₀ ≈ ∇⁰ ≈ d₀" for the spin connection (an abuse of notation). Extending it degree-wise as an exterior covariant derivative is a **reconstruction**, conditional wherever it is used. Whether it is Clifford-contracted in (9.16) is open (B05-D) | p. 36 |
| d₀\* | **not defined.** Presumably the formal adjoint of d₀ | looked: pp. 36–47 |
| ∗ | the Hodge star on Y^{7,7}. In B02, the pinned-star convention | (8.1), (9.3) |
| ⊚ | the Shiab family (8.1): a sum of terms \*ⁿ i^{(1±1)/2} [(ε⁻¹Φ_rε) ∧ \*^m η]_±, defined for **ad-valued** η. Its action on $-valued forms is not defined (B05-Q) | (8.1), Definition 8.1, (9.2)–(9.3) |
| Φ_r | basis of [Λ^r(ℝ^{7,7}) ⊗ 𝔲(64,64)]^{Spin(7,7)}, r = 0…14 | Definition 8.1, (8.7) |
| ρ(ε), ρ(ε⁻¹) | a decoration on the row and column vectors of (9.16). Presumably the action of ε on spinors through ϱ_D, i.e. the fields "dressed" by ε⁻¹ and ε. Not defined in §9.3 | (9.16), (9.17) χ_{ε⁻¹} |
| bar (ν̄, ζ̄) | **not defined.** "four distinct fields" (p. 46). Whether ν̄, ζ̄ are Dirac adjoints, independent fields, or Berezin partners is open (B05-B, B05-R) | looked: pp. 31–47, 60–62 |
| subscript ± on ζ, ν | **not defined** in §9.3. p. 51's diagram labels ν± ∈ Ω⁰(S±) and ζ± ∈ Ω¹(S±), the signed spinor bundles. The other sign systems in that diagram (Spin superscripts, component signs) are not uniformly the same, and no C projector is asserted. Plausibly chirality, as in (12.20) with $_L, $_R | p. 51 (rev 1), (12.20) p. 61 |
| 𝒢, ℋ, 𝒩 | 𝒢 = ℋ ⋉ 𝒩 | (5.8)–(5.9) |
| τ_{A₀}, ℋ_τ ("Tedha"), Seedhe | (6.4), Definition 6.2 | pp. 36–37 |
| A_ω, B_ω | ∇⁰ + ϖ_ω and ∇⁰ + ε_ω⁻¹∇⁰ε_ω | (6.22) |
| 𝒟_ω, 𝒟^F_ω, χ | the operator of (9.16), its action on (ζ, ν), and the fermion content | (9.16)–(9.17) |
| ϒ^F | the fermionic variation | (9.18)–(9.19) |
| d | dim Y = 14 | (9.2), (9.19) |

## Branch register

The `code` column says whether `experiments/B05/operator_check.py` enumerates the branch.

| ID | Open reading | Readings | Evidence | code |
|---|---|---|---|---|
| B05-L | What ± on ϖ and on the fields labels | (i) the eigenvalue of the chirality C; (ii) the eigenspaces of a candidate form A (the "64,64" of U(64,64)) | p. 61 uses $_L/$_R for chirality. ℂ^{64,64} on p. 24 names a signature split. Neither is said in §9.3 | `LABEL` |
| B05-L′ | ϖ's labels in a **different** system from the fields' | e.g. fields by chirality, ϖ by A-signature | none either way | **no** |
| B05-O | Which subscript of ϖ_{ab} is the target | (i) a = target; (ii) a = source | none | `ORDER` |
| B05-B | What the row subscript on ζ̄_±, ν̄_± means | (i) the bar of ζ_± (Dirac adjoint labelled by the unbarred field: pairs opposite chirality when AC = −CA); (ii) the barred field's own right C-eigenvalue, ζ̄₋ := (ζ₊)†A, which pairs equal labels and matches the row/column order of (9.16); (iii) an independent field in the dual of $_±, which also pairs equal labels | the layout of (9.16): row ζ̄₋ above column ζ₊; "four distinct fields" | `BAR` (ii and iii share `dual_field`) |
| B05-J | What ϖ̄\*_{ab} is | (i) the A-adjoint A⁻¹ϖ_{ab}†A; (ii) ϖ with the subscripts swapped (as a label map) | none | `ADJ` |
| B05-H | A block applied outside its domain | (i) a type error; (ii) the zero map (block extended by zero) | none | `HOM` |
| B05-P | The pairing ⟨ψ̄, X⟩ | (i) ψ̄ ∧ X is a top form; (ii) a pointwise inner product, deg ψ̄ = deg X | (9.18)–(9.19) typing, below | `PAIR` |
| B05-D | What d₀ is in (9.16) | (i) the exterior covariant derivative d_{∇⁰}; (ii) Clifford-contracted, c(eⁱ)∇ᵢ | p. 36 "A₀ ≈ ∇⁰ ≈ d₀"; (9.18) writes d_{A_ω}; (12.12) uses ∂̸_A off-diagonal | `D0KIND` |
| B05-D′ | d₀ as d + d\*, or with a frame/Clifford piece mixing labels | — | none | **no** |
| B05-X | The printed ∗ in front of ⊚ | (i) a further Hodge star; (ii) (8.1)'s own outer \*ⁿ with n = 1 | (9.18) prints "∗⊚d_{A_ω}ζ" inside an outer ∗ | `STARPARSE` |
| B05-S | The (8.1) parameters m, n, r for ⊚ on spinor forms | m, n ∈ {0, 1}; r = 0…14 | Definition 8.1; (9.3) uses r = 1, 2 | `SHIAB_M/N/R` |
| B05-S′ | ⊚ as a **sum** of (8.1) terms (as in (9.3)) | — | "or perhaps a sum of such terms" (p. 41) | **no** (each term separately) |
| B05-Q | Whether ⊚ preserves spinor labels: does Φ_r act on the spinor factor, and how? | — | (8.1) is defined for ad-valued η only | **no** (assumed label-preserving) |
| B05-I | Index placement of ± before or after the adjoint | — | none | **no** |
| B05-W | Row-dependent pairings | — | none | **no** |
| B05-R | The reality condition | R0 none; R1 Dirac adjoint with a candidate A; R2 Majorana at (7,7) via J (J² = +1); R2′ symplectic Majorana at (9,5) | "four distinct fields", Berezinian (p. 46) | **no** (Task 5) |
| B05-T | Transformation laws of ν, ζ, ν̄, ζ̄ under ℋ, ℋ_τ, 𝒩 | — | only the ρ(ε)/ρ(ε⁻¹) decorations | **no** (Task 5) |
| B05-Z | The lower-right "non-trivial map" version | — | p. 46 | **no** (unspecified) |
| B05-A | How ϖ (and ϖ̄\*) acts on spinor-valued forms (rev 1) | wedge with the represented 𝔲(64,64) action (degree +1); Clifford action or contraction of its form index (degree 0 or −1) | pp. 31–33 make ϖ an ad-valued 1-form. p. 46 does not say how it acts on Ω^k($). The coefficient type does not choose wedge | **no** (code assumes wedge: +1 and −1) |
| B05-V | The bar and the superscript star on the **bosonic** potential (rev 1) | coefficient conjugation; a pairing-induced (fibre) adjoint; a formal differential/form adjoint; an independent barred potential | p. 46 prints the operations without defining them. "Four distinct fields" refers to fermions, not to ϖ | partly (`ADJ`: 2 readings) |
| B05-T′ | Gauge decorations (rev 1) | whether the differentials act on the ρ(ε⁻¹)-dressed fields, or the dressing dependence is already inside 𝒟̸_ω | p. 46 prints whole-vector decorations only | **no** (Task 5) |
| B05-K | A whole-block adjoint relation between the upper-right and lower-left blocks (rev 1) | — | the positions and signs are printed. No transpose/adjoint identity is stated, and none can be inferred until ordering, bar, form adjoint and pairing are fixed together | **no** (not a transcription fact) |
| B05-M | What the display is (rev 1) | a local bilinear; an action density; an integrated action; an equation ((9.17) has "= 0", (9.16) does not) | p. 46 | **no** |
| B05-N | Normalization and physical assignments (rev 1) | the integration/density convention; operator domains and boundary conditions for adjoints; assigning particular entries to masses, CKM or Yukawa terms (p. 46 text), which is not proven | p. 46 | **no** |
| B05-Y | ⊚ degree conflict across occurrences in (9.18)–(9.19) (rev 1) | per-occurrence Shiab maps; or an unresolved source inconsistency | hand derivation 4, source cross-check | **no** |

## Hand derivations (P3 expected values for Task 4)

**1. AC = (−1)^q CA.** In even dimension d, C ∝ Γ₀⋯Γ_{d−1} anticommutes with every Γ_a. If A = c·Γ_{a₁}⋯Γ_{a_q} with q factors, moving C through A gives AC = (−1)^q CA. For (3,1), (1,3), (7,7) and (9,5), both the timelike product (q factors) and the spacelike product (p factors) have an odd count, so AC = −CA. For (2,2) the count is even, so AC = CA.

**2. Neutral signature.** Suppose A is a **nondegenerate** Hermitian form, C is a Hermitian involution and AC = −CA. The candidate monomial forms are invertible. Then A maps the +1-eigenspace V₊ of C into V₋, and vice versa. In a basis adapted to V₊ ⊕ V₋, A has the form [[0, B†], [B, 0]] with B invertible, since A is. Such a matrix has eigenvalues ±σᵢ(B), so its signature is (n/2, n/2). At (7,7) that is (64,64), consistent with U(64,64).

**3. U(1) membership.** X ∈ 𝔲(A) iff X†A + AX = 0.
- X = iI: −iA + iA = 0, so iI ∈ 𝔲(A).
- X = C: CA + AC = 0, so C ∈ 𝔲(A).
- X = iC: −iCA + iAC = i(AC − CA) = 2iAC ≠ 0, so iC ∉ 𝔲(A).

The draft agrees: (8.5) lists Λ¹⁴ (∝ C) inside 𝔰𝔬(64,64) ⊂ 𝔲(64,64), and (8.6) lists the i-multiplied classes, which omit Λ¹⁴.

**R1 variation (Task 5's criterion, pre-registered).** Take ψ̄ = ψ†A with A fixed. Then δψ = Sψ gives δψ̄ = ψ̄S♯, with S♯ = A⁻¹S†A. Take K anticommuting with C (e.g. Γ₀):
- S = iC: S♯ = iC, and the variation is i(CK + KC) = 0;
- S = C: S♯ = −C, and the variation is KC − CK = 2KC ≠ 0;
- S = iI: S♯ = −iI, and the variation is 0.

**4. Degree of ∗⊚(ϖ ∧ ζ) on a 1-form, d = 14.** ϖ ∧ ζ has degree 2.
- With m = 1, n = 0, r = 1 and an extra star: ∗^m gives 12, Φ₁∧ gives 13, n = 0 keeps 13, and the extra ∗ gives 1.
- Under the outer-star parse (no extra star, n = 1): 2 → 12 → 13 → 1.

**Source cross-check (not from code; corrected in rev 1).** Read with ordinary wedge degrees, (9.18)–(9.19) give **conflicting** degree requirements for ⊚. **The source does not fix the pairing.**
- **First component.** (9.18)–(9.19) put ∗(d_{A_ω}ν + ∗⊚d_{A_ω}ζ) in Ω^{13}($). So the inner sum is a 1-form, and ∗⊚d_{A_ω}ζ is a 1-form. With "∗⊚" read as ∗ after ⊚, ⊚ sends the 2-form d_{A_ω}ζ to a **13-form**, the same degree map (9.2) gives for ad-valued 2-forms.
- **Third component.** It prints ∗(ν̄ζ + ζ̄ν + ⊚ζ̄ζ) ∈ Ω^{13}(ad). Here ν̄ζ and ζ̄ν are 1-forms, so the inner sum is a 1-form, and ⊚ζ̄ζ must be a **1-form**. So ⊚ sends the 2-form ζ̄ζ to a 1-form. If it sent 2 → 13 as in the first component, the printed outer ∗ would give Ω¹, not Ω^{13}. (Rev 0 claimed this component confirms ⊚: Ω² → Ω^{13}. That was an arithmetic error: it dropped the outer ∗. Codex's comparison caught it, and Claude re-derived it.)
- **Consequence.** The two occurrences need different degree maps, 2 → 13 and 2 → 1, which are related by a star. That fits either per-occurrence Shiab maps (B05-Y) or an unresolved inconsistency in the source. Neither a star is silently added nor the printed one removed.
- **What still holds, under the stated readings only.** (9.3)'s two printed terms are each the map Ω² → Ω^{13}:
  - the Ricci-like term [Φ¹ ∧ ∗ξ] is (m = 1, n = 0, r = 1);
  - the Ricci-scalar-like term ∗[Φ¹ ∧ ∗[Φ² ∧ ∗ξ]] runs 2 → 12 → 14 → 0 → 1 → 13.

  The second component, ∗d\*_{A_ω}ζ ∈ Ω^{14}, has d\*ζ ∈ Ω⁰. These are consistent with the metric-pairing branch (B05-P ii) of the matrix bookkeeping, but they do **not** establish it. (9.16) itself has no outer star, and converting it into (9.18) takes further choices.

**5. Textbook controls.** Here "nonzero" means the pairing channel is not forced to vanish by the label rules, not that every field configuration gives a nonzero value.
- ψ̄₋(∂̸ψ₋): ∂̸ anticommutes with C, so ∂̸ψ₋ ∈ V₊. Under a Dirac adjoint labelled by the unbarred field (AC = −CA), ψ̄₋ pairs with V₊, so the term is nonzero. This is the Weyl kinetic term ψ_L†σ̄·∂ψ_L.
- ψ̄₋ψ₋ = ψ₋†Aψ₋: Aψ₋ ∈ V₊ ⊥ ψ₋, so it is 0. A mass term couples L to R.
- ψ̄₋ mψ₊ with m: V₊ → V₊ is nonzero.

**6. The (ζ̄₋, ζ₋) cell collision.** The cell is ∗⊚(d₀ζ₋ + ϖ₊₋ζ₋). Take ⊚ and ∗ to be label-preserving (B05-Q assumed) and d₀ exterior (B05-D i).
- **Degree.** Assume ϖ acts by wedge (B05-A) and d₀ is exterior (both reconstructions). Then d₀ζ₋ and ϖ₊₋ ∧ ζ₋ are both 2-forms, so the sum is degree-consistent. This does not exclude a reconstruction where both act by Clifford action or contraction.
- **Labels, chirality reading (B05-L i).** Exterior d₀ = d_{∇⁰} commutes with C, so d₀ζ₋ ∈ V₋.
  - With a = target (B05-O i), ϖ₊₋: V₋ → V₊, so ϖ₊₋ζ₋ ∈ V₊. The two summands land in different chiralities, so whichever chirality ζ̄₋ pairs with, exactly one survives:
    - bar reading B05-B (i): ζ̄₋ pairs with V₊, so d₀ζ₋ pairs to zero and ϖ₊₋ζ₋ is nonzero;
    - bar readings (ii) and (iii): ζ̄₋ pairs with V₋, so d₀ζ₋ is nonzero and ϖ₊₋ζ₋ pairs to zero.
  - With a = source (B05-O ii), ϖ₊₋: V₊ → V₋ does not accept ζ₋ ∈ V₋. That is a type error under B05-H (i), or zero under B05-H (ii).
  - So under every enumerated chirality reading with exterior d₀, **at most one of the two printed summands pairs nonzero.**
- **Labels, signature reading (B05-L ii).** ∇⁰ takes values in 𝔰𝔭𝔦𝔫(7,7). Its noncompact part mixes the eigenspaces of A, so the support of d₀ζ₋ is not established. Status `undetermined`.
- **Readings that could reconcile the two summands.** None is chosen here:
  - ⊚ acting on the spinor labels (B05-Q);
  - a frame or Clifford piece in d₀ that flips chirality (B05-D′);
  - ϖ's ± in a different system from the fields' (B05-L′).

  (6.22) A_ω = ∇⁰ + ϖ and the (9.18) form d_{A_ω} suggest that "d₀ + ϖ₊₋" is a block of d_{A_ω}. Under the chirality reading, ∇⁰ has no (+,−) block, which is the same tension seen from the connection side.
- **Scope.** This is a statement about the enumerated readings, not a verdict on (9.16).

## Hand verdicts (pre-registered; compared with `run.py`'s `label_table` in Task 4, Step 8)

Statuses use the plan's vocabulary. The six summands are those in the first **two** columns (ζ₊ and ζ₋) under rows ζ̄₋ and ν̄₋. Codex's comparison checked all twelve against the stated rules and they agree. The derivations use only the rules stated in the branch register.

**Branch α:** (chirality, target_source, dirac_adjoint, a_adjoint, strict, exterior). Row ζ̄₋ and row ν̄₋ pair with V₊.

| Cell, summand | Derivation | Status |
|---|---|---|
| (ζ̄₋, ζ₊) ∗⊚ϖ₊₊ | ϖ₊₊: V₊ → V₊; ζ₊ ∈ V₊ ↦ V₊; the row wants V₊ | `nonzero` |
| (ζ̄₋, ζ₋) ∗⊚d₀ | exterior d₀ keeps V₋; the row wants V₊ | `pairs_to_zero` |
| (ζ̄₋, ζ₋) ∗⊚ϖ₊₋ | ϖ₊₋: V₋ → V₊; the row wants V₊ | `nonzero` |
| (ν̄₋, ζ₊) ϖ̄\*₊₊ | the A-adjoint of V₊ → V₊ is V₋ → V₋ (AC = −CA flips both); ζ₊ ∉ V₋ | `domain_mismatch` |
| (ν̄₋, ζ₋) d₀\* | keeps V₋; the row wants V₊ | `pairs_to_zero` |
| (ν̄₋, ζ₋) ϖ̄\*₊₋ | ϖ₊₋: V₋ → V₊, so its A-adjoint is V₋ → V₊; ζ₋ ↦ V₊; the row wants V₊ | `nonzero` |

**Branch β:** (chirality, target_source, dual_field, subscript_swap, strict, clifford). Row ζ̄₋ and row ν̄₋ pair with V₋.

| Cell, summand | Derivation | Status |
|---|---|---|
| (ζ̄₋, ζ₊) ∗⊚ϖ₊₊ | ζ₊ ↦ V₊; the row wants V₋ | `pairs_to_zero` |
| (ζ̄₋, ζ₋) ∗⊚d₀ | Clifford d₀ flips: V₋ ↦ V₊; the row wants V₋ | `pairs_to_zero` |
| (ζ̄₋, ζ₋) ∗⊚ϖ₊₋ | V₋ ↦ V₊; the row wants V₋ | `pairs_to_zero` |
| (ν̄₋, ζ₊) ϖ̄\*₊₊ | the swap of (+,+) is V₊ → V₊; ζ₊ ↦ V₊; the row wants V₋ | `pairs_to_zero` |
| (ν̄₋, ζ₋) d₀\* | Clifford flips: V₋ ↦ V₊; the row wants V₋ | `pairs_to_zero` |
| (ν̄₋, ζ₋) ϖ̄\*₊₋ | ϖ₊₋ is V₋ → V₊, so the swap is V₊ → V₋; ζ₋ ∉ V₊ | `domain_mismatch` |

**Degrees,** with metric pairing, exterior d₀ and extra_star (m = 1, n = 0, r = 1). Every summand of rows ζ̄ ends as a 1-form, and every summand of rows ν̄ as a 0-form:
- ϖ ∧ ν is a 1-form;
- d₀ν is a 1-form;
- ϖ̄\*ζ and d₀\*ζ are 0-forms;
- the ∗⊚ terms follow hand derivation 4.

So this degree branch is consistent on all 18 summands. Clifford d₀ fails it: d₀ν stays a 0-form under a 1-form row.

## Open items for Task 5 (after the rev 1 comparison)

- The unenumerated branches added in rev 1 (B05-A, V, T′, K, M, N, Y) must be carried, as unenumerated, into `spec.md`'s status table and the README before any elimination or covariance claim.
- Whether the row/column subscript pattern supports B05-B (ii) over (i). The layout fact is recorded; no reading is chosen.
- The signs: the lower rows' minus signs, and the relative sign between d₀ and ϖ within one entry, are needed for any covariance computation. They live here and in `source_operator.py`'s signs.
