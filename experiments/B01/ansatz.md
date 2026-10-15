<!-- experiments/B01/ansatz.md -->
# B01 ansatz (pre-registered)

Provenance: [ext] parameterization; [GU-recon] until reconciled with GU (3.8)–(3.10), p. 19, and §3.5, p. 22.

**Family.** On X = R^{1,3}, η = diag(1,−1,−1,−1). Vertical fibre Sym²(R⁴) with
B_λ(H,K) = tr(ηHηK) − λ tr(ηH) tr(ηK). Chimeric form on R⁴ ⊕ Sym²: s_H·η ⊕ s_V·B_λ, with s_H, s_V ∈ {±1}.

**Claims to check exactly (expected outcomes):**
1. Eigenvalues of B_λ in the basis {E_ii} together with {E_ij + E_ji : i<j}: −2 (×3), 2 (×3), 1 (×3), 1−4λ (×1).
2. Vertical inertia: (7,3,0) for λ < 1/4; (6,3,1) at λ = 1/4; (6,4,0) for λ > 1/4.
3. Chimeric inertia at λ ∈ {0, 1/4, 1}: the table in tests/test_b01.py, derived by adding horizontal inertia (1,3,0) to the vertical inertia, swapping positive/negative counts on each negatively signed summand; confirm the earlier probe exactly.

**Reconciliation criterion (Task 4).** "Match" means: the draft's metric on V ⊕ H* equals s_H·η ⊕ s_V·B_λ for some λ and signs, up to a positive rescaling of each summand, under an explicit map of the draft's symbols to ours. Anything else is reported as a documented mismatch. Neither outcome selects a physical signature.

Scope of claims 1–3: identity (exact, all λ via the symbolic eigenvalues; the table at listed λ).

This is confirmatory pre-registration: the expectations were known from the prior probe and plan before this experiment. Diagonal Gram block is I_4 - lambda*v*v^T with v=(1,-1,-1,-1), so its eigenvalues are 1 (three times) and 1-4lambda. The three time-space off-diagonal basis matrices have norm -2; the three space-space ones have norm +2. These yield claims 1–3 without using the implementation output. Numeric lambda values are rational; the symbolic path uses the real LAM symbol.
