# B07 escape: independent Codex re-derivation

Scope: exact 4D pointwise algebra at (3,1) and (1,3), pinned Hodge convention,
algebraic curvature at T = 0, and the specified finite Cayley family. This is a
fresh implementation, not a blind prediction: the plan and derivations disclose
the expected numbers. There is no 14D, dynamical, spectrum, or phenomenology claim.

**Result after the E_OP addendum: all 192 comparisons agree, with no unavailable
rows.** E_OP fits (0, 0, -4, -1) and gives Q(KN(g,g))=-576 at both signatures.
CCC and CAA fit (0, 0, -1, -1/4); CAC fits zero, with all imaginary coefficients
zero, at both signatures. The invariant order is
(W.W, W.*W, Ric0.Ric0, S.S). All 30 independently computed centralizer dimensions
match each of the three modes' recorded `residual` values. The requested CCC
leak ranks at (3,1) are 10, 6, 5, 0 for blades 0001, 0011, 0111, 1111.

## Independence and construction

The checker imports only the standard library, SymPy, and `gammas` from
`gu.clifford`. It does not import the producing operators, curvature helpers,
adjoint helpers, or another experiments module. The forbidden implementation
files and the previous re-derivation were not opened. `result.json` is read only
as comparison data; it does not supply basis vectors, operators, or fit values
to the independent calculations.

Formula sources are `escape/derivations.md`, `B02/transcription.md`,
`B02/proofs.md`, `B02/README.md`, `B07/phase2/derivations.md`, and
`gu/clifford.py`. The addendum additionally permits `B07/phase2/README.md`,
which supplies E_OP's three-block definition. Repository `docs/methods.md` and the plan's mathematical and
Task 4 instructions supply the procedure. Expected values were known before
execution. In particular, the methods retrospective already mentions the
earlier worker's normalization ambiguity; no discovery priority is claimed here.

1. Start with the 21 symmetric pair tensors in Sym^2(Lambda^2), impose all
   cyclic Bianchi equations, and compute a rational nullspace of dimension 20.
   The Ricci contraction's nullspace gives a 10-dimensional Weyl basis.
2. Split R into W, Ric0, S using
   W = R - KN(g,Ric)/2 + S KN(g,g)/12. Independently check that its Ricci
   contraction vanishes on the whole curvature basis.
3. Represent every form coefficient by an actual 4 by 4 gamma matrix. Construct
   the pinned star from wedge orientation and the metric; construct both
   brackets by matrix multiplication; assemble (9.3) directly, including its
   nested term. Use Phi=(F,B) for CCC/CAA and (F+Fprime,Bprime) for CAC.
   For E_OP, independently build the raw first and nested second blocks, with
   the latter excluding (9.3)'s external -1/2. Apply the newly permitted
   formula -2 first[C](F) - second[CC](F,B) + second[AA](F,B).
4. Pair outputs using Tr(x wedge *y)/4, with the actual matrix trace. Fit all
   210 polarized basis pairs to the four invariants, checking exact consistency
   and rank 4. The nonzero output check includes CAC, whose quadratic form is
   zero despite nonzero operator responses.
5. Compute each centralizer as 6 minus the exact real rank of the six matrix
   commutators [Gamma_a Gamma_b,h]. Separating real and imaginary coordinates
   prevents an unintended complex dimension count. Each h also satisfies
   h^dagger A h=A by direct matrix computation with a Hermitian timelike gamma
   product. This uses no membership helper from the producing code.
6. Compute the four CCC leaks using c_h shiab(c_h^-1 xiW), with the independently
   assembled shiab. Check the transported Weyl subspace gives zero too.

All numeric claim paths use exact rational/Gaussian-rational arithmetic. The
coercion gate rejects binary floats, SymPy floats, and Python complex values;
it preserves 2/3 and 2^64. Ranks and nullspaces use rational elimination, with
no modular ranks. Runtime measurement uses integer nanoseconds.

## Findings and their disposition

**FINDING (resolved by the addendum): E_OP was not independently reconstructible
from the original permitted formula documents.** Those documents named it,
stated its expected Q and control, and described the general block family, but
did not specify its three block coefficients. The initial report correctly
left two fits and two KN(g,g) controls unavailable rather than infer an operator
from Q. The addendum identifies an orchestrator omission and now permits
`B07/phase2/README.md:63`, which explicitly defines E_OP. Its three-block
formula has now been implemented and all four rows agree. No production
expectation or protected source file was changed.

The block convention follows the bracket and star placement of B02 (9.3):
first[m](Phi)(x) = [Phi wedge *x]_m, and
second[m1,m2](Phi1,Phi2)(x) = *[Phi1 wedge *[Phi2 wedge *x]_m1]_m2.
The second block has no external -1/2. This also follows from the newly
allowed README's stated linear response: B02's formulas give
*first[C](F)(xiR)=-E_F(Ric), *second[CC](F,B)(xiR)=0, and
*second[AA](F,B)(xiR)=-S E_F(g). Hence the stated E_OP combination has
*E_OP(xiR)=2E_F(Ric)-S E_F(g). The checker verifies this independently on all
20 curvature basis inputs at both signatures before computing its quadratic
fit. Neither a block coefficient nor its normalization is fitted to expected Q.

**FINDING: the B02 README's xi summation range is unstated.** The reconstruction
uses xi(R) = (1/2) sum_(a<b,c<d) R_abcd eta_c eta_d e^ab Gamma_c Gamma_d.
This is pinned by the same allowed README's independent KN(g,g) controls:
*CCC(xi)=-6F and *CAA(xi)=6F in four dimensions. A sum over all ordered pairs
with the printed 1/2 would be four times this xi and sixteen times Q. The
precommitted xi-scale fault explicitly tests that error and is rejected.
Resolution: the summation ranges are stated in this checker and this report;
the original documents and expectations remain unchanged.

**FINDING: the first checker revision returned exit 1 for collected mathematical
disagreements, while P2 asks for an assertion failure.** All three initial fault
runs detected the intended mathematical discrepancies. A subsequent code-only
commit replaces that exit gate with an assertion after printing every comparison.
The baseline and all three faults are rerun from that committed revision; the
mathematical formulas and expectations are unchanged.

No unseeded numerical disagreement occurred. All deliberate fault discrepancies
are retained below and in their complete run logs; they are not findings against
Task 2/3.

## Hand controls and P4 witness

The hand Weyl tensor has only diagonal pair components
W_abab=eta_a eta_b k_ab, with k_01=k_23=1, k_02=k_13=-1,
k_03=k_12=0, extended by pair antisymmetry. Its Ricci tensor vanishes and
W.W=16. Construct D=*W independently using the complementary pair, so the
two antisymmetric terms have already canceled the factor 1/2. The executable
full epsilon sum reproduces D and gives W.*D=-16. The mixed Weyl tensor W+D
has (W+D).*(W+D)=-32; this nonzero parity-odd control detects a missing 1/2
even though the fitted parity-odd coefficients vanish.

KN(g,g) independently gives Ric=6g, S=24 and Ric.Ric=144 at both signatures.
Its named-branch responses pin xi as above. The independently assembled E_OP
now gives Q(E_OP)=-576 directly at both signatures.

The exact supplied P4 witness at (3,1) belongs to xi(Weyl), checked by adjoining
it to the independently built Weyl embedding and obtaining rank 10. For blade
0111, its dressed CCC output is zero. Its transported input c_h^-1 x has the
following nonzero grade-3 Clifford coefficients, keyed by (form, Clifford)
bitmask:

| Key | Coefficient |
|---|---|
| (3,14) | 160i/3 |
| (6,11) | 160i/3 |

Thus membership in the transported Weyl subspace is sufficient but not necessary
for zero dressed output. The exact condition is c_h^-1 x in ker(shiab).

For the centralizers, [L,h]=0 implies the simultaneous spin action commutes with
c_h and with undressed shiab, hence with c_h shiab c_h^-1. The independently
computed centralizer is therefore contained in the operator stabilizer. Equality
of its dimension with the recorded stabilizer dimension establishes equality
on these finite family members, conditional on the recorded stabilizer results.
The stabilizers themselves are not recomputed here.

## Seeded faults

All fault switches are precommitted and affect this independent checker only.
They do not modify the production implementation or its expected results.
The following three counts describe the original, pre-addendum checker runs;
the two added E_OP faults are recorded separately below.

| Fault | Intended mathematical detection at each signature | Total discrepancies |
|---|---|---|
| xi-scale: xi coefficient 1/2 to 2 | CCC/CAA real fits become (0,0,-16,-4); both KN response comparisons fail | 8 |
| dual-half: dual coefficient 1/2 to 1 | Hand dual equality fails; W.*D becomes -32 instead of -16; mixed value becomes -64 instead of -32 | 6 |
| scalar-sign: outer -1/2 to +1/2 | CAA real fit becomes (0,0,-1,-9/4); CAA KN response comparison fails | 4 |

FINDING (seeded xi-scale): all eight discrepancies are the two named real fits
and two KN response comparisons at each signature. Resolution: disable the
deliberate switch; the unchanged baseline passes.

FINDING (seeded dual-half): all six discrepancies are the three dual controls
at each signature. Resolution: disable the deliberate switch; the unchanged
baseline passes.

FINDING (seeded scalar-sign): all four discrepancies are the CAA real fit and
CAA KN response comparison at each signature. Resolution: disable the deliberate
switch; the unchanged baseline passes.

## Runs and provenance

Initial producing commit: `acd9783d7bbce857b840b77e3e3801fe388f5ce8`, committed
before the first attempted execution. Every run preserves a separate complete
log. The first attempt was blocked by uv cache access before Python started;
it is retained as an infrastructure failure, not a mathematical run. Subsequent
runs used the authorized uv cache access. The checker records HEAD and checks
that it is unchanged at the end.

Original pre-addendum final producing commit: `80b81e22bb9b2c517448f47813f7608c92db3f79`.
The only change from the initial producing commit is the final assertion gate.
The two baseline comparison tables are identical (192 lines including the
header: 186 agreements and four unavailable rows). Commands are
`uv run python -m experiments.B07.escape.rederive_codex` and that same command
with `--fault xi-scale`, `--fault dual-half`, or `--fault scalar-sign`.

| Log | Producing commit | Checker milliseconds | Wall milliseconds | Exit and result |
|---|---|---:|---:|---|
| run-01.log | acd9783 | not started | 233 | 2; uv cache access failure |
| run-02.log | acd9783 | 26650 | 27666 | 0; 186 agree, 0 disagree, 4 unavailable |
| fault-xi-scale.log | acd9783 | 31788 | 32553 | 1; 8 deliberate discrepancies |
| fault-dual-half.log | acd9783 | 34528 | 35323 | 1; 6 deliberate discrepancies |
| fault-scalar-sign.log | acd9783 | 33620 | 34411 | 1; 4 deliberate discrepancies |
| run-03.log | 80b81e2 | 29705 | 30450 | 0; 186 agree, 0 disagree, 4 unavailable |
| fault-xi-scale-02.log | 80b81e2 | 32417 | 33270 | 1; assertion on 8 mathematical discrepancies |
| fault-dual-half-02.log | 80b81e2 | 32007 | 32836 | 1; assertion on 6 mathematical discrepancies |
| fault-scalar-sign-02.log | 80b81e2 | 33152 | 33930 | 1; assertion on 4 mathematical discrepancies |

The final fault failures were inspected: each reaches the mathematical
comparison assertion, with exactly the discrepancies listed above. None fails
on an import, syntax error, or unrelated exception. Faults run in separate
processes and leave the committed code unchanged.

A separate read-only adversarial review, limited to this checker and the same
allowed sources, found no high-confidence correctness defect. It also confirmed
the E_OP source limitation. That reviewer did not execute the checker; execution
evidence is the recorded runs above. An optional local strengthening of the
witness membership assertion was deferred: explicitly compare rank([A|x]) to
rank(A), although xi is injective on the proven 10-dimensional Weyl basis and
the blade-0001 leak rank independently establishes rank 10 on its image.

## E_OP addendum execution

Producing commit: `50732749a95fd9c9df53a73e8bf3d7b8f39864b1`, committed before
the extended checker's first run. This adds the raw block construction, four
formerly unavailable comparisons, and two linear-response checks. Existing
named-branch, centralizer, leak, and witness calculations are unchanged.

The command remains `uv run python -m experiments.B07.escape.rederive_codex`.
Its addendum `run-01.log` records 192 agreements, zero disagreements, zero
unavailable rows, exit 0, checker time 29874 ms and wall time 30686 ms.
This log is distinct from the original pre-addendum `run-01.log` above.

All 186 previous agreement rows are identical to the prior baseline. The four
previously unavailable rows now agree, and the two additional linear-response
checks agree. No unseeded numerical discrepancy occurred in the addendum.

Two precommitted fault switches test the added E_OP implementation. Each is
run by appending the named `--fault` value to the baseline command, and each
fails the mathematical comparison assertion, not an import or unrelated check.

| Addendum log | Checker milliseconds | Wall milliseconds | Result |
|---|---:|---:|---|
| fault-eop-first-sign.log | 33748 | 34689 | Exit 1; 186 agree, 6 disagree, 0 unavailable |
| fault-eop-second-scale.log | 34943 | 35759 | Exit 1; 186 agree, 6 disagree, 0 unavailable |

**FINDING (seeded eop-first-sign):** changing -2 first[C] to +2 first[C]
fails the documented linear-response check at both signatures, changes each
real fit to (0,0,-4,-9) with zero imaginary part, and changes each KN(g,g)
value to -5184. These are all six discrepancies. Resolution: without the
deliberate switch, the same committed implementation gives the six expected
values. No production code or expectation was changed.

**FINDING (seeded eop-second-scale):** changing +second[AA] to +second[AA]/2
fails the documented linear-response check at both signatures, changes each
real fit to (0,0,-4,0) with zero imaginary part, and changes each KN(g,g)
value to 0. These are all six discrepancies. Resolution: without the
deliberate switch, the same committed implementation gives the six expected
values. No production code or expectation was changed.

A follow-up read-only adversarial review checked the extension against the
newly permitted source and found no substantive defect. It confirmed the raw
second-block convention and the linear-response derivation. That reviewer
did not execute code.

## Complete addendum baseline comparison table

Every executed comparison is reproduced verbatim
below. The expected column comes from Task 2/3 `result.json` where present;
adapter, basis-split, U(A), normalization, and witness controls use the explicit
documented or hand-derived values described above.

| Quantity | Independent value | Task 2/3 or documented control | Comparison |
|---|---|---|---|
| exact rational adapter | 2/3 | 2/3 | agree |
| exact large integer adapter | 18446744073709551616 | 18446744073709551616 | agree |
| inexact inputs rejected | 3 | 3 | agree |
| (3,1) curvature dimension | 20 | 20 | agree |
| (3,1) Weyl dimension | 10 | 10 | agree |
| (3,1) Weyl projection has zero Ricci | True | True | agree |
| (3,1) invariant design rank | 4 | 4 | agree |
| (3,1) CCC nonzero response exists | True | True | agree |
| (3,1) Q(CCC) re fit (210 pairs) | (0, 0, -1, -1/4) | (0, 0, -1, -1/4) | agree |
| (3,1) Q(CCC) im fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (3,1) CCC undressed Weyl rank | 0 | 0 | agree |
| (3,1) CAA nonzero response exists | True | True | agree |
| (3,1) Q(CAA) re fit (210 pairs) | (0, 0, -1, -1/4) | (0, 0, -1, -1/4) | agree |
| (3,1) Q(CAA) im fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (3,1) CAA undressed Weyl rank | 0 | 0 | agree |
| (3,1) CAC nonzero response exists | True | True | agree |
| (3,1) Q(CAC) re fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (3,1) Q(CAC) im fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (3,1) CAC undressed Weyl rank | 0 | 0 | agree |
| (3,1) E_OP linear response 2E_F(Ric)-S E_F(g) (20 inputs) | True | True | agree |
| (3,1) Q(E_OP) re/im fits | ((0, 0, -4, -1), (0, 0, 0, 0)) | ((0, 0, -4, -1), (0, 0, 0, 0)) | agree |
| (3,1) hand W Ricci | (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) | (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) | agree |
| (3,1) dual matches hand complement construction | True | True | agree |
| (3,1) W.W nonvacuity | 16 | 16 | agree |
| (3,1) W.*(hand *W) | -16 | -16 | agree |
| (3,1) mixed W.*W normalization | -32 | -32 | agree |
| (3,1) KN(g,g) Ricci=6g | True | True | agree |
| (3,1) KN(g,g) scalar | 24 | 24 | agree |
| (3,1) KN(g,g) Ric.Ric | 144 | 144 | agree |
| (3,1) KN(g,g) *CCC(xi)=(-6)F | True | True | agree |
| (3,1) KN(g,g) *CAA(xi)=(6)F | True | True | agree |
| (3,1) KN(g,g) Q(E_OP) | -576 | -576 | agree |
| (3,1) blade 0001 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 0001 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 0001 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 0001 h^dagger A h=A | True | True | agree |
| (3,1) blade 0010 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 0010 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 0010 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 0010 h^dagger A h=A | True | True | agree |
| (3,1) blade 0011 centralizer vs CCC residual | 2 | 2 | agree |
| (3,1) blade 0011 centralizer vs CAA residual | 2 | 2 | agree |
| (3,1) blade 0011 centralizer vs CAC residual | 2 | 2 | agree |
| (3,1) blade 0011 h^dagger A h=A | True | True | agree |
| (3,1) blade 0100 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 0100 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 0100 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 0100 h^dagger A h=A | True | True | agree |
| (3,1) blade 0101 centralizer vs CCC residual | 2 | 2 | agree |
| (3,1) blade 0101 centralizer vs CAA residual | 2 | 2 | agree |
| (3,1) blade 0101 centralizer vs CAC residual | 2 | 2 | agree |
| (3,1) blade 0101 h^dagger A h=A | True | True | agree |
| (3,1) blade 0110 centralizer vs CCC residual | 2 | 2 | agree |
| (3,1) blade 0110 centralizer vs CAA residual | 2 | 2 | agree |
| (3,1) blade 0110 centralizer vs CAC residual | 2 | 2 | agree |
| (3,1) blade 0110 h^dagger A h=A | True | True | agree |
| (3,1) blade 0111 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 0111 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 0111 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 0111 h^dagger A h=A | True | True | agree |
| (3,1) blade 1000 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 1000 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 1000 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 1000 h^dagger A h=A | True | True | agree |
| (3,1) blade 1001 centralizer vs CCC residual | 2 | 2 | agree |
| (3,1) blade 1001 centralizer vs CAA residual | 2 | 2 | agree |
| (3,1) blade 1001 centralizer vs CAC residual | 2 | 2 | agree |
| (3,1) blade 1001 h^dagger A h=A | True | True | agree |
| (3,1) blade 1010 centralizer vs CCC residual | 2 | 2 | agree |
| (3,1) blade 1010 centralizer vs CAA residual | 2 | 2 | agree |
| (3,1) blade 1010 centralizer vs CAC residual | 2 | 2 | agree |
| (3,1) blade 1010 h^dagger A h=A | True | True | agree |
| (3,1) blade 1011 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 1011 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 1011 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 1011 h^dagger A h=A | True | True | agree |
| (3,1) blade 1100 centralizer vs CCC residual | 2 | 2 | agree |
| (3,1) blade 1100 centralizer vs CAA residual | 2 | 2 | agree |
| (3,1) blade 1100 centralizer vs CAC residual | 2 | 2 | agree |
| (3,1) blade 1100 h^dagger A h=A | True | True | agree |
| (3,1) blade 1101 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 1101 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 1101 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 1101 h^dagger A h=A | True | True | agree |
| (3,1) blade 1110 centralizer vs CCC residual | 3 | 3 | agree |
| (3,1) blade 1110 centralizer vs CAA residual | 3 | 3 | agree |
| (3,1) blade 1110 centralizer vs CAC residual | 3 | 3 | agree |
| (3,1) blade 1110 h^dagger A h=A | True | True | agree |
| (3,1) blade 1111 centralizer vs CCC residual | 6 | 6 | agree |
| (3,1) blade 1111 centralizer vs CAA residual | 6 | 6 | agree |
| (3,1) blade 1111 centralizer vs CAC residual | 6 | 6 | agree |
| (3,1) blade 1111 h^dagger A h=A | True | True | agree |
| (3,1) CCC blade 0001 leak rank | 10 | 10 | agree |
| (3,1) CCC blade 0001 transported Weyl defect | 0 | 0 | agree |
| (3,1) CCC blade 0011 leak rank | 6 | 6 | agree |
| (3,1) CCC blade 0011 transported Weyl defect | 0 | 0 | agree |
| (3,1) CCC blade 0111 leak rank | 5 | 5 | agree |
| (3,1) CCC blade 0111 transported Weyl defect | 0 | 0 | agree |
| (3,1) CCC blade 1111 leak rank | 0 | 0 | agree |
| (3,1) CCC blade 1111 transported Weyl defect | 0 | 0 | agree |
| P4 witness belongs to xi(Weyl) | 10 | 10 | agree |
| P4 witness transported grade-3 is nonzero | True | True | agree |
| P4 witness dressed CCC output zero | True | True | agree |
| (1,3) curvature dimension | 20 | 20 | agree |
| (1,3) Weyl dimension | 10 | 10 | agree |
| (1,3) Weyl projection has zero Ricci | True | True | agree |
| (1,3) invariant design rank | 4 | 4 | agree |
| (1,3) CCC nonzero response exists | True | True | agree |
| (1,3) Q(CCC) re fit (210 pairs) | (0, 0, -1, -1/4) | (0, 0, -1, -1/4) | agree |
| (1,3) Q(CCC) im fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (1,3) CCC undressed Weyl rank | 0 | 0 | agree |
| (1,3) CAA nonzero response exists | True | True | agree |
| (1,3) Q(CAA) re fit (210 pairs) | (0, 0, -1, -1/4) | (0, 0, -1, -1/4) | agree |
| (1,3) Q(CAA) im fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (1,3) CAA undressed Weyl rank | 0 | 0 | agree |
| (1,3) CAC nonzero response exists | True | True | agree |
| (1,3) Q(CAC) re fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (1,3) Q(CAC) im fit (210 pairs) | (0, 0, 0, 0) | (0, 0, 0, 0) | agree |
| (1,3) CAC undressed Weyl rank | 0 | 0 | agree |
| (1,3) E_OP linear response 2E_F(Ric)-S E_F(g) (20 inputs) | True | True | agree |
| (1,3) Q(E_OP) re/im fits | ((0, 0, -4, -1), (0, 0, 0, 0)) | ((0, 0, -4, -1), (0, 0, 0, 0)) | agree |
| (1,3) hand W Ricci | (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) | (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) | agree |
| (1,3) dual matches hand complement construction | True | True | agree |
| (1,3) W.W nonvacuity | 16 | 16 | agree |
| (1,3) W.*(hand *W) | -16 | -16 | agree |
| (1,3) mixed W.*W normalization | -32 | -32 | agree |
| (1,3) KN(g,g) Ricci=6g | True | True | agree |
| (1,3) KN(g,g) scalar | 24 | 24 | agree |
| (1,3) KN(g,g) Ric.Ric | 144 | 144 | agree |
| (1,3) KN(g,g) *CCC(xi)=(-6)F | True | True | agree |
| (1,3) KN(g,g) *CAA(xi)=(6)F | True | True | agree |
| (1,3) KN(g,g) Q(E_OP) | -576 | -576 | agree |
| (1,3) blade 0001 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 0001 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 0001 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 0001 h^dagger A h=A | True | True | agree |
| (1,3) blade 0010 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 0010 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 0010 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 0010 h^dagger A h=A | True | True | agree |
| (1,3) blade 0011 centralizer vs CCC residual | 2 | 2 | agree |
| (1,3) blade 0011 centralizer vs CAA residual | 2 | 2 | agree |
| (1,3) blade 0011 centralizer vs CAC residual | 2 | 2 | agree |
| (1,3) blade 0011 h^dagger A h=A | True | True | agree |
| (1,3) blade 0100 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 0100 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 0100 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 0100 h^dagger A h=A | True | True | agree |
| (1,3) blade 0101 centralizer vs CCC residual | 2 | 2 | agree |
| (1,3) blade 0101 centralizer vs CAA residual | 2 | 2 | agree |
| (1,3) blade 0101 centralizer vs CAC residual | 2 | 2 | agree |
| (1,3) blade 0101 h^dagger A h=A | True | True | agree |
| (1,3) blade 0110 centralizer vs CCC residual | 2 | 2 | agree |
| (1,3) blade 0110 centralizer vs CAA residual | 2 | 2 | agree |
| (1,3) blade 0110 centralizer vs CAC residual | 2 | 2 | agree |
| (1,3) blade 0110 h^dagger A h=A | True | True | agree |
| (1,3) blade 0111 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 0111 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 0111 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 0111 h^dagger A h=A | True | True | agree |
| (1,3) blade 1000 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 1000 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 1000 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 1000 h^dagger A h=A | True | True | agree |
| (1,3) blade 1001 centralizer vs CCC residual | 2 | 2 | agree |
| (1,3) blade 1001 centralizer vs CAA residual | 2 | 2 | agree |
| (1,3) blade 1001 centralizer vs CAC residual | 2 | 2 | agree |
| (1,3) blade 1001 h^dagger A h=A | True | True | agree |
| (1,3) blade 1010 centralizer vs CCC residual | 2 | 2 | agree |
| (1,3) blade 1010 centralizer vs CAA residual | 2 | 2 | agree |
| (1,3) blade 1010 centralizer vs CAC residual | 2 | 2 | agree |
| (1,3) blade 1010 h^dagger A h=A | True | True | agree |
| (1,3) blade 1011 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 1011 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 1011 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 1011 h^dagger A h=A | True | True | agree |
| (1,3) blade 1100 centralizer vs CCC residual | 2 | 2 | agree |
| (1,3) blade 1100 centralizer vs CAA residual | 2 | 2 | agree |
| (1,3) blade 1100 centralizer vs CAC residual | 2 | 2 | agree |
| (1,3) blade 1100 h^dagger A h=A | True | True | agree |
| (1,3) blade 1101 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 1101 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 1101 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 1101 h^dagger A h=A | True | True | agree |
| (1,3) blade 1110 centralizer vs CCC residual | 3 | 3 | agree |
| (1,3) blade 1110 centralizer vs CAA residual | 3 | 3 | agree |
| (1,3) blade 1110 centralizer vs CAC residual | 3 | 3 | agree |
| (1,3) blade 1110 h^dagger A h=A | True | True | agree |
| (1,3) blade 1111 centralizer vs CCC residual | 6 | 6 | agree |
| (1,3) blade 1111 centralizer vs CAA residual | 6 | 6 | agree |
| (1,3) blade 1111 centralizer vs CAC residual | 6 | 6 | agree |
| (1,3) blade 1111 h^dagger A h=A | True | True | agree |
