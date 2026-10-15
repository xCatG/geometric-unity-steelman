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
