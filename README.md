# Geometric Unity: a steelman check of the 2021 draft

This repository holds an attempt to take Eric Weinstein's *Geometric Unity* (GU), in its April 1, 2021 "Author's Working Draft", at its strongest reading and then check its central claims with exact computation and, where it fit, Lean 4 proofs. AI coding agents did the work over October 14–25, 2026, directed by Yenchi Lin: Claude Opus 5.5 orchestrated, Codex (GPT-6 Astra) executed and re-derived, Grok 4.7 reviewed, and Gemini 4 Argon proposed ideas.

**What this is not.** It is not peer-reviewed physics, and no physicist has reviewed it. It does not prove or disprove GU. Every verdict is scoped to a pinned reading of the draft, at stated dimensions and signatures. Readings we did not test remain open.

## Results

| The draft's claim | What we checked | Verdict |
|---|---|---|
| The 14D metric has the signature the draft says (B01) | The signature of the metric on the 14D space, computed exactly | **Holds.** The draft leaves two signature options open, and nothing in the algebra picks one |
| The Shiab operator turns curvature into Einstein's tensor (B02) | The eight bracket choices in the displayed operator, within a pinned choice of its inputs, in 4D and 14D | **The literal reading fails.** Its scalar term is identically zero, so it gives Ricci curvature, not Einstein's tensor. A reconstructed reading (CAA) does produce Einstein's shape, algebraically |
| 14D spinors split into the Standard Model's fermions (B03) | The full 1,920-dimensional space, split exactly | **The splitting identities hold** under a pinned dictionary. Three generations as dynamics are not established |
| The matter (Dirac) operator is well defined (B05) | What the draft actually specifies | **Under-specified.** Lean checks that two printed signs in the transformation law can't both hold, in an algebraic model of it |
| The action (9.4) varies to the printed field equation (9.7) (B07) | A repaired reading of the action, varied with the metric held fixed; then the full 40-dimensional symmetric operator space on a flat 4D model | **Fails for every nonzero operator** in the searched space. Follow-ups on non-Einstein channels (E1, E2) and the torsion sector (option C) found no Einstein–Hilbert action |

Start with each experiment's README:

- [`experiments/B01/`](experiments/B01/README.md), [`B02/`](experiments/B02/README.md), [`B03/`](experiments/B03/README.md), [`B05/`](experiments/B05/README.md)
- [`experiments/B07/`](experiments/B07/README.md), then [`phase2/`](experiments/B07/phase2/README.md), [`escape/`](experiments/B07/escape/README.md) and [`optionc/`](experiments/B07/optionc/README.md)
- [`docs/gaps/register.md`](docs/gaps/register.md): the gap register B01–B12, with the status of each entry
- [`lean/COVERAGE.md`](lean/COVERAGE.md): what the Lean proofs cover, and what they don't

## How the checks were run

The rules are in [`docs/methods.md`](docs/methods.md). In short:

- **Expected results were written down first.** Each experiment has a design and plan in [`docs/superpowers/`](docs/superpowers/), written and reviewed before the code ran.
- **Exact arithmetic only.** Integers, rationals, Gaussian rationals and algebraic numbers; no floating-point tolerances on any claim.
- **Seeded faults.** Copies of the code with one deliberate bug each had to turn the tests red.
- **Independent re-derivation.** A separate agent session rebuilt each major calculation from the written formulas.
- **Clean-clone reruns.** The results were reproduced from a fresh clone, and the scientific output was compared exactly.

## Running it

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
uv run pytest -q                              # 421 tests, about 15 min
uv run python -m experiments.B07.optionc.run  # one runner, about 22 min
```

The code is single-process, exact and slow. Recorded runtimes on an AMD 5950X:

| Runner | Time |
|---|---:|
| `experiments.B07.run` | about 1.5–2 h |
| `experiments.B07.phase2.run` | about 70–85 min |
| `experiments.B07.optionc.run` | about 22 min |
| `experiments.B07.escape.run`, `run14` | about 4 min, 2 min |

Each runner writes the `result.json` next to it. The committed copies are the official runs. They differ from a rerun only in the `seconds` and `source_commit` fields.

The Lean 4 proofs (`lean/`, Lean 4.24.0 with Mathlib) build with `lake build` from `lean/`. The first build downloads and compiles Mathlib, which takes several GB.

## Reading the records

- `docs/HANDOFF.md` is the project's working log, kept for agents resuming after a context reset. It mentions tmux panes and agent sessions; it is history, not documentation.
- Paths written as `notes:<task>/…` point to the agents' working notes (briefs, raw logs, reviews). They aren't published. Every claim relies on tracked files only.
- `argon*.md` files are Gemini 4 Argon's pasted proposals. They were inputs to verify, not authorities, and aren't included.
- [`overview.md`](overview.md) is the original starting prompt. The plan changed considerably after it.

The draft itself is not included. The SHA-256 of the PDF used is `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.

## License

MIT; see [LICENSE](LICENSE).
