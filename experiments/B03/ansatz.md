# B03 ansatz: spinor and Rarita–Schwinger branching (pre-registered, revision 1.1)

Provenance:
- The draft identities are `[GU-orig]`.
- The chirality dictionary, the Standard-Model embedding and the (9,5) splits are `[GU-recon]`/`[ext]`, per `transcription.md` revision 1.
- Spec §7 P3 exit: **a branching table only, within this ansatz. No claim about light generations.**

**Revisions.**
- Revision 0 is `a0bc8e0`.
- Revision 1 (2026-10-15) applies Codex's two-subagent review (`.agent-handoff/b03-ansatz-review/result.md`, verdict *revise*, R1–R5):
  - R1: projector targets now name tr P and tr Q separately, and the RS space is im Q.
  - R2: E is pinned by explicit maps; E′ is demoted to a conjugacy control.
  - R3: a concrete gamma-to-weight adapter is added (test 0).
  - R4: p. 53 rows are aggregated before the character comparison.
  - R5: test 7 is data only, with defined counts.
- **Revision 1.1** (2026-10-15, before any production code) changes only the conventions:
  - The real axes are now Jordan–Wigner pairs (2k, 2k+1), so that every Cartan generator is diagonal in the library's basis.
  - The adapter is defined in the Euclidean frame, as in the review's chirality probe.
  - The signatures of every split are unchanged.
  - Claude's plan smoke test ran after this revision; its outcomes are not evidence.
- The review's scratch scripts computed some outcomes before revision 1. These are listed under "Known before the run". This revision pre-registers what is still unknown:
  - the row-by-row comparison of the §11.3 tables;
  - every concrete-matrix result produced by tracked code;
  - the adapter.

## Signatures, splits and real axes

The library `gu.clifford.gammas(p, q)` puts the p positive axes first (indices 0…p−1) and the q negative axes after them. The split is fixed by explicit axis lists, in this order:

| Ambient | Horizontal (signature: axes) | Normal (signature: axes) | Status |
|---|---|---|---|
| (7,7) | (1,3): pairs (6,7), (8,9) | (6,4): pairs (0,1), (2,3), (4,5), (10,11), (12,13) | the draft's split (12.19) |
| (9,5) | (1,3): pairs (8,9), (10,11) | (8,2): pairs (0,1), (2,3), (4,5), (6,7), (12,13) | `[ext]` |
| (9,5) | (3,1): pairs (6,7), (8,9) | (6,4): pairs (0,1), (2,3), (4,5), (10,11), (12,13) | `[ext]` |
| (3,1) | (1,1): pair (2,3) | (2,0): pair (0,1) | small control (P5) only |

The complex data are the same for all three 14-dimensional rows. Real-structure data are tested per row.

## Pinned conventions

- **Cartan adapter** (review R3; rev 1.1).
  - Euclidean frame: E_a = Γ_a if η_a = +1, and E_a = −iΓ_a if η_a = −1.
  - For each listed pair (a, b), h = −iE_aE_b. This is diagonal with entries ±1 in the library basis (asserted).
  - Horizontal pairs give the coordinates (y₁, y₂), and normal pairs give (y₃, …, y₇). The doubled weight of basis spinor j is y.
  - The RS weight character is read from Q″ = dδ − E_aE_b, which equals cQc⁻¹ with c = diag(1 or i) on the vector index (asserted exactly). The vectors E_a ± iE_b of a pair carry doubled weight ±2.
- **Abstract chirality.** S₊ is the span of even-minus-count weights, i.e. ω₇ of D7. The relation between `gu.clifford.chirality(p, q)` and S± is **computed and asserted per row** by test 0, not assumed.
- **D2 = A1_L × A1_R.** The A1_L doubled weight is (y₁ + y₂)/2 and the A1_R weight is (y₁ − y₂)/2. So L = (2,1) is the even horizontal half-spin, and R = (1,2) is the odd one. This reverses Bourbaki's D2 node order (review R3), on purpose.
- **D5.** 16 = ω₅ is even in (y₃…y₇), and 16̄ = ω₄.
- **Weights in reps.py.** Dynkin labels in Bourbaki order. Conversions to and from doubled orthonormal coordinates are explicit and tested.
- **Derived modules.**
  - RS_± = ker(V ⊗ S_± → S_∓) = im Q on that chirality.
  - H = ker(10 ⊗ 16 → 16̄), dimension 144.
  - (3,2) = ker((2,2) ⊗ L → R).
- **Dictionary to the draft** (transcription branch 2), `[GU-recon]`:
  - 2₊ = L, 2₋ = R;
  - 16₊ = 16, 16₋ = 16̄;
  - 6₊ = (3,2), 6₋ = (2,3);
  - **144₊ = H̄, 144₋ = H**;
  - 64₋ = S₊, 64₊ = S₋;
  - 832_± = RS_±;
  - 𝕊_L^{64} = S₊.

  "Holds" means holds under this dictionary. The README also states the convention-free form.
- **Standard-Model embedding E** (review R2). Fixed from root data, independently of the p. 53 table. In doubled orthonormal D5 coordinates y = (y₁, …, y₅):
  - SU(3) Dynkin weight ((y₂ − y₁)/2, (y₃ − y₂)/2);
  - SU(2) Dynkin weight (y₅ − y₄)/2;
  - n = n₅ = (2y₁ + 2y₂ + 2y₃ − 3y₄ − 3y₅)/2, i.e. n = 6Y.

  The parent charge X = y₁ + … + y₅ is reported alongside (SU(5) × U(1)_X labels).
- **E′ (flipped), a control only.** n′ = (−n₅ + 6X)/5. It is conjugate to E inside Spin(10) by the y₄, y₅ flip, so **every complete D5 character must give identical SM characters under E and E′**. Test 6 asserts this equality. It is not a discriminator.

## Tests and gates

| # | Test | Gate | Scope |
|---|---|---|---|
| 0 | **Adapter** (R3) | For each row of the split table: the h_k commute and square to 1; their joint eigenvalues are ±1 with multiplicity 1 per weight on the 128-dimensional Dirac module; the full weight multiset equals the D7 Dirac character; the relation C = ±Π (Π the even-minus parity) is recorded per row. **Seeded faults:** reversing one pair's orientation, and swapping the D2 factor order, must fail the labelled character comparisons below | identity |
| 1 | **`gu/reps.py` positive controls** (P2) | A1: ½ ⊗ ½ = 1 ⊕ 0 and 1 ⊗ ½ = 3/2 ⊕ ½. D5: 16 → 10₁ + 5̄₋₃ + 1₅. D7 dimensions 14/64/64/832/832. V ⊗ S_± = RS_± ⊕ S_∓. All are exact character equalities with tracked LiE fixtures. Seeded faults: a swapped spinor node, an omitted trace, and a dropped Freudenthal root contribution must fail | identity |
| 2 | **Complex branching** of S_±, RS_±, V ⊗ S_± under D7 ⊃ D2 × D5 | reps.py reproduces the LiE fixture exactly: every (a,b;λ) multiplicity, with zero remainder | identity (finite character) |
| 3 | **Explicit RS projector**: Q^a_b = dδ^a_b I − Γ^aΓ_b (Γ^a = η_aΓ_a), P = Q/d, for every row | Q² = dQ; Σ_a Γ_a Q^a_b = 0; **tr Q = 23296 (Dirac), 11648 (per chirality) at d = 14, and 48 / 24 at d = 4; equivalently tr P = 1664 / 832 and 12 / 6**; Pv = v on a nonzero gamma-traceless v; P kills a nonzero γ-inserted spinor; covariance under all adjacent Spin generators. Through the test-0 adapter, the weight character of im Q on each ambient chirality equals reps.py's RS_±, computed as tr(Q restricted to the weight space)/d after Q² = dQ is checked. A disagreement between correct matrix output and a gate first triggers gate review (P3), and is not silently ruled an implementation bug | identity |
| 4 | **Real structure** J = B ∘ conj, with B built from the monomial gammas, not by a linear solve | J commutes with all Spin generators. **At d = 14:** J preserves each ambient chirality, and J² = +1 in (7,7), −1 in (9,5) `[lit]` (Figueroa-O'Farrill, Table 2). At d = 4 the tested J exchanges chiralities; the chirality clause is not applied there. The induced J on V ⊗ S commutes with Q and has the same J². Per factor (horizontal and normal), record which conjugate pairs J exchanges | identity (explicit matrices, finite generator set; identity component) |
| 5 | **Draft identities B1–B4**: (11.1), (11.2), (11.3) on full and on chiral modules, (11.6) and (12.20) | Each printed block equals the computed block under the dictionary. Each identity gets its own line | identity |
| 6 | **Standard-Model tables B5**: branch 16, 16̄, H, H̄ under E (and E′ as a control) | **Aggregate** the source rows first (R4). Sum multiplicities over identical (SU(3), SU(2), n), giving 23 aggregated terms from the 25 p. 53 rows. Then require exact character equality with one D5 irrep's restriction, with no missing and no extra terms. Report which D5 irrep (if any) each of the three tables equals. The raw rows, names and stars are kept as metadata. The allocation of repeated copies to "Imposter" names is **not** determined by characters and stays unresolved | identity (finite character) |
| 7 | **"Imposter" data B7** (R5, data only) | For each ambient chirality and each candidate (ℱ: Lorentz 2-carriers × 16/16̄; 𝒵: Lorentz 2-carriers × H/H̄), report (i) the six SM-generation multiplicities (Q, d^c, u^c, L, e^c, ν^c) under E and (ii) the largest k such that χ − k·χ_gen ≥ 0 termwise. No location verdict follows from containment | identity (data) |
| 8 | **Mirror inventory B6** | Full ν ⊕ ζ fibre over both ambient chiralities: every (a,b;λ) with multiplicity and its J-partner. Report χ(λ) = mult(L,λ) − mult(R,λ), a *complex-fibre Weyl multiplicity diagnostic*, which is not an anomaly or spectrum index; it ignores the 6-dimensional Lorentz modules by definition | identity |

## Verdict rules (fixed now)

Each claim gets its own line, and lines are never merged.
- **(11.1), (11.2), (11.3), (11.6), (12.20), (12.22):**
  - `holds (identity, under dictionary)`; or
  - `holds (identity, convention-free)`; or
  - `mismatch` with the block.
- **Each §11.3 table:** `equals <D5 irrep> under E`, or `mismatch` with the missing and extra aggregated terms listed.
- **Reality:** `holds` or `mismatch`, per row of the J test.
- **Generation and chirality physics claims** are `unresolved (needs dynamics)`, and B03 contributes data only:
  - "a third family is merely effectively identical";
  - "above the dashed line is our world";
  - VEV decoupling;
  - (12.21);
  - which states are "imposters".

## Known before the run (not predictions)

**From the LiE oracle run and Claude's weight multisets:**
- S₊ → (L,16) + (R,16̄).
- RS₊ → (R,16) + (L,16̄) + ((3,2),16) + ((2,3),16̄) + (L,H) + (R,H̄). RS₋ is its mirror.
- V ⊗ S_± = RS_± ⊕ S_∓.
- ν ⊕ ζ: each (L|R, 16|16̄) appears 3 times, and each RS-type block once.

**From Claude's scratch reps.py** (exact Freudenthal): all of the above, reproduced from LiE's restriction matrix.

**From the review's scratch scripts** (computed before this revision):
- Complete E-restrictions of 16, 16̄, 10, H, H̄.
- E = E′ on complete characters.
- Generation-pattern counts: 16 gives 1, H̄ gives 1, H gives 0.
- χ = 0 for every D5 irrep on the full fibre.
- Library C = +Π at (3,1) and (9,5), and −Π at (7,7). This used a Euclidean Cartan ordering; test 0 re-derives it with the pinned adapter, and the sign may differ.
- tr Q = 23296 / 11648 and 48 / 24.
- J² = +1 / −1 at (7,7) / (9,5), and JQ = QJ.

**Not yet computed by anyone:** the comparison of the p. 53 table, and of the two p. 52 tables, against those restrictions.

## Inputs fixed now

- `gu.clifford` (monomial gammas, chirality) and `gu.forms`.
- New code:
  - `gu/reps.py`: A_n and D_n Freudenthal, complex characters only, exact integers, no identification by dimension alone, with a proved finite candidate bound;
  - a Rarita–Schwinger, J and adapter module beside `gu.clifford`.
- **External oracle.** LiE 2.2.2 (Ubuntu noble). The fixtures (LiE input script, raw output, version, restriction matrices, charge convention, hashes) are generated outside pytest and tracked. Tests read the fixtures and need no WSL. The fixture generator checks LiE's error text and a completion marker.
- **Seeded faults for the plan:** the review's table (`.agent-handoff/b03-ansatz-review/result.md`, "Practical plan guidance"), plus the two test-0 faults above. Each must fail an assertion and be restored by hash.
