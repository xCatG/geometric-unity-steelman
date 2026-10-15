# GU Steelman: Design Spec

Date: 2026-10-14 · Revision 2, after adversarial review · Status: draft for user review

## 1. Purpose

A personal deep-dive into Eric Weinstein's Geometric Unity, using the April 2021 draft. We give the theory the benefit of the doubt: find its gaps, propose the most charitable repairs, and test each repair with computation (and with Lean where that adds real confidence). Exploring is the goal; polish isn't. The deliverable is the gap register `docs/gaps/register.md`, whose entries end in verdicts backed by code.

**Non-goals:** validating GU as physics, quantization, deciding dynamical questions (unitarity, positivity of energy) by algebra alone. A passing algebraic check is reported as exactly that.

## 2. Claim discipline (two axes)

Every claim carries **one provenance tag and one evidence status**. This matches register §"Sources".

| Provenance | Meaning |
|---|---|
| `[GU-orig]` | Stated in the draft, with page or equation |
| `[GU-recon]` | Our reading of an ambiguous passage, with the alternatives listed |
| `[ext]` | Our repair or new assumption |
| `[lit]` | External source: S-id from `docs/gaps/sources/INDEX.md`, or until that exists the register's labels (NP, T, W, O) with page |

| Evidence status | Meaning |
|---|---|
| `verified:<path>` | Backed by a tracked script, test or proof under `experiments/`, `tests/` or `lean/`. Never under `.agent-handoff/`, which git ignores. |
| `unverified` | Everything else |

A verified `[ext]` stays `[ext]`. Rules:
- Obstructions are stated "within ansatz X".
- X is committed to git before the run that tests it.
- Agreement between agents is not evidence.

## 3. Agents and roles

| Agent | Where | Owns |
|---|---|---|
| Claude (Opus 5.5) | pane 0:2 | Direction, spec and plans, repair design, review, independent transcriptions, write-ups. Orchestrates every task. |
| Codex (GPT-6-Astra) | pane 0:3 | Gap register, library, experiments, Lean |
| agy (Gemini 3.8 Flash) | pane 0:4 | Literature: `docs/gaps/sources/`. No claims. Its hook errors are known and ignored. |
| Fable 5.1 | Claude subagent | Theory bottlenecks only, under the rules in §8 |

Handoffs follow tmux-agent-orchestration: `.agent-handoff/<task>/`, one writer per file.

### Verification protocol: replication, not reproduction

Rerunning the same code catches nothing, and the weakest link is turning the PDF into code. So:

1. **Independent transcription.** Before any code exists for a GU formula, the agent *not* writing the code produces `experiments/<id>/transcription.md`, typed directly from the PDF with page and equation numbers. It covers every symbol's type, the conventions, and the alternatives tagged `[GU-recon]`. The implementer codes from the transcription. Any disagreement with their own reading is resolved in that file first.
2. **Positive controls.** Every search or "nonexistence" engine must first recover a known nonzero answer, e.g. the Riemann→Ricci contraction in the Riemannian analog, or the known Spin(10) 16 branching. Only then does a zero result count.
3. **External oracle** for representation theory: published tables (Slansky 1981; Yamatsu's tables) or LiE run under WSL if it installs cleanly. The `gu` library's branching code must agree with the oracle on its test cases.
4. **Pre-registration.** Commit the ansatz and the expected-outcome criteria first. Commit the results in a later commit.

## 4. Repository layout (minimal; grows per experiment)

```
docs/gaps/                  register.md (Codex); sources/ (agy); notes/
docs/superpowers/           specs and plans (Claude)
docs/fable-ledger.md
gu/
  inertia.py    exact inertia of symmetric forms (Sylvester / LDLᵀ over ℚ). No floating-point signature claims.
  clifford.py   gamma matrices for any (p,q), exact Gaussian integers (seeded from argon.md Agent 1); chirality; charge and Dirac conjugation; reality and Majorana tests; Rarita–Schwinger (gamma-traceless) projector
  forms.py      exterior algebra on R^{p,q}; Hodge star with the ★² sign; the explicit Λ^{n-1} ≅ Λ¹ identification
  adjoint.py    ad P = u(64,64): ℂl ≅ End(ℂ¹²⁸) ≅ ⊕Λᵏ, the (64,64) Hermitian form, the real structure; generators of u(64,64) and of Spin(p,q); one representative per non-identity component
  reps.py       only when B03 needs it: weights and branching for D_n (Freudenthal), checked against the oracle
experiments/<gap-id>/       transcription.md, ansatz.md (pre-registered), run script, result.json, README with the verdict
tests/                      pytest: textbook facts, positive controls, oracle agreement
lean/                       only when a Lean task is scheduled
```

Dropped from revision 1 as YAGNI: a general `dewitt.py`, since GU's base is a fixed 4D X, so B01 lives in `experiments/B01/`. Also dropped: a generic `equivariant.py`; the intertwiner search is now a fallback (§5).

Exact arithmetic means sympy and integer matrices for small objects. For exact rank and nullspace at size 10³ or more, use `python-flint`, or modular rank at several random primes followed by rational reconstruction.

## 5. Technical approach

Each question splits into three layers:
1. **Complex-algebraic data.** This is the same for every signature (weights, characters, complex Hom counts).
2. **Real-form data**, which depends on the signature:
   - whether each real irrep is of real, complex or quaternionic type (Frobenius–Schur; p−q mod 8). This multiplies dim Hom over ℝ by 1, 2 or 4.
   - Spin(p,q) for p,q ≥ 1 is disconnected, so Lie-algebra equivariance covers only the identity component. Test component representatives separately.
   - ★ is SO-equivariant, not O-equivariant.
   - whether Λ⁷ splits into self-dual and anti-self-dual parts over ℝ depends on the signature.
3. **Dynamical residue:** kinetic signs, unitarity (B04). Out of scope for algebraic verdicts; recorded as open.

B01 (the inertia of a quadratic form on T⊕Sym²) is none of these layers. It is plain exact linear algebra.

**B02 is a direct check, not a search.**
- Transcribe (9.3) independently. Implement it on u(64,64)-valued forms; everything is a 128×128 matrix, so it's cheap.
- Test, in order:
  1. form degree
  2. that the image stays in the real form u(64,64)
  3. the dressed covariance identity `Shiab_(εh)(h⁻¹ηh) = h⁻¹ Shiab_ε(η) h` (register B02), on Lie-algebra generators of u(64,64) and Spin(7,7), plus component representatives
  4. separately, the claimed kernel on Weyl-type curvature, restricted to the Levi-Civita-induced subspace and with a cited page
- Only if (9.3) fails do we search for alternatives. That search counts Hom with characters first, uses ★ to turn Λ¹³ into Λ¹, splits ad as ⊕Λᵏ, and applies the pre-registered constraints (degree, dressing, Weyl-kernel target) before solving anything. The full space is about 3×10¹¹ entries, so we never solve it unreduced.

## 6. Gap lifecycle

`open → transcribed → ansatz-registered → checked → {holds | obstructed-within-X | repaired [ext] | unresolved}`. Each verdict links its experiment directory.

## 7. Phases

| Phase | Content | Exit criterion |
|---|---|---|
| P0 ✅ | Gap register (Codex); sources (agy, best effort) | Done; register committed |
| P1 | **B01 now.** Claude independently transcribes GU (3.8)–(3.10) and §3.5. Codex moves the probe into `experiments/B01/` and switches to exact inertia. Reconcile the λ family with the transcription. | Convention map or exact mismatch, `verified:experiments/B01/…`; register links repointed |
| P2 | Library for B02 (inertia, clifford, forms, adjoint) with tests and positive controls; then the B02 direct check | (9.3) verdict on each test 1–4, within the transcribed conventions |
| P3 | B03: branching of the chiral spinor and of the gamma-traceless vector-spinor under Spin(7,7) → Spin(1,3)×Spin(6,4) (and the (9,5) analog), tracking chirality and reality, with a mirror-sector inventory | **Branching table only, within ansatz X.** No claim about light generations. |
| P4 | Repairs: `[ext]` on obstructed entries; Fable under the §8 rules | Time box: at most 2 repair attempts per entry before marking it unresolved |
| P5 (optional) | Lean for 1–2 statements that their definitions don't directly encode, e.g. the Clifford relations of the explicit matrices | `lake build` |
| P6 | Write-up | Both axes tagged |

Later, picked from the register: B05 anomalies (14D and 4D), B07 variational equations, B09 observation and closure.

## 8. Fable rules ($20 cap)

- **Escalation trigger:** an entry is obstructed or unresolved after the pre-registered ansatz, plus one cheap variant by Claude or Codex, *and* the bottleneck is a derivation or construction, not a computation.
- **Fixed context pack per call:** the transcription, the ansatz, the result.json, and the relevant register entry. The PDF and the whole register are not included. Input cap about 40k tokens. Effort `high`; ask for a bounded answer.
- **Estimate:** about $10/MTok × 40k = $0.40 in, plus $50/MTok × ≤30k = $1.50 out, so ≤ $2 per call. Record actual usage in `docs/fable-ledger.md`. Announce each call to the user before making it. Stop at $20.

## 9. Known traps (forbidden in briefs)

These come from the review of `argon.md`, LLM-generated scaffolding that looks like computation:
- **Uncited filter directions.** Example: GU's Shiab is claimed (register B02) to annihilate Weyl-type curvature, so a filter that *rejects* Weyl-annihilating candidates, as argon.md has, inverts it. Every filter direction cites a draft page.
- **Invented background objects** (e.g. a "canonical 3-form T"). Each input is `[GU-orig]` with a page, or `[ext]` with a reason.
- **Postulated conclusions.** Writing the target term, e.g. a Higgs potential, as a symbol and then "deriving" from it.
- **Lean theorems true by definition.**
- **Unused machinery reported as a search.** Every listed candidate is evaluated; every claimed filter is computed.
- **Riemann symmetries imposed on gauge curvature.** A gauge field strength is only a 2-form obeying the differential Bianchi identity. Weyl-type tests use the Levi-Civita-induced subspace only.
- **Chirality bookkeeping.** In 4D, rewriting a right-handed 16̄ as a left-handed 16 does *not* let it cancel against another left-handed 16. Anomalies cancel only across species whose contributions genuinely have opposite signs.

`argon.md` Agent 1 (the Clifford (9,5) construction, checked exact) seeds `gu/clifford.py`. Its Weyl/Ricci/scalar split seeds a test helper.

## 10. Environment and process

- Windows host, psmux. uv project with numpy, scipy, sympy and pytest; `python-flint` will be added when P2 needs it.
- Codex runs with Full Access, and Claude approves its commands.
- Commits go directly on `master` (user decision). Each experiment uses a pre-registration commit followed by a results commit, so a bad result reverts cleanly.
- Lean (elan) is installed only if P5 is scheduled.

## 11. Risks

- **Draft underdetermines a definition.** Mitigation: `[GU-recon]` with every alternative tested.
- **Common-mode library bugs.** Mitigation: positive controls and the oracle.
- **Exact linear algebra too slow.** Mitigation: flint or modular rank; reduce before solving.
- **Fable spend.** Mitigation: the §8 rules.
