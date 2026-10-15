"""Additional signature samples: actual Python against the Lean Samples model."""
from pathlib import Path
import shutil
import subprocess

import numpy as np
from check import ROOT, canonical, parse_output
from gu.cliffform import star
from gu.shiab import eta_of, phi_basis, shiab, xi


def main():
    expected = {}
    for p, q in ((2, 2), (4, 0), (3, 1), (1, 1)):
        n = p + q
        eta = eta_of(p, q)
        r = np.zeros((n, n, n, n), dtype=object)
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        r[a, b, c, d] = eta[a] * eta[b] * (
                            int(a == c and b == d) - int(a == d and b == c))
        phi = phi_basis(p, q)
        for mode in ("CCC", "CAA"):
            expected[f"{p}{q}_{mode}"] = canonical(
                star(shiab(phi["F"], phi["B"], xi(r, eta), mode, eta), eta))
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake.exe")
    subprocess.run([lake, "build", "B02.Samples"], cwd=ROOT / "lean", check=True)
    actual = parse_output(subprocess.check_output(
        [lake, "env", "lean", "--run", "bridge/SampleBridge.lean"],
        cwd=ROOT / "lean", text=True))
    assert actual.keys() == expected.keys()
    for label in expected:
        assert actual[label] == expected[label], (label, actual[label], expected[label])
        print(f"PASS {label}: {actual[label]}")
    print("PASS: 8 additional exact signature sample cases")


if __name__ == "__main__":
    main()

