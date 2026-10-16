# B02 and B03 theorem-to-claim inventory

B02: 188 theorem declarations (179 public). Private helpers are included as supporting identities; their dependencies are reached through the public theorems. Fidelity is relative to the named subargument, not the full classification. See COVERAGE.md for the claim-level boundaries.

| Lean theorem | Source | Prose argument | Fidelity |
|---|---|---|---|
| `B02.Concrete.bracketContribution_kernel_factor` | [B02/Bilinearity.lean:11](B02/Bilinearity.lean#L11) | Headline/Hodge/parameter extension: concrete coefficient and bilinearity support | exact supporting identity |
| `B02.Concrete.weighted_sum_coefficients` | [B02/Bilinearity.lean:22](B02/Bilinearity.lean#L22) | Headline/Hodge/parameter extension: concrete coefficient and bilinearity support | exact supporting identity |
| `B02.Concrete.coefficient_bracket_finite` | [B02/Bilinearity.lean:36](B02/Bilinearity.lean#L36) | Headline/Hodge/parameter extension: concrete coefficient and bilinearity support | exact supporting identity |
| `B02.Concrete.coefficient_bracket_congr` | [B02/Bilinearity.lean:59](B02/Bilinearity.lean#L59) | Headline/Hodge/parameter extension: concrete coefficient and bilinearity support | exact supporting identity |
| `B02.Concrete.coefficient_bracket_scale_right` | [B02/Bilinearity.lean:66](B02/Bilinearity.lean#L66) | Headline/Hodge/parameter extension: concrete coefficient and bilinearity support | exact supporting identity |
| `B02.Concrete.coefficient_bracket_scale_left` | [B02/Bilinearity.lean:81](B02/Bilinearity.lean#L81) | Headline/Hodge/parameter extension: concrete coefficient and bilinearity support | exact supporting identity |
| `B02.Concrete.witness_pair_symmetric` | [B02/Concrete.lean:140](B02/Concrete.lean#L140) | Headline negative-scope counterexample: executable witness and symmetries | exact |
| `B02.Concrete.witness_first_antisymmetric` | [B02/Concrete.lean:149](B02/Concrete.lean#L149) | Headline negative-scope counterexample: executable witness and symmetries | exact |
| `B02.Concrete.witness_second_antisymmetric` | [B02/Concrete.lean:153](B02/Concrete.lean#L153) | Headline negative-scope counterexample: executable witness and symmetries | exact |
| `B02.Concrete.witness_bianchi` | [B02/Concrete.lean:157](B02/Concrete.lean#L157) | Headline negative-scope counterexample: executable witness and symmetries | exact |
| `B02.Concrete.pinned_witness_inner_B` | [B02/Concrete.lean:161](B02/Concrete.lean#L161) | Headline negative-scope counterexample: executable witness and symmetries | exact |
| `B02.Concrete.dropped_witness_inner_B` | [B02/Concrete.lean:165](B02/Concrete.lean#L165) | Headline negative-scope counterexample: executable witness and symmetries | exact |
| `B02.Concrete.dropped_witness_inner_BPrime` | [B02/Concrete.lean:170](B02/Concrete.lean#L170) | Headline negative-scope counterexample: executable witness and symmetries | exact |
| `B02.Concrete.linearEval_nil` | [B02/ConcreteHeadline.lean:11](B02/ConcreteHeadline.lean#L11) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.linearEval_cons` | [B02/ConcreteHeadline.lean:14](B02/ConcreteHeadline.lean#L14) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.linearEval_addTerm` | [B02/ConcreteHeadline.lean:18](B02/ConcreteHeadline.lean#L18) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.linearEval_fold (private helper)` | [B02/ConcreteHeadline.lean:36](B02/ConcreteHeadline.lean#L36) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.linearEval_clean` | [B02/ConcreteHeadline.lean:43](B02/ConcreteHeadline.lean#L43) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.linearEval_star` | [B02/ConcreteHeadline.lean:47](B02/ConcreteHeadline.lean#L47) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.bracketContribution_factor` | [B02/ConcreteHeadline.lean:71](B02/ConcreteHeadline.lean#L71) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.coefficient_bracket_linear` | [B02/ConcreteHeadline.lean:77](B02/ConcreteHeadline.lean#L77) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.mem_pairs` | [B02/ConcreteHeadline.lean:85](B02/ConcreteHeadline.lean#L85) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.nodup_pairs` | [B02/ConcreteHeadline.lean:99](B02/ConcreteHeadline.lean#L99) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.pairSet_injective` | [B02/ConcreteHeadline.lean:119](B02/ConcreteHeadline.lean#L119) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.sum_map_flatMap (private helper)` | [B02/ConcreteHeadline.lean:138](B02/ConcreteHeadline.lean#L138) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.rational_eq_algebraMap` | [B02/ConcreteHeadline.lean:145](B02/ConcreteHeadline.lean#L145) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.integer_eq_cast` | [B02/ConcreteHeadline.lean:146](B02/ConcreteHeadline.lean#L146) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.commKernel_antisymm` | [B02/ConcreteHeadline.lean:154](B02/ConcreteHeadline.lean#L154) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.pair_disjoint_compl_iff` | [B02/ConcreteHeadline.lean:162](B02/ConcreteHeadline.lean#L162) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.diagonal_star_kernel` | [B02/ConcreteHeadline.lean:178](B02/ConcreteHeadline.lean#L178) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.coefficient_inner_B_expanded` | [B02/ConcreteHeadline.lean:216](B02/ConcreteHeadline.lean#L216) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.coefficient_inner_B_contracted` | [B02/ConcreteHeadline.lean:234](B02/ConcreteHeadline.lean#L234) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.antisymmetric_sum_zero (private helper)` | [B02/ConcreteHeadline.lean:261](B02/ConcreteHeadline.lean#L261) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.headline_inner_B_concrete` | [B02/ConcreteHeadline.lean:285](B02/ConcreteHeadline.lean#L285) | Literal CCC: concrete B cancellation and its finite-sum support | stronger: all n, arbitrary integer eta, pair symmetry only |
| `B02.Concrete.integer_negation` | [B02/ConcreteHodge.lean:25](B02/ConcreteHodge.lean#L25) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.coefficient_otherStar` | [B02/ConcreteHodge.lean:29](B02/ConcreteHodge.lean#L29) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.homogeneous_coefficient_zero` | [B02/ConcreteHodge.lean:51](B02/ConcreteHodge.lean#L51) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.otherStar_two` | [B02/ConcreteHodge.lean:64](B02/ConcreteHodge.lean#L64) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.otherStar_top` | [B02/ConcreteHodge.lean:73](B02/ConcreteHodge.lean#L73) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.coefficient_otherStar_one` | [B02/ConcreteHodge.lean:82](B02/ConcreteHodge.lean#L82) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.homogeneous_otherStar` | [B02/ConcreteHodge.lean:94](B02/ConcreteHodge.lean#L94) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.coefficient_star_scaled` | [B02/ConcreteHodge.lean:102](B02/ConcreteHodge.lean#L102) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.coefficient_otherStar_output` | [B02/ConcreteHodge.lean:109](B02/ConcreteHodge.lean#L109) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.otherShiab_coefficient` | [B02/ConcreteHodge.lean:121](B02/ConcreteHodge.lean#L121) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.otherShiab_degree` | [B02/ConcreteHodge.lean:145](B02/ConcreteHodge.lean#L145) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.coefficient_bracket_scaled_right` | [B02/ConcreteHodge.lean:166](B02/ConcreteHodge.lean#L166) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.otherShiab_reparametrization` | [B02/ConcreteHodge.lean:182](B02/ConcreteHodge.lean#L182) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.otherShiab_readout_reparametrization` | [B02/ConcreteHodge.lean:204](B02/ConcreteHodge.lean#L204) | Hodge convention reparametrization and readout sign | exact: concrete rational model; final identities even n>=2 |
| `B02.Concrete.denote_plus` | [B02/ConcreteLinear.lean:47](B02/ConcreteLinear.lean#L47) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.Concrete.denote_scale` | [B02/ConcreteLinear.lean:50](B02/ConcreteLinear.lean#L50) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.Concrete.denote_star` | [B02/ConcreteLinear.lean:57](B02/ConcreteLinear.lean#L57) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.Concrete.denote_bracket` | [B02/ConcreteLinear.lean:61](B02/ConcreteLinear.lean#L61) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.Concrete.denote_shiab` | [B02/ConcreteLinear.lean:66](B02/ConcreteLinear.lean#L66) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.Concrete.concrete_parameter_affine` | [B02/ConcreteLinear.lean:74](B02/ConcreteLinear.lean#L74) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.Concrete.concrete_six_probe_formula` | [B02/ConcreteLinear.lean:89](B02/ConcreteLinear.lean#L89) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.Concrete.concrete_input_linear` | [B02/ConcreteLinear.lean:106](B02/ConcreteLinear.lean#L106) | Parameter extension and curvature-input linearity | exact rational executable structure; weaker than real closed-form classification |
| `B02.inversion_transpose (private helper)` | [B02/ConcreteTwistedHeadline.lean:7](B02/ConcreteTwistedHeadline.lean#L7) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.reorderSign_compl_left` | [B02/ConcreteTwistedHeadline.lean:14](B02/ConcreteTwistedHeadline.lean#L14) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.reorderSign_compl_right` | [B02/ConcreteTwistedHeadline.lean:24](B02/ConcreteTwistedHeadline.lean#L24) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.metric_union_compl_inter` | [B02/ConcreteTwistedHeadline.lean:35](B02/ConcreteTwistedHeadline.lean#L35) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.twisted_coefficient_normal_form` | [B02/ConcreteTwistedHeadline.lean:54](B02/ConcreteTwistedHeadline.lean#L54) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.twisted_coefficient_antisymm` | [B02/ConcreteTwistedHeadline.lean:68](B02/ConcreteTwistedHeadline.lean#L68) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.twisted_output_symm` | [B02/ConcreteTwistedHeadline.lean:77](B02/ConcreteTwistedHeadline.lean#L77) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.twistedCommKernel_antisymm` | [B02/ConcreteTwistedHeadline.lean:86](B02/ConcreteTwistedHeadline.lean#L86) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.bladeMul_volume_exact` | [B02/ConcreteTwistedHeadline.lean:97](B02/ConcreteTwistedHeadline.lean#L97) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.linearEval_rightMulVolume` | [B02/ConcreteTwistedHeadline.lean:104](B02/ConcreteTwistedHeadline.lean#L104) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.diagonal_star_kernel_general` | [B02/ConcreteTwistedHeadline.lean:117](B02/ConcreteTwistedHeadline.lean#L117) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.twisted_sum_map_flatMap (private helper)` | [B02/ConcreteTwistedHeadline.lean:142](B02/ConcreteTwistedHeadline.lean#L142) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.coefficient_inner_BPrime_expanded` | [B02/ConcreteTwistedHeadline.lean:150](B02/ConcreteTwistedHeadline.lean#L150) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.coefficient_inner_BPrime_contracted` | [B02/ConcreteTwistedHeadline.lean:172](B02/ConcreteTwistedHeadline.lean#L172) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.twisted_antisymmetric_sum_zero (private helper)` | [B02/ConcreteTwistedHeadline.lean:201](B02/ConcreteTwistedHeadline.lean#L201) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.headline_inner_BPrime_concrete` | [B02/ConcreteTwistedHeadline.lean:227](B02/ConcreteTwistedHeadline.lean#L227) | Literal CCC: concrete B-prime cancellation and its sign/sum support | stronger: all n, arbitrary integer eta and phase |
| `B02.Concrete.addTerm_form_property` | [B02/Degree.lean:9](B02/Degree.lean#L9) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.Concrete.fold_addTerm_form_property` | [B02/Degree.lean:19](B02/Degree.lean#L19) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.Concrete.clean_form_property` | [B02/Degree.lean:29](B02/Degree.lean#L29) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.Concrete.homogeneous_plus` | [B02/Degree.lean:33](B02/Degree.lean#L33) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.Concrete.homogeneous_scale` | [B02/Degree.lean:37](B02/Degree.lean#L37) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.Concrete.homogeneous_star` | [B02/Degree.lean:44](B02/Degree.lean#L44) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.Concrete.homogeneous_bracket` | [B02/Degree.lean:51](B02/Degree.lean#L51) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.Concrete.shiab_degree` | [B02/Degree.lean:67](B02/Degree.lean#L67) | Test 1: form-degree preservation and homogeneous-operation support | exact; final response assumes n>=2 |
| `B02.DimensionTwo.sectional_component` | [B02/DimensionTwo.lean:47](B02/DimensionTwo.lean#L47) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.curvature_is_algebraic` | [B02/DimensionTwo.lean:50](B02/DimensionTwo.lean#L50) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.ricci_is_metric` | [B02/DimensionTwo.lean:57](B02/DimensionTwo.lean#L57) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.scalar_is_two` | [B02/DimensionTwo.lean:60](B02/DimensionTwo.lean#L60) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.embedded_metric` | [B02/DimensionTwo.lean:63](B02/DimensionTwo.lean#L63) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.description_kappa_zero` | [B02/DimensionTwo.lean:66](B02/DimensionTwo.lean#L66) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.description_kappa_one` | [B02/DimensionTwo.lean:71](B02/DimensionTwo.lean#L71) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.response_nonzero` | [B02/DimensionTwo.lean:76](B02/DimensionTwo.lean#L76) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.DimensionTwo.nonunique_parameter_descriptions` | [B02/DimensionTwo.lean:82](B02/DimensionTwo.lean#L82) | Literal CCC kappa scope: concrete dimension-two counterexample and contractions | exact witness; not a universal 2D classification |
| `B02.rank_sandwich` | [B02/Extension.lean:8](B02/Extension.lean#L8) | Extension to all algebraic curvature | weaker: generic supplied space/set, rank/dimension/basis checks explicit; actual chart uninstantiated |
| `B02.span_eq_top_of_rank_certificate` | [B02/Extension.lean:18](B02/Extension.lean#L18) | Extension to all algebraic curvature | weaker: generic supplied space/set, rank/dimension/basis checks explicit; actual chart uninstantiated |
| `B02.curvature_extension` | [B02/Extension.lean:30](B02/Extension.lean#L30) | Extension to all algebraic curvature | weaker: generic supplied space/set, rank/dimension/basis checks explicit; actual chart uninstantiated |
| `B02.curvature_dimension_numerals` | [B02/Extension.lean:43](B02/Extension.lean#L43) | Curvature dimensions 20 and 3185 | weaker: arithmetic only, no dimension theorem |
| `B02.rational_span_extends_to_real` | [B02/Extension.lean:50](B02/Extension.lean#L50) | Rational spanning implies real spanning | exact tensor base-change argument; concrete curvature identification remains |
| `B02.real_scalar_extension_identity` | [B02/Extension.lean:59](B02/Extension.lean#L59) | Extension to all algebraic curvature | weaker: generic supplied space/set, rank/dimension/basis checks explicit; actual chart uninstantiated |
| `B02.wedgeStarWeight_diagonal` | [B02/Headline.lean:13](B02/Headline.lean#L13) | Literal CCC: symmetric coefficients cancel antisymmetric commutators | exact algebraic subargument; concrete instantiation proved separately |
| `B02.symmetric_commutator_sum` | [B02/Headline.lean:32](B02/Headline.lean#L32) | Literal CCC: symmetric coefficients cancel antisymmetric commutators | exact algebraic subargument; concrete instantiation proved separately |
| `B02.headline_inner_C` | [B02/Headline.lean:61](B02/Headline.lean#L61) | Literal CCC: symmetric coefficients cancel antisymmetric commutators | exact algebraic subargument; concrete instantiation proved separately |
| `B02.central_twisted_commutator` | [B02/Headline.lean:91](B02/Headline.lean#L91) | Literal CCC: symmetric coefficients cancel antisymmetric commutators | exact algebraic subargument; concrete instantiation proved separately |
| `B02.even_dimension_star_parity` | [B02/Hodge.lean:7](B02/Hodge.lean#L7) | Hodge convention: per-degree parity factors | exact supporting identity |
| `B02.oppositeStarSign_degree` | [B02/Hodge.lean:15](B02/Hodge.lean#L15) | Hodge convention: per-degree parity factors | exact supporting identity |
| `B02.oppositeStarSign_two` | [B02/Hodge.lean:22](B02/Hodge.lean#L22) | Hodge convention: per-degree parity factors | exact supporting identity |
| `B02.oppositeStarSign_top` | [B02/Hodge.lean:27](B02/Hodge.lean#L27) | Hodge convention: per-degree parity factors | exact supporting identity |
| `B02.oppositeStarSign_one` | [B02/Hodge.lean:31](B02/Hodge.lean#L31) | Hodge convention: per-degree parity factors | exact supporting identity |
| `B02.oppositeStarSign_output` | [B02/Hodge.lean:37](B02/Hodge.lean#L37) | Hodge convention: per-degree parity factors | exact supporting identity |
| `B02.Samples.split_CCC` | [B02/Samples.lean:34](B02/Samples.lean#L34) | Signature parity samples / dimension-two scope | weaker: fixed constant-curvature samples only; native_decide |
| `B02.Samples.split_CAA` | [B02/Samples.lean:39](B02/Samples.lean#L39) | Signature parity samples / dimension-two scope | weaker: fixed constant-curvature samples only; native_decide |
| `B02.Samples.euclidean_CCC` | [B02/Samples.lean:44](B02/Samples.lean#L44) | Signature parity samples / dimension-two scope | weaker: fixed constant-curvature samples only; native_decide |
| `B02.Samples.euclidean_CAA` | [B02/Samples.lean:48](B02/Samples.lean#L48) | Signature parity samples / dimension-two scope | weaker: fixed constant-curvature samples only; native_decide |
| `B02.Samples.dimension_two_CCC` | [B02/Samples.lean:54](B02/Samples.lean#L54) | Signature parity samples / dimension-two scope | weaker: fixed constant-curvature samples only; native_decide |
| `B02.Concrete.coefficient_nil` | [B02/Semantics.lean:6](B02/Semantics.lean#L6) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_cons` | [B02/Semantics.lean:9](B02/Semantics.lean#L9) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_addTerm` | [B02/Semantics.lean:15](B02/Semantics.lean#L15) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_fold (private helper)` | [B02/Semantics.lean:42](B02/Semantics.lean#L42) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_clean` | [B02/Semantics.lean:52](B02/Semantics.lean#L52) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_plus` | [B02/Semantics.lean:56](B02/Semantics.lean#L56) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_scale` | [B02/Semantics.lean:60](B02/Semantics.lean#L60) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_star` | [B02/Semantics.lean:71](B02/Semantics.lean#L71) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_bracket_raw` | [B02/Semantics.lean:93](B02/Semantics.lean#L93) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_append` | [B02/Semantics.lean:106](B02/Semantics.lean#L106) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.Concrete.coefficient_bracket` | [B02/Semantics.lean:124](B02/Semantics.lean#L124) | Reference conventions supporting headline/Hodge/extension | exact coefficient semantics for concrete sparse operations |
| `B02.reorderSign_sq` | [B02/Signs.lean:21](B02/Signs.lean#L21) | Literal CCC: pinned Hodge weight; opening parity / kappa findings | exact supporting identity or counterexample |
| `B02.pinned_hodge_weight` | [B02/Signs.lean:28](B02/Signs.lean#L28) | Literal CCC: pinned wedge-star weight | stronger: all blades, all n, arbitrary integer eta |
| `B02.pinned_pair_weight` | [B02/Signs.lean:34](B02/Signs.lean#L34) | Literal CCC: w_ab=+eta_a eta_b | stronger: all n and arbitrary integer eta |
| `B02.wedge_total_degree_counterexample` | [B02/Signs.lean:41](B02/Signs.lean#L41) | Opening even-total-degree sentence (F1) | exact counterexample at n=4 |
| `B02.bracket_degree_products_even` | [B02/Signs.lean:44](B02/Signs.lean#L44) | Opening graded-sign rationale (F1 correction) | exact corrected operand-degree-product statement, even n>=2 |
| `B02.dimension_two_kappa_nonunique` | [B02/Signs.lean:55](B02/Signs.lean#L55) | Headline kappa scope (F2 precursor) | weaker: scalar arithmetic only; actual model theorem is in DimensionTwo |
| `B02.commutation_lie_closed` | [B02/Spin.lean:7](B02/Spin.lean#L7) | Test 4(iii): Lie closure and exponentiation | exact individual step; weaker than Spin0 equivariance until representation is instantiated |
| `B02.commutation_exponential` | [B02/Spin.lean:16](B02/Spin.lean#L16) | Test 4(iii): Lie closure and exponentiation | exact individual step; weaker than Spin0 equivariance until representation is instantiated |
| `B02.invariant_lie_closed` | [B02/Spin.lean:22](B02/Spin.lean#L22) | Test 4(iii): Lie closure and exponentiation | exact individual step; weaker than Spin0 equivariance until representation is instantiated |
| `B02.Structural.OperatorData.response_apply` | [B02/Structural.lean:22](B02/Structural.lean#L22) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_input_add` | [B02/Structural.lean:26](B02/Structural.lean#L26) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_input_smul` | [B02/Structural.lean:29](B02/Structural.lean#L29) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_first_add` | [B02/Structural.lean:32](B02/Structural.lean#L32) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_first_smul` | [B02/Structural.lean:36](B02/Structural.lean#L36) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_second_affine` | [B02/Structural.lean:41](B02/Structural.lean#L41) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_parameter_extension` | [B02/Structural.lean:49](B02/Structural.lean#L49) | Parameter extension from six checks | exact any-field interpolation argument for supplied linear/bilinear data; closed-form checks are inputs |
| `B02.Structural.OperatorData.hodge_reparametrization` | [B02/Structural.lean:63](B02/Structural.lean#L63) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_mem` | [B02/Structural.lean:71](B02/Structural.lean#L71) | Test 2(a): response closure | weaker: supplied real submodule and operation closure, no concrete adjoint/Phi instantiation |
| `B02.Structural.OperatorData.response_covariant` | [B02/Structural.lean:85](B02/Structural.lean#L85) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.OperatorData.response_derivation` | [B02/Structural.lean:95](B02/Structural.lean#L95) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.linear_eq_of_spanning` | [B02/Structural.lean:111](B02/Structural.lean#L111) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.commutator_skew` | [B02/Structural.lean:127](B02/Structural.lean#L127) | Test 2(a): skew-adjoint commutator closure | exact under stated StarRing laws |
| `B02.Structural.imaginary_anticommutator_skew` | [B02/Structural.lean:134](B02/Structural.lean#L134) | Test 2(a): skew-adjoint i-anticommutator closure | exact under stated StarRing and imaginary-centrality laws |
| `B02.Structural.inner_derivation_product` | [B02/Structural.lean:147](B02/Structural.lean#L147) | Test 4(iii) step 1: ad product rule | exact associative-ring identity |
| `B02.Structural.unitConjugate_mul` | [B02/Structural.lean:160](B02/Structural.lean#L160) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.unitConjugate_add` | [B02/Structural.lean:164](B02/Structural.lean#L164) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.unitConjugate_sub` | [B02/Structural.lean:168](B02/Structural.lean#L168) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.unitConjugate_composition` | [B02/Structural.lean:173](B02/Structural.lean#L173) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.unitConjugate_commutator` | [B02/Structural.lean:177](B02/Structural.lean#L177) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.unitConjugate_central` | [B02/Structural.lean:183](B02/Structural.lean#L183) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.unitConjugate_imaginary_anticommutator` | [B02/Structural.lean:189](B02/Structural.lean#L189) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.AssociativeDerivation.commutator_rule` | [B02/Structural.lean:222](B02/Structural.lean#L222) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.AssociativeDerivation.imaginary_anticommutator_rule` | [B02/Structural.lean:229](B02/Structural.lean#L229) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.AssociativeDerivation.scalar_killed` | [B02/Structural.lean:238](B02/Structural.lean#L238) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.AssociativeDerivation.inner_kills_central` | [B02/Structural.lean:256](B02/Structural.lean#L256) | Shared operator composition/extension support | weaker: abstract operation data; concrete specialization stated separately |
| `B02.Structural.equivariant_of_exponential_generators` | [B02/Structural.lean:296](B02/Structural.lean#L296) | Test 4(iii): subgroup generation step | weaker: named generation and exponential-commutation hypotheses; no Spin0 model |
| `B02.Structural.tensorConjugate_tmul` | [B02/TensorCovariance.lean:22](B02/TensorCovariance.lean#L22) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorFormMap_tmul` | [B02/TensorCovariance.lean:26](B02/TensorCovariance.lean#L26) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorConjugate_formMap` | [B02/TensorCovariance.lean:31](B02/TensorCovariance.lean#L31) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorConjugate_composition` | [B02/TensorCovariance.lean:39](B02/TensorCovariance.lean#L39) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.componentC_covariance` | [B02/TensorCovariance.lean:46](B02/TensorCovariance.lean#L46) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.componentA_covariance` | [B02/TensorCovariance.lean:51](B02/TensorCovariance.lean#L51) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracketC_tmul` | [B02/TensorCovariance.lean:68](B02/TensorCovariance.lean#L68) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracketA_tmul` | [B02/TensorCovariance.lean:72](B02/TensorCovariance.lean#L72) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracketC_covariance` | [B02/TensorCovariance.lean:77](B02/TensorCovariance.lean#L77) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracketA_covariance` | [B02/TensorCovariance.lean:89](B02/TensorCovariance.lean#L89) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracket_covariance` | [B02/TensorCovariance.lean:107](B02/TensorCovariance.lean#L107) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracketC_derivation` | [B02/TensorCovariance.lean:117](B02/TensorCovariance.lean#L117) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracketA_derivation` | [B02/TensorCovariance.lean:140](B02/TensorCovariance.lean#L140) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorBracket_derivation` | [B02/TensorCovariance.lean:162](B02/TensorCovariance.lean#L162) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorDerivation_formMap` | [B02/TensorCovariance.lean:176](B02/TensorCovariance.lean#L176) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensor_response_covariance` | [B02/TensorCovariance.lean:205](B02/TensorCovariance.lean#L205) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensor_dressed_covariance` | [B02/TensorCovariance.lean:219](B02/TensorCovariance.lean#L219) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensor_response_derivation` | [B02/TensorCovariance.lean:234](B02/TensorCovariance.lean#L234) | Tests 3(a),4(iii): actual tensor covariance/derivation/composition | weaker: tensor algebra theorem; sparse-Clifford identification remains |
| `B02.Structural.tensorDerivationMap_tmul` | [B02/TensorDerivation.lean:16](B02/TensorDerivation.lean#L16) | Test 4(iii) step 1: tensor and componentwise bracket Leibniz rules | weaker: genuine tensor derivations; generator_action identification remains |
| `B02.Structural.tensorDerivation_product` | [B02/TensorDerivation.lean:24](B02/TensorDerivation.lean#L24) | Test 4(iii) step 1: tensor and componentwise bracket Leibniz rules | weaker: genuine tensor derivations; generator_action identification remains |
| `B02.Structural.componentC_derivation` | [B02/TensorDerivation.lean:63](B02/TensorDerivation.lean#L63) | Test 4(iii) step 1: tensor and componentwise bracket Leibniz rules | weaker: genuine tensor derivations; generator_action identification remains |
| `B02.Structural.componentA_derivation` | [B02/TensorDerivation.lean:77](B02/TensorDerivation.lean#L77) | Test 4(iii) step 1: tensor and componentwise bracket Leibniz rules | weaker: genuine tensor derivations; generator_action identification remains |
| `B02.expandedTwistedInnerC_eq` | [B02/TwistedHeadline.lean:27](B02/TwistedHeadline.lean#L27) | Literal CCC: abstract B-prime commutator factoring | exact algebraic subargument; concrete B-prime proved separately |
| `B02.headline_inner_C_twisted` | [B02/TwistedHeadline.lean:38](B02/TwistedHeadline.lean#L38) | Literal CCC: abstract B-prime commutator factoring | exact algebraic subargument; concrete B-prime proved separately |
| `B02.volume_count (private helper)` | [B02/Volume.lean:8](B02/Volume.lean#L8) | Literal CCC: volume commutes with even blades | stronger: all n and arbitrary integer eta |
| `B02.inversion_volume_sum (private helper)` | [B02/Volume.lean:23](B02/Volume.lean#L23) | Literal CCC: volume commutes with even blades | stronger: all n and arbitrary integer eta |
| `B02.reorderSign_volume_even` | [B02/Volume.lean:35](B02/Volume.lean#L35) | Literal CCC: volume commutes with even blades | stronger: all n and arbitrary integer eta |
| `B02.reorderSign_volume_pair` | [B02/Volume.lean:46](B02/Volume.lean#L46) | Literal CCC: volume commutes with even blades | stronger: all n and arbitrary integer eta |
| `B02.Concrete.bladeMul_volume_even` | [B02/Volume.lean:53](B02/Volume.lean#L53) | Literal CCC: volume commutes with even blades | stronger: all n and arbitrary integer eta |
| `B02.Concrete.bladeMul_volume_pair` | [B02/Volume.lean:59](B02/Volume.lean#L59) | Literal CCC: volume commutes with even blades | stronger: all n and arbitrary integer eta |
| `B02.Concrete.bladeMul_volume_bivector` | [B02/Volume.lean:64](B02/Volume.lean#L64) | Literal CCC: volume commutes with even blades | stronger: all n and arbitrary integer eta |

## B03 theorem-to-claim inventory

81 new public theorems. Each is kernel-checked; none uses native_decide. The combined inventory now contains 269 declarations, 260 public.

| Lean theorem | Source | README/result claim or supporting argument | Fidelity |
|---|---|---|---|
| `B03.selection77` | [B03/Certificates.lean:7](B03/Certificates.lean#L7) | J definition: product of all purely imaginary gammas | exact selector/column-parity justification |
| `B03.selection95` | [B03/Certificates.lean:8](B03/Certificates.lean#L8) | J definition: product of all purely imaginary gammas | exact selector/column-parity justification |
| `B03.first_chirality77` | [B03/Certificates.lean:9](B03/Certificates.lean#L9) | Library C: first square-one and Hermitian phase | exact fixed-signature certificate |
| `B03.first_chirality95` | [B03/Certificates.lean:10](B03/Certificates.lean#L10) | Library C: first square-one and Hermitian phase | exact fixed-signature certificate |
| `B03.j_square77` | [B03/Certificates.lean:11](B03/Certificates.lean#L11) | README Reality / result.json J_square | exact fixed-signature identity |
| `B03.j_square95` | [B03/Certificates.lean:13](B03/Certificates.lean#L13) | README Reality / result.json J_square | exact fixed-signature identity; shared by both (9,5) splits |
| `B03.chirality_parity77` | [B03/Certificates.lean:15](B03/Certificates.lean#L15) | README Reality / result.json chirality_vs_parity | exact full monomial equality for the specified split |
| `B03.chirality_parity95a` | [B03/Certificates.lean:17](B03/Certificates.lean#L17) | README Reality / result.json chirality_vs_parity | exact full monomial equality for the specified split |
| `B03.chirality_parity95b` | [B03/Certificates.lean:19](B03/Certificates.lean#L19) | README Reality / result.json chirality_vs_parity | exact full monomial equality for the specified split |
| `B03.clifford31` | [B03/Certificates.lean:28](B03/Certificates.lean#L28) | Clifford relations {Gamma_a,Gamma_b}=2 eta_ab | exact; generic lifting theorem instantiated by the three certificates |
| `B03.clifford77` | [B03/Certificates.lean:29](B03/Certificates.lean#L29) | Clifford relations {Gamma_a,Gamma_b}=2 eta_ab | exact; generic lifting theorem instantiated by the three certificates |
| `B03.clifford95` | [B03/Certificates.lean:30](B03/Certificates.lean#L30) | Clifford relations {Gamma_a,Gamma_b}=2 eta_ab | exact; generic lifting theorem instantiated by the three certificates |
| `B03.j_gamma31` | [B03/Certificates.lean:36](B03/Certificates.lean#L36) | J commutes with spin generators: common gamma intertwining sign | exact supporting fixed-signature identity |
| `B03.j_gamma77` | [B03/Certificates.lean:37](B03/Certificates.lean#L37) | J commutes with spin generators: common gamma intertwining sign | exact supporting fixed-signature identity |
| `B03.j_gamma95` | [B03/Certificates.lean:38](B03/Certificates.lean#L38) | J commutes with spin generators: common gamma intertwining sign | exact supporting fixed-signature identity |
| `B03.j_chirality31` | [B03/Certificates.lean:39](B03/Certificates.lean#L39) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.j_chirality77` | [B03/Certificates.lean:41](B03/Certificates.lean#L41) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.j_chirality95` | [B03/Certificates.lean:43](B03/Certificates.lean#L43) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.Mono.extensional` | [B03/Model.lean:17](B03/Model.lean#L17) | All matrix claims: column equality determines monomial equality | exact supporting identity |
| `B03.selection31` | [B03/Model.lean:77](B03/Model.lean#L77) | J definition: product of all purely imaginary gammas | exact selector/column-parity justification |
| `B03.first_chirality31` | [B03/Model.lean:78](B03/Model.lean#L78) | Library C: first square-one and Hermitian phase | exact fixed-signature certificate |
| `B03.j_square31` | [B03/Model.lean:79](B03/Model.lean#L79) | README Reality / result.json J_square | exact fixed-signature identity |
| `B03.chirality_parity31` | [B03/Model.lean:80](B03/Model.lean#L80) | README Reality / result.json chirality_vs_parity | exact full monomial equality for the specified split |
| `B03.bivector_intertwining` | [B03/Operators.lean:7](B03/Operators.lean#L7) | J commutes with spin generators: extend common sign to every pair | stronger: general monomial algebra; certificate hypotheses supplied for all requested signatures |
| `B03.all_bivectors` | [B03/Operators.lean:18](B03/Operators.lean#L18) | J commutes with spin generators: extend common sign to every pair | stronger: general monomial algebra; certificate hypotheses supplied for all requested signatures |
| `B03.imaginary_selector_iff` | [B03/Operators.lean:24](B03/Operators.lean#L24) | J definition: product of all purely imaginary gammas | exact selector/column-parity justification |
| `B03.real_structure_square77` | [B03/Operators.lean:37](B03/Operators.lean#L37) | README Reality / result.json J_square | exact fixed-signature identity |
| `B03.real_structure_square95` | [B03/Operators.lean:39](B03/Operators.lean#L39) | README Reality / result.json J_square | exact fixed-signature identity; shared by both (9,5) splits |
| `B03.real_structure_square31` | [B03/Operators.lean:41](B03/Operators.lean#L41) | README Reality / result.json J_square | exact fixed-signature identity |
| `B03.J_all_generators77` | [B03/Operators.lean:44](B03/Operators.lean#L44) | J commutes with spin generators | stronger than adjacent-only check: all axis pairs, all complex spinors |
| `B03.J_all_generators95` | [B03/Operators.lean:48](B03/Operators.lean#L48) | J commutes with spin generators | stronger than adjacent-only check: all axis pairs, all complex spinors |
| `B03.J_all_generators31` | [B03/Operators.lean:52](B03/Operators.lean#L52) | J commutes with spin generators | stronger than adjacent-only check: all axis pairs, all complex spinors |
| `B03.J_chirality77` | [B03/Operators.lean:56](B03/Operators.lean#L56) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.J_chirality95` | [B03/Operators.lean:59](B03/Operators.lean#L59) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.J_chirality31` | [B03/Operators.lean:62](B03/Operators.lean#L62) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.clifford_operators` | [B03/Operators.lean:68](B03/Operators.lean#L68) | Clifford relations {Gamma_a,Gamma_b}=2 eta_ab | exact; generic lifting theorem instantiated by the three certificates |
| `B03.clifford_relations77` | [B03/Operators.lean:89](B03/Operators.lean#L89) | Clifford relations {Gamma_a,Gamma_b}=2 eta_ab | exact; generic lifting theorem instantiated by the three certificates |
| `B03.clifford_relations95` | [B03/Operators.lean:93](B03/Operators.lean#L93) | Clifford relations {Gamma_a,Gamma_b}=2 eta_ab | exact; generic lifting theorem instantiated by the three certificates |
| `B03.clifford_relations31` | [B03/Operators.lean:97](B03/Operators.lean#L97) | Clifford relations {Gamma_a,Gamma_b}=2 eta_ab | exact; generic lifting theorem instantiated by the three certificates |
| `B03.chirality_preserves77` | [B03/Operators.lean:102](B03/Operators.lean#L102) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.chirality_preserves95` | [B03/Operators.lean:106](B03/Operators.lean#L106) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.chirality_exchanges31` | [B03/Operators.lean:110](B03/Operators.lean#L110) | README Reality / result.json J_preserves_chirality | exact operator/eigenspace statement for the specified signature |
| `B03.cartan_commutes` | [B03/Operators.lean:118](B03/Operators.lean#L118) | Adapter: diagonal sign-valued, pairwise commuting Cartans | exact; generic consequences instantiated by cartan2 and cartan7 |
| `B03.cartan_eigenvalues` | [B03/Operators.lean:121](B03/Operators.lean#L121) | Adapter: diagonal sign-valued, pairwise commuting Cartans | exact; generic consequences instantiated by cartan2 and cartan7 |
| `B03.every_weight31` | [B03/Operators.lean:128](B03/Operators.lean#L128) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.every_weight77` | [B03/Operators.lean:130](B03/Operators.lean#L130) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.every_weight95a` | [B03/Operators.lean:132](B03/Operators.lean#L132) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.every_weight95b` | [B03/Operators.lean:134](B03/Operators.lean#L134) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.Mono.mul_assoc` | [B03/Semantics.lean:10](B03/Semantics.lean#L10) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.Mono.conj_mul` | [B03/Semantics.lean:14](B03/Semantics.lean#L14) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.Mono.shift_mul` | [B03/Semantics.lean:18](B03/Semantics.lean#L18) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.Mono.mul_shift` | [B03/Semantics.lean:22](B03/Semantics.lean#L22) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.Mono.shift_shift` | [B03/Semantics.lean:26](B03/Semantics.lean#L26) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.Mono.shift_zero` | [B03/Semantics.lean:30](B03/Semantics.lean#L30) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.Mono.diagonal_commute` | [B03/Semantics.lean:32](B03/Semantics.lean#L32) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.phaseValue_add` | [B03/Semantics.lean:40](B03/Semantics.lean#L40) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.phaseValue_neg` | [B03/Semantics.lean:42](B03/Semantics.lean#L42) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.act_single` | [B03/Semantics.lean:47](B03/Semantics.lean#L47) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.act_mul` | [B03/Semantics.lean:51](B03/Semantics.lean#L51) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.act_one` | [B03/Semantics.lean:56](B03/Semantics.lean#L56) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.act_shift` | [B03/Semantics.lean:60](B03/Semantics.lean#L60) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.act_shift_two` | [B03/Semantics.lean:67](B03/Semantics.lean#L67) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.conjugation_single` | [B03/Semantics.lean:74](B03/Semantics.lean#L74) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.conjugation_involutive` | [B03/Semantics.lean:77](B03/Semantics.lean#L77) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.conjugation_act` | [B03/Semantics.lean:79](B03/Semantics.lean#L79) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.J_antilinear` | [B03/Semantics.lean:88](B03/Semantics.lean#L88) | J=B composed with complex conjugation is antilinear | stronger: every monomial B and dimension |
| `B03.J_squared` | [B03/Semantics.lean:90](B03/Semantics.lean#L90) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.J_intertwines` | [B03/Semantics.lean:92](B03/Semantics.lean#L92) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.act_column_entry` | [B03/Semantics.lean:99](B03/Semantics.lean#L99) | J/Clifford/chirality claims: monomial and complex-operator semantic support | exact supporting identity for arbitrary monomials/dimension |
| `B03.hermitian_entries` | [B03/Semantics.lean:102](B03/Semantics.lean#L102) | Library C: Hermitian acceptance predicate | exact interpretation as conjugate-transposed complex entries |
| `B03.cartan2` | [B03/Weights.lean:9](B03/Weights.lean#L9) | Adapter: diagonal sign-valued, pairwise commuting Cartans | exact; generic consequences instantiated by cartan2 and cartan7 |
| `B03.cartan7` | [B03/Weights.lean:10](B03/Weights.lean#L10) | Adapter: diagonal sign-valued, pairwise commuting Cartans | exact; generic consequences instantiated by cartan2 and cartan7 |
| `B03.weight_inverse31` | [B03/Weights.lean:19](B03/Weights.lean#L19) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.weight_inverse77` | [B03/Weights.lean:20](B03/Weights.lean#L20) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.weight_inverse95a` | [B03/Weights.lean:21](B03/Weights.lean#L21) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.weight_inverse95b` | [B03/Weights.lean:22](B03/Weights.lean#L22) | Adapter: every sign pattern occurs exactly once | exact fixed split; inverse certificates or their unique-existence consequences |
| `B03.weight_exactly_once` | [B03/Weights.lean:24](B03/Weights.lean#L24) | Adapter: inverse weight encoding gives multiplicity one | stronger: generic inverse-to-unique-existence implication |
| `B03.j_weight31` | [B03/Weights.lean:34](B03/Weights.lean#L34) | README Reality / result.json J_weight_signs | exact fixed split, every column and coordinate |
| `B03.j_weight77` | [B03/Weights.lean:35](B03/Weights.lean#L35) | README Reality / result.json J_weight_signs | exact fixed split, every column and coordinate |
| `B03.j_weight95a` | [B03/Weights.lean:37](B03/Weights.lean#L37) | README Reality / result.json J_weight_signs | exact fixed split, every column and coordinate |
| `B03.j_weight95b` | [B03/Weights.lean:39](B03/Weights.lean#L39) | README Reality / result.json J_weight_signs | exact fixed split, every column and coordinate |

## B05 sign check: full theorem inventory

All fidelity labels are relative to the explicit directional-algebra model in
`COVERAGE.md`. "Exact" does not assert a global smooth-bundle realization.

| Theorem | Source | Claim / source equation | Fidelity |
|---|---|---|---|
| `B05Sign.Diff.one` | [B05Sign/Algebra.lean:23](B05Sign/Algebra.lean#L23) | Leibniz prerequisite for (6.5), (7.4) | stronger: every unital ring endoderivation kills 1 |
| `B05Sign.Diff.zero` | [B05Sign/Algebra.lean:28](B05Sign/Algebra.lean#L28) | Additivity prerequisite for (6.2) | exact: zero rule of the declared model |
| `B05Sign.Diff.inverse` | [B05Sign/Algebra.lean:30](B05Sign/Algebra.lean#L30) | Inverse differentiation used by (6.5)/(6.14) | stronger: derived from Leibniz in any noncommutative ring |
| `B05Sign.conj_one` | [B05Sign/Algebra.lean:41](B05Sign/Algebra.lean#L41) | (5.9), identity conjugation | exact supporting identity in the directional model |
| `B05Sign.conj_zero` | [B05Sign/Algebra.lean:42](B05Sign/Algebra.lean#L42) | (5.9), zero conjugation | exact supporting identity in the directional model |
| `B05Sign.conj_add` | [B05Sign/Algebra.lean:43](B05Sign/Algebra.lean#L43) | (5.9), additive conjugation | exact supporting identity in the directional model |
| `B05Sign.conj_neg` | [B05Sign/Algebra.lean:45](B05Sign/Algebra.lean#L45) | (5.9)/(6.5), negative conjugation | exact supporting identity in the directional model |
| `B05Sign.conj_sub` | [B05Sign/Algebra.lean:46](B05Sign/Algebra.lean#L46) | (7.4), difference conjugation | exact supporting identity in the directional model |
| `B05Sign.conj_comp` | [B05Sign/Algebra.lean:49](B05Sign/Algebra.lean#L49) | (5.9), right order of conjugation composition | exact supporting identity in the directional model |
| `B05Sign.conj_cancel` | [B05Sign/Algebra.lean:52](B05Sign/Algebra.lean#L52) | (6.14), inverse conjugation cancellation | exact supporting identity in the directional model |
| `B05Sign.logD_one` | [B05Sign/Algebra.lean:58](B05Sign/Algebra.lean#L58) | (6.4), value at the identity | exact supporting identity in the directional model |
| `B05Sign.logD_mul` | [B05Sign/Algebra.lean:60](B05Sign/Algebra.lean#L60) | (6.5)/(7.4), product derivative cocycle | stronger: every noncommutative ring with the declared derivation |
| `B05Sign.Gauge.ext` | [B05Sign/Algebra.lean:70](B05Sign/Algebra.lean#L70) | (5.9), equality of group coordinates | modelling choice: pair of a unit and a ring element |
| `B05Sign.mul_unit` | [B05Sign/Algebra.lean:99](B05Sign/Algebra.lean#L99) | (5.9), first multiplication coordinate | exact in the directional model |
| `B05Sign.mul_shift` | [B05Sign/Algebra.lean:100](B05Sign/Algebra.lean#L100) | (5.9), second multiplication coordinate | exact in the directional model |
| `B05Sign.tauLit_mul` | [B05Sign/Algebra.lean:106](B05Sign/Algebra.lean#L106) | (6.4)/(6.5), literal map respects multiplication | exact algebraic content; weaker than Lie homomorphism: smoothness not modeled |
| `B05Sign.tauRec_mul` | [B05Sign/Algebra.lean:111](B05Sign/Algebra.lean#L111) | Plus reconstruction of (6.4)/(6.5) | modelling choice: positive cocycle also respects multiplication |
| `B05Sign.tauLit_injective` | [B05Sign/Algebra.lean:134](B05Sign/Algebra.lean#L134) | Lemma 6.1, injectivity | exact algebraic content; weaker than Lie embedding: no topology |
| `B05Sign.tauRec_injective` | [B05Sign/Algebra.lean:137](B05Sign/Algebra.lean#L137) | Reconstructed Lemma 6.1, injectivity | modelling choice: plus map is also injective |
| `B05Sign.tilted_action_lit` | [B05Sign/Algebra.lean:141](B05Sign/Algebra.lean#L141) | (6.13), literal right multiplication | exact in the directional model |
| `B05Sign.tilted_action_rec` | [B05Sign/Algebra.lean:148](B05Sign/Algebra.lean#L148) | Plus reconstruction of (6.13) | modelling choice: explicitly changed sign |
| `B05Sign.act62_mul` | [B05Sign/Algebra.lean:155](B05Sign/Algebra.lean#L155) | (6.2) and (5.9), right action composition | exact algebraic action law on affine coordinate alpha=A-A0 |
| `B05Sign.act62_one` | [B05Sign/Algebra.lean:160](B05Sign/Algebra.lean#L160) | (6.2), identity right action | exact algebraic action law on affine coordinate alpha=A-A0 |
| `B05Sign.torsion_lit` | [B05Sign/Algebra.lean:167](B05Sign/Algebra.lean#L167) | (6.13-lit)+(7.3), checking (7.4) | exact residual -2 h^-1 D h; refutes unrestricted printed covariance |
| `B05Sign.torsion_rec` | [B05Sign/Algebra.lean:172](B05Sign/Algebra.lean#L172) | (6.13-rec)+(7.3), reconstructed (7.4) | modelling choice: exact covariance after the explicit sign change |
| `B05Sign.connection_lit` | [B05Sign/Algebra.lean:184](B05Sign/Algebra.lean#L184) | (6.13-lit)+(6.19)/(6.22), checking (6.20) first coordinate | exact residual -2 h^-1 D h with affine origin retained |
| `B05Sign.connection_rec` | [B05Sign/Algebra.lean:190](B05Sign/Algebra.lean#L190) | Reconstructed (6.20), first coordinate | modelling choice: exact covariance after the explicit sign change |
| `B05Sign.second_connection` | [B05Sign/Algebra.lean:195](B05Sign/Algebra.lean#L195) | (6.20), second coordinate | stronger: holds for multiplication by any Gauge element, independently of its shift |
| `B05Sign.biConnection_rec` | [B05Sign/Algebra.lean:200](B05Sign/Algebra.lean#L200) | Reconstructed (6.20), both coordinates | modelling choice: exact pair equivariance after the explicit sign change |
| `B05Sign.conj_mul_inv` | [B05Sign/Surrounding.lean:7](B05Sign/Surrounding.lean#L7) | (6.14)-(6.16), inverse product order | exact supporting identity in the directional model |
| `B05Sign.leftAct_formula` | [B05Sign/Surrounding.lean:15](B05Sign/Surrounding.lean#L15) | (6.15), displayed left action | exact rewriting, preserving multiplication order |
| `B05Sign.leftAct_mul` | [B05Sign/Surrounding.lean:21](B05Sign/Surrounding.lean#L21) | (6.15)-(6.16), left action composition | exact algebraic law; independent of either tilted-map choice |
| `B05Sign.leftAct_one` | [B05Sign/Surrounding.lean:26](B05Sign/Surrounding.lean#L26) | (6.15), identity left action | exact algebraic law; independent of either tilted-map choice |
| `B05Sign.projection_formula` | [B05Sign/Surrounding.lean:33](B05Sign/Surrounding.lean#L33) | (6.11), displayed projection | exact rewriting in the directional model |
| `B05Sign.projection_lit` | [B05Sign/Surrounding.lean:38](B05Sign/Surrounding.lean#L38) | (6.14), literal projection invariance | exact algebraic invariance; weaker than full quotient/principal bundle construction |
| `B05Sign.projection_rec` | [B05Sign/Surrounding.lean:45](B05Sign/Surrounding.lean#L45) | Checking (6.14) after plus reconstruction | modelling choice: exact residual 2 epsilon (D h) h^-1 epsilon^-1 |
| `B05Sign.stabilizer_lit` | [B05Sign/Surrounding.lean:53](B05Sign/Surrounding.lean#L53) | (6.6)-(6.9), literal stabilizer | exact algebraic origin-fixing identity |
| `B05Sign.stabilizer_rec` | [B05Sign/Surrounding.lean:56](B05Sign/Surrounding.lean#L56) | Checking (6.6)-(6.9) after plus reconstruction | modelling choice: exact origin image 2 h^-1 D h |
| `B05Sign.Witness.swap_squared` | [B05Sign/Witness.lean:23](B05Sign/Witness.lean#L23) | Concrete countermodel unit construction | modelling choice: square of the integer swap matrix is 1 |
| `B05Sign.Witness.logarithm` | [B05Sign/Witness.lean:32](B05Sign/Witness.lean#L32) | Concrete input to the residual theorems | modelling choice: inner derivation gives diag(-1,1); not the central-phase jet |
| `B05Sign.Witness.residual_nonzero` | [B05Sign/Witness.lean:36](B05Sign/Witness.lean#L36) | Nonvanishing of literal (6.20)/(7.4) residual | exact for the specified integer-matrix countermodel |
| `B05Sign.Witness.torsion_not_covariant` | [B05Sign/Witness.lean:43](B05Sign/Witness.lean#L43) | Counterexample to literal (7.4) | exact in the specified ring; weaker than a U(64,64) geometric realization |
| `B05Sign.Witness.connection_not_covariant` | [B05Sign/Witness.lean:50](B05Sign/Witness.lean#L50) | Counterexample to literal (6.20), A0=0 | exact in the specified ring; weaker than a U(64,64) geometric realization |
| `B05Sign.Witness.reconstructed_projection_not_invariant` | [B05Sign/Witness.lean:58](B05Sign/Witness.lean#L58) | Counterexample to (6.14) after changing only the tilted sign | exact in the specified ring; no claim about repaired projection definitions |

Additional proof-bearing definitions included in the axiom audit:

| Definition | Source equation | Fidelity |
|---|---|---|
| `B05Sign.gaugeGroup` | (5.9) | exact algebraic group structure in the declared model |
| `B05Sign.tauLitHom` | (6.4)-(6.5) | exact algebraic group homomorphism; no Lie smoothness |
| `B05Sign.tauRecHom` | reconstructed (6.4)-(6.5) | modelling choice: the plus cocycle is also a group homomorphism |
| `B05Sign.innerDiff` | witness prerequisite | modelling choice: commutator is additive and obeys Leibniz |
