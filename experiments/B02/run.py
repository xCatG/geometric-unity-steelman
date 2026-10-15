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
