# B07 escape, Task 4: independent re-derivation of E1 and E2

Re-deriver: a fresh Claude subagent, 2026-10-17. The plan names Codex; Codex and Grok were unavailable. Code: `rederive.py`, committed before its first run (`25d50b3`), with one fix committed before the second run (`a41f016`). Command: `uv run python -m experiments.B07.escape.rederive`. The decisive run took 141.6 s and exited 0. After a non-Claude audit (Grok), a revision `0e389ea` (committed before its run) changed three comparisons and added ten; that run took 124.1 s and exited 0.

**Verdict: 719 comparisons, 719 agree, 0 disagree** (709 before the audit revision). Nothing disagrees with `result.json` (source `b000c3f`) or with the plan's controls. Not every row is an independent check; see the audit revision below.

## Audit revision (`0e389ea`)

A Grok audit of this re-derivation found that some agree rows do not check what their labels say.
- **Covariance defect (90 rows).** Run 2 counted Weyl inputs with ⊚_h(c_h x) ≠ 0, a different predicate from Task 2's `cov_defect` (inputs with ⊚_h(c_h x) ≠ c_h ⊚(x)), and zero by construction here. The revision compares Task 2's predicate. It follows from the covariance identity ⊚_h = c_h ∘ ⊚ ∘ c_h⁻¹, which the identity-route rows check on ξ(Weyl) inputs (here it is applied to c_h ξ(Weyl)), so these rows are a consistency check of Task 2's recorded field, not a separate derivation.
- **`basis_dim` (2 rows).** Run 2 compared the literal 20; the revision compares the size of the built basis (its rank 20 is asserted by the builder).
- **P4 counterexample (10 new rows).** Run 2 locked only "at least one grade-3 coefficient" and only the `phase` branch. The revision locks, for both u_I signs, the grade-3 coefficient count 2 (pinned from the inspected run 2), the Clifford grades {2, 3}, the zero dressed output, c_h⁻¹x ∈ ker ⊚ and c_h⁻¹x ∉ ξ(Weyl).
- **Entailed, not independent.** Grade-4 leak ranks follow from the pseudoscalar's Cayley dressing commuting with every bivector (so the leak equals the undressed leak 0, derivations E2.6). The prime Q rows are the pinned rows with the 3-form sign flip of the same Hodge star, not a second Hodge computation. Both still catch a `result.json` that got them wrong.
- The identity-route rows, U(A) checks, centralizer-versus-`residual` rows, the ∗W non-vacuity row and the direct KN(g, g) Q(E_OP) = −576 are real comparisons.

## Independence

- **Imports:** the standard library, numpy, and `gu.clifford` (`gammas`, `chirality`, `dirac_pairing`) only. There is no `gu.shiab`, `gu.cliffform`, `gu.curvature`, `gu.adjoint` or `experiments` import. The Task 2 modules, their tests and those `gu` sources were not opened.
- **Arithmetic:** `fractions.Fraction` throughout. Gaussian rationals are (re, im) pairs of Fraction matrices. Ranks and fits use exact Gaussian elimination. There are no floats and no modular ranks. One coercion helper (`q`) rejects anything other than ints, numpy ints and Fractions.
- **Rebuilt from the docs:**
  - the 20-dimensional algebraic curvature space: a bivector-pair parametrization plus the one Bianchi constraint, with rank 20 and every symmetry checked;
  - Ricci, with Ric_bd = η^{ac}R_abcd;
  - the Weyl / trace-free-Ricci / scalar split, by the textbook n = 4 formula;
  - the four invariants, and ∗W with ε₀₁₂₃ = +1;
  - forms as bitmask dictionaries, and the pinned Hodge star (α∧∗β = ⟨α,β⟩vol);
  - ξ, F/F′/B/B′, both brackets, (9.3), and E_OP's three blocks;
  - the pairing Tr(x∧∗y)/2^{n/2}, using the actual 4×4 matrix trace;
  - u(A), via X♯ = A⁻¹X†A;
  - the blade Cayley family, the centralizer, the identity route and the P4 counterexample.

## Conventions reconstructed, and how each was pinned

| Item | Reconstruction | Source / pin |
|---|---|---|
| ξ | ξ(R) = ½ Σ_{a<b, c<d} R_abcd η_cη_d e^{ab}⊗Γ_cΓ_d | B02 README formula; the overall scale is pinned by B02's documented responses (see the note below) |
| Hodge star | e^I∧∗e^I = η_I vol, with vol = e^{0123}; prime: ∗′ = (−1)^{deg}∗ | B02 README convention map; B07 phase2 H14 |
| Φ | F = Σe^aΓ_a, F′ = Σe^aΓ_aC, B = Σ_{a<b}e^{ab}Γ_aΓ_b, B′ = Σ_{a<b}e^{ab}iΓ_aΓ_bC; C from `gu.clifford.chirality` | B02 transcription, branch 2 |
| Brackets | C: XY − YX; A: i(XY + YX); componentwise and ungraded | B02 transcription (12.26)–(12.27); proofs.md |
| (9.3) | [Φ¹∧∗x]_{m₀} − ½∗[Φ¹∧∗[Φ²∧∗x]_{m₁}]_{m₂} | proofs.md |
| E_OP | −2·[F∧∗x]_C − second[CC](F,B) + second[AA](F,B), with second = ∗[F∧∗[B∧∗x]] (no −½) | B07 phase2 README. Checked: the response is 2E_F(Ric) − S·E_F(g) on all 20 basis tensors, at both signatures |
| CAC | Φ¹ = F + F′, Φ² = B′, modes CAC | derivations E2.1 |
| u(A) phase | the smallest k ∈ {0,1,2,3} with i^kG_I ∈ u(A). This gives k = 0 for grades 1 and 2, and k = 1 for grades 3 and 4, at both signatures | transcription, branch 5 (real grades 1, 2; imaginary grades 0, 3, 4) |
| Dressing | h = (1 − X)(1 + X)⁻¹ with X = ½u_I; c_h(x) = h⁻¹xh | derivations E2.1–E2.2 |

**Response checks (convention pins; all agree).** At both signatures, ∗X(ξR) equals the documented closed form on all 20 basis tensors:
- CCC: −E_F(Ric);
- CAA: −E_F(Ric) + (S/2)E_F(g);
- CAC: −E_F(Ric) − E_F′(Ric) + (S/2)(E_F(g) + E_F′(g));
- E_OP: 2E_F(Ric) − S·E_F(g).

**Note on ξ (a documentation issue, not a disagreement in the results).**
- **What happened.** Run 1 read the B02 README formula "ξ(R) = ½ Σ R_abcd η_cη_d e^{ab} ⊗ Γ_cΓ_d" as a sum over all a, b, c, d. That is 4× the convention the rest of the B02 record uses. It gave:
  - a KN(g,g) CCC response of −24F, against B02's documented −2(n−1)F = −6F;
  - every E1 fit at 16× the Task 3 value;
  - Q(E_OP)(KN(g,g)) = −9216, against −576.
- **The fix** (`a41f016`) takes the sum over a < b, c < d. This reproduces every documented response.
- **What run 1 already matched.** Every scale-free result was already identical in run 1: the leak ranks, the centralizers, the counterexample, which fits are consistent, the zero W coefficients, the sign flips, and the −4 : −1 and −1 : −¼ ratios.
- **Consequence.** The absolute scale of Q, and so the value −576, is consistent with B02's documented response normalization. It is not fixed independently of that normalization.
- **Suggestion.** The README formula would be clearer if it stated its summation range.

## What was checked

**(a) E1, at both signatures, with the pinned and the prime pairing.**
- **The fit.** Q_X(R) = ⟨X(ξR), X(ξR)⟩ is fitted to (W·W, W·∗W, Ric₀·Ric₀, S²) on all 210 pairs i ≤ j of the 20-element basis, real and imaginary parts, for E_OP, CCC, CAA and CAC.
- **The response Gram.** The 4×4 Gram on the maps ∗⁻¹E_F(Ric), ∗⁻¹E_F′(Ric), ∗⁻¹(S E_F(g)) and ∗⁻¹(S E_F′(g)).
- **The KN(g,g) control.** Ric = 6g, Ric·Ric = 144 and W = 0. Q(E_OP) = −576, both directly and from the fit.
- **The ∗W normalization control:**
  - the tensor formula ½ε_cd^{fg}W_abfg equals a dual built entry by entry from the pinned 2-form star;
  - ∗∗W = −W;
  - W·∗(∗W) = −W·W;
  - W·D equals the fit's W·∗W;
  - W·∗W is nonzero on some basis pair.

**(b) E2, at both signatures, on all 15 blades.**
- **Group membership.** h ∈ U(A), checked as h†Ah = A.
- **Centralizer.** Its dimension is 6 − rank{[J_ab, h]}, with J_ab = ½Γ_aΓ_b. It is compared with the stabilizer recorded for every mode.
- **Leak rank.** The rank of W ↦ ⊚_h(ξW) on the 10-dimensional Weyl space, by the identity route c_h⊚(c_h⁻¹ξW), for every blade and all three modes. The brief asked only for CCC on blades 0001, 0011, 0111 and 1111.
- **Identity route against direct dressing.** The identity route equals the directly dressed operator (Φ → h⁻¹Φh) on every Weyl basis input.
- **Other controls:**
  - the covariance defect ⊚_h(c_hξW);
  - the undressed leak ranks;
  - the dressed-Q fits (a consistent value, or `None`);
  - for the four named blades under CCC, the leak rank with the opposite u_I sign (h → h⁻¹).

**Inclusion argument.** By derivations E2.6, the centralizer is contained in the stabilizer. For every blade, mode and signature, the rederived centralizer dimension equals the recorded stabilizer dimension: 3 for grade 1, 2 for grade 2, 3 for grade 3 and 6 for grade 4. So the stabilizer equals the centralizer on every member of the family.

**P4 counterexample (CCC, (3,1), blade 0111 = Γ₀Γ₁Γ₂).**
- The input is x = −12 e^{01}⊗Γ₀Γ₃ + 12 e^{03}⊗Γ₀Γ₁ − 12 e^{12}⊗Γ₂Γ₃ + 12 e^{23}⊗Γ₁Γ₂.
- x lies in ξ(Weyl): adding it leaves the rank at 10.
- The undressed CCC annihilates x, and the dressed output ⊚_h(x) is 0.
- c_h⁻¹x = hxh⁻¹ has Clifford grades {2, 3}, with two nonzero grade-3 coefficients. It lies in ker ⊚ but not in ξ(Weyl).
- The same holds with the opposite u_I sign.

## Summary table

| Quantity | Rederived | Task 2/3 (`result.json`) or plan | Agree |
|---|---|---|---|
| E1 Q pinned, E_OP, (3,1) and (1,3) | (0, 0, −4, −1), im 0 | (0, 0, −4, −1), im 0 | agree |
| E1 Q pinned, CCC literal and CAA Einstein | (0, 0, −1, −¼), im 0 | (0, 0, −1, −¼), im 0 | agree |
| E1 Q pinned, CAC chiral | 0 | 0 | agree |
| E1 Q prime, every operator | the pinned values with sign flipped | the same | agree |
| E1 response Gram, 16 entries × 2 signatures | G₁₁ = (0,0,−1,−¼), G₂₂ = (0,0,1,¼), G₁₃ = (0,0,0,−1), G₂₄ = (0,0,0,1), G₃₃ = (0,0,0,−4), G₄₄ = (0,0,0,4), the symmetric transposes G₃₁ = G₁₃ and G₄₂ = G₂₄, every other entry 0 | the same | agree |
| E1 KN(g,g): Ric, Ric·Ric, W, Q(E_OP) | 6g, 144, 0, −576 (direct and via the fit) | plan: 6g, 144, 0, −576 | agree |
| E1 ∗W normalization control | passes; non-vacuous | plan; derivations E1.2 | agree |
| E1 documented responses (4 operators × 2 signatures) | match | B02 README; phase2 README | agree |
| E2 Weyl dimension | 10 | 10 | agree |
| E2 h ∈ U(A), 15 blades × 2 | all | all accepted | agree |
| E2 centralizer = stabilizer, 15 blades × 3 modes × 2 | 3/2/3/6 by grade | 3/2/3/6 by grade | agree |
| E2 undressed leak rank, 3 modes × 2 | 0 | 0 | agree |
| E2 leak rank, 15 blades × 3 modes × 2 | grade 1: 10; grade 2: 6; grade 3: 5 (CCC, CAA), 10 (CAC); grade 4: 0 | the same | agree |
| E2 identity route = direct dressed operator | every case | (control) | agree |
| E2 covariance defect (Task 2's predicate since `0e389ea`; follows from the covariance identity) | 0 everywhere | 0 everywhere | agree |
| E2 dressed Q | `None`, except the pseudoscalar (= the undressed Q) and CAC under grade 2 (≡ 0) | the same | agree |
| E2 CCC leak rank with the opposite u_I sign, blades 0001/0011/0111/1111 | 10/6/5/0 | 10/6/5/0 | agree |
| P4 counterexample, both u_I signs: x ∈ ξ(Weyl); ⊚_h(x) = 0; grade-3 coefficient count; grades; c_h⁻¹x ∈ ker ⊚; c_h⁻¹x ∉ ξ(Weyl) | true; true; 2; {2, 3}; true; true | plan Task 4; derivations E2.5 | agree |

There are no `FINDING:` lines, because nothing disagrees.

## Not done

- **The stabilizer itself** (commutation with ρ(L) on ξ(𝓡)) was not recomputed. Only the centralizer was, as the plan specifies. Equality follows from the inclusion together with the equal dimensions.
- **The C1-kernel statements of E1.5** were not rebuilt: the radical, the null lines and the 6-dimensional zero-response directions. That would need the 40-dimensional equivariant space.
- **The singular-skip count at t = 1** was not re-run.

## Full comparison table (revision `0e389ea` output)

| quantity | rederived | Task 2/3 or plan value | agree |
|---|---|---|---|
| E1 (3, 1) Q[pinned] E_OP re | ["0", "0", "-4", "-1"] | ["0", "0", "-4", "-1"] | agree |
| E1 (3, 1) Q[pinned] E_OP im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[pinned] CCC literal re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E1 (3, 1) Q[pinned] CCC literal im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[pinned] CAA Einstein re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E1 (3, 1) Q[pinned] CAA Einstein im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[pinned] CAC chiral re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[pinned] CAC chiral im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[prime] E_OP re | ["0", "0", "4", "1"] | ["0", "0", "4", "1"] | agree |
| E1 (3, 1) Q[prime] E_OP im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[prime] CCC literal re | ["0", "0", "1", "1/4"] | ["0", "0", "1", "1/4"] | agree |
| E1 (3, 1) Q[prime] CCC literal im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[prime] CAA Einstein re | ["0", "0", "1", "1/4"] | ["0", "0", "1", "1/4"] | agree |
| E1 (3, 1) Q[prime] CAA Einstein im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[prime] CAC chiral re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) Q[prime] CAC chiral im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (3, 1) response_gram[0][0] | {"re": ["0", "0", "-1", "-1/4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "-1", "-1/4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[0][1] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[0][2] | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[0][3] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[1][0] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[1][1] | {"re": ["0", "0", "1", "1/4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "1", "1/4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[1][2] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[1][3] | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[2][0] | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[2][1] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[2][2] | {"re": ["0", "0", "0", "-4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "-4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[2][3] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[3][0] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[3][1] | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[3][2] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) response_gram[3][3] | {"re": ["0", "0", "0", "4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (3, 1) basis_dim | 20 | 20 | agree |
| E1 (3, 1) KN(g,g) Q(E_OP) (plan: -576) | ["-576", "0"] | ["-576", "0"] | agree |
| E1 (3, 1) KN(g,g) Ric.Ric (plan: 144) | "144" | "144" | agree |
| E1 (3, 1) KN(g,g) Ric=6g (plan) | true | true | agree |
| E1 (3, 1) KN(g,g) W=0 (plan) | true | true | agree |
| E1 (3, 1) KN(g,g) Q(E_OP) via fit (plan: -576) | "-576" | "-576" | agree |
| E1 (3, 1) *W normalization control (derivations E1.2) | true | true | agree |
| E1 (3, 1) W.*W nonzero on Weyl basis (non-vacuity) | true | true | agree |
| E1 (3, 1) response of E_OP = documented closed form | true | true | agree |
| E1 (3, 1) response of CCC literal = documented closed form | true | true | agree |
| E1 (3, 1) response of CAA Einstein = documented closed form | true | true | agree |
| E1 (3, 1) response of CAC chiral = documented closed form | true | true | agree |
| E1 (1, 3) Q[pinned] E_OP re | ["0", "0", "-4", "-1"] | ["0", "0", "-4", "-1"] | agree |
| E1 (1, 3) Q[pinned] E_OP im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[pinned] CCC literal re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E1 (1, 3) Q[pinned] CCC literal im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[pinned] CAA Einstein re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E1 (1, 3) Q[pinned] CAA Einstein im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[pinned] CAC chiral re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[pinned] CAC chiral im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[prime] E_OP re | ["0", "0", "4", "1"] | ["0", "0", "4", "1"] | agree |
| E1 (1, 3) Q[prime] E_OP im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[prime] CCC literal re | ["0", "0", "1", "1/4"] | ["0", "0", "1", "1/4"] | agree |
| E1 (1, 3) Q[prime] CCC literal im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[prime] CAA Einstein re | ["0", "0", "1", "1/4"] | ["0", "0", "1", "1/4"] | agree |
| E1 (1, 3) Q[prime] CAA Einstein im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[prime] CAC chiral re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) Q[prime] CAC chiral im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E1 (1, 3) response_gram[0][0] | {"re": ["0", "0", "-1", "-1/4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "-1", "-1/4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[0][1] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[0][2] | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[0][3] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[1][0] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[1][1] | {"re": ["0", "0", "1", "1/4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "1", "1/4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[1][2] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[1][3] | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[2][0] | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "-1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[2][1] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[2][2] | {"re": ["0", "0", "0", "-4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "-4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[2][3] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[3][0] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[3][1] | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "1"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[3][2] | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "0"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) response_gram[3][3] | {"re": ["0", "0", "0", "4"], "im": ["0", "0", "0", "0"]} | {"re": ["0", "0", "0", "4"], "im": ["0", "0", "0", "0"]} | agree |
| E1 (1, 3) basis_dim | 20 | 20 | agree |
| E1 (1, 3) KN(g,g) Q(E_OP) (plan: -576) | ["-576", "0"] | ["-576", "0"] | agree |
| E1 (1, 3) KN(g,g) Ric.Ric (plan: 144) | "144" | "144" | agree |
| E1 (1, 3) KN(g,g) Ric=6g (plan) | true | true | agree |
| E1 (1, 3) KN(g,g) W=0 (plan) | true | true | agree |
| E1 (1, 3) KN(g,g) Q(E_OP) via fit (plan: -576) | "-576" | "-576" | agree |
| E1 (1, 3) *W normalization control (derivations E1.2) | true | true | agree |
| E1 (1, 3) W.*W nonzero on Weyl basis (non-vacuity) | true | true | agree |
| E1 (1, 3) response of E_OP = documented closed form | true | true | agree |
| E1 (1, 3) response of CCC literal = documented closed form | true | true | agree |
| E1 (1, 3) response of CAA Einstein = documented closed form | true | true | agree |
| E1 (1, 3) response of CAC chiral = documented closed form | true | true | agree |
| E2 (3, 1) weyl_dim | 10 | 10 | agree |
| E2 (3, 1) blade 0001 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 0001 h in U(A) | true | true | agree |
| E2 (3, 1) blade 0001 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 0001 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 0001 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 0010 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 0010 h in U(A) | true | true | agree |
| E2 (3, 1) blade 0010 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 0010 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 0010 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 0011 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (3, 1) blade 0011 h in U(A) | true | true | agree |
| E2 (3, 1) blade 0011 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (3, 1) blade 0011 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (3, 1) blade 0011 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (3, 1) blade 0100 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 0100 h in U(A) | true | true | agree |
| E2 (3, 1) blade 0100 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 0100 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 0100 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 0101 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (3, 1) blade 0101 h in U(A) | true | true | agree |
| E2 (3, 1) blade 0101 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (3, 1) blade 0101 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (3, 1) blade 0101 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (3, 1) blade 0110 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (3, 1) blade 0110 h in U(A) | true | true | agree |
| E2 (3, 1) blade 0110 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (3, 1) blade 0110 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (3, 1) blade 0110 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (3, 1) blade 0111 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 0111 h in U(A) | true | true | agree |
| E2 (3, 1) blade 0111 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 0111 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 0111 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 1000 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 1000 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1000 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 1000 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 1000 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 1001 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (3, 1) blade 1001 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1001 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (3, 1) blade 1001 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (3, 1) blade 1001 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (3, 1) blade 1010 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (3, 1) blade 1010 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1010 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (3, 1) blade 1010 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (3, 1) blade 1010 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (3, 1) blade 1011 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 1011 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1011 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 1011 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 1011 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 1100 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (3, 1) blade 1100 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1100 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (3, 1) blade 1100 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (3, 1) blade 1100 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (3, 1) blade 1101 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 1101 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1101 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 1101 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 1101 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 1110 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (3, 1) blade 1110 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1110 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (3, 1) blade 1110 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (3, 1) blade 1110 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (3, 1) blade 1111 centralizer dim vs stabilizer (CCC) | 6 | 6 | agree |
| E2 (3, 1) blade 1111 h in U(A) | true | true | agree |
| E2 (3, 1) blade 1111 centralizer dim vs stabilizer (CAA) | 6 | 6 | agree |
| E2 (3, 1) blade 1111 centralizer dim vs stabilizer (CAC) | 6 | 6 | agree |
| E2 (3, 1) blade 1111 centralizer vs plan grade table | 6 | 6 | agree |
| E2 (3, 1) CCC undressed leak rank | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0001 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CCC blade 0001 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 0001 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0001 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 0001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 0010 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CCC blade 0010 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 0010 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0010 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 0010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 0011 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CCC blade 0011 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 0011 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0011 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 0011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 0100 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CCC blade 0100 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 0100 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0100 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 0100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 0101 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CCC blade 0101 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 0101 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0101 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 0101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 0110 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CCC blade 0110 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 0110 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0110 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 0110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 0111 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CCC blade 0111 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 0111 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 0111 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 0111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1000 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CCC blade 1000 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1000 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1000 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 1000 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1001 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CCC blade 1001 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1001 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1001 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 1001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1010 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CCC blade 1010 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1010 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1010 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 1010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1011 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CCC blade 1011 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1011 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1011 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 1011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1100 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CCC blade 1100 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1100 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1100 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 1100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1101 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CCC blade 1101 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1101 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1101 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 1101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1110 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CCC blade 1110 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1110 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1110 dressed Q re | null | null | agree |
| E2 (3, 1) CCC blade 1110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 1111 leak rank (identity route) | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1111 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CCC blade 1111 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CCC blade 1111 dressed Q re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E2 (3, 1) CCC blade 1111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA undressed leak rank | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0001 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAA blade 0001 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 0001 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0001 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 0001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 0010 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAA blade 0010 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 0010 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0010 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 0010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 0011 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAA blade 0011 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 0011 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0011 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 0011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 0100 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAA blade 0100 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 0100 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0100 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 0100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 0101 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAA blade 0101 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 0101 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0101 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 0101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 0110 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAA blade 0110 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 0110 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0110 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 0110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 0111 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CAA blade 0111 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 0111 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 0111 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 0111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1000 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAA blade 1000 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1000 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1000 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 1000 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1001 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAA blade 1001 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1001 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1001 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 1001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1010 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAA blade 1010 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1010 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1010 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 1010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1011 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CAA blade 1011 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1011 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1011 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 1011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1100 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAA blade 1100 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1100 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1100 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 1100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1101 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CAA blade 1101 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1101 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1101 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 1101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1110 leak rank (identity route) | 5 | 5 | agree |
| E2 (3, 1) CAA blade 1110 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1110 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1110 dressed Q re | null | null | agree |
| E2 (3, 1) CAA blade 1110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAA blade 1111 leak rank (identity route) | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1111 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAA blade 1111 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAA blade 1111 dressed Q re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E2 (3, 1) CAA blade 1111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC undressed leak rank | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0001 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 0001 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 0001 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0001 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 0001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0010 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 0010 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 0010 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0010 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 0010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0011 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAC blade 0011 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 0011 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0011 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0100 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 0100 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 0100 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0100 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 0100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0101 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAC blade 0101 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 0101 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0101 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0110 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAC blade 0110 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 0110 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0110 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 0111 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 0111 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 0111 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 0111 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 0111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1000 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 1000 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1000 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1000 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 1000 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1001 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAC blade 1001 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1001 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1001 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1010 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAC blade 1010 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1010 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1010 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1011 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 1011 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1011 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1011 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 1011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1100 leak rank (identity route) | 6 | 6 | agree |
| E2 (3, 1) CAC blade 1100 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1100 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1100 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1101 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 1101 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1101 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1101 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 1101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1110 leak rank (identity route) | 10 | 10 | agree |
| E2 (3, 1) CAC blade 1110 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1110 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1110 dressed Q re | null | null | agree |
| E2 (3, 1) CAC blade 1110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1111 leak rank (identity route) | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1111 identity route = direct dressed operator | true | true | agree |
| E2 (3, 1) CAC blade 1111 covariance defect | 0 | 0 | agree |
| E2 (3, 1) CAC blade 1111 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CAC blade 1111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (3, 1) CCC blade 0001 leak rank with opposite u_I sign (h -> h^-1) | 10 | 10 | agree |
| E2 (3, 1) CCC blade 0011 leak rank with opposite u_I sign (h -> h^-1) | 6 | 6 | agree |
| E2 (3, 1) CCC blade 0111 leak rank with opposite u_I sign (h -> h^-1) | 5 | 5 | agree |
| E2 (3, 1) CCC blade 1111 leak rank with opposite u_I sign (h -> h^-1) | 0 | 0 | agree |
| E2 (1, 3) weyl_dim | 10 | 10 | agree |
| E2 (1, 3) blade 0001 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 0001 h in U(A) | true | true | agree |
| E2 (1, 3) blade 0001 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 0001 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 0001 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 0010 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 0010 h in U(A) | true | true | agree |
| E2 (1, 3) blade 0010 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 0010 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 0010 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 0011 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (1, 3) blade 0011 h in U(A) | true | true | agree |
| E2 (1, 3) blade 0011 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (1, 3) blade 0011 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (1, 3) blade 0011 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (1, 3) blade 0100 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 0100 h in U(A) | true | true | agree |
| E2 (1, 3) blade 0100 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 0100 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 0100 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 0101 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (1, 3) blade 0101 h in U(A) | true | true | agree |
| E2 (1, 3) blade 0101 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (1, 3) blade 0101 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (1, 3) blade 0101 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (1, 3) blade 0110 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (1, 3) blade 0110 h in U(A) | true | true | agree |
| E2 (1, 3) blade 0110 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (1, 3) blade 0110 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (1, 3) blade 0110 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (1, 3) blade 0111 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 0111 h in U(A) | true | true | agree |
| E2 (1, 3) blade 0111 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 0111 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 0111 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 1000 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 1000 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1000 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 1000 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 1000 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 1001 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (1, 3) blade 1001 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1001 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (1, 3) blade 1001 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (1, 3) blade 1001 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (1, 3) blade 1010 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (1, 3) blade 1010 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1010 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (1, 3) blade 1010 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (1, 3) blade 1010 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (1, 3) blade 1011 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 1011 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1011 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 1011 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 1011 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 1100 centralizer dim vs stabilizer (CCC) | 2 | 2 | agree |
| E2 (1, 3) blade 1100 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1100 centralizer dim vs stabilizer (CAA) | 2 | 2 | agree |
| E2 (1, 3) blade 1100 centralizer dim vs stabilizer (CAC) | 2 | 2 | agree |
| E2 (1, 3) blade 1100 centralizer vs plan grade table | 2 | 2 | agree |
| E2 (1, 3) blade 1101 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 1101 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1101 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 1101 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 1101 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 1110 centralizer dim vs stabilizer (CCC) | 3 | 3 | agree |
| E2 (1, 3) blade 1110 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1110 centralizer dim vs stabilizer (CAA) | 3 | 3 | agree |
| E2 (1, 3) blade 1110 centralizer dim vs stabilizer (CAC) | 3 | 3 | agree |
| E2 (1, 3) blade 1110 centralizer vs plan grade table | 3 | 3 | agree |
| E2 (1, 3) blade 1111 centralizer dim vs stabilizer (CCC) | 6 | 6 | agree |
| E2 (1, 3) blade 1111 h in U(A) | true | true | agree |
| E2 (1, 3) blade 1111 centralizer dim vs stabilizer (CAA) | 6 | 6 | agree |
| E2 (1, 3) blade 1111 centralizer dim vs stabilizer (CAC) | 6 | 6 | agree |
| E2 (1, 3) blade 1111 centralizer vs plan grade table | 6 | 6 | agree |
| E2 (1, 3) CCC undressed leak rank | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0001 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CCC blade 0001 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 0001 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0001 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 0001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 0010 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CCC blade 0010 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 0010 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0010 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 0010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 0011 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CCC blade 0011 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 0011 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0011 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 0011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 0100 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CCC blade 0100 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 0100 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0100 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 0100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 0101 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CCC blade 0101 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 0101 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0101 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 0101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 0110 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CCC blade 0110 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 0110 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0110 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 0110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 0111 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CCC blade 0111 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 0111 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 0111 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 0111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1000 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CCC blade 1000 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1000 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1000 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 1000 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1001 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CCC blade 1001 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1001 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1001 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 1001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1010 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CCC blade 1010 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1010 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1010 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 1010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1011 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CCC blade 1011 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1011 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1011 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 1011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1100 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CCC blade 1100 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1100 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1100 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 1100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1101 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CCC blade 1101 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1101 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1101 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 1101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1110 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CCC blade 1110 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1110 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1110 dressed Q re | null | null | agree |
| E2 (1, 3) CCC blade 1110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 1111 leak rank (identity route) | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1111 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CCC blade 1111 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CCC blade 1111 dressed Q re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E2 (1, 3) CCC blade 1111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA undressed leak rank | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0001 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAA blade 0001 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 0001 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0001 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 0001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 0010 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAA blade 0010 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 0010 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0010 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 0010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 0011 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAA blade 0011 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 0011 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0011 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 0011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 0100 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAA blade 0100 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 0100 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0100 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 0100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 0101 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAA blade 0101 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 0101 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0101 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 0101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 0110 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAA blade 0110 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 0110 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0110 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 0110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 0111 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CAA blade 0111 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 0111 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 0111 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 0111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1000 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAA blade 1000 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1000 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1000 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 1000 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1001 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAA blade 1001 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1001 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1001 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 1001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1010 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAA blade 1010 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1010 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1010 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 1010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1011 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CAA blade 1011 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1011 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1011 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 1011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1100 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAA blade 1100 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1100 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1100 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 1100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1101 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CAA blade 1101 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1101 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1101 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 1101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1110 leak rank (identity route) | 5 | 5 | agree |
| E2 (1, 3) CAA blade 1110 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1110 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1110 dressed Q re | null | null | agree |
| E2 (1, 3) CAA blade 1110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAA blade 1111 leak rank (identity route) | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1111 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAA blade 1111 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAA blade 1111 dressed Q re | ["0", "0", "-1", "-1/4"] | ["0", "0", "-1", "-1/4"] | agree |
| E2 (1, 3) CAA blade 1111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC undressed leak rank | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0001 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 0001 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 0001 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0001 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 0001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0010 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 0010 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 0010 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0010 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 0010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0011 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAC blade 0011 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 0011 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0011 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0100 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 0100 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 0100 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0100 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 0100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0101 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAC blade 0101 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 0101 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0101 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0110 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAC blade 0110 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 0110 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0110 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 0111 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 0111 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 0111 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 0111 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 0111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1000 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 1000 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1000 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1000 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 1000 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1001 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAC blade 1001 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1001 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1001 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1001 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1010 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAC blade 1010 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1010 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1010 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1010 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1011 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 1011 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1011 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1011 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 1011 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1100 leak rank (identity route) | 6 | 6 | agree |
| E2 (1, 3) CAC blade 1100 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1100 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1100 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1100 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1101 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 1101 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1101 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1101 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 1101 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1110 leak rank (identity route) | 10 | 10 | agree |
| E2 (1, 3) CAC blade 1110 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1110 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1110 dressed Q re | null | null | agree |
| E2 (1, 3) CAC blade 1110 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1111 leak rank (identity route) | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1111 identity route = direct dressed operator | true | true | agree |
| E2 (1, 3) CAC blade 1111 covariance defect | 0 | 0 | agree |
| E2 (1, 3) CAC blade 1111 dressed Q re | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CAC blade 1111 dressed Q im | ["0", "0", "0", "0"] | ["0", "0", "0", "0"] | agree |
| E2 (1, 3) CCC blade 0001 leak rank with opposite u_I sign (h -> h^-1) | 10 | 10 | agree |
| E2 (1, 3) CCC blade 0011 leak rank with opposite u_I sign (h -> h^-1) | 6 | 6 | agree |
| E2 (1, 3) CCC blade 0111 leak rank with opposite u_I sign (h -> h^-1) | 5 | 5 | agree |
| E2 (1, 3) CCC blade 1111 leak rank with opposite u_I sign (h -> h^-1) | 0 | 0 | agree |
| P4 counterexample: x in xi(Weyl) | true | true | agree |
| P4 counterexample: dressed CCC output zero (blade 0111, (3,1)) | true | true | agree |
| P4 counterexample: c_h^-1 x has grade-3 parts | true | true | agree |
| P4 counterexample [phase]: grade-3 coefficient count (pinned from the inspected run) | 2 | 2 | agree |
| P4 counterexample [phase]: Clifford grades of c_h^-1 x | [2, 3] | [2, 3] | agree |
| P4 counterexample [phase]: dressed CCC output zero | true | true | agree |
| P4 counterexample [phase]: c_h^-1 x in ker CCC | true | true | agree |
| P4 counterexample [phase]: c_h^-1 x not in xi(Weyl) | false | false | agree |
| P4 counterexample [opposite_phase]: grade-3 coefficient count (pinned from the inspected run) | 2 | 2 | agree |
| P4 counterexample [opposite_phase]: Clifford grades of c_h^-1 x | [2, 3] | [2, 3] | agree |
| P4 counterexample [opposite_phase]: dressed CCC output zero | true | true | agree |
| P4 counterexample [opposite_phase]: c_h^-1 x in ker CCC | true | true | agree |
| P4 counterexample [opposite_phase]: c_h^-1 x not in xi(Weyl) | false | false | agree |
| P4 counterexample: c_h^-1 x not in xi(Weyl) | false | false | agree |
| P4 counterexample: undressed CCC kills x (P4) | true | true | agree |

comparisons: 719, disagreements: 0
