# B07 Phase 2: the operator (9.4) actually varies to, and the second-order Lagrangian (9.11)–(9.15)

**Status:** results recorded and independently re-derived; README audited by Codex (6 findings, all resolved); register updated; P7 clean-clone reproduction passed (payload identical apart from `seconds` and `source_commit`; 387 tests passed; 13/13 seeded faults RED).

**Result, in one paragraph.** Under reading V, on the flat model, every real Spin-equivariant u(A)-preserving algebraic ⊚ was searched at the Lorentzian signatures (3,1) and (1,3). Within that space:
- there **are** operators with L = L† (C1 = 0) and B02's Einstein ratio κ = ½;
- **no nonzero operator** also passes the order-T² test C2, under any of the three readings N0, N1, N2 of [T,T].

Under reading V, (9.4) therefore does not vary to (9.7) for any **nonzero** operator in this space. Among the operators that pass C1, the obstruction is at order T². Separately, the exact variation of (9.11) differs from the printed (9.12)–(9.13) in three of four terms at the odd-q Lorentzian signatures (two of four at even q). Also, (9.14)'s kinetic term is not ordinary Yang–Mills for any map tested.

Plan: `docs/superpowers/plans/2026-10-16-b07-phase2.md`, rev 2 (`6bc202d`), approved by the user. Derivations H9–H14: `derivations.md` (`ed3f6d8`, Grok review folded in `1d9510b`). Phase 1: `../README.md` and `../transcription.md`.

## The two questions

1. **The `[ext]` repair of (9.4) → (9.7).**
   - Varying (9.4) produces the symmetrized operator ½(L + L†), with L = ⊚∘d_B (Phase 1, B07-S).
   - Is L† again algebraic on curvature?
   - Does **any** Spin-equivariant algebraic ⊚, not only B02's Shiab family, give L = L† together with κ = ½, and also pass C2 under N0, N1 and N2?
2. **The second-order Lagrangian.** Vary (9.11), I₂ = ‖Υᴮ‖², exactly and compare with (9.12)–(9.15). Record the literal mismatches `[GU-orig]` and the corrected variation `[GU-recon]`.

## Scope

- **Reading V (`[GU-recon]`)**, as in Phase 1:
  - only the ϖ direction is varied (δT = δA = α);
  - ε and the metric are fixed;
  - the pairing is the metric trace pairing ⟨a, b⟩ = ∫Tr(a∧∗b).
- **Two kinds of adjoint.**
  - For the first-order gates, L† is the wedge-integral transpose defined by ∫Tr(T∧Lα) = ∫Tr(α∧L†T) (H9, Phase 1 H2). So L and L† both map Ω¹ to Ω^{n−1}.
  - In the second-order calculation, ⊚^*, d_A^* and ∗^† are metric adjoints.
- **Flat model:** B = d, ε = 1, constant coefficients. Phase 1 H5 removes a fixed dressing. Curved backgrounds are covered only through H11's four hypotheses (below).
- **⊚ is algebraic and Spin(p,q)-equivariant.** It is not Pin- or U(A)-ad-equivariant; neither is the Shiab family.
- **Exact arithmetic throughout:** rationals and Gaussian rationals; floats are rejected at every entry point (P4).

## The search space and its dimension check (H12)

The search space B07-U is every real Spin(p,q)-equivariant map Ω²(u(A)) → Ω³(u(A)) that preserves u(A). In 4D it is **40-dimensional**.
- That number is fixed in advance by sl₂×sl₂ character theory, block by block over Clifford grades j → l. The 12 nonzero blocks have dimensions 2 or 6.
- The computed nullspace matches the count in every block, at both signatures.
- The space contains B02's 20 building blocks across bracket modes. Those span only 16 dimensions, with four exact zero relations.
- By the Hom-space argument it contains every undressed real (9.3)/(8.1) Shiab and every real mixed-mode sum (B07-M).
- It does **not** contain the raw ordinary-product reading B07-G: at (3,1) that map produces a real identity component, which lies outside u(A).

## Results (`result.json`)

The runner took 4206.4 s at `source_commit` `8a44e8c`. All computed result sections agree exactly with the plan's rev 1 smoke artifact. The scope text was corrected to specify the separate homogeneous Fourier coefficients; timing and source metadata also differ.

**4D, (3,1) and (1,3), identical at both:**

| Space | dim | C1 kernel (L = L†) | Einstein response rank on it | SO kernel (L† algebraic) | C1 + C2, N0 | N1 | N2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Unreduced B07-U | 40 | 8 | 2 | 16 | 0 | 0 | 0 |
| B02 block span | 16 | 2 | 2 | 4 | 0 | 0 | 0 |

A 0 in this table means **no nonzero operator** passes that gate.

**The C1 survivors, their Einstein response, and their C2 fate.**

At both (3,1) and (1,3), the unreduced C1 kernel has dimension 8. Responses are given in the basis (E_F Ric, E_F′ Ric, S E_F g, S E_F′ g).
- In the reported basis, two directions have responses (½, 0, −¼, 0) and (0, ±½, 0, ∓¼), with the upper signs at (3,1).
- The other six annihilate every algebraic curvature ξ(R).
- So the response image has rank 2, and every nonzero response has Einstein ratio κ = ½. Adding a response-zero direction does not change it.

In the block span, the C1 kernel has dimension 2 and response rank 2. It contains E_OP = −2·first[C](F) − second[CC](F,B) + second[AA](F,B), with response 2E_F(Ric) − S·E_F(g).

Thus L = L† and κ = ½ are attainable at order T¹. But **no nonzero operator in the entire 8-dimensional C1 kernel passes C2 under N0, N1 or N2**. Under these hypotheses, no nonzero operator in the unreduced space passes both orders.

**L† algebraic (H10).** L† = X♯∘d iff the symmetrized obstruction SO vanishes. SO's kernel has dimension 16 (unreduced) and 4 (block span). For B02's named Einstein branches CAA and CAC, SO has an exact nonzero witness (value ±4) at (3,1), (1,3), (7,7) and (9,5).

**14D, bounded witnesses (counterexample scope), E_OP at (7,7) and (9,5):**
- C1: none of the 19,200 entries checked is nonzero. That is inconclusive, not a proof.
- C2: exact nonzero witnesses under N0 (8), N1 (−16/3) and N2 (−8).
- So E_OP fails (9.7) in 14D at order T² under every normalization.
- The 14D unreduced space (≈ 3.4 × 10¹¹ matrix entries) was not searched.

**From the symbol to the operator (H11).**
- On the flat model, C1 = 0 is exactly L = L†.
- On a curved background this follows under four hypotheses:
  1. X is parallel;
  2. the form connection is torsion-free;
  3. the trace is compatible with the connection;
  4. boundary terms vanish.
- Constant Spin intertwiners are parallel when the form and internal connections come from one Spin connection. An independent u(A)-valued internal connection needs a separate check.

## The second-order Lagrangian (9.11)–(9.15) (H14)

The variation was computed from the action alone with exact Fourier modes. It was checked at (3,1), (1,3), (2,2) and (4,0), under both Hodge conventions, for CCC, CAA, CAC and E_OP. Each κ order is homogeneous in k, so the finite wavevector set decides it completely.

| (9.13) term | `[GU-orig]` as printed | `[GU-recon]` derived | Depends on |
|---|---|---|---|
| 1. d_A^*⊚^*⊚F_A | matches | the same | — |
| 2. κ₁d_A^*⊚^*T | ill-typed: ⊚^* maps Ω^{n−1} → Ω², so a ∗ is missing | κ₁d_A^*⊚^*(∗T) | — |
| 3. κ₁∗⊚F_A | wrong sign | κ₁∗^†⊚F_A = −κ₁∗⊚F_A | every signature, both conventions (even n) |
| 4. κ₁²T | right iff q is even | κ₁²∗^†∗T = (−1)^q κ₁²T | q; Phase 1 H8's four signatures all have odd q |

- (9.12)'s Id stands where ∗^† is needed.
- The adjoint is ∗^† = (−1)^{k(n−k)}∗, so ∗^†∗ = (−1)^q on Ω¹ under both conventions for even n. All 40 (n, p, convention) cases with n ∈ {4, 14} were checked.
- No match is vacuous. Terms 1, 3 and 4, and term 2 after inserting its missing ∗, are nonzero somewhere in every tested case. The literal second term is ill-typed, so the Fourier comparison uses its repaired form.

**(9.14) as ordinary Yang–Mills: no, at the principal-symbol level.**
- The criterion asks whether the flat kinetic symbol δ⊚^*⊚(iK∧·) is one nonzero multiple of the ordinary YM symbol δ(iK∧·).
- For every map tested it is not. Under the **pinned Hodge convention**, the distinct entry ratios at (3,1) and (1,3) are:
  - CCC {0, 8, 10, 14, 16, 20, 24};
  - CAA {0, 2, 4, 6, 8};
  - CAC {−8, 0, 8};
  - E_OP {0, 8, 16, 24, 32}.
- Each map also has entries where the YM symbol vanishes and its own does not: 978, 576, 1344 and 648 respectively.
- The 3D control X = id gives ratio 1 with no mismatch.
- These are entry ratios, not eigenvalues or couplings.
- ⊚^*⊚ ∝ Id fails as well, but it is only a sufficient shortcut. A nonzero multiple is impossible by rank: 96 → 64 in 4D.
- This decides **ordinary** YM only. (9.14)'s generalized packaging D^* = d_A^*⊚^*⊚ is a different statement and is not tested here.

**(9.15).** Configurations with Υ = 0 are stationary points of I₂, since δI₂ = 2⟨δΥ, Υ⟩. That is all this shows:
- it is not an equivalence between (9.15) and Υ = 0, or between (9.15) and (9.7);
- the pairing is indefinite, so it says nothing about minima or stability.

## Grade split of the C1 kernel

The exact [grade-pair survey](grade_split.py) and [recorded output](grade_split.json) locate the six zero-response directions in the flat algebraic model, at both (3,1) and (1,3). Each pair spans both directed blocks j→l and l→j. C1 splits over these unordered grade pairs because the scalar top-form pairing pairs equal Clifford grades; the equivariant space has no nonzero diagonal blocks.

| Grade pair | Span dim | C1 dim | SO dim | Einstein response dim | C1-kernel responses (a,b,c,d) | Joint N0/N1/N2 |
|---|---:|---:|---:|---:|---|---|
| 0↔1, 0↔3, 1↔4, 3↔4 (each) | 4 | 1 | 2 | 0 | (0,0,0,0) | 0/0/0 |
| 1↔2 | 12 | 2 | 4 | 1 | (½,0,−¼,0), (0,0,0,0) | 0/0/0 |
| 2↔3 | 12 | 2 | 4 | 1 | (3,1): (0,½,0,−¼), (0,0,0,0); (1,3): (0,−½,0,¼), (0,0,0,0) | 0/0/0 |
| Total | 40 | 8 | 16 | 2 | Zero-response dimension 6 | 0/0/0 |

For K = ker C1 and Z = {v ∈ K : response(v) = 0}, the canonical support data are:

| Grade pair | (dim K, dim(K ∩ block j→l), dim(K ∩ block l→j)) | (dim Z, dim(Z ∩ block j→l), dim(Z ∩ block l→j)) |
|---|---|---|
| 0↔1, 0↔3, 1↔4, 3↔4 (each) | (1,0,0) | (1,0,0) |
| 1↔2, 2↔3 (each) | (2,0,0) | (1,0,0) |

These numbers are identical at both signatures. Thus there is one zero-response line in each of the six unordered pairs, and every nonzero vector in each line uses both directed blocks. These are subspace intersections, invariant under a change of kernel basis; the displayed response representatives depend on the basis. The totals check against the universal entries of [result.json](result.json) passes for dim, C1, SO, Einstein response dimension and each joint norm. No nonzero operator in any pair passes joint C1+C2. These flat-model directions are not established operators of a non-gravitational sector.

The grade-split run took 1007.3 s at `source_commit` `3e1894cfa703f0a61401e88c9c34e170de447a90`.

## Independent re-derivation

`rederive.py` (committed `be91369` before its first run) and `rederivation.md` (`98bb832`).
- It shares only explicit gamma matrices with production (`gu.clifford`).
- It uses its own exterior and Hodge arithmetic and its own sparse exact elimination.
- It imports no B07 module, `gu.shiab` or `gu.cliffform`.
- All 18 required comparisons agree: block dimensions, 40, C1 8, Einstein 2, the joint kernels 0, block rank 16 with four relations, the star signs, CAA Fourier, and the CAA and E_OP YM ratios and mismatch counts.
- It is independent but not blind: the smoke values were known.

## GU's own claims vs GR-shaped model choices

- The tests check GU's own claims: literal CCC gives κ = 0 (B02), and C1/C2 ask whether (9.4) varies to (9.7). They are separate from the GR-shaped choices: a torsion-free form connection, a fixed metric and ε with δT = δA, Lorentzian 4D, and a flat algebraic ⊚.
- The order-T² obstruction is an algebraic identity on the flat model, not a torsion term dropped by H9. Cartan torsion of the form connection appears only in H11's curved lift of C1; the augmented torsion T is the varied field.
- Weakening H11 hypothesis 2 to "torsion trace-free" is not enough. On the parallel coframe e⁰ = dx, e¹ = dy, e² = dz − x dy, e³ = dw, the torsion is trace-free and X(β) = e²∧β is parallel with C1 = 0. Yet L†t − Lt = −t∧de², which is nonzero at t = e³. This is a hand derivation, checked by two reviewers; X is not claimed to be a Spin intertwiner.
- Varying ε, so that δT ≠ δA, is one registered `[ext]` model (B07-P2), not a demonstrated lift of the ϖ equation. At fixed ε that equation's order-T² piece is still C2 (H5).
- In the flat algebraic model at (3,1)/(1,3), the six zero-response C1 directions split as one line in each of 0↔1, 0↔3, 1↔4, 3↔4, 1↔2 and 2↔3. Every line requires both directed blocks (see [grade split](#grade-split-of-the-c1-kernel)); these are not established operators of a non-gravitational sector.

## Not covered

- **B07-Q:** the pairing is fixed. Grade-weighted pairings are Spin- but not ad-invariant.
- **B07-P2:** Palatini/BF actions with independent fields, and one-leg or ε variations.
- **B07-Bi:** a conservation or Bianchi gate.
- **B07-X:** coefficient derivatives (non-parallel Φ, or Φ depending on ϖ).
- **B07-G:** no reality-preserving completion has been fixed.
- **The 14D unreduced space.**
- **Lower-order terms beyond H11's hypotheses on non-flat backgrounds**, including torsionful form connections (above).
- **Universal coverage** holds only at the two tested Lorentzian signatures, (3,1) and (1,3).

## On `argon_b7.md`

Its conjecture that no Shiab-type operator can make L self-adjoint with a Ricci response is refuted in 4D at order T¹: E_OP and the 2-dimensional block-span C1 kernel, both of whose directions are Einstein, do it. Its proposals of a gauge-adjusted pairing and of a Palatini-type model are out of scope here (B07-Q, B07-P2).

## Files

| File | Role |
|---|---|
| `derivations.md` | H9–H14 and the register additions |
| `symmetric.py`, `universal.py`, `gates.py`, `second_order.py`, `run.py` | Production code, verbatim from the plan (`8a44e8c`) |
| `result.json` | Runner output (`a16ad79`) |
| `rederive.py`, `rederivation.md` | Independent re-derivation |
| `grade_split.py`, `grade_split.json` | Exact grade-pair survey and canonical sub-block intersections |
| `../../../tests/test_b07_phase2.py` | 27 tests; suite 392 passed; new grade-split fault P14 RED (P1–P13 RED in the earlier Phase 2 verification) |
