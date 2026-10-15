# B03: spinor and Rarita–Schwinger branching, the §11.3 tables, and the "imposter generation"

Author: Claude (plan Task 5, step 1), 2026-10-15.

Inputs:
- `transcription.md` (revision 1; draft pp. 50–53, 61–62)
- `ansatz.md` (pre-registered, revision 1.3)
- `source_tables.py` (the draft's printed rows and blocks)
- `result.json` (`source_commit` 895fc08)
- `lie/oracle.out` (LiE 2.2.2 fixture, SHA-256 `576888f2…`)
- plan `docs/superpowers/plans/2026-10-15-b03-branching.md` (revision 1.2)

**Provenance.** Every result below was known before the committed run: from the LiE oracle, Claude's plan smoke test and the plan review (ansatz, "Known before the run"). None is a prediction. The committed run reproduces them with tracked code. That code is checked against an exact external fixture (LiE) and fault-tested: 297 tests pass, and 13 seeded faults each fail an assertion. Its `result.json` was regenerated identically from a clean clone at `895fc08` (Claude, P7).

## What is being compared

The draft pulls the 14-dimensional spinor and vector-spinor bundles back along ג: X^{1,3} → Y^{7,7}, with ג\*(TY) = TX ⊕ N^{6,4} (12.19). It then reads off Spin(1,3) × Spin(6,4) blocks (pp. 50–53, 61–62). On the complex side this is the branching D7 ⊃ D2 × D5, i.e. so(14,ℂ) ⊃ so(4,ℂ) × so(10,ℂ).

Notation (convention-free):
- **D7:** S₊ = ω₇ and S₋ = ω₆ (S₊ spanned by the even-minus-count weights); V = ω₁ (dimension 14); RS_± = ker(V ⊗ S_± → S_∓) (dimension 832).
- **D2 = A1_L × A1_R:** L = (2,1) and R = (1,2) are the Lorentz Weyl spinors; (3,2) and (2,3) are the Lorentz vector-spinor halves (dimension 6).
- **D5:** 16 = ω₅, 16̄ = ω₄, H = ω₁ + ω₅ = ker(10 ⊗ 16 → 16̄) (dimension 144), and its conjugate H̄.

The draft gives no highest weights, so its labels need a dictionary. This one is `[GU-recon]` and was fixed in the ansatz before the run:

| Draft | 2₊ | 2₋ | 16₊ | 16₋ | 6₊ | 6₋ | **144₊** | **144₋** | 64₋ | 64₊ | 832_± | 𝕊_L^{64} |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ours | L | R | 16 | 16̄ | (3,2) | (2,3) | **H̄** | **H** | S₊ | S₋ | RS_± | S₊ |

**The 144 labels are mixed relative to the 16 labels:** 16₊ = 16 but 144₊ = H̄. That is permitted, and it is the only assignment that matches every printed block. It is a declared convention, not a finding. Seeded fault F11 (swapping 144± for H and H̄) breaks the p. 51 match.

## The branching (convention-free, LiE-exact)

- **S₊ → (L,16) + (R,16̄)**, and S₋ → (L,16̄) + (R,16).
- **RS₊ → (R,16) + (L,16̄) + ((3,2),16) + ((2,3),16̄) + (L,H) + (R,H̄)**, and RS₋ is its mirror.
- **V ⊗ S_± = RS_± ⊕ S_∓**: the gamma trace carries the *opposite* chirality.

Each of these is an exact character equality. reps.py computes it with exact Freudenthal arithmetic, and it is compared term by term with the LiE fixture (`tests/test_reps.py`).

## Verdict

One line per draft claim, under the ansatz's verdict rules. "Under dictionary" means the table above; the convention-free form follows each line.

| Claim | Verdict | Convention-free form |
|---|---|---|
| **(11.1)** W ⊗ 𝕊 = 𝕊 ⊕ ℝ | **holds (identity, convention-free)** | V ⊗ S_± = RS_± ⊕ S_∓. The draft does not say which chirality the 𝕊 summand carries; it is the opposite one. |
| **(11.2)** 𝕊(U ⊕ V) = 𝕊(U) ⊗ 𝕊(V), full modules | **holds (identity, convention-free)** | S₊ + S₋ restricts to (L + R) ⊗ (16 + 16̄). |
| **(11.2)** chiral refinement, i.e. **(12.20)** | **holds (identity, under dictionary)**, both halves | S₊ → (L,16) + (R,16̄) ("Luminous"); S₋ → (L,16̄) + (R,16) ("Dark Decoupled Looking Glass"). |
| **(11.3)/(12.22)**, full modules | **holds (identity, convention-free)** | RS(TX ⊕ N) = RS(TX) ⊗ S(N) ⊕ S(TX) ⊗ RS(N) ⊕ S(TX) ⊗ S(N): 1664 = 384 + 1152 + 128. The S(TX) ⊗ S(N) term is contained in the full RS module. |
| **(11.3)** chiral refinement, i.e. 832_± = 𝒵 ⊕ 𝒬 ⊕ ℱ | **holds (identity, under dictionary)** | The RS₊ line above. |
| **(11.6)** and the p. 51 diagram: all 10 printed rows (ζ±, ν± and each whole fibre) | **holds (identity, under dictionary)**, 10/10 | ℱ = Lorentz spinor × 16/16̄; 𝒬 = Lorentz vector-spinor × 16/16̄; 𝒵 = Lorentz spinor × H/H̄. |
| §11.3 table 1, p. 52 ("Left Quarks …") | **equals 16 under E** | 6 aggregated terms, with no missing and no extra terms. |
| §11.3 table 2, p. 52 (the 𝒬⁺ "cousin") | **equals 16̄ under E** | 6 aggregated terms, exact. |
| §11.3 table 3, p. 53 (unlabelled 144) | **equals H̄ under E** (= 144₊) | 25 printed rows sum to **23** aggregated terms (rows 20 and 21 repeat), with no missing and no extra terms. |
| Reality, per 14D row | **holds**, 3/3 rows (see "Reality") | J² = +1 at (7,7), −1 at (9,5). |
| "a third family is merely effectively identical"; "above the dashed line is our world"; VEV decoupling; (12.21); which states are "imposters" | **unresolved (needs dynamics)** | B03 contributes data only (below). |

**The embedding E** is fixed from root data before any comparison, never fitted to the tables. SU(5) ⊂ SO(10) with SU(3) on y₁…y₃ and SU(2) on y₄, y₅, and n = 6Y. The LiE matrix for E is the images of the five D5 fundamental weights (Grok's review confirmed it is root-derived). The wrong-hypercharge impostor n = X fails the 16 fixture (fault F4). The flipped-charge control E′, n′ = (−n + 6X)/5, gives identical characters on every complete D5 module tested (`e_equals_e_prime`). So E versus E′ is not a discriminator, and the table matches do not depend on choosing between them.

SU(5) × U(1)_X parents, from `result.json` (`su5_x_parent_labels`) and checked against LiE: 16 = 10₁ + 5̄₋₃ + 1₅, and 16̄ = 1₋₅ + 5₃ + 10̄₋₁. In A4 Dynkin labels with X, H = [0001]₇ + [1000]₃ + [0010]₋₁ + [0002]₋₁ + [1001]₋₅ + [1100]₋₁ + [0101]₃, of dimensions 5, 5, 10, 15, 24, 40 and 45 (sum 144). H̄ is its conjugate.

## Reality (explicit matrices)

J = B ∘ conj, with B the product of the purely imaginary gammas. The checks are on explicit 128 × 128 monomial matrices (`gu/rarita.py`, `verify_split`). J commutes with every adjacent and every Cartan-pair generator, commutes with the RS projector Q, and preserves each ambient chirality at d = 14.

| Split | Signatures | J² | C vs parity Π | J weight signs | J partners |
|---|---|---|---|---|---|
| (7,7) \| (1,3) + (6,4) | the draft's (12.19) | **+1** | C = −Π | (+, −, −, −, −, −, −) | (a,b;λ) ↔ (b,a;λ̄) |
| (9,5) \| (1,3) + (8,2) | `[ext]` | **−1** | C = +Π | (+, −, −, −, −, −, −) | same |
| (9,5) \| (3,1) + (6,4) | `[ext]` | **−1** | C = +Π | (−, +, −, −, −, −, −) | same |
| (3,1) \| (1,1) + (2,0) | control only | −1 | C = +Π | (+, −) | J exchanges chiralities |

The J² signs match the literature (Figueroa-O'Farrill, *Majorana spinors*, Table 2). The partner map is the same in all three 14D splits. Its six pairs are (L;16) ↔ (R;16̄), (L;16̄) ↔ (R;16), (L;H) ↔ (R;H̄), (L;H̄) ↔ (R;H), ((3,2);16) ↔ ((2,3);16̄) and ((3,2);16̄) ↔ ((2,3);16).

**What J² does and does not license:**
- **J² = +1 at (7,7).** J admits a Majorana–Weyl condition Jψ = ψ on each chirality. Under it, the (R;16̄) block of S₊ is not independent: it is the conjugate of (L;16). The real Majorana–Weyl 64 then carries the content of one Weyl 16, and the same holds block by block in RS.
- **J² = −1 at (9,5).** There is no nonzero solution of Jψ = ψ. A symplectic Majorana condition needs a doublet. With one copy, (L;16) and (R;16̄) remain independent complex components.
- **Either way, the partner pairing does not remove a block by itself.** Whether the "Looking Glass" sector decouples is a statement about the operator, not about J.

**Scope of the matrix characters (Layer 1).** The RS weight character is read from Q″ = cQc⁻¹, with c = diag(1 or i) on the vector index. That conjugation is a GL(14, ℂ) similarity into so(14, ℂ), so the character is the same for every signature. It confirms the complex data, not the real form. Real-form content enters only through J and the chirality relation C = ±Π. The character extraction reads only the seven Cartan-pair blocks. It is sound only when called through `verify_split`, which first checks:
- Q² = dQ;
- γ·Q = 0;
- tr Q = 23296, split evenly between the chiralities;
- Q fixes a hand-built gamma-traceless map and kills a gamma-inserted map;
- covariance under every generator.

## The "imposter generation": data, no location verdict

The draft places the "Imposter Third Generation" in two different places:
- **(12.22)** puts it at S(TX) ⊗ S(N) ⊂ RS(TY), the ℱ-type blocks of 832 (Lorentz spinor × 16/16̄).
- **The p. 53 table** attaches the names "Imposter Quarks / Anti-Quarks / Leptons / Anti-Electron / Anti-Neutrino" to rows of the 144, i.e. 𝒵 (Lorentz spinor × H/H̄).

The p. 53 names mark rows with repeated quantum numbers, and characters cannot decide which copy is the "imposter". The allocation stays unresolved (ansatz test 6).

The records below cover both candidates in each ambient chirality (`imposter_data`). The six columns are the SM-generation multiplicities under E. The last column, k, is the largest number of complete generation patterns the block contains.

| Ambient | Candidate | Block | Q | d^c | u^c | L | e^c | ν^c | k |
|---|---|---|---|---|---|---|---|---|---|
| RS₊ | ℱ | (R;16) | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| RS₊ | ℱ | (L;16̄) | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| RS₊ | 𝒵 | (L;H) | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| RS₊ | 𝒵 | (R;H̄) | 3 | 2 | 2 | 2 | 1 | 1 | **1** |
| RS₋ | ℱ | (L;16) | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| RS₋ | ℱ | (R;16̄) | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| RS₋ | 𝒵 | (R;H) | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| RS₋ | 𝒵 | (L;H̄) | 3 | 2 | 2 | 2 | 1 | 1 | **1** |

Both candidates contain exactly one complete generation pattern per ambient chirality. That is the ℱ block carrying 16, or the 𝒵 block carrying H̄, which is also where the p. 53 table sits. **Containment does not locate a generation.** Which block, if any, yields light chiral fermions on X is a question about the operator and its vacuum, which B03 does not test.

## Mirror inventory

The full fibre ν ⊕ ζ = (S₊ + S₋) ⊕ V ⊗ (S₊ + S₋) has dimension **1920** = 128 + 14 · 128. Over D2 × D5 it has twelve blocks:
- **Spin-½ × 16-type:** each of (L;16), (L;16̄), (R;16) and (R;16̄) appears **3** times. That is once in ν, and twice in ζ: once in the gamma trace and once in RS.
- **Spin-3/2 × 16-type:** each of ((3,2);16), ((3,2);16̄), ((2,3);16) and ((2,3);16̄) appears once.
- **Spin-½ × H-type:** each of (L;H), (L;H̄), (R;H) and (R;H̄) appears once.

Every block has its J-partner in the inventory with equal multiplicity.

The complex-fibre Weyl multiplicity diagnostic χ(λ) = mult(L;λ) − mult(R;λ) is **0 for all four D5 irreps** (16, 16̄, H, H̄). The fibre as a whole is vector-like over X. This is a complex-fibre count, not an anomaly or spectrum index: it ignores the vector-spinor Lorentz blocks by definition, and says nothing about which modes are light.

## What this does not establish

- **Generations.** B03 shows that each ambient chirality's RS module contains blocks with one generation pattern in two places (ℱ ⊗ 16 and 𝒵 ⊗ H̄), and that the full fibre is vector-like. That three light generations arise, or that the third is "effectively identical", needs the operator and its spectrum.
- **Decoupling and the dashed line.** "Two separate Dirac-like operators" at zero VEV, "above the dashed line is our world", and "currently dark to us" are dynamical claims. The J pairing does not remove the mirror blocks.
- **Dark sectors.** The inventory lists every block, named or not. It does not say which are massive.
- **(12.21)** (cosmological constant ↔ spinless gauge field ↔ fermion mass) is not a representation identity and is not tested.
- **Real form beyond J.** The matrix characters are Layer 1. Signature enters only through J² and C = ±Π.
- **The §11.4 reduction route** (Pati–Salam, then U(3) × U(2)) is not tested. The tables are checked only against the SU(5) embedding E, fixed in advance. E′ gives the same characters.
