# B07 option C: independent exact re-derivation

The independent reconstruction at code commit 2627696 exits 0 and agrees with all **1,444 compared records**, with **zero remaining disagreements**. Twelve producer metadata/control groups are explicitly marked not reconstructed below. These counts include structural fields and shared "not computed" declarations; they are not counts of independent mathematical theorems.

Scope: identity at a 4D point, signatures (3,1) and (1,3), the four named undressed operators, frozen metric, flat background, epsilon = 1, reading V, quadratic order, pinned normalized trace pairing. Nullities below are polarization-space dimensions.

Run: `uv run python -m experiments.B07.optionc.rederive_codex`. The script prints exact reconstructed data and every comparison to stdout, and writes no files. The script was committed alone before its first execution (850c4d0). Its correction was committed alone before rerunning (2627696). The producer source revision recorded in the comparison file is aac4e42c0681dee13c75222ee8a9d31bced6d6fe.

## Independence and sources

The re-derivation shares only `gammas` and `dirac_pairing` from `gu.clifford`. Other imports are Python standard library and SymPy. Only `gu/clifford.py` and the new reconstruction script were opened as Python source. No producer modules or tests were inspected. No other plan tasks were displayed or executed.

Authorized formula sources read:

- `docs/superpowers/specs/2026-10-17-b07-optionc-design.md`, rev 3.1.
- `experiments/B07/phase2/derivations.md`, especially H9 and H12-H14.
- `experiments/B07/phase2/README.md`, including E_OP at line 63.
- `experiments/B02/README.md`.
- `experiments/B02/transcription.md`.
- `experiments/B02/proofs.md`.
- `experiments/B07/escape/derivations.md`.
- `gu/clifford.py`.

Only Global Constraints and Task 3 were extracted from `docs/superpowers/plans/2026-10-17-b07-optionc.md`. The comparison file `experiments/B07/optionc/result.json` was inspected for its schema and recorded values; this was independent, **not blind**. Formulas were chosen from the authorized sources. The script itself finishes all mathematical computations before reading that JSON, which is never an input to its operators or linear algebra.

## Construction and coordinate transport

Gamma matrices are converted to exact SymPy matrices from their integer real/imaginary arrays. Every ordered blade is an increasing product of gamma matrices. The 256 blade products are recovered from normalized matrix traces and checked entrywise against the original matrix products. Chirality is the first phase of the volume product that is Hermitian and squares to the identity.

For each blade Gamma_c, its phase pi_c is chosen from {1,i} by the direct membership equation (pi_c Gamma_c)^dagger A + A(pi_c Gamma_c) = 0. In the two signatures these are the documented phased u(A) bases: phase 1 on grades 1 and 2, phase i on grades 0, 3 and 4. Exterior basis indices are increasing bitmasks, with the exterior index outer and the Clifford blade inner.

The raw-to-phased coefficient map is x_raw = Pi x_phased, Pi_(f,c) = pi_c. Thus raw bilinear matrices are Pi^(-T) B_phased Pi^(-1). C1's count is evaluated after this transport, over all four covector indices and raw indices i <= j, including diagonal entries. The counted matrix is G1 N + N^T G1, transported to raw coordinates; the unnormalized C1 adds the nonzero common trace factor 4, which cannot change the count. A blade-order permutation does not change this upper-triangle count of a symmetric array. Directed Clifford-grade support is read directly in the phased basis.

The exterior product and Hodge star are independently implemented from wedge permutation signs and eta products. Both C and i-anticommutator brackets act on the Clifford coefficients. CCC/CAA use (F,B); CAC uses (F+Fprime,Bprime). E_OP uses the unweighted first/second building blocks of the Phase 2 specification; see the resolved normalization finding below.

Let J be the matrix of star: Omega1 -> Omega3, H = J^T G3 J = (-1)^q G1, and N(k) = J^(-1) X(k wedge). Then U(k) = J(1+iN(k)), and the independently assembled Hessian parts are

- S0 = 2 N^T H N;
- S1 = 2i(HN-N^T H);
- S2 = 2H.

All matrices are exact. The normalized trace pairing is bilinear; Hermitian restrictions use conjugate transpose only at the specified real Fourier roots. The script checks the six Spin generators on the pairing, star, N and Hessian.

For Q2, the 36 curvature coordinates form a 6 by 6 pair matrix. The independent projectors are P15=(1-tau)/2, P1=epsilon epsilon^T/6 and P20=(1+tau)/2-P1, with epsilon_0123=+1. Ranks, idempotence, annihilation and the identity sum are checked. The soldering includes eta_c eta_d/2. E and Ea are built from symmetric and antisymmetric tensor embeddings. Algebraic response coefficients are fitted and checked on every P20 column.

The full rational characteristic polynomial of N on the timelike ray is factored over Q. For each nonzero irreducible factor, an exact algebraic root defines the field for U and M kernels. Ranks at one representative extend to its algebraic conjugates because the matrices are rational functions of that root. Successive nullities of powers of N-nu determine all U partial multiplicities. Covariance and the Gram identity give the doubled determinant multiplicity for M; where its kernel dimension equals that multiplicity, all M partial multiplicities equal 1. Other M partial multiplicities remain explicitly uncomputed.

Q4(i)-(ii) uses both signs of every real root with rational omega^2. Q4(i) is |omega| M'(omega) restricted to ker M. Q4(ii) is (U' V_U)^dagger G3 (U' V_U), checked against V_U^dagger M'' V_U/4. Q4(iii) is computed on all three pinned rays. Exact Hermitian congruence uses scalar pivots or neutral 2 by 2 pivots; no numerical eigenvalues, floats, or modular ranks supply a result.

## Agreement summary

The following values are identical at both signatures. S1 rank is the rank at each of the four basis covectors; the S0 ranks are ordered timelike, spacelike, null.

| Operator | S1 rank at each e_m | Raw C1 nonzero count | Q2 rank on 15 | dim(image intersect E), dim(image intersect Ea) | 1-part coefficients | Nilpotent multiplicity of N | S0 ranks |
|---|---:|---:|---:|---|---|---:|---|
| CCC | 38 | 192 | 6 | 0, 6 | 0, 0 | 34 | 31, 31, 20 |
| CAA | 38 | 144 | 6 | 0, 6 | 0, 0 | 40 | 34, 34, 19 |
| CAC | 24 | 192 | 6 | 0, 6 | 0, 0 | 64 | 12, 12, 6 |
| E_OP | 30 | 0 | 6 | 0, 6 | 0, 0 | 34 | 30, 30, 17 |

CCC inner rank on the 15-part is 6 at both signatures, and the inner term vanishes on the 20- and 1-parts. Every recorded covariance flag, nested kernel dimension, quotient dimension, real-root inertia, nonzero-factor kernel, multiplicity, inclusion and semisimplicity value agrees.

### Timelike characteristic polynomials

Each expression is the full monic characteristic polynomial; the exponent of nu is the generalized zero-eigenspace dimension.

| Signature | Operator | Independent factorization (equals recorded factorization) |
|---|---|---|
| (3,1) | CCC | nu^34 * (nu**2 + 16)^1 * (nu**2 + 12)^3 * (nu**2 + 4)^5 * (nu**2 + 8)^6 |
| (3,1) | CAA | nu^40 * (nu - 2)^3 * (nu + 2)^3 * (nu**2 - 8)^1 * (nu**2 + 8)^3 * (nu**2 + 4)^5 |
| (3,1) | CAC | nu^64 |
| (3,1) | E_OP | nu^34 * (nu**2 + 64)^1 * (nu**2 + 32)^6 * (nu**2 + 16)^8 |
| (1,3) | CCC | nu^34 * (nu - 4)^1 * (nu + 4)^1 * (nu - 2)^5 * (nu + 2)^5 * (nu**2 - 12)^3 * (nu**2 - 8)^6 |
| (1,3) | CAA | nu^40 * (nu - 2)^5 * (nu + 2)^5 * (nu**2 + 8)^1 * (nu**2 - 8)^3 * (nu**2 + 4)^3 |
| (1,3) | CAC | nu^64 |
| (1,3) | E_OP | nu^34 * (nu - 8)^1 * (nu + 8)^1 * (nu - 4)^8 * (nu + 4)^8 * (nu**2 - 32)^6 |

## FINDING: E_OP block normalization in the first independent implementation — resolved

The first version treated "second" as the already weighted contribution -star[Phi1,star[Phi2,star x]]/2. In the Phase 2 block specification, "second" denotes the unweighted nested block. This yielded the incorrect independently fitted response (2,0,1/2,0), against the source-pinned (2,0,-1,0), and violated the documented C1=0 property. Thus the authorized formula sources themselves reject the first implementation.

If first=f and the weighted contributions returned by parts are c_CC and c_AA, the specification is E_OP=-2f+2c_CC-2c_AA. Commit 2627696 applies that conversion and adds gates for the documented algebraic responses and E_OP C1=0. All E_OP differences, including initially unmatched polynomial factors, disappear. The comparison file and producer code were not changed.

## FINDING: Semisimple M partial multiplicities initially omitted — resolved

The initial script declared every M partial multiplicity uncomputed. The reference records six simple partial multiplicities for CAA at nu-2 and nu+2 in (3,1), and at nu^2+4 in (1,3). Independently, dim ker M equals its determinant-root multiplicity 6, so all six partial multiplicities must be 1. Commit 2627696 now derives these entries. This was an omission in the independent reconstruction, not a mathematical disagreement with the producer.

## FINDING: Empty inapplicable Q4 arrays — resolved presentation difference

The first script emitted Q4=[] beside Q4_status=not_applicable, whereas the reference omits the array. Commit 2627696 omits this redundant array. No kernel, root, sign or applicability decision changed.

### Complete initial discrepancy ledger

Each row records an initial disagreement or unmatched spectral record, its original value, and its resolution. All are retained even though the final run agrees.

| Finding | First independent value | Recorded value | Resolution |
|---|---|---|---|
| FINDING: result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.partial_multiplicities_M | "not computed" | [1,1,1,1,1,1] | Resolved: semisimple M multiplicities derived in 2627696. |
| FINDING: result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.partial_multiplicities_M | "not computed" | [1,1,1,1,1,1] | Resolved: semisimple M multiplicities derived in 2627696. |
| FINDING: result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[0].operators[3].Q1.S1_rank_at_e_m | [44,44,44,44] | [30,30,30,30] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q1.c1_nonzero | 96 | 0 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q1.grade_pairs_coupled | [[0,3],[1,2],[2,1],[3,0],[3,4],[4,3]] | [[0,3],[1,2],[2,1],[3,0]] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [12,10,19] | [17,16,14] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [1,1,39] | [1,1,45] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.dim_ker_A | 29 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.dim_ker_S0 | 41 | 47 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 13 | 18 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 12 | 13 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [14,13,0] | [17,17,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,27] | [0,0,34] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 11 | 18 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.rank_S0_kappa0.null | 23 | 17 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.rank_S0_kappa0.spacelike | 37 | 30 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.rank_S0_kappa0.timelike | 37 | 30 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 100 | {"factor":"nu**2 + 100","degree":2,"exponent":1,"massive_type":["1/100","1/100"],"tachyonic_type":[],"non_real":0,"rational_massive":["1/100","1/100"],"Q3":{"factor":"nu**2 + 100","field_degree":2,"dim_ker_U":1,"dim_ker_M":1,"multiplicity_det_U":1,"multiplicity_det_M":2,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"hermitian_radical","partial_multiplicities_U":[1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[{"w0":"sqrt(1/100)","w0_squared":"1/100","dim_ker_U":1,"dim_ker_M":1,"multiplicity_det_U":1,"multiplicity_det_M":2,"kernel_gap_hermitian_radical":0,"semisimple_U":true,"semisimple_M":false,"control_ker_U_in_ker_M":true,"control_derivative_form_zero_on_ker_U":true,"control_QU_quarter_second_derivative":true,"derivative_form_rank":0,"derivative_form_inertia":[0,0,1],"second_order_form_rank":1,"second_order_form_inertia":[0,1,0]},{"w0":"-sqrt(1/100)","w0_squared":"1/100","dim_ker_U":1,"dim_ker_M":1,"multiplicity_det_U":1,"multiplicity_det_M":2,"kernel_gap_hermitian_radical":0,"semisimple_U":true,"semisimple_M":false,"control_ker_U_in_ker_M":true,"control_derivative_form_zero_on_ker_U":true,"control_QU_quarter_second_derivative":true,"derivative_form_rank":0,"derivative_form_inertia":[0,0,1],"second_order_form_rank":1,"second_order_form_inertia":[0,1,0]}],"Q4_status":"computed"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.dim_ker_M | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.dim_ker_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.multiplicity_det_M | 10 | 16 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.multiplicity_det_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1,1,1,1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).derivative_form_inertia | [0,0,5] | [0,0,8] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).dim_ker_M | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).dim_ker_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).multiplicity_det_M | 10 | 16 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).multiplicity_det_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).second_order_form_inertia | [0,5,0] | [0,8,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).second_order_form_rank | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).derivative_form_inertia | [0,0,5] | [0,0,8] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).dim_ker_M | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).dim_ker_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).multiplicity_det_M | 10 | 16 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).multiplicity_det_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).second_order_form_inertia | [0,5,0] | [0,8,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).second_order_form_rank | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.exponent | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32 | "not reconstructed" | {"Q3":{"control_ker_U_in_ker_M":true,"dim_ker_M":6,"dim_ker_U":6,"factor":"nu**2 + 32","field_degree":2,"kernel_gap":0,"kernel_gap_reading":"hermitian_radical","multiplicity_det_M":12,"multiplicity_det_U":6,"partial_multiplicities_M":"not computed","partial_multiplicities_U":[1,1,1,1,1,1],"semisimple_M":false,"semisimple_U":true},"Q4":[{"control_QU_quarter_second_derivative":true,"control_derivative_form_zero_on_ker_U":true,"control_ker_U_in_ker_M":true,"derivative_form_inertia":[0,0,6],"derivative_form_rank":0,"dim_ker_M":6,"dim_ker_U":6,"kernel_gap_hermitian_radical":0,"multiplicity_det_M":12,"multiplicity_det_U":6,"second_order_form_inertia":[6,0,0],"second_order_form_rank":6,"semisimple_M":false,"semisimple_U":true,"w0":"sqrt(1/32)","w0_squared":"1/32"},{"control_QU_quarter_second_derivative":true,"control_derivative_form_zero_on_ker_U":true,"control_ker_U_in_ker_M":true,"derivative_form_inertia":[0,0,6],"derivative_form_rank":0,"dim_ker_M":6,"dim_ker_U":6,"kernel_gap_hermitian_radical":0,"multiplicity_det_M":12,"multiplicity_det_U":6,"second_order_form_inertia":[6,0,0],"second_order_form_rank":6,"semisimple_M":false,"semisimple_U":true,"w0":"-sqrt(1/32)","w0_squared":"1/32"}],"Q4_status":"computed","degree":2,"exponent":6,"factor":"nu**2 + 32","massive_type":["1/32","1/32"],"non_real":0,"rational_massive":["1/32","1/32"],"tachyonic_type":[]} | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 36 | {"factor":"nu**2 + 36","degree":2,"exponent":3,"massive_type":["1/36","1/36"],"tachyonic_type":[],"non_real":0,"rational_massive":["1/36","1/36"],"Q3":{"factor":"nu**2 + 36","field_degree":2,"dim_ker_U":3,"dim_ker_M":3,"multiplicity_det_U":3,"multiplicity_det_M":6,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"hermitian_radical","partial_multiplicities_U":[1,1,1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[{"w0":"sqrt(1/36)","w0_squared":"1/36","dim_ker_U":3,"dim_ker_M":3,"multiplicity_det_U":3,"multiplicity_det_M":6,"kernel_gap_hermitian_radical":0,"semisimple_U":true,"semisimple_M":false,"control_ker_U_in_ker_M":true,"control_derivative_form_zero_on_ker_U":true,"control_QU_quarter_second_derivative":true,"derivative_form_rank":0,"derivative_form_inertia":[0,0,3],"second_order_form_rank":3,"second_order_form_inertia":[0,3,0]},{"w0":"-sqrt(1/36)","w0_squared":"1/36","dim_ker_U":3,"dim_ker_M":3,"multiplicity_det_U":3,"multiplicity_det_M":6,"kernel_gap_hermitian_radical":0,"semisimple_U":true,"semisimple_M":false,"control_ker_U_in_ker_M":true,"control_derivative_form_zero_on_ker_U":true,"control_QU_quarter_second_derivative":true,"derivative_form_rank":0,"derivative_form_inertia":[0,0,3],"second_order_form_rank":3,"second_order_form_inertia":[0,3,0]}],"Q4_status":"computed"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.dim_ker_M | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.dim_ker_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.multiplicity_det_M | 6 | 2 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.multiplicity_det_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.partial_multiplicities_U | [1,1,1] | [1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).derivative_form_inertia | [0,0,3] | [0,0,1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).dim_ker_M | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).dim_ker_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).multiplicity_det_M | 6 | 2 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).multiplicity_det_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).second_order_form_inertia | [0,3,0] | [0,1,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).second_order_form_rank | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).derivative_form_inertia | [0,0,3] | [0,0,1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).dim_ker_M | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).dim_ker_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).multiplicity_det_M | 6 | 2 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).multiplicity_det_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).second_order_form_inertia | [0,3,0] | [0,1,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).second_order_form_rank | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.exponent | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 8 | {"factor":"nu**2 + 8","degree":2,"exponent":6,"massive_type":["1/8","1/8"],"tachyonic_type":[],"non_real":0,"rational_massive":["1/8","1/8"],"Q3":{"factor":"nu**2 + 8","field_degree":2,"dim_ker_U":6,"dim_ker_M":6,"multiplicity_det_U":6,"multiplicity_det_M":12,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"hermitian_radical","partial_multiplicities_U":[1,1,1,1,1,1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[{"w0":"sqrt(1/8)","w0_squared":"1/8","dim_ker_U":6,"dim_ker_M":6,"multiplicity_det_U":6,"multiplicity_det_M":12,"kernel_gap_hermitian_radical":0,"semisimple_U":true,"semisimple_M":false,"control_ker_U_in_ker_M":true,"control_derivative_form_zero_on_ker_U":true,"control_QU_quarter_second_derivative":true,"derivative_form_rank":0,"derivative_form_inertia":[0,0,6],"second_order_form_rank":6,"second_order_form_inertia":[6,0,0]},{"w0":"-sqrt(1/8)","w0_squared":"1/8","dim_ker_U":6,"dim_ker_M":6,"multiplicity_det_U":6,"multiplicity_det_M":12,"kernel_gap_hermitian_radical":0,"semisimple_U":true,"semisimple_M":false,"control_ker_U_in_ker_M":true,"control_derivative_form_zero_on_ker_U":true,"control_QU_quarter_second_derivative":true,"derivative_form_rank":0,"derivative_form_inertia":[0,0,6],"second_order_form_rank":6,"second_order_form_inertia":[6,0,0]}],"Q4_status":"computed"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 28 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [8,19,0] | [14,20,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,27] | [0,0,34] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_A | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 11 | 18 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].Q3_Q4.timelike.rank_S0_kappa0 | 37 | 30 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[0].operators[3].response | ["2","0","1/2","0"] | ["2","0","-1","0"] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.partial_multiplicities_M | "not computed" | [1,1,1,1,1,1] | Resolved: semisimple M multiplicities derived in 2627696. |
| FINDING: result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[3].Q1.S1_rank_at_e_m | [44,44,44,44] | [30,30,30,30] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q1.c1_nonzero | 96 | 0 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q1.grade_pairs_coupled | [[0,3],[1,2],[2,1],[3,0],[3,4],[4,3]] | [[0,3],[1,2],[2,1],[3,0]] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [10,12,19] | [15,18,14] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [1,1,39] | [1,1,45] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.dim_ker_A | 29 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.dim_ker_S0 | 41 | 47 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 13 | 18 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 12 | 13 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [12,15,0] | [14,20,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,27] | [0,0,34] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 11 | 18 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.rank_S0_kappa0.null | 23 | 17 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.rank_S0_kappa0.spacelike | 37 | 30 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.rank_S0_kappa0.timelike | 37 | 30 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 10 | {"factor":"nu + 10","degree":1,"exponent":1,"massive_type":[],"tachyonic_type":["-1/100"],"non_real":0,"rational_massive":[],"Q3":{"factor":"nu + 10","field_degree":1,"dim_ker_U":1,"dim_ker_M":1,"multiplicity_det_U":1,"multiplicity_det_M":2,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"cross_annihilator","partial_multiplicities_U":[1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[],"Q4_status":"not_applicable"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.dim_ker_M | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.dim_ker_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.multiplicity_det_M | 10 | 16 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.multiplicity_det_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1,1,1,1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.exponent | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 6 | {"factor":"nu + 6","degree":1,"exponent":3,"massive_type":[],"tachyonic_type":["-1/36"],"non_real":0,"rational_massive":[],"Q3":{"factor":"nu + 6","field_degree":1,"dim_ker_U":3,"dim_ker_M":3,"multiplicity_det_U":3,"multiplicity_det_M":6,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"cross_annihilator","partial_multiplicities_U":[1,1,1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[],"Q4_status":"not_applicable"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.dim_ker_M | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.dim_ker_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.multiplicity_det_M | 6 | 2 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.multiplicity_det_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.partial_multiplicities_U | [1,1,1] | [1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.exponent | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 10 | {"factor":"nu - 10","degree":1,"exponent":1,"massive_type":[],"tachyonic_type":["-1/100"],"non_real":0,"rational_massive":[],"Q3":{"factor":"nu - 10","field_degree":1,"dim_ker_U":1,"dim_ker_M":1,"multiplicity_det_U":1,"multiplicity_det_M":2,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"cross_annihilator","partial_multiplicities_U":[1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[],"Q4_status":"not_applicable"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.dim_ker_M | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.dim_ker_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.multiplicity_det_M | 10 | 16 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.multiplicity_det_U | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1,1,1,1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.exponent | 5 | 8 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 6 | {"factor":"nu - 6","degree":1,"exponent":3,"massive_type":[],"tachyonic_type":["-1/36"],"non_real":0,"rational_massive":[],"Q3":{"factor":"nu - 6","field_degree":1,"dim_ker_U":3,"dim_ker_M":3,"multiplicity_det_U":3,"multiplicity_det_M":6,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"cross_annihilator","partial_multiplicities_U":[1,1,1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[],"Q4_status":"not_applicable"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.dim_ker_M | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.dim_ker_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.multiplicity_det_M | 6 | 2 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.multiplicity_det_U | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.partial_multiplicities_U | [1,1,1] | [1] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q4 | [] | "not recorded" | Resolved: omitted empty inapplicable Q4 array in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.exponent | 3 | 1 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32 | "not reconstructed" | {"Q3":{"control_ker_U_in_ker_M":true,"dim_ker_M":6,"dim_ker_U":6,"factor":"nu**2 - 32","field_degree":2,"kernel_gap":0,"kernel_gap_reading":"cross_annihilator","multiplicity_det_M":12,"multiplicity_det_U":6,"partial_multiplicities_M":"not computed","partial_multiplicities_U":[1,1,1,1,1,1],"semisimple_M":false,"semisimple_U":true},"Q4_status":"not_applicable","degree":2,"exponent":6,"factor":"nu**2 - 32","massive_type":[],"non_real":0,"rational_massive":[],"tachyonic_type":["-1/32","-1/32"]} | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 8 | {"factor":"nu**2 - 8","degree":2,"exponent":6,"massive_type":[],"tachyonic_type":["-1/8","-1/8"],"non_real":0,"rational_massive":[],"Q3":{"factor":"nu**2 - 8","field_degree":2,"dim_ker_U":6,"dim_ker_M":6,"multiplicity_det_U":6,"multiplicity_det_M":12,"control_ker_U_in_ker_M":true,"kernel_gap":0,"kernel_gap_reading":"cross_annihilator","partial_multiplicities_U":[1,1,1,1,1,1],"partial_multiplicities_M":"not computed","semisimple_U":true,"semisimple_M":false},"Q4":[],"Q4_status":"not_applicable"} | "not recorded" | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 28 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [14,13,0] | [17,17,0] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,27] | [0,0,34] | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_A | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 27 | 34 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 11 | 18 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].Q3_Q4.timelike.rank_S0_kappa0 | 37 | 30 | Resolved: E_OP unweighted block normalization in 2627696. |
| FINDING: result.signatures[1].operators[3].response | ["2","0","1/2","0"] | ["2","0","-1","0"] | Resolved: E_OP unweighted block normalization in 2627696. |

## Not reconstructed

- The two auxiliary signatures (2,2) and (4,0), and their convention-control records.
- The producer backend-control suite. The independent elimination has its own exact off-diagonal and non-square-field hand checks, but does not import or compare against gu.inertia.
- The producer signature-level control aggregate: its named direct-action fixtures, its specific hand xi fixture, and its projector-equivariance/curvature-span certificates. Projector ranks, idempotence, mutual annihilation and identity sum, the soldering formula, the mass/star pairing identity, and full algebraic responses are independently checked, but the full aggregate is not claimed reproduced.
- Producer runtime, provenance, status and scope metadata. These are recorded comparison data, not outputs of this independent mathematical derivation.
- M partial multiplicities at non-semisimple roots, for which the reference itself says "not computed". Their semisimplicity, determinant multiplicities and kernel dimensions are reconstructed.
- No separate replay of the producer's homogeneous-reconstruction, direct-action, fixed-X-prime, serializer or dirty-tree tests is claimed. No expanded determinant of M was computed independently; determinant multiplicity uses the independently reconstructed square-symbol Gram identity and covariance.

All required Q1-Q4 quantities in Task 3 Step 2 are reconstructed. An uncomputed control group is not an agreement assertion. The table below lists the reference values for every such group alongside that limitation.

## Full field comparison

Paths use signature indices 0=(3,1), 1=(1,3), and operator indices 0=CCC, 1=CAA, 2=CAC, 3=E_OP. Factors and Q4 roots are matched by their exact labels, independent of record order. Arrays of scalar values are compared as complete arrays. An omitted producer control group is displayed in full as JSON.

| Quantity | Independent value | result.json value | Agree/disagree |
|---|---|---|---|
| result.auxiliary | "not reconstructed" | [{"backend_controls":true,"mass_sign":1,"operators":{"CAA":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true},"CAC":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true},"CCC":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true},"E_OP":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true}},"signature":[2,2],"star_adjoint_sign_1":-1},{"backend_controls":true,"mass_sign":1,"operators":{"CAA":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true},"CAC":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true},"CCC":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true},"E_OP":{"S2_identity":true,"prime_identity":true,"real_closure":false,"reconstruction":true,"transpose_identity":true}},"signature":[4,0],"star_adjoint_sign_1":-1}] | not reconstructed |
| result.backend_controls | "not reconstructed" | {"classify_massive":true,"classify_non_real":true,"classify_tachyonic":true,"conjugation_convention":true,"gram_toy_[1, -1]":true,"gram_toy_[1, -1]_over_field":true,"gram_toy_[1, 1]":true,"gram_toy_[1, 1]_over_field":true,"hermitian_d1_vs_gu_inertia":true,"hermitian_d2_hand":true,"jordan_chain":true,"jordan_chain_realified":true,"nilpotent_algebraic_multiplicity":true,"real_eigenvalue_root":true,"scalar_massive":true,"scalar_massless_null_zero_polynomial":true,"scalar_massless_timelike":true,"second_order_form_d1_4":true,"second_order_form_d2":true,"singular_leading_degree_deficit":true} | not reconstructed |
| result.design | "not reconstructed" | "docs/superpowers/specs/2026-10-17-b07-optionc-design.md rev 3.1" | not reconstructed |
| result.scope | "not reconstructed" | "identity: 4D point, (3,1) and (1,3), flat background, eps = 1, metric frozen, delta T = delta A, quadratic order; operators CCC, CAA, CAC (variation.BRANCHES) and E_OP (phase2 run.e_op); pinned star, fixed-X prime convention as a control; (2,2)/(4,0) convention controls only" | not reconstructed |
| result.seconds | "not reconstructed" | 1340.1 | not reconstructed |
| result.signatures[0].controls | "not reconstructed" | {"direct_hessian":["GQ(2, 0)","GQ(0, 4)","GQ(0, -4)","GQ(0, -4)","GQ(0, 0)"],"hand_xi_entry":true,"mass_sign":-1,"projectors":{"algebraic_part_is_curvature_span":true,"equivariant":true,"idempotent":true,"mutually_annihilating":true,"ranks":{"P1":1,"P15":15,"P20":20},"sum_identity":true},"star_adjoint_sign_1":-1} | not reconstructed |
| result.signatures[0].operators[0].Q1.S1_identically_zero | false | false | agree |
| result.signatures[0].operators[0].Q1.S1_rank_at_e_m | [38,38,38,38] | [38,38,38,38] | agree |
| result.signatures[0].operators[0].Q1.c1_nonzero | 192 | 192 | agree |
| result.signatures[0].operators[0].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[0].Q1.grade_pairs_coupled | [[1,2],[2,1],[3,4],[4,3]] | [[1,2],[2,1],[3,4],[4,3]] | agree |
| result.signatures[0].operators[0].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[0].Q2.ccc_inner_rank_15 | 6 | 6 | agree |
| result.signatures[0].operators[0].Q2.controls.ccc_inner_zero_on_20_and_1 | true | true | agree |
| result.signatures[0].operators[0].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[0].operators[0].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[0].operators[0].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[0].operators[0].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[0].operators[0].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[0].operators[0].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[0].operators[0].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[0].operators[0].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [15,13,16] | [15,13,16] | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [3,3,38] | [3,3,38] | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.dim_ker_A | 33 | 33 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.dim_ker_S0 | 44 | 44 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 17 | 17 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 11 | 11 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [17,16,0] | [17,16,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,33] | [0,0,33] | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 33 | 33 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 33 | 33 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 17 | 17 | agree |
| result.signatures[0].operators[0].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.rank_S0_kappa0.null | 20 | 20 | agree |
| result.signatures[0].operators[0].Q3_Q4.rank_S0_kappa0.spacelike | 31 | 31 | agree |
| result.signatures[0].operators[0].Q3_Q4.rank_S0_kappa0.timelike | 31 | 31 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.dim_ker_M | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.factor | "nu**2 + 12" | "nu**2 + 12" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.partial_multiplicities_U | [1,1,1] | [1,1,1] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).derivative_form_inertia | [0,0,3] | [0,0,3] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).dim_ker_M | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).second_order_form_inertia | [0,3,0] | [0,3,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).second_order_form_rank | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).w0 | "-sqrt(1/12)" | "-sqrt(1/12)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.-sqrt(1/12).w0_squared | "1/12" | "1/12" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).derivative_form_inertia | [0,0,3] | [0,0,3] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).dim_ker_M | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).second_order_form_inertia | [0,3,0] | [0,3,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).second_order_form_rank | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).w0 | "sqrt(1/12)" | "sqrt(1/12)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4.sqrt(1/12).w0_squared | "1/12" | "1/12" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.exponent | 3 | 3 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.factor | "nu**2 + 12" | "nu**2 + 12" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.massive_type | ["1/12","1/12"] | ["1/12","1/12"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.non_real | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.rational_massive | ["1/12","1/12"] | ["1/12","1/12"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 12.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.factor | "nu**2 + 16" | "nu**2 + 16" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).derivative_form_inertia | [0,0,1] | [0,0,1] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).dim_ker_M | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).dim_ker_U | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).multiplicity_det_M | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).multiplicity_det_U | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).second_order_form_inertia | [0,1,0] | [0,1,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).second_order_form_rank | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).w0 | "-sqrt(1/16)" | "-sqrt(1/16)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).w0_squared | "1/16" | "1/16" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).derivative_form_inertia | [0,0,1] | [0,0,1] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).dim_ker_M | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).dim_ker_U | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).multiplicity_det_M | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).multiplicity_det_U | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).second_order_form_inertia | [0,1,0] | [0,1,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).second_order_form_rank | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).w0 | "sqrt(1/16)" | "sqrt(1/16)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).w0_squared | "1/16" | "1/16" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.exponent | 1 | 1 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.factor | "nu**2 + 16" | "nu**2 + 16" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.massive_type | ["1/16","1/16"] | ["1/16","1/16"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.non_real | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.rational_massive | ["1/16","1/16"] | ["1/16","1/16"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.dim_ker_M | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.dim_ker_U | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.factor | "nu**2 + 4" | "nu**2 + 4" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.multiplicity_det_M | 10 | 10 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.multiplicity_det_U | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).derivative_form_inertia | [0,0,5] | [0,0,5] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).dim_ker_M | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).dim_ker_U | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).multiplicity_det_M | 10 | 10 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).multiplicity_det_U | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).second_order_form_inertia | [0,5,0] | [0,5,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).second_order_form_rank | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).w0 | "-sqrt(1/4)" | "-sqrt(1/4)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).w0_squared | "1/4" | "1/4" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).derivative_form_inertia | [0,0,5] | [0,0,5] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).dim_ker_M | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).dim_ker_U | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).multiplicity_det_M | 10 | 10 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).multiplicity_det_U | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).second_order_form_inertia | [0,5,0] | [0,5,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).second_order_form_rank | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).w0 | "sqrt(1/4)" | "sqrt(1/4)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).w0_squared | "1/4" | "1/4" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.exponent | 5 | 5 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.factor | "nu**2 + 4" | "nu**2 + 4" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.massive_type | ["1/4","1/4"] | ["1/4","1/4"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.non_real | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.rational_massive | ["1/4","1/4"] | ["1/4","1/4"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.dim_ker_U | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.factor | "nu**2 + 8" | "nu**2 + 8" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.multiplicity_det_M | 12 | 12 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.multiplicity_det_U | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.partial_multiplicities_U | [1,1,1,1,1,1] | [1,1,1,1,1,1] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).derivative_form_inertia | [0,0,6] | [0,0,6] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).dim_ker_U | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).multiplicity_det_M | 12 | 12 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).multiplicity_det_U | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).second_order_form_inertia | [3,3,0] | [3,3,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).second_order_form_rank | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).w0 | "-sqrt(1/8)" | "-sqrt(1/8)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).w0_squared | "1/8" | "1/8" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).derivative_form_inertia | [0,0,6] | [0,0,6] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).dim_ker_U | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).multiplicity_det_M | 12 | 12 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).multiplicity_det_U | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).second_order_form_inertia | [3,3,0] | [3,3,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).second_order_form_rank | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).semisimple_M | false | false | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).semisimple_U | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).w0 | "sqrt(1/8)" | "sqrt(1/8)" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).w0_squared | "1/8" | "1/8" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.degree | 2 | 2 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.exponent | 6 | 6 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.factor | "nu**2 + 8" | "nu**2 + 8" | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.massive_type | ["1/8","1/8"] | ["1/8","1/8"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.non_real | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.rational_massive | ["1/8","1/8"] | ["1/8","1/8"] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 34 | 34 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [8,25,0] | [8,25,0] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,33] | [0,0,33] | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.dim_ker_A | 33 | 33 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 33 | 33 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 17 | 17 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[0].operators[0].Q3_Q4.timelike.rank_S0_kappa0 | 31 | 31 | agree |
| result.signatures[0].operators[0].operator | "CCC" | "CCC" | agree |
| result.signatures[0].operators[0].response | ["-1","0","0","0"] | ["-1","0","0","0"] | agree |
| result.signatures[0].operators[1].Q1.S1_identically_zero | false | false | agree |
| result.signatures[0].operators[1].Q1.S1_rank_at_e_m | [38,38,38,38] | [38,38,38,38] | agree |
| result.signatures[0].operators[1].Q1.c1_nonzero | 144 | 144 | agree |
| result.signatures[0].operators[1].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[1].Q1.grade_pairs_coupled | [[0,3],[1,2],[2,1],[3,0],[3,4],[4,3]] | [[0,3],[1,2],[2,1],[3,0],[3,4],[4,3]] | agree |
| result.signatures[0].operators[1].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[1].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[0].operators[1].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[0].operators[1].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[0].operators[1].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[0].operators[1].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[0].operators[1].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[0].operators[1].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[0].operators[1].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[0].operators[1].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [16,13,16] | [16,13,16] | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [3,3,39] | [3,3,39] | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.dim_ker_A | 30 | 30 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.dim_ker_S0 | 45 | 45 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 14 | 14 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 15 | 15 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [16,14,0] | [16,14,0] | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,30] | [0,0,30] | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 30 | 30 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 30 | 30 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 14 | 14 | agree |
| result.signatures[0].operators[1].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.rank_S0_kappa0.null | 19 | 19 | agree |
| result.signatures[0].operators[1].Q3_Q4.rank_S0_kappa0.spacelike | 34 | 34 | agree |
| result.signatures[0].operators[1].Q3_Q4.rank_S0_kappa0.timelike | 34 | 34 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.factor | "nu + 2" | "nu + 2" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.field_degree | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.kernel_gap | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.partial_multiplicities_M | [1,1,1,1,1,1] | [1,1,1,1,1,1] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.partial_multiplicities_U | [1,1,1] | [1,1,1] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.semisimple_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.degree | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.exponent | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.factor | "nu + 2" | "nu + 2" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.massive_type | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.non_real | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.rational_massive | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.tachyonic_type | ["-1/4"] | ["-1/4"] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.factor | "nu - 2" | "nu - 2" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.field_degree | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.kernel_gap | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.partial_multiplicities_M | [1,1,1,1,1,1] | [1,1,1,1,1,1] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.partial_multiplicities_U | [1,1,1] | [1,1,1] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.semisimple_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.degree | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.exponent | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.factor | "nu - 2" | "nu - 2" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.massive_type | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.non_real | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.rational_massive | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.tachyonic_type | ["-1/4"] | ["-1/4"] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.dim_ker_M | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.dim_ker_U | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.factor | "nu**2 + 4" | "nu**2 + 4" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.multiplicity_det_M | 10 | 10 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.multiplicity_det_U | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).derivative_form_inertia | [0,0,5] | [0,0,5] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).dim_ker_M | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).dim_ker_U | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).multiplicity_det_M | 10 | 10 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).multiplicity_det_U | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).second_order_form_inertia | [0,5,0] | [0,5,0] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).second_order_form_rank | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).semisimple_M | false | false | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).w0 | "-sqrt(1/4)" | "-sqrt(1/4)" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).w0_squared | "1/4" | "1/4" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).derivative_form_inertia | [0,0,5] | [0,0,5] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).dim_ker_M | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).dim_ker_U | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).multiplicity_det_M | 10 | 10 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).multiplicity_det_U | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).second_order_form_inertia | [0,5,0] | [0,5,0] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).second_order_form_rank | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).semisimple_M | false | false | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).w0 | "sqrt(1/4)" | "sqrt(1/4)" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).w0_squared | "1/4" | "1/4" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.degree | 2 | 2 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.exponent | 5 | 5 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.factor | "nu**2 + 4" | "nu**2 + 4" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.massive_type | ["1/4","1/4"] | ["1/4","1/4"] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.non_real | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.rational_massive | ["1/4","1/4"] | ["1/4","1/4"] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.dim_ker_M | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.factor | "nu**2 + 8" | "nu**2 + 8" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.partial_multiplicities_U | [1,1,1] | [1,1,1] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).derivative_form_inertia | [0,0,3] | [0,0,3] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).dim_ker_M | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).second_order_form_inertia | [3,0,0] | [3,0,0] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).second_order_form_rank | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).semisimple_M | false | false | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).w0 | "-sqrt(1/8)" | "-sqrt(1/8)" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).w0_squared | "1/8" | "1/8" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).derivative_form_inertia | [0,0,3] | [0,0,3] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).dim_ker_M | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).dim_ker_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).multiplicity_det_M | 6 | 6 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).multiplicity_det_U | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).second_order_form_inertia | [3,0,0] | [3,0,0] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).second_order_form_rank | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).semisimple_M | false | false | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).w0 | "sqrt(1/8)" | "sqrt(1/8)" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).w0_squared | "1/8" | "1/8" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.degree | 2 | 2 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.exponent | 3 | 3 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.factor | "nu**2 + 8" | "nu**2 + 8" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.massive_type | ["1/8","1/8"] | ["1/8","1/8"] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.non_real | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.rational_massive | ["1/8","1/8"] | ["1/8","1/8"] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.factor | "nu**2 - 8" | "nu**2 - 8" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.degree | 2 | 2 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.exponent | 1 | 1 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.factor | "nu**2 - 8" | "nu**2 - 8" | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.massive_type | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.non_real | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.rational_massive | [] | [] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.tachyonic_type | ["-1/8","-1/8"] | ["-1/8","-1/8"] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 40 | 40 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [11,19,0] | [11,19,0] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,30] | [0,0,30] | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.dim_ker_A | 30 | 30 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 30 | 30 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 14 | 14 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[0].operators[1].Q3_Q4.timelike.rank_S0_kappa0 | 34 | 34 | agree |
| result.signatures[0].operators[1].operator | "CAA" | "CAA" | agree |
| result.signatures[0].operators[1].response | ["-1","0","1/2","0"] | ["-1","0","1/2","0"] | agree |
| result.signatures[0].operators[2].Q1.S1_identically_zero | false | false | agree |
| result.signatures[0].operators[2].Q1.S1_rank_at_e_m | [24,24,24,24] | [24,24,24,24] | agree |
| result.signatures[0].operators[2].Q1.c1_nonzero | 192 | 192 | agree |
| result.signatures[0].operators[2].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[2].Q1.grade_pairs_coupled | [[0,1],[0,3],[1,0],[1,2],[2,1],[2,3],[3,0],[3,2]] | [[0,1],[0,3],[1,0],[1,2],[2,1],[2,3],[3,0],[3,2]] | agree |
| result.signatures[0].operators[2].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[2].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[0].operators[2].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[0].operators[2].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[0].operators[2].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[0].operators[2].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[0].operators[2].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[0].operators[2].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[0].operators[2].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[0].operators[2].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[0].operators[2].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [26,26,6] | [26,26,6] | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [7,7,44] | [7,7,44] | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.dim_ker_A | 40 | 40 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.dim_ker_S0 | 58 | 58 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 24 | 24 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 18 | 18 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [20,20,12] | [20,20,12] | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [3,3,46] | [3,3,46] | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 40 | 40 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 52 | 52 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 24 | 24 | agree |
| result.signatures[0].operators[2].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 12 | 12 | agree |
| result.signatures[0].operators[2].Q3_Q4.rank_S0_kappa0.null | 6 | 6 | agree |
| result.signatures[0].operators[2].Q3_Q4.rank_S0_kappa0.spacelike | 12 | 12 | agree |
| result.signatures[0].operators[2].Q3_Q4.rank_S0_kappa0.timelike | 12 | 12 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.charpoly.factors | [] | [] | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 64 | 64 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [20,20,12] | [20,20,12] | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [3,3,46] | [3,3,46] | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.dim_ker_A | 40 | 40 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 52 | 52 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 24 | 24 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 12 | 12 | agree |
| result.signatures[0].operators[2].Q3_Q4.timelike.rank_S0_kappa0 | 12 | 12 | agree |
| result.signatures[0].operators[2].operator | "CAC" | "CAC" | agree |
| result.signatures[0].operators[2].response | ["-1","-1","1/2","1/2"] | ["-1","-1","1/2","1/2"] | agree |
| result.signatures[0].operators[3].Q1.S1_identically_zero | false | false | agree |
| result.signatures[0].operators[3].Q1.S1_rank_at_e_m | [30,30,30,30] | [30,30,30,30] | agree |
| result.signatures[0].operators[3].Q1.c1_nonzero | 0 | 0 | agree |
| result.signatures[0].operators[3].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[3].Q1.grade_pairs_coupled | [[0,3],[1,2],[2,1],[3,0]] | [[0,3],[1,2],[2,1],[3,0]] | agree |
| result.signatures[0].operators[3].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[0].operators[3].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[0].operators[3].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[0].operators[3].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[0].operators[3].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[0].operators[3].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[0].operators[3].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[0].operators[3].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[0].operators[3].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[0].operators[3].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [17,16,14] | [17,16,14] | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [1,1,45] | [1,1,45] | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.dim_ker_A | 34 | 34 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.dim_ker_S0 | 47 | 47 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 18 | 18 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 13 | 13 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [17,17,0] | [17,17,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,34] | [0,0,34] | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 34 | 34 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 34 | 34 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 18 | 18 | agree |
| result.signatures[0].operators[3].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.rank_S0_kappa0.null | 17 | 17 | agree |
| result.signatures[0].operators[3].Q3_Q4.rank_S0_kappa0.spacelike | 30 | 30 | agree |
| result.signatures[0].operators[3].Q3_Q4.rank_S0_kappa0.timelike | 30 | 30 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.dim_ker_M | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.dim_ker_U | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.factor | "nu**2 + 16" | "nu**2 + 16" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.multiplicity_det_M | 16 | 16 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.multiplicity_det_U | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.partial_multiplicities_U | [1,1,1,1,1,1,1,1] | [1,1,1,1,1,1,1,1] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).derivative_form_inertia | [0,0,8] | [0,0,8] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).dim_ker_M | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).dim_ker_U | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).multiplicity_det_M | 16 | 16 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).multiplicity_det_U | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).second_order_form_inertia | [0,8,0] | [0,8,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).second_order_form_rank | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).w0 | "-sqrt(1/16)" | "-sqrt(1/16)" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.-sqrt(1/16).w0_squared | "1/16" | "1/16" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).derivative_form_inertia | [0,0,8] | [0,0,8] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).dim_ker_M | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).dim_ker_U | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).multiplicity_det_M | 16 | 16 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).multiplicity_det_U | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).second_order_form_inertia | [0,8,0] | [0,8,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).second_order_form_rank | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).w0 | "sqrt(1/16)" | "sqrt(1/16)" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4.sqrt(1/16).w0_squared | "1/16" | "1/16" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.degree | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.exponent | 8 | 8 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.factor | "nu**2 + 16" | "nu**2 + 16" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.massive_type | ["1/16","1/16"] | ["1/16","1/16"] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.non_real | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.rational_massive | ["1/16","1/16"] | ["1/16","1/16"] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 16.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.dim_ker_U | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.factor | "nu**2 + 32" | "nu**2 + 32" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.multiplicity_det_M | 12 | 12 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.multiplicity_det_U | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.partial_multiplicities_U | [1,1,1,1,1,1] | [1,1,1,1,1,1] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).derivative_form_inertia | [0,0,6] | [0,0,6] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).dim_ker_U | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).multiplicity_det_M | 12 | 12 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).multiplicity_det_U | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).second_order_form_inertia | [6,0,0] | [6,0,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).second_order_form_rank | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).w0 | "-sqrt(1/32)" | "-sqrt(1/32)" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.-sqrt(1/32).w0_squared | "1/32" | "1/32" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).derivative_form_inertia | [0,0,6] | [0,0,6] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).dim_ker_M | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).dim_ker_U | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).multiplicity_det_M | 12 | 12 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).multiplicity_det_U | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).second_order_form_inertia | [6,0,0] | [6,0,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).second_order_form_rank | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).w0 | "sqrt(1/32)" | "sqrt(1/32)" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4.sqrt(1/32).w0_squared | "1/32" | "1/32" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.degree | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.exponent | 6 | 6 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.factor | "nu**2 + 32" | "nu**2 + 32" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.massive_type | ["1/32","1/32"] | ["1/32","1/32"] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.non_real | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.rational_massive | ["1/32","1/32"] | ["1/32","1/32"] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 32.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.factor | "nu**2 + 64" | "nu**2 + 64" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.field_degree | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q3.semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).derivative_form_inertia | [0,0,1] | [0,0,1] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).dim_ker_M | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).dim_ker_U | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).multiplicity_det_M | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).multiplicity_det_U | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).second_order_form_inertia | [0,1,0] | [0,1,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).second_order_form_rank | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).w0 | "-sqrt(1/64)" | "-sqrt(1/64)" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.-sqrt(1/64).w0_squared | "1/64" | "1/64" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).derivative_form_inertia | [0,0,1] | [0,0,1] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).derivative_form_rank | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).dim_ker_M | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).dim_ker_U | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).multiplicity_det_M | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).multiplicity_det_U | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).second_order_form_inertia | [0,1,0] | [0,1,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).second_order_form_rank | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).semisimple_M | false | false | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).semisimple_U | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).w0 | "sqrt(1/64)" | "sqrt(1/64)" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4.sqrt(1/64).w0_squared | "1/64" | "1/64" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.Q4_status | "computed" | "computed" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.degree | 2 | 2 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.exponent | 1 | 1 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.factor | "nu**2 + 64" | "nu**2 + 64" | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.massive_type | ["1/64","1/64"] | ["1/64","1/64"] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.non_real | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.rational_massive | ["1/64","1/64"] | ["1/64","1/64"] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 + 64.tachyonic_type | [] | [] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 34 | 34 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [14,20,0] | [14,20,0] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,34] | [0,0,34] | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_A | 34 | 34 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 34 | 34 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 18 | 18 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[0].operators[3].Q3_Q4.timelike.rank_S0_kappa0 | 30 | 30 | agree |
| result.signatures[0].operators[3].operator | "E_OP" | "E_OP" | agree |
| result.signatures[0].operators[3].response | ["2","0","-1","0"] | ["2","0","-1","0"] | agree |
| result.signatures[0].signature | [3,1] | [3,1] | agree |
| result.signatures[0].status | "not reconstructed" | "complete" | not reconstructed |
| result.signatures[1].controls | "not reconstructed" | {"direct_hessian":["GQ(2, 0)","GQ(0, 4)","GQ(0, -4)","GQ(0, -4)","GQ(0, 0)"],"hand_xi_entry":true,"mass_sign":-1,"projectors":{"algebraic_part_is_curvature_span":true,"equivariant":true,"idempotent":true,"mutually_annihilating":true,"ranks":{"P1":1,"P15":15,"P20":20},"sum_identity":true},"star_adjoint_sign_1":-1} | not reconstructed |
| result.signatures[1].operators[0].Q1.S1_identically_zero | false | false | agree |
| result.signatures[1].operators[0].Q1.S1_rank_at_e_m | [38,38,38,38] | [38,38,38,38] | agree |
| result.signatures[1].operators[0].Q1.c1_nonzero | 192 | 192 | agree |
| result.signatures[1].operators[0].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[0].Q1.grade_pairs_coupled | [[1,2],[2,1],[3,4],[4,3]] | [[1,2],[2,1],[3,4],[4,3]] | agree |
| result.signatures[1].operators[0].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[0].Q2.ccc_inner_rank_15 | 6 | 6 | agree |
| result.signatures[1].operators[0].Q2.controls.ccc_inner_zero_on_20_and_1 | true | true | agree |
| result.signatures[1].operators[0].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[1].operators[0].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[1].operators[0].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[1].operators[0].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[1].operators[0].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[1].operators[0].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[1].operators[0].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[1].operators[0].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[1].operators[0].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[1].operators[0].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [13,15,16] | [13,15,16] | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [3,3,38] | [3,3,38] | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.dim_ker_A | 33 | 33 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.dim_ker_S0 | 44 | 44 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 17 | 17 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 11 | 11 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [16,17,0] | [16,17,0] | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,33] | [0,0,33] | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 33 | 33 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 33 | 33 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 17 | 17 | agree |
| result.signatures[1].operators[0].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.rank_S0_kappa0.null | 20 | 20 | agree |
| result.signatures[1].operators[0].Q3_Q4.rank_S0_kappa0.spacelike | 31 | 31 | agree |
| result.signatures[1].operators[0].Q3_Q4.rank_S0_kappa0.timelike | 31 | 31 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.dim_ker_M | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.dim_ker_U | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.factor | "nu + 2" | "nu + 2" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.multiplicity_det_M | 10 | 10 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.multiplicity_det_U | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.exponent | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.factor | "nu + 2" | "nu + 2" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.massive_type | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.non_real | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.rational_massive | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 2.tachyonic_type | ["-1/4"] | ["-1/4"] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.factor | "nu + 4" | "nu + 4" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.exponent | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.factor | "nu + 4" | "nu + 4" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.massive_type | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.non_real | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.rational_massive | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu + 4.tachyonic_type | ["-1/16"] | ["-1/16"] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.dim_ker_M | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.dim_ker_U | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.factor | "nu - 2" | "nu - 2" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.multiplicity_det_M | 10 | 10 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.multiplicity_det_U | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.exponent | 5 | 5 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.factor | "nu - 2" | "nu - 2" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.massive_type | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.non_real | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.rational_massive | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 2.tachyonic_type | ["-1/4"] | ["-1/4"] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.factor | "nu - 4" | "nu - 4" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.degree | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.exponent | 1 | 1 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.factor | "nu - 4" | "nu - 4" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.massive_type | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.non_real | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.rational_massive | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu - 4.tachyonic_type | ["-1/16"] | ["-1/16"] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.dim_ker_M | 3 | 3 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.dim_ker_U | 3 | 3 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.factor | "nu**2 - 12" | "nu**2 - 12" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.field_degree | 2 | 2 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.multiplicity_det_M | 6 | 6 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.multiplicity_det_U | 3 | 3 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.partial_multiplicities_U | [1,1,1] | [1,1,1] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.degree | 2 | 2 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.exponent | 3 | 3 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.factor | "nu**2 - 12" | "nu**2 - 12" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.massive_type | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.non_real | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.rational_massive | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 12.tachyonic_type | ["-1/12","-1/12"] | ["-1/12","-1/12"] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.dim_ker_M | 6 | 6 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.dim_ker_U | 6 | 6 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.factor | "nu**2 - 8" | "nu**2 - 8" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.field_degree | 2 | 2 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.multiplicity_det_M | 12 | 12 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.multiplicity_det_U | 6 | 6 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.partial_multiplicities_U | [1,1,1,1,1,1] | [1,1,1,1,1,1] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.degree | 2 | 2 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.exponent | 6 | 6 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.factor | "nu**2 - 8" | "nu**2 - 8" | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.massive_type | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.non_real | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.rational_massive | [] | [] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.tachyonic_type | ["-1/8","-1/8"] | ["-1/8","-1/8"] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 34 | 34 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [17,16,0] | [17,16,0] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,33] | [0,0,33] | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.dim_ker_A | 33 | 33 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 33 | 33 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 17 | 17 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[1].operators[0].Q3_Q4.timelike.rank_S0_kappa0 | 31 | 31 | agree |
| result.signatures[1].operators[0].operator | "CCC" | "CCC" | agree |
| result.signatures[1].operators[0].response | ["-1","0","0","0"] | ["-1","0","0","0"] | agree |
| result.signatures[1].operators[1].Q1.S1_identically_zero | false | false | agree |
| result.signatures[1].operators[1].Q1.S1_rank_at_e_m | [38,38,38,38] | [38,38,38,38] | agree |
| result.signatures[1].operators[1].Q1.c1_nonzero | 144 | 144 | agree |
| result.signatures[1].operators[1].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[1].Q1.grade_pairs_coupled | [[0,3],[1,2],[2,1],[3,0],[3,4],[4,3]] | [[0,3],[1,2],[2,1],[3,0],[3,4],[4,3]] | agree |
| result.signatures[1].operators[1].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[1].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[1].operators[1].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[1].operators[1].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[1].operators[1].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[1].operators[1].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[1].operators[1].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[1].operators[1].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[1].operators[1].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[1].operators[1].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [14,15,16] | [14,15,16] | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [3,3,39] | [3,3,39] | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.dim_ker_A | 30 | 30 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.dim_ker_S0 | 45 | 45 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 14 | 14 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 15 | 15 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [13,17,0] | [13,17,0] | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,30] | [0,0,30] | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 30 | 30 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 30 | 30 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 14 | 14 | agree |
| result.signatures[1].operators[1].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.rank_S0_kappa0.null | 19 | 19 | agree |
| result.signatures[1].operators[1].Q3_Q4.rank_S0_kappa0.spacelike | 34 | 34 | agree |
| result.signatures[1].operators[1].Q3_Q4.rank_S0_kappa0.timelike | 34 | 34 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.dim_ker_M | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.dim_ker_U | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.factor | "nu + 2" | "nu + 2" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.multiplicity_det_M | 10 | 10 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.multiplicity_det_U | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.degree | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.exponent | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.factor | "nu + 2" | "nu + 2" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.massive_type | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.non_real | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.rational_massive | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu + 2.tachyonic_type | ["-1/4"] | ["-1/4"] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.dim_ker_M | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.dim_ker_U | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.factor | "nu - 2" | "nu - 2" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.multiplicity_det_M | 10 | 10 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.multiplicity_det_U | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.partial_multiplicities_U | [1,1,1,1,1] | [1,1,1,1,1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.degree | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.exponent | 5 | 5 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.factor | "nu - 2" | "nu - 2" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.massive_type | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.non_real | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.rational_massive | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu - 2.tachyonic_type | ["-1/4"] | ["-1/4"] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.dim_ker_M | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.dim_ker_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.factor | "nu**2 + 4" | "nu**2 + 4" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.field_degree | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.kernel_gap | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.multiplicity_det_M | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.multiplicity_det_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.partial_multiplicities_M | [1,1,1,1,1,1] | [1,1,1,1,1,1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.partial_multiplicities_U | [1,1,1] | [1,1,1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.semisimple_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).derivative_form_inertia | [3,3,0] | [3,3,0] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).derivative_form_rank | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).dim_ker_M | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).dim_ker_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).kernel_gap_hermitian_radical | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).multiplicity_det_M | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).multiplicity_det_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).second_order_form_inertia | [0,0,3] | [0,0,3] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).second_order_form_rank | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).semisimple_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).w0 | "-sqrt(1/4)" | "-sqrt(1/4)" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.-sqrt(1/4).w0_squared | "1/4" | "1/4" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).derivative_form_inertia | [3,3,0] | [3,3,0] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).derivative_form_rank | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).dim_ker_M | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).dim_ker_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).kernel_gap_hermitian_radical | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).multiplicity_det_M | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).multiplicity_det_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).second_order_form_inertia | [0,0,3] | [0,0,3] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).second_order_form_rank | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).semisimple_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).w0 | "sqrt(1/4)" | "sqrt(1/4)" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4.sqrt(1/4).w0_squared | "1/4" | "1/4" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.Q4_status | "computed" | "computed" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.degree | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.exponent | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.factor | "nu**2 + 4" | "nu**2 + 4" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.massive_type | ["1/4","1/4"] | ["1/4","1/4"] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.non_real | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.rational_massive | ["1/4","1/4"] | ["1/4","1/4"] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 4.tachyonic_type | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.factor | "nu**2 + 8" | "nu**2 + 8" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.field_degree | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.kernel_gap_reading | "hermitian_radical" | "hermitian_radical" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).derivative_form_inertia | [0,0,1] | [0,0,1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).derivative_form_rank | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).dim_ker_M | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).dim_ker_U | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).multiplicity_det_M | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).multiplicity_det_U | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).second_order_form_inertia | [0,1,0] | [0,1,0] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).second_order_form_rank | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).semisimple_M | false | false | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).w0 | "-sqrt(1/8)" | "-sqrt(1/8)" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.-sqrt(1/8).w0_squared | "1/8" | "1/8" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_QU_quarter_second_derivative | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_derivative_form_zero_on_ker_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).derivative_form_inertia | [0,0,1] | [0,0,1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).derivative_form_rank | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).dim_ker_M | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).dim_ker_U | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).kernel_gap_hermitian_radical | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).multiplicity_det_M | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).multiplicity_det_U | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).second_order_form_inertia | [0,1,0] | [0,1,0] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).second_order_form_rank | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).semisimple_M | false | false | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).w0 | "sqrt(1/8)" | "sqrt(1/8)" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4.sqrt(1/8).w0_squared | "1/8" | "1/8" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.Q4_status | "computed" | "computed" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.degree | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.exponent | 1 | 1 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.factor | "nu**2 + 8" | "nu**2 + 8" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.massive_type | ["1/8","1/8"] | ["1/8","1/8"] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.non_real | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.rational_massive | ["1/8","1/8"] | ["1/8","1/8"] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 + 8.tachyonic_type | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.dim_ker_M | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.dim_ker_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.factor | "nu**2 - 8" | "nu**2 - 8" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.field_degree | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.multiplicity_det_M | 6 | 6 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.multiplicity_det_U | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.partial_multiplicities_U | [1,1,1] | [1,1,1] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.degree | 2 | 2 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.exponent | 3 | 3 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.factor | "nu**2 - 8" | "nu**2 - 8" | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.massive_type | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.non_real | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.rational_massive | [] | [] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.factors.nu**2 - 8.tachyonic_type | ["-1/8","-1/8"] | ["-1/8","-1/8"] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 40 | 40 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [14,16,0] | [14,16,0] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,30] | [0,0,30] | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.dim_ker_A | 30 | 30 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 30 | 30 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 14 | 14 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[1].operators[1].Q3_Q4.timelike.rank_S0_kappa0 | 34 | 34 | agree |
| result.signatures[1].operators[1].operator | "CAA" | "CAA" | agree |
| result.signatures[1].operators[1].response | ["-1","0","1/2","0"] | ["-1","0","1/2","0"] | agree |
| result.signatures[1].operators[2].Q1.S1_identically_zero | false | false | agree |
| result.signatures[1].operators[2].Q1.S1_rank_at_e_m | [24,24,24,24] | [24,24,24,24] | agree |
| result.signatures[1].operators[2].Q1.c1_nonzero | 192 | 192 | agree |
| result.signatures[1].operators[2].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[2].Q1.grade_pairs_coupled | [[0,1],[0,3],[1,0],[1,2],[2,1],[2,3],[3,0],[3,2]] | [[0,1],[0,3],[1,0],[1,2],[2,1],[2,3],[3,0],[3,2]] | agree |
| result.signatures[1].operators[2].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[2].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[1].operators[2].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[1].operators[2].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[1].operators[2].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[1].operators[2].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[1].operators[2].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[1].operators[2].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[1].operators[2].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[1].operators[2].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[1].operators[2].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [26,26,6] | [26,26,6] | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [7,7,44] | [7,7,44] | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.dim_ker_A | 40 | 40 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.dim_ker_S0 | 58 | 58 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 24 | 24 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 18 | 18 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [20,20,12] | [20,20,12] | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [3,3,46] | [3,3,46] | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 40 | 40 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 52 | 52 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 24 | 24 | agree |
| result.signatures[1].operators[2].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 12 | 12 | agree |
| result.signatures[1].operators[2].Q3_Q4.rank_S0_kappa0.null | 6 | 6 | agree |
| result.signatures[1].operators[2].Q3_Q4.rank_S0_kappa0.spacelike | 12 | 12 | agree |
| result.signatures[1].operators[2].Q3_Q4.rank_S0_kappa0.timelike | 12 | 12 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.charpoly.factors | [] | [] | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 64 | 64 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [20,20,12] | [20,20,12] | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [3,3,46] | [3,3,46] | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.dim_ker_A | 40 | 40 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 52 | 52 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 24 | 24 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 12 | 12 | agree |
| result.signatures[1].operators[2].Q3_Q4.timelike.rank_S0_kappa0 | 12 | 12 | agree |
| result.signatures[1].operators[2].operator | "CAC" | "CAC" | agree |
| result.signatures[1].operators[2].response | ["-1","-1","1/2","1/2"] | ["-1","-1","1/2","1/2"] | agree |
| result.signatures[1].operators[3].Q1.S1_identically_zero | false | false | agree |
| result.signatures[1].operators[3].Q1.S1_rank_at_e_m | [30,30,30,30] | [30,30,30,30] | agree |
| result.signatures[1].operators[3].Q1.c1_nonzero | 0 | 0 | agree |
| result.signatures[1].operators[3].Q1.derived_term3_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[3].Q1.grade_pairs_coupled | [[0,3],[1,2],[2,1],[3,0]] | [[0,3],[1,2],[2,1],[3,0]] | agree |
| result.signatures[1].operators[3].Q1.repaired_term2_nonzero_at_e0 | true | true | agree |
| result.signatures[1].operators[3].Q2.controls.dims_E_Ea | [20,12,32] | [20,12,32] | agree |
| result.signatures[1].operators[3].Q2.controls.intersections_sum_to_rank | true | true | agree |
| result.signatures[1].operators[3].Q2.controls.schur_15_in_E_plus_Ea | true | true | agree |
| result.signatures[1].operators[3].Q2.controls.schur_1_in_span_g | true | true | agree |
| result.signatures[1].operators[3].Q2.dim_15_in_E | 0 | 0 | agree |
| result.signatures[1].operators[3].Q2.dim_15_in_Ea | 6 | 6 | agree |
| result.signatures[1].operators[3].Q2.one_part.coefficients_EF_g_EFprime_g | ["0","0"] | ["0","0"] | agree |
| result.signatures[1].operators[3].Q2.one_part.rank | 0 | 0 | agree |
| result.signatures[1].operators[3].Q2.rank_15 | 6 | 6 | agree |
| result.signatures[1].operators[3].Q3_Q4.covariance.A_intertwines | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.covariance.covariance_verified | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.covariance.hessian_covariant | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.covariance.pairing_invariant | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.covariance.star_intertwines | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.covariance.traceless | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.G1_restricted_inertia | [15,18,14] | [15,18,14] | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.S1_restricted_inertia | [1,1,45] | [1,1,45] | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.dim_ker_A | 34 | 34 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.dim_ker_S0 | 47 | 47 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.quotient_kerA_over_exact | 18 | 18 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_null.quotient_kerS0_over_kerA | 13 | 13 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.G1_restricted_inertia | [14,20,0] | [14,20,0] | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.S1_restricted_inertia | [0,0,34] | [0,0,34] | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_A | 34 | 34 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.dim_ker_S0 | 34 | 34 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.quotient_kerA_over_exact | 18 | 18 | agree |
| result.signatures[1].operators[3].Q3_Q4.kernel_S0_spacelike.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.rank_S0_kappa0.null | 17 | 17 | agree |
| result.signatures[1].operators[3].Q3_Q4.rank_S0_kappa0.spacelike | 30 | 30 | agree |
| result.signatures[1].operators[3].Q3_Q4.rank_S0_kappa0.timelike | 30 | 30 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.degree | 64 | 64 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.dim_ker_M | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.dim_ker_U | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.factor | "nu + 4" | "nu + 4" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.multiplicity_det_M | 16 | 16 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.multiplicity_det_U | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.partial_multiplicities_U | [1,1,1,1,1,1,1,1] | [1,1,1,1,1,1,1,1] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.exponent | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.factor | "nu + 4" | "nu + 4" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.massive_type | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.non_real | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.rational_massive | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 4.tachyonic_type | ["-1/16"] | ["-1/16"] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.factor | "nu + 8" | "nu + 8" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.exponent | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.factor | "nu + 8" | "nu + 8" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.massive_type | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.non_real | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.rational_massive | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu + 8.tachyonic_type | ["-1/64"] | ["-1/64"] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.dim_ker_M | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.dim_ker_U | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.factor | "nu - 4" | "nu - 4" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.multiplicity_det_M | 16 | 16 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.multiplicity_det_U | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.partial_multiplicities_U | [1,1,1,1,1,1,1,1] | [1,1,1,1,1,1,1,1] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.exponent | 8 | 8 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.factor | "nu - 4" | "nu - 4" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.massive_type | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.non_real | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.rational_massive | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 4.tachyonic_type | ["-1/16"] | ["-1/16"] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.dim_ker_M | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.dim_ker_U | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.factor | "nu - 8" | "nu - 8" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.field_degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.multiplicity_det_M | 2 | 2 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.multiplicity_det_U | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.partial_multiplicities_U | [1] | [1] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.degree | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.exponent | 1 | 1 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.factor | "nu - 8" | "nu - 8" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.massive_type | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.non_real | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.rational_massive | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu - 8.tachyonic_type | ["-1/64"] | ["-1/64"] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.control_ker_U_in_ker_M | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.dim_ker_M | 6 | 6 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.dim_ker_U | 6 | 6 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.factor | "nu**2 - 32" | "nu**2 - 32" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.field_degree | 2 | 2 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.kernel_gap | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.kernel_gap_reading | "cross_annihilator" | "cross_annihilator" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.multiplicity_det_M | 12 | 12 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.multiplicity_det_U | 6 | 6 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.partial_multiplicities_M | "not computed" | "not computed" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.partial_multiplicities_U | [1,1,1,1,1,1] | [1,1,1,1,1,1] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.semisimple_M | false | false | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q3.semisimple_U | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.Q4_status | "not_applicable" | "not_applicable" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.degree | 2 | 2 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.exponent | 6 | 6 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.factor | "nu**2 - 32" | "nu**2 - 32" | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.massive_type | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.non_real | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.rational_massive | [] | [] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.factors.nu**2 - 32.tachyonic_type | ["-1/32","-1/32"] | ["-1/32","-1/32"] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.charpoly.nilpotent_multiplicity | 34 | 34 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.G1_restricted_inertia | [17,17,0] | [17,17,0] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.S1_restricted_inertia | [0,0,34] | [0,0,34] | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.controls.exact_in_ker_A | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.controls.exact_rank | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.controls.ker_A_in_ker_S0 | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.controls.nullity_S0_at_least_exact | true | true | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.dim_exact_directions | 16 | 16 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_A | 34 | 34 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.dim_ker_S0 | 34 | 34 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.quotient_kerA_over_exact | 18 | 18 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.kernel_S0.quotient_kerS0_over_kerA | 0 | 0 | agree |
| result.signatures[1].operators[3].Q3_Q4.timelike.rank_S0_kappa0 | 30 | 30 | agree |
| result.signatures[1].operators[3].operator | "E_OP" | "E_OP" | agree |
| result.signatures[1].operators[3].response | ["2","0","-1","0"] | ["2","0","-1","0"] | agree |
| result.signatures[1].signature | [1,3] | [1,3] | agree |
| result.signatures[1].status | "not reconstructed" | "complete" | not reconstructed |
| result.source_commit | "not reconstructed" | "aac4e42c0681dee13c75222ee8a9d31bced6d6fe" | not reconstructed |
| result.status | "not reconstructed" | "complete" | not reconstructed |
| result.uncomputed | "not reconstructed" | [] | not reconstructed |
