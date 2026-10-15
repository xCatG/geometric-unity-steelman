# B03 formalization plan and fixed expectations

Scope: the explicit monomial real-structure/chirality claims in B03, not its branching, RS projector or dynamics. Use the existing Lean 4.24.0 / pinned Mathlib project. All edits stay in lean/.

The model uses the exact column convention M[perm[j],j]=i^phase[j], leading Jordan-Wigner Z strings, and multiplication by i on timelike gammas. Expected signs come from the handoff, README matrix table and independent rederivation, never from adjusted Lean output.

1. Implement the monomial model and required all-entry Python bridge; validate the (3,1) control first.
2. Kernel-check J squared (+1 for 7,7; -1 for 9,5 and 3,1), C/parity (-,+,+), Clifford products, common J/gamma sign and C intertwining. Certify the imaginary-gamma selector and the library's *first* admissible chirality phase.
3. Prove generic complex-vector semantics (antilinearity, product and conjugation) and lift certificates to J/spinor statements. Extend common gamma intertwining to all bivectors algebraically.
4. Certify diagonal sign-valued Cartans, bijective weights, split-dependent J weight flips; prove pairwise Cartan commutation. The recorded flips are (+------), (+------), (-+-----), (+-).
5. Run convention faults against unchanged Python expectations: reverse Y phase, omit timelike i, reverse chirality sign. Retain why each fails. Audit every public theorem, update coverage/inventory, and time a clean B02+B03 build with dependency caches retained.

Prefer kernel decide and structural proofs throughout. If native_decide becomes necessary, record every occurrence and both native trust axioms. Current expectation: no numerical discrepancy; report any discovered discrepancy immediately rather than changing the target signs.
