# B03 ansatz: spinor and Rarita–Schwinger branching (pre-registered, revision 0)

Provenance:
- The draft identities are `[GU-orig]`.
- The chirality dictionary, the Standard-Model embedding and the (9,5) splits are `[GU-recon]`/`[ext]`, per `transcription.md` revision 1.
- Spec §7 P3 exit: **a branching table only, within this ansatz. No claim about light generations.**

**What is known before the run.** The LiE oracle run (`.agent-handoff/b03-oracle/`) and Claude's weight-multiset check already fixed the complex D7 ⊃ D2 × D5 tables. They are listed under "Known before the run". They are not predictions. What this ansatz pre-registers, before any production B03 code exists, is:
- the conventions;
- the dictionary;
- the Standard-Model embedding;
- the tests and their gates;
- the verdict rules.

No SU(3) × SU(2) × U(1) branching of the 16 or 144 has been computed yet. Neither has any explicit projector or J.

## Signatures and splits

Ordered (p positive, q negative), as in `gu.clifford`:

| Ambient | Horizontal | Normal | Status |
|---|---|---|---|
| (7,7) | (1,3) | (6,4) | the draft's split (12.19) |
| (9,5) | (1,3) | (8,2) | `[ext]`, horizontal order kept |
| (9,5) | (3,1) | (6,4) | `[ext]`, normal order kept |
| (3,1) | (1,1) | (2,0) | small control (P5) only |

The complex data are the same for all three 14-dimensional rows. Only real-structure data are tested per row.

## Pinned conventions

- **Weights.** D_n weights are in doubled orthonormal coordinates, i.e. integer tuples with entries ±1 for spinors and ±2 for vectors. Dynkin labels follow Bourbaki order (α_n = e_{n−1} + e_n).
- **Chiralities.**
  - S₊ of D_n is the half-spin whose weights have an even number of minus signs.
  - S₊ of D7 = ω₇ and S₋ = ω₆.
  - On X: L = (2,1) = even, R = (1,2) = odd.
  - On N: 16 = ω₅ = even, 16̄ = ω₄ = odd.
- **Splitting.** The split 14 = 4 + 10 takes the first two orthonormal coordinates to D2 and the last five to D5.
- **Derived modules.**
  - RS_± = ker(V ⊗ S_± → S_∓), the gamma contraction.
  - H = ker(10 ⊗ 16 → 16̄), of dimension 144.
  - (3,2) = ker((2,2) ⊗ L → R).
- **Dictionary to the draft** (transcription branch 2), declared and `[GU-recon]`:
  - 2₊ = L, 2₋ = R;
  - 16₊ = 16, 16₋ = 16̄;
  - 6₊ = (3,2), 6₋ = (2,3);
  - **144₊ = H̄, 144₋ = H**;
  - 64₋ = S₊, 64₊ = S₋;
  - 832_± = RS_±;
  - 𝕊_L^{64} = S₊.

  Any claim graded "holds" holds **under this dictionary**. The README must also state the convention-free form.
- **Standard-Model embedding E** (transcription branch 4): SU(3) × SU(2) × U(1)_Y ⊂ SU(5) ⊂ Spin(10). The SU(5) comes from the first four D5 simple roots with the A4 diagram reversed (as in the oracle run), and n = 6Y. Because the hypercharge axis inside Spin(10) is ambiguous, E is fixed by one requirement: the 16 must contain (3,2)_{n=1} with multiplicity 1.
  - **Alternative E′ (also run):** the flipped assignment, i.e. the other U(1) combination in SU(5) × U(1)_X ⊂ Spin(10) for which a 16 contains (3,2)_{n=1}.
  - Both are reported. Neither is tuned against the p. 53 table.

## Tests and gates

| # | Test | Gate | Scope |
|---|---|---|---|
| 1 | **`gu/reps.py` positive controls** (P2, spec §3.2): A1 spins ½ ⊗ ½ and 1 ⊗ ½; D5 16 → 10₁ + 5̄₋₃ + 1₅; D7 dims 14/64/64/832/832; V ⊗ S_± = RS_± ⊕ S_∓ | exact character equality with the LiE outputs stored in tracked fixtures; a swapped-spinor-node fault and an omitted-trace fault must fail | identity |
| 2 | **Complex branching** of S_±, RS_±, V ⊗ S_± under D7 ⊃ D2 × D5 | `reps.py` reproduces the LiE table exactly: multiplicities of every (a,b;λ), with zero remainder | identity (finite character) |
| 3 | **Explicit RS projector**: Q^a_b = dδ^a_b I − Γ^aΓ_b on the monomial gammas, in (3,1), (7,7), (9,5) | Q² = dQ; Σ_a Γ_a Q^a_b = 0; tr Q = d(d−1)·dim S (1664 Dirac, 832 per chirality at d = 14; 12 and 6 at d = 4); Spin-generator covariance; the kernel's **weight character**, computed from the Cartan generators on the monomial basis, equals the reps.py RS_± character; nonvacuity controls (a γ-inserted spinor is killed, a kernel vector-spinor is fixed) | identity |
| 4 | **Real structure** J = B ∘ conj on S and the induced J on RS (charge conjugation; spec P3 deliverable) | J commutes with the Spin generators, J preserves each chirality, and J² = +1 in (7,7) and −1 in (9,5) `[lit]` Figueroa-O'Farrill, Table 2. Induced J commutes with Q, with the same sign. Per factor, 2 of Spin(1,3) and 16 of Spin(6,4) and Spin(8,2): J maps L ↔ R and 16 ↔ 16̄ (conjugate pairs), as the oracle text predicts; recorded, not tuned | identity (explicit matrices, finite generator set) |
| 5 | **Draft identities B1–B4**: (11.1), (11.2), (11.3) on full and on chiral modules, (11.6) and (12.20) | Each printed block equals the computed block under the dictionary. Each identity gets its own line: `holds (under dictionary)` or `mismatch: <block>` | identity |
| 6 | **Standard-Model tables B5**: branch 16, 16̄ and 144 (= H̄ = 144₊ and H = 144₋) under E and E′ | Row-by-row comparison with the two p. 52 tables and all 25 p. 53 rows: SU(3) rep, SU(2) rep, n and multiplicity, counting starred repeats as printed. A row "matches" only on exact equality of (rep, rep, n, mult) | identity (finite character) |
| 7 | **"Imposter" location B7**: for ℱ ⊂ 832 (the reading of (12.22) and pp. 65 and 68) and for 𝒵 = 2 ⊗ 144 (the p. 53 names) | Report which carries the quantum numbers of one SM generation (16 under E), with multiplicity. **No verdict on "generation".** | identity (data) |
| 8 | **Mirror inventory and net chirality B6**: the full ν ⊕ ζ fibre over both ambient chiralities | List every (a,b;λ) with multiplicity and its J-partner. Net chirality index: for each D5 irrep λ, χ(λ) = mult(L,λ) − mult(R,λ). Report all; nothing is dropped | identity |

**Gate wording (P10).** Test 3's trace targets are numbers, not "the right size". Test 6 compares named rows, not dimensions. A rank-832 projector with the wrong character fails test 3.

## Verdict rules (fixed now)

Each draft claim gets its own line, and the verdict never merges lines.
- **(11.1), (11.2), (11.3), (11.6), (12.20), (12.22) as representation identities:**
  - `holds (identity, under dictionary)`; or
  - `holds (identity, convention-free)` if no dictionary choice is used; or
  - `mismatch` with the block.
- **§11.3 tables:** `matches under E` / `matches under E′` / `mismatch rows: …`, per table.
- **Reality:** `holds` per signature row of the J test; otherwise `mismatch`.
- **Generation and chirality physics claims** are out of scope for B03 and marked `unresolved (needs dynamics; see B05/B07/B09)`:
  - "a third family is merely effectively identical";
  - "matter above the dashed line is our world";
  - decoupling at zero VEV;
  - (12.21).

  B03 contributes only the data of tests 7 and 8.
- **A test-1 or test-3 failure is an implementation bug**, not a finding, if LiE and the weight-multiset route agree.

## Known before the run (from the oracle and Claude's re-derivation; not predictions)

- S₊ → (L,16) + (R,16̄); S₋ → (R,16) + (L,16̄).
- RS₊ → (R,16) + (L,16̄) + ((3,2),16) + ((2,3),16̄) + (L,H) + (R,H̄); RS₋ is its mirror. This is 64 + 192 + 576 = 832.
- V ⊗ S_± = RS_± ⊕ S_∓: the trace has the opposite chirality.
- ν ⊕ ζ over both chiralities, 1920 complex components in all:
  - each (L|R, 16|16̄) appears 3 times;
  - each RS-type block appears once.
- The four (L|R) × (16|16̄) blocks in RS_± can be matched to the printed blocks under the dictionary above. It is not yet established that (11.6) and (12.20) hold in full; that is test 5.

## Inputs fixed now

- `gu.clifford` (monomial gammas, chirality) and the existing `gu.forms`.
- New code: `gu/reps.py`, interface per the oracle proposal (complex characters only, exact integers, no dimension-only identification), and an RS projector/J module beside `gu.clifford`.
- **External oracle:** LiE 2.2.2 (Ubuntu noble package). Its outputs are stored as tracked fixtures, with the LiE input script, so tests do not need WSL at run time.
