"""Verify bridge sensitivity using disposable exact source copies.

Proof declarations are excluded so this tests the executable comparison alone.
The maintained Concrete.lean and Bridge.lean are hash-checked, never mutated.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile

from check import ROOT, expected_cases, parse_output


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    concrete_path = ROOT / "lean/B02/Concrete.lean"
    bridge_path = ROOT / "lean/Bridge.lean"
    hashes = {p: digest(p) for p in (concrete_path, bridge_path)}
    concrete = concrete_path.read_text(encoding="utf-8-sig")
    # Keep precisely the executable definitions, omitting theorem declarations.
    concrete = concrete.split("/-- The witness really has the pair symmetry", 1)[0]
    concrete += "\nend B02.Concrete\n"
    bridge = bridge_path.read_text(encoding="utf-8-sig")
    bridge = bridge.replace("import B02.Concrete", "", 1)
    expected = expected_cases()
    mutations = [
        ("reverse_star_sign", "integer (starSign eta t.form)", "integer (-starSign eta t.form)"),
        ("drop_xi_raising", "xiWithRaising eta R true", "xiWithRaising eta R false"),
        ("remove_A_imaginary", "| .A => c * imaginary", "| .A => c"),
    ]
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake.exe")
    with tempfile.TemporaryDirectory(prefix="mutation_", dir=ROOT / "lean/bridge") as directory:
        for name, before, after in mutations:
            assert concrete.count(before) == 1, (name, "ambiguous mutation")
            source = Path(directory) / f"{name}.lean"
            source.write_text(concrete.replace(before, after, 1) + bridge, encoding="utf-8")
            print(f"Running {name}", flush=True)
            output = subprocess.check_output([lake, "env", "lean", "--run", str(source)],
                                             cwd=ROOT / "lean", text=True)
            actual = parse_output(output)
            assert actual.keys() == expected.keys()
            failures = [key for key in expected if actual[key] != expected[key]]
            assert failures, f"SURVIVING MUTATION: {name}"
            key = failures[0]
            print(f"DETECTED {name}: {len(failures)} mismatches; first {key}: "
                  f"Lean={actual[key]}, Python={expected[key]}", flush=True)
    for path, before in hashes.items():
        assert digest(path) == before, f"Maintained source changed: {path}"
        print(f"UNCHANGED SHA256 {path.name}: {before}")


if __name__ == "__main__":
    main()
