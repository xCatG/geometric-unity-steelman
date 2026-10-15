"""Verify Ricci, scalar, embedding, and the nonunique n=2 descriptions."""
from pathlib import Path
import shutil
import subprocess

import numpy as np
from check import ROOT, canonical, parse_output
from gu.cliffform import GQ, scale, star
from gu.curvature import is_algebraic_curvature, ricci, scalar
from gu.shiab import embed_tensor, eta_of, phi_basis, shiab, xi


def main():
    eta = eta_of(1, 1)
    r = np.zeros((2, 2, 2, 2), dtype=object)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    r[a, b, c, d] = eta[a] * eta[b] * (
                        int(a == c and b == d) - int(a == d and b == c))
    assert is_algebraic_curvature(r)
    ric = ricci(r, np.array(eta))
    s = scalar(r, np.array(eta))
    g = np.diag(eta)
    assert np.array_equal(ric, g)
    assert s == 2
    phi = phi_basis(1, 1)
    out = star(shiab(phi["F"], phi["B"], xi(r, eta), "CCC", eta), eta)
    expected = {
        "Ricci": {(1 << a, 1 << b): GQ(ric[a, b]) for a in range(2) for b in range(2)},
        "scalar": {(0, 0): GQ(s)},
        "embed_metric": embed_tensor(g, 1, 0, 1, 1),
        "response": out,
        "kappa_zero": scale(embed_tensor(ric, 1, 0, 1, 1), -1),
        "kappa_one": embed_tensor(ric - s * g, 1, 0, 1, 1),
    }
    expected = {key: canonical(value) for key, value in expected.items()}
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake.exe")
    subprocess.run([lake, "build", "B02.DimensionTwo"], cwd=ROOT / "lean", check=True)
    actual = parse_output(subprocess.check_output(
        [lake, "env", "lean", "--run", "bridge/DimensionTwoBridge.lean"],
        cwd=ROOT / "lean", text=True))
    assert actual.keys() == expected.keys()
    for key in expected:
        assert actual[key] == expected[key], (key, actual[key], expected[key])
    assert expected["response"] == expected["kappa_zero"] == expected["kappa_one"]
    assert expected["response"]
    print("PASS: 6 exact dimension-two contraction/embedding/response cases")
    print("Ric=g, S=2; nonzero response -F has (c,kappa)=(-1,0) and (1,1)")


if __name__ == "__main__":
    main()
