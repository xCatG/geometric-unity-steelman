# B07 non-GR channels: the curvature-squared sector of (9.11) and the dressed Weyl response of (9.3)

**Status:** results recorded and independently re-derived twice: by a fresh Claude subagent (719/719 agree after an audit revision) and by Codex (192/192 agree, exact SymPy, written without opening the Task 2 code or the first re-derivation); see below. README and first re-derivation audited by a fresh Claude subagent (11 findings) and by Grok (4 findings), all folded; register updated; P7 clean-clone reproduction at `b000c3f` passed (payload identical apart from `seconds` and `source_commit`; 401 tests passed; 8/8 seeded faults RED).

**Result, in one paragraph.** Two non-GR channels were tested with exact algebra on GU's own constructions, at a 4D point, signatures (3,1) and (1,3), on Phase 2's flat model under reading V.
- **E1.** On algebraic curvature at T = 0, the curvature sector of the second-order Lagrangian (9.11) is Ricci-squared. The W·W and W·∗W coefficients of the pointwise integrand are 0, and on B02's Einstein ratio it is (b² − a²) Ric·Ric (pinned pairing; the prime pairing flips the sign). As an equivalent action density this is (b² − a²)(½W² + ⅓R²): the Gauss–Bonnet density is a total derivative on a closed manifold or with suitable boundary terms. Read conditionally as a metric action (`[ext]`, R1, with the Levi-Civita connection of a varied metric), for b² ≠ a² that is fourth-order quadratic gravity with no Einstein–Hilbert term at this order, not GR. The independent-connection reading R2 is not established.
- **E2.** The dressed operator ⊚_ε responds to Weyl curvature, even for dressings inside Spin₀ (leak rank 6 on the 10-dimensional Weyl space). Whether the output is zero is gauge-invariant. The draft's P4 ("the Weyl curvature tensor is annihilated", p. 43) holds for the undressed operator (measured for CCC, CAA and CAC; argued for every equivariant X in 4D by Phase 2 H13). Under dressing, the exact condition is c_h⁻¹x ∈ ker ⊚, with transport into ξ(Weyl) only sufficient.

Neither is a 4D field equation, a spectrum, or an observational claim.

Plan: `docs/superpowers/plans/2026-10-16-b07-escape.md`, rev 1.1 (`2593adf`), approved by the user. Derivations E1–E2: `derivations.md` (`8c3592e`, Grok review folded). Code and tests: `b000c3f`. Result: `result.json` (`2b75c7e`). Independent re-derivation: `rederivation.md` (`25d50b3`, `a41f016`, `5d12afb`).

## The question

The user asked: "What can we do to escape? Outside of Einstein GR".
- **Lovelock.** In 4D, the only symmetric, divergence-free tensor built from a metric and at most its second derivatives is a combination of the Einstein tensor and Λg. A non-GR answer therefore needs an extra field, higher derivatives, D > 4, or torsion/a non-metric connection. Lovelock constrains which metric field equations are possible; it does not say that GU's operators realize one. That the response lies in the four-dimensional Ricci/scalar span is forced by representation theory (Phase 2 H13). That the response image of the 8-dimensional C1 kernel has rank 2 with κ = ½ is measured (Phase 2).
- Grok's adversarial review (2026-10-16) of Claude's proposal and of Argon's four exits kept two channels on GU's own constructions. **E1** is the higher-derivative exit: which curvature-squared invariants does I₂ = ⟨Υ, Υ⟩ contain? **E2** is the extra-field exit (Argon exit 4; GU's P3/P4): with ε as the field, does ⊚_ε respond to Weyl curvature, what does the covariance identity say about it, and what Lorentz symmetry does each dressing leave?

## Scope

- 4D point, (3,1) and (1,3), flat model, reading V (ε and the metric fixed, δT = δA). Exact rationals and Gaussian rationals only (P4).
- **Conventions** (every sign below rests on these): η = diag(+1 × p, −1 × q); ⟨x, y⟩ = Tr(x∧∗y)/2^{n/2} with the pinned ∗ (`second_order.mpair`); Ric_bd = η^{ac}R_abcd; (∗W)_abcd = ½ε_cd^{fg}W_abfg with ε₀₁₂₃ = +1; B02's response r = (a, b, c, d) in the basis (E_F(Ric), E_F′(Ric), S E_F(g), S E_F′(g)), with the Einstein ratio c = −a/2, d = −b/2.
- **E1:** `identity` on a 20-element basis of algebraic curvature 𝓡 (all 210 basis pairs), at T = 0, F = ξ(R) only. The four invariants W·W, W·∗W, Ric₀·Ric₀, S² span every Spin-invariant quadratic form on 𝓡 (`derivations.md` E1.2).
- **E2:** `identity` on the stated finite family: the Cayley transforms h = (1 − X)(1 + X)⁻¹ of X = ½u_I for all 15 nonzero blades I, each checked to lie in U(A). Not a search over U(A); not 14D.

## E1 results (`result.json` → `E1`)

Q_X(R) = ⟨X(ξR), X(ξR)⟩, fitted to (W·W, W·∗W, Ric₀·Ric₀, S²). Both signatures agree. All imaginary parts are 0.

| Operator | Pinned pairing | Prime pairing (operator fixed, pairing varied) |
|---|---|---|
| E_OP (Phase 2 block representative) | (0, 0, −4, −1) = −4 Ric·Ric | (0, 0, 4, 1) |
| CCC literal; CAA Einstein | (0, 0, −1, −¼) = −Ric·Ric | (0, 0, 1, ¼) |
| CAC chiral | 0 | 0 |

- The prime column is ⟨x, y⟩′ = (−1)^{deg y}⟨x, y⟩ with y a 3-form, so Q′ = −Q. It is **not** the full Hodge-convention switch inside (9.3), which reparametrizes Φ² (for CAA with fixed (F, B) that switch fits (0, 0, 1, 9/4); from the plan's rev 1 review, not computed here).
- **Response Gram (pinned).** With B02's response r = (a, b, c, d): Q = (b² − a²) Ric·Ric + (−2ac + 2bd − 4c² + 4d²) S². On the Einstein ratio (c = −a/2, d = −b/2) the S² coefficient cancels exactly: Q = (b² − a²) Ric·Ric.
- **The C1 kernel** (hand, from the Gram and Phase 2; not independently rebuilt). The six zero-response directions of the 8-dimensional C1 kernel (operator space, in the 40-dimensional B07-U) are its radical (contribution 0, cross terms included). On the 2-dimensional response image, Q is indefinite with null lines b = ±a. Each null line pulls back to a 7-dimensional null subspace of the 8-dimensional kernel. CAC lies on one.
- **Controls.** KN(g, g): Ric = 6g, S = 24, W = 0, so Q(E_OP) = −576 (pinned pairing; hand from the fit, re-derived directly; the test checks S·S = 576). Hand-built Weyl dual D = ∗W: W·∗D = −W·W and W·D = W·∗W (`test_weyl_dual_normalization`).

## E2 results (`result.json` → `E2`)

Undressed, the Weyl response is 0 for CCC, CAA and CAC. Leak rank = rank of W ↦ ∗⊚_h(ξW) on the 10-dimensional Weyl space; stabilizer = dimension of {L ∈ spin(p,q) : ρ(L)⊚_h = ⊚_h ρ(L) on ξ(𝓡)}, out of 6 (`residual` in `result.json`).

| Dressing | Leak rank (Weyl space, of 10) | Stabilizer dimension (spin(p,q), of 6) |
|---|---|---|
| grade 1 (4 blades) | 10 | 3 |
| grade 2 (6 blades; in Spin₀) | 6 | 2 |
| grade 3 (4 blades) | 5 for CCC/CAA, 10 for CAC | 3 |
| grade 4 (pseudoscalar) | 0 | 6 |

- **Covariance control:** ⊚_h(c_h ξW) = c_h ⊚(ξW) = 0, defect 0 for every mode, dressing and Weyl basis input.
- **Dressed Q:** consistent for the pseudoscalar dressing (equal to the undressed Q) and for CAC under grade-2 dressings (identically 0); `None` (not Spin-invariant) for every other mode/dressing pair.
- **Family:** at t = ½ all 15 blades are nonsingular and in U(A); at t = 1, 8 of 15 are singular and recorded as skipped (`test_dressing_family_records_skips_and_lies_in_u_a`, (3,1) only; not in `result.json`).
- (3,1) and (1,3) agree row by row.

## Independent re-derivation (`rederivation.md`)

`rederive.py` (`25d50b3`, one fix `a41f016` committed before the decisive run; table `5d12afb`) was written by a fresh Claude subagent. The plan names Codex, which was then out of quota (Grok was out of credits); the deviation is recorded in `rederivation.md`, and Codex's own re-derivation followed (next section). It imports only the standard library, numpy and `gu.clifford` (gamma matrices), and rebuilds algebraic curvature, ξ, the Φ bases, the bracket modes, E_OP's blocks and the pairing from the documented formulas. **719 comparisons against `result.json` and the plan's controls, 0 disagreements**, at both signatures, after the Grok-audit revision `0e389ea` (124.1 s, run by Claude; 709/709 before it, 141.6 s).
- **E1:** every pinned fit (E_OP, CCC, CAA, CAC), the prime sign flip, all 16 response-Gram entries, the KN(g, g) control (Q(E_OP) = −576) and the ∗W normalization control.
- **E2:** leak rank via the identity route ⊚_h(ξW) = c_h ⊚(c_h⁻¹ξW) with its own ⊚ (checked equal to the direct dressing on every Weyl input), Task 2's covariance predicate and dressed Q, for every blade and mode. The covariance rows follow from the covariance identity, so they check Task 2's recorded field rather than derive anything new; before `0e389ea` they compared a different predicate that is zero by construction. The centralizer dimension of every member equals the recorded stabilizer dimension, so by the inclusion (`derivations.md` E2.6) **stabilizer = centralizer** on the whole family.
- **P4 counterexample** (CCC, (3,1), blade 0111): the input lies in ξ(Weyl), the dressed output is 0, and c_h⁻¹x has two nonzero grade-3 Clifford coefficients, so c_h⁻¹x ∈ ker ⊚ but not in ξ(Weyl). Since `0e389ea` the count, the grades {2, 3} and the opposite u_I sign are locked as rows.
- **Entailed rows.** The grade-4 leak ranks follow from the pseudoscalar dressing commuting with every bivector (derivations E2.6), and the prime Q column is the pinned column with the 3-form sign flip of the same Hodge star. They catch an inconsistent `result.json` but are not separate derivations.
- **What is not independent.** Run 1 (`25d50b3`) disagreed on 30 of 709 comparisons, all by a uniform factor 16 in E1 scale (including Q(E_OP) = −9216). The fix `a41f016` reads ξ's sum over a < b, c < d and widens the W·∗W non-vacuity check to basis pairs. It was recorded as a documentation note, not a `FINDING:`. The B02 README formula for ξ does not state its summation range; summing over a < b, c < d reproduces B02's documented responses. So the *absolute scale* of Q (including −576) is pinned by B02's documented normalization, not independently of it. The Grok audit found the fix follows from B02's documented ξ and its KN(g, g) CCC response −6F, not from `result.json` (the all-index reading is 4× the ordered sum, so Q is 16×), and Codex reached the same range on its own. Every scale-free result (zero Weyl coefficients, ratios, sign flips, ranks, centralizers, the counterexample) agreed already in the first run.
- **Not rebuilt:** the stabilizer itself (only the centralizer, as planned), the C1-kernel radical and null lines (they need the 40-dimensional equivariant space), and the t = 1 skip count.

## Second independent re-derivation, by Codex (`rederivation_codex.md`)

`rederive_codex.py` (`acd9783`, committed before its first run; an assertion-gate fix `80b81e2`; an E_OP extension `5073274`, committed before its run; tables `08927ab`, `245196b`) was written by Codex. It imports only the standard library, SymPy and `gammas` from `gu.clifford`. It works in exact arithmetic. Codex built it from the documented formulas without opening the Task 2 code, the tests or `rederive.py`, and reads `result.json` only as comparison data. **192 comparisons, 0 disagreements** at both signatures (29.9 s; Claude re-ran it: same count, exit 0). Three seeded faults (ξ scale, Weyl-dual half, scalar sign) and two E_OP faults each fail a mathematical comparison.
- **E1:** the pinned fits for E_OP, CCC, CAA and CAC (210 basis pairs, gamma-matrix traces), the ∗W normalization control, and the KN(g, g) controls including Q(E_OP) = −576. E_OP is built from its three-block definition and checked against the documented linear response 2E_F(Ric) − S·E_F(g) on all 20 curvature-basis inputs.
- **E2:** the centralizer dimension of all 15 blades at both signatures equals the recorded `residual` of every mode, with h ∈ U(A) checked; the CCC leak ranks at (3,1) for blades 0001, 0011, 0111 and 1111 are 10/6/5/0.
- **P4 counterexample:** the input lies in ξ(Weyl), its dressed CCC output is 0, and c_h⁻¹x has exactly two nonzero grade-3 coefficients, (3, 14) and (6, 11), each 160i/3 (keyed (form, Clifford) bitmask).
- **Same caveat on scale.** Codex also found that B02's ξ formula omits its summation range, and pinned it to a < b, c < d with coefficient ½ from B02's documented KN(g, g) responses (`FINDING:` in its report, resolved there). So the absolute E1 scale is again pinned by B02's normalization. Codex's first brief also omitted the file that defines E_OP; the extension added it (also a resolved `FINDING:`).
- **Narrower than the first:** no response Gram, prime pairing, dressed Q, or leak ranks beyond the four named CCC blades.

## Consequences

1. **E1.**
   - On algebraic curvature at T = 0, the curvature sector of (9.11) is Ricci-squared: the W·W and W·∗W coefficients of the pointwise integrand are 0, and on the Einstein ratio there is no separate S² term.
   - In 4D, Ric·Ric = ½(W² − E) + ⅓R², where E = Riem² − 4Ric² + R² is a total-derivative density: on a closed manifold, or with suitable boundary terms, it does not change the metric field equation. So *an equivalent action density* is ½W² + ⅓R², which contains W² even though the pointwise integrand has W·W coefficient 0. Keep both halves.
   - **R1 (`[ext]`, conditional).** If this restricted term is read as a metric action, with the connection the Levi-Civita connection of a varied metric, then for b² ≠ a² it is a quadratic-curvature action with no Einstein–Hilbert term at this order. That is fourth-order quadratic gravity, and not GR.
   - **R2 (not established).** The draft varies ϖ at fixed metric (reading V: δT = δA). An independent connection's curvature is generally not algebraic, and the T-terms and cross terms are omitted here. This fit therefore does not establish an independent-connection Ricci-squared theory. "Yang–Mills-type" describes only the derivative order of the unreduced quadratic functional, not Yang–Mills equivalence (H14). Such a theory would be non-GR, but not an escape from Einstein's equation.
2. **E2.**
   - A Weyl response does **not** need ε outside the Spin image: the grade-2 dressings, which lie in Spin, leak at rank 6.
   - The covariance identity is exact on the whole family. Whether the output is zero is gauge-invariant, so the leak of the pair (h, ξW) is not removed by any gauge transformation. What the control shows is that ⊚_h annihilates the transported Weyl subspace c_h ξ(Weyl).
   - **P4 under dressing.** c_h⁻¹x ∈ ξ(Weyl) is *sufficient* for ⊚_h(x) = 0. The exact condition is c_h⁻¹x ∈ ker ⊚, which is strictly larger (Codex's counterexample).
   - **Stabilizers.** The dimensions 3, 2, 3 and 6 are algebraic results about fixed dressed operators restricted to algebraic-curvature inputs.
   - **Reading D2, conditional.** For a fixed ε background, the dressed operator has the computed stabilizer on algebraic-curvature inputs. Whether a dynamical ε theory breaks Lorentz symmetry requires an action and a background solution. No ε action, vacuum or observable has been specified; dynamics and phenomenology are the D2 follow-up.

## What is not covered

- The T-sector of I₂ (κ₁ cross terms, κ₁²|T|²) and whether an Einstein–Hilbert-like term is induced.
- Curvature outside ξ(𝓡): an independent connection's non-algebraic curvature (reading R2).
- Any field equation, linearized spectrum, ghost analysis or low-energy limit.
- 14D (bounded witnesses at (7,7)/(9,5) are a follow-up).
- The 14D→4D pullback and the zero set of the C2 residual (both cut by Grok's review).
- The B07-Bi compatibility gate for (9.7).
- Dynamics of ε (D2): no ε action, vacuum or observable is specified.

## Argon's four exits

- **Exit 4 (Weyl leak through ε):** the one this run measures: on the stated finite dressing family at a 4D point, E2 shows a Weyl response for fixed dressings, including Spin₀ ones (leak rank 6 on the 10-dimensional Weyl space), with stabilizer dimensions 3/2/3/6 in spin(p,q); it is a fixed-background statement, and dynamics (D2) are open.
- **Exit 3 (non-linear torsion backgrounds):** as a test of whether (9.7) is the variation, C2 is a pointwise condition that must hold for every T at order T², so restricting to special T only picks out the zero set of the residual (cut by Grok's review); Phase 2 shows that no nonzero operator in the 8-dimensional C1 kernel passes C2 on the flat model, while curved and torsionful form-connection backgrounds beyond H11 remain open; the higher-derivative channel that survived review is E1, with its metric reading R1 conditional.
- **Exit 1 (drop the Lagrangian; algebraic constraints):** reframed as the B07-Bi compatibility gate for (9.7) as a standalone equation; a follow-up, not an escape.
- **Exit 2 (formalize the T² no-go):** a scoped technical note with a Lean check of one C2 witness; a follow-up, not an escape.

## Files

- `derivations.md`: E1–E2 derivations and register additions.
- `quadratic.py`: E1 (invariant fit, response Gram). `weyl_dressing.py`: E2 (family, leak, covariance, stabilizer). `run.py`: runner. Tests: `tests/test_b07_escape.py` (9).
- `result.json`: the run (scope, source commit, E1, E2, seconds).
- `rederive.py`, `rederivation.md`: independent re-derivation (gamma matrices only).
