# B07 non-GR channels: the curvature-squared sector of (9.11) and the dressed Weyl response of (9.3)

**Status:** results recorded and independently re-derived (709/709 agree); README audit pending; register pending; P7 pending.

**Result, in one paragraph.** Two non-GR channels were tested with exact algebra on GU's own constructions, at a 4D point, signatures (3,1) and (1,3), on Phase 2's flat model under reading V.
- **E1.** On algebraic curvature at T = 0, the curvature sector of the second-order Lagrangian (9.11) is Ricci-squared. The pointwise integrand has no nonzero W·W or W·∗W coefficient, and on B02's Einstein ratio it is (b² − a²) Ric·Ric. Modulo the Gauss–Bonnet density this is (b² − a²)(½W² + ⅓R²). Read as a metric action (`[ext]`, R1), that is fourth-order quadratic gravity, not GR.
- **E2.** The dressed operator ⊚_ε responds to Weyl curvature, even for dressings inside Spin₀ (leak rank 6 on the 10-dimensional Weyl space). Whether the output is zero is gauge-invariant. The draft's P4 ("the Weyl curvature tensor is annihilated", p. 43) holds for the undressed operator. Under dressing, the exact condition is c_h⁻¹x ∈ ker ⊚, with transport into ξ(Weyl) only sufficient.

Neither is a 4D field equation, a spectrum, or an observational claim.

Plan: `docs/superpowers/plans/2026-10-16-b07-escape.md`, rev 1.1 (`2593adf`), approved by the user. Derivations E1–E2: `derivations.md` (`8c3592e`, Grok review folded). Code and tests: `b000c3f`. Result: `result.json` (`2b75c7e`). Independent re-derivation: `rederivation.md` (`25d50b3`, `a41f016`, `5d12afb`).

## The question

The user asked: "What can we do to escape? Outside of Einstein GR".
- **Lovelock.** In 4D, the only symmetric, divergence-free tensor built from a metric and at most its second derivatives is a combination of the Einstein tensor and Λg. A non-GR answer therefore needs an extra field, higher derivatives, D > 4, or torsion/a non-metric connection. Only the Ricci/scalar span is forced by this; Phase 2's rank 2 and κ = ½ are measured, not forced.
- Grok's adversarial review (2026-10-16) of Claude's proposal and of Argon's four exits kept two channels on GU's own constructions. **E1** is the higher-derivative exit: which curvature-squared invariants does I₂ = ⟨Υ, Υ⟩ contain? **E2** is the extra-field exit (Argon exit 4; GU's P3/P4): with ε as the field, does ⊚_ε respond to Weyl curvature, what does the covariance identity say about it, and what Lorentz symmetry does each dressing leave?

## Scope

- 4D point, (3,1) and (1,3), flat model, reading V (ε and the metric fixed, δT = δA). Exact rationals and Gaussian rationals only (P4).
- **E1:** `identity` on a 20-element basis of algebraic curvature 𝓡 (all 210 basis pairs), at T = 0, F = ξ(R) only. The four invariants W·W, W·∗W, Ric₀·Ric₀, S² span every Spin-invariant quadratic form on 𝓡 (`derivations.md` E1.2).
- **E2:** `identity` on the stated finite family: the Cayley transforms h = (1 − X)(1 + X)⁻¹ of X = ½u_I for all 15 nonzero blades I, each checked to lie in U(A). Not a search over U(A); not 14D.

## E1 results (`result.json` → `E1`)

Q_X(R) = ⟨X(ξR), X(ξR)⟩, fitted to (W·W, W·∗W, Ric₀·Ric₀, S²). Both signatures agree. All imaginary parts are 0.

| Operator | Pinned pairing | Prime pairing (operator fixed, pairing varied) |
|---|---|---|
| E_OP (Phase 2 block representative) | (0, 0, −4, −1) = −4 Ric·Ric | (0, 0, 4, 1) |
| CCC literal; CAA Einstein | (0, 0, −1, −¼) = −Ric·Ric | (0, 0, 1, ¼) |
| CAC chiral | 0 | 0 |

- The prime column is ⟨x, y⟩′ = (−1)^{deg y}⟨x, y⟩ with y a 3-form, so Q′ = −Q. It is **not** the full Hodge-convention switch inside (9.3), which reparametrizes Φ² (for CAA with fixed (F, B) that switch fits (0, 0, 1, 9/4)).
- **Response Gram (pinned).** With B02's response r = (a, b, c, d): Q = (b² − a²) Ric·Ric + (−2ac + 2bd − 4c² + 4d²) S². On the Einstein ratio (c = −a/2, d = −b/2) the S² coefficient cancels exactly: Q = (b² − a²) Ric·Ric.
- **The C1 kernel.** The six zero-response directions of the 8-dimensional C1 kernel are its radical (contribution 0, cross terms included). On the 2-dimensional response image, Q is indefinite with null lines b = ±a. Each null line pulls back to a 7-dimensional null subspace of the 8-dimensional kernel. CAC lies on one.
- **Controls.** KN(g, g): Ric = 6g, S = 24, W = 0, so Q(E_OP) = −576. Hand-built Weyl dual D = ∗W: W·∗D = −W·W and W·D = W·∗W (`test_weyl_dual_normalization`).

## E2 results (`result.json` → `E2`)

Undressed, the Weyl response is 0 for CCC, CAA and CAC. Leak rank = rank of W ↦ ∗⊚_h(ξW) on the 10-dimensional Weyl space; stabilizer = dimension of {L ∈ spin(p,q) : ρ(L)⊚_h = ⊚_h ρ(L) on ξ(𝓡)}, out of 6.

| Dressing | Leak rank (Weyl space, of 10) | Stabilizer dimension (spin(p,q), of 6) |
|---|---|---|
| grade 1 (4 blades) | 10 | 3 |
| grade 2 (6 blades; in Spin₀) | 6 | 2 |
| grade 3 (4 blades) | 5 for CCC/CAA, 10 for CAC | 3 |
| grade 4 (pseudoscalar) | 0 | 6 |

- **Covariance control:** ⊚_h(c_h ξW) = c_h ⊚(ξW) = 0, defect 0 for every mode, dressing and Weyl basis input.
- **Dressed Q:** consistent for the pseudoscalar dressing (equal to the undressed Q) and for CAC under grade-2 dressings (identically 0); `None` (not Spin-invariant) for every other mode/dressing pair.
- **Family:** at t = ½ all 15 blades are nonsingular and in U(A); at t = 1, 8 are singular and recorded as skipped.
- (3,1) and (1,3) agree row by row.

## Independent re-derivation (`rederivation.md`)

`rederive.py` (`25d50b3`, one fix `a41f016` committed before the decisive run; table `5d12afb`) was written in a fresh context. It imports only the standard library, numpy and `gu.clifford` (gamma matrices), and rebuilds algebraic curvature, ξ, the Φ bases, the bracket modes, E_OP's blocks and the pairing from the documented formulas. **709 comparisons against `result.json` and the plan's controls, 0 disagreements**, at both signatures (141.6 s; Claude re-ran it: same count, exit 0).
- **E1:** every pinned fit (E_OP, CCC, CAA, CAC), the prime sign flip, all 16 response-Gram entries, the KN(g, g) control (Q(E_OP) = −576) and the ∗W normalization control.
- **E2:** leak rank, covariance defect and dressed Q for every blade and mode, via the identity route ⊚_h(ξW) = c_h ⊚(c_h⁻¹ξW) with its own ⊚. The centralizer dimension of every member equals the recorded stabilizer dimension, so by the inclusion (`derivations.md` E2.6) **stabilizer = centralizer** on the whole family.
- **P4 counterexample** (CCC, (3,1), blade 0111): the input lies in ξ(Weyl), the dressed output is 0, and c_h⁻¹x has two nonzero grade-3 Clifford coefficients, so c_h⁻¹x ∈ ker ⊚ but not in ξ(Weyl).
- **What is not independent.** The first run disagreed by a uniform factor 16 on every E1 fit. The B02 README formula for ξ does not state its summation range; summing over a < b, c < d reproduces B02's documented responses. So the *absolute scale* of Q (including −576) is pinned by B02's documented normalization, not independently of it. Every scale-free result (zero Weyl coefficients, ratios, sign flips, ranks, centralizers, the counterexample) agreed already in the first run.
- **Not rebuilt:** the stabilizer itself (only the centralizer, as planned), the C1-kernel radical and null lines (they need the 40-dimensional equivariant space), and the t = 1 skip count.

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

- **Exit 4 (Weyl leak through ε):** the strongest, and now a measured channel: E2 shows a Weyl response for fixed dressings, including Spin₀ ones (rank 6), with stabilizers 3/2/3/6; it is a fixed-background statement, and dynamics (D2) are open.
- **Exit 3 (non-linear torsion backgrounds):** the mechanism is wrong; the order-T² test C2 is pointwise and must vanish for every T, so no background removes it (Phase 2), and E1 is the higher-derivative exit that does survive.
- **Exit 1 (drop the Lagrangian; algebraic constraints):** reframed as the B07-Bi compatibility gate for (9.7) as a standalone equation; a follow-up, not an escape.
- **Exit 2 (formalize the T² no-go):** a scoped technical note with a Lean check of one C2 witness; a follow-up, not an escape.

## Files

- `derivations.md`: E1–E2 derivations and register additions.
- `quadratic.py`: E1 (invariant fit, response Gram). `weyl_dressing.py`: E2 (family, leak, covariance, stabilizer). `run.py`: runner. Tests: `tests/test_b07_escape.py` (9).
- `result.json`: the run (scope, source commit, E1, E2, seconds).
- `rederive.py`, `rederivation.md`: independent re-derivation (gamma matrices only).
