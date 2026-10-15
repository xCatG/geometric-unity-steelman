# B02 Direct Check of GU (9.3) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. In this project the worker is Codex (pane 0:3) and the orchestrator is Claude; read `docs/methods.md` (P1–P11) first.

**Goal:** Decide, at `identity` scope where possible, whether the displayed Shiab operator GU (9.3) produces an Einstein-like response (κ = ½), separately for the literal bracket reading (CCC) and every reconstructed reading. Record the dressed-covariance and open-data results.

**Architecture:** A sparse exact engine represents Λ(V*) ⊗ Cl(V) elements as `{(form_mask, blade_mask): GQ}` dicts. It is validated against the dense `gu.clifford` Mono model and `gu.forms.hodge`. `gu/shiab.py` builds the invariant Φ bases, the curvature input ξ(R), the operator (9.3), the Spin action and sparse Cayley dressings. One experiment script checks a closed-form response formula on a certified spanning set of algebraic curvature tensors. Multilinearity extends it to every real Φ¹ = αF + βF′, Φ² = γB + δB′, and linearity to all algebraic curvature.

**Tech Stack:** Python ≥ 3.12 via `uv`; `fractions.Fraction` (exact); numpy int64 arrays only for integer curvature tensors; python-flint 0.9.0 (`nmod_mat` rank, `fmpq_mat` for adapter checks); pytest.

**Spec:** `docs/superpowers/specs/2026-10-14-gu-steelman-design.md` (rev 4.1, approved). Pre-registration: `experiments/B02/ansatz.md` (amendment 1, `f75bb66`). Source: `experiments/B02/transcription.md` (rev 2).

## Global Constraints

- No floats on any claim path. `GQ` rejects floats, bools and complex (P4).
- Every test docstring states its claim and scope (`identity` / `sampled` / `counterexample`); a test without one is a control (P1).
- Seed 2–3 realistic faults per new module. Each must fail an **assertion** (not a NameError), and the restore must be verified (P2). Adapters get a positive example and an ambient impostor (P2b).
- Expected values come from outside the code under test (P3). The closed-form response comes from the hand derivation in `.agent-handoff/b02-transcription/evidence/derivation.md`, extended bilinearly in Task 5.
- Small signature first: every check runs on (3,1) before (7,7) and (9,5) (P5).
- Commits go on master with an explicit pathspec. Code is committed before `result.json`, whose `source_commit` must name a commit containing the producing code (P8). Codex's trailer: `Co-Authored-By: Codex <noreply@openai.com>`.
- Gates use the pre-registered target κ = ½ and the branch's own embedding E_T (P10).
- No Fable spend. Codex may spawn subagents.

## Review Focus

1. **The verifier re-implements the operator instead of calling it.** The plan's own smoke test hit this: a checker that reassembled the brackets itself stayed green with the −½ flipped. `response.py` must call `shiab_parts` and `assemble`, and the −½ seeded fault must turn it red (Task 4, Step 4).
2. **A vacuous spanning set.** If the KN products were rank-deficient, or outputs all zero, a green run would prove nothing. Assert rank = dim (3185 at n = 14, 20 at n = 4), and record `nonzero_outputs` > 0 (Task 4).
3. **The chirality phase differs by dimension** (C = vol at n = 14, i·vol at n = 4). It is derived from `gu.clifford.chirality`, never hard-coded, and tested in all signatures (Task 1).
4. **Wrong controls.** Dressing by a Spin-image ε is **not** a no-op: Φ is invariant under the joint form + Clifford action, while dressing acts on the Clifford factor alone. The no-op control uses a central ε (Task 3). This was a real error in the first draft of this plan's tests.
5. **Exactness leaks.** Two were found in review: `Fraction(np.int64)` keeps the fixed-width numerator, so `GQ(np.int64(2**62))*4` was 0 (R1); and `int()` casts in `xi` and `embed_tensor` dropped rationals and silently truncated floats (R2). The fix routes every coefficient through `gu.cliffform.exact`, which converts to Python `int`/`Fraction` and raises on floats. Tests: Task 1 (large integers), Task 2 (rational inputs, float rejection).

**Revision 2 (2026-10-15).** This revision folds in Codex's two-subagent plan review (`.agent-handoff/b02-plan-review/`; verdict *revise*, R1–R8) and argon's review.
- **R1/R2 (exactness):** `exact()`, plus controls.
- **R3–R5 (Task 6 classification):** corrected families, the N-b domain, the scalar-sector boundary, and null Φ² directions.
- **R6:** `git add` before every new-file commit.
- **R7:** (9,5) covariance samples.
- **R8:** runner asserts case counts, nonzero outputs and an independent hand control; the small rank test now exists.
- **Argon:** a mixed-Φ formula test, an end-to-end Spin₀ equivariance test, and a general `_in_u_A` that checks `shiab` outputs (Test 2) with a mixed-phase impostor.
- **Claude:** one dressing sample was identically zero, because KN(E₀₁+E₁₀, diag(1,2,0,…)) = 0. It was replaced, and `test_xi_samples_are_nonzero` added.

**Revision 3 (2026-10-15).** This revision folds in an independent Grok review via pi (`.agent-handoff/b02-plan-review-grok/`; verdict *revise*, 5 new findings, all reproduced by Claude).
- **G1 (Hodge convention):** the other standard star, ∗′ = (−1)^{k(n−k)}∗, is *exactly* the pinned operator with Φ² → −Φ². Claude checked this for all 8 modes × {F, F′} × {B, B′} in (3,1) and (2,2); the proof goes in Task 5. Task 6 now carries the star as a branch: under ∗′ the Einstein point is γ = −1.
- **G2 (normalization):** the verdict must lead with the scale-stable consequence (CCC has no scalar term at any scale). κ = ½ belongs to unit Γ_aΓ_b (N-a). Under the spin generator σ_ab = ½Γ_aΓ_b it is ¼, and under N-b it is 1 (Task 6).
- **G3:** Task 6 no longer asks to confirm κ "against `result.json`", which contains no κ. κ is derived from the formula the runner asserts.
- **G4:** `spanning_rank` asserts that every KN product is an algebraic curvature tensor. The coordinate chart Sym²(Λ²) has C(n,4) more coordinates than the algebraic space (1 at n = 4, 1001 at n = 14; the first Bianchi map onto Λ⁴). Argon caught that an earlier draft said "one more".
- **G5:** the runner's hand control now also checks CAA on KN(g,g), giving (n−1)(n−2)·F, so the −½ scalar term has an independent numerical control.
- **Claude:** the relative sign of the two terms holds for odd q. For even q, κ → −κ (checked at (2,2) and (4,0)). Every signature in this project has odd q: (3,1), (1,3), (7,7), (9,5), (5,9). Task 6 states this.

## File structure

| File | Owner | Responsibility |
|---|---|---|
| `gu/cliffform.py` | Codex | `GQ` Gaussian rationals; blade/form sign rules; Hodge star; C/A brackets; volume multiplication; Mono adapter; chirality phase |
| `gu/shiab.py` | Codex | Φ bases F, F′, B, B′; ξ(R); `shiab_parts`/`assemble`/`shiab`; Spin generator action; E_T embedding; sparse dressing |
| `tests/test_cliffform.py`, `tests/test_shiab.py`, `tests/test_dressing.py` | Codex | Controls and claims, scope-tagged |
| `experiments/B02/__init__.py` (empty), `experiments/B02/response.py`, `experiments/B02/run.py` | Codex | Spanning rank; identity-scope response check; 5′ open data; writes `result.json` |
| `experiments/B02/result.json` | Codex (generated) | Evidence, with `source_commit` |
| `experiments/B02/proofs.md` | Claude (Codex checks) | Tests 1, 2(a), 3(a), 4(iii) and the composition argument |
| `experiments/B02/README.md` | Claude (Codex re-derives) | Reconciliation, κ classification, verdict lines |
| `docs/gaps/register.md` | Codex | B02 entry |

Tasks 1 → 2 → 3 → 4 are sequential (Codex). Task 5 (Claude) can run in parallel with Tasks 1–4. Task 6 needs Tasks 4 and 5.

**Smoke test (not evidence).** Claude ran every code block below (revision 2) in an uncommitted scratch copy of the repo: 222 tests passed (164 existing + 58 new). Codex's practical reviewer replayed revision 1 literally: all Expected lines matched, all 9 seeded faults failed assertions, and the full run took 541 s. Only Codex's committed run counts as evidence.

**Commit rule for every task (R6).** New files must be staged before a pathspec commit: `git add -- <exact paths>`, then `git commit -m "..." -- <exact paths>`. Never use a bare `git add -A` or a bare `git commit`; the index is shared.

---

### Task 1: Sparse Λ ⊗ Cl engine

**Files:**
- Create: `gu/cliffform.py`
- Test: `tests/test_cliffform.py`

**Interfaces:**
- Consumes: `gu.clifford.{gammas, chirality, Mono}`, `gu.forms.hodge`.
- Produces: `exact(x) -> Fraction` (rejects floats/bools; numpy ints become Python ints), `GQ(re, im)`, `I`, `bits(mask)`, `reorder_sign(a, b) -> ±1`, `blade_mul(a, b, eta) -> (blade, ±1)`, `clean`, `scale(x, c)`, `plus(*xs)`, `star(x, eta)`, `bracket(x, y, mode, eta)` with mode `"C"`/`"A"`, `right_mul_volume(x, phase, eta)`, `blade_to_mono(blade, gs)`, `chirality_phase(p, q) -> GQ` (cached).

- [ ] **Step 1: Write the tests** (`tests/test_cliffform.py`):

```python
# tests/test_cliffform.py
"""Controls for the sparse Lambda (x) Cl engine (P1: no scope tag = control)."""
import itertools
import random
from fractions import Fraction

import numpy as np
import pytest

from gu.clifford import chirality, gammas
from gu.cliffform import (GQ, I, blade_mul, blade_to_mono, bracket, chirality_phase,
                          reorder_sign, right_mul_volume, star)
from gu.forms import hodge


def _eta(p, q):
    return [1] * p + [-1] * q


def _signed(m, s):
    return m if s == 1 else -m


def test_gq_rejects_floats_and_bools():
    for bad in (0.5, 1e0, True, complex(1, 0), np.float64(1)):
        with pytest.raises(TypeError):
            GQ(bad)


def test_gq_arithmetic_against_hand_values():
    a, b = GQ(1, 2), GQ(Fraction(1, 2), -1)
    assert a * b == GQ(Fraction(5, 2), 0)          # (1+2i)(1/2-i) = 1/2 - i + i + 2
    assert I * I == -1 and (a / a) == 1 and a - a == 0 and not (a - a)
    assert GQ(np.int64(3)) == 3


def test_gq_numpy_integers_cannot_overflow():
    """Exactness control (review R1): numpy fixed-width ints become Python ints."""
    big = GQ(np.int64(2**62)) * 4
    assert big == 2**64 and type(big.re.numerator) is int
    assert GQ(Fraction(np.int64(3), np.int64(4))) == Fraction(3, 4)


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (2, 2)])
def test_blade_mul_matches_mono_on_all_pairs(p, q):
    """Positive adapter control (P2b): every blade pair, against gu.clifford."""
    eta, n, gs = _eta(p, q), p + q, gammas(p, q)
    mono = [blade_to_mono(a, gs) for a in range(1 << n)]
    for a, b in itertools.product(range(1 << n), repeat=2):
        c, s = blade_mul(a, b, eta)
        assert mono[a] @ mono[b] == _signed(mono[c], s)


@pytest.mark.parametrize("p,q", [(7, 7), (9, 5)])
def test_blade_mul_matches_mono_sampled_14d(p, q):
    eta, gs, rng = _eta(p, q), gammas(p, q), random.Random(20261015)
    for _ in range(200):
        a, b = rng.randrange(1 << 14), rng.randrange(1 << 14)
        c, s = blade_mul(a, b, eta)
        assert blade_to_mono(a, gs) @ blade_to_mono(b, gs) == _signed(blade_to_mono(c, gs), s)


def test_reorder_sign_hand_values():
    assert reorder_sign(0b10, 0b01) == -1      # e1 e0 = -e0 e1
    assert reorder_sign(0b01, 0b10) == 1
    assert reorder_sign(0b110, 0b001) == 1     # e1 e2 e0: two swaps


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (7, 7), (9, 5)])
def test_star_matches_gu_forms_hodge(p, q):
    """Positive adapter control: every basis form of the degrees (9.3) uses."""
    eta, n = _eta(p, q), p + q
    for k in sorted({0, 1, 2, n - 2, n - 1, n}):
        for idx in itertools.combinations(range(n), k):
            f = sum(1 << i for i in idx)
            want = {(sum(1 << i for i in J), 0): GQ(v) for J, v in hodge({idx: 1}, eta).items()}
            assert star({(f, 0): GQ(1)}, eta) == want


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (7, 7), (9, 5)])
def test_chirality_phase_reproduces_library_chirality(p, q):
    gs = gammas(p, q)
    ph = chirality_phase(p, q)
    k = {GQ(1): 0, I: 1, GQ(-1): 2, -I: 3}[ph]
    assert blade_to_mono((1 << (p + q)) - 1, gs).times_i_power(k) == chirality(p, q)


def test_bracket_hand_values_3_1():
    eta = _eta(3, 1)
    g0, g1 = {(0, 1): GQ(1)}, {(0, 2): GQ(1)}     # 0-forms G_0, G_1
    assert bracket(g0, g1, "C", eta) == {(0, 3): GQ(2)}       # [G0,G1] = 2 G0G1
    assert bracket(g0, g1, "A", eta) == {}                    # i{G0,G1} = 0
    assert bracket(g0, g0, "A", eta) == {(0, 0): GQ(0, 2)}    # i{G0,G0} = 2i
    t = {(0, 8): GQ(1)}                                       # timelike G_3, G3^2 = -1
    assert bracket(t, t, "A", eta) == {(0, 0): GQ(0, -2)}
    e0, e1 = {(1, 0): GQ(1)}, {(2, 0): GQ(1)}
    assert bracket(e0, e1, "A", eta) == {(3, 0): GQ(0, 2)}    # e0 ^ e1 (x) i{1,1}
    assert bracket(e1, e0, "A", eta) == {(3, 0): GQ(0, -2)}


def test_bracket_rejects_unknown_mode():
    with pytest.raises(ValueError):
        bracket({}, {}, "X", [1, -1])


def test_right_mul_volume_is_mono_product():
    eta, gs = _eta(3, 1), gammas(3, 1)
    for a in range(16):
        ((f, c), v), = right_mul_volume({(0, a): GQ(1)}, GQ(1), eta).items()
        assert blade_to_mono(a, gs) @ blade_to_mono(15, gs) == _signed(blade_to_mono(c, gs), int(v.re))
```

- [ ] **Step 2: Run them and see them fail**

Run: `uv run pytest tests/test_cliffform.py -q`
Expected: collection error, `ModuleNotFoundError: No module named 'gu.cliffform'`.

- [ ] **Step 3: Implement** (`gu/cliffform.py`):

```python
# gu/cliffform.py
"""Sparse exact elements of Lambda(V*) (x) Cl(V), V = R^{p,q}.

An element is a dict {(form, blade): GQ}. `form` is a bitmask for the increasing
wedge e^{i1}^...^e^{ik}; `blade` is a bitmask for the increasing product
G_{i1}...G_{ik} of gu.clifford gammas. Coefficients are exact Gaussian rationals.
No floats anywhere.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from numbers import Integral, Rational


def exact(x) -> Fraction:
    """Exact rational from an integer or rational (incl. numpy ints); rejects floats/bools.

    Numerators/denominators are converted to Python int so numpy fixed-width
    integers cannot overflow later.
    """
    if isinstance(x, bool) or not isinstance(x, (Integral, Rational)):
        raise TypeError(f"exact integer or rational required, got {type(x).__name__}")
    if isinstance(x, Integral):
        return Fraction(int(x))
    return Fraction(int(x.numerator), int(x.denominator))


class GQ:
    """Exact Gaussian rational re + i*im."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = exact(re), exact(im)

    @staticmethod
    def _of(x) -> "GQ":
        return x if isinstance(x, GQ) else GQ(x)

    def __add__(self, o):
        o = GQ._of(o)
        return GQ(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return GQ(-self.re, -self.im)

    def __sub__(self, o):
        return self + (-GQ._of(o))

    def __mul__(self, o):
        o = GQ._of(o)
        return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = GQ._of(o)
        d = o.re * o.re + o.im * o.im
        if d == 0:
            raise ZeroDivisionError("GQ division by zero")
        return self * GQ(o.re / d, -o.im / d)

    def __eq__(self, o):
        if not isinstance(o, (GQ, Integral, Rational)) or isinstance(o, bool):
            return NotImplemented
        o = GQ._of(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __bool__(self):
        return bool(self.re) or bool(self.im)

    def __repr__(self):
        return f"GQ({self.re}, {self.im})"


I = GQ(0, 1)


def bits(mask: int) -> list[int]:
    return [i for i in range(mask.bit_length()) if mask >> i & 1]


def reorder_sign(a: int, b: int) -> int:
    """Sign of sorting the concatenation (increasing a)(increasing b)."""
    n = sum((b & ((1 << i) - 1)).bit_count() for i in bits(a))
    return -1 if n % 2 else 1


def blade_mul(a: int, b: int, eta: list[int]) -> tuple[int, int]:
    """G_a G_b = sign * G_{a xor b}; repeated indices square to eta_i."""
    s = reorder_sign(a, b)
    for i in bits(a & b):
        s *= eta[i]
    return a ^ b, s


def _add(out: dict, key, v) -> None:
    w = out.get(key, GQ()) + v
    if w:
        out[key] = w
    else:
        out.pop(key, None)


def clean(x: dict) -> dict:
    out: dict = {}
    for k, v in x.items():
        _add(out, k, GQ._of(v))
    return out


def scale(x: dict, c) -> dict:
    c = GQ._of(c)
    return clean({k: v * c for k, v in x.items()})


def plus(*xs: dict) -> dict:
    out: dict = {}
    for x in xs:
        for k, v in x.items():
            _add(out, k, v)
    return out


def star(x: dict, eta: list[int]) -> dict:
    """Hodge star on the form factor; same convention as gu.forms.hodge."""
    full = (1 << len(eta)) - 1
    out: dict = {}
    for (f, c), v in x.items():
        t = reorder_sign(f, full ^ f)
        for i in bits(f):
            t *= eta[i]
        _add(out, (full ^ f, c), v * t)
    return out


def bracket(x: dict, y: dict, mode: str, eta: list[int]) -> dict:
    """[x ^ y] with C: commutator (GU 12.26) or A: i*anticommutator (GU 12.27)."""
    if mode not in ("C", "A"):
        raise ValueError("mode must be 'C' or 'A'")
    out: dict = {}
    for (f, a), u in x.items():
        for (g, b), v in y.items():
            if f & g:
                continue
            c, z = blade_mul(a, b, eta)
            _, w = blade_mul(b, a, eta)
            k = (z - w) if mode == "C" else (z + w)
            if k:
                coeff = u * v * (reorder_sign(f, g) * k)
                _add(out, (f | g, c), coeff * I if mode == "A" else coeff)
    return out


def right_mul_volume(x: dict, phase: GQ, eta: list[int]) -> dict:
    """Right-multiply the Clifford factor by phase * G_0 G_1 ... G_{n-1}."""
    full = (1 << len(eta)) - 1
    out: dict = {}
    for (f, a), v in x.items():
        c, z = blade_mul(a, full, eta)
        _add(out, (f, c), v * phase * z)
    return out


def blade_to_mono(blade: int, gs):
    """The Mono for the increasing product of gammas in `blade`."""
    from gu.clifford import Mono
    out = Mono.identity(gs[0].n)
    for i in bits(blade):
        out = out @ gs[i]
    return out


@lru_cache(maxsize=None)
def chirality_phase(p: int, q: int) -> GQ:
    """The phase k with gu.clifford.chirality(p, q) == k * G_0...G_{n-1}."""
    from gu.clifford import chirality, gammas
    gs = gammas(p, q)
    vol = blade_to_mono((1 << (p + q)) - 1, gs)
    C = chirality(p, q)
    for k, ph in enumerate((GQ(1), I, GQ(-1), -I)):
        if vol.times_i_power(k) == C:
            return ph
    raise AssertionError("chirality is not a phase times the volume blade")
```

- [ ] **Step 4: Run the tests**

Run: `uv run pytest tests/test_cliffform.py -q`
Expected: `20 passed`.

- [ ] **Step 5: Seeded faults (P2).** Apply each fault, run the file, confirm assertion failures, then restore and verify by SHA-256:
  - In `exact`, return `Fraction(x)` for integers (no `int(...)`). Expected: `test_gq_numpy_integers_cannot_overflow` fails.
  - In `blade_mul`, replace `s *= eta[i]` with `s *= 1`. Expected: `test_blade_mul_matches_mono_*`, `test_bracket_hand_values_3_1` and `test_right_mul_volume_is_mono_product` fail (Claude saw 7 failures).
  - In `reorder_sign`, return `1` unconditionally. Expected: `test_reorder_sign_hand_values` and the Mono and Hodge comparisons fail.
  - In `bracket`, drop the `* I` for mode `"A"`. Expected: `test_bracket_hand_values_3_1` fails.

  Record the table in `result.md`.

- [ ] **Step 6: Commit**

```bash
git add -- gu/cliffform.py tests/test_cliffform.py
git commit -m "Add sparse exact Lambda (x) Cl engine with Mono/Hodge adapter controls" -- gu/cliffform.py tests/test_cliffform.py
```
(With the Codex trailer.)

---

### Task 2: The undressed operator, Φ bases and the Spin action

**Files:**
- Create: `gu/shiab.py` (the part above the `# ---- dressing` marker)
- Test: `tests/test_shiab.py`

**Interfaces:**
- Consumes: Task 1; `gu.adjoint.{from_mono, is_in_algebra}`; `gu.clifford.dirac_pairing`; `gu.curvature.{kulkarni_nomizu, ricci, scalar}`.
- Produces:
  - `eta_of(p, q)`;
  - `phi_basis(p, q) -> {"F", "F'", "B", "B'"}`;
  - `xi(R, eta)`;
  - `shiab_parts(phi1, phi2, x, eta) -> {"first": {m}, "second": {m1m2}}`;
  - `assemble(parts, modes)`;
  - `shiab(phi1, phi2, x, modes, eta)`, which returns an (n−1)-form;
  - `generator_action(x, a, b, eta)`;
  - `embed_tensor(H, alpha, beta, p, q)`.

- [ ] **Step 1: Write the tests** (`tests/test_shiab.py`):

```python
# tests/test_shiab.py
"""B02 claims about GU (9.3). Scope tags per P1; small signature first (P5)."""
import itertools
from fractions import Fraction

import numpy as np
import pytest

from gu.adjoint import from_mono, is_in_algebra
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import GQ, I, blade_to_mono, bits, plus, scale, star
from gu.curvature import kulkarni_nomizu, ricci, scalar
from gu.shiab import (embed_tensor, eta_of, generator_action, phi_basis, shiab,
                      shiab_parts, xi)

SIGS = [(3, 1), (7, 7), (9, 5)]


def _in_u_A(x: dict, p: int, q: int) -> bool:
    """x is u(A)-valued. Distinct blades are linearly independent and each blade is
    sharp-even or sharp-odd, so this holds iff every coefficient is purely real or
    purely imaginary with the phase its blade requires (sign is irrelevant)."""
    gs, A = gammas(p, q), from_mono(dirac_pairing(p, q))
    for (f, c), v in x.items():
        if v.re and v.im:
            return False
        if not is_in_algebra(from_mono(blade_to_mono(c, gs).times_i_power(1 if v.im else 0)), A):
            return False
    return True


@pytest.mark.parametrize("p,q", SIGS)
def test_phi_bases_are_u_A_valued(p, q):
    """Test 2(b), scope: identity (every coefficient checked)."""
    for name, phi in phi_basis(p, q).items():
        assert _in_u_A(phi, p, q), name


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7)])
def test_impostors_outside_u_A_are_rejected(p, q):
    """P2b impostors: right shape, wrong phase."""
    phis = phi_basis(p, q)
    assert not _in_u_A(scale(phis["F"], I), p, q)       # i F
    assert not _in_u_A(scale(phis["B'"], -I), p, q)     # B C without the i
    assert not _in_u_A({(1, 1): GQ(1, 1)}, p, q)         # mixed phase on one blade


@pytest.mark.parametrize("p,q", SIGS)
def test_phi_bases_are_spin_invariant(p, q):
    """Test 4(i), scope: identity (identity component; all 13 adjacent generators)."""
    eta, n = eta_of(p, q), p + q
    for name, phi in phi_basis(p, q).items():
        for a in range(n - 1):
            assert generator_action(phi, a, a + 1, eta) == {}, (name, a)


@pytest.mark.parametrize("p,q", SIGS)
def test_index_raised_impostor_is_not_invariant(p, q):
    """P2b impostor: sum e^a (x) eta_a G_a has the right grades but is not invariant."""
    eta, n = eta_of(p, q), p + q
    bad = {(1 << a, 1 << a): GQ(eta[a]) for a in range(n)}
    assert any(generator_action(bad, a, a + 1, eta) for a in range(n - 1))


@pytest.mark.parametrize("p,q", SIGS)
def test_star_is_equivariant(p, q):
    """Test 4(ii), scope: identity on the degrees (9.3) uses (full bases)."""
    eta, n = eta_of(p, q), p + q
    for k in sorted({0, 1, 2, n - 2, n - 1, n}):
        for idx in itertools.combinations(range(n), k):
            w = {(sum(1 << i for i in idx), 0): GQ(1)}
            for a in range(n - 1):
                assert star(generator_action(w, a, a + 1, eta), eta) == \
                    generator_action(star(w, eta), a, a + 1, eta)


def _sym_basis(n):
    out = []
    for i in range(n):
        for j in range(i, n):
            s = np.zeros((n, n), dtype=np.int64)
            s[i, j] = s[j, i] = 1
            out.append(s)
    return out


def predicted(R, eta, modes, al, be, ga, de, p, q):
    """Closed form (hand-derived, review derivation.md; extended bilinearly):
    *shiab(xi) = -[m0=C] E_T(Ric) + S/2 ([m1m2=AA] ga E_T(g) + [m1m2=AC] de E_T'(g)),
    with T = (al, be), T' = (be, al)."""
    n = len(eta)
    g = np.diag(eta).astype(np.int64)
    out = {}
    if modes[0] == "C":
        out = plus(out, scale(embed_tensor(ricci(R, eta), al, be, p, q), -1))
    S = Fraction(int(scalar(R, eta)), 2)
    if modes[1:] == "AA":
        out = plus(out, scale(embed_tensor(g, al, be, p, q), S * ga))
    if modes[1:] == "AC":
        out = plus(out, scale(embed_tensor(g, be, al, p, q), S * de))
    return out


@pytest.mark.parametrize("p,q", [(3, 1)])
def test_response_closed_form_on_spanning_set_small(p, q):
    """Test 5, scope: identity for (3,1) on all KN products of a symmetric basis
    (spanning set; rank certified in tests/test_b02_response.py, Task 4)."""
    eta = eta_of(p, q)
    phis = phi_basis(p, q)
    sym = _sym_basis(p + q)
    for s, t in itertools.combinations_with_replacement(range(len(sym)), 2):
        R = kulkarni_nomizu(sym[s], sym[t])
        x = xi(R, eta)
        for p1, (al, be) in (("F", (1, 0)), ("F'", (0, 1))):
            for p2, (ga, de) in (("B", (1, 0)), ("B'", (0, 1)), (None, (0, 0))):
                phi2 = phis[p2] if p2 else {}
                for modes in map("".join, itertools.product("CA", repeat=3)):
                    got = star(shiab(phis[p1], phi2, x, modes, eta), eta)
                    assert got == predicted(R, eta, modes, al, be, ga, de, p, q), (s, t, p1, p2, modes)


def test_shiab_parts_assemble_to_shiab():
    eta = eta_of(3, 1)
    phis = phi_basis(3, 1)
    R = kulkarni_nomizu(np.diag([1, 2, 0, 0]).astype(np.int64), np.eye(4, dtype=np.int64))
    x = xi(R, eta)
    parts = shiab_parts(phis["F"], phis["B"], x, eta)
    for modes in map("".join, itertools.product("CA", repeat=3)):
        assert shiab(phis["F"], phis["B"], x, modes, eta) == \
            plus(parts["first"][modes[0]], scale(parts["second"][modes[1:]], Fraction(-1, 2)))


def _R31():
    h = np.diag([1, 2, 0, -1]).astype(np.int64)
    k = np.zeros((4, 4), dtype=np.int64)
    k[0, 1] = k[1, 0] = 1
    k[2, 2] = 3
    return kulkarni_nomizu(h, k)


MODES = ["".join(m) for m in itertools.product("CA", repeat=3)]


def test_mixed_phi_matches_formula():
    """Control on the bilinear extension: a genuinely mixed Phi1, Phi2 (argon review)."""
    p, q = 3, 1
    eta, phis, R = eta_of(p, q), phi_basis(p, q), _R31()
    phi1 = plus(scale(phis["F"], 2), scale(phis["F'"], -3))
    phi2 = plus(scale(phis["B"], 5), scale(phis["B'"], 7))
    x = xi(R, eta)
    assert x
    for m in MODES:
        assert star(shiab(phi1, phi2, x, m, eta), eta) == predicted(R, eta, m, 2, -3, 5, 7, p, q), m


def test_shiab_is_equivariant_end_to_end():
    """Test 4, scope: sampled direct check of the composition proof (argon review);
    includes a non-Levi-Civita gauge term."""
    p, q = 3, 1
    eta, phis = eta_of(p, q), phi_basis(p, q)
    x = plus(xi(_R31(), eta), {(0b11, 0b111): GQ(0, 1)})
    for m in MODES:
        for a in range(3):
            assert generator_action(shiab(phis["F"], phis["B'"], x, m, eta), a, a + 1, eta) == \
                shiab(phis["F"], phis["B'"], generator_action(x, a, a + 1, eta), m, eta)


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_outputs_stay_in_u_A(p, q):
    """Test 2, scope: sampled direct check of the closure proof on shiab outputs."""
    eta, phis, n = eta_of(p, q), phi_basis(p, q), p + q
    s = np.zeros((n, n), dtype=np.int64)
    s[0, 1] = s[1, 0] = 1
    t = np.diag([1, 2, 3] + [0] * (n - 3)).astype(np.int64)
    t[0, 2] = t[2, 0] = 1
    x = plus(xi(kulkarni_nomizu(s, t), eta), {(0b11, 0b111): GQ(0, 1)})
    assert x and _in_u_A(x, p, q)
    nonzero = 0
    for m in (MODES if n == 4 else ["CCC", "CAA", "CAC"]):
        for k1, k2 in itertools.product(["F", "F'"], ["B", "B'"]):
            out = shiab(phis[k1], phis[k2], x, m, eta)
            assert _in_u_A(out, p, q), (m, k1, k2)
            nonzero += bool(out)
    assert nonzero > 0


def test_adapters_take_exact_rationals_and_reject_floats():
    """Exactness controls (review R2, P4)."""
    eta = eta_of(3, 1)
    half = Fraction(1, 2)
    R = np.zeros((4, 4, 4, 4), dtype=object)
    R[:] = 0
    R[0, 1, 0, 1] = R[1, 0, 1, 0] = half
    R[0, 1, 1, 0] = R[1, 0, 0, 1] = -half
    assert xi(R, eta) == {(0b11, 0b11): GQ(Fraction(1, 4))}    # 1/2 * R_0101 * eta0 eta1
    H = np.zeros((4, 4), dtype=object)
    H[:] = 0
    H[0, 0] = half
    assert embed_tensor(H, 1, 0, 3, 1) == {(1, 1): GQ(half)}
    with pytest.raises(TypeError):
        xi(np.full((4, 4, 4, 4), 0.5), eta)
    with pytest.raises(TypeError):
        embed_tensor(np.diag([1.9, 0.0, 0.0, 0.0]), 1, 0, 3, 1)
```

- [ ] **Step 2: Run them and see them fail**

Run: `uv run pytest tests/test_shiab.py -q`
Expected: `ModuleNotFoundError: No module named 'gu.shiab'`.

- [ ] **Step 3: Implement** (`gu/shiab.py`, undressed part):

```python
# gu/shiab.py
"""GU (9.3), undressed (epsilon = 1), on sparse Lambda (x) Cl elements.

Pinned conventions (experiments/B02/ansatz.md, amendment 1):
  e^{ab} = e^a ^ e^b and G_{ab} = G_a G_b for a < b; all sums over increasing sets;
  xi(R) = 1/2 sum_{a<b, c<d} R_abcd eta_c eta_d e^{ab} (x) G_c G_d;
  F = sum e^a G_a, F' = F*C, B = sum e^{ab} G_a G_b, B' = B*(i C), C = gu chirality;
  E_T(H) = sum e^a (x) H_a^b T_b with T_b = alpha G_b + beta G_b C (2nd index raised).
"""
from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np

from gu.cliffform import (GQ, I, bracket, chirality_phase, clean, exact, plus, reorder_sign,
                          right_mul_volume, scale, star)


def eta_of(p: int, q: int) -> list[int]:
    return [1] * p + [-1] * q


def phi_basis(p: int, q: int) -> dict[str, dict]:
    """Real bases of the Spin-invariant spaces: F, F' (degree 1) and B, B' (degree 2)."""
    eta, n = eta_of(p, q), p + q
    cph = chirality_phase(p, q)
    F = {(1 << a, 1 << a): GQ(1) for a in range(n)}
    B = {((1 << a) | (1 << b), (1 << a) | (1 << b)): GQ(1)
         for a, b in itertools.combinations(range(n), 2)}
    return {"F": F, "F'": right_mul_volume(F, cph, eta),
            "B": B, "B'": right_mul_volume(B, I * cph, eta)}


def xi(R: np.ndarray, eta: list[int]) -> dict:
    """Entries must be exact integers or rationals (floats raise TypeError)."""
    n = len(eta)
    out = {}
    for a, b in itertools.combinations(range(n), 2):
        for c, d in itertools.combinations(range(n), 2):
            r = exact(R[a, b, c, d])
            if r:
                out[((1 << a) | (1 << b), (1 << c) | (1 << d))] = GQ(r * eta[c] * eta[d] / 2)
    return out


def shiab_parts(phi1: dict, phi2: dict, x: dict, eta: list[int]) -> dict:
    """The six bracket pieces of (9.3), before assembly.

    first[m0] = [phi1 ^ *x]_m0;  second[m1+m2] = *[phi1 ^ *[phi2 ^ *x]_m1]_m2.
    """
    sx = star(x, eta)
    first = {m: bracket(phi1, sx, m, eta) for m in "CA"}
    inner = {m: star(bracket(phi2, sx, m, eta), eta) for m in "CA"}
    second = {m1 + m2: star(bracket(phi1, inner[m1], m2, eta), eta) for m1 in "CA" for m2 in "CA"}
    return {"first": first, "second": second}


def assemble(parts: dict, modes: str) -> dict:
    """(9.3): first[m0] - (1/2) * second[m1+m2]. The only place the -1/2 lives."""
    if len(modes) != 3 or set(modes) - {"C", "A"}:
        raise ValueError("modes must be three of 'C'/'A'")
    return plus(parts["first"][modes[0]], scale(parts["second"][modes[1:]], Fraction(-1, 2)))


def shiab(phi1: dict, phi2: dict, x: dict, modes: str, eta: list[int]) -> dict:
    """(9.3) with epsilon = 1; `modes` = brackets for (Ricci term, inner, outer).

    Returns an ad-valued (n-1)-form.
    """
    return assemble(shiab_parts(phi1, phi2, x, eta), modes)


def generator_action(x: dict, a: int, b: int, eta: list[int]) -> dict:
    """Infinitesimal Spin(p,q) action of X = 1/2 G_a G_b (a < b) on Lambda (x) Cl.

    On the Clifford factor: ad_X. On vectors this gives E_b -> eta_b E_a, E_a -> -eta_a E_b,
    so on covectors (dual, minus transpose): e^a -> -eta_b e^b, e^b -> eta_a e^a,
    extended to forms as a derivation.
    """
    if not a < b:
        raise ValueError("need a < b")
    X = {(0, (1 << a) | (1 << b)): GQ(Fraction(1, 2))}
    cl = bracket(X, x, "C", eta)
    fm: dict = {}
    for (f, c), v in x.items():
        for src, dst, s in ((a, b, -eta[b]), (b, a, eta[a])):
            if f >> src & 1 and not f >> dst & 1:
                g = f ^ (1 << src)                  # remove e^src at its sorted slot
                sign_out = reorder_sign(1 << src, g)  # e^src ^ rest -> sorted f
                sign_in = reorder_sign(1 << dst, g)
                fm = plus(fm, {(g | (1 << dst), c): v * (s * sign_out * sign_in)})
    return plus(cl, fm)


def embed_tensor(H: np.ndarray, alpha, beta, p: int, q: int) -> dict:
    """E_T(H) = sum e^a (x) H_a^b (alpha G_b + beta G_b C)."""
    eta, n = eta_of(p, q), p + q
    base = clean({(1 << a, 1 << b): GQ(exact(H[a, b]) * eta[b])
                  for a in range(n) for b in range(n) if exact(H[a, b])})
    return plus(scale(base, alpha), scale(right_mul_volume(base, chirality_phase(p, q), eta), beta))
```

- [ ] **Step 4: Run the tests**

Run: `uv run pytest tests/test_shiab.py -q`
Expected: `22 passed` (about 1.5 minutes; the 14D u(A) membership checks dominate).

- [ ] **Step 5: Seeded faults (P2).** Each must fail an assertion:
  - In `xi`, replace `exact(R[a, b, c, d])` with `int(R[a, b, c, d])`. Expected: `test_adapters_take_exact_rationals_and_reject_floats` fails.
  - In `assemble`, `Fraction(-1, 2)` → `Fraction(1, 2)`. Expected: `test_response_closed_form_on_spanning_set_small` and `test_shiab_parts_assemble_to_shiab` fail.
  - In `generator_action`, `-eta[b]` → `eta[b]`. Expected: `test_phi_bases_are_spin_invariant` and `test_star_is_equivariant` fail.
  - In `phi_basis`, `I * cph` → `cph` (B′ = B·C without the i). Expected: `test_phi_bases_are_u_A_valued` fails.

- [ ] **Step 6: Commit**

```bash
git add -- gu/shiab.py tests/test_shiab.py
git commit -m "Add undressed GU (9.3) operator, invariant Phi bases and Spin action" -- gu/shiab.py tests/test_shiab.py
```

---

### Task 3: Sparse dressing, covariance samples, open data

**Files:**
- Modify: `gu/shiab.py` (append the dressing section)
- Test: `tests/test_dressing.py`

**Interfaces:**
- Consumes: Task 2; `gu.adjoint.{cayley, from_mono, is_in_group}`; `flint.{fmpq, fmpq_mat}`.
- Produces:
  - `left(u, x, eta)` and `right(x, u, eta)`, where u is a 0-form Clifford element;
  - `cayley_blade(blade, t, eta) -> (h, h_inv)`;
  - `shiab_dressed(phi1, phi2, x, modes, eta, eps, eps_inv)`.

- [ ] **Step 1: Write the tests** (`tests/test_dressing.py`):

```python
# tests/test_dressing.py
"""B02 test 3(b) (sampled) and 5' (open data); sparse Cayley adapter controls."""
import itertools
from fractions import Fraction

import pytest
from flint import fmpq, fmpq_mat

from gu.adjoint import cayley, from_mono, is_in_group
from gu.clifford import dirac_pairing, gammas
from gu.cliffform import GQ, I, blade_to_mono, plus
from gu.curvature import kulkarni_nomizu
from gu.shiab import cayley_blade, eta_of, left, phi_basis, right, shiab, shiab_dressed, xi


def dense(u: dict, p: int, q: int) -> fmpq_mat:
    """Adapter: sparse 0-form Clifford element -> gu.adjoint real embedding."""
    gs = gammas(p, q)
    out = None
    for (f, b), v in u.items():
        assert f == 0
        m = blade_to_mono(b, gs)
        term = from_mono(m) * fmpq(v.re.numerator, v.re.denominator) + \
            from_mono(m.times_i_power(1)) * fmpq(v.im.numerator, v.im.denominator)
        out = term if out is None else out + term
    return out


HALF = GQ(Fraction(1, 2))
# (blade, coefficient): elements of u(A): grade 1 real, grade 2 real, grade 3 imaginary.
GENERATORS = [(0b1, HALF), (0b11, HALF), (0b111, HALF * I), (0b1010, HALF), (0b1000, HALF)]


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_sparse_cayley_matches_library_cayley(p, q):
    """Positive adapter control (P2b): same matrix as gu.adjoint.cayley; in U(A)."""
    A = from_mono(dirac_pairing(p, q))
    eta = eta_of(p, q)
    for blade, t in GENERATORS:
        h, hinv = cayley_blade(blade, t, eta)
        assert dense(h, p, q) == cayley(dense({(0, blade): t}, p, q))
        assert is_in_group(dense(h, p, q), A)
        assert left(h, hinv, eta) == {(0, 0): GQ(1)}


def test_cayley_of_non_algebra_element_is_rejected():
    """P2b impostor: i*G_0 is not in u(A); its Cayley transform is not in U(A)."""
    p, q = 3, 1
    h, _ = cayley_blade(0b1, HALF * I, eta_of(p, q))
    assert not is_in_group(dense(h, p, q), from_mono(dirac_pairing(p, q)))


def _xi_samples(p, q):
    """General u(A)-valued 2-forms (not only Levi-Civita), plus one curvature input."""
    import numpy as np
    eta = eta_of(p, q)
    n = p + q
    s = np.zeros((n, n), dtype=np.int64); s[0, 1] = s[1, 0] = 1
    t = np.diag([1, 2, 3] + [0] * (n - 3)).astype(np.int64); t[0, 2] = t[2, 0] = 1
    return [{(0b11, 0b101): GQ(1), (0b110, 0b1): GQ(2)},
            {(0b101, 0b111): GQ(0, 1)},
            xi(kulkarni_nomizu(s, t), eta)]


def test_xi_samples_are_nonzero():
    assert all(all(_xi_samples(*sig)) for sig in [(3, 1), (7, 7), (9, 5)])


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_dressed_covariance_samples(p, q):
    """Test 3(b), scope: sampled. Shiab_{eps h}(h^-1 xi h) == h^-1 Shiab_eps(xi) h."""
    eta = eta_of(p, q)
    phis = phi_basis(p, q)
    hs = [cayley_blade(b, t, eta) for b, t in GENERATORS[:3]]
    epss = [cayley_blade(b, t, eta) for b, t in GENERATORS[3:]]
    modes = ["CAA", "CCC", "ACA"] if p + q == 4 else ["CAA"]   # 14D: keep the suite fast
    for (h, hi), (e, ei), x, m in itertools.product(hs, epss, _xi_samples(p, q), modes):
        eh, ehi = left(e, h, eta), left(hi, ei, eta)
        lhs = shiab_dressed(phis["F"], phis["B"], left(hi, right(x, h, eta), eta), m, eta, eh, ehi)
        rhs = left(hi, right(shiab_dressed(phis["F"], phis["B"], x, m, eta, e, ei), h, eta), eta)
        assert lhs == rhs


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7)])
def test_central_dressing_is_a_no_op(p, q):
    """Control: eps = Cayley(i/2 * I) is central in U(A), so conjugation is trivial.
    (A Spin-image eps is NOT a no-op: Phi is invariant only under the joint action
    on form and Clifford factors, while dressing acts on the Clifford factor alone.)"""
    eta = eta_of(p, q)
    phis = phi_basis(p, q)
    e, ei = cayley_blade(0, HALF * I, eta)
    assert is_in_group(dense(e, p, q), from_mono(dirac_pairing(p, q)))
    for x in _xi_samples(p, q):
        assert shiab_dressed(phis["F"], phis["B"], x, "CAA", eta, e, ei) == shiab(phis["F"], phis["B"], x, "CAA", eta)


@pytest.mark.parametrize("p,q", [(3, 1), (7, 7), (9, 5)])
def test_open_data_weyl_under_non_spin_dressing(p, q, record_property):
    """Test 5', scope: sampled, open data (no expectation). Records whether
    Shiab_eps(xi(W)) vanishes for odd eps (outside the even Spin image)."""
    import numpy as np
    from gu.curvature import is_algebraic_curvature, ricci
    eta, n = eta_of(p, q), p + q
    W = np.zeros((n, n, n, n), dtype=np.int64)
    for a, b, val in [(0, 1, 1), (2, 3, 1), (0, 2, -1), (1, 3, -1)]:
        val *= eta[a] * eta[b]
        W[a, b, a, b] = W[b, a, b, a] = val
        W[a, b, b, a] = W[b, a, a, b] = -val
    assert is_algebraic_curvature(W) and not np.any(ricci(W, eta))
    phis = phi_basis(p, q)
    x = xi(W, eta)
    assert shiab(phis["F"], phis["B"], x, "CAA", eta) == {}       # undressed: annihilated
    for blade, t in [(0b1, HALF), (0b111, HALF * I)]:
        e, ei = cayley_blade(blade, t, eta)
        out = shiab_dressed(phis["F"], phis["B"], x, "CAA", eta, e, ei)
        record_property(f"weyl_{blade:b}", "zero" if not out else f"nonzero({len(out)} terms)")
        print(p, q, bin(blade), "zero" if not out else f"nonzero ({len(out)} terms)")
```

- [ ] **Step 2: Run them and see them fail**

Run: `uv run pytest tests/test_dressing.py -q`
Expected: `ImportError: cannot import name 'cayley_blade' from 'gu.shiab'`.

- [ ] **Step 3: Append to `gu/shiab.py`:**

```python
# ---- dressing (GU 8.1: epsilon acts on the bundle factor by conjugation) ----

def left(u: dict, x: dict, eta: list[int]) -> dict:
    """u * x, where u is a 0-form Clifford element {(0, blade): GQ}."""
    out: dict = {}
    for (f0, b), uv in u.items():
        if f0:
            raise ValueError("left factor must be a 0-form")
        for (f, a), xv in x.items():
            c, s = blade_mul(b, a, eta)
            out = plus(out, {(f, c): uv * xv * s})
    return out


def right(x: dict, u: dict, eta: list[int]) -> dict:
    """x * u, where u is a 0-form Clifford element."""
    out: dict = {}
    for (f0, b), uv in u.items():
        if f0:
            raise ValueError("right factor must be a 0-form")
        for (f, a), xv in x.items():
            c, s = blade_mul(a, b, eta)
            out = plus(out, {(f, c): uv * xv * s})
    return out


def cayley_blade(blade: int, t: GQ, eta: list[int]) -> tuple[dict, dict]:
    """(h, h^-1) for h = (1 - X)(1 + X)^-1 with X = t * G_blade.

    X^2 = t^2 * sq is a scalar, so (1 + X)^-1 = (1 - X) / (1 - t^2 sq) and
    h = (1 - X)^2 / (1 - t^2 sq), h^-1 = (1 + X)^2 / (1 - t^2 sq).
    """
    _, sq = blade_mul(blade, blade, eta)
    d = GQ(1) - t * t * sq
    if not d:
        raise ZeroDivisionError("1 + X is singular")
    one, X = {(0, 0): GQ(1)}, {(0, blade): t}
    sq_minus = left(plus(one, scale(X, -1)), plus(one, scale(X, -1)), eta)
    sq_plus = left(plus(one, X), plus(one, X), eta)
    return scale(sq_minus, GQ(1) / d), scale(sq_plus, GQ(1) / d)


def shiab_dressed(phi1, phi2, x, modes, eta, eps, eps_inv):
    """(9.3) with Phi^i replaced by eps^-1 Phi^i eps."""
    c1 = left(eps_inv, right(phi1, eps, eta), eta)
    c2 = left(eps_inv, right(phi2, eps, eta), eta)
    return shiab(c1, c2, x, modes, eta)
```

and add `blade_mul` to the `gu.cliffform` import in `gu/shiab.py`.

- [ ] **Step 4: Run the tests**

Run: `uv run pytest tests/test_dressing.py -q -s`
Expected: `13 passed` (about 2 minutes). The 5′ test prints one zero/nonzero line per case; this is open data, with no expectation.

- [ ] **Step 5: Seeded faults (P2):**
  - In `shiab_dressed`, conjugate as `left(eps, right(phi, eps_inv))`, i.e. the inverse placed wrongly. Expected: `test_dressed_covariance_samples` fails.
  - In `cayley_blade`, swap the returned pair. Expected: `test_sparse_cayley_matches_library_cayley` fails.

- [ ] **Step 6: Commit**

```bash
git add -- tests/test_dressing.py
git commit -m "Add sparse Cayley dressings: covariance samples and Weyl open data" -- gu/shiab.py tests/test_dressing.py
```

---

### Task 4: Identity-scope response check and `result.json`

**Files:**
- Create: `experiments/B02/__init__.py` (empty), `experiments/B02/response.py`, `experiments/B02/run.py`
- Test: `tests/test_b02_response.py`
- Generated: `experiments/B02/result.json`

**Interfaces:**
- Consumes: Tasks 1–3; `gu.curvature.{dims, kulkarni_nomizu, ricci, scalar, is_algebraic_curvature}`; `flint.nmod_mat`.
- Produces: `result.json` with keys `scope`, `formula`, `spanning_rank` (`"4"`, `"14"`), `response` (one row per signature: `inputs`, `cases`, `nonzero_outputs`), `open_data_5prime`, `versions`, `source_commit`, `command`.

- [ ] **Step 1: Write `experiments/B02/response.py`:**

```python
# experiments/B02/response.py
"""Test 5 at identity scope: the closed-form response of (9.3) on a spanning set.

For every R = KN(s, t) over unordered pairs of a symmetric basis (5565 tensors at
n = 14, rank 3185 = dim of algebraic curvature tensors, checked in spanning_rank),
every bracket assignment, Phi1 in {F, F'} and Phi2 in {B, B', 0}, assert
  *shiab(xi(R)) == -[m0=C] E_T(Ric) + S/2 ([m1m2=AA] ga E_T(g) + [m1m2=AC] de E_T'(g)).
By multilinearity in (Phi1, Phi2) this proves the formula for every real
(alpha, beta, gamma, delta) and, by linearity in R, on all algebraic curvature.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import numpy as np
from flint import nmod_mat

from gu.cliffform import plus, scale, star
from gu.curvature import dims, is_algebraic_curvature, kulkarni_nomizu, ricci, scalar
from gu.shiab import assemble, embed_tensor, eta_of, phi_basis, shiab_parts, xi

MODES = ["".join(m) for m in itertools.product("CA", repeat=3)]
PRIME = 1_000_003


def sym_basis(n: int) -> list[np.ndarray]:
    """s_ij = E_ij + E_ji for i < j, and s_ii = E_ii (diagonal entry 1, not 2)."""
    out = []
    for i in range(n):
        for j in range(i, n):
            s = np.zeros((n, n), dtype=np.int64)
            s[i, j] = s[j, i] = 1
            out.append(s)
    return out


def spanning_pairs(n: int) -> list[tuple[int, int]]:
    return list(itertools.combinations_with_replacement(range(n * (n + 1) // 2), 2))


def spanning_rank(n: int) -> tuple[int, int]:
    """(rank mod PRIME of the KN products, dim of algebraic curvature tensors).

    rank mod p <= rank over Q <= dim, so equality certifies spanning over Q, provided
    every row is an algebraic curvature tensor (the chart is Sym^2(Lambda^2), which has
    C(n,4) more coordinates than dim: 1 at n = 4, 1001 at n = 14; asserted below).
    """
    sym = sym_basis(n)
    cols = [(a, b, c, d) for a, b in itertools.combinations(range(n), 2)
            for c, d in itertools.combinations(range(n), 2) if (a, b) <= (c, d)]
    rows = []
    for s, t in spanning_pairs(n):
        R = kulkarni_nomizu(sym[s], sym[t])
        if not is_algebraic_curvature(R):
            raise AssertionError(f"KN product {(s, t)} is not algebraic")
        rows.append([int(R[k]) % PRIME for k in cols])
    return nmod_mat(rows, PRIME).rank(), sum(dims(n))


def check_signature(p: int, q: int, limit: int | None = None) -> dict:
    eta, n = eta_of(p, q), p + q
    g = np.diag(eta).astype(np.int64)
    phis = phi_basis(p, q)
    T = {"F": (1, 0), "F'": (0, 1)}
    Eg = {k: embed_tensor(g, *ab, p, q) for k, ab in T.items()}
    Eg_swap = {k: embed_tensor(g, ab[1], ab[0], p, q) for k, ab in T.items()}
    sym = sym_basis(n)
    pairs = spanning_pairs(n)[:limit]
    checked = nonzero = 0
    for s, t in pairs:
        R = kulkarni_nomizu(sym[s], sym[t])
        x = xi(R, eta)
        S = Fraction(int(scalar(R, eta)), 2)
        Ric = ricci(R, eta)
        for k1, (al, be) in T.items():
            ERic = embed_tensor(Ric, al, be, p, q)
            for k2, (ga, de) in (("B", (1, 0)), ("B'", (0, 1)), (None, (0, 0))):
                parts = shiab_parts(phis[k1], phis[k2] if k2 else {}, x, eta)
                for m in MODES:
                    raw = assemble(parts, m)
                    if any(f.bit_count() != n - 1 for f, _ in raw):
                        raise AssertionError(f"degree (test 1) at {(p, q, s, t, k1, k2, m)}")
                    got = star(raw, eta)
                    nonzero += bool(got)
                    want = scale(ERic, -1) if m[0] == "C" else {}
                    if m[1:] == "AA":
                        want = plus(want, scale(Eg[k1], S * ga))
                    if m[1:] == "AC":
                        want = plus(want, scale(Eg_swap[k1], S * de))
                    if got != want:
                        raise AssertionError(f"mismatch at {(p, q, s, t, k1, k2, m)}")
                    checked += 1
    return {"signature": [p, q], "inputs": len(pairs), "cases": checked, "nonzero_outputs": nonzero}


if __name__ == "__main__":
    p, q = int(sys.argv[1]), int(sys.argv[2])
    lim = int(sys.argv[3]) if len(sys.argv) > 3 else None
    print(check_signature(p, q, lim))
```

- [ ] **Step 2: Write `experiments/B02/run.py`:**

```python
# experiments/B02/run.py
"""Produce experiments/B02/result.json. Run: uv run python -m experiments.B02.run"""
from __future__ import annotations

import json
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np

from experiments.B02.response import check_signature, spanning_rank
from gu.cliffform import GQ, I, scale, star
from gu.curvature import is_algebraic_curvature, kulkarni_nomizu, ricci
from gu.shiab import cayley_blade, eta_of, phi_basis, shiab, shiab_dressed, xi

SIGNATURES = [(3, 1), (7, 7), (9, 5)]
HALF = GQ(1) / 2


def weyl_control(p: int, q: int) -> np.ndarray:
    """Sectional curvatures +-1 on an orthogonal 4-plane, Ricci-flat by construction."""
    eta, n = eta_of(p, q), p + q
    W = np.zeros((n, n, n, n), dtype=np.int64)
    for a, b, val in [(0, 1, 1), (2, 3, 1), (0, 2, -1), (1, 3, -1)]:
        val *= eta[a] * eta[b]
        W[a, b, a, b] = W[b, a, b, a] = val
        W[a, b, b, a] = W[b, a, a, b] = -val
    assert is_algebraic_curvature(W) and not np.any(ricci(W, eta))
    return W


def hand_control(p: int, q: int) -> bool:
    """Independent nonzero controls on KN(g, g): Ric = 2(n-1) g and S = 2n(n-1)
    (gu.curvature tests), and E_F(g) = F. With Phi1 = F, Phi2 = B:
      CCC (no scalar term): *shiab = -E_F(Ric) = -2(n-1) F;
      CAA (inner A on B gives i(S/2) I by hand; outer A doubles it; times -1/2):
          *shiab = -2(n-1) F + (S/2) F = (n-1)(n-2) F.  Built from F directly.
    The relative sign holds for q odd (every signature run here); for q even both
    hand values change (checked at (2,2), (4,0))."""
    eta, n = eta_of(p, q), p + q
    g = np.diag(eta).astype(np.int64)
    phis = phi_basis(p, q)
    x = xi(kulkarni_nomizu(g, g), eta)
    ccc = star(shiab(phis["F"], phis["B"], x, "CCC", eta), eta)
    caa = star(shiab(phis["F"], phis["B"], x, "CAA", eta), eta)
    return (bool(ccc) and ccc == scale(phis["F"], -2 * (n - 1))
            and bool(caa) and caa == scale(phis["F"], (n - 1) * (n - 2)))


def open_data(p: int, q: int) -> list[dict]:
    """Test 5': Shiab_eps(xi(W)) for odd eps (outside the even Spin image). No expectation."""
    eta = eta_of(p, q)
    phis = phi_basis(p, q)
    x = xi(weyl_control(p, q), eta)
    rows = []
    for blade, t, label in [(0b1, HALF, "Cayley(G_0/2)"), (0b111, HALF * I, "Cayley(i G_0 G_1 G_2/2)")]:
        e, ei = cayley_blade(blade, t, eta)
        for modes in ("CCC", "CAA"):
            out = shiab_dressed(phis["F"], phis["B"], x, modes, eta, e, ei)
            rows.append({"eps": label, "modes": modes, "phi": "F,B",
                         "undressed_zero": not shiab(phis["F"], phis["B"], x, modes, eta),
                         "dressed_zero": not out, "dressed_terms": len(out)})
    return rows


def main() -> None:
    out = {
        "scope": {"response": "identity (spanning set of algebraic curvature, all real Phi by multilinearity)",
                  "open_data": "sampled, no expectation"},
        "formula": "*shiab(xi) == -[m0=C] E_T(Ric) + S/2 ([m1m2=AA] gamma E_T(g) + [m1m2=AC] delta E_T'(g))",
        "spanning_rank": {},
        "response": [],
        "open_data_5prime": {},
    }
    for n in (4, 14):
        rank, dim = spanning_rank(n)
        assert rank == dim, (n, rank, dim)
        out["spanning_rank"][str(n)] = {"rank_mod_p": rank, "dim": dim}
    for p, q in SIGNATURES:
        row = check_signature(p, q)
        n_pairs = (p + q) * (p + q + 1) // 2
        assert row["inputs"] == n_pairs * (n_pairs + 1) // 2 and row["cases"] == 48 * row["inputs"], row
        assert row["nonzero_outputs"] > 0, row                     # Review Focus 2
        assert hand_control(p, q), (p, q)
        out["response"].append(row)
        out["open_data_5prime"][f"{p},{q}"] = open_data(p, q)
        print(f"done {(p, q)}", flush=True)
    out["versions"] = {"python": platform.python_version(), "numpy": np.__version__}
    out["source_commit"] = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    out["command"] = "uv run python -m experiments.B02.run"
    path = Path(__file__).with_name("result.json")
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Small case first (P5).** Write `tests/test_b02_response.py`:

```python
# tests/test_b02_response.py
"""Task 4 small-case permanents (P5): spanning certificate and response identity at n = 4."""
from experiments.B02.response import check_signature, spanning_rank
from experiments.B02.run import hand_control


def test_kn_products_span():
    """Certificate control: rank mod p of the 55 KN products = 20 = dim at n = 4."""
    assert spanning_rank(4) == (20, 20)


def test_response_identity_small():
    """Test 5, scope: identity for (3,1) (spanning set x all branches)."""
    row = check_signature(3, 1)
    assert row == {"signature": [3, 1], "inputs": 55, "cases": 2640, "nonzero_outputs": 912}


def test_hand_control():
    """Independent nonzero control (KN(g, g), CCC, Phi1 = F)."""
    assert hand_control(3, 1)
```

Run: `uv run python -m experiments.B02.response 3 1`
Expected: `{'signature': [3, 1], 'inputs': 55, 'cases': 2640, 'nonzero_outputs': 912}`

Run: `uv run pytest tests/test_b02_response.py -q`
Expected: `3 passed`.

- [ ] **Step 4: Seeded fault against the checker (Review Focus 1).** In `gu/shiab.py` `assemble`, set `Fraction(1, 2)`, then rerun Step 3.
Expected: `AssertionError: mismatch at (3, 1, 0, 4, 'F', 'B', 'CAA')`.
Restore and verify by SHA-256.

- [ ] **Step 5: Commit the code before running (P8)**

```bash
git add -- experiments/B02/__init__.py experiments/B02/response.py experiments/B02/run.py tests/test_b02_response.py
git commit -m "B02: identity-scope response checker and result runner" -- experiments/B02/__init__.py experiments/B02/response.py experiments/B02/run.py tests/test_b02_response.py
```

Then check `git status --short gu experiments/B02 tests`: it must show no changes to tracked files.

- [ ] **Step 6: Run** (about 10 minutes)

Run: `uv run python -m experiments.B02.run`
Expected:
- `spanning_rank` gives `{"4": {"rank_mod_p": 20, "dim": 20}, "14": {"rank_mod_p": 3185, "dim": 3185}}`;
- three `response` rows with `cases` of 2640, 267120 and 267120 respectively, each with `nonzero_outputs` > 0;
- the script exits 0. The runner itself asserts the case counts, `nonzero_outputs > 0` and the hand control (Review Focus 2). A mismatch raises `AssertionError` naming the case: **stop and report it (P3); do not edit the formula.**

- [ ] **Step 7: Commit the result**

```bash
git add -- experiments/B02/result.json
git commit -m "B02: result.json (response identity check, spanning ranks, 5' open data)" -- experiments/B02/result.json
```

- [ ] **Step 8: Full suite.** Run `uv run pytest -q`. Expected: `222 passed` (about 4 minutes).

---

### Task 5 (Claude): Proofs for tests 1, 2(a), 3(a), 4(iii) and the bilinear extension

**Files:**
- Create: `experiments/B02/proofs.md`

Codex then checks it adversarially (a brief, with a `result.md`).

- [ ] **Step 1: Write the proofs.**
  - **Test 1 (degree):** form degrees are independent of Clifford coefficients. ∗: Ω² → Ω¹², wedge with Ω¹ gives Ω¹³; the second term gives Ω¹⁴ → Ω⁰ → Ω¹ → Ω¹³. `response.py` also asserts the degree on every assembled output.
  - **Test 2(a) (real form):** if X♯ = −X and Y♯ = −Y, then [X,Y]♯ = −[X,Y] and (i(XY+YX))♯ = −i(XY+YX). Together with Φ ∈ 𝔲(A) (Task 2) and real Hodge coefficients (the `star` signs are ±1), the outputs are 𝔲(A)-valued for every 𝔲(A)-valued input.
  - **Test 3(a) (covariance):** (εh)⁻¹Φ(εh) = h⁻¹(ε⁻¹Φε)h. Conjugation by h is an algebra automorphism, so it commutes with both brackets. ∗ and the wedge act on the form factor only. Hence Shiab_{εh}(h⁻¹ξh) = h⁻¹Shiab_ε(ξ)h.
  - **Test 4 (equivariance, identity component):** the generators act as derivations of the wedge (form factor) and as ad_X, a derivation of the Clifford product, so they act as derivations of both brackets. ∗ is equivariant (Task 2, on full bases). Φ is invariant (Task 2). Composing these gives equivariance of (9.3) for Spin₀(p,q).
  - **Parameter extension** (review: affine, not jointly bilinear). U(Φ¹, Φ²) = L(Φ¹) + B(Φ¹, Φ²) is linear in Φ¹ and affine in Φ². So U(F, γB + δB′) = (1−γ−δ)U(F, 0) + γU(F, B) + δU(F, B′), likewise for F′, and then combine in (α, β). The formula's right side has the same structure. Task 4 checks F, F′ × {B, B′, 0}, so the formula holds for all real (α, β, γ, δ). By linearity in R, it holds on all algebraic curvature tensors (spanning rank = dimension).
  - **Hodge convention (review G1):** let ∗′ = (−1)^{k(n−k)}∗ on k-forms (the convention ∗β ∧ α = ⟨α,β⟩vol). For even n, ∗′ = ∗ except on odd k. In (9.3) the stars act on degrees 2 (∗ξ), n (inner) and 1 (outer, inside the second term). Only the last of these flips, so Shiab′(Φ¹, Φ²) = Shiab(Φ¹, −Φ²) exactly, for every bracket assignment. The final ∗ on the (n−1)-form flips the overall sign of the response under ∗′; κ is unaffected. The star convention is therefore a reparametrization (γ, δ) → (−γ, −δ), not a new branch.
  - **Recorded substitutions:** the composition proof replaces the ansatz's literal operator-basis execution for test 4, which applies to Spin₀ only (no Pin/O claim). The full response identity replaces separate pure-sector executions for test 5. The `int()`-free adapters are needed for the executable code to accept rational curvature; the formal identity does not depend on them.

- [ ] **Step 2: Commit** with `git add -- experiments/B02/proofs.md`, then the pathspec commit. Then brief Codex to check it.

---

### Task 6: Reconciliation, verdict, register

**Files:**
- Create: `experiments/B02/README.md` (Claude)
- Modify: `docs/gaps/register.md` (Codex)

- [ ] **Step 1 (Claude): Classify κ from the verified formula.**

  On ξ, ∗Shiab = −[m₀=C]·E_T(Ric) + (S/2)·([m₁m₂=AA]·γ·E_T(g) + [m₁m₂=AC]·δ·E_{T′}(g)), with T = (α,β) and T′ = (β,α). The classification below is revision 2, corrected per review R3–R5 and checked by Codex's exact counterexamples. `result.json` does not contain κ. Derive κ from the formula that the runner asserts at identity scope; the classification below is a consequence of that formula, not something read off `result.json` (review G3). It holds for odd q, which covers every signature in this project; for even q, κ → −κ. For T ≠ 0:
  - **m₀ = A, or T = 0:** r_T = 0, so 5a fails and κ is **undefined** (not 0).
  - **CCC (literal) and CCA:** κ = 0 for every Φ; the scalar and traceless sectors are both nonzero.
  - **CAA:** κ = γ/2. The scalar response vanishes at γ = 2/n, which fails 5a. Einstein holds iff γ = 1 (N-a).
  - **CAC:** if δ = 0, κ = 0. Otherwise the same-embedding response needs β = sα with s = ±1. Then δE_{T′} = sδ·E_T, κ = sδ/2, the scalar response vanishes at sδ = 2/n, and Einstein holds iff sδ = 1. These Φ¹ = α(F ± F′) = Σeᵃ⊗αΓₐ(1 ± C) are chirally projected soldering forms, and they are null for the natural trace norm (review F4). Report them as such; this is not a headline.
  - **N-b domain (R3):** the inner A result is (S/2)(iγI − δC). Rescaling to exactly iS·I is possible only when the inner bracket is A, δ = 0 and γ ≠ 0. Then CAA has κ = 1 and CAC has κ = 0, so there is **no N-b Einstein branch**. Elsewhere, N-b is "unavailable".
  - **Which norm** (argon's clarification request; verified exactly in all three signatures with this plan's code). "The trace norm" means the Ad-invariant, complex-bilinear (no conjugate), indefinite form N(X) = Σ_I η_I Tr(X_I X_I)/dim S. Under it, N(αF + βF′) = n(α² − β²) and N(γB + δB′) = C(n,2)(δ² − γ²). The dual copies carry the opposite-sign norm, because (Γₐ C)² = −Γₐ² for odd Γₐ and (iC)² = −1 for even blades, and the cross terms are traceless. So F ± F′ and B ± B′ are null for one shared reason. A positive-definite norm such as Re Tr(X†Y) has no null directions, but it is not Ad-invariant for U(64,64).
  - **Norm filter:** the source names no norm. If null directions under the trace norm are excluded, apply this to Φ² as well, since B ± B′ is null (R5). CAA Einstein then additionally needs α² ≠ β² and δ ≠ ±1. Report both the filtered and unfiltered families; do not pick a norm silently.
  - **H0** (F, B, N-a, pinned star): CAA alone gives κ = ½. Confirm it as its own line, with all four qualifiers.
  - **Star branch (G1):** under the other Hodge convention ∗′, every γ and δ above changes sign (Task 5). So CAA Einstein holds iff γ = −1, and CAC Einstein holds iff sδ = −1. The pinned star is a choice, not a transcription; the convention map must say so.
  - **Scale (G2):** the source fixes neither the scale nor the sign of Φ² relative to Φ¹ ("normed" names no norm). With the spin generator σ_ab = ½Γ_aΓ_b as the unit 2-form, γ = ½ and κ = ¼. This still passes 5a at n = 14, since ½ ≠ 2/14. Under N-b, κ = 1. Under N-a, κ = ½.
  - **Open-data scope:** 5′ samples cover only F, B with CCC and CAA, and two odd dressings. Say so.

- [ ] **Step 2 (Claude): Write `README.md`.** Follow the structure of `experiments/B01/README.md`:
  - verdict lines per the ansatz rules (the literal reading; every reconstructed reading that passes; H0). Lead with the consequence that is stable under every convention (P9, review G2): literal CCC has no scalar term at any scale of ξ, Φ¹ or Φ², under either Hodge convention and either generator normalization, because the inner commutator is antisymmetric under pair exchange and R_abcd = R_cdab. Only then state that the Einstein point of CAA depends on the unit and sign of Φ²: γ = 1 under (N-a, pinned star), γ = −1 under ∗′, κ = ¼ under σ, and κ = 1 under N-b;
  - the convention map (P9: formula / normalization / consequence);
  - findings;
  - 3(b) and 5′ data;
  - "What this does not establish". This section covers non-Levi-Civita gauge curvature, where the inner-commutator cancellation needs pair symmetry, and the lost preferred operator (transcription P6).

- [ ] **Step 3 (Codex):** re-derive the README's classification independently, then update the B02 register entry with its three tags and links to tracked files only. Write the result to `.agent-handoff/<task>/result.md`.

- [ ] **Step 4 (Claude):** resolve any disagreements, add the retro entry to `docs/methods.md`, update `docs/HANDOFF.md`, and commit each with its own pathspec.
