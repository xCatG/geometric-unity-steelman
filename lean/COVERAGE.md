# Coverage of the B02 prose arguments

This is a partial formalization with explicit boundaries, not a certificate of the complete B02 classification or of `result.json`. The concrete model follows the repository's sparse form/blade conventions over exact Gaussian rationals. General tensor-algebra theorems are separate from that executable model wherever the algebra identification has not been proved.

## Findings

**F1 — incorrect opening parity sentence.** The first wedge has total form degree n-1 (3 at n=4), and the final pre-star wedge has degree 1. The relevant even number is the *product* of the operand degrees, not their sum. `B02.wedge_total_degree_counterexample` refutes the literal sentence; `B02.bracket_degree_products_even` proves the corrected statement for every even n>=2. This is a wording/justification defect, not evidence that the componentwise C/A definitions are wrong.

**F2 — dimension-two ambiguity in the all-even-n kappa wording.** In signature (1,1), take R_abcd = eta_a eta_b (delta_ac delta_bd - delta_ad delta_bc), Phi1=F, Phi2=B, CCC. The actual contractions give Ric=g and S=2, and the response is the nonzero -F. Both (c,kappa)=(-1,0) and (1,1) describe that same response as c E_F(Ric-kappa Sg). `B02.DimensionTwo.nonunique_parameter_descriptions` certifies these concrete equalities. This does not refute the zero inner commutator, a chosen representation with kappa=0, or the n=4/n=14 classification. It refutes uniqueness inferred solely from the stated all-even-n scope: n=2 has no independent traceless-Ricci sector. The formal witness is one nonzero curvature; it does not by itself quantify over all 2D curvature. Proposed correction: restrict a unique-kappa conclusion to dimensions with a nontrivial traceless-Ricci sector and establish the nondegeneracy used to identify the coefficients.

**Stronger headline scope.** Actual sparse B and B-prime inner C cancellation needs pair symmetry only. The proofs work for every n and arbitrary integer eta; B-prime also allows arbitrary Gaussian-rational phase. No even-n, Bianchi, or metric-unit hypothesis is needed for these two identities.

## Claim-level coverage

Names below are qualified by B02 unless otherwise stated. The exhaustive theorem table follows this document's narrative in the generated report. `exact` means the specified argument or supporting identity, not a claim that all later classification conclusions follow. `weaker` always identifies the unproved specialization.

| Prose claim | Main theorem(s) | Fidelity and boundary |
|---|---|---|
| Pinned w_ab=eta_a eta_b | pinned_hodge_weight; pinned_pair_weight | stronger: all dimensions, all blades (first theorem), arbitrary integer eta |
| Inner C against B vanishes | Concrete.headline_inner_B_concrete | stronger: actual sparse coefficients, all n and eta, pair symmetry only |
| Inner C against B-prime vanishes | Concrete.headline_inner_BPrime_concrete | stronger: actual sparse coefficients, all n and eta, arbitrary phase, pair symmetry only |
| Dropping xi raising factors breaks cancellation | Concrete.dropped_witness_inner_B; Concrete.dropped_witness_inner_BPrime; witness_* symmetry certificates | exact negative-scope examples in (3,1); B-prime uses native_decide |
| Test 1 degree | Concrete.shiab_degree | exact: actual sparse model, n>=2, arbitrary homogeneous Phi1/Phi2/input and all 8 modes |
| Hodge reparametrization | Concrete.otherShiab_reparametrization; otherShiab_readout_reparametrization | exact over the permitted rational model: even n>=2, actual sparse operations and all 8 modes; the second includes the readout sign |
| Test 2(a) bracket closure | Structural.commutator_skew; imaginary_anticommutator_skew | exact algebraic argument under the stated StarRing/central-imaginary laws |
| Test 2(a) full response closure | Structural.OperatorData.response_mem | weaker: closure in a supplied real submodule with explicit operation-preservation assumptions; no concrete A-adjoint or Phi membership identification |
| Test 3(a) dressed covariance | Structural.tensor_dressed_covariance | weaker: fully proved in genuine tensor products of associative algebras, including factorwise stars and C/A; no identification of this ring model with sparse blade multiplication |
| Parameter affine structure and six probes | Concrete.concrete_parameter_affine; concrete_six_probe_formula; Structural.response_parameter_extension | exact rational executable interpolation; generic any-field extension argument is proved. Weaker than the final real closed-form assertion: no concrete real-coefficient model or six closed-form identities is certified |
| Input linearity | Concrete.concrete_input_linear | exact rational sparse Shiab linearity, all n/eta/modes |
| Rank sandwich/spanning | rank_sandwich; span_eq_top_of_rank_certificate; curvature_extension | weaker: rank lower bound, ambient dimension and checks on a supplied set are named inputs; no actual KN membership, rank3185/20, or dimension proof |
| Rational to real extension | rational_span_extends_to_real; real_scalar_extension_identity | exact tensor scalar-extension argument; weaker than actual real curvature identity until the coordinate-space identification and checks are supplied |
| Test 4(iii) steps 1 and 4 | Structural.tensorDerivation_product; tensorBracket_derivation; tensor_response_derivation | weaker in specialization only: actual algebra/tensor Leibniz and composition proved; identifying sparse generator_action with these derivations remains unproved |
| Tests 4(i),4(ii) | hypotheses ha,hb,hH2,hHN,hH1 of tensor_response_derivation | hypothesis-only: Phi annihilation and form-star commutation are explicit, not silently taken as axioms |
| Lie closure and integration | commutation_lie_closed; invariant_lie_closed; commutation_exponential | exact individual algebraic/analytic steps; the analytic step uses Mathlib's proved exponential theorem |
| Spin0 from exponentials | Structural.equivariant_of_exponential_generators | weaker: group representation, exponentials_generate, and commutes_with_exponentials supplied; actual Spin0 and representation-exp compatibility not constructed |
| Signature parity | Samples.split_CCC; split_CAA; euclidean_CCC; euclidean_CAA | weaker: actual constant-curvature samples in (2,2),(4,0), not all curvature or parity in all signatures; native_decide |
| Recorded substitutions / full closed form | no final classification theorem | hypothesis-only/gap: a finite bridge does not certify the original 3185-row computation, full response formula, or pure-sector classifications |

## Remaining obligations, explicitly not proved

1. Associativity and the concrete sparse-to-tensor algebra isomorphism, plus the A-adjoint StarRing identification. The concrete headline, Hodge, degree, and rational interpolation proofs do not need that bridge. Tensor covariance and closure are valid algebraic theorems but not yet instantiated to the executable Clifford implementation.
2. The form derivation corresponding to `generator_action`, its agreement with the tensor construction, invariant Phi, and form-Hodge equivariance for general n. The finite (3,1) generator bridge tests agreement of implementations, not these general laws.
3. Actual Spin0 and its representation; adjacent-generator Lie spanning; representation compatibility with exponentiation; generation of the identity component. No custom Lean axioms are declared: all used assumptions are theorem arguments. The generic subgroup theorem takes exponential commutation directly; connecting it to `commutation_exponential` is still an obligation.
4. Actual KN rows in a formal curvature space, its dimension, rank certificate at n=4 or n=14, and its real scalar-extension identification. `curvature_dimension_numerals` proves only arithmetic 20/3185. The modular-to-rational rank inequality is also an explicit input, not a certified rank algorithm.
5. The full response formula on the six parameter probes and the curvature spanning family, concrete xi/Ric/S linear maps for general n, concrete real parameter extension, nondegenerate identification of c/kappa, and general signature parity. The rational interpolation and generic scalar-extension machinery prove the extension *argument*, not its numerical premises.
6. No theorem directly packages all scaling/Hodge/parameter-span consequences of inner cancellation into a complete CCC classification. The concrete coefficient and bilinearity theorems provide the relevant components; the scope report does not count an unproved final corollary as proved.

## Lie-theory sources for the uninstantiated hypotheses

- Jamie Mason, *Representation Theory*, Lecture 6, Theorem 1.6.5: the exponential image generates the identity component; Proposition 1.6.6 uses compatibility of a Lie homomorphism with exponentials. https://www.maths.dur.ac.uk/users/jamie.j.mason/RepresentationTheoryNotes-epiphany/Ch1.S6.html
- Jean Gallier, *Clifford Algebras, Clifford Groups, and a Generalization of the Quaternions*, sections 1.6 and 1.9, supplies the Spin(p,q)/SO(p,q) and Lie-algebra setting. https://www.cis.upenn.edu/~jean/clifford.pdf
- The specific adjacent-bivector spanning step still needs a formal proof. In the diagonal Clifford convention the recurrence [J_ab,J_bc]=eta_b J_ac for a<b<c, J_ab=Gamma_a Gamma_b/2, explains how adjacent pairs reach all pairs. This recurrence and its identification with the cited Lie algebra are unformalized obligations, not claims imported as certified facts from a citation.

## Trust boundary

No sorry and no custom axioms. General identities use at most propext, Classical.choice and Quot.sound. `native_decide` adds Lean.ofReduceBool **and Lean.trustCompiler** in Lean 4.24. It occurs in the dropped-factor B-prime witness and optional sample/dimension-two canonical-list certificates (including downstream users). These finite computations trust the native compiler; they are additionally compared with the actual Python implementation. Kernel `decide +kernel` certificates do not incur those native axioms. `Audit.lean` prints every public theorem's actual dependencies; `AxiomAudit.txt` and the handoff result retain the full output.
