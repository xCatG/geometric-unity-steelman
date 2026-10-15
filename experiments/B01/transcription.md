# B01 transcription: GU (3.7)–(3.10) and §3.2, §3.5 (signature of the chimeric metric)

Transcriber: Claude (Opus 5.5), 2026-10-15. Plan Task 3.

**Independence caveat.** Claude did not read Codex's `experiments/B01/dewitt_family.py`. However, Claude wrote the plan, which contains that code and the expected inertia table, and Claude computed the DeWitt family earlier in the session. So this transcription is independent of the implementation's *execution*, but not of its *design*. Codex's `rederivation.md` (Task 4) provides the second route.

## Source

- Eric Weinstein, *Geometric Unity: Author's Working Draft, v1.0*, April 1, 2021.
- URL: `https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf`
- SHA-256: `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4` (2,087,649 bytes, 69 pages, fetched 2026-10-15)
- Pages read: 18–22 (printed numbers equal PDF pages). Transcribed from page images rendered at 110 dpi.

## Verbatim equations and passages

**p. 18, (3.7).**
$$H^* = \pi^*(T^*(X)) \qquad H^* \hookrightarrow T^*(Y)$$
"which at the point g ∈ Y carries an induced metric g via $H_{\pi^*(\pi_*(g))}$ as the pull back of the push-forward metric. We will refer to the dual bundle $(H^*)^*$ simply as H." "… the total space Y carries a vertical sub-bundle V ⊂ T(Y) as the subspace of vectors pointing along the fibers of Y over X."

**p. 19, (3.8).** "At a point y ∈ Y, lying in the fiber $\pi^{-1}(\pi(y))$ let two symmetric two tensors $A, B \in T^V_y(X)$ represent a random choice of two elements in the vertical tangent space … Then, by the symmetry of the metrics, the Frobenius inner product is defined by the double contraction against the metric represented by the point y which, in an orthonormal basis would look like:"
$$\langle A,B\rangle_y = \mathrm{Tr}_y(A^T\cdot B) = \mathrm{Tr}_y(A\cdot B) \tag{3.8}$$

**p. 19, between (3.8) and (3.9).** "Here the space of metrics breaks into a Trace and Traceless component. The Traceless component has signature $(i\cdot n - i^2,\ \frac{n^2+2i^2-2i\cdot n+n-2}{2})$ with a freedom to assign either a (0,1) or (1,0) signature to the trace component. In this exposition we choose the later so as to assume our Frobenius metric can be taken to be of signature"
$$\Big(i\cdot n - i^2 + 1,\ \frac{n^2+2i^2-2i\cdot n+n-2}{2}\Big) = (4,6)\quad\text{for } i=1,\ n=4 \tag{3.9}$$
"for the four dimensional (1,3) metric of greatest physical interest with one temporal and three spatial dimensions. Naturally, this would work equally well for a cosmetic shift to the (3,1) sector …" Footnote 2: "NB: This choice is one of the few non-forced choices allowed in the strong form of GU."

**p. 19, (3.10).**
$$C(Y) = C = V \oplus H^* \qquad C^*(Y) = C^* = V^*\oplus H \tag{3.10}$$
"We now define two metric bundles which, with the above assignments, are canonically isomorphic."

**p. 20 (end of §3.2).** "Because the fibers at a point g ∈ Y impart metrics to to the vertical $V_g$ and horizontal sub-bundles $H^*_g$, taking those sub-spaces to be orthogonal to each other allows for two different choices of metric to be inherited by their direct sum according to choices of sign."

**p. 22, §3.5 (verbatim).** "We should begin by noting that the choice of (1,3) metric signature (which can be mirrored by choice of a (3,1) and thus is not meaningfully distinguished from it) is treated by us as anthropic data. … This recognition, forces a (3,6) signature on the space of traceless symmetric two tensors which, when combined with the trace portion seen as either a (0,1) or (1,0) space, can become either a (3,7) or the (4,6) metric respectively. Here again, we make an anthropic choice and select the latter of the two for two reasons. In the first place, we believe that (3,7) will not be compatible with the observed forces and symmetries of the Standard Model. Secondly, we want to leave ourselves room for complex techniques and view a real $(4,6)_\mathbb{R}$ structure as holding the door open for some models we have been playing with favoring reduction to $(2,3)_\mathbb{C}$.

Lastly we must combine these choices of fiber metrics in Y with metrics pulled up from the base space of signature (1,3). These combinations in turn could lead to (4,10) or (8,6) in the discarded former cases of (7,3) or (3,7), or (5,9) or (7,7) in the case of the latter (4,6) or (6,4). We do not know how to choose between these however as this is one of the few places in the model where choices are made that are not yet forced.

To begin with, we will assume that the metric on Y is split with signature (7,7) (rather than (9,5) which can be worked out by the interested reader) as it is more balanced and appears to lend itself better to both some complex and Clifford Algebra techniques."

Then (3.18) $\mathrm{Cl}_{7,7}\cong\mathbb{R}(128)$; (3.19) $\mathrm{Spin}(7,7)\to\mathrm{SO}(64,64)\to\mathrm{U}(64,64)$; (3.20) $\rho_{\mathrm{Spin}}:\mathrm{Spin}(14,\mathbb{C})\to\mathrm{U}(128,\mathbb{C})$.

## Symbol table

| Symbol | Type | Defined |
|---|---|---|
| X | base manifold, dim n = 4 | throughout |
| Y | space of pointwise metrics on X (fibre over x: Sym²-type metrics); dim 4 + 10 = 14 | §3.1 |
| π: Y → X | bundle projection | §3.1 |
| y or g ∈ Y | a point of Y = a metric on T_{π(y)}X | p. 18–19 |
| V ⊂ TY | vertical bundle; fibre ≅ symmetric 2-tensors on T_xX, real dim 10 | p. 18 |
| H* = π*(T*X) ⊂ T*Y | pulled-back cotangent bundle, real dim 4; metric induced from the point g | (3.7) |
| ⟨A,B⟩_y | Frobenius form on V_y: "double contraction against the metric y" | (3.8) |
| C = V ⊕ H* | chimeric bundle, real dim 14, metric = (sign)·Frobenius ⊕ (sign)·g | (3.10), p. 20 |
| i, n | i = number of temporal directions in the base metric, n = dim X | (3.9) |

## Conventions as stated

1. **The Frobenius form** is the double contraction with y. In coordinates this is $\langle A,B\rangle_y = y^{ac}y^{bd}A_{ab}B_{cd}$, i.e. tr(y⁻¹A y⁻¹B). "Tr(A^T·B)" is written "in an orthonormal basis". The draft has **no DeWitt trace coefficient** (λ). It sets the sign of the trace direction by fiat ("freedom to assign (0,1) or (1,0)"), and footnote 2 calls this a non-forced choice.
2. **The traceless signature formula** is $(i(n-i),\ [n(n+1)/2 - 1 - i(n-i)])$. Arithmetic check: n(n+1)/2 − 1 − i(n−i) = (n² + n − 2 − 2in + 2i²)/2, which matches the draft's second entry. The first entry i(n−i) is the number of mixed temporal–spatial components. At i = 1, n = 4 this gives (3,6).
3. **The trace component goes into the first slot:** "(1,0)" gives (4,6) and "(0,1)" gives (3,7).
4. **Combining with the base** (p. 22): vertical (3,7) or (7,3) gives total (4,10) or (8,6); vertical (4,6) or (6,4) gives total (5,9) or (7,7). Every listed total equals (base (1,3)) + (vertical), with the base summand's sign held fixed and only the vertical summand's overall sign varied.
5. **Signature order** (which slot counts negative directions) is never stated explicitly. See branches R1–R2.

## `[GU-recon]` branches

- **R1: the draft writes signatures as (#negative, #positive) throughout.** Here "(1,3), one temporal and three spatial" is the mostly-plus metric with time negative. With the Frobenius form tr(y⁻¹Ay⁻¹B), the i(n−i) mixed components are negative and the rest of the traceless part is positive. That makes the traceless part (3 neg, 6 pos) = "(3,6)" ✓. The trace "(1,0)" is then a negative trace direction. All of §3.5's enumeration is internally consistent under R1.
- **R2: the draft writes (#positive, #negative) throughout.** Then the traceless part "(3,6)" has 3 positive directions. Contraction with y gives the opposite count (6 positive) for either overall sign of y, because y⁻¹ appears twice. So R2 requires the Frobenius form to carry an overall minus sign that the draft never states. R2 is consistent only together with that unstated sign.
- **R3: mixed order** (base in one order, fibre in the other). Not excluded by the text. Recorded for completeness.
- **The "(9,5)" remark.** "(9,5)" is not among the four totals the draft enumerates: (4,10), (8,6), (5,9), (7,7). Two readings:
  - **(9a)** "(9,5)" is "(5,9)" written in the opposite slot order, i.e. the same metric up to an overall sign.
  - **(9b)** It is a fifth configuration that flips the base summand's sign relative to the enumeration.

  The text does not decide between them.
- **"(1,3) can be mirrored by (3,1), not meaningfully distinguished."** Either this is an overall sign flip of the base metric alone (which changes the totals), or a flip of the whole metric on Y (which swaps the slots of every total). Unresolved.

## Draft's stated signature claims (for reconciliation)

- The vertical (Frobenius) signature is (4,6), by choice (eq. 3.9, footnote 2) `[GU-orig]`.
- The total is (5,9) or (7,7); the choice is "not yet forced" (p. 22) `[GU-orig]`.
- The working assumption is (7,7), with (9,5) as an alternative left to the reader (p. 22) `[GU-orig]`.
- Cl₇,₇ ≅ ℝ(128) and Spin(7,7) → SO(64,64) → U(64,64) (3.18–3.19) `[GU-orig]`.
