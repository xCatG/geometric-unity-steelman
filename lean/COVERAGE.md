# Lean coverage: B02 prose and B03 explicit matrices

The B02 portion is a partial formalization with explicit boundaries, not a certificate of the complete B02 classification or of `result.json`. The concrete model follows the repository's sparse form/blade conventions over exact Gaussian rationals. General tensor-algebra theorems are separate from that executable model wherever the algebra identification has not been proved.

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

## B03: explicit real structures and chirality

All required fixed-instance claims in the B03 handoff are proved for the four
specified splits. There are 81 new public theorem declarations, no sorry, no
custom axioms, and no native_decide in B03. The existing B02 coverage and its
separate native-computation boundary remain as documented above.

The coefficients of the interpreted operators are complex numbers. The
executable monomial representation stores a column permutation on Fin (2^m)
and phases in Fin 4, with M[perm[j],j]=i^phase[j]. `act_column_entry` proves
that the complex-linear interpretation uses precisely this column convention;
`act_mul` proves compatibility with matrix composition. `J` is an actual
complex-antilinear map on the full complex spinor space, not just a sign table.

The model computes leading-Z Jordan-Wigner columns directly from the bits of j.
The 14,644-column bridge compares those entries exhaustively with the actual
Python functions on every requested matrix and split. This is an executable
cross-check, not a formal semantics proof for the Python language. The generic
Mono structure permits arbitrary column maps; all concrete Clifford generators
have the certified square relations, so the required inverse/permutation laws
are consequences rather than an unverified matrix-instance assumption.

Two optimizations are explicitly justified. `imaginary_selector_iff` and the
three `selection*` certificates prove that the axis-parity selector is exactly
the Python predicate that all gamma entries are imaginary. Each `first_chirality*`
certificate proves the selected candidate squares to one and is Hermitian,
and rejects every earlier phase by failure of square-one. `hermitian_entries`
connects that predicate to actual conjugate-transposed complex entries. Thus
the model checks the library's *first* accepted phase, not just an arbitrary
valid chirality sign.

| Required claim | Theorems in namespace B03 | Fidelity |
|---|---|---|
| Clifford anticommutators | clifford_relations77, clifford_relations95, clifford_relations31; underlying clifford* certificates | exact on every complex spinor and every pair of axes |
| J complex-antilinear | J_antilinear | stronger: arbitrary dimension and arbitrary monomial B |
| J squared is +1 at (7,7), -1 at (9,5),(3,1) | real_structure_square77, real_structure_square95, real_structure_square31; underlying j_square* | exact; both (9,5) splits share the same matrix |
| J commutes with spin generators | J_all_generators77, J_all_generators95, J_all_generators31 | stronger than adjacent-only scope: every gamma bivector, with no Lie-generation hypothesis |
| J preserves C at d=14 and exchanges at (3,1) | J_chirality77/95/31; chirality_preserves77/95; chirality_exchanges31 | exact operator and real-eigenvalue statements; J-square supplies invertibility |
| Cartans diagonal with entries +1 or -1 | cartan2, cartan7; cartan_eigenvalues | exact, for every pair/column in the natural ordering; split order selects these same pairs |
| Cartans pairwise commute | cartan_commutes with cartan2 or cartan7 | exact via the proved general diagonal-monomial commutation law |
| Every sign pattern occurs once | every_weight31, every_weight77, every_weight95a, every_weight95b | exact existence and uniqueness for every Boolean sign tuple; false means +1, true means -1 |
| C=-Pi at (7,7), C=+Pi at the others | chirality_parity77, chirality_parity95a, chirality_parity95b, chirality_parity31 | exact full monomial equality; Pi is defined from even-minus-count parity of the actual Cartan weights |
| J weight signs (+------), (+------), (-+-----), (+-) | j_weight77, j_weight95a, j_weight95b, j_weight31 | exact for every basis column and every split-ordered coordinate |

**Findings:** no numerical disagreement or unstated convention was found within
these explicitly pinned constructions. In particular the control's J-square
is -1 and it exchanges chirality, as recorded. The signs are claims about the
specified B and library C; this does not assert that every possible real
structure or chirality convention gives the same representative.

**Remaining gaps within the requested fixed-instance claims:** none. The
optional general-signature formula was not proved. This work does not prove
RS projector identities, branching/character equalities, the named module
partner dictionary, Spin-group integration, or dynamical conclusions. Those
are outside this handoff's enumerated matrix claims. B02's earlier explicit
gaps are unchanged.

All B03 finite certificates use `decide +kernel`, including the 128-dimensional
J-square and C/Pi facts. The complete public axiom output is retained in
`AxiomAuditB03.txt` and the combined `AxiomAudit.txt`. See `ValidationB03.md` for
fresh build, bridge and seeded-fault evidence; every B03 theorem is mapped in
the appended section of `THEOREMS.md`.

## B05 tilted-action sign check

`B05Sign` checks the algebra behind GU (5.9), (6.2), (6.4)-(6.5),
(6.11)-(6.16), (6.19)-(6.22), and (7.3)-(7.4). It keeps the printed
minus sign (`tauLit`) and the proposed plus sign (`tauRec`) separate.

The model assumes an arbitrary possibly noncommutative ring, units, and an
additive endoderivation satisfying Leibniz. It replaces the module of
one-forms by the same coefficient algebra, as when taking one directional
component of a covariant derivative. All coefficient order is retained.
This is a **modelling choice**, not a formalization of smooth bundles,
exterior calculus, or the specific U(64,64) gauge group. General-ring
identities are exact in that model and algebraically stronger than a
matrix-only identity; no Lie-group smoothness is proved.

The affine-coordinate distinction matters: (6.2) acts on `alpha=A-A0`.
`connectionAct D A0 A h` is defined as
`A0 + act62 D (A-A0) (h,0)`, with `D` representing `d_A0`.
This does not assume that the base connection is invariant under gauge
transformations. The pair `biConnection` is exactly the affine-coordinate
reading `(A0+varpi, A0+epsilon^-1 D epsilon)` of (6.19)/(6.22).

| Claim | Literal minus | Reconstructed plus |
|---|---|---|
| (6.4)/(6.5) is an injective algebraic group homomorphism into (5.9) | yes | yes |
| (6.20), first connection | residual `-2 h^-1 D h` | covariant |
| (6.20), second connection | covariant | covariant |
| (7.4), torsion defined by (7.3) | residual `-2 h^-1 D h` | covariant |
| (6.14), projection defined by (6.11) | invariant | residual `2 epsilon (D h) h^-1 epsilon^-1` |
| (6.6)-(6.9), stabilizes affine origin | yes | origin maps to `2 h^-1 D h` |
| (6.15)-(6.16) defines a left action of (5.9) | yes; independent of the tilted-map choice | same formula is still a left action; its printed projection no longer descends along this tilted action |

The matrix witness takes `R=Matrix (Fin 2) (Fin 2) Int`,
`z=diag(1,0)`, `D x=z*x-x*z`, and the swap matrix as the unit `h`.
Its logarithmic derivative is `diag(-1,1)` and the literal residual is
`diag(2,-2)`, provably nonzero. With `epsilon=1`, `varpi=0`, the literal
connection/torsion covariance claims fail, and the reconstructed projection
invariance claim fails. This is a concrete countermodel to the general
ring identities, not an assertion that these integer matrices realize the
source's gauge subgroup or the audit's central U(1) jet.

The audit's `h=1` means `h(p)=1`, with a nonzero derivative at that point.
Our endoderivation necessarily kills the constant ring identity; this is a
representation limitation, **not a correction to that local-jet example**.
No sign choice alone preserves all the listed printed formulas. In
characteristic two or when `2 h^-1 D h=0`, the displayed residual may
vanish; the structural theorem retains this possibility.

Every B05 theorem is inventoried in `THEOREMS.md`. `AxiomAuditB05Sign.txt`
contains the actual axiom output, including the group instance and both
homomorphism structures. Validation and source provenance are recorded in
`ValidationB05Sign.md`. No fermionic covariance, anomaly, physical gauge
symmetry, or global geometric claim is proved; B02/B03 scope is unchanged.

## B07 Argon: generous readings, five targets

`B07Argon` is a default Lake target. It adds 57 theorems and three audited
proof-bearing definitions. All five requested targets were run. These are
pointwise algebraic results, not a new gravitational theory or a verification of
an embedding, the GU action as printed, or the numerical B07 classification.

**T1 (Gauss).** With positive unit normal convention,
`R(a,b,c,d)=h(a,c)h(b,d)-h(a,d)h(b,c)=(h ⊙ h)/2` and
`Ric(i,j)=sum_a eta(a) R(a,i,a,j)`, the actual contractions give
`Ric=tr_g(h)h-h g^-1 h` and
`S=tr_g(h)^2-sum_(i,a) eta(i)eta(a)h(i,a)h(a,i)`.
For `h=lam*g`, `Ric=(n-1)lam^2*g`, `S=n(n-1)lam^2`, and
`G=-(n-1)(n-2)lam^2*g/2`. The Einstein tensor is proportional to g iff
`h g^-1 h-tr_g(h)h` is proportional to g, in every dimension, including four.
The symmetric Euclidean witness `diag(1,2,0,0)` is non-umbilic and has
`G=diag(0,0,-2,-2)` by hand. Lean certifies G00=0 and G22=-2, which suffice to prove it is not proportional to g; it does not certify the full diagonal. Coefficients are an
arbitrary characteristic-zero field; characteristic two is excluded by the
half, and fields of odd positive characteristic are not covered by this module.
The contraction identities themselves need neither symmetry nor a lower bound
on dimension. Symmetry is needed to interpret the input as a second fundamental
form. A timelike normal changes the overall Gauss sign; no ambient geometry,
Clifford Shiab, dynamics, or cosmological evolution is constructed.

**T2 (Cartan torsion).** This is Cartan torsion of the form connection, not GU's
augmented torsion. `K(a,b,c)=g((nabla-LC)_a e_b,e_c)`, with K antisymmetric in
the last two indices. Define `tau(a,b,c)=K(a,b,c)-K(b,a,c)` and
`t(b)=sum_a eta(a)tau(a,b,a)`. The proved divergence difference is `t(b)V(b)`.
Over the rational pointwise model, trace torsion is
`(g(a,c)t(b)-g(b,c)t(a))/(n-1)`, axial torsion is the cyclic average of tau,
and the tensor part is the remainder. The axial part is totally alternating;
the tensor part is antisymmetric in the first pair, has zero trace and zero
cyclic sum. Their divergence contributions vanish. The proof requires `n-1`
nonzero for the decomposition, and `eta(a)^2=1` for its trace normalization.
This is an algebraic decomposition, not a formal theorem about integrals.
The one-form formula `d w=Alt(nabla w)+tau contracted with w` is proved in
coordinates. A rational 3D axial example has zero trace and nonzero exterior
correction. Thus a trace-only divergence theorem does not make the entire H11
adjoint defect trace-only. See the hand-derived counterexample below.

**T3 (epsilon).** Reuse the B05Sign `Diff` model already present on master;
no pending branch was merged. Extend the derivation coefficientwise to actual
Mathlib central dual numbers over an arbitrary noncommutative ring. For
`epsilon(s)=epsilon(1+s beta)`, the coefficient of s in `epsilon^-1 D epsilon`
is `D beta+[epsilon^-1 D epsilon,beta]`; the augmented torsion variation at
fixed varpi is its negative. H5 C1 and weighted cubic residuals are invariant
when all arguments and operator slots are conjugated together and the supplied
pairing is invariant. The directional derivative identity undresses `D_B` to D;
the full action-shaped algebraic expression undresses along with it.
For `U=Ad(epsilon)T`, the actual dual-number calculation gives
`delta U=-Ad(epsilon)(D beta+[varpi,beta])`. The hypothesis of
`epsilon_no_independent_equation` is `forall a, E(Ad(epsilon) a)=0`.
Because Ad(epsilon) is bijective, this is E=0 on the whole ring; the epsilon
direction is one element of that ring. The spanning interpretation is that
the varpi directions already fill U-space. The theorem specializes the proved
dual-number direction under this assumption; it constructs neither varpi
variations nor a chain rule and is **not a Noether certificate**. The analytic
chain rule, integration by parts, spacetime forms and a local Euler-Lagrange
distribution are not formalized. Redundancy for an entire action is conditional
on factorization through U and that spanning interpretation, with the A
connection rather than just B in the induced direction. Extra epsilon
dependence, a variable metric, or a different completion can change the action
and its varpi equation; none is silently included.

**T4 (grades).** The scalar-support proof uses `B02.Concrete.bladeMul`, not a
replacement Clifford product. Its output blade is empty iff the two blades
are equal; if all metric entries are nonzero, its coefficient is nonzero too.
The bilinear scalar pairing of homogeneous unequal grades vanishes. In an
abstract full basis (which may include all form and internal indices), the
paired symbol matrix has `C1=M+transpose(M)`. Projecting to an unordered grade
pair commutes with C1, and C1 vanishes iff it vanishes on every pair. This is a
kernel splitting criterion; a bundled Lean direct-sum equivalence with the
Python gate matrices is not constructed. `diagonal_block_zero` proves only the
last arithmetic sign step in dimension 1: a rational scalar x satisfying the
assumed equality `(-1)^(2+j) x = (-1)^(3+j) x` is zero. Intertwining is assumed,
not constructed. This is not a block theorem and is **not citable as H12 parity**.
Applying the sign step to j=l blocks requires establishing the total-parity
intertwiner and its relevant central Spin action separately; the blade model
does not supply them. No theorem attributes the six response-zero directions
to particular grade pairs.

**T5 (Schur).** Mathlib's actual `FDRep` category over the complex numbers gives
scalar endomorphisms of simple objects. In a chosen finite semisimple biproduct,
inequivalent simple components have zero off-diagonal entries, and a
multiplicity-one simple summand is preserved and acted on by a scalar. On m
copies of one simple representation, every endomorphism is a scalar-entry
biproduct matrix and the matrix assignment is injective: all m-by-m matrices
are available, with unique coefficients. This certifies the matrix description
of the commutant on chosen isotypic components; a bundled algebra isomorphism
to a direct sum of matrix algebras is not separately constructed. There is no
concrete Spin representation, no grade-to-isotypic identification, and no
interpretation of `ym_symbol` entry ratios as eigenvalues or couplings.

### B07 findings and boundaries

1. **FINDING: trace-only is a divergence statement.** The optional extension to
   the full `L†-L` remainder is false without extra hypotheses on X. An explicit
   hand counterexample in four dimensions is the coframe
   `e0=dx, e1=dy, e2=dz-x dy, e3=dw`. Declare the frame parallel and orthonormal.
   This gives a metric connection with torsion `tau^2=de2=-e0 wedge e1` and
   zero torsion trace. Set `theta=e2` and `X(beta)=theta wedge beta`. X is parallel
   and its first-order C1 symbol vanishes by exterior antisymmetry. Its wedge
   transpose is `X^t(t)=t wedge theta`; hence
   `L†t-Lt=-t wedge dtheta`, nonzero at `t=e3`. This full geometric example is
   a hand derivation, not a Lean manifold certificate. The Lean axial witness
   separately certifies the failure of trace-only dependence for d itself.
   This X is not asserted to be one of the universal Spin intertwiners.
2. **FINDING: full epsilon dressing matters.** The bare delta-T formula uses B,
   but the variation of the entire undressed field uses A. For an action
   factorized through U, with varpi directions spanning U-space and E vanishing
   on all those directions, the epsilon direction supplies no additional
   stationarity condition. The formal result is not a Noether certificate or
   a demonstrated independent epsilon equation lifting C2.
   This sharpens the discussion's proposed extension; it does not rule out a
   genuinely different action with independent epsilon or metric dependence.
3. **FINDING: a pure Gauss term is not generic bending.** The umbilic case gives
   a Lambda-type algebraic tensor; the non-umbilic witness fails. There is no
   deduction of dynamic dark energy, a shifted Shiab kappa, or a Higgs field.
4. **FINDING: the field scope needs a half.** The task's unrestricted “field”
   wording needs characteristic not two. The formal file uses characteristic
   zero; extending to odd positive characteristic is not claimed.

`B07Audit.lean` prints every new theorem and the three proof-bearing dual-number
definitions. `Audit.lean` includes the same checks with all previous audits.
The new sources contain no sorry, admit, native_decide or custom axioms.
Existing B02 native-computation dependencies remain as documented above and
are not used by the new main theorems.
