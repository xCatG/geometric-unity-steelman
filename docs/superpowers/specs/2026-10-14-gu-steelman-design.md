# GU Steelman: Design Spec

Date: 2026-10-14 · Revision 4.1, after Codex adversarial review (with one independent subagent) and argon's final review · Status: draft for user review

## 1. Purpose

A personal deep-dive into Eric Weinstein's Geometric Unity, using the April 2021 draft. We give the theory the benefit of the doubt: find its gaps, propose the most charitable repairs, and test each repair with computation (and with Lean where that adds real confidence). Exploring is the goal; polish isn't. The deliverable is the gap register `docs/gaps/register.md`, whose entries end in verdicts backed by code.

**Non-goals:** validating GU as physics, quantization, deciding dynamical questions (unitarity, positivity of energy) by algebra alone. A passing algebraic check is reported as exactly that.

## 2. Claim discipline (two axes plus scope)

Every claim carries **one provenance tag, one evidence status and one scope**. This matches register §"Sources".

| Provenance | Meaning |
|---|---|
| `[GU-orig]` | Stated in the draft, with page or equation |
| `[GU-recon]` | Our reading of an ambiguous passage, with the alternatives listed |
| `[ext]` | Our repair or new assumption |
| `[lit]` | External source: S-id from `docs/gaps/sources/INDEX.md`, or until that exists the register's labels (NP, T, W, O) with page |

| Evidence status | Meaning |
|---|---|
| `verified:<path>` | Backed by a tracked script, test or proof under `experiments/`, `tests/` or `lean/`, with the command, its output and the source commit. Never under `.agent-handoff/`, which git ignores. |
| `unverified` | Everything else |

| Scope | Meaning |
|---|---|
| `counterexample` | One exact input on which the claim fails. Suffices to refute. |
| `sampled` | Exact passes on a finite, listed set of inputs. Never promoted to `holds`. |
| `identity` | Proved for all admissible inputs, symbolically or by a stated finite-determination argument (e.g. degree bound plus interpolation grid). |

A verified `[ext]` stays `[ext]`. Rules:
- Obstructions are stated "within ansatz X".
- X is committed to git before the run that tests it.
- Agreement between agents is not evidence.

## 3. Agents and roles

| Agent | Where | Owns |
|---|---|---|
| Claude (Opus 5.5) | pane 0:2 | Direction, spec and plans, repair design, review, independent transcriptions and re-derivations, write-ups. Orchestrates every task. |
| Codex (GPT-6-Astra) | pane 0:3 | Gap register, library, experiments, Lean, and literature/sources (`docs/gaps/sources/`). May spawn its own subagents, e.g. an independent reviewer or a source collector, when the brief allows. |
| Fable 5.1 | Claude subagent | Theory bottlenecks only, under the rules in §8 |

agy is not used (a tool update broke it). Handoffs follow tmux-agent-orchestration: `.agent-handoff/<task>/`, one writer per file.

### Verification protocol: replication, not just reproduction

Rerunning code checks reproducibility and the worker's execution claims, but it does not catch errors common to the algorithm. The weakest link is turning the PDF into code. So:

1. **Independent transcription.** Before any code exists for a GU formula, the agent *not* writing the code produces `experiments/<id>/transcription.md`, typed directly from the PDF with page and equation numbers. It covers every symbol's type, the conventions (bracket, phases, normalization, which invariant embeddings), and the alternatives tagged `[GU-recon]`. The implementer codes from the transcription. Any disagreement with their own reading is resolved in that file first.
2. **Positive controls.** Every engine, including the direct implementation of a GU formula, must first produce a known *nonzero* answer. Search or "nonexistence" engines must recover e.g. the Riemann→Ricci contraction or the known Spin(10) 16 branching. Only then does a zero result count.
3. **External oracle** for representation theory: published tables (Slansky 1981; Yamatsu's tables) or LiE run under WSL if it installs cleanly. The `gu` library's branching code must agree with the oracle on its test cases.
4. **Pre-registration.** Commit the ansatz and the expected-outcome criteria first. Commit the results in a later commit.
5. **Independent re-derivation of decisive results.** Before a verdict enters the register, the agent that did not implement it re-derives the decisive step by a different route (hand derivation, a different algorithm, or an oracle), not by rerunning the same script.

## 4. Repository layout (minimal; grows per experiment)

```
docs/gaps/                  register.md, sources/ (both Codex); notes/
docs/superpowers/           specs and plans (Claude)
docs/fable-ledger.md
gu/
  inertia.py    exact inertia of symmetric/Hermitian forms (Sylvester / LDLᵀ over ℚ or ℚ(i)). No floating-point signature claims.
  clifford.py   gamma matrices for any (p,q), exact Gaussian integers, monomial storage; chirality; the Dirac pairing A
  forms.py      exterior algebra on R^{p,q}; Hodge star defined by α∧★β = ⟨α,β⟩_η vol; the explicit Λ^{n-1} ≅ Λ¹ identification.
                Controls: e_I∧★e_I = η_II vol for every basis form; ★★ = (−1)^{k(n−k)+q} for k ∈ {0,1,2,7,13,14}, both (9,5) and (7,7)
  adjoint.py    the internal gauge algebra u(64,64) = {M : M†A + AM = 0}: membership predicate, Cayley elements, ℂl ≅ End(ℂ¹²⁸) ≅ ⊕Λᵏ
  curvature.py  algebraic curvature tensors: scalar / traceless-Ricci / Weyl split with one documented index convention
  reps.py       only when B03 needs it: weights and branching for D_n (Freudenthal), checked against the oracle
experiments/<gap-id>/       transcription.md, ansatz.md (pre-registered), run script, result.json, README with the verdict
tests/                      pytest: textbook facts, positive controls, oracle agreement
lean/                       only when a Lean task is scheduled
```

Dropped as YAGNI: a general `dewitt.py` (B01 lives in `experiments/B01/`) and a generic `equivariant.py` (the intertwiner search is a fallback, §5). Deferred to P3, off the B02 critical path: charge conjugation and Majorana tests, the Rarita–Schwinger projector, `reps.py`.

**Two groups, kept apart.** The *geometric* group Spin(p,q) acts on form indices and, through Clifford multiplication, on spinors. The *internal gauge* group U(64,64) is defined by the pairing A. They are not interchangeable: e.g. γ_sγ_t (one spacelike, one timelike unit vector) satisfies hA = −Ah, so h†Ah = −A and h ∉ U(64,64), for every q. Dressed gauge identities are tested only on h with h†Ah = A.

**The pairing A.** A is built from the product of the q timelike gammas, times a phase so that A† = A. That product is already Hermitian for q = 7 but anti-Hermitian for q = 5, which needs a factor of i. Controls: A† = A, and A has exact inertia (64,64).

`gu/clifford.py` stores gamma matrices as monomial matrices (a permutation plus a ℤ₄ phase), the representation from argon_update.md, with its broken assert removed. When P3 adds the Rarita–Schwinger projector P^a_b = δ^a_b − (1/d)Γ^aΓ_b (indices raised and lowered consistently), its controls are, all in integers:
- (dP)² = d(dP)
- Γ_a P^a_b = 0
- tr P = (d−1)·2^{d/2}, i.e. 1664 on the full Dirac module for d = 14 and 832 on one chirality

Exact arithmetic means sympy and integer matrices for small objects. python-flint has no Gaussian-integer matrix type, so a + ib is embedded as the real block [[a,−b],[b,a]], and complex rank = real rank / 2. For exact rank and nullspace at size 10³ or more, use `python-flint`, or modular rank at several random primes followed by rational reconstruction.

## 5. Technical approach

Each question splits into three layers:
1. **Complex-algebraic data.** This is the same for every signature (weights, characters, complex Hom counts).
2. **Real-form data**, which depends on the signature:
   - **Counting real intertwiners.** For real representations V, W: Hom_G(V,W) ⊗_ℝ ℂ = Hom(V_ℂ, W_ℂ), so dim_ℝ Hom_G(V,W) equals the complex count, with no extra factor. The Schur factors 1/2/4 appear only when decomposing into *real* irreducibles U and summing (multiplicity products) × dim_ℝ End_G(U). Each experiment states which method it uses, never mixes them, and checks one real-, one complex- and one quaternionic-type example first. p−q mod 8 classifies spinor reality, not every tensor irrep.
   - **Spinor reality.** For (7,7), p−q ≡ 0 mod 8: real, Majorana–Weyl. For (9,5), p−q ≡ 4 mod 8: quaternionic, i.e. an antilinear J with J² = −1 on each Weyl module, giving symplectic-Majorana–Weyl structure, not a fixed-point condition Jψ = ψ.
   - **Components.** "Spin(p,q) has two components" depends on the definition (norm-one cover of SO⁺ versus the even-Clifford cover of all of SO). Each experiment fixes its definition. Lie-algebra equivariance covers only the identity component. A non-identity geometric element acts on form indices, the pairing and the Clifford identification; any test of it states that action and is not a U(64,64) test. If the gauge/dressing domain is extended to include such elements, that is an `[ext]` variant.
   - ★ is SO-equivariant, not O-equivariant. On Λ⁷, ★² = (−1)^{49+q} = +1 for both q = 7 and q = 5, so self-dual splitting of Λ⁷ does not distinguish the two signatures.
3. **Dynamical residue:** kinetic signs, unitarity (B04). Out of scope for algebraic verdicts; recorded as open.

B01 (the inertia of a quadratic form on T⊕Sym²) is none of these layers. It is plain exact linear algebra. Its fiberwise object is V ⊕ H* over Y; P1 makes no claim of a canonical global tangent splitting, and it reports the horizontal/vertical sign choices and the degenerate boundary rather than one "selected" signature.

### B02: a direct check of (9.3), not a search

**Known in advance (scope: identity).** Weyl curvature has D7 highest weight (2,2,0,…,0). Every irreducible constituent of ΛᵏV has highest-weight coordinates in {−1,0,1}, and tensoring with the minuscule V shifts one coordinate by ±1, so at most one coordinate can reach 2. Hence Hom_Spin(14)(Weyl, V ⊗ ΛᵏV) = 0 for all k, and hence into V ⊗ ℂl(14). Any undressed equivariant map annihilates Weyl, *including the zero map*. Weyl annihilation therefore discriminates nothing on its own; everything discriminating lives in the nonzero scalar and Ricci responses and in the dressing. (Independently derived by Claude and by Codex's subagent; to be recorded in register B02 with `experiments/B02/` evidence.)

Transcribe (9.3) independently: bracket conventions, phases, normalization, which invariant Φ embeddings. Implement it on u(64,64)-valued forms; everything is a 128×128 matrix. Then test, in order:

1. **Form degree.**
2. **Real form:** the image stays in u(64,64). Only commutators of u(64,64) elements stay in u(64,64); raw Clifford products and anticommutators land in i·u(64,64), and grades differ by factors of i. The transcription records, as `[GU-recon]` branches where unclear, whether (9.3) uses a bracket, i·anticommutator, or raw product followed by the projection M ↦ ½(M − A⁻¹M†A).
3. **Dressed gauge covariance** `Shiab_(εh)(h⁻¹ηh) = h⁻¹ Shiab_ε(η) h` for h with h†Ah = A.
   - *Primary, scope identity:* derive it symbolically from conjugation of each dressed Φ, matrix products and brackets, and ★ acting only on form indices. Claude writes the derivation; Codex checks it independently (§3 step 5).
   - *Regression, scope sampled:* exact Cayley elements h = (I−X)(I+X)⁻¹ of A-skew X over ℚ(i). Require det(I+X) ≠ 0; if singular (the unit boost already is), rescale X by a rational or resample, and log the rejection separately from operator failures.
   - If an infinitesimal form is used, it is the two-term Leibniz identity `D_ε Shiab[εX](η) + Shiab_ε([η,X]) = [Shiab_ε(η), X]`. With the Cayley parameterization, the generator at 0 is −2X, used on both sides. Passing it on a generating set is sampled scope unless the passage to the connected group is argued.
4. **Geometric Spin(p,q) equivariance of the undressed tensors**, checked separately. Dressing can make test 3 hold for any underlying linear map, even a geometrically wrong one. Since the undressed map L is linear and commuting with X, Y implies commuting with [X,Y], exact commutation with the 13 adjacent generators J_{a,a+1} on a basis of the input space proves Lie-algebra equivariance (scope identity, identity component only). This shortcut does not apply to the dressed group identity in test 3.
5. **Curvature response, the exit gate.** On certified pure-sector inputs from `gu/curvature.py` (Levi-Civita-induced subspace only):
   - scalar and traceless-Ricci inputs must give *nonzero*, candidate-specific outputs matching the transcribed response, with normalization and relative coefficient stated or explicitly marked unresolved;
   - Weyl inputs give zero, as a consistency check only;
   - with nontrivial dressing, covariance transports the Weyl subspace to Ad(ε⁻¹)·Weyl; the test uses that subspace, not a fixed undressed one. Shiab_ε(ε⁻¹Wε) = ε⁻¹Shiab₁(W)ε = 0 follows from tests 3 and 5, so it is a regression check, not new evidence;
   - **open data, no expected outcome:** Shiab_ε(W) for undressed geometric W and ε ∈ U(64,64) outside the image of Spin(p,q). Record whether it vanishes; no physical interpretation is drawn in P2.

**Generating sets, never full bases.** u(64,64) has real dimension 16384, so its basis is never materialized; elements are Gaussian-integer matrices tested by M†A + AM = 0. No bracket-closure dimension certificate is computed. Where a generating claim is needed, prove that a small standard generating set (including the central iI) generates, by hand.

**Signature is a runtime parameter.** `(p,q)` is taken from B01's outcome, never hard-coded. Run B02 for (7,7) and for (9,5).

Only if (9.3) fails do we search for alternatives. That search counts Hom with characters first (by the real-form rule above), uses ★ to turn Λ¹³ into Λ¹, splits ad as ⊕Λᵏ, and applies the pre-registered constraints (degree, dressing, nonzero Ricci response) before solving anything. The full space is about 3×10¹¹ entries, so we never solve it unreduced.

## 6. Gap lifecycle

`open → transcribed → ansatz-registered → checked → {holds | obstructed-within-X | repaired [ext] | unresolved}`. Each verdict links its experiment directory and states its scope (§2). `holds` requires scope `identity`; a `sampled` pass is reported as such.

## 7. Phases

| Phase | Content | Exit criterion |
|---|---|---|
| P0 ✅ | Gap register (Codex) | Done; register committed |
| P1 | **B01 now.** Claude independently transcribes GU (3.8)–(3.10), p. 19, and §3.5, p. 22. Codex moves the probe into `experiments/B01/` and switches to exact inertia. Reconcile the λ family (a `[GU-recon]`/`[ext]` parameterization, not a draft parameter) with the transcription. | Convention map or exact mismatch, `verified:experiments/B01/…`; register links repointed |
| P2 | Minimal library for B02 (inertia, clifford with A, forms, adjoint, curvature) with tests and positive controls; then the B02 direct check | Verdict with scope on each test 1–5, within the transcribed conventions; test 5 nonzero responses required for `holds` |
| P3 | B03: branching of the chiral spinor and of the gamma-traceless vector-spinor under Spin(7,7) → Spin(1,3)×Spin(6,4) (and the (9,5) analog), tracking chirality and reality, with a mirror-sector inventory. Adds charge conjugation, RS projector, `reps.py`. | **Branching table only, within ansatz X.** No claim about light generations. |
| P4 | Repairs: `[ext]` on obstructed entries; Fable under the §8 rules | Time box: at most 2 repair attempts per entry before marking it unresolved |
| P5 (optional) | Lean for 1–2 statements that their definitions don't directly encode, e.g. the Clifford relations of the explicit matrices | `lake build` |
| P6 | Write-up | All three axes tagged |

Later, picked from the register: B05 anomalies (14D and 4D), B07 variational equations, B09 observation and closure. Sources are collected by Codex when an entry needs them.

## 8. Fable rules ($20 cap)

- **Escalation trigger:** an entry is obstructed or unresolved after the pre-registered ansatz, plus one cheap variant by Claude or Codex, *and* the bottleneck is a derivation or construction, not a computation.
- **Fixed context pack per call:** the transcription, the ansatz, the result.json, and the relevant register entry. The PDF and the whole register are not included. Input cap about 40k tokens; hard `max_tokens` on output; no automatic retries.
- **Reserve before dispatch.** Each call's maximum billable cost = input tokens × input rate + max_tokens × output rate (thinking tokens count as output), at the endpoint's actual rates; at $10/$50 per MTok that is ≤ $0.40 + $1.50 ≈ $2. Dispatch only if spent + this maximum ≤ $20. Record actual usage in `docs/fable-ledger.md`. Announce each call to the user before making it.
- Fable output is `[ext] unverified` until it passes the ordinary experiment gate.

## 9. Known traps (forbidden in briefs)

These come from the review of `argon.md`, LLM-generated scaffolding that looks like computation:
- **Uncited filter directions.** Example: GU's Shiab is claimed (register B02) to annihilate Weyl-type curvature, so a filter that *rejects* Weyl-annihilating candidates, as argon.md has, inverts it. Every filter direction cites a draft page.
- **Vacuous acceptance.** A test the zero operator passes is not a gate (see B02: Weyl annihilation is automatic).
- **Invented background objects** (e.g. a "canonical 3-form T"). Each input is `[GU-orig]` with a page, or `[ext]` with a reason.
- **Postulated conclusions.** Writing the target term, e.g. a Higgs potential, as a symbol and then "deriving" from it.
- **Lean theorems true by definition.**
- **Unused machinery reported as a search.** Every listed candidate is evaluated; every claimed filter is computed.
- **Riemann symmetries imposed on gauge curvature.** A gauge field strength is only a 2-form obeying the differential Bianchi identity. Weyl-type tests use the Levi-Civita-induced subspace only.
- **Mixing geometric and gauge groups** (§4): a geometric Spin element is not automatically a gauge transformation.
- **Chirality bookkeeping.** In 4D, rewriting a right-handed 16̄ as a left-handed 16 does *not* let it cancel against another left-handed 16. Anomalies cancel only across species whose contributions genuinely have opposite signs.

`argon.md` Agent 1 (the Clifford (9,5) construction, checked exact) seeds `gu/clifford.py`. argon's Weyl/Ricci/scalar split is **not** reused as is: its contraction and reconstruction use opposite signs, so it returns W = 2R on constant-curvature input. `gu/curvature.py` fixes one convention and must pass, before use: exact reconstruction R = W + Ricci part + scalar part; W traceless; algebraic curvature symmetries and first Bianchi preserved; pure scalar, traceless-Ricci and Weyl controls; component dimensions 1 + 104 + 3080 = 3185 at d = 14.

## 10. Environment and process

- Windows host, psmux. uv project with numpy, scipy, sympy and pytest; `python-flint` will be added when P2 needs it.
- Codex runs with Full Access, and Claude approves its commands.
- Commits go directly on `master` (user decision). Each experiment uses a pre-registration commit followed by a results commit, so a bad result reverts cleanly.
- Lean (elan) is installed only if P5 is scheduled.

## 11. Risks

- **Draft underdetermines a definition.** Mitigation: `[GU-recon]` with every alternative tested.
- **Common-mode library bugs.** Mitigation: positive controls, the oracle, independent re-derivation.
- **False success from samples.** Mitigation: the scope axis; `holds` needs `identity`.
- **Exact linear algebra too slow.** Mitigation: flint or modular rank; reduce before solving.
- **Fable spend.** Mitigation: the §8 reservation rule.
