# B07, one-direction variation: does (9.4) vary to (9.7)?

**Status:** survey and re-derivation complete, pending the Task 5 audit. **Result:** under reading V, the printed (9.7) is **not** the Euler–Lagrange equation of (9.4) in the ϖ direction for any nonzero member of B02's Shiab family in 4D, nor for the named branches in 14D. This is a finding about reading V. It is not a claim that no reading of (9.4) works.

## The question

§9.1 of the April 2021 draft (pp. 43–45) prints a first-order bosonic action (9.4) and states, "by the calculus of variations", that its first variation in the direction δϖ = α is

⟨α, ⊚_ω F_{A_ω} + ∗κ₁T_ω⟩ = ⟨α, Υᴮ_ω⟩   (9.7).

B07 asks whether this follows. It tests the ϖ direction only, with ε and the metric fixed (register row B07-F). Plan: `docs/superpowers/plans/2026-10-16-b07-variation.md`, rev 1.1 (`be2ae34`). Codex and Grok each reviewed it twice, then the user approved it.

## Reading V (`[GU-recon]`)

(9.4) is degree-inconsistent as printed, so it cannot be varied literally (`transcription.md`, conflict 2):
- in line 1, the outer ∗ encloses ⊚(…) + (κ₁/2)T, a sum of an (d−1)-form and a 1-form;
- in lines 2–4, the integrand Tr(T ∧ ∗(⊚(…))) is a 2-form, not a top form.

**Reading V** is a star-scope repair of line 1. It moves the κ term outside the ∗:

I₁ = ⟨T, ∗⊚(F_B + ½d_BT + ⅓[T,T])⟩ + (κ₁/2)⟨T,T⟩,

with the metric trace pairing ⟨a, b⟩ = ∫Tr(a∧∗b), compact support, and ε and the metric fixed. With the pinned Hodge convention (`gu/forms.py`), ∗∗ = +1 on (d−1)-forms at (3,1), (1,3), (7,7) and (9,5). So ⟨T, ∗ω⟩ = ∫Tr(T∧ω), and

I₁ = ∫Tr(T∧⊚F_B) + ½∫Tr(T∧LT) + ⅓∫Tr(T∧⊚b(T,T)) + (κ₁/2)⟨T,T⟩,   L := ⊚∘d_B.

V is a reconstruction `[GU-recon]`, not the printed text. The other readings are in the register (`transcription.md`, Readings register). They include the literal lines (not well-defined functionals), symmetrized or per-occurrence ⊚, restricted variations, mixed bracket modes, and bracketed products read as ordinary products (B07-G). None of them was executed.

## What the variation gives

Both sides of the comparison are polynomials in T. They are compared order by order at s = 0 (`transcription.md`, H1–H6).

- **Order T⁰ matches**: ∫Tr(α∧⊚F_B).
- **Order T¹ leaves a residual.** The variation of ½∫Tr(T∧LT) is ½∫Tr(α∧(L + L†)T). The target has ∫Tr(α∧LT). So the Euler–Lagrange expression carries the **extra term ½(L†−L)T**, and the residual is R₁ = ½∫Tr(α∧(L†−L)T). Its principal symbol gives the pointwise test

  C1(k; t, a) = Tr(t∧⊚(eᵏ∧a)) + Tr(a∧⊚(eᵏ∧t)).

  C1 = 0 is **necessary** for (9.7) under V (H2). A single nonzero C1 entry therefore rejects (9.7) under V, whatever the curvature, coefficient derivatives or ε. C1 does not involve the bracket.
- **Order T² leaves the pointwise test** C2 = ⅓Tr(α∧⊚b(T,T)) + ⅔Tr(T∧⊚b(α,T)) − Tr(α∧⊚(T∧T)) (H3). C2 depends on the normalization of [T,T], which the draft does not define for ad-valued 1-forms:
  - **N1**: b(T,T) = T∧T. This is the Chern–Simons-consistent reading.
  - **N2**: the graded commutator, so b(T,T) = 2T∧T.
  - **N0**: an ungraded commutator of the whole form-valued product, [x,y] = x∧y − y∧x, so [T,T] = 0. This is **not** the coefficient-wise extension of (12.26): wedging the forms and taking ab − ba of the coefficients gives [T,T] = 2T∧T, which is N2 (and is `gu.cliffform.bracket`'s mode C).
- **The κ term matches** under line 1's κ₁/2. Under line 4's κ₁ it is off by a factor 2 (H6; conflict 1).

## Results (`result.json`)

The runner took 5293.6 s at `source_commit` `b60bbfc`. Its scope tags: `identity` for the 4D family and `counterexample` for the 14D witnesses.

**4D, the whole family.** The runner tests the six Shiab-family monomials F, F+B, F+B′, F′, F′+B, F′+B′ (coefficients α, −αγ/2, −αδ/2, β, −βγ/2, −βδ/2). It does this for each of the eight bracket modes m₀m₁m₂ ∈ {C, A}³ at signatures (3,1) and (1,3), with exact rational arithmetic:

| Kernel over the six monomials | Dimension, every mode and both signatures |
|---|---|
| C1 | 0 |
| C2 under N1 | 0 |
| C2 under N2 | 0 |
| C1 and C2 jointly, N1 | 0 |
| C1 and C2 jointly, N2 | 0 |

Every column is nonzero on its own, with 96 to 168 nonzero C1 entries per column. So within each fixed-mode family, the only combination with C1 = 0 is the zero operator. The same holds for C2 under N1 and under N2. This is the dimension-4 analogue of the 14D question, not the 14D question itself.

**14D, the named branches.** Each branch has an exact nonzero C1 entry at every signature tested:

| Branch (B02) | t | α | C1 at (3,1) | (1,3) | (7,7) | (9,5) |
|---|---|---|---|---|---|---|
| CCC literal, Φ₁ = F, Φ₂ = B | [0, 1] | [1, 3] | −2 | −2 | −2 | −2 |
| CAA Einstein, Φ₁ = F, γ = 1, δ = 0 | [0, 4] | [1, 6] | 2 | −2 | 2 | 2 |
| CAC chiral, Φ₁ = F + F′, δ = 1, γ = 0 | [0, 4] | [1, 6] | 2 | −2 | 2 | 2 |

Here k = 0 throughout, and t and α are given as [form index, Clifford mask]. These are counterexamples, not a 14D kernel computation.

**Controls** (`tests/test_b07.py`, 12 tests). The 3D Chern–Simons control (⊚ = id) gives C1 = 0 and C2(N1) = 0, and its N2 impostor gives C2 ≠ 0 (H4). A non-self-adjoint impostor gives C1 ≠ 0. The family columns reassemble to B02's `shiab` on all 96 basis 2-forms at (3,1), for all eight modes. The three named branches match B02's `shiab`.

**Independent re-derivation** (Task 4, `rederive.py`, `rederivation.md`, Codex). It does not import `gu.shiab`, `gu.cliffform`, `gu.forms` or any B07 module, and does not read `result.json`. It shares only `gu.clifford`'s gamma matrices. It has its own exterior algebra and Hodge star, and uses the actual matrix trace (2^{n/2} times the scalar-coefficient trace). It is an independent algorithm, not a blind derivation: Codex read the plan's column and residual definitions and the witness inputs. It recomputed 13 results, and all 13 agree with `result.json`:
- the eight C1 kernels at (3,1), all trivial, with identical nonzero counts per column;
- the C2/N1 kernels for CCC and CAA, trivial, with identical counts;
- the three named-branch C1 witnesses at (7,7): matrix trace ∓256, which is ∓2 after dividing by 128.

Claude re-checked the ten kernel rows against `result.json`. The re-derivation's own controls and three seeded faults are recorded in `rederivation.md`.

## What this means

- Under V, the printed (9.7) omits the term ½(L†−L)T. It is the Euler–Lagrange equation of (9.4) only if L = ⊚∘d_B is formally self-adjoint at the principal-symbol level. No nonzero member of B02's fixed-mode Shiab family is, in 4D. The three named 14D branches are not either.
- Symmetrizing the action does not help (B07-S): ½⟨T, LT⟩ already equals ½⟨T, ½(L+L†)T⟩ up to boundary terms. Making (9.7) follow under V requires changing the **target** to ½(L+L†)T, or changing ⊚.
- **Not shown:** that no reading works. Unexecuted readings that could change C1 include per-occurrence ⊚ (B07-Y), restricted variations (B07-R), the author's lost operator (B07-O, fn. 10), mixed bracket modes (B07-M), ordinary products (B07-G), ϖ-dependent Φ (B07-X), and a different trace/pairing convention (B07-Q).
- **N0** was recorded but not executed (user decision). Under N0 the cubic term vanishes, so the "C-S like" terms are not Chern–Simons-like, and C2 reduces to −Tr(α∧⊚(T∧T)). N0 cannot rescue (9.7), because C1 does not involve the bracket.

  Grok's independent review (requested by the user) agrees with the rescue claim and with H3's N0 residual. It ranks the readings N1 > N2 ≫ N0. N0 makes the braced "C-S Like Terms" vanish identically, against the printed label, and is best kept as a degenerate literalization. Its N0 residual was **not** surveyed, so this README states no N0 kernel dimension and does not claim C2 ≠ 0 under N0 for the Shiab family. The nonzero N1/N2 columns mix −Tr(α∧⊚(T∧T)) with the cubic variation, so they do not settle it.

## Conflicts in the printed displays (`transcription.md`)

- **κ normalization** (conflict 1): κ₁/2 in line 1, κ₁ in line 4.
- **(9.4) lines 1 and 2–4** are degree-inconsistent as printed (conflict 2). V repairs line 1.
- **(9.12)/(9.13)** (conflict 4, H8). Under the pinned convention, ∗ is an anti-isometry on 1-forms (q odd), so ∗\* = −∗ between Ω¹ and Ω^{d−1}. The metric gradient of I₂/2 is

  d\*_A⊚\*⊚F_A + κ₁d\*_A⊚\*(∗T) − κ₁∗⊚F_A − κ₁²T.

  (9.13) drops a ∗ in term 2 (⊚\*T is ill-typed) and has the wrong sign in terms 3 and 4. (9.12)'s Id stands where ∗\* = −∗ is needed. These are bookkeeping findings; B07 does not compute the second-order Lagrangian.

## The fermionic side (H7)

The fermionic variation (9.16)–(9.22) was not computed; it is blocked on B05-Q's open pairing and adjoint conventions.

The draft prints no fermionic action, only operators "like" (9.16) and the compiled variation (9.18) (conflict 7). H7 is a conditional ledger relative to a reconstructed action S_F = ∫⟨Ψ̄, 𝒟̸_ω Ψ⟩. Its findings:
- (9.18) lists equations for the unbarred fields only. The ν- and ζ-variations (equations for the barred fields) are absent, although p. 46 calls the four fields distinct (conflict 6). This is a completeness concern, not evidence that the printed equations are false.
- Components 1 and 2 follow under the B05-Q, B05-Y, B05-A and B05-V hypotheses, component 2 only up to an overall sign.
- In component 3, the ζ̄ν and ν̄ζ terms follow conditionally. The ⊚ζ̄ζ term does **not** follow as printed: varying ζ̄∗⊚(αζ) gives a transpose of ⊚, not ⊚, and its degree conflicts with the other two terms (conflict 5).

No C1 or C2 result transfers to this ledger: a spinor-valued ⊚ is a different map from the ad-valued ⊚ tested here. See `experiments/B05/README.md` for the open B05 inputs.

## The (6.13) sign, in Lean

B05 found that (6.4)/(6.13) print a minus sign on h⁻¹dh, while (6.2), (6.20) and (7.4) need a plus. Lean checks both signs (merge `a134286`; `lean/B05Sign/`; the B05Sign section of `lean/COVERAGE.md`; `lean/ValidationB05Sign.md`).
- The literal minus leaves a residual −2h⁻¹Dh in (6.20)'s first connection and in (7.4)'s torsion.
- The reconstructed plus leaves a residual in (6.14)'s projection.
- **No single sign preserves all the listed printed formulas.**

Scope: this is a directional differential-ring formalization of both signs. The ring is arbitrary and possibly noncommutative, with an endoderivation and the one-forms replaced by the coefficient algebra. It is not a Lean check of B07, and not a global geometric repair. It does not enter B07's computation: B07 varies ϖ at fixed ε, and B = ∇⁰ + ε⁻¹d₀ε is fixed whichever sign the tilted map carries (H5).

## Provenance

| Item | Commit | Author |
|---|---|---|
| Plan rev 0 / rev 1 / rev 1.1 (approved) | `7b07e50` / `7d89105` / `be2ae34` | Claude |
| Transcription rev 0 / rev 1 (rev 1 folds Codex's blind second reading and comparison) | `0912d4c` / `564ed4a` | Claude |
| `variation.py`, `run.py`, `tests/test_b07.py` (verbatim from the plan) | `b60bbfc` | Codex |
| `result.json` (`source_commit` `b60bbfc`) | `c7229e9` | Codex |
| `rederive.py` / `rederivation.md` | `de8ab67` / `dccc0a4` | Codex |
| Transcription rev 1.1 (Grok's N0-mechanism correction) | this commit | Claude |
| This README | this commit | Claude |

Source PDF SHA-256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.

Test results:
- 12 B07 tests pass, and the full suite has 365 passed.
- Eight seeded faults (F1–F6, F1b and F6b, defined in the plan's Task 3 Step 5) each fail on the named assertion, with byte-verified restores.
- Claude compared `result.json` with the plan's smoke run, minus `seconds` and `source_commit`: they are identical. Grok replayed the 12 tests and 8 faults in a scratch clone, and recomputed the 12 witnesses with `c1_witness`. The P7 clean-clone re-run comes after the audit.

## Scope

The scope tags are `identity` (exact kernels over the six-monomial family, per bracket mode, in 4D) and `counterexample` (one exact nonzero C1 entry per named branch in 14D). Everything is under reading V, in the ϖ direction, at fixed ε and metric. This stage makes no claim about the second-order Lagrangian (9.11)–(9.15) beyond the H8 bookkeeping, nor about the fermionic variation, nor about readings outside the register.
