# GU Steelman: Design Spec

Date: 2026-10-14 · Status: draft for user review

## 1. Purpose

A personal deep-dive into Eric Weinstein's Geometric Unity, using the April 2021 draft. We give the theory the benefit of the doubt: find its gaps, propose the most charitable repairs, and test each repair with computation (and with Lean where that adds real confidence). Exploring is the goal; polish isn't. The deliverable is a living **gap register** whose entries end in a verdict backed by code.

**Non-goals:** validating GU as physics, quantization, publication-grade rigor. A passing algebraic check is reported as exactly that.

## 2. Claim discipline

Every claim in the register, the notes and the write-ups carries exactly one tag:

| Tag | Meaning |
|---|---|
| `[GU-orig]` | Stated in the draft, with page or section |
| `[GU-recon]` | Our reading of an ambiguous passage, with the alternatives listed |
| `[ext]` | Our proposed repair or extension of GU |
| `[verified]` | Backed by a script, test or proof in the repo, with its path |
| `[lit]` | External source, cited by S-id from `docs/gaps/sources/INDEX.md` |

Rules:
- Steelmanning may change GU's assumptions, but only under `[ext]`.
- An obstruction is always stated as "within ansatz X". X is fixed before the search runs.
- Agreement between agents is not evidence.

## 3. Agents and roles

| Agent | Where | Owns |
|---|---|---|
| Claude (Opus 5.5) | pane 0:2 | Direction, this spec and the plans, repair design, review and cross-checks, write-ups. Orchestrates every task. |
| Codex (GPT-6-Astra) | pane 0:3 | Gap register, exact computations, implementation, Lean |
| agy (Gemini 3.8 Flash) | pane 0:4 | Literature: source collection, `docs/gaps/sources/`, citation lookups. No claims. |
| Fable 5.1 | Claude subagent | Sharply framed theory bottlenecks only. **$20 cap**, about 8 calls. Each call is announced to the user first and logged in `docs/fable-ledger.md`. |

Handoffs follow tmux-agent-orchestration: `.agent-handoff/<task>/` with task.md, status, result.md and evidence/; the directory is git-excluded. One writer per file. For a decisive result (signature, Shiab typing, branching), the agent that didn't produce it re-derives it independently.

## 4. Repository layout

```
docs/
  gaps/register.md            gap register (Codex)
  gaps/notes/<id>.md          per-entry working notes
  gaps/sources/               PDFs and INDEX.md (agy)
  superpowers/specs|plans/    design and plans (Claude)
  fable-ledger.md             Fable calls: framing, tokens, cost, outcome
gu/                           reusable library (Python 3.12, uv)
  clifford.py    gamma matrices for any (p,q); chirality; charge conjugation and Dirac conjugation; reality and Majorana tests
  forms.py       exterior algebra on R^{p,q}: wedge, contraction, Hodge star with the correct sign of ★²
  dewitt.py      DeWitt supermetric family G_λ on Sym²(R^{p,q}); signature as a function of λ
  lie.py         so(p,q) generators in the vector, adjoint, Λ^k, spinor and tensor-product representations
  equivariant.py dimension of Hom_G(V, W) via weights/characters; explicit intertwiners via nullspace solves on decomposed blocks
experiments/<gap-id>/         one script per check, writing result.json and a README with the verdict
tests/                        pytest; the library is tested against textbook facts
lean/                         added only when a Lean task is scheduled
```

Library first: the experiments import `gu`. Nothing in `gu/` is specific to GU. It is standard linear algebra and representation theory and can be tested on its own.

## 5. Core technical approach

- **Exact over numeric.** Gamma matrices are built as tensor products of Pauli matrices, so every entry is in {0, ±1, ±i}. Use integer and Gaussian-integer arithmetic where possible. Floating point is allowed only for eigenvalue-sign checks that have a stated margin.
- **Equivariance engine.** Nonzero Spin-equivariant maps V → W exist exactly when V and W share an irreducible representation. Count them with weight multisets first, which is cheap. Construct them explicitly only on the shared irreducible blocks, so we never solve over the full space. For example, Λ²⊗ad into Λ¹³⊗ad would otherwise be a matrix with about 10⁷ unknowns.
- **Signature lives in the real form.** The complexified so(p+q) is the same for every signature. So the signature question becomes concrete in three places:
  - the sign of ★² and the reality of Hodge duality,
  - reality and Majorana conditions on spinors,
  - whether the map we find commutes with the real structure.
  
  This is where we expect the Shiab and complexification gaps to be decided, and where the main `[ext]` repairs will be tried.

## 6. Gap lifecycle

`open → check-designed → checked → {holds | obstructed-within-X | repaired [ext] | unresolved}`. Each verdict links its experiment and test. Obstructed entries may go to Fable if a cheap ansatz change doesn't resolve them.

## 7. Phases

| Phase | Content | Exit criterion |
|---|---|---|
| P0 (running) | Source collection (agy) and gap register (Codex) | Register reviewed by Claude; top-3 checks agreed |
| P1 | `gu/` library and tests: clifford, forms, dewitt, lie, equivariant | Tests pass against known facts: Cl(p,q) table, Majorana-Weyl existence for p−q mod 8, ★² sign, DeWitt signature for Riemannian metrics, dim so(n), spinor branching of Spin(10) |
| P2 | Experiments for priorities 1–3: signature, Shiab typing and real form, fermion branching and generations | Each has a verdict in the register, cross-checked by the other agent |
| P3 | Repairs: `[ext]` attempts on obstructed entries; Fable where reasoning is the bottleneck | Ledger ≤ $20; each attempt has a verdict |
| P4 (optional) | Lean for one or two crisp finite facts, e.g. the signature and the Clifford relations, if worth it | `lake build` passes |
| P5 | Write-up of findings for the user | Claims tagged, links to experiments |

Later candidates, picked from the register: anomalies (cubic traces, global SU(2), 14D chiral anomaly), Higgs from Gauss–Codazzi, invariance of the inhomogeneous gauge group's action.

## 8. Environment

Windows host, psmux tmux, uv project with numpy, scipy, sympy and pytest. Codex's default shell is broken: it runs in Full Access mode, and Claude may approve its commands. Work is committed directly on `master`. Lean (elan) is installed only when P4 is scheduled.

## 9. Risks

- **Source ambiguity.** The draft may underdetermine a definition. Mitigation: `[GU-recon]` with all alternatives tried.
- **Combinatorial size.** Mitigation: irreducible-block decomposition before solving.
- **Agents' claims drifting from evidence.** Mitigation: the claim tags, cross-checks, and Claude rerunning decisive checks.
- **Fable spend.** Mitigation: the ledger and announcing each call first.
