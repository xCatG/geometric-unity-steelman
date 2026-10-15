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


def _reject_floats(*values) -> None:
    for value in values:
        if sp.sympify(value).has(sp.Float):
            raise ValueError("B01 requires exact inputs; use Rational instead of float")


def dewitt(h: sp.Matrix, k: sp.Matrix, lam) -> sp.Expr:
    _reject_floats(h, k, lam)
    return (ETA * h * ETA * k).trace() - lam * (ETA * h).trace() * (ETA * k).trace()


def vertical_gram(lam) -> sp.Matrix:
    _reject_floats(lam)
    b = _sym_basis()
    return sp.Matrix(10, 10, lambda i, j: dewitt(b[i], b[j], lam))


def chimeric_gram(lam, h_sign: int, v_sign: int) -> sp.Matrix:
    _reject_floats(lam, h_sign, v_sign)
    if h_sign not in (-1, 1) or v_sign not in (-1, 1):
        raise ValueError("chimeric signs must be exact +1 or -1")
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
