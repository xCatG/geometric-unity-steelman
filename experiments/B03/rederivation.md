# B03: independent branching and real-structure re-derivation

Author: Codex, 2026-10-15. I implemented the production experiment and already
knew its outputs. Independence means a different computation, not a blinded
second author. The calculations below import neither `gu.reps`, `gu.rarita`,
`experiments.B03.branching`, nor `gu.clifford`. Only the transcribed
[source tables](source_tables.py) and [recorded results](result.json) are read
for comparison. No result or source table is edited.

Provenance: `[ext]` for the representation calculation, `[GU-recon]` for the
dictionary and SM embedding, `[GU-orig]` for the transcribed claims.
Evidence: `verified:experiments/B03/rederivation.md`. Scope: `identity` for
the finite characters and exact matrices described here. No dynamics or
physical spectrum is derived.

## Reproduction and independence

Scratch scripts, as requested by the Task 5 brief, are untracked under
`notes:b03-task5/`: `derive_tables.py`, its freshly generated
`independent.lie`, and `derive_matrices.py`. They are cited here as local
reproduction artifacts, not tracked dependencies. Their hashes are below.
The durable mathematical route, commands, conventions and outputs are recorded
in this document; the task report retains the raw stdout and stderr.

From the repository root in native Windows PowerShell:

```powershell
# T: direct LiE plus independently parsed comparisons
.venv/Scripts/python.exe -B notes:b03-task5/derive_tables.py
# L: the actual external oracle invocation performed by T
wsl -d Ubuntu-24.04 -- bash -lc 'lie < /mnt/c/work/src/GU/notes:b03-task5/independent.lie'
# M: independently built Pauli matrices
.venv/Scripts/python.exe -B notes:b03-task5/derive_matrices.py
```

All three commands exit 0 with empty stderr. T writes fresh input instead of
executing or copying `lie/oracle.lie`; L runs LiE 2.2.2 directly. The comparison
parser is new and does not import the fixture parser. LiE uses its canonical
`res_mat(D5A1A1)` for D7. Output order is D5 Dynkin labels followed by A1_L,
A1_R Dynkin labels. An A1 label a denotes dimension a+1.

The D7 highest weights entered into LiE are omega1, omega7, omega6,
omega1+omega7 and omega1+omega6. Calling `branch`, `dim` and `tensor`
directly gives V, S+, S-, RS+, RS- and both vector-spinor products.

For D5 the doubled orthonormal fundamental weights are
(2,0,0,0,0), (2,2,0,0,0), (2,2,2,0,0), (1,1,1,1,-1), (1,1,1,1,1).
Applying the ansatz's explicit root/charge map to these gives the fresh
restriction matrix for A2 A1 T1:

```
[-1, 0, 0, 2]
[ 0,-1, 0, 4]
[ 0, 0, 0, 6]
[ 0, 0,-1, 3]
[ 0, 0, 0, 0]
```

The fourth coordinate is n=6Y. E' is generated independently by replacing it
with (-n+6X)/5, where X is the sum of doubled coordinates. The SU(5) parent
matrix follows from the reversed A4 roots and the same X; no parent labels
are inferred from dimension alone. LiE branches all four D5 inputs omega5,
omega4, omega1+omega5 and omega1+omega4 directly.

## Branching and source comparisons

Write L=(2,1), R=(1,2), 16=omega5, 16bar=omega4, H=omega1+omega5 and
Hbar=omega1+omega4. The direct output gives

```
V   = ((2,2),1) + ((1,1),10)
S+  = (L,16) + (R,16bar)
S-  = (L,16bar) + (R,16)
RS+ = (R,16) + (L,16bar) + ((3,2),16) + ((2,3),16bar) + (L,H) + (R,Hbar)
RS- = (L,16) + (R,16bar) + ((2,3),16) + ((3,2),16bar) + (R,H) + (L,Hbar)
V x S+ = RS+ + S-
V x S- = RS- + S+
```

The p.51 dictionary is fixed by the ansatz, including 144+=Hbar and
144-=H. Summing the separately transcribed blocks gives the direct LiE
branches, including the opposite-chirality trace. The ten comparisons are
six printed module entries plus four whole-fibre checks, not ten distinct
printed module entries. Both (12.20) halves agree.

The full-module forms are S4 x S10, dimension 4*32=128, and
RS4 x S10 + S4 x RS10 + S4 x S10, dimension
12*32 + 4*288 + 4*32 = 384+1152+128 = 1664.
The source p.52 tables equal 16 and 16bar. Adding the p.53 repeated rows
produces 23 terms, dimension 144, exactly Hbar. In particular the repeated
quark-doublet multiplicity is 1+2=3 and lepton-doublet multiplicity 1+1=2.
All four candidate comparisons, including every recorded missing/extra list,
agree with the independently restricted characters.

Adding S+ + S- + V x (S+ + S-) gives 128+14*128=1920. Its four
L/R x 16/16bar blocks have multiplicity 3; its four six-dimensional Lorentz
x 16/16bar blocks and four L/R x H/Hbar blocks have multiplicity 1.
The dimension is also 4*3*2*16 + 4*6*16 + 4*2*144 = 1920.
The L-minus-R multiplicity is zero for each of the four D5 parents. This
diagnostic omits the six-dimensional Lorentz carriers and is not a spectrum
or anomaly index.

## Independent exact matrices

Let X,Y,Z be the Pauli matrices. For m=(p+q)/2, construct
E_(2k)=I^tensor k tensor X tensor Z^tensor(m-k-1) and replace X by Y for
E_(2k+1). These use trailing Z strings; the production construction uses
leading strings. Conjugation by the product of controlled-Z matrices over all
tensor-factor pairs changes every leading string into its trailing string:
on a binary basis vector b this real diagonal change of basis is
(-1)^sum_(i<j)(b_i b_j). It preserves axis labels and every oriented axis pair.
Thus there is a basis difference
but no sign difference in the reported C/parity relation.

Set Gamma_a=E_a for a<p and i E_a otherwise. Every Clifford anticommutator
is checked against 2 eta_ab I. Products are computed as pairs of sparse
integer real/imaginary matrices, without floating or complex-floating arrays.
Each factor and product is monomial with unit Gaussian-integer entries;
residual entries have magnitude at most 2, so int64 cannot overflow here.
These bounded matrices are distinct from the unbounded public weight APIs
repaired in Part A.

With Omega=Gamma_0 ... Gamma_(d-1), Omega^2=(-1)^(q+d(d-1)/2).
Choose C=Omega if that exponent is even, otherwise C=i Omega. C is checked
Hermitian and C^2=I. Let h_k=-i E_(2k) E_(2k+1) and Pi=product(h_k).
This Pi records even-minus weight parity. At d=14, C/Pi=i^(q+7):
-1 for q=7 and +1 for q=5. At (3,1), the extra i in C makes C/Pi=+1.

Let B be the product of the purely imaginary Gamma matrices in increasing
axis order and J=B followed by entrywise conjugation. The script verifies
B conjugate(Gamma_a)=s Gamma_a B with a common sign s, so J commutes with
every bivector, and computes J^2=B conjugate(B) explicitly. There are six
imaginary factors in either 14D case. Their squares have products -1 at
(7,7) and +1 at (9,5); reordering contributes (-1)^15, yielding J^2=+1
and -1 respectively. It also verifies preservation of C and obtains each
Cartan weight sign directly, then reorders pairs to the pinned splits.

The five normal signs negate D5 weights, hence conjugate every D5 parent;
the horizontal sign patterns (+,-) and (-,+) both exchange the two A1
carriers up to A1 Weyl reflection. This proves the common partner rule
(a,b;lambda) <-> (b,a;conjugate(lambda)) for the inventory. At d=14 J
preserves ambient chirality. J^2=+1 allows a Majorana-Weyl fixed subspace;
J^2=-1 forbids a nonzero fixed vector because J psi=psi would imply
-psi=psi. Neither statement supplies a mass or removes a representation
block by itself.

The real/quaternionic classification also agrees with Table 2 on printed
page 9 of [Figueroa-O'Farrill, Majorana spinors](https://www.maths.ed.ac.uk/~jmf/Teaching/Lectures/Majorana.pdf):
signature difference 0 modulo 8 has real Weyl modules; difference 4 has
quaternionic Weyl modules. This is a literature cross-check of the independent
calculation, not its input.

## Per-result command/output ledger

Each line below gives a verdict, the command alias defined above, and its
actual output. `Sp/Sm/Rp/Rm` denote S+/S-/RS+/RS-. SM tuple entries are
(SU3 Dynkin a,b; SU2 Dynkin k; n); multiplicities follow each tuple.

- **agrees** — T: D7 V; output `{"dimension": 14, "branch": [[[0, 0, 0, 0, 0, 1, 1], 1], [[1, 0, 0, 0, 0, 0, 0], 1]]}`.
- **agrees** — T: D7 Sp; output `{"dimension": 64, "branch": [[[0, 0, 0, 0, 1, 1, 0], 1], [[0, 0, 0, 1, 0, 0, 1], 1]]}`.
- **agrees** — T: D7 Sm; output `{"dimension": 64, "branch": [[[0, 0, 0, 0, 1, 0, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 1]]}`.
- **agrees** — T: D7 Rp; output `{"dimension": 832, "branch": [[[0, 0, 0, 0, 1, 0, 1], 1], [[0, 0, 0, 0, 1, 2, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 1], [[0, 0, 0, 1, 0, 1, 2], 1], [[1, 0, 0, 0, 1, 1, 0], 1], [[1, 0, 0, 1, 0, 0, 1], 1]]}`.
- **agrees** — T: D7 Rm; output `{"dimension": 832, "branch": [[[0, 0, 0, 0, 1, 1, 0], 1], [[0, 0, 0, 0, 1, 1, 2], 1], [[0, 0, 0, 1, 0, 0, 1], 1], [[0, 0, 0, 1, 0, 2, 1], 1], [[1, 0, 0, 0, 1, 0, 1], 1], [[1, 0, 0, 1, 0, 1, 0], 1]]}`.
- **agrees** — T: gamma trace Sp; output `[[[0, 0, 0, 0, 0, 1, 0], 1], [[1, 0, 0, 0, 0, 0, 1], 1]]`.
- **agrees** — T: gamma trace Sm; output `[[[0, 0, 0, 0, 0, 0, 1], 1], [[1, 0, 0, 0, 0, 1, 0], 1]]`.
- **agrees** — T: p51 zeta- 832-; output `[[[0, 0, 0, 0, 1, 1, 0], 1], [[0, 0, 0, 0, 1, 1, 2], 1], [[0, 0, 0, 1, 0, 0, 1], 1], [[0, 0, 0, 1, 0, 2, 1], 1], [[1, 0, 0, 0, 1, 0, 1], 1], [[1, 0, 0, 1, 0, 1, 0], 1]]`.
- **agrees** — T: p51 zeta- 64-; output `[[[0, 0, 0, 0, 1, 1, 0], 1], [[0, 0, 0, 1, 0, 0, 1], 1]]`.
- **agrees** — T: p51 zeta- whole fibre; output `[[[0, 0, 0, 0, 1, 1, 0], 2], [[0, 0, 0, 0, 1, 1, 2], 1], [[0, 0, 0, 1, 0, 0, 1], 2], [[0, 0, 0, 1, 0, 2, 1], 1], [[1, 0, 0, 0, 1, 0, 1], 1], [[1, 0, 0, 1, 0, 1, 0], 1]]`.
- **agrees** — T: p51 zeta+ 832+; output `[[[0, 0, 0, 0, 1, 0, 1], 1], [[0, 0, 0, 0, 1, 2, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 1], [[0, 0, 0, 1, 0, 1, 2], 1], [[1, 0, 0, 0, 1, 1, 0], 1], [[1, 0, 0, 1, 0, 0, 1], 1]]`.
- **agrees** — T: p51 zeta+ 64+; output `[[[0, 0, 0, 0, 1, 0, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 1]]`.
- **agrees** — T: p51 zeta+ whole fibre; output `[[[0, 0, 0, 0, 1, 0, 1], 2], [[0, 0, 0, 0, 1, 2, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 2], [[0, 0, 0, 1, 0, 1, 2], 1], [[1, 0, 0, 0, 1, 1, 0], 1], [[1, 0, 0, 1, 0, 0, 1], 1]]`.
- **agrees** — T: p51 nu+ 64-; output `[[[0, 0, 0, 0, 1, 1, 0], 1], [[0, 0, 0, 1, 0, 0, 1], 1]]`.
- **agrees** — T: p51 nu+ whole fibre; output `[[[0, 0, 0, 0, 1, 1, 0], 1], [[0, 0, 0, 1, 0, 0, 1], 1]]`.
- **agrees** — T: p51 nu- 64+; output `[[[0, 0, 0, 0, 1, 0, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 1]]`.
- **agrees** — T: p51 nu- whole fibre; output `[[[0, 0, 0, 0, 1, 0, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 1]]`.
- **agrees** — T: 12.20 S_L; output `[[[0, 0, 0, 0, 1, 1, 0], 1], [[0, 0, 0, 1, 0, 0, 1], 1]]`.
- **agrees** — T: 12.20 S_R; output `[[[0, 0, 0, 0, 1, 0, 1], 1], [[0, 0, 0, 1, 0, 1, 0], 1]]`.
- **agrees** — T: p52_left; output `{"equals": ["16"], "terms": 6, "dimension": 16, "character": [[[0, 0, 0, 0], 1], [[0, 0, 0, 6], 1], [[0, 0, 1, -3], 1], [[0, 1, 0, -4], 1], [[0, 1, 0, 2], 1], [[1, 0, 1, 1], 1]]}`.
- **agrees** — T: p52_cousin; output `{"equals": ["16b"], "terms": 6, "dimension": 16, "character": [[[0, 0, 0, -6], 1], [[0, 0, 0, 0], 1], [[0, 0, 1, 3], 1], [[0, 1, 1, -1], 1], [[1, 0, 0, -2], 1], [[1, 0, 0, 4], 1]]}`.
- **agrees** — T: p53; output `{"equals": ["Hb"], "terms": 23, "dimension": 144, "character": [[[0, 0, 0, 0], 1], [[0, 0, 0, 6], 1], [[0, 0, 1, -9], 1], [[0, 0, 1, -3], 2], [[0, 0, 1, 3], 1], [[0, 0, 2, 0], 1], [[0, 0, 2, 6], 1], [[0, 1, 0, -4], 2], [[0, 1, 0, 2], 2], [[0, 1, 1, 5], 1], [[0, 1, 2, -4], 1], [[0, 1, 2, 2], 1], [[0, 2, 1, 1], 1], [[1, 0, 0, -8], 1], [[1, 0, 0, -2], 1], [[1, 0, 1, -5], 1], [[1, 0, 1, 1], 3], [[1, 0, 1, 7], 1], [[1, 1, 0, 0], 1], [[1, 1, 0, 6], 1], [[1, 1, 1, -3], 1], [[2, 0, 0, -4], 1], [[2, 0, 0, 2], 1]]}`.
- **agrees** — T: SM 16 E/Eprime; output `[[[0, 0, 0, 0], 1], [[0, 0, 0, 6], 1], [[0, 0, 1, -3], 1], [[0, 1, 0, -4], 1], [[0, 1, 0, 2], 1], [[1, 0, 1, 1], 1]]`.
- **agrees** — T: SU5 X 16; output `[[[0, 0, 0, 0], 5, 1], [[0, 0, 0, 1], -3, 1], [[0, 1, 0, 0], 1, 1]]`.
- **agrees** — T: SM 16b E/Eprime; output `[[[0, 0, 0, -6], 1], [[0, 0, 0, 0], 1], [[0, 0, 1, 3], 1], [[0, 1, 1, -1], 1], [[1, 0, 0, -2], 1], [[1, 0, 0, 4], 1]]`.
- **agrees** — T: SU5 X 16b; output `[[[0, 0, 0, 0], -5, 1], [[0, 0, 1, 0], -1, 1], [[1, 0, 0, 0], 3, 1]]`.
- **agrees** — T: SM H E/Eprime; output `[[[0, 0, 0, -6], 1], [[0, 0, 0, 0], 1], [[0, 0, 1, -3], 1], [[0, 0, 1, 3], 2], [[0, 0, 1, 9], 1], [[0, 0, 2, -6], 1], [[0, 0, 2, 0], 1], [[0, 1, 0, 2], 1], [[0, 1, 0, 8], 1], [[0, 1, 1, -7], 1], [[0, 1, 1, -1], 3], [[0, 1, 1, 5], 1], [[0, 2, 0, -2], 1], [[0, 2, 0, 4], 1], [[1, 0, 0, -2], 2], [[1, 0, 0, 4], 2], [[1, 0, 1, -5], 1], [[1, 0, 2, -2], 1], [[1, 0, 2, 4], 1], [[1, 1, 0, -6], 1], [[1, 1, 0, 0], 1], [[1, 1, 1, 3], 1], [[2, 0, 1, -1], 1]]`.
- **agrees** — T: SU5 X H; output `[[[0, 0, 0, 1], 7, 1], [[0, 0, 0, 2], -1, 1], [[0, 0, 1, 0], -1, 1], [[0, 1, 0, 1], 3, 1], [[1, 0, 0, 0], 3, 1], [[1, 0, 0, 1], -5, 1], [[1, 1, 0, 0], -1, 1]]`.
- **agrees** — T: SM Hb E/Eprime; output `[[[0, 0, 0, 0], 1], [[0, 0, 0, 6], 1], [[0, 0, 1, -9], 1], [[0, 0, 1, -3], 2], [[0, 0, 1, 3], 1], [[0, 0, 2, 0], 1], [[0, 0, 2, 6], 1], [[0, 1, 0, -4], 2], [[0, 1, 0, 2], 2], [[0, 1, 1, 5], 1], [[0, 1, 2, -4], 1], [[0, 1, 2, 2], 1], [[0, 2, 1, 1], 1], [[1, 0, 0, -8], 1], [[1, 0, 0, -2], 1], [[1, 0, 1, -5], 1], [[1, 0, 1, 1], 3], [[1, 0, 1, 7], 1], [[1, 1, 0, 0], 1], [[1, 1, 0, 6], 1], [[1, 1, 1, -3], 1], [[2, 0, 0, -4], 1], [[2, 0, 0, 2], 1]]`.
- **agrees** — T: SU5 X Hb; output `[[[0, 0, 0, 1], -3, 1], [[0, 0, 1, 1], 1, 1], [[0, 1, 0, 0], 1, 1], [[1, 0, 0, 0], -7, 1], [[1, 0, 0, 1], 5, 1], [[1, 0, 1, 0], -3, 1], [[2, 0, 0, 0], 1, 1]]`.
- **agrees** — T: fibre inventory; output `[[[0, 0, 0, 0, 1, 0, 1], 3], [[0, 0, 0, 0, 1, 1, 0], 3], [[0, 0, 0, 0, 1, 1, 2], 1], [[0, 0, 0, 0, 1, 2, 1], 1], [[0, 0, 0, 1, 0, 0, 1], 3], [[0, 0, 0, 1, 0, 1, 0], 3], [[0, 0, 0, 1, 0, 1, 2], 1], [[0, 0, 0, 1, 0, 2, 1], 1], [[1, 0, 0, 0, 1, 0, 1], 1], [[1, 0, 0, 0, 1, 1, 0], 1], [[1, 0, 0, 1, 0, 0, 1], 1], [[1, 0, 0, 1, 0, 1, 0], 1]]`.
- **agrees** — T: fibre dimension; output `1920`.
- **agrees** — T: chirality index; output `{"(0, 0, 0, 0, 1)": 0, "(0, 0, 0, 1, 0)": 0, "(1, 0, 0, 0, 1)": 0, "(1, 0, 0, 1, 0)": 0}`.
- **agrees** — T: 11.2 full Dirac; output `"S4 x S10 = 128"`.
- **agrees** — T: 11.3/12.22 full RS; output `"RS4 x S10 + S4 x RS10 + S4 x S10 = 1664"`.
- **agrees** — T: 12.22 imposter containment; output `"S4 x S10 contained; location/dynamics not inferred"`.
- **agrees** — T: imposter RS+ R 16; output `{"multiplicities": {"Q": 1, "dc": 1, "uc": 1, "L": 1, "ec": 1, "nuc": 1}, "max_copies": 1}`.
- **agrees** — T: imposter RS+ L 16b; output `{"multiplicities": {"Q": 0, "dc": 0, "uc": 0, "L": 0, "ec": 0, "nuc": 1}, "max_copies": 0}`.
- **agrees** — T: imposter RS+ L H; output `{"multiplicities": {"Q": 0, "dc": 1, "uc": 0, "L": 1, "ec": 0, "nuc": 1}, "max_copies": 0}`.
- **agrees** — T: imposter RS+ R Hb; output `{"multiplicities": {"Q": 3, "dc": 2, "uc": 2, "L": 2, "ec": 1, "nuc": 1}, "max_copies": 1}`.
- **agrees** — T: imposter RS- L 16; output `{"multiplicities": {"Q": 1, "dc": 1, "uc": 1, "L": 1, "ec": 1, "nuc": 1}, "max_copies": 1}`.
- **agrees** — T: imposter RS- R 16b; output `{"multiplicities": {"Q": 0, "dc": 0, "uc": 0, "L": 0, "ec": 0, "nuc": 1}, "max_copies": 0}`.
- **agrees** — T: imposter RS- R H; output `{"multiplicities": {"Q": 0, "dc": 1, "uc": 0, "L": 1, "ec": 0, "nuc": 1}, "max_copies": 0}`.
- **agrees** — T: imposter RS- L Hb; output `{"multiplicities": {"Q": 3, "dc": 2, "uc": 2, "L": 2, "ec": 1, "nuc": 1}, "max_copies": 1}`.
- **agrees** — M: output `{"signature": [1, 1], "dimension": 2, "imaginary_axes": [], "Clifford": true, "J_square": 1, "chirality_vs_parity": -1, "J_preserves_chirality": true, "natural_J_weight_signs": [1], "matched_rows": []}`.
- **agrees** — M: output `{"signature": [3, 1], "dimension": 4, "imaginary_axes": [1], "Clifford": true, "J_square": -1, "chirality_vs_parity": 1, "J_preserves_chirality": false, "natural_J_weight_signs": [-1, 1], "matched_rows": ["3,1|1,1+2,0"]}`.
- **agrees** — M: output `{"signature": [7, 7], "dimension": 128, "imaginary_axes": [1, 3, 5, 8, 10, 12], "Clifford": true, "J_square": 1, "chirality_vs_parity": -1, "J_preserves_chirality": true, "natural_J_weight_signs": [-1, -1, -1, 1, -1, -1, -1], "matched_rows": ["7,7|1,3+6,4"]}`.
- **agrees** — M: output `{"signature": [9, 5], "dimension": 128, "imaginary_axes": [1, 3, 5, 7, 10, 12], "Clifford": true, "J_square": -1, "chirality_vs_parity": 1, "J_preserves_chirality": true, "natural_J_weight_signs": [-1, -1, -1, -1, 1, -1, -1], "matched_rows": ["9,5|1,3+8,2", "9,5|3,1+6,4"]}`.

## Artifact fingerprints

- `derive_tables.py`: SHA-256 `5c6853b08b178a1fea5b52dfca0184a8f7ca83b9d5f09fefb3f80707fdde8cf0`.
- `independent.lie`: SHA-256 `cd34c527350ee30593033bb7834d4fdf108eedc92487bdf31612804948019f28`.
- `derive_matrices.py`: SHA-256 `c24dcedc5dc6842ba438fef1fcb939b9a9ce52206629cf2a09af8276960870eb`.
- Direct LiE raw stdout: SHA-256 `40b868f0c3ed5bcc03c212c654521dc1f17065e8739d7489609b38ad9f52fe18`.

No mathematical disagreement was found in these comparisons. The README
wording audit is reported separately to its owner. Scratch development
corrected whitespace handling in the LiE parser and the d=4 chirality phase
before producing this successful ledger; no production expectation was changed.
