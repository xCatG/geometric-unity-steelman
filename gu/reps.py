"""Exact weight characters for simply-laced simple Lie algebras (A_n, D_n) and products.

Weights are integer tuples of Dynkin labels. A character is a Counter {weight: multiplicity}.
Freudenthal's formula is evaluated on dominant weights only; non-dominant multiplicities are
read from the dominant conjugate. All arithmetic is exact (int / Fraction).

Exactness contract (P4): every public entry point routes numbers through exact_int, which accepts
Python and numpy integers and integral Fractions, converts them to Python int, and rejects floats,
bools and nonintegral rationals. Ordinary characters have one weight width and nonnegative integral
multiplicities; invalid input is rejected before any arithmetic.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from numbers import Integral


def exact_int(x, what: str = "value") -> int:
    if isinstance(x, bool) or not isinstance(x, (Integral, Fraction)):
        raise ValueError(f"{what} must be an exact integer, got {type(x).__name__}")
    if isinstance(x, Fraction):
        if x.denominator != 1:
            raise ValueError(f"{what} must be integral, got {x}")
        return int(x.numerator)
    return int(x)


def weight(w, width: int | None = None, what: str = "weight") -> tuple[int, ...]:
    if width is not None:
        width = exact_int(width, "width")
    w = tuple(exact_int(x, what) for x in w)
    if width is not None and len(w) != width:
        raise ValueError(f"{what} has width {len(w)}, expected {width}")
    return w


def character(ch, width: int | None = None) -> Counter:
    """Validate an ordinary character; returns a Counter of int tuples -> positive ints."""
    if width is not None:
        width = exact_int(width, "width")
    out, widths = Counter(), set()
    for w, m in dict(ch).items():
        w = weight(w, width)
        widths.add(len(w))
        m = exact_int(m, "multiplicity")
        if m < 0:
            raise ValueError(f"negative multiplicity {m} at {w}")
        if m:
            out[w] += m
    if len(widths) > 1:
        raise ValueError(f"mixed weight widths {sorted(widths)}")
    return out


def cartan(family: str, rank: int) -> tuple[tuple[int, ...], ...]:
    rank = exact_int(rank, "rank")
    if family == "A" and rank >= 1:
        return tuple(tuple(2 if i == j else -1 if abs(i - j) == 1 else 0 for j in range(rank))
                     for i in range(rank))
    if family == "D" and rank >= 3:
        a = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
        for i in range(rank - 2):
            a[i][i + 1] = a[i + 1][i] = -1
        a[rank - 3][rank - 1] = a[rank - 1][rank - 3] = -1
        return tuple(map(tuple, a))
    raise ValueError(f"unsupported type {family}{rank}")


def _inverse(m):
    n = len(m)
    a = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(m)]
    for c in range(n):
        p = next(r for r in range(c, n) if a[r][c] != 0)
        a[c], a[p] = a[p], a[c]
        a[c] = [x / a[c][c] for x in a[c]]
        for r in range(n):
            if r != c and a[r][c] != 0:
                a[r] = [x - a[r][c] * y for x, y in zip(a[r], a[c])]
    return tuple(tuple(row[n:]) for row in a)


class Simple:
    """A simply-laced simple Lie algebra; (alpha_i, alpha_i) = 2."""

    def __init__(self, family: str, rank: int):
        rank = exact_int(rank, "rank")
        self.name = f"{family}{rank}"
        self.A = cartan(family, rank)
        self.rank = rank
        self.Ainv = _inverse(self.A)
        self.simple = [tuple(row) for row in self.A]  # alpha_i in Dynkin labels
        self.positive = self._positive_roots()
        self.rho = tuple([1] * rank)

    def _positive_roots(self):
        # roots in simple-root coordinates, closed under simple reflections
        n = self.rank
        roots = {tuple(int(i == j) for j in range(n)) for i in range(n)}
        frontier = list(roots)
        while frontier:
            new = []
            for r in frontier:
                d = self.to_dynkin_root(r)
                for i in range(n):
                    s = list(r)
                    s[i] -= d[i]
                    s = tuple(s)
                    if all(x >= 0 for x in s) and any(s) and s not in roots:
                        roots.add(s)
                        new.append(s)
            frontier = new
        return [self.to_dynkin_root(r) for r in sorted(roots)]

    def to_dynkin_root(self, coeffs):
        coeffs = weight(coeffs, self.rank, "root coefficients")
        return tuple(sum(c * self.A[i][j] for i, c in enumerate(coeffs)) for j in range(self.rank))

    def ip(self, x, y) -> Fraction:
        x, y = weight(x, self.rank), weight(y, self.rank)
        return sum(x[i] * self.Ainv[i][j] * y[j] for i in range(self.rank) for j in range(self.rank))

    def dominant(self, w):
        w = list(weight(w, self.rank))
        while True:
            i = next((i for i, x in enumerate(w) if x < 0), None)
            if i is None:
                return tuple(w)
            c = w[i]
            w = [x - c * self.A[i][j] for j, x in enumerate(w)]

    def orbit(self, w):
        w = weight(w, self.rank)
        seen, frontier = {tuple(w)}, [tuple(w)]
        while frontier:
            nxt = []
            for v in frontier:
                for i in range(self.rank):
                    if v[i] != 0:
                        u = tuple(x - v[i] * self.A[i][j] for j, x in enumerate(v))
                        if u not in seen:
                            seen.add(u)
                            nxt.append(u)
            frontier = nxt
        return seen

    def dimension(self, hw) -> int:
        hw = self._check(hw)
        num = den = Fraction(1)
        lr = tuple(a + b for a, b in zip(hw, self.rho))
        for a in self.positive:
            num *= self.ip(lr, a)
            den *= self.ip(self.rho, a)
        q = num / den
        assert q.denominator == 1
        return int(q.numerator)

    def _check(self, hw):
        hw = weight(hw, self.rank, f"highest weight for {self.name}")
        if any(x < 0 for x in hw):
            raise ValueError(f"bad highest weight {hw} for {self.name}")
        return hw

    def character(self, hw) -> Counter:
        hw = self._check(hw)
        return Counter(_character(self, hw))


@lru_cache(maxsize=None)
def _dominant_mults(g: Simple, hw):
    lr = tuple(a + b for a, b in zip(hw, g.rho))
    norm = g.ip(lr, lr)
    # dominant weights below hw, by depth (sum of simple-root coefficients)
    dom = {hw}
    frontier = [hw]
    while frontier:
        nxt = []
        for mu in frontier:
            for a in g.positive:
                nu = g.dominant(tuple(m - x for m, x in zip(mu, a)))
                if nu not in dom and _below(g, nu, hw):
                    dom.add(nu)
                    nxt.append(nu)
        frontier = nxt
    depth = {mu: sum(_root_coeffs(g, tuple(h - m for h, m in zip(hw, mu)))) for mu in dom}
    mult = {}
    for mu in sorted(dom, key=lambda m: depth[m]):
        if mu == hw:
            mult[mu] = 1
            continue
        s = Fraction(0)
        for a in g.positive:
            k = 1
            while True:
                nu = tuple(m + k * x for m, x in zip(mu, a))
                m_nu = mult.get(g.dominant(nu), 0) if _below(g, g.dominant(nu), hw) else 0
                if m_nu == 0 and not _below(g, g.dominant(nu), hw):
                    break
                s += m_nu * g.ip(nu, a)
                k += 1
        mr = tuple(a + b for a, b in zip(mu, g.rho))
        q = 2 * s / (norm - g.ip(mr, mr))
        assert q.denominator == 1 and q >= 0, (g.name, hw, mu, q)
        mult[mu] = int(q.numerator)
    return {m: c for m, c in mult.items() if c}


def _root_coeffs(g, w):
    c = [sum(Fraction(w[j]) * g.Ainv[j][i] for j in range(g.rank)) for i in range(g.rank)]
    return c


def _below(g, mu, hw) -> bool:
    c = _root_coeffs(g, tuple(h - m for h, m in zip(hw, mu)))
    return all(x.denominator == 1 and x >= 0 for x in c)


def _character(g, hw):
    out = {}
    for mu, m in _dominant_mults(g, hw).items():
        for w in g.orbit(mu):
            out[w] = m
    return out


class Product:
    """Product of simple factors and u1 U(1) charges; weights are concatenated tuples."""

    def __init__(self, factors: list[Simple], u1: int = 0):
        u1 = exact_int(u1, "number of U(1) factors")
        self.factors, self.u1 = factors, u1
        self.slices = []
        o = 0
        for f in factors:
            self.slices.append(slice(o, o + f.rank))
            o += f.rank
        self.width = o + u1

    def split(self, w):
        w = weight(w, self.width)
        return [tuple(w[s]) for s in self.slices], tuple(w[self.width - self.u1:])

    def character(self, hws, charges=()):
        if len(hws) != len(self.factors) or len(charges) != self.u1:
            raise ValueError("wrong number of factor highest weights or charges")
        charges = weight(charges, self.u1, "charge")
        ch = Counter({(): 1})
        for f, hw in zip(self.factors, hws):
            c = f.character(hw)
            ch = Counter({a + b: m * n for a, m in ch.items() for b, n in c.items()})
        return Counter({w + tuple(charges): m for w, m in ch.items()})

    def decompose(self, ch: Counter) -> Counter:
        ch = character(ch, self.width)
        out = Counter()
        while ch:
            # highest weight: maximise height in each factor (rho-pairing), then charge
            def key(w):
                parts, q = self.split(w)
                return (sum(f.ip(p, f.rho) for f, p in zip(self.factors, parts)), q)
            top = max(ch, key=key)
            parts, q = self.split(top)
            if any(x < 0 for p in parts for x in p):
                raise ValueError(f"not a character: top weight {top} not dominant")
            m = ch[top]
            out[(tuple(parts), q)] += m
            irr = self.character(parts, q)
            for w, k in irr.items():
                ch[w] -= m * k
            if any(v < 0 for v in ch.values()):
                raise ValueError("negative remainder: not a character of this group")
            ch = +ch
        return out


def tensor(a: Counter, b: Counter) -> Counter:
    a = character(a)
    b = character(b, len(next(iter(a))) if a else None)
    out = Counter()
    for x, m in a.items():
        for y, n in b.items():
            out[tuple(i + j for i, j in zip(x, y))] += m * n
    return out


def restrict(ch: Counter, matrix) -> Counter:
    """Apply an integer restriction matrix (rows = source labels, cols = target coords)."""
    matrix = [weight(row, None, "matrix entry") for row in matrix]
    if len({len(row) for row in matrix}) != 1:
        raise ValueError("ragged restriction matrix")
    ch = character(ch, len(matrix))
    out = Counter()
    for w, m in ch.items():
        out[tuple(sum(w[i] * matrix[i][j] for i in range(len(w))) for j in range(len(matrix[0])))] += m
    return out


# ---- coordinates: doubled orthonormal weights (entries of 2x) <-> Dynkin labels

def _half(v: int) -> int:
    if v % 2:
        raise ValueError("not an integral weight")
    return v // 2


def dn_dynkin(y) -> tuple[int, ...]:
    """D_n Dynkin labels of a doubled orthonormal weight y (Bourbaki: a_n = e_{n-1} + e_n)."""
    y = weight(y)
    n = len(y)
    return tuple(_half(y[i] - y[i + 1]) for i in range(n - 1)) + (_half(y[n - 2] + y[n - 1]),)


def dn_doubled(labels) -> tuple[int, ...]:
    """Inverse of dn_dynkin."""
    labels = weight(labels)
    n = len(labels)
    y = [0] * n
    y[n - 1] = labels[n - 1] - labels[n - 2]          # y_{n-1}+y_n = 2 l_n, y_{n-1}-y_n = 2 l_{n-1}
    y[n - 2] = labels[n - 1] + labels[n - 2]
    for i in range(n - 3, -1, -1):
        y[i] = y[i + 1] + 2 * labels[i]
    return tuple(y)


def d2_as_a1a1(y2) -> tuple[int, int]:
    """Horizontal doubled weight (y1, y2) -> (A1_L, A1_R) Dynkin labels; L = even half-spin."""
    y2 = weight(y2, 2)
    return _half(y2[0] + y2[1]), _half(y2[0] - y2[1])


def split_14(y) -> tuple[int, ...]:
    """D7 doubled weight, horizontal coordinates first -> (D5 labels..., A1_L, A1_R)."""
    y = weight(y, 7)
    return dn_dynkin(tuple(y[2:])) + d2_as_a1a1(tuple(y[:2]))


def d7_to_d5a1a1(ch: Counter) -> Counter:
    ch = character(ch, 7)
    out = Counter()
    for w, m in ch.items():
        out[split_14(dn_doubled(w))] += m
    return out


def sm_weight(y5) -> tuple[int, int, int, int]:
    """Embedding E (ansatz rev 1): D5 doubled weight -> (SU3 Dynkin a, b; SU2 Dynkin k; n = 6Y)."""
    y1, y2, y3, y4, y5_ = weight(y5, 5)
    n2 = 2 * y1 + 2 * y2 + 2 * y3 - 3 * y4 - 3 * y5_
    return _half(y2 - y1), _half(y3 - y2), _half(y5_ - y4), _half(n2)


def sm_weight_flipped(y5) -> tuple[int, int, int, int]:
    """Control E' (ansatz rev 1): n' = (-n5 + 6X)/5, X = sum y."""
    y5 = weight(y5, 5)
    a, b, k, n5 = sm_weight(y5)
    num = -n5 + 6 * sum(y5)
    if num % 5:
        raise ValueError("non-integral flipped charge")
    return a, b, k, num // 5
