# B07 non-GR channels: derivations E1–E2 and register additions

Plan: `docs/superpowers/plans/2026-10-16-b07-escape.md` (rev 1.1, approved 2026-10-16). Inputs: `experiments/B02/transcription.md` ((8.1), (9.3), P3, P4), `experiments/B02/proofs.md` (dressed covariance), `experiments/B07/transcription.md` (reading V, A = B + T), `experiments/B07/phase2/derivations.md` (H12–H14).

**The question.** The user asked: "What can we do to escape? Outside of Einstein GR". In 4D, Lovelock's theorem says the only symmetric, divergence-free tensor built from a metric and at most its second derivatives is a combination of the Einstein tensor and Λg. So a non-GR answer needs an extra field, higher derivatives, D > 4, or torsion. Grok's review (2026-10-16) kept two channels on GU's own constructions:
- **E1, higher derivatives.** The curvature-squared content of the second-order Lagrangian (9.11).
- **E2, an extra field.** The Weyl response of the dressed operator ⊚_ε of (9.3), with ε as the field.

**Scope.** Everything is at a 4D point, signatures (3,1) and (1,3), on the flat model of Phase 2: B = d, constant coefficients, reading V (ε and the metric fixed, δT = δA). E1 is restricted to T = 0 and to F = ξ(R) with R algebraic. E2 uses a finite, stated dressing family.

**Notation.** As in Phase 2: n = p + q = 4; η = diag(+1 × p, −1 × q); ⟨x, y⟩ = Tr(x∧∗y)/2^{n/2} (`second_order.mpair`); ⊚ is (9.3) with the bracket mode named (CCC, CAA, CAC); ξ: algebraic curvature → Ω²(Cl) is B02's soldering map. 𝓡 is the 20-dimensional space of algebraic curvature tensors. Indices are contracted with η throughout. Scope tags (P1): *identity* = exact, executed or derived; *hand* = derived here, not computed; *counterexample* = an exact witness.

## E1 — the curvature sector of (9.11) at T = 0

### E1.1 The reduction (hand)

(9.11) is I₂ = ⟨Υ, Υ⟩ with Υ = X(F_A) + κ₁∗T (Phase 2 H14). Under reading V, A = B + T, so at T = 0 we have F_A = F_B and Υ = X(F_B). On the flat model with F_B = ξ(R), the pointwise integrand is the quadratic form

$$Q_X(R)=\langle X(\xi R),\,X(\xi R)\rangle,\qquad R\in\mathcal R .$$

- The pairing is bilinear and indefinite (H14). It is not a Hermitian norm, so no sign of Q_X is a positivity statement.
- **The prime column.** The other Hodge convention pairs as ⟨x, y⟩′ = (−1)^{deg y}⟨x, y⟩ (H14). Here y = X(ξR) is an (n−1) = 3-form, so ⟨y, y⟩′ = −⟨y, y⟩ and Q′_X = −Q_X. That is the whole content of the "prime" column: the operator X is held fixed and only the pairing changes. Switching every Hodge star inside (9.3) as well is a different operation. It reparametrizes Φ² (B02 `proofs.md`), and for CAA with fixed (F, B) the fit becomes (0, 0, 1, 9/4), not (0, 0, 1, 1/4). The run never makes that switch.
- **Invariance.** If X is Spin(p,q)-equivariant, Q_X is a Spin-invariant quadratic form on 𝓡, since ξ, ∗ and the trace pairing are equivariant.

### E1.2 The four invariants are complete (hand, representation theory)

In 4D Lorentzian signature, 𝓡 = (scalar) ⊕ (trace-free Ricci) ⊕ (Weyl), dimensions 1 + 9 + 10, each irreducible over ℝ.
- The scalar and trace-free Ricci summands are absolutely irreducible: each carries exactly one invariant quadratic form, S² and Ric₀·Ric₀.
- The real Weyl representation is the realification of the complex irreducible W⁺ (spinor type (2,0)), with W⁻ its complex conjugate. Its commutant is ℂ, so it carries exactly two real invariant quadratic forms. They are W·W and W·∗W, with (∗W)_abcd = ½ε_cd^{fg}W_abfg and ε₀₁₂₃ = +1.
- Distinct summands are inequivalent, so by Schur they do not pair invariantly.

So every Spin-invariant quadratic form on 𝓡 is a unique combination of W·W, W·∗W, Ric₀·Ric₀ and S². The polarized fit (`quadratic.bilinear_fit`) has 210 equations (basis pairs i ≤ j) in 4 unknowns. A consistent fit is the identity on 𝓡. An inconsistent one is recorded as `None`, not raised: that is what a non-equivariant (dressed) X produces.

**Normalization of W·∗W.** The ½ is the one in the dual. A hand-built control (`test_weyl_dual_normalization`) fixes it independently of the fit. It builds D = ∗W entry by entry and checks W·∗D = −W·W (because ∗∗ = −1 on 2-forms in Lorentzian signature) and W·D = W·∗W.

### E1.3 Why the Weyl coefficients vanish (identity, via H13)

For an equivariant X whose response lies in B02's four-dimensional span (H13: every equivariant X in 4D; `gates.response` checks this on all 55 generators and raises otherwise),

$$*X(\xi R)=a\,E_F(\mathrm{Ric})+b\,E_{F'}(\mathrm{Ric})+c\,S\,E_F(g)+d\,S\,E_{F'}(g).$$

The right side depends on R only through Ric and S. Hence X(ξR) does too, Q_X is a quadratic form in (Ric₀, S) alone, and the W·W and W·∗W coefficients are 0. This is the response-level form of P4 for undressed operators. It is a consequence of the grade count in H13, not an extra assumption.

### E1.4 The response Gram and the Einstein ratio (identity, executed)

Let b₁ … b₄ be the four maps R ↦ ∗⁻¹(E_F(Ric)), ∗⁻¹(E_{F′}(Ric)), ∗⁻¹(S E_F(g)), ∗⁻¹(S E_{F′}(g)) (`quadratic.response_basis`). Then X(ξR) = Σ rᵢ bᵢ(R) with r = (a, b, c, d), and by bilinearity Q_X = Σᵢⱼ rᵢrⱼ Gᵢⱼ, where Gᵢⱼ is the fit of ⟨bᵢ, bⱼ⟩. The executed Gram (pinned convention, both signatures) gives

$$Q_X=(b^2-a^2)\,\mathrm{Ric}\cdot\mathrm{Ric}+(-2ac+2bd-4c^2+4d^2)\,S^2,\qquad \mathrm{Ric}\cdot\mathrm{Ric}=\mathrm{Ric}_0\cdot\mathrm{Ric}_0+\tfrac14 S^2 .$$

**On the Einstein ratio** c = −a/2, d = −b/2 (H13): −2ac = a², 2bd = −b², −4c² = −a², 4d² = b². The S² coefficient is a² − b² − a² + b² = 0 exactly, so

$$Q_X=(b^2-a^2)\,\mathrm{Ric}\cdot\mathrm{Ric}.$$

Checks against direct fits (pinned):
- **E_OP:** (0, 0, −4, −1), i.e. −4 Ric·Ric (so b² − a² = −4).
- **CCC literal and CAA Einstein:** (0, 0, −1, −¼) = −Ric·Ric.
- **CAC chiral:** 0. It lies on a null line (below).
- **Hand control** R = KN(g, g), with R_abcd = 2(g_ac g_bd − g_ad g_bc): Ric = 6g, S = 24, Ric·Ric = 144 and W = 0, so Q(E_OP) = −576.

All imaginary parts are 0.

### E1.5 The C1 kernel: radical and null lines (identity)

The C1 kernel is 8-dimensional (Phase 2). Its response map r: kernel → ℚ⁴ has a 6-dimensional kernel, the zero-response directions, with X(ξR) = 0 on 𝓡. Its image is the 2-dimensional Einstein plane {(a, b, −a/2, −b/2)} (rank 2, κ = ½; Phase 2 README).
- Q_X depends on X only through r(X), so the six zero-response directions form the radical: they contribute 0, cross terms included.
- On the 2-dimensional response image (the quotient of the 8-dimensional kernel by the radical), Q is the indefinite form (b² − a²) Ric·Ric. Its null lines are b = ±a.
- Each null line pulls back to a 7-dimensional null subspace of the 8-dimensional kernel (6 + 1). CAC lies on one of them.

### E1.6 The Gauss–Bonnet rewriting (hand)

In 4D, with E = Riem² − 4 Ric² + R² and W² = Riem² − 2 Ric² + ⅓R²,

$$\mathrm{Ric}\cdot\mathrm{Ric}=\tfrac12\big(W^2-\mathcal E\big)+\tfrac13 R^2 .$$

√|g| E is a total-derivative density. On a closed manifold, or with suitable boundary terms, it does not change the metric field equation. So **an equivalent action density** for (b² − a²) Ric·Ric is (b² − a²)(½W² + ⅓R²). This contains W², even though the pointwise integrand has W·W coefficient 0. Both statements are true and both are kept.

### E1.7 Readings

- **R1 (`[ext]`, conditional).** Read the restricted term as a metric action: the connection is the Levi-Civita connection of a varied metric. Then for b² ≠ a², it is a quadratic-curvature action, ∝ ½W² + ⅓R² up to E, with no Einstein–Hilbert term at this order. That is fourth-order quadratic gravity, which is not GR. For b² = a² (CAC and the null lines), the curvature-squared term vanishes on algebraic curvature, and nothing is left at T = 0 in this restriction.
- **R2 (not established).** The draft varies ϖ at fixed metric (reading V: δT = δA). An independent connection's curvature is generally not algebraic (it lacks the pair symmetry and the first Bianchi identity), and the T-terms of I₂ (the κ₁ cross terms and κ₁²|T|²) are omitted here. So this fit does not establish an independent-connection Ricci-squared theory. "Yang–Mills-type" describes only the derivative order of the unreduced quadratic functional, not Yang–Mills equivalence (H14). Such a theory would be non-GR, but it would not be an escape from Einstein's equation.

**Not claimed:** the T-sector of I₂; the κ₁ cross terms; curvature outside ξ(𝓡); a field equation, spectrum, ghost analysis or low-energy limit; anything at 14D.

## E2 — the dressed Weyl response of (9.3)

### E2.1 The family (identity)

⊚_ε is (9.3) with Φⁱ → ε⁻¹Φⁱε, the conjugation acting on the Clifford factor only ((8.1) text; `gu.shiab.shiab_dressed`). The family is the Cayley transform h = (1 − X)(1 + X)⁻¹ of X = t·u_I, t = ½, for every nonzero blade I. Here u_I is the u(A) generator on blade I: G_I or iG_I, as fixed by `universal.phases`.
- X ∈ u(A), so h ∈ U(A) whenever 1 + X is invertible. Each member is also checked directly (hᵗAh = A, `gu.adjoint.is_in_group`).
- At t = ½ all 15 blades give invertible 1 + X. At t = 1, 8 of the 15 are singular. They are skipped and listed (`family_report`).
- Modes: CCC and CAA with Φ = (F, B); CAC with Φ¹ = F + F′, Φ² = B′.

### E2.2 Covariance, and why the leak is gauge-invariant (hand; B02 `proofs.md`)

For invertible h acting on the Clifford factor, with c_h(x) = h⁻¹xh (B02 Test 3(a)):

$$\circledcirc_{\varepsilon h}(c_h x)=c_h\,\circledcirc_\varepsilon(x).$$

At ε = 1 this reads ⊚_h(x) = c_h ⊚(c_h⁻¹x).
- **Zero output is gauge-invariant.** c_g is invertible, so ⊚_ε(x) = 0 iff ⊚_{εg}(c_g x) = 0. A nonzero response of the pair (h, ξW) stays nonzero for the transformed pair (hg, c_g ξW), for every g. No gauge transformation removes it.
- **What the covariance control shows.** The control evaluates ⊚_h(c_h ξW) = c_h ⊚(ξW) = 0. That is a statement about a *different*, aligned pair: ⊚_h annihilates the transported Weyl subspace c_h ξ(Weyl). It says nothing about ⊚_h(ξW).
- **Where the leak comes from.** ⊚_h(ξW) = c_h ⊚(c_h⁻¹ξW). c_h⁻¹ acts on the Clifford factor alone and leaves the 2-form indices of ξW in place. So c_h⁻¹ξW is in general not in ξ(Weyl), and may have Clifford parts of other grades. Nothing forces it into ker ⊚.

### E2.3 Grade-2 Cayley elements lie in Spin (hand; Codex verified at t = ½)

Let G_I be a simple bivector with G_I² = s ∈ {±1}, t real, and X = tG_I. Since 1 − X and 1 + X commute and (1 + X)(1 − X) = 1 − t²s,

$$h=\frac{(1-X)^2}{1-t^2s}=\alpha+\beta G_I,\qquad \alpha=\frac{1+t^2s}{1-t^2s},\quad \beta=\frac{-2t}{1-t^2s}.$$

- With reversion G̃_I = −G_I: h h̃ = α² − β²s = [(1 + t²s)² − 4t²s]/(1 − t²s)² = 1.
- h is even, and h v h̃ is a vector for every vector v. Write G_I = Γ_aΓ_b. If v is orthogonal to the a–b plane, v commutes with G_I and h v h̃ = v h h̃ = v. If v lies in the plane, v anticommutes with G_I, so h v = v h̄ with h̄ = α − βG_I. Reversion gives h̃ = α − βG_I = h̄, so h v h̃ = v h̄² = v(α² + β²s − 2αβG_I). Here v G_I is again a vector in the plane.
- Hence h lies in the Spin image. For t ∈ [0, ½] the denominator 1 − t²s never vanishes, so the path from h = 1 stays in the group: h is in the identity component Spin₀(p,q).

So a Weyl response does **not** need ε outside the Spin image.

### E2.4 The leak table (identity, executed)

Leak rank = rank of W ↦ ∗⊚_h(ξW) on the 10-dimensional Weyl space. Stabilizer = dimension of {L ∈ spin(p,q) : ρ(L)⊚_h = ⊚_h ρ(L) on ξ(𝓡)}, computed as 6 − rank of the stacked commutator columns. Undressed, the leak rank is 0 for all three modes.

| Dressing | Leak rank (of 10, Weyl space) | Stabilizer dimension (of 6, spin(p,q)) |
|---|---|---|
| grade 1 (4 blades) | 10 | 3 |
| grade 2 (6 blades; in Spin₀) | 6 | 2 |
| grade 3 (4 blades) | 5 for CCC/CAA, 10 for CAC | 3 |
| grade 4 (pseudoscalar) | 0 | 6 |

- Covariance defect 0 for every mode, dressing and Weyl basis input, at both signatures.
- Dressed Q (E1's fit applied to ⊚_h): consistent for the pseudoscalar dressing, where it equals the undressed Q, and for CAC under grade-2 dressings, where it is identically 0. Otherwise `None`: the dressed operator is not Spin-equivariant.
- (3,1) and (1,3) agree row by row.

### E2.5 P4 under dressing (hand, with a counterexample)

From E2.2: ⊚_h(x) = 0 iff c_h⁻¹x ∈ ker ⊚.
- **Sufficient:** c_h⁻¹x ∈ ξ(Weyl) ⇒ ⊚_h(x) = 0, since P4 holds for the undressed ⊚.
- **Not necessary.** ker ⊚ is strictly larger than ξ(Weyl). Codex's counterexample: CCC at (3,1), blade 0111 (grade 3), and the Weyl input x ∈ ξ(Weyl) with sparse entries, keyed (form blade, Clifford blade) as bitmasks, (3, 9): −12, (9, 3): 12, (6, 12): −12, (12, 6): 12. Then ⊚_h(x) = 0, while c_h⁻¹x has nonzero grade-3 Clifford coefficients, so c_h⁻¹x ∉ ξ(Weyl). Task 4 makes this a regression control.

So the draft's P4, "the Weyl curvature tensor is annihilated" (p. 43), holds for the undressed operator. It fails for some dressed operators on fixed Weyl input, including the six Spin₀ grade-2 dressings (leak rank 6 on the 10-dimensional Weyl space). It does not fail for the pseudoscalar dressing. The exact replacement is the kernel condition above, with transport into ξ(Weyl) as a sufficient case.

### E2.6 Stabilizers (identity, with an inclusion to be checked)

The stabilizer dimensions 3, 2, 3, 6 are algebraic statements about fixed dressed operators on algebraic-curvature inputs.
- **Inclusion.** If [L, h] = 0 then ρ(L) commutes with c_h, and with ⊚ by equivariance, so it commutes with ⊚_h = c_h ⊚ c_h⁻¹. Hence the centralizer {L ∈ spin : [L, h] = 0} is contained in the stabilizer.
- Task 4 computes the centralizer independently. Equal dimensions, together with the inclusion, give equality on the checked members.
- **The pseudoscalar row, by hand.** For I = 1111, h ∈ span{1, C}, where C is the pseudoscalar. In 4D, C commutes with every even element. ξ(R) has bivector Clifford coefficients, so c_h⁻¹ξW = ξW and ⊚_h(ξW) = c_h ⊚(ξW) = 0: leak 0. C commutes with every bivector, so [L, h] = 0 for all L ∈ spin: centralizer 6, and so stabilizer 6.

### E2.7 Reading D2 (conditional)

The draft says the dressing "rotates only the bundle valued portion … exactly compensates" (p. 41, P3). The covariance identity confirms the compensation as an identity between *pairs*: transformed operator and transformed input. It does not make ⊚_ε equal to ⊚.
- **For a fixed ε background**, the dressed operator responds to Weyl curvature with the computed rank, and its stabilizer on algebraic-curvature inputs is the computed subalgebra of spin(p,q).
- **Dynamical symmetry breaking is a separate question.** Whether a theory with dynamical ε breaks Lorentz symmetry needs an action for ε and a background solution. No ε action, vacuum or observable is specified in the draft or here. Dynamics and phenomenology are the D2 follow-up.

**Not claimed:** a search over U(A); 14D; any physical Lorentz violation.

## Register additions

| ID | Statement | Scope | Source |
|---|---|---|---|
| B07-E1 | On algebraic curvature at T = 0, the curvature sector of (9.11) is Ric²: Q_X = (b² − a²) Ric·Ric on the Einstein ratio, with W·W and W·∗W coefficients 0. Ric·Ric is equivalent to ½W² + ⅓R² up to the Gauss–Bonnet density, so Q_X is (b² − a²) times that density | identity at (3,1)/(1,3), flat model, reading V, ξ(𝓡) only | E1.3–E1.6 |
| B07-E1-R1 | Metric reading of B07-E1: quadratic-curvature gravity without an Einstein–Hilbert term, for b² ≠ a² | `[ext]`, conditional | E1.7 |
| B07-E1-R2 | Independent-connection reading | not established | E1.7 |
| B02-P4d | P4 fails for some dressed ⊚_h on fixed Weyl input, including the six Spin₀ grade-2 dressings (leak rank 6 of 10); it does not fail for the pseudoscalar dressing. ⊚_h(x) = 0 iff c_h⁻¹x ∈ ker ⊚, with c_h⁻¹x ∈ ξ(Weyl) sufficient only | identity on the stated blade-Cayley family; counterexample for necessity | E2.2–E2.5 |
| B02-D2 | Stabilizer dimensions 3, 2, 3, 6 of spin(p,q), by dressing grade, for fixed ε on this family; no dynamical claim | identity (stabilizers); dynamics unspecified | E2.6–E2.7 |
