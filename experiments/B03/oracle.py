"""Read the tracked LiE fixture (experiments/B03/lie/oracle.out); no LiE needed at test time."""
import re
from collections import Counter
from pathlib import Path

FIXTURE = Path(__file__).with_name("lie") / "oracle.out"
_TERM = re.compile(r"(-?\d+)X\[([-\d,\s]+)\]")


def sections(path: Path = FIXTURE) -> dict[str, list]:
    """Title -> list of items (int dimension or Counter polynomial); matrices are skipped."""
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if not lines or lines[-1] != "END B03 ORACLE":
        raise ValueError("LiE fixture is incomplete (no completion marker)")
    if any("error" in ln.lower() or "unknown" in ln.lower() for ln in lines):
        raise ValueError("LiE fixture contains an error message")
    out, title, buf, in_matrix = {}, None, "", False
    for ln in lines:
        if re.search(r"[A-WYZa-z]", ln):
            if buf:
                raise ValueError(f"unfinished polynomial before {ln!r}")
            title = ln
            out[title] = []
            continue
        if ln.startswith("[[") or (in_matrix and (ln.startswith(",[") or ln == "]")):
            in_matrix = ln != "]"
            continue
        if re.fullmatch(r"-?\d+", ln) and not buf:
            out[title].append(int(ln))
            continue
        buf += " " + ln
        if not ln.endswith("+"):
            poly = Counter()
            for m, w in _TERM.findall(buf):
                poly[tuple(int(x) for x in w.split(","))] += int(m)
            out[title].append(+poly if any(poly.values()) else Counter())
            buf = ""
    return out


def polynomial(title: str, index: int = 0) -> Counter:
    item = sections()[title][index]
    if not isinstance(item, Counter):
        raise TypeError(f"{title}[{index}] is not a polynomial")
    return item
