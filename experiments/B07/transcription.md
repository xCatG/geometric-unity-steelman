# B07 transcription: the first-order bosonic action (9.4), its claimed variation (9.7), and the surrounding §9 equations

Transcriber: Claude (Opus 5.5), 2026-10-16. **Revision 1.1** (rev 1 plus Grok's correction of N0's mechanism in the [T, T] row; see the N0 note).

- **Revision 0** (`0912d4c`) was written before the blind second reading.
- **Revision 1** applies Codex's comparison (`.agent-handoff/b07-transcription/transcription-comparison.md`; the blind reading by a fresh subagent is `second-reader.md` in the same directory). All coefficients, algebraic signs, matrix entries and star placements in (9.1)–(9.22) agree between the two readings. The corrections:
  1. **H8 term 3 has a definite wrong sign in (9.13).** Under the pinned convention ∗† = −∗ between Ω¹ and Ω^{d−1}, so the derived term is −κ₁∗⊚F_A, not "±". Claude re-derived this (⟨∗a, u⟩ = −⟨a, ∗u⟩ from the anti-isometry and ∗∗ = +1 on Ω¹).
  2. **Conflict 8 is withdrawn as stated.** It identified (9.20)'s 𝒟 with (9.6)'s 𝔇 without support; the remaining issue is the undefined operator and embedding. Its quotation of the right side is corrected to Υ^F_ω.
  3. **Verbatim details:** the second colon in (9.1); no parentheses around the space stack in (9.5); the "Displaced Torsion" brace in (9.8) is an underbrace; item 3 of (9.4)'s "where" list is written out (it has ⊚_ε and omits the g_{μν} annotation); footnote 10 is on p. 43.
  4. **p. 47 does not select N2**: F_A has degree 2, so its bracket's grading sign is always +1. N0 is marked as an extension of the coefficient commutator (12.26), not forced by it.
  5. **H2:** for L = ⊚∘d_B the transpose differentiates ⊚'s coefficients and the density, not the connection. **H5:** conjugation in the full matrix algebra suffices; no Spin(7,7) restriction on ε is needed. **H6:** K½ and K1 give different field equations at a fixed numerical κ₁; they agree after reparametrizing κ₁, and C1/C2 are unaffected.
  6. **New register rows:** G (bracketed products read as ordinary matrix products, which mix bracket modes), D (d_B on T as the adjoint derivative or as left multiplication), F (which fields vary), S0 (evaluation at s = 0), E (equality as definition of Υᴮ or as a variational claim), Q (trace/reality/pairing convention), and Bd (boundary and analytic setting).
  7. **New contextual conflict 9:** (8.3) on p. 42 writes Cl(T\*X) where the surrounding text uses Y.

Plan: `docs/superpowers/plans/2026-10-16-b07-variation.md`, rev 1.1 (`be2ae34`), Task 1.

**Independence caveat.** The transcriber also wrote the plan's smoke version of `variation.py` and has seen its smoke results (trivial C1 kernels in 4D, three 14D witnesses). The hand derivations below are derived from the printed text and standard calculus of variations, not copied from runner output, but they are not a blind prediction. The blind reading in Task 2 and Codex's independent re-derivation in Task 4 supply the independent checks.

## Source

- **The PDF.** Same as B01–B05: GU, *Author's Working Draft v1.0*, April 1, 2021. SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, re-verified 2026-10-16. Printed page numbers equal one-based PDF pages.
- **How the pages were read.** Pages 41–47 were rendered at 150 dpi with PyMuPDF and read as images. Text extraction was used only as a cross-check; it loses ⊚, ϖ, the bars and the layout of the displays.
- **Cross-references followed (P11):**
  - ⊚ → (8.1) p. 41, Definition 8.1 p. 42, (9.2)–(9.3) p. 43, and B02's transcription of the appendix (12.26)–(12.27);
  - A_ω, B_ω, T_ω → (6.22), (7.3) (as recorded in `experiments/B05/transcription.md`), and item 4 of the (9.4) "where" list;
  - the fermionic display (9.16) → `experiments/B05/transcription.md`, which this file reuses verbatim;
  - the curvature identity d_A∘d_Aφ = [F_A∧φ] → p. 47 (§10).

  Looked for, and **not found** in pp. 36–47 or the appendix as recorded by B02/B05:
  - an expansion of F_{B+T} in terms of F_B, d_BT and T;
  - a statement of how [·,·] acts on a pair of ad-valued **1-forms** (graded or ungraded);
  - the written fermionic action (only "operators like" (9.16) and the compiled variation (9.18) are printed);
  - a definition of ⟨·,·⟩ between a 1-form and an (d−1)-form;
  - a definition of the adjoints d\*_A, ⊚\* used in (9.12)–(9.15).

## Verbatim

### §8, p. 41

$$\circledcirc_\varepsilon\eta=*^n\, i^{\frac{1\pm1}{2}}\big[(\varepsilon^{-1}\Phi_r\varepsilon)\wedge *^m\eta\big]_\pm\tag{8.1}$$

"or perhaps a sum of such terms, where typically Φ_r is a normed Lie Algebra Valued r-form valued in an invariant subspace of the structure group of the tangent bundle and the bracket is either a commutator or an anti-commutator with a factor of i out front in the case of the latter."

### §9.1, pp. 43–45

"The purely Bosonic portion of the action is a real valued function:"

$$\mathcal I_1^{\mathrm B}:\mathcal G\times\mathcal{MET}(X^{1,3}):\longrightarrow\mathbb R\tag{9.1}$$

"While there are other possibilities to explore for the choice of the Shiab operator, Let"

$$\circledcirc_\varepsilon:\Omega^2(Y^{7,7},\mathrm{ad})\longrightarrow\Omega^{d-1}(Y^{7,7},\mathrm{ad})\tag{9.2}$$

"we will begin with one¹⁰ which makes the parallel to Einstein's contraction of the full Riemannian curvature explicit:"

$$\circledcirc_\varepsilon\xi=\underbrace{\big[(\varepsilon^{-1}\Phi^1\varepsilon)\wedge(*\xi)\big]}_{\text{Ricci Like}}-\frac{*}{2}\big[\underbrace{(\varepsilon^{-1}\Phi^1\varepsilon)}_{g_{\mu\nu}\text{- like.}}\wedge*\underbrace{\big[(\varepsilon^{-1}\Phi^2\varepsilon)\wedge(*\xi)\big]}_{\text{Ricci Scalar Like}}\big]\tag{9.3}$$

"for a gauge covariant ad-valued 2-form ξ ∈ Ω²(Y, ad)." Footnote 10 (p. 43): "The Shiab operator that he settled on (but cannot yet now locate) was chosen for its properties relative to the Bianchi identity."

p. 44: "… an action I₁ᴮ which for only the Bosonic fields of integral spin (ε, ϖ on Y and ℷ on X) looks like:"

$$\mathcal I_1^{\mathrm B}(\omega_Y,ℷ_X)=\mathcal I_1^{\mathrm B}((\varepsilon_Y,\varpi_Y),ℷ_X)\tag{9.4}$$

**Line 1** (with the printed under/over-brace labels):

$$=\Big\langle\ \overbrace{T_\omega}^{\text{Shifted Torsion}}\ ,\ \underbrace{*}_{\text{Hodge Star}}\Big(\ \overbrace{\circledcirc_\omega}^{\text{Einstein Ricci Shiab}}\Big(\ \underbrace{F_{B_\omega}}_{\text{Metric Curvature}}+\overbrace{\tfrac12\,d_{B_\omega}T_\omega+\tfrac13[T_\omega,T_\omega]}^{\text{C-S Like Terms}}\Big)+\frac{\kappa_1}{2}\underbrace{T_\omega}_{\text{Shifted Torsion}}\Big)\Big\rangle_{\overbrace{g_ℷ}^{\text{Zorro Metric}}}$$

**Lines 2–4:**

$$=\int_Y\mathrm{Tr}\Big((\varpi-\varepsilon^{-1}d_0\varepsilon)\wedge*\big(\underbrace{[(\varepsilon^{-1}\Phi^1\varepsilon)\wedge(*(\cdot))]}_{\text{Ricci Like}}-\frac{*}{2}[(\varepsilon^{-1}\Phi^1\varepsilon)\wedge*\underbrace{[(\varepsilon^{-1}\Phi^2\varepsilon)\wedge(*(\cdot))]}_{\text{Ricci Scalar Like}}]\big)$$
$$\big(\varepsilon^{-1}\widetilde{R^\theta_{ij\sigma}}\varepsilon+\tfrac12(d_0+\varepsilon^{-1}d_0\varepsilon)(\varpi-\varepsilon^{-1}d_0\varepsilon)+\tfrac13[\varpi-\varepsilon^{-1}d_0\varepsilon,\varpi-\varepsilon^{-1}d_0\varepsilon]\big)\Big)$$
$$+\kappa_1\int_Y\mathrm{Tr}\big((\varpi-\varepsilon^{-1}d_0\varepsilon)\wedge*(\varpi-\varepsilon^{-1}d_0\varepsilon)\big)$$

"where:
1. R̃^θ_{ijσ} is the Spinor bundle's Riemannian curvature induced from the Levi-Civita connection.
2. T_ω = ϖ − ε⁻¹d₀ε ∈ Ω¹(Y, ad) is the augmented torsion tensor.
3. The Shiab Operator ⊚_ω on an ad-valued 2-form ξ ∈ Ω²(Y, ad)is given in accordance with the Einsteinian contraction

   ⊚_εξ = [(ε⁻¹Φ¹ε) ∧ (∗ξ)] (underbrace "Ricci Like") − (∗/2)[(ε⁻¹Φ¹ε) ∧ ∗[(ε⁻¹Φ²ε) ∧ (∗ξ)]] (underbrace "Ricci Scalar Like"; the g_{μν}-like annotation of (9.3) is absent here)
4. The B_ω connection is the gauge rotation of the Levi-Civita Spin Connection: B_ω = ∇⁰ + ε⁻¹d₀ε"

"By the calculus of variations we obtain Euler-Lagrange Equations of the form:"

$$d\mathcal I_1^B(ℷ,\omega)|_{Y^{14}}=\begin{pmatrix}\Upsilon_\omega\\ \oplus\\ \Xi_\omega\end{pmatrix}\in\begin{matrix}\Omega^{d-1}(\mathrm{ad})\\ \oplus\\ \Omega^{d}(\mathrm{ad})\end{matrix}\tag{9.5}$$

"where generally"

$$\Xi=\mathfrak D_\omega\Upsilon_\omega\tag{9.6}$$

"for some operator differential 𝔇_ω so that the vanishing of Ξ_ω = 0 need not be considered if Υ_ω = 0 by the redundant nature of the second equation."

p. 45: "And by gathering up terms we can express them in a fashion that is closer to the more familiar equations of General Relativity. Thus we have:"

$$\frac{\partial\mathcal I_1^{\mathrm B}((\varepsilon_Y,\varpi_Y+s\alpha),ℷ_X)}{\partial s}=\langle\alpha,\circledcirc_\omega F_{A_\omega}+*\kappa_1T_\omega\rangle=\langle\alpha,\Upsilon^B_\omega\rangle\tag{9.7}$$

$$\underbrace{\circledcirc F_\omega}_{\substack{\text{Swerved Curvature}\\=\ \text{Swervature}=\mathcal S_\omega}}=\underbrace{-*\kappa_1\underbrace{T_\omega}_{\text{Displaced Torsion}}}_{\text{Displasion}=\mathcal T_\omega}\tag{9.8}$$

$$\Upsilon_\omega=\mathcal S_\omega-\mathcal T_\omega=0\tag{9.9}$$

$$\underbrace{\underbrace{\mathcal S_\omega}_{R_{\mu\nu}-\frac s2 g_{\mu\nu}}=\underbrace{\mathcal T_\omega}_{\Lambda g_{\mu\nu}}}_{T_{\mu\nu}}\tag{9.10}$$

### §9.2, p. 45

"To this end we focus on second Lagrangian of 2nd order:"

$$\mathcal I_2^{\mathrm B}((\varepsilon_Y,\varpi_Y),ℷ_X)=\|\Upsilon^B_\omega\|^2\tag{9.11}$$

$$\frac{\partial\mathcal I_2^{\mathrm B}((\varepsilon_Y,\varpi_Y+s\alpha),ℷ_X)}{\partial s}=\langle\alpha,2(d^*_{A_\omega}\circledcirc^*_\omega+\kappa_1\mathrm{Id})\Upsilon^B_\omega\rangle\tag{9.12}$$

$$=2\langle\alpha,\ \underbrace{d^*_{A_\omega}\circledcirc^*_\omega\circledcirc_\omega F_{A_\omega}}_{\text{New `Yang-Mills' Term}}+\kappa_1d^*_{A_\omega}\circledcirc^*_\omega T_\omega+\kappa_1*\circledcirc_\omega F_{A_\omega}+\kappa_1^2T_\omega\rangle\tag{9.13}$$

"yielding"

$$\underbrace{\mathbf D^*_\omega F_{A_\omega}=J^B_\omega}_{\text{Yang-Mills-Maxwell like equation with Bosonic source.}}\tag{9.14}$$

"but more efficiently as"

$$\mathcal D^*_\omega\Upsilon_\omega=0\tag{9.15}$$

"which is more natural within Geometric Unity."

### §9.3, pp. 46–47

(9.16)–(9.19) and their surrounding sentences are transcribed verbatim in `experiments/B05/transcription.md` § "The operator, p. 46", re-read here from the p. 46 image with no disagreement. They are reproduced so that H7 can cite them:

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

$$\not{\mathcal D}^F_\omega\begin{pmatrix}\zeta\\ \nu\end{pmatrix}_{\rho(\varepsilon^{-1})}=\not{\mathcal D}_\omega\chi_{\varepsilon^{-1}}=0 \tag{9.17}$$

"Let us compile the Bosonic and Fermionic variations of the Spinorial Lagrangian terms in a single term:"

$$\Upsilon^F=*\begin{pmatrix} d_{A_\omega}\nu+*\circledcirc d_{A_\omega}\zeta\\ \oplus\\ d^*_{A_\omega}\zeta\\ \oplus\\ \bar\nu\zeta+\bar\zeta\nu+\circledcirc\bar\zeta\zeta\end{pmatrix}\tag{9.18}
\qquad
\Upsilon^F_\omega\in\begin{pmatrix}\Omega^{d-1}(Y,\$)\\ \oplus\\ \Omega^{d}(Y,\$)\\ \oplus\\ \Omega^{d-1}(Y,\mathrm{ad})\end{pmatrix}\tag{9.19}$$

"as a kind of 1-form on some SuperSpace-like structure over 𝒜:" … "which can be combined with the variation of either a first or second order purely Bosonic Lagrangian so as to form:"

$$\Upsilon_\omega=\Upsilon^B_\omega+\Upsilon^F_\omega=0\quad\text{or}\quad\mathcal D\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega\tag{9.20}$$

(The second alternative is printed "𝒟ω\*Υᴮ_ω" with ω at baseline, not as a subscript.)

p. 47: "… we choose to view 'wedging' with Υ_ω as the application of a zeroth order operator and ask if it possesses a non-trivial square root the in form of a first order differential operator δ^ω so that:"

$$\Upsilon_\omega=0\ \text{ and }\ \sqrt{\Upsilon_\omega}=\delta^\omega\ \rightsquigarrow\ (\delta^\omega)^2=0\ \rightsquigarrow\ \text{Cohomology}\tag{9.21}$$

$$\Upsilon_\omega=(\delta^\omega)^2=\delta^\omega_2\circ\delta^\omega_1=0\tag{9.22}$$

"of a geometrically meaningful cohomology complex." §10, p. 47: "In a certain sense, one can view the usual (twisted) DeRahm complex as the square root of the of the curvature as d_A ∘ d_Aφ = [F_A ∧ φ]."

## Conventions

| Item | Value used | Source / status |
|---|---|---|
| A_ω, B_ω, T_ω | A = ∇⁰ + ϖ; B = ∇⁰ + ε⁻¹d₀ε; T = ϖ − ε⁻¹d₀ε, so **A = B + T** | (6.22), (7.3), (9.4) items 2 and 4 `[GU-orig]` |
| F_A | F_{B+T} = F_B + d_BT + T∧T (matrix product in the Clifford factor, wedge in the form factor) | standard curvature of a connection shifted by an ad-valued 1-form; not printed in the draft `[std]` |
| F_B | B is the ε-gauge rotation of ∇⁰, so F_B = ε⁻¹F_{∇⁰}ε; line 2's ε⁻¹R̃ε is this | (9.4) item 4 and line 2 `[GU-orig]` |
| d_B in line 2 | printed (d₀ + ε⁻¹d₀ε)(ϖ − ε⁻¹d₀ε), i.e. d_B with ∇⁰ written d₀ | (9.4) line 2; "A₀ ≈ ∇⁰ ≈ d₀" p. 36 `[GU-orig]` |
| [T, T] | **not defined for ad-valued 1-forms.** Three readings: **N0** an ungraded commutator of the whole form-valued product, [x,y] = x∧y − y∧x, giving [T,T] = T∧T − T∧T = 0 (rev 1.1, per Grok's review: this is **not** the coefficient-wise extension of (12.26), which wedges the forms and takes ab − ba of the coefficients and gives [T,T] = 2T∧T, i.e. N2 and `gu.cliffform.bracket` mode C; (12.26) defines the bracket on coefficients only, so neither extension is forced); **N1** b(x,y) = ½[x∧y]\_graded, so b(T,T) = T∧T (the Chern–Simons-consistent reading); **N2** the graded commutator [x∧y] = x∧y + y∧x on 1-forms, so [T,T] = 2T∧T. p. 47's d_A∘d_Aφ = [F_A∧φ] does not decide between them: F_A has degree 2, so the grading sign is +1 for every φ | (12.26) p. 66; branch, see register |
| ⊚_ω | a member of B02's Shiab family (9.3), with the dressing ε⁻¹Φε; ⊚_ε = Ad(ε⁻¹)∘⊚∘Ad(ε) (H5) | (9.3), B02 `[GU-orig]` / `[GU-recon]` for the family |
| ⟨·,·⟩ in (9.4) | the metric trace pairing ⟨a, b⟩ = ∫Tr(a∧∗b) of same-degree forms, metric g_ℷ | "Zorro Metric" label `[GU-recon]` |
| ⟨·,·⟩ in (9.7) | pairs a 1-form α with an (d−1)-form: ∫Tr(α∧·) | (9.7) degrees `[GU-recon]` |
| "Tr" | trace on 𝔲(64,64) ⊂ Cl_ℂ(7,7) = ℂ(128); represented in code by the scalar Clifford coefficient (Tr/2^{n/2}) | (8.4) `[GU-recon]` |
| Hodge star | pinned (`gu/forms.py`): a∧∗b = ⟨a,b⟩vol, ∗∗ = (−1)^{k(n−k)+q} | spec rev 4.1 `[std]` |
| ∗∗ on (n−1)-forms | (−1)^{(n−1)+q} = **+1** at (3,1), (1,3), (7,7), (9,5) | computed |
| ∗ on 1-forms | an **anti-isometry**: ⟨∗a, ∗b⟩ = (−1)^q⟨a,b⟩ = −⟨a,b⟩ at all four signatures (q odd), checked with `gu.forms.inner`/`hodge` on every basis 1-form | computed; used in H8 |
| the κ term | line 1: (κ₁/2)T inside the outer ∗; line 2: κ₁∫Tr(T∧∗T) | printed conflict 1 |

## Printed conflicts (recorded, not repaired)

1. **The κ normalization.** (9.4) line 1 has κ₁/2; the expanded line 4 has κ₁. Under the metric pairing, (κ₁/2)⟨T,T⟩ varies to κ₁⟨α,T⟩, which is (9.7)'s coefficient; κ₁⟨T,T⟩ varies to 2κ₁⟨α,T⟩ (H6).
2. **(9.4) line 1 and lines 2–4 are both degree-inconsistent as printed.**
   - Line 1: the outer ∗ encloses ⊚(…) + (κ₁/2)T. ⊚(…) is an (d−1)-form by (9.2) and T is a 1-form, so the sum has no single degree for d = 14. Reading V repairs this by moving the κ term outside the ∗: ⟨T, ∗⊚(…)⟩ + (κ₁/2)⟨T, T⟩ `[GU-recon]`.
   - Line 2: Tr(T ∧ ∗(⊚(…))) is T (degree 1) wedged with ∗ of an (d−1)-form, a 1-form: a 2-form, not a top form. The integrand is not integrable over Y¹⁴. (Taking the outer ∗ as the metric pairing's ∗ and dropping the ∗ on ⊚'s output, or vice versa, repairs it; both give V.)
3. **(9.4) against (9.7).** (9.7) puts ∗ on the torsion term only, ⟨α, ⊚F + ∗κ₁T⟩, and pairs a 1-form with an (d−1)-form. (9.4) line 1 uses the metric pairing of same-degree forms with ∗ on everything. Under V and the pinned convention these agree: ⟨T, ∗ω⟩ = ∫Tr(T∧∗∗ω) = ∫Tr(T∧ω) for ω ∈ Ω^{d−1}, exactly, at all four signatures.
4. **(9.12) against (9.13).** Expanding (9.12) with Υᴮ = ⊚F + ∗κ₁T gives d\*⊚\*⊚F + κ₁d\*⊚\*∗T + κ₁⊚F + κ₁²∗T, which differs from (9.13) in the ∗ on terms 2, 3 and 4. H8 derives the variation and compares term by term.
5. **(9.18) third component, degree.** ν̄ζ and ζ̄ν are spinor bilinears of a 0-form and a 1-form (degree 1); ⊚ζ̄ζ applies ⊚ (Ω² → Ω^{d−1} on ad-valued forms) to a degree-2 bilinear (degree d−1). They cannot be summed, and after the outer ∗ only the first two land in Ω^{d−1}(ad) as (9.19) claims. This is B05-Y's per-occurrence degree conflict seen in (9.18).
6. **(9.18) has three components; there are four independent fermion fields.** p. 46 calls ν̄, ζ̄, ν, ζ "four distinct fields". Varying a Lagrangian bilinear in (barred, unbarred) gives one equation per field: four spinor equations. (9.18) lists two spinor components, which are (at most) the ζ̄- and ν̄-variations. The ν- and ζ-variations (equations for the barred fields) are absent (H7).
7. **The fermionic Lagrangian is not written.** §9.3 prints operators "like" (9.16) and the compiled variation (9.18), but no action integral, pairing or measure. Every fermionic variation in H7 is therefore relative to a reconstructed action.
8. **(9.20) second alternative** (rev 1, restated). "𝒟ω\*Υᴮ_ω = Υ^F_ω" applies an operator 𝒟ω\* that is not defined in §9 to Υᴮ ∈ Ω^{d−1}(ad) and equates the result with Υ^F, an element of the mixed direct sum (9.19). The glyph resembles (9.15)'s 𝒟\*_ω, not (9.6)'s 𝔇_ω, and nothing identifies it with either. The open issue is the undefined operator and the embedding of a bosonic quantity into the bosonic–fermionic sum, not a specific degree mismatch. (Rev 0's degree-d claim relied on an unsupported identification with (9.6) and is withdrawn.)
9. **(8.3), p. 42 (context).** ϑ : Λ\*(T\*Y) → Cl(T\*X) = ℝ(128) writes X in the target where the surrounding discussion and (8.4) use Y. No effect on B07.

## Readings register

| ID | Reading | Class | Can change | Executed here |
|---|---|---|---|---|
| B07-V | Line 1 with the κ term moved outside ∗: I₁ = ⟨T, ∗⊚(F_B + ½d_BT + ⅓[T,T])⟩ + (κ₁/2)⟨T,T⟩, metric trace pairing, compact support, ε and metric fixed | explicit repair `[GU-recon]` | — (reference reading) | **yes** |
| B07-L1 | Line 1 literally (∗ over ⊚(…) + κT) | source, ill-typed (conflict 2) | everything | no: not a well-defined functional |
| B07-L2 | Lines 2–4 literally | source, ill-typed (conflict 2) | everything | no |
| B07-P | (9.7)'s ⟨·,·⟩ read as the metric pairing of α with ∗(…) instead of the wedge pairing | different convention | nothing, at the four signatures (∗∗ = +1 on Ω^{n−1}) | no (shown equivalent by hand) |
| B07-S | An action built from a symmetric operator, e.g. ½(L + L†) | different model | C1 (removes it) but not the target | no. The quadratic functional ½∫Tr(T∧LT) already equals ½∫Tr(T∧½(L+L†)T) modulo boundary terms (L† as in H2), so symmetrizing the action does not change its variation and cannot produce the unsymmetrized target ⟨α, LT⟩. Making (9.7) follow requires changing the **target** to ½(L+L†)T. |
| B07-T | "⊚ᵀ in place of ⊚" | ill-typed | — | no: the wedge transpose of ⊚ : Λ² → Λ^{n−1} is Λ¹ → Λ^{n−2} |
| B07-Y | A ⊚ that differs per occurrence (in the quadratic term, the cubic term, and the target) | different model (B05-Y analogue) | C1, C2 | no |
| B07-R | Variations restricted to a subspace of Ω¹(Y, ad) (e.g. a Spin-invariant subspace, or the (12.21) mass block) | different model; the source's translation space is all of Ω¹(Y, ad) (p. 44 item 2) | C1, C2 | no |
| B07-O | The author's lost preferred operator (fn. 10, p. 43) instead of (9.3) | untested, unavailable | C1, C2 | no |
| B07-M | Sums mixing bracket modes, allowed by (8.1)'s "or perhaps a sum of such terms" but outside B02's fixed-mode family | untested | C1, C2 | no (family is per mode) |
| B07-N0 / N1 / N2 | The [T, T] normalization (Conventions) | source ambiguity | C2 only | N1 and N2 yes; **N0 no** (see note) |
| B07-K½ / K1 | κ₁/2 (line 1) or κ₁ (line 4) | source conflict 1 | κ normalization only | by hand (H6) |
| B07-G | Bracketed products in (9.3) read as **ordinary** matrix products (grouping), not as a commutator or i·anticommutator. With C(a,b) = ab − ba and A(a,b) = i(ab + ba), ab = (C − iA)/2, so nested ordinary products expand into a combination of bracket modes; it also needs a reality/ad-closure convention, since a product of two Lie-algebra elements need not lie in the Lie algebra | different completion, within M | C1, C2 | no: the eight fixed-mode surveys do **not** cover it; it would need a combined-mode adapter |
| B07-D | In lines 2–4, (d₀ + ε⁻¹d₀ε)T read as the induced adjoint covariant derivative (d_B) or as left multiplication | notation ambiguity; the compact d_B and T ∈ Ω¹(ad) favour the adjoint derivative | zeroth-order part of R₁ only | adjoint derivative assumed; C1 is the same for both (same principal symbol), so C1 witnesses reject either |
| B07-F | Which fields vary: ϖ only (this plan) or the full system with ε and the metric | scope | additional equations | ϖ only; (9.6)'s redundancy assertion supplies no metric equation |
| B07-S0 | (9.7)'s derivative evaluated at s = 0 (not printed); alternatives: at every s along the line, or (literal) equality for all s with a fixed right side | convention | nothing at s = 0; the literal all-s reading is a stronger, generally false claim for a nonlinear action | s = 0 (equivalently, the identity at every base point) |
| B07-E | (9.7)'s last equality defines Υᴮ; its first equality is still an asserted variational identity ("By the calculus of variations", "gathering up terms") | reading of the claim | what may be concluded | the first equality is what is tested |
| B07-Q | The trace/reality/pairing convention: bilinear trace (assumed), its real part, a Hermitian pairing, or changed degree-dependent signs | convention | C1, C2 (other than a common nonzero scale), H8 signs | bilinear trace only; a different convention must be specified, with consistent adjoints, before claiming coverage |
| B07-Bd | Boundary terms and the analytic setting (not given in the source) | scope | nothing for C1: interior compactly supported variations already expose a bulk principal-symbol defect | compact support |
| B07-X | A Shiab operator whose Φ depends on ϖ or other fields | different model (related to Y, O) | adds δ⊚ terms | no: (9.3) with fixed invariant Φ and fixed metric is independent of ϖ |

**Note on N0.** Under N0 the cubic term vanishes identically, so the "C-S like terms" are not Chern–Simons-like, and C2 reduces to −Tr(α∧⊚(T∧T)). N0 cannot rescue (9.7): C1 does not involve the bracket, so any C1 failure stands under N0. The code does not execute N0; adding it would only fill in C2's value under a reading in which C2 is not needed for the verdict. This is reported to the user per the plan's Task 2 Step 3 rule. Grok's review of Task 3 (rev 1.1) agrees with the rescue claim and with H3's N0 residual, ranks the readings N1 > N2 ≫ N0, and notes that N0 makes the cubic summand of the braced "C-S Like Terms" vanish identically (½d_BT remains), against the printed label: a degenerate literalization.

## Hand derivations

Throughout: fix ε and the metric. Then B = B_ω, F_B, the Hodge star, Φ¹, Φ² and the dressing are fixed; only ϖ moves, with δϖ = α ∈ Ω¹_c(Y, ad). So δT = α, δA = α, δF_A = d_Aα. ⟨T, ∗ω⟩ = ∫Tr(T∧ω) for ω ∈ Ω^{n−1} (Conventions). Under V,

$$I_1=\int\mathrm{Tr}\big(T\wedge\circledcirc F_B\big)+\tfrac12\int\mathrm{Tr}\big(T\wedge LT\big)+\tfrac13\int\mathrm{Tr}\big(T\wedge\circledcirc b(T,T)\big)+\tfrac{\kappa_1}{2}\langle T,T\rangle,\qquad L:=\circledcirc\circ d_B .$$

The target (9.7), evaluated at s = 0 (B07-S0), is ∫Tr(α∧⊚F_A) + κ₁⟨α, T⟩ = ∫Tr(α∧⊚F_B) + ∫Tr(α∧LT) + ∫Tr(α∧⊚(T∧T)) + κ₁⟨α,T⟩. Both sides are polynomials in T; compare them order by order.

### H1, order T⁰

δ∫Tr(T∧⊚F_B) = ∫Tr(α∧⊚F_B), since F_B and ⊚ are fixed. This is the target's order-T⁰ term. **Matches.**

### H2, order T¹

δ[½∫Tr(T∧LT)] = ½∫Tr(α∧LT) + ½∫Tr(T∧Lα). Define L† by ∫Tr(T∧Lα) = ∫Tr(α∧L†T) for compactly supported α, T. Then the variation is ½∫Tr(α∧(L + L†)T), and subtracting the target's ∫Tr(α∧LT) leaves the **residual**

$$R_1(\alpha,T)=\tfrac12\int\mathrm{Tr}\big(\alpha\wedge(L^\dagger-L)T\big).$$

This holds with variable coefficients: derivatives of ⊚'s coefficients and of the density are part of L†. (The connection term in d_B is zeroth order and is transposed algebraically; no derivative of B arises.)

**Principal symbol.** In a local frame, d_Bα = Σ_k e^k∧∂_kα + (zeroth order). Put M^k(t, a) := Tr(t∧⊚(e^k∧a)), a pointwise bilinear form on ad-valued 1-forms. Then ∫Tr(T∧Lα) = Σ_k∫M^k(T, ∂_kα) + (zeroth order in α). Integrating by parts **at the level of coefficient functions** (∫f∂_kg = −∫(∂_kf)g, with derivatives of M^k and of the density being zeroth order), this is −Σ_k∫M^k(∂_kT, α) + (zeroth order in T). No sign from moving d across forms arises, because d is never moved across a form: only scalar coefficient functions are differentiated. So in the residual, the coefficient of ∂_kT is

$$-\tfrac12\big(M^k(\cdot,\alpha)+M^k(\alpha,\cdot)\big),$$

identically in odd and even dimension.

**Claim.** If R₁(α, T) = 0 for all compactly supported α, T, then for every k, t, a:

$$C1(k;t,a)=\mathrm{Tr}\big(t\wedge\circledcirc(e^k\wedge a)\big)+\mathrm{Tr}\big(a\wedge\circledcirc(e^k\wedge t)\big)=0 .$$

*Proof.* R₁(α, T) = ∫Tr(α∧PT) with P a first-order differential operator. R₁ ≡ 0 for all α forces P = 0 (the trace pairing is nondegenerate). Then for any function f, 0 = P(fT) − fP(T) = σ_P(df)T, where σ_P(ξ) = −½Σ_kξ_k S^k and S^k is the matrix of C1(k; ·, ·). Choosing f with df = e^k at a point gives S^k = 0. ∎

**Scope.**
- C1 is **necessary** for (9.7) under V. A nonzero C1 rejects (9.7) under V regardless of curvature, coefficient derivatives, or whether ε is constant on Y. "ε fixed" means fixed under the variation, not constant; nothing above uses constancy.
- C1 = 0 alone would **not** prove R₁ ≡ 0: the zeroth-order part of P would remain.
- C1 depends on ⊚ only through its value at a point, so it can be evaluated on the flat model (B = d, ε = 1) after H5 removes the dressing.
- The Chern–Simons controls (H4) validate the algebraic signs of this reduction, not the geometric argument; that argument is carried here by hand.

### H3, order T²

δ[⅓∫Tr(T∧⊚b(T,T))] = ⅓∫Tr(α∧⊚b(T,T)) + ⅓∫Tr(T∧⊚(b(α,T) + b(T,α))). For N1 and N2, b is symmetric on 1-forms (the graded commutator of two 1-forms is x∧y + y∧x), so this is ⅓∫Tr(α∧⊚b(T,T)) + ⅔∫Tr(T∧⊚b(α,T)). The target's order-T² term is ∫Tr(α∧⊚(T∧T)). The order-T² variation has no derivatives, so the residual vanishes for all α, T iff, pointwise,

$$C2(\alpha;T)=\tfrac13\mathrm{Tr}\big(\alpha\wedge\circledcirc b(T,T)\big)+\tfrac23\mathrm{Tr}\big(T\wedge\circledcirc b(\alpha,T)\big)-\mathrm{Tr}\big(\alpha\wedge\circledcirc(T\wedge T)\big)=0 .$$

- **N1** (b(T,T) = T∧T): C2 = ⅓Tr(α∧⊚(T∧T)) + ⅓Tr(T∧⊚(α∧T + T∧α)) − Tr(α∧⊚(T∧T)).
- **N2** (b(T,T) = 2T∧T): every b doubles, so C2 = ⅔Tr(α∧⊚(T∧T)) + ⅔Tr(T∧⊚(α∧T + T∧α)) − Tr(α∧⊚(T∧T)).
- **N0** (b ≡ 0 on the diagonal, antisymmetric): C2 = −Tr(α∧⊚(T∧T)).

C2 is quadratic in T; the code polarizes it (T = tᵢ + tⱼ minus the diagonal parts) to get a trilinear form whose vanishing on basis triples is equivalent.

### H4, the Chern–Simons controls (3D, ⊚ = id, Clifford factor of Cl(3,0))

With ⊚ = id, I₁'s T-dependent part is ∫Tr(½T∧dT + ⅓T∧b(T,T)). Under N1 this is ½∫Tr(T∧dT + ⅔T∧T∧T), half the Chern–Simons functional, whose variation is ∫Tr(α∧(dT + T∧T)): the target's T¹ and T² terms.
- **C1 = 0.** M^k(t, a) = Tr(t∧e^k∧a). Moving the 1-form a past the 2-form t∧e^k under the graded-cyclic trace gives Tr(a∧t∧e^k) (sign (−1)^{1·2} = +1), and swapping the 1-forms t and e^k gives −Tr(a∧e^k∧t) = −M^k(a, t). So C1 = 0.
- **C2 (N1) = 0.** Graded cyclicity for three 1-forms gives Tr(T∧α∧T) = Tr(T∧T∧α) = Tr(α∧T∧T). So C2 = (⅓ + ⅓ + ⅓ − 1)Tr(α∧T∧T) = 0.
- **C2 (N2) ≠ 0.** C2 = (⅔ + ⅔ + ⅔ − 1)Tr(α∧T∧T) = Tr(α∧T∧T), nonzero for suitable α, T (for example where the Clifford product of the three factors has a scalar part).

These are the executable controls `test_chern_simons_control_c1`, `test_chern_simons_control_c2_n1` and `test_chern_simons_impostor_n2`.

### H5, the dressing

For each bracket mode, conjugation by ε is an algebra automorphism of the Clifford factor and commutes with ∗ (which acts on the form factor) and with both brackets ([·,·] and i{·,·}). So [(ε⁻¹Φε)∧∗ξ] = ε⁻¹[Φ∧∗(εξε⁻¹)]ε, and the nested second term transforms the same way. Hence

$$\circledcirc_\varepsilon=\mathrm{Ad}(\varepsilon^{-1})\circ\circledcirc\circ\mathrm{Ad}(\varepsilon)$$

pointwise. With the trace's conjugation invariance, C1 for ⊚_ε at (t, a) equals C1 for ⊚ at (Ad(ε)t, Ad(ε)a), and the same holds for C2. Ad(ε) is invertible, so the vanishing of C1 and C2 does not depend on ε. Nothing here uses constancy of ε, and the (6.4)/(6.13) sign does not enter: the variation is in ϖ at fixed ε, and B = ∇⁰ + ε⁻¹d₀ε is fixed whichever sign the tilted map carries. *Assumption:* ε acts on the Clifford coefficients by conjugation in the full matrix algebra, preserving the chosen real adjoint space `[GU-recon]`; ε ∈ ℋ (p. 42), and no restriction to the Spin(7,7) image is needed.

### H6, the κ term

The pairing ⟨a, b⟩ = ∫Tr(a∧∗b) is symmetric on same-degree forms. So δ[(κ₁/2)⟨T,T⟩] = κ₁⟨α, T⟩ = κ₁∫Tr(α∧∗T), which is (9.7)'s torsion term. **Matches under K½.** Under K1 (line 4's κ₁⟨T,T⟩) the variation is 2κ₁⟨α,T⟩: the κ coefficient in (9.7) is off by a factor 2. At a fixed numerical κ₁ the two field equations ⊚F + κ₁∗T = 0 and ⊚F + 2κ₁∗T = 0 differ; they agree after reparametrizing κ₁. C1 and C2 are unaffected.

### H7, the fermionic conditional ledger

*Rev 1 note.* The omitted barred-field equations are a completeness concern, not evidence that the two displayed spinor equations are false. The relative minus sign of rows 3–4 matters for a packaged variational one-form even though it changes no solutions of a standalone equation.

**Not a computation.** The fermionic action is not printed (conflict 7). Take the reconstruction S_F = ∫⟨Ψ̄, 𝒟̸_ω Ψ⟩ with Ψ = (ζ₊, ζ₋, ν₊, ν₋)_{ρ(ε⁻¹)} and Ψ̄ = (ζ̄₋, ζ̄₊, ν̄₋, ν̄₊)_{ρ(ε)} as four independent fields `[GU-recon]`. Every entry below is conditional on the listed B05-Q inputs. A spinor-valued ⊚ is a different map from the ad-valued ⊚ that C1 tests, so no C1 or C2 result transfers to this ledger.

| Varied field | Terms of (9.16) it multiplies | Needs (formal adjoints, pairings, bilinears) | Unresolved B05 inputs | Compared with (9.18) |
|---|---|---|---|---|
| ζ̄ (rows 1–2) | ∗⊚ϖ₊₊ζ₊ + ∗⊚(d₀+ϖ₊₋)ζ₋ + ϖ₊₊ν₊ + (d₀+ϖ₊₋)ν₋, and the row-2 analogue | a spinor-form pairing ⟨ζ̄, ·⟩ on 1-forms; ⊚ on **spinor**-valued 2-forms; the blocks ϖ₊₊, ϖ₊₋, … assembling into the action of ϖ, so that d₀ + ϖ = d_A blockwise | B05-Q (bar/pairing), B05-Y (⊚ on spinors), B05-A (how ϖ acts), B05-T′ (derivatives vs. ρ decorations) | component 1, d_Aν + ∗⊚d_Aζ: **follows under** those hypotheses (degree 1, then the outer ∗ gives Ω^{d−1}($) as (9.19) says) |
| ν̄ (rows 3–4) | −ϖ̄\*₊₊ζ₊ + (−d₀\* − ϖ̄\*₊₋)ζ₋, and the row-4 analogue | d₀\* the formal adjoint of d₀ under the spinor-form pairing; ϖ̄\* the adjoint of ϖ's action, so that d₀\* + ϖ̄\* = d\*_A | B05-Q, B05-V (the barred potential), B05-K (whole-block adjoint) | component 2, d\*_Aζ: **follows up to an overall sign** (rows 3–4 carry minus signs; (9.18) prints none) under those hypotheses; degree 0, outer ∗ gives Ω^d($) |
| ζ (columns 1–2) | ζ̄₋∗⊚ϖ₊₊ + ζ̄₊∗⊚(d₀+ϖ₋₊) − ν̄₋ϖ̄\*₊₊ − ν̄₊(d₀\*+ϖ̄\*₋₊), transposed | the transposes of ∗⊚, d₀ and d₀\* under the spinor-form pairing | B05-Q, B05-K | **absent from (9.18)** (conflict 6): this is the equation for the barred fields. It would coincide with a (9.18) row only under a reality condition tying barred to unbarred fields, which p. 46 explicitly does not impose ("four distinct fields") |
| ν (columns 3–4) | ζ̄₋ϖ₊₊ + ζ̄₊(d₀+ϖ₋₊), transposed | the transpose of d₀ | B05-Q | **absent from (9.18)** (as above) |
| ϖ (bosonic direction) | ζ̄∗⊚(αζ), ζ̄αν, and, if ϖ̄\* depends on ϖ, ν̄ᾱ\*ζ | a spinor-to-ad bilinear (moment map) ψ̄⊗χ ↦ ad; the transpose of ⊚ on spinor forms for the first term; whether ϖ̄\* is ϖ's adjoint (then it varies) or an independent field (then it does not) | B05-Q, B05-V, B05-Y, the bilinear (not defined anywhere) | component 3: the ζ̄ν and ν̄ζ terms **follow under** those hypotheses (degree 1, outer ∗ gives Ω^{d−1}(ad)). The ⊚ζ̄ζ term **does not follow as printed**: the variation of ζ̄∗⊚(αζ) produces a **transpose** of ⊚ applied to the bilinear of ζ̄ and ζ, not ⊚ itself, and its degree conflicts with the other two terms (conflict 5) |
| ε (not varied here) | the ρ(ε), ρ(ε⁻¹) decorations and the dressing | the ℋ-action on $ | B05 (6.13) sign; Lean `lean/B05Sign/` | out of scope (ϖ direction only) |

- **(9.18) by component:** component 1 follows conditionally; component 2 follows conditionally, up to sign; component 3 follows conditionally for two of its three terms, and its ⊚ζ̄ζ term does not follow as printed.
- **(9.20)** is a conditional assembly: Υᴮ + Υ^F = 0 adds (9.7)'s ad component to (9.18)'s third component, which is well typed only for the ζ̄ν, ν̄ζ terms; its second alternative uses an undefined operator (conflict 8).
- **(9.21)–(9.22)** are unproved square-root/complex obligations (δ^ω with (δ^ω)² = Υ_ω); they are B08's subject and are not touched here.

**Summary for the README:** the fermionic variation (9.16)–(9.22) was not computed; it is blocked on B05-Q's open pairing and adjoint conventions, and the ledger above records what each component would need.

### H8, (9.12)/(9.13) bookkeeping

Υᴮ = ⊚F_A + ∗κ₁T (9.7). In the ϖ direction δΥᴮ = ⊚d_Aα + ∗κ₁α (δ⊚ = 0, δF_A = d_Aα, δT = α). With I₂ = ‖Υᴮ‖² = ⟨Υᴮ, Υᴮ⟩:

$$\partial_s\mathcal I_2=2\langle\delta\Upsilon^B,\Upsilon^B\rangle=2\big\langle\alpha,\ (d_A^*\circledcirc^*+\kappa_1*^*)\Upsilon^B\big\rangle,$$

where ⊚\*, ∗\* are metric adjoints and d\*_A is the formal adjoint of d_A. (Symmetry of ⟨·,·⟩ is used; ⟨·,·⟩ is the indefinite metric trace pairing, so ‖·‖² is not a norm.)

- **(9.12) against this.** The printed operator is 2(d\*_A⊚\* + κ₁Id). The derived one is 2(d\*_A⊚\* + κ₁∗\*). "Id" maps Ω^{d−1} to Ω^{d−1} and cannot be paired with the 1-form α under the metric pairing; ∗\* maps Ω^{d−1} → Ω¹. So (9.12)'s Id stands where ∗\* is needed.
- **Expanding the derived form:**

$$(d_A^*\circledcirc^*+\kappa_1*^*)(\circledcirc F_A+\kappa_1*T)=d_A^*\circledcirc^*\circledcirc F_A+\kappa_1d_A^*\circledcirc^*{*T}+\kappa_1*^*\circledcirc F_A+\kappa_1^2*^**T .$$

- **Against (9.13), term by term:**
  1. d\*_A⊚\*⊚F_A: **matches**.
  2. κ₁d\*_A⊚\*∗T derived; (9.13) prints κ₁d\*_A⊚\*T. ⊚\* maps Ω^{d−1} → Ω², so ⊚\*T with T ∈ Ω¹ is ill-typed: (9.13) **drops a ∗**.
  3. Under the pinned convention ∗\* = **−∗** between Ω¹ and Ω^{d−1} (rev 1): for a ∈ Ω¹, u ∈ Ω^{d−1}, ⟨∗a, u⟩ = ⟨∗a, ∗(∗u)⟩ = −⟨a, ∗u⟩, using the anti-isometry and ∗∗ = +1 on Ω^{d−1}. So the derived term is **−κ₁∗⊚F_A**; (9.13) prints **+κ₁∗⊚F_A**. A definite sign disagreement (and not (9.12)'s Id).
  4. κ₁²∗\*∗T = −κ₁²∗∗T = **−κ₁²T** (∗∗ = +1 on Ω¹); (9.13) prints **+κ₁²T**.
- **Conclusion.** Under the pinned pairings the metric gradient of I₂/2 is d\*_A⊚\*⊚F_A + κ₁d\*_A⊚\*(∗T) − κ₁∗⊚F_A − κ₁²T. (9.13) drops a ∗ in term 2 and has the wrong sign in terms 3 and 4; (9.12)'s Id cannot stand for ∗\* = −∗. A different pairing convention changes adjoints, but must change them consistently for every operator and degree; it cannot justify only the last two terms. These are bookkeeping findings about the printed displays, recorded for the README; B07 does not compute the second-order Lagrangian.
