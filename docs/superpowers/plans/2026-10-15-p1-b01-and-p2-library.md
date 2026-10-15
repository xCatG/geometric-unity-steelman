# P1 (B01) and P2 Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. In this project, code tasks are executed by Codex (pane 0:3) through `.agent-handoff/<task>/` briefs. Claude owns the transcription, reconciliation and review tasks.

**Goal:** Settle B01 (the inertia of the chimeric metric, reconciled with the April 2021 draft) and build the exact-arithmetic library that B02 needs: inertia, Clifford with the Dirac pairing A, forms, curvature and the u(64,64) adjoint. The plan ends with the B02 transcription and pre-registration. A follow-up plan implements the B02 check itself, because that code depends on the transcription.

**Architecture:** A small `gu/` package of exact-arithmetic modules: sympy for small symbolic objects, monomial integer arrays for gamma matrices, and python-flint `fmpq_mat` with a real 2×2 block embedding for dense 128×128 complex work. Each experiment lives in `experiments/<id>/` with its own transcription, pre-registered ansatz, script, result.json and README. Tests in `tests/` carry the textbook facts and positive controls.

**Tech Stack:** Python 3.14 via uv; numpy, scipy, sympy 1.14, python-flint 0.9.0, pytest.

**Spec:** `docs/superpowers/specs/2026-10-14-gu-steelman-design.md` (rev 4.1, approved). Read it before any task.

## Global Constraints

- Exact arithmetic only. No floating-point signature, rank or equality claims (spec §4).
- `verified:<path>` points only into tracked `experiments/`, `tests/` or `lean/`; never `.agent-handoff/` (spec §2).
- Every claim carries provenance, evidence status and scope (`counterexample` / `sampled` / `identity`); `holds` requires `identity` (spec §2, §6).
- `(p,q)` is a parameter; library code never hard-codes (7,7) or (9,5) (spec §5).
- The geometric Spin(p,q) and the internal gauge group U(64,64) are kept apart; dressed gauge identities use only h with h†Ah = A (spec §4).
- Pre-registration: commit `ansatz.md` before the commit containing results (spec §3.4, §10).
- Commits go directly on `master`. Commit messages end with the `Co-Authored-By` line of the agent that made the commit.
- Ownership: Codex writes `gu/`, `tests/`, experiment code and `docs/gaps/register.md`. Claude writes `transcription.md`, the reconciliation README and the spec and plans. Neither edits the other's files; disagreements go to the handoff `result.md`.
- When an expected value in a test fails, stop and report it. Never edit the expected value to make the test pass.

## Review Focus

- **A Hermitian matrix whose diagonal is entirely zero partway through elimination** (e.g. [[0,0,0],[0,0,1],[0,1,0]]): inertia must still be exact. The test is in Task 1.
- **Floats sneaking into exact code** (e.g. `0.25` instead of `Rational(1,4)` for λ): must raise, not silently round. The test is in Task 1.
- **The degenerate boundary λ = 1/4:** must report a zero eigenvalue rather than drop it. The test is in Task 2.
- **q = 0 or a timelike-free signature:** A = I has no (64,64) inertia; tests must not assume it does. The test is in Task 5.
- **A singular Cayley denominator** (the unit boost): must raise `SingularCayley`, never return a matrix or count as an operator failure. The test is in Task 8.

---

### Task 1: Package setup and exact inertia (`gu/inertia.py`) — Codex

**Files:**
- Modify: `pyproject.toml` (add python-flint and the pytest config)
- Create: `gu/__init__.py` (empty), `experiments/__init__.py` (empty), `gu/inertia.py`
- Test: `tests/test_inertia.py`

**Interfaces:**
- Produces: `gu.inertia.inertia(M) -> tuple[int, int, int]`, which returns `(n_pos, n_neg, n_zero)` for a square Hermitian sympy-compatible matrix with entries in ℚ(i). It raises `ValueError` on non-square, non-Hermitian or non-exact input.

- [ ] **Step 1: Set up the project**

Run: `uv add python-flint==0.9.0`

Append to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
```

Create empty `gu/__init__.py` and `experiments/__init__.py`.

- [ ] **Step 2: Write the failing tests**

```python
# tests/test_inertia.py
import pytest
import sympy as sp

from gu.inertia import inertia


def test_diagonal():
    assert inertia(sp.diag(1, -1, 0, 3)) == (2, 1, 1)


def test_all_zero():
    assert inertia(sp.zeros(3)) == (0, 0, 3)


def test_zero_diagonal_needs_off_diagonal_pivot():
    assert inertia(sp.Matrix([[0, 1], [1, 0]])) == (1, 1, 0)


def test_zero_diagonal_with_null_row():
    assert inertia(sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])) == (1, 1, 1)


def test_hermitian_complex_offdiagonal():
    assert inertia(sp.Matrix([[0, sp.I], [-sp.I, 0]])) == (1, 1, 0)


def test_real_congruence_invariance():
    D = sp.diag(3, -2, 0, 5, -1)
    P = sp.Matrix([[1, 2, 0, -1, 1],
                   [0, 1, 3, 0, 0],
                   [0, 0, 1, -1, 4],
                   [0, 0, 0, 1, 2],
                   [0, 0, 0, 0, 1]])
    P = P.T * P.permute([4, 2, 0, 1, 3])  # mix rows; still invertible
    assert P.det() != 0
    assert inertia(P * D * P.T) == (2, 2, 1)


def test_complex_congruence_invariance():
    D = sp.diag(1, -1, 0)
    P = sp.Matrix([[1, sp.I, 0], [0, 1, 2 - sp.I], [0, 0, 1]])
    assert inertia((P * D * P.H).applyfunc(sp.expand)) == (1, 1, 1)


def test_rational_entries():
    assert inertia(sp.Matrix([[sp.Rational(1, 3), 0], [0, sp.Rational(-2, 7)]])) == (1, 1, 0)


def test_accepts_unexpanded_gaussian_expressions():
    z = (1 + sp.I) ** 2  # = 2i
    assert inertia(sp.Matrix([[0, z], [sp.conjugate(z), 0]])) == (1, 1, 0)


def test_rejects_float():
    with pytest.raises(ValueError):
        inertia(sp.Matrix([[0.5]]))


def test_rejects_non_hermitian():
    with pytest.raises(ValueError):
        inertia(sp.Matrix([[1, 2], [3, 4]]))


def test_rejects_non_square():
    with pytest.raises(ValueError):
        inertia(sp.Matrix([[1, 2]]))
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `uv run pytest tests/test_inertia.py -v`
Expected: collection error, `ModuleNotFoundError: No module named 'gu.inertia'`.

- [ ] **Step 4: Implement**

```python
# gu/inertia.py
"""Exact inertia of Hermitian matrices over QQ(i).

Hermitian congruence (symmetric Gaussian elimination) with sympy. Sylvester's
law of inertia makes the result independent of pivot order. No floating point.
"""
from __future__ import annotations

import sympy as sp


def _is_zero(x) -> bool:
    return sp.expand(x) == 0


def _check_exact(M: sp.Matrix) -> None:
    for e in M:
        re, im = sp.re(e), sp.im(e)
        if not (re.is_Rational and im.is_Rational):
            raise ValueError(f"inertia() needs entries in QQ(i), got {e!r}")


def inertia(M) -> tuple[int, int, int]:
    """Return (n_pos, n_neg, n_zero) of a Hermitian matrix with entries in QQ(i)."""
    M = sp.Matrix(M).applyfunc(sp.expand)  # unexpanded QQ(i) expressions like (1+I)**2 confuse sp.im
    if M.rows != M.cols:
        raise ValueError("matrix must be square")
    _check_exact(M)
    if not (M - M.H).applyfunc(sp.expand).is_zero_matrix:
        raise ValueError("matrix must be Hermitian")

    pos = neg = 0
    while M.rows:
        n = M.rows
        k = next((i for i in range(n) if not _is_zero(M[i, i])), None)
        if k is None:
            off = next(((i, j) for i in range(n) for j in range(n)
                        if i != j and not _is_zero(M[i, j])), None)
            if off is None:
                return pos, neg, n
            i, j = off
            # Add conj(M[j,i]) * row j to row i (and the conjugate on columns):
            # the new (i,i) entry is 2|M[j,i]|^2 > 0.
            P = sp.eye(n)
            P[i, j] = sp.conjugate(M[j, i])
            M = (P * M * P.H).applyfunc(sp.expand)
            k = i
        d = sp.re(M[k, k])
        if d > 0:
            pos += 1
        else:
            neg += 1
        rest = [r for r in range(n) if r != k]
        v = M.extract(rest, [k])
        M = (M.extract(rest, rest) - v * v.H / d).applyfunc(sp.expand)
    return pos, neg, 0
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `uv run pytest tests/test_inertia.py -v`
Expected: 12 passed.

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml uv.lock gu/__init__.py experiments/__init__.py gu/inertia.py tests/test_inertia.py
git commit -m "Add exact Hermitian inertia (gu/inertia.py) and python-flint"
```

---

### Task 2: B01 pre-registration and the exact DeWitt-family experiment — Codex

**Files:**
- Create: `experiments/B01/__init__.py` (empty), `experiments/B01/ansatz.md`, `experiments/B01/dewitt_family.py`, `experiments/B01/result.json` (generated)
- Test: `tests/test_b01.py`

**Interfaces:**
- Consumes: `gu.inertia.inertia`
- Produces: `experiments.B01.dewitt_family` with `ETA`, `LAM`, `vertical_gram(lam) -> sp.Matrix` (10×10), `chimeric_gram(lam, h_sign, v_sign) -> sp.Matrix` (14×14), `run(lams) -> dict`. Running `uv run python -m experiments.B01.dewitt_family` writes `experiments/B01/result.json`.

- [ ] **Step 1: Write and commit the pre-registration on its own**

```markdown
<!-- experiments/B01/ansatz.md -->
# B01 ansatz (pre-registered)

Provenance: [ext] parameterization; [GU-recon] until reconciled with GU (3.8)–(3.10), p. 19, and §3.5, p. 22.

**Family.** On X = R^{1,3}, η = diag(1,−1,−1,−1). Vertical fibre Sym²(R⁴) with
B_λ(H,K) = tr(ηHηK) − λ tr(ηH) tr(ηK). Chimeric form on R⁴ ⊕ Sym²: s_H·η ⊕ s_V·B_λ, with s_H, s_V ∈ {±1}.

**Claims to check exactly (expected outcomes):**
1. Eigenvalues of B_λ in the basis {E_ij + E_ji}: −2 (×3), 2 (×3), 1 (×3), 1−4λ (×1).
2. Vertical inertia: (7,3,0) for λ < 1/4; (6,3,1) at λ = 1/4; (6,4,0) for λ > 1/4.
3. Chimeric inertia at λ ∈ {0, 1/4, 1}: the table in tests/test_b01.py, taken from the earlier float probe and now required to hold exactly.

**Reconciliation criterion (Task 4).** "Match" means: the draft's metric on V ⊕ H* equals s_H·η ⊕ s_V·B_λ for some λ and signs, up to a positive rescaling of each summand, under an explicit map of the draft's symbols to ours. Anything else is reported as a documented mismatch. Neither outcome selects a physical signature.

Scope of claims 1–3: identity (exact, all λ via the symbolic eigenvalues; the table at listed λ).
```

```bash
git add experiments/B01/ansatz.md
git commit -m "B01: pre-register DeWitt-family ansatz and reconciliation criterion"
```

- [ ] **Step 2: Write the failing tests**

```python
# tests/test_b01.py
import pytest
import sympy as sp

from experiments.B01.dewitt_family import LAM, chimeric_gram, run, vertical_gram
from gu.inertia import inertia

R = sp.Rational


def test_vertical_eigenvalues_symbolic():
    assert vertical_gram(LAM).eigenvals() == {-2: 3, 2: 3, 1: 3, 1 - 4 * LAM: 1}


@pytest.mark.parametrize("lam,expected", [
    (R(-1), (7, 3, 0)), (R(0), (7, 3, 0)), (R(1, 8), (7, 3, 0)),
    (R(1, 4), (6, 3, 1)),
    (R(1, 2), (6, 4, 0)), (R(1), (6, 4, 0)),
])
def test_vertical_inertia(lam, expected):
    assert inertia(vertical_gram(lam)) == expected


CHIMERIC = {
    (R(0), 1, 1): (8, 6, 0), (R(0), 1, -1): (4, 10, 0),
    (R(0), -1, 1): (10, 4, 0), (R(0), -1, -1): (6, 8, 0),
    (R(1, 4), 1, 1): (7, 6, 1), (R(1, 4), 1, -1): (4, 9, 1),
    (R(1, 4), -1, 1): (9, 4, 1), (R(1, 4), -1, -1): (6, 7, 1),
    (R(1), 1, 1): (7, 7, 0), (R(1), 1, -1): (5, 9, 0),
    (R(1), -1, 1): (9, 5, 0), (R(1), -1, -1): (7, 7, 0),
}


@pytest.mark.parametrize("key", sorted(CHIMERIC, key=str))
def test_chimeric_inertia(key):
    lam, hs, vs = key
    assert inertia(chimeric_gram(lam, hs, vs)) == CHIMERIC[key]


def test_rejects_float_lambda():
    with pytest.raises(ValueError):
        inertia(vertical_gram(0.25))


def test_run_reports_exact_table():
    out = run([R(0), R(1, 4), R(1)])
    assert out["cases"][2]["chimeric"]["-1,1"] == [9, 5, 0]
    assert out["method"] == "exact Hermitian congruence (gu.inertia)"
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `uv run pytest tests/test_b01.py -v`
Expected: collection error, `ModuleNotFoundError: No module named 'experiments.B01'`.

- [ ] **Step 4: Implement**

```python
# experiments/B01/dewitt_family.py
"""B01: exact inertia of the DeWitt-family chimeric form (see ansatz.md).

[ext] parameterization. Whether it matches GU (3.8)-(3.10) is settled in README.md.
"""
from __future__ import annotations

import json
import platform
import subprocess
from pathlib import Path

import sympy as sp

from gu.inertia import inertia

ETA = sp.diag(1, -1, -1, -1)
LAM = sp.Symbol("lambda", real=True)
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]


def _sym_basis() -> list[sp.Matrix]:
    out = []
    for i, j in PAIRS:
        h = sp.zeros(4)
        h[i, j] = 1
        h[j, i] = 1
        out.append(h)
    return out


def dewitt(h: sp.Matrix, k: sp.Matrix, lam) -> sp.Expr:
    return (ETA * h * ETA * k).trace() - lam * (ETA * h).trace() * (ETA * k).trace()


def vertical_gram(lam) -> sp.Matrix:
    b = _sym_basis()
    return sp.Matrix(10, 10, lambda i, j: dewitt(b[i], b[j], lam))


def chimeric_gram(lam, h_sign: int, v_sign: int) -> sp.Matrix:
    return sp.diag(h_sign * ETA, v_sign * vertical_gram(lam))


def run(lams) -> dict:
    cases = []
    for lam in lams:
        cases.append({
            "lambda": str(lam),
            "vertical": list(inertia(vertical_gram(lam))),
            "chimeric": {f"{hs},{vs}": list(inertia(chimeric_gram(lam, hs, vs)))
                         for hs in (1, -1) for vs in (1, -1)},
        })
    return {
        "scope": "identity for listed lambda; [ext] family, not yet reconciled with GU",
        "method": "exact Hermitian congruence (gu.inertia)",
        "inertia_order": "(n_pos, n_neg, n_zero)",
        "chimeric_key": "h_sign,v_sign",
        "eigenvalues": {str(k): v for k, v in vertical_gram(LAM).eigenvals().items()},
        "cases": cases,
    }


def main() -> None:
    R = sp.Rational
    out = run([R(-1), R(0), R(1, 8), R(1, 4), R(1, 2), R(1)])
    out["versions"] = {"python": platform.python_version(), "sympy": sp.__version__}
    out["source_commit"] = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    out["command"] = "uv run python -m experiments.B01.dewitt_family"
    path = Path(__file__).with_name("result.json")
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `uv run pytest tests/test_b01.py -v`
Expected: all pass (6 vertical, 12 chimeric, 3 others). If any CHIMERIC value fails, stop and report; do not edit it.

- [ ] **Step 6: Generate the result and commit**

Run: `uv run python -m experiments.B01.dewitt_family`
Expected: `wrote ...experiments\B01\result.json`.

```bash
git add experiments/B01/__init__.py experiments/B01/dewitt_family.py experiments/B01/result.json tests/test_b01.py
git commit -m "B01: exact inertia of DeWitt-family chimeric form"
```

---

### Task 3: B01 independent transcription — Claude

Runs in parallel with Tasks 1–2. Claude does not read `dewitt_family.py` while transcribing.

**Files:**
- Create: `experiments/B01/transcription.md`

- [ ] **Step 1: Get the source.** Download `https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf` into the scratchpad. Record its SHA-256 in the transcription.
- [ ] **Step 2: Transcribe** pp. 18–23: eqs. (3.8)–(3.10) and §3.5, verbatim in LaTeX with page and equation numbers. Use these sections:
  - **Source:** URL, SHA-256, pages.
  - **Verbatim equations:** each one numbered as in the draft.
  - **Symbol table:** each symbol with its type (bundle, fibre, form degree, field ℝ/ℂ) and where it is defined.
  - **Conventions:** metric signature order, trace normalization, any free parameter (the draft's analog of λ or its absence), and the signs on the horizontal and vertical parts.
  - **`[GU-recon]` branches:** each ambiguity with every reading listed.
  - **Draft's stated signature claim:** quoted, with page.
- [ ] **Step 3: Commit**

```bash
git add experiments/B01/transcription.md
git commit -m "B01: independent transcription of GU (3.8)-(3.10) and section 3.5"
```

---

### Task 4: B01 reconciliation, independent re-derivation and register update — Claude, then Codex

**Files:**
- Create: `experiments/B01/README.md` (Claude), `experiments/B01/rederivation.md` (Codex)
- Modify: `docs/gaps/register.md` (Codex; B01 and A01 entries and any evidence link into `.agent-handoff/`)

- [ ] **Step 1 (Claude): Write the convention map.** In `README.md`, map each draft symbol from `transcription.md` onto `ETA`, `B_λ`, `s_H`, `s_V`. Apply the reconciliation criterion in `ansatz.md` and state one of:
  - `match: λ = …, (s_H, s_V) = …`, with the resulting inertia read from `result.json`;
  - `mismatch: …`, naming the first symbol that does not map.

  Every claim gets provenance, evidence (`verified:experiments/B01/result.json` or `unverified`) and scope. List the degenerate boundary λ = 1/4 and every sign choice the draft leaves open. Do not name a single "selected" signature unless the draft fixes all of the choices.
- [ ] **Step 2 (Codex): Re-derive the result independently** by a different route, in `rederivation.md`. Without running `dewitt_family.py`, split Sym² = (trace line) ⊕ (traceless part) by hand. Show that B_λ is block-diagonal: the trace direction has norm 4(1−4λ) and the traceless block has inertia (6,3) independent of λ. Then confirm the vertical and chimeric inertia table by hand addition. Report any disagreement with `result.json` or `README.md`.
- [ ] **Step 3 (Codex): Update the register.** Point the B01 and A01 evidence to `experiments/B01/`. Remove every link into `.agent-handoff/`. Set the B01 status per README.md, with all three tags.
- [ ] **Step 4: Verify links**

Run: `grep -n "agent-handoff" docs/gaps/register.md`
Expected: no output.

- [ ] **Step 5: Commit** (two commits, one per author)

```bash
git add experiments/B01/README.md && git commit -m "B01: reconciliation with GU conventions"
git add experiments/B01/rederivation.md docs/gaps/register.md && git commit -m "B01: independent re-derivation; register links repointed"
```

---

### Task 5: Monomial Clifford algebra with the Dirac pairing (`gu/clifford.py`) — Codex

**Files:**
- Create: `gu/clifford.py`
- Test: `tests/test_clifford.py`

**Interfaces:**
- Produces:
  - `Mono(perm: np.ndarray, phase: np.ndarray)` with `M[perm[j], j] = i**phase[j]`.
  - Methods: `@`, unary `-`, `times_i_power(k)`, `dagger()`, `==`, `trace() -> tuple[int,int]` (re, im), `to_dense() -> tuple[np.ndarray, np.ndarray]` (int64 re, im), `n`, `Mono.identity(n)`.
  - `eta(p, q) -> list[int]`, `gammas(p, q) -> list[Mono]`, `dirac_pairing(p, q) -> Mono`, `chirality(p, q) -> Mono`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_clifford.py
import pytest

from gu.clifford import Mono, chirality, dirac_pairing, eta, gammas

SIGS = [(1, 1), (3, 1), (14, 0), (7, 7), (9, 5)]


@pytest.mark.parametrize("p,q", SIGS)
def test_clifford_relations(p, q):
    G, e = gammas(p, q), eta(p, q)
    n = 2 ** ((p + q) // 2)
    I = Mono.identity(n)
    assert all(g.n == n for g in G)
    for a in range(p + q):
        assert G[a] @ G[a] == (I if e[a] == 1 else -I)
        for b in range(a + 1, p + q):
            assert G[a] @ G[b] == -(G[b] @ G[a])


@pytest.mark.parametrize("p,q", SIGS)
def test_dirac_pairing(p, q):
    G, A = gammas(p, q), dirac_pairing(p, q)
    I = Mono.identity(A.n)
    assert A.dagger() == A
    assert A @ A == I
    if q == 0:
        assert A == I
    else:
        assert A.trace() == (0, 0)  # A^2 = I, Hermitian, traceless => inertia (n/2, n/2)
    for g in G:  # A G_a A^-1 = (-1)^q G_a^dagger
        rhs = g.dagger() @ A
        assert A @ g == (rhs if q % 2 == 0 else -rhs)


@pytest.mark.parametrize("p,q", SIGS)
def test_spin_generators_are_A_skew(p, q):
    G, A = gammas(p, q), dirac_pairing(p, q)
    for a in range(p + q):
        for b in range(a + 1, p + q):
            S = G[a] @ G[b]
            assert S.dagger() @ A == -(A @ S)


@pytest.mark.parametrize("p,q", SIGS)
def test_chirality(p, q):
    G, C = gammas(p, q), chirality(p, q)
    assert C @ C == Mono.identity(C.n)
    assert C.dagger() == C
    assert C.trace() == (0, 0)
    for g in G:
        assert C @ g == -(g @ C)


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (7, 7), (9, 5)])
def test_spacelike_timelike_product_is_anti_isometry(p, q):
    # spec rev 4, section 4: gamma_s gamma_t is NOT in U(A)
    G, A = gammas(p, q), dirac_pairing(p, q)
    h = G[0] @ G[p]
    assert h.dagger() @ A @ h == -A


def test_odd_dimension_rejected():
    with pytest.raises(ValueError):
        gammas(2, 1)


def test_dense_roundtrip():
    G = gammas(1, 1)
    re, im = G[1].to_dense()
    assert (re ** 2 + im ** 2).sum() == 2  # one unit entry per column
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_clifford.py -v`
Expected: `ModuleNotFoundError: No module named 'gu.clifford'`.

- [ ] **Step 3: Implement**

```python
# gu/clifford.py
"""Exact gamma matrices for Cl(p,q) as monomial matrices over Z[i].

Convention: {G_a, G_b} = 2 eta_ab I, eta = diag(+1 x p, -1 x q).
A monomial matrix has one nonzero entry per column: M[perm[j], j] = i**phase[j].
Euclidean gammas come from the Jordan-Wigner construction; timelike ones are i times them.
"""
from __future__ import annotations

import numpy as np

_RE = np.array([1, 0, -1, 0], dtype=np.int64)
_IM = np.array([0, 1, 0, -1], dtype=np.int64)


class Mono:
    __slots__ = ("perm", "phase")

    def __init__(self, perm, phase):
        self.perm = np.asarray(perm, dtype=np.int64)
        self.phase = np.asarray(phase, dtype=np.int64) % 4

    @staticmethod
    def identity(n: int) -> "Mono":
        return Mono(np.arange(n), np.zeros(n))

    @property
    def n(self) -> int:
        return len(self.perm)

    def __matmul__(self, other: "Mono") -> "Mono":
        return Mono(self.perm[other.perm], other.phase + self.phase[other.perm])

    def times_i_power(self, k: int) -> "Mono":
        return Mono(self.perm, self.phase + k)

    def __neg__(self) -> "Mono":
        return self.times_i_power(2)

    def dagger(self) -> "Mono":
        inv = np.empty_like(self.perm)
        inv[self.perm] = np.arange(self.n)
        phase = np.empty_like(self.phase)
        phase[self.perm] = -self.phase
        return Mono(inv, phase)

    def __eq__(self, other) -> bool:
        return (isinstance(other, Mono) and np.array_equal(self.perm, other.perm)
                and np.array_equal(self.phase, other.phase))

    __hash__ = None

    def trace(self) -> tuple[int, int]:
        fixed = self.phase[self.perm == np.arange(self.n)]
        return int(_RE[fixed].sum()), int(_IM[fixed].sum())

    def to_dense(self) -> tuple[np.ndarray, np.ndarray]:
        re = np.zeros((self.n, self.n), dtype=np.int64)
        im = np.zeros((self.n, self.n), dtype=np.int64)
        cols = np.arange(self.n)
        re[self.perm, cols] = _RE[self.phase]
        im[self.perm, cols] = _IM[self.phase]
        return re, im


def _kron(a: Mono, b: Mono) -> Mono:
    ja, jb = np.divmod(np.arange(a.n * b.n), b.n)
    return Mono(a.perm[ja] * b.n + b.perm[jb], a.phase[ja] + b.phase[jb])


_I2 = Mono([0, 1], [0, 0])
_X = Mono([1, 0], [0, 0])
_Y = Mono([1, 0], [1, 3])  # [[0,-i],[i,0]]
_Z = Mono([0, 1], [0, 2])


def _kron_all(ms: list[Mono]) -> Mono:
    out = ms[0]
    for m in ms[1:]:
        out = _kron(out, m)
    return out


def eta(p: int, q: int) -> list[int]:
    return [1] * p + [-1] * q


def gammas(p: int, q: int) -> list[Mono]:
    d = p + q
    if d % 2 or d == 0:
        raise ValueError("gammas() supports even p+q >= 2 only")
    m = d // 2
    euclid = []
    for k in range(m):
        for P in (_X, _Y):
            euclid.append(_kron_all([_Z] * k + [P] + [_I2] * (m - k - 1)))
    return [g if a < p else g.times_i_power(1) for a, g in enumerate(euclid)]


def _product(ms: list[Mono], n: int) -> Mono:
    out = Mono.identity(n)
    for m in ms:
        out = out @ m
    return out


def dirac_pairing(p: int, q: int) -> Mono:
    """Phase times the product of the timelike gammas, chosen Hermitian."""
    G = gammas(p, q)
    A0 = _product(G[p:], G[0].n)
    for k in range(4):
        A = A0.times_i_power(k)
        if A.dagger() == A:
            return A
    raise AssertionError("no Hermitian phase for A")  # unreachable: A0^dagger = +-A0


def chirality(p: int, q: int) -> Mono:
    """Phase times G_0...G_{d-1}, chosen with C^2 = I and C Hermitian."""
    G = gammas(p, q)
    P = _product(G, G[0].n)
    I = Mono.identity(G[0].n)
    for k in range(4):
        C = P.times_i_power(k)
        if C @ C == I and C.dagger() == C:
            return C
    raise AssertionError("no chirality phase")
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_clifford.py -v`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add gu/clifford.py tests/test_clifford.py
git commit -m "Add monomial Clifford algebra with Dirac pairing and chirality"
```

---

### Task 6: Exterior forms and the pinned Hodge star (`gu/forms.py`) — Codex

**Files:**
- Create: `gu/forms.py`
- Test: `tests/test_forms.py`

**Interfaces:**
- Produces: forms are `dict[tuple[int, ...], int]` (strictly increasing index tuples). Functions: `basis(n, k)`, `wedge(a, b)`, `eta_I(eta, I) -> int`, `vol(n)`, `inner(a, b, eta) -> int`, `hodge(a, eta)`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_forms.py
import pytest

from gu.forms import basis, eta_I, hodge, inner, vol, wedge


def _eta(p, q):
    return [1] * p + [-1] * q


@pytest.mark.parametrize("p,q", [(9, 5), (7, 7)])
@pytest.mark.parametrize("k", [0, 1, 2, 7, 13, 14])
def test_pinned_convention_and_star_squared(p, q, k):
    eta, n = _eta(p, q), p + q
    sign = (-1) ** (k * (n - k) + q)
    for I in basis(n, k):
        e = {I: 1}
        assert wedge(e, hodge(e, eta)) == {tuple(range(n)): eta_I(eta, I)}
        assert hodge(hodge(e, eta), eta) == {I: sign}


def test_lorentzian_known_values():
    eta = _eta(3, 1)  # e3 timelike
    assert hodge({(0, 1): 1}, eta) == {(2, 3): 1}
    assert hodge(hodge({(0, 1): 1}, eta), eta) == {(0, 1): -1}  # star^2 = -1 on 2-forms in 4D Lorentzian


def test_wedge_basics():
    assert wedge({(0,): 1}, {(0,): 1}) == {}
    assert wedge({(1,): 1}, {(0,): 1}) == {(0, 1): -1}
    assert wedge({(0,): 2}, {(1,): 3}) == {(0, 1): 6}


def test_inner_and_vol():
    eta = _eta(1, 1)
    assert inner({(1,): 1}, {(1,): 1}, eta) == -1
    assert inner(vol(2), vol(2), eta) == -1
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_forms.py -v`
Expected: `ModuleNotFoundError: No module named 'gu.forms'`.

- [ ] **Step 3: Implement**

```python
# gu/forms.py
"""Exterior algebra on R^{p,q} with exact integer coefficients.

A k-form is a dict {I: coeff}, I a strictly increasing index tuple.
Hodge star convention (pinned, spec rev 4.1): a ^ *b = <a, b>_eta vol,
with <e_I, e_I> = eta_I = prod_{i in I} eta_i. Then ** = (-1)^{k(n-k)+q}.
The Lambda^{n-1} = Lambda^1 identification is hodge() restricted to (n-1)-forms.
"""
from __future__ import annotations

from itertools import combinations
from math import prod


def basis(n: int, k: int) -> list[tuple[int, ...]]:
    return list(combinations(range(n), k))


def _sort_sign(idx: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    if len(set(idx)) < len(idx):
        return 0, ()
    inversions = sum(1 for i in range(len(idx)) for j in range(i + 1, len(idx)) if idx[i] > idx[j])
    return (-1) ** inversions, tuple(sorted(idx))


def _clean(f: dict) -> dict:
    return {K: v for K, v in f.items() if v != 0}


def wedge(a: dict, b: dict) -> dict:
    out: dict = {}
    for I, x in a.items():
        for J, y in b.items():
            s, K = _sort_sign(I + J)
            if s:
                out[K] = out.get(K, 0) + s * x * y
    return _clean(out)


def eta_I(eta: list[int], I: tuple[int, ...]) -> int:
    return prod(eta[i] for i in I)


def vol(n: int) -> dict:
    return {tuple(range(n)): 1}


def inner(a: dict, b: dict, eta: list[int]) -> int:
    return sum(x * b[I] * eta_I(eta, I) for I, x in a.items() if I in b)


def hodge(a: dict, eta: list[int]) -> dict:
    n = len(eta)
    out: dict = {}
    for I, x in a.items():
        Ic = tuple(i for i in range(n) if i not in I)
        s, _ = _sort_sign(I + Ic)
        out[Ic] = out.get(Ic, 0) + s * eta_I(eta, I) * x
    return _clean(out)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_forms.py -v`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add gu/forms.py tests/test_forms.py
git commit -m "Add exterior forms with pinned Hodge convention"
```

---

### Task 7: Algebraic curvature split (`gu/curvature.py`) — Codex

**Files:**
- Create: `gu/curvature.py`
- Test: `tests/test_curvature.py`

**Interfaces:**
- Produces:
  - `kulkarni_nomizu(h, k) -> np.ndarray`, `ricci(R, eta) -> np.ndarray`, `scalar(R, eta) -> int`, `is_algebraic_curvature(R) -> bool`.
  - `decompose(R, eta) -> Split`, where `Split` is a dataclass with `denominator: int`, `scalar_part`, `ricci_part`, `weyl` (integer numerator arrays: part = numerator / denominator).
  - `dims(n) -> tuple[int, int, int]` for (scalar, traceless Ricci, Weyl).
  - `random_curvature(n, rng, terms=6) -> np.ndarray`.
  - `R` is an int64 array of shape (n,n,n,n); `eta` is a 1-D int array of ±1.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_curvature.py
import numpy as np
import pytest
from flint import fmpz_mat

from gu.curvature import (decompose, dims, is_algebraic_curvature, kulkarni_nomizu,
                          random_curvature, ricci, scalar)

SIGS = [(4, 0), (3, 1), (9, 5), (7, 7)]


def _eta(p, q):
    return np.array([1] * p + [-1] * q, dtype=np.int64)


@pytest.mark.parametrize("p,q", SIGS)
def test_constant_curvature_is_pure_scalar(p, q):
    # Positive control for the argon sign bug: W must be 0, not 2R.
    eta = _eta(p, q); g = np.diag(eta); n = p + q
    R = kulkarni_nomizu(g, g) // 2  # eta_ac eta_bd - eta_ad eta_bc
    assert np.array_equal(ricci(R, eta), (n - 1) * g)
    s = decompose(R, eta)
    assert not s.weyl.any() and not s.ricci_part.any()
    assert np.array_equal(s.scalar_part, s.denominator * R)


@pytest.mark.parametrize("p,q", SIGS)
def test_pure_traceless_ricci(p, q):
    eta = _eta(p, q); g = np.diag(eta); n = p + q
    rng = np.random.default_rng(1)
    h = rng.integers(-3, 4, (n, n)); h = h + h.T
    h[0, 0] -= eta[0] * int((eta * np.diag(h)).sum())  # make eta-traceless
    assert int((eta * np.diag(h)).sum()) == 0
    R = kulkarni_nomizu(h, g)
    s = decompose(R, eta)
    assert scalar(R, eta) == 0
    assert not s.weyl.any() and not s.scalar_part.any()
    assert np.array_equal(s.ricci_part, s.denominator * R)


@pytest.mark.parametrize("p,q", SIGS)
def test_generic_split(p, q):
    eta = _eta(p, q)
    R = random_curvature(p + q, np.random.default_rng(2))
    assert is_algebraic_curvature(R)
    s = decompose(R, eta)
    assert np.array_equal(s.weyl + s.ricci_part + s.scalar_part, s.denominator * R)
    assert is_algebraic_curvature(s.weyl)
    assert not ricci(s.weyl, eta).any()
    assert s.weyl.any()


@pytest.mark.parametrize("p,q", [(4, 0), (3, 1), (5, 0), (4, 2)])
def test_component_ranks_small_n(p, q):
    eta, n = _eta(p, q), p + q
    rng = np.random.default_rng(3)
    total = n * n * (n * n - 1) // 12
    Rs = [random_curvature(n, rng) for _ in range(total + 10)]
    rank = lambda arrs: fmpz_mat([[int(x) for x in a.ravel()] for a in arrs]).rank()
    assert rank(Rs) == total
    assert rank([decompose(R, eta).weyl for R in Rs]) == dims(n)[2]


def test_dims_d14():
    assert dims(14) == (1, 104, 3080)
    assert sum(dims(14)) == 14 * 14 * (14 * 14 - 1) // 12 == 3185
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_curvature.py -v`
Expected: `ModuleNotFoundError: No module named 'gu.curvature'`.

- [ ] **Step 3: Implement**

```python
# gu/curvature.py
"""Algebraic curvature tensors and their exact scalar / traceless-Ricci / Weyl split.

Convention (pinned, spec rev 4.1): R[a,b,c,d] is antisymmetric in (a,b) and (c,d),
pair-symmetric, and satisfies first Bianchi. Ric[b,d] = eta^{ac} R[a,b,c,d]
(contract slots 1 and 3). Unit sphere: R = eta_ac eta_bd - eta_ad eta_bc, Ric = (n-1) eta.
R = W + Ric0 (KN) g / (n-2) + S g (KN) g / (2n(n-1)). Integer arithmetic with an explicit denominator.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def kulkarni_nomizu(h: np.ndarray, k: np.ndarray) -> np.ndarray:
    return (np.einsum("ac,bd->abcd", h, k) + np.einsum("bd,ac->abcd", h, k)
            - np.einsum("ad,bc->abcd", h, k) - np.einsum("bc,ad->abcd", h, k))


def ricci(R: np.ndarray, eta: np.ndarray) -> np.ndarray:
    return np.einsum("a,abad->bd", eta, R)


def scalar(R: np.ndarray, eta: np.ndarray) -> int:
    return int(np.einsum("b,bb->", eta, ricci(R, eta)))


def is_algebraic_curvature(R: np.ndarray) -> bool:
    return bool(np.array_equal(R, -np.einsum("bacd->abcd", R))
                and np.array_equal(R, -np.einsum("abdc->abcd", R))
                and np.array_equal(R, np.einsum("cdab->abcd", R))
                and not (R + np.einsum("acdb->abcd", R) + np.einsum("adbc->abcd", R)).any())


@dataclass
class Split:
    denominator: int
    scalar_part: np.ndarray
    ricci_part: np.ndarray
    weyl: np.ndarray


def decompose(R: np.ndarray, eta: np.ndarray) -> Split:
    n = len(eta)
    if n < 3:
        raise ValueError("decompose() needs n >= 3")
    g = np.diag(eta)
    S = scalar(R, eta)
    N = 2 * n * (n - 1) * (n - 2)
    n_ric0 = n * ricci(R, eta) - S * g                    # n * Ric0, integer
    ricci_part = 2 * (n - 1) * kulkarni_nomizu(n_ric0, g)  # N * Ric0 (KN) g / (n-2)
    scalar_part = (n - 2) * S * kulkarni_nomizu(g, g)     # N * S g (KN) g / (2n(n-1))
    return Split(N, scalar_part, ricci_part, N * R - ricci_part - scalar_part)


def dims(n: int) -> tuple[int, int, int]:
    return 1, n * (n + 1) // 2 - 1, n * (n + 1) * (n + 2) * (n - 3) // 12


def random_curvature(n: int, rng: np.random.Generator, terms: int = 6) -> np.ndarray:
    R = np.zeros((n, n, n, n), dtype=np.int64)
    for _ in range(terms):
        h = rng.integers(-3, 4, (n, n)); h = h + h.T
        k = rng.integers(-3, 4, (n, n)); k = k + k.T
        R += kulkarni_nomizu(h, k)
    return R
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_curvature.py -v`
Expected: all pass. `test_component_ranks_small_n` needs enough independent samples; if the rank comes out short, raise `terms`, not the expected value.

- [ ] **Step 5: Commit**

```bash
git add gu/curvature.py tests/test_curvature.py
git commit -m "Add exact curvature split with pure-sector controls"
```

---

### Task 8: The u(64,64) gauge algebra and Cayley group elements (`gu/adjoint.py`) — Codex

**Files:**
- Create: `gu/adjoint.py`
- Test: `tests/test_adjoint.py`

**Interfaces:**
- Consumes: `gu.clifford.Mono`, `gammas`, `dirac_pairing`.
- Produces:
  - `embed(re, im) -> fmpq_mat` (2n×2n real block form, entry a+ib ↦ [[a,−b],[b,a]]; M† ↦ transpose).
  - `from_mono(m) -> fmpq_mat`.
  - `is_in_algebra(M, A) -> bool` (Mᵀ A + A M = 0) and `is_in_group(h, A) -> bool` (hᵀ A h = A).
  - `random_algebra_element(A, rng, nonzeros=8, scale=3) -> fmpq_mat`.
  - `cayley(X) -> fmpq_mat`, which raises `SingularCayley` when det(I+X) = 0.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_adjoint.py
import numpy as np
import pytest
from flint import fmpq, fmpq_mat

from gu.adjoint import (SingularCayley, cayley, embed, from_mono, is_in_algebra,
                        is_in_group, random_algebra_element)
from gu.clifford import dirac_pairing, gammas


@pytest.fixture(scope="module", params=[(7, 7), (9, 5)])
def setup(request):
    p, q = request.param
    return p, q, gammas(p, q), from_mono(dirac_pairing(p, q))


def _eye(n):
    return fmpq_mat(n, n, [1 if i == j else 0 for i in range(n) for j in range(n)])


def test_A_is_symmetric_involution(setup):
    _, _, _, A = setup
    assert A.transpose() == A and A * A == _eye(A.nrows())


def test_spin_generators_in_algebra(setup):
    p, q, G, A = setup
    for a in range(p + q):
        for b in range(a + 1, p + q):
            assert is_in_algebra(from_mono(G[a] @ G[b]), A)


def test_central_iI_in_algebra(setup):
    _, _, _, A = setup
    n = A.nrows() // 2
    assert is_in_algebra(embed(np.zeros((n, n), dtype=np.int64), np.eye(n, dtype=np.int64)), A)


def test_cayley_of_random_algebra_elements(setup):
    _, _, _, A = setup
    rng = np.random.default_rng(0)
    for _ in range(3):
        X = random_algebra_element(A, rng)
        assert is_in_algebra(X, A)
        assert is_in_group(cayley(X), A)


def test_spacelike_timelike_product_not_in_group(setup):
    p, _, G, A = setup
    h = from_mono(G[0] @ G[p])
    assert not is_in_group(h, A)
    assert h.transpose() * A * h == -A


def test_singular_cayley_guard():
    A = embed(np.diag([1, -1]), np.zeros((2, 2), dtype=np.int64))
    X = embed(np.array([[0, 1], [1, 0]]), np.zeros((2, 2), dtype=np.int64))  # unit boost
    assert is_in_algebra(X, A)
    with pytest.raises(SingularCayley):
        cayley(X)
    h = cayley(X * fmpq(1, 2))
    assert is_in_group(h, A)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_adjoint.py -v`
Expected: `ModuleNotFoundError: No module named 'gu.adjoint'`.

- [ ] **Step 3: Implement**

```python
# gu/adjoint.py
"""The internal gauge algebra u(A) (= u(64,64) for d=14, q>=1) and its group, exactly.

Complex n x n matrices are embedded as real 2n x 2n rational matrices,
a+ib -> [[a,-b],[b,a]]. Under this embedding M^dagger becomes the transpose, so
u(A) = {M : M^T A + A M = 0} and U(A) = {h : h^T A h = A} are tested over QQ.
The basis of u(A) is never materialized (spec rev 4.1, section 5).
"""
from __future__ import annotations

import numpy as np
from flint import fmpq, fmpq_mat

from gu.clifford import Mono


class SingularCayley(ValueError):
    """det(I + X) = 0: rescale or resample X. Not an operator failure."""


def embed(re: np.ndarray, im: np.ndarray) -> fmpq_mat:
    n = re.shape[0]
    big = np.zeros((2 * n, 2 * n), dtype=object)
    big[0::2, 0::2] = re
    big[0::2, 1::2] = -im
    big[1::2, 0::2] = im
    big[1::2, 1::2] = re
    return fmpq_mat(2 * n, 2 * n, [int(x) for x in big.flat])


def from_mono(m: Mono) -> fmpq_mat:
    return embed(*m.to_dense())


def _eye(n: int) -> fmpq_mat:
    return fmpq_mat(n, n, [1 if i == j else 0 for i in range(n) for j in range(n)])


def is_in_algebra(M: fmpq_mat, A: fmpq_mat) -> bool:
    return M.transpose() * A + A * M == fmpq_mat(A.nrows(), A.ncols())


def is_in_group(h: fmpq_mat, A: fmpq_mat) -> bool:
    return h.transpose() * A * h == A


def random_algebra_element(A: fmpq_mat, rng: np.random.Generator,
                           nonzeros: int = 8, scale: int = 3) -> fmpq_mat:
    """X = (Y - A Y^dagger A) / scale for a sparse Gaussian-integer Y. Requires A^2 = I."""
    N = A.nrows()
    if A * A != _eye(N):
        raise ValueError("random_algebra_element() assumes A^2 = I")
    n = N // 2
    re = np.zeros((n, n), dtype=np.int64)
    im = np.zeros((n, n), dtype=np.int64)
    for _ in range(nonzeros):
        i, j = rng.integers(0, n, 2)
        re[i, j] += rng.integers(-2, 3)
        im[i, j] += rng.integers(-2, 3)
    Y = embed(re, im)
    return (Y - A * Y.transpose() * A) * fmpq(1, scale)


def cayley(X: fmpq_mat) -> fmpq_mat:
    """h = (I - X)(I + X)^{-1}; in U(A) whenever X is in u(A)."""
    I = _eye(X.nrows())
    D = I + X
    if D.det() == 0:
        raise SingularCayley("det(I + X) = 0")
    return (I - X) * D.inv()
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_adjoint.py -v`
Expected: all pass. If a random X hits `SingularCayley`, change the seed in the test and note it in the commit message. Never catch the exception inside `cayley`.

- [ ] **Step 5: Run the full suite and commit**

Run: `uv run pytest -v`
Expected: all tests in Tasks 1–8 pass.

```bash
git add gu/adjoint.py tests/test_adjoint.py
git commit -m "Add exact u(64,64) membership and Cayley group elements"
```

---

### Task 9: B02 transcription and pre-registration — Claude (Codex reviews the transcription)

**Files:**
- Create: `experiments/B02/transcription.md`, `experiments/B02/ansatz.md`
- Modify (Codex): `docs/gaps/register.md` (B02: add the Weyl-vacuity fact with scope `identity`, citing `experiments/B02/ansatz.md` until a tracked script exists)

- [ ] **Step 1 (Claude): Transcribe** GU pp. 41–43: §8.2, eq. (8.7), eq. (9.3) and footnote 10, using the same sections as Task 3. In addition, record:
  - the dressing definition and how ε acts;
  - each Φ embedding;
  - the bracket used, as `[GU-recon]` branches: commutator, i·anticommutator, or raw product with the projection ½(M − A⁻¹M†A);
  - phases and normalization;
  - the expected scalar and traceless-Ricci responses, with relative coefficients, or "unresolved".
- [ ] **Step 2 (Claude): Write `ansatz.md`.** Pre-register spec §5 tests 1–5 with their pass criteria and scopes, the open-data case Shiab_ε(W), and the signatures (7,7) and (9,5).
- [ ] **Step 3 (Codex): Review the transcription** against the PDF. Write disagreements to `.agent-handoff/b02-transcription/result.md`; Claude resolves them in `transcription.md`.
- [ ] **Step 4: Commit the pre-registration** before any B02 code exists

```bash
git add experiments/B02/transcription.md experiments/B02/ansatz.md
git commit -m "B02: transcription of (9.3) and pre-registered test criteria"
```

- [ ] **Step 5 (Claude):** Write the follow-up plan `docs/superpowers/plans/<date>-b02-direct-check.md` from the committed transcription.
