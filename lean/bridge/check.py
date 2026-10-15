"""Compare the compiled Lean model with the actual GU Python implementation.

Run from the repository root: uv run python lean/bridge/check.py
No floating-point comparisons, saved golden values, or copied Python algorithms.
"""
from __future__ import annotations

import itertools
from fractions import Fraction
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import numpy as np
from gu.cliffform import GQ, I, bracket, chirality_phase, star
from gu.shiab import eta_of, generator_action, phi_basis, shiab, xi


def canonical(x):
    return tuple(sorted((f, b, v.re, v.im) for (f, b), v in x.items() if v))


def curvature():
    """Pair-symmetric algebraic curvature with R_0103=R_0301=1."""
    out = np.zeros((4, 4, 4, 4), dtype=object)
    for a, b, c, d in ((0, 1, 0, 3), (0, 3, 0, 1)):
        for aa, bb, s in ((a, b, 1), (b, a, -1)):
            for cc, dd, t in ((c, d, 1), (d, c, -1)):
                out[aa, bb, cc, dd] = s * t
    return out


def expected_cases():
    eta = eta_of(3, 1)
    phase = chirality_phase(3, 1)
    cases = {"phase": {(0, 0): phase}}
    for f in range(16):
        for b in range(16):
            cases[f"star_{f}_{b}"] = star({(f, b): GQ(2, -3)}, eta)
    # Every Clifford blade pair, including metric repetitions and mixed signs;
    # four form pairs exercise positive/negative wedge signs and zero overlaps.
    for f, g in ((0, 0), (1, 2), (2, 1), (3, 1)):
        for a in range(16):
            for b in range(16):
                for m in "CA":
                    cases[f"bracket_{f}_{g}_{a}_{b}_{m}"] = bracket(
                        {(f, a): GQ(Fraction(2, 3), -1)},
                        {(g, b): GQ(-2, Fraction(1, 5))}, m, eta)
    phis = phi_basis(3, 1)
    cases.update({f"phi_{k}": v for k, v in phis.items()})
    r = curvature()
    x = xi(r, eta)
    dropped = {(3, 9): GQ(Fraction(1, 2)), (9, 3): GQ(Fraction(1, 2))}
    cases["xi"] = x
    cases["xi_dropped"] = dropped
    for k in ("B", "B'"):
        cases[f"inner_pinned_{k}"] = bracket(phis[k], star(x, eta), "C", eta)
        cases[f"inner_dropped_{k}"] = bracket(phis[k], star(dropped, eta), "C", eta)
    for p1 in ("F", "F'"):
        for p2 in ("B", "B'"):
            for ms in itertools.product("CA", repeat=3):
                mode = "".join(ms)
                cases[f"shiab_{p1}_{p2}_{mode}"] = shiab(phis[p1], phis[p2], x, mode, eta)
    for a in range(3):
        for f in range(16):
            for b in range(16):
                cases[f"action_{a}_{f}_{b}"] = generator_action({(f, b): GQ(1, 2)}, a, a + 1, eta)
    return {k: canonical(v) for k, v in cases.items()}


def parse_output(text):
    cases = {}
    for line in text.splitlines():
        label, raw = line.split("|", 1)
        if label in cases:
            raise AssertionError(f"Duplicate Lean case {label}")
        values = []
        if raw:
            for term in raw.split(";"):
                f, b, re, im = term.split(",")
                values.append((int(f), int(b), Fraction(re), Fraction(im)))
        assert values == sorted(values), f"Noncanonical Lean term order: {label}"
        assert all(re or im for _, _, re, im in values), f"Zero term: {label}"
        assert len({(f, b) for f, b, _, _ in values}) == len(values), f"Duplicate term: {label}"
        cases[label] = tuple(values)
    return cases


def main():
    expected = expected_cases()
    executable = ROOT / "lean/.lake/build/bin/bridge.exe"
    if not executable.exists():
        executable = executable.with_suffix("")
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake.exe")
    # Rebuild imports too: lean --run alone can load a stale Concrete.olean.
    target = "B02.Concrete" if "--lean-run" in sys.argv else "bridge"
    subprocess.run([lake, "build", target], check=True, cwd=ROOT / "lean")
    if "--lean-run" in sys.argv:
        command = [lake, "env", "lean", "--run", "Bridge.lean"]
    elif executable.exists():
        command = [str(executable)]
    else:
        raise SystemExit("Lean bridge executable missing; run lake build in lean/ first")
    actual = parse_output(subprocess.check_output(command, text=True, cwd=ROOT / "lean"))
    assert actual.keys() == expected.keys(), (actual.keys() - expected.keys(), expected.keys() - actual.keys())
    for key in expected:
        assert actual[key] == expected[key], (key, actual[key], expected[key])
    assert not expected["inner_pinned_B"]
    assert expected["inner_dropped_B"]
    print(f"PASS: {len(expected)} exact Lean/Python cases")
    print("Dropped-index witness R_0103=R_0301=1, eta=(1,1,1,-1):")
    print(f"  pinned [B,*xi]_C = {expected['inner_pinned_B']}")
    print(f"  dropped [B,*xi]_C = {expected['inner_dropped_B']}")
    print(f"  dropped [B',*xi]_C = {expected["inner_dropped_B'"]}")


if __name__ == "__main__":
    main()



