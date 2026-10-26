# B03 transcription: spinor and Rarita–Schwinger branching, GU (11.1)–(11.6), §11.3 tables, (12.18)–(12.22)

Transcriber: Claude (Opus 5.5), 2026-10-15. Revision 1.

- **Revision 0** was written before Codex's independent second reading (`notes:b03-oracle/second-reader.md`).
- **Revision 1** applies Codex's comparison (`transcription-comparison.md` in the same directory), which found no disagreement in content and asked for five corrections:
  1. the symbol gimel (ג, named on p. 26);
  2. (12.21) added;
  3. branch 7 signatures corrected;
  4. branch 4 scope narrowed;
  5. the chirality dictionary extended to 6 and 144.
- Representation facts quoted in branch 2 come from the LiE oracle run (`notes:b03-oracle/`). Claude re-derived them by explicit weight multisets (`notes:b03-transcription/weights_check.py`).
- Dimension arithmetic marked ✓ is Claude's hand check.

## Source

- Same PDF as B01/B02: SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, re-verified 2026-10-15.
- Pages read as rendered images: 50–53 (§11.1–11.4) and 61–62 (§12.9–12.10). Text extraction was used only as a cross-check.
- Cross-references followed (P11):
  - p. 22: the (6,4) vertical signature, from B01;
  - pp. 28–30: Spin(1,3) × Spin(6,4) and its reductions;
  - p. 46: definitions of ν, ζ;
  - p. 58: the "Dirac–Rarita–Schwinger" field table;
  - p. 63: footnote 13.

## Verbatim

**p. 50, (11.1).** "there is a simple rule for tensor products of defining representations and spinors whereby the tensor product"
$$W\otimes \mathbb{S}_W = \mathbb{S}_W\oplus \mathbb{R}_W \tag{11.1}$$
"breaks into a piece representing the action of gamma matrices as spinor endomorphisms and a second piece giving the pure Rarita-Schwinger spin 3/2 representation corresponding to the sum of the highest weights of the factors."

**p. 50, (11.2).** "spinor representations carry the property of the exponential …"
$$W=U\oplus V \rightsquigarrow \mathbb S(W)=\mathbb S(U\oplus V)=\mathbb S(U)\otimes\mathbb S(V) \tag{11.2}$$

**p. 50, (11.3).** "the Rarita-Schwinger representation has slightly odd behavior when applied to direct sums …"
$$\mathbb R(U\oplus V)=\mathbb R(U)\otimes\mathbb S(V)\ \oplus\ \mathbb S(U)\otimes\mathbb R(V)\ \oplus\ \mathbb S(U)\otimes\mathbb S(V) \tag{11.3}$$
"with an odd re-appearance of a final term which has purely spinorial with no 3/2 spin Rarita-Schwinger component."

**p. 50, (11.4).** "ζ represents a spinor valued 1-form and ν a spinor on Y with U representing the Horizontal and V the Vertical normal bundle N_ג to the metric as an embedding ג: X → Y."

**p. 50–51, §11.2.** The section is titled "The Three Family Problem in GU and Imposter Generations". It makes two claims:
- "a third family is merely effectively identical to the other two and, presumably, only at low energy";
- nature "is merely effectively chiral so that at a deeper level it remains intrinsically balanced between left and right".

"we will decompose our Fermionic sector under the decompositions of ג\*(𝕊(T\*Y)) and ג\*(ℝ(T\*Y)) under"
$$\gimel^*(T^*Y)=T^*X\oplus N_\gimel \tag{11.5}$$

**p. 51, the diagram (unnumbered), "our rolled up Fermionic complex".** A 0 → · → · → 0 complex with four columns. The diagram is described here; it is not reproduced.
- Column Ω¹(𝕊₋, Y¹⁴), the field ζ₋:
  - (𝒵⁻_{1/2} ⊕ 𝒬⁺_{3/2} ‑‑⊕‑‑ ℱ⁻_{1/2}) labelled Spin(7,7)⁺, 832₋,
  - ⊕ (ℱ⁻_{1/2}) Spin(7,7)⁺, 64₋.
- Column Ω¹³(𝕊₊, Y¹⁴):
  - (𝒵⁺ ⊕ 𝒬⁻ ‑‑⊕‑‑ ℱ⁺) 832₊,
  - ⊕ (ℱ⁺) 64₊.
- Middle rows:
  - Ω⁰(𝕊₊): (ℱ⁻) Spin(7,7)⁺ 64₋, the field ν₊;
  - Ω¹⁴(𝕊₋): (ℱ⁺) 64₊;
  - below the dashed line, Ω⁰(𝕊₋): (ℱ⁺) Spin(7,7)⁻ 64₊, the field ν₋;
  - Ω¹⁴(𝕊₊): (ℱ⁻) 64₋.
- Bottom: Ω¹(𝕊₊), the field ζ₊:
  - (ℱ⁺) 64₊ ⊕ (ℱ⁺ ⊕ 𝒬⁻ ⊕ 𝒵⁺) Spin(7,7)⁻ 832₊,
  - mapping to Ω¹³(𝕊₋): (ℱ⁻) 64₋ ⊕ (ℱ⁻ ⊕ 𝒬⁺ ⊕ 𝒵⁻) 832₋.

The superscripts Spin(7,7)^± on the blocks are unexplained (see branch 5).

**p. 52, (11.6).**
$$\mathcal F^\pm_{1/2}=\begin{pmatrix}2_\mp\otimes16_+\\ \oplus\\ 2_\pm\otimes16_-\end{pmatrix}\quad
\mathcal Q^\pm_{3/2}=\begin{pmatrix}6_\mp\otimes16_+\\ \oplus\\ 6_\pm\otimes16_-\end{pmatrix}\quad
\mathcal Z^\pm_{1/2}=\begin{pmatrix}2_\mp\otimes144_+\\ \oplus\\ 2_\pm\otimes144_-\end{pmatrix} \tag{11.6}$$
"for Spin(1,3) × Spin(6,4)." Then:
- "the full operator depicted decouples effectively into two separate Dirac like operators, when there is no vacuum expectation value pulling the various sub-fields of ϖ to values significantly above zero";
- "a non-chiral total theory splits at the emergent level into two separate chiral theories";
- "the one above the dashed line corresponds to matter in our world with the other sectors not labeled by ℱ to the left and above the line are currently dark to us."

**p. 52, §11.3, first table** ("internal quantum numbers … after reductions of the structure groups"). The Notation and Name(s) columns are empty. Rows (Name, Multiplicity, Dimension, Structure):

| Name | Mult. | Dim. | Structure |
|---|---|---|---|
| Left Quarks | 1 | 6 | [3 × 2]_L^{n=1} |
| Left Anti-Quarks | 1 | 3 | [3̄ × 1]_L^{n=2} |
| Left Anti-Quarks | 1 | 3 | [3̄ × 1]_L^{n=−4} |
| Left Leptons | 1 | 2 | [1 × 2]_L^{n=−3} |
| Left Anti-Lepton | 1 | 1 | [1 × 1]_L^{n=6} |
| Left Anti-Lepton | 1 | 1 | [1 × 1]_L^{n=0} |

**p. 52, second table.** "Another surprise would be a new cousin spin-3/2 'generation' 𝒬⁺_{3/2}, in which the logic of the known matters is reversed in the sense that it is right handed matter and left handed anti-matter that feel the effects of Weak-Isospin." The Names column is empty. Its rows are the conjugates of the first table: [3̄ × 2]^{−1}, [3 × 1]^{−2}, [3 × 1]^{+4}, [1 × 2]^{+3}, [1 × 1]^{−6} and [1 × 1]^{0}, all subscript L, all multiplicity 1.

**p. 53, third table (no caption).** Columns: Number, Multiplicity, Dimension, Structure, Electric Charge, Name(s). Rows are grouped by rules in the original, in this order:

| No. | Mult. | Dim. | Structure | Charge | Name |
|---|---|---|---|---|---|
| 1 | 1 | 16 | [8 × 2]^{−3} | −1, 0 | |
| 2 | 1 | 8 | [8 × 1]^{0} | 0 | |
| 3 | 1 | 8 | [8 × 1]^{6} | 1 | |
| 6 | 1 | 12 | [6̄ × 2]^{1} | +2/3, −1/3 | |
| 5 | 1 | 6 | [6 × 1]^{2} | +1/3 | |
| 4 | 1 | 6 | [6 × 1]^{−4} | −2/3 | |
| 12 | 1 | 9 | [3̄ × 3]^{2} | +4/3, +1/3, −2/3 | |
| 11 | 1 | 9 | [3̄ × 3]^{−4} | +1/3, −2/3, −5/3 | |
| 8 | 1 | 6 | [3 × 2]^{7} | +5/3, +2/3 | |
| 7 | 1 | 6 | [3 × 2]^{−5} | −1/3, −4/3 | |
| 20 | \*1 | 6 | [3 × 2]^{1} | +2/3, −1/3 | |
| 13 | 1 | 6 | [3̄ × 2]^{5} | +4/3, +1/3 | |
| 10 | 1 | 3 | [3 × 1]^{−2} | −1/3 | |
| 9 | 1 | 3 | [3 × 1]^{−8} | −4/3 | |
| 20 | \*2 | 6 | [3 × 2]^{1} | +2/3, −1/3 | Imposter Quarks |
| 18 | 2 | 3 | [3̄ × 1]^{2} | +1/3 | Imposter Anti-Quarks |
| 19 | 2 | 3 | [3̄ × 1]^{−4} | −2/3 | Imposter Anti-Quarks |
| 15 | 1 | 3 | [1 × 3]^{6} | +2, +1, 0 | |
| 16 | 1 | 2 | [1 × 2]^{−9} | −2, −1 | |
| 23 | 1 | 1 | [1 × 1]^{0} | 0 | Imposter Anti-Neutrino |
| 14 | 1 | 3 | [1 × 3]^{0} | +1, 0, −1 | |
| 21 | \*1 | 2 | [1 × 2]^{−3} | −1, 0 | Imposter Leptons |
| 22 | 1 | 1 | [1 × 1]^{6} | +1 | Imposter Anti-Electron |
| 17 | 1 | 2 | [1 × 2]^{3} | +1, 0 | |
| 21 | \*1 | 2 | [1 × 2]^{−3} | −1, 0 | |

All structures carry subscript L.
- Rows 20 and 21 appear more than once, with starred multiplicities.
- Hand check: Σ multiplicity × dimension over every printed row, counting each repeated row where it appears, is **144** ✓.
- Every row satisfies dim = dim SU(3) rep × dim SU(2) rep, and every charge list equals T₃ + n/6 over the SU(2) multiplet (script check, all 25 printed rows; `notes:b03-transcription/check_tables.{py,out}`).
- The table therefore reads as the Standard-Model content of one 144. Its caption does not say this.

**p. 53, §11.4.** The draft lists three reduction stages:
1. ג\*(T\*Y) = T\*X ⊕ N;
2. Spin(6,4) → Spin(6) × Spin(4) ≅ SU(4) × SU(2) × SU(2), "in accordance with the Pati-Salam theory";
3. → U(3) × U(2), "where a final reductive factor may be removed or not by privileging a complex volume form."

**p. 61, (12.13)–(12.17).** These are a "stylized toy example" of a Dirac spinor on Y. Here ∂̸_A ψ_L = (R/4)ψ_R and ∂̸_A ψ_R = (R/4)ψ_L, so the mass is m = R(y)/4, and the two decouple where R ≈ 0.

**p. 61, (12.18)–(12.20).**
- ג: X^{1,3} → Y^{7,7} (12.18).
- ג\*(TY^{7,7}) = TX^{1,3} ⊕ N^{6,4}_ג (12.19).
- "at the level of the chiral Weyl halves of the total Dirac Spinor we have two decompositions":
$$\gimel^*(\mathbb S^{64}_L(TY))=\overbrace{(\mathbb S^2_L(TX)\otimes\mathbb S^{16}_L(N))\oplus(\mathbb S^2_R(TX)\otimes\mathbb S^{16}_R(N))}^{\text{Luminous Light Standard Model Family Matter}}$$
$$\gimel^*(\mathbb S^{64}_R(TY))=\underbrace{(\mathbb S^2_L(TX)\otimes\mathbb S^{16}_R(N))\oplus(\mathbb S^2_R(TX)\otimes\mathbb S^{16}_L(N))}_{\text{Dark Decoupled Looking Glass Matter}} \tag{12.20}$$
- "Left handed spinors on Y do not remain exclusively Left handed on X."

**p. 62, (12.21) and context.** "for every field on Y in the Observerse, there is both a naive spin and a true spin." The example given: Ω¹(Y, ad) has naive spin one but contains "an invariant subspace that derives from Λ¹ ⊗ Λ¹ ⊂ Λ¹ ⊗ Λ\*", which is "truly spinless from the point of view of Y". So "the field playing the role of the fundamental mass for the generalized Dirac equations is actually part of the gauge potential":
$$	ext{Cosmological ‘Constant’ }\Lambda\ \leftrightarrow\ 	ext{Spinless Gauge Field}\ \leftrightarrow\ 	ext{Fermion Mass} 	ag{12.21}$$
This is not a representation identity. It is recorded because the mass mechanism it names is the dynamics B03 does not test (branch 6).

**p. 62, §12.10, (12.22).** The section is titled "Three Generations Should be Replaced by 2+1 model of two True Generations and one Effective Imposter Generation". It says "the so-called third generation of matter is instead part of pure Rarita-Schwinger Spin-3/2 matter on Y and its Spin-1/2 appearance on X is the result of branching rules under pull back":
$$\gimel^*(\mathbb R(TY))=\mathbb R(\gimel^*(TY))=\mathbb R(TX\oplus N)=\begin{pmatrix}\mathbb R(TX)\otimes\mathbb S(N)\\ \oplus\\ \mathbb S(TX)\otimes\mathbb R(N)\\ \oplus\\ \underbrace{\mathbb S(\mathbf{TX})\otimes\mathbb S(\mathbf N)}_{\text{Imposter Third Generation}}\end{pmatrix} \tag{12.22}$$
"part of the field ζ ∈ Ω¹(Y, 𝕊_R) is an ordinary second generation spinor in Ω⁰(Y, 𝕊_L) via the Dirac gamma matrix contraction while the complement ℝ_R(TY) corresponding to the sum of the highest weights contains the imposter third generation …" Footnote 13 adds: "we are speaking loosely here as if mass eigenstates and flavor eigenstates were one and the same."

## Hand dimension checks (Claude; to be replaced by oracle output)

- **Vector-spinor of D7.** 14 × 64 = 896 = 832 + 64, so dim ℝ_± = 13 · 64 = 832 ✓. This matches the 832± in the diagram and the spec's tr P = 832 on one chirality.
- **(11.6) blocks.**
  - ℱ = 2·16 + 2·16 = 64 ✓.
  - 𝒬 = 6·16 + 6·16 = 192.
  - 𝒵 = 2·144 + 2·144 = 576.
  - 𝒵 + 𝒬 + ℱ = 832 ✓.
  - Here 6 is the Spin(1,3) gamma-traceless vector-spinor (4 · 2 − 2), and 144 is the Spin(10) one (10 · 16 − 16).
- **(11.3) and (12.22) on full Dirac modules** (dim 𝕊(U) = 4, 𝕊(V) = 32, ℝ(U) = 12, ℝ(V) = 288): 12·32 + 4·288 + 4·32 = 384 + 1152 + 128 = 1664 = 13 · 128 ✓.
- **First §11.3 table.** 6 + 3 + 3 + 2 + 1 + 1 = 16. With n = 6Y and Q = T₃ + Y, it is one Standard-Model generation plus ν^c, i.e. the SO(10) 16, *if* n = 6Y (branch 4). Row 1 of the p. 53 table, [8 × 2]^{−3} with charges −1, 0, agrees with Q = T₃ + n/6.

## Symbol table

| Symbol | Meaning (as used) | Source |
|---|---|---|
| 𝕊_W, 𝕊(W) | spinor module of W; chirality halves 𝕊_±, also written 𝕊_{L/R} | (11.1), (12.20) |
| ℝ_W, ℝ(W) | gamma-traceless vector-spinor (Rarita–Schwinger), "sum of the highest weights" | (11.1), (12.22) |
| ג | the embedding X → Y (the metric as a section) | (11.4), (12.18) |
| N_ג | normal bundle, signature (6,4) | (12.19), p. 22 |
| ν, ζ | ν ∈ Ω⁰(Y, 𝕊), ζ ∈ Ω¹(Y, 𝕊) | p. 46 |
| 64±, 832± | half-spin and RS irreps of Spin(7,7) | p. 51 |
| 2±, 6±; 16±, 144± | half-spin and RS irreps of Spin(1,3) and of Spin(6,4) | (11.6) |
| ℱ, 𝒬, 𝒵 | the three blocks of (11.6) | (11.6) |
| n | U(1) charge in the tables; consistent with n = 6Y | §11.3 |

## `[GU-recon]` branches and open questions

1. **Complex versus real branching.** The draft states (11.2), (11.3) and (11.6) as representation identities "for Spin(1,3) × Spin(6,4)". At the complexified level, D7 ⊃ D2 × D5, they are standard rules to be checked by the oracle. The real-form statements are separate:
   - which 2±, 16± are complex conjugates of each other in (1,3) and (6,4);
   - whether 64± is real, quaternionic or complex in (7,7) versus (9,5).
   Spec §5 says to check complex data first.
2. **Chirality pairing.** (11.6) pairs opposite-sign chiralities, ℱ^± = 2_∓ ⊗ 16_+ ⊕ 2_± ⊗ 16_−. (12.20) pairs same-label chiralities, 𝕊_L^{64} = 𝕊_L² ⊗ 𝕊_L^{16} ⊕ 𝕊_R² ⊗ 𝕊_R^{16}. These are consistent only under a dictionary between ±, L/R and the 64± labels, and the dictionary must also cover 6± and 144±. It depends on the orientation and volume-element conventions on X, N and Y, so it is a convention, not a fact.

**Oracle (convention-free form).** Let S₊ = ω₇ and S₋ = ω₆ of D7, L = (2,1), R = (1,2), 16 = ω₅ and 16̄ = ω₄ of D5, and H = ω₁ + ω₅ (dimension 144). Then:
- S₊ → (L,16) + (R,16̄);
- RS₊ → (R,16) + (L,16̄) + ((3,2),16) + ((2,3),16̄) + (L,H) + (R,H̄);
- the gamma trace of V ⊗ S_± is S_∓ (opposite chirality).

**One dictionary that matches every printed block** of p. 51, (11.6) and (12.20). This is `[GU-recon]`; the source gives no Dynkin labels:
- 2₊ = L, 2₋ = R;
- 16₊ = 16, 16₋ = 16̄;
- 6₊ = (3,2), 6₋ = (2,3);
- 144₊ = H̄, 144₋ = H;
- 64₋ = ℱ⁻ = S₊, 64₊ = ℱ⁺ = S₋;
- 832_± = RS_±;
- 𝕊_L^{64} = S₊.

The 144 labels are mixed relative to the 16 labels. That is permitted, but it must be declared. The ansatz fixes it.
3. **Where is the "imposter third generation"?**
   - (12.22) puts it at 𝕊(TX) ⊗ 𝕊(N) inside ℝ(TY). That term is a 4 × 32 = 128 full-Dirac copy, i.e. 64 per chirality, which is the ℱ inside 832 in (11.6).
   - The p. 53 table instead attaches the names "Imposter Quarks / Anti-Quarks / Leptons / Anti-Electron / Anti-Neutrino" to rows of what sums to a 144, i.e. 𝒵.
   - Either the imposter generation is the ℱ ⊂ 832 of (12.22), with the p. 53 names marking 144 states carrying those quantum numbers, or the two passages disagree. Recorded; the ansatz must name which claim is tested.
4. **The U(1) normalization n.** It is unstated. n = 6Y matches every charge column, as checked by script on all 25 p. 53 rows; matching charges and dimension 144 do not by themselves certify a character equality. The SU(3) × SU(2) × U(1) branchings of the 16 and 144 are a *future* oracle check, once the ansatz selects the embedding. The oracle run so far covers only D5 ⊃ A4 × U(1) for the 16 and D7 ⊃ D2 × D5. Stage 3 of §11.4 says a "final reductive factor may be removed or not", so the U(1) embedding itself is a branch: via SU(5), or via U(3) × U(2) from Pati–Salam.
5. **Spin(7,7)^± superscripts on p. 51.** These are unexplained. Possibly the two halves of the complex (above and below the dashed line), or a second grading. Not used by any tested claim unless the second reader finds a definition.
6. **"Generation" claims are not branching claims.** The physics claims are three:
   - the ℱ above the dashed line is "our world";
   - the remaining sectors are dark;
   - the spectrum decouples at zero VEV.
   These need dynamics (the operator on p. 51 and (12.13)–(12.17)), which B03 does not test (spec §7 P3: branching table only). B03 can check whether every block the draft names exists with the stated dimension and chirality, and inventory every sector the draft does not name ("mirror/exotic").
7. **(9,5).** The draft computes only (7,7) → (1,3) ⊕ (6,4). For the ordered ambient (9,5), horizontal (1,3) forces N = (8,2), and horizontal (3,1) forces N = (6,4). The normals (4,6) and (2,8) belong to the globally reversed ambient (5,9). The complex branching is identical; only the real data change. The oracle notes that the half-spins are Majorana–Weyl (J² = +1) in (7,7) and quaternionic (J² = −1) in (9,5) (Figueroa-O'Farrill, *Majorana spinors*, Table 2). The same then holds for RS, by an argument still to be checked with an explicit J. This is `[ext]`.

## The draft's stated properties (to test)

- **(B1)** (11.1) for W = ℂ¹⁴: V ⊗ S_± = S_∓ ⊕ RS_± (which chirality the trace part carries is to be checked) `[GU-orig]`.
- **(B2)** (11.2): S(U ⊕ V) = S(U) ⊗ S(V), with the chiral refinement per branch 2 `[GU-orig]`.
- **(B3)** (11.3)/(12.22): RS(U ⊕ V) = RS(U) ⊗ S(V) ⊕ S(U) ⊗ RS(V) ⊕ S(U) ⊗ S(V), on full modules and chirally refined `[GU-orig]`.
- **(B4)** (11.6): 832_± = 𝒵 ⊕ 𝒬 ⊕ ℱ with the stated chirality labels, and 64_± = ℱ `[GU-orig]`.
- **(B5)** §11.3 tables: the 16, the 16̄ (the 𝒬⁺ "cousin" table) and the 144 under SU(3) × SU(2) × U(1), row by row, with charges `[GU-orig]`, U(1) embedding `[GU-recon]`.
- **(B6)** The mirror inventory: every D2 × D5 block in S_±, RS_± and V ⊗ S_±, with chirality on X, including blocks the draft does not name `[ext]` (register B03, "Gap/source").
