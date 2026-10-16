"""Independent B07 Phase 2 re-derivation, reading V, exact arithmetic.

Only gu.clifford's explicit gamma/Mono matrices are shared with production.
The exterior/matrix arithmetic below is carried forward from the independent
Phase 1 re-derivation, not imported from B07. The equivariance equations,
sparse rational elimination, gates, curvature fit and Fourier matrices are
assembled independently here. No production result is read by this program.
Run: uv run python -m experiments.B07.phase2.rederive
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
import json
from numbers import Integral

from gu.clifford import Mono, gammas

COLUMNS = ("F", "F+B", "F+B'", "F'", "F'+B", "F'+B'")
MODES = tuple("".join(m) for m in product("CA", repeat=3))
ZERO = (0, 0)

def exact(value):
    if isinstance(value, Fraction):
        return Fraction(int(value.numerator), int(value.denominator))
    if isinstance(value, Integral):
        return Fraction(int(value))
    raise ValueError("coefficients must be exact integers or Fractions")


def add(*forms):
    out = {}
    for form in forms:
        for key, value in form.items():
            total = out.get(key, 0) + value
            if total:
                out[key] = total
            else:
                out.pop(key, None)
    return out


def scale(form, value):
    value = exact(value)
    return {key: value * c for key, c in form.items() if value * c}


def zadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def zscale(a, c):
    return a[0] * c, a[1] * c


@lru_cache(None)
def exterior(left, right):
    """Sorted tuple union and permutation parity; repeated indices kill a wedge."""
    if set(left).intersection(right):
        return (), 0
    inversions = sum(a > b for a in left for b in right)
    return tuple(sorted(left + right)), (-1) ** inversions


class Algebra:
    def __init__(self, p, q):
        self.n = p + q
        self.metric = (1,) * p + (-1,) * q
        self.volume = tuple(range(self.n))
        self.dim = 2 ** (self.n // 2)
        self.matrices = []
        self.ids = {}
        self.identity = self.intern(Mono.identity(self.dim))
        self.gamma = [self.intern(g) for g in gammas(p, q)]
        volume = self.blade(self.volume)
        raw_volume = self.materialize(volume)
        identity = Mono.identity(self.dim)
        for phase in range(4):
            candidate = raw_volume.times_i_power(phase)
            if candidate @ candidate == identity and candidate.dagger() == candidate:
                self.chirality_phase = phase
                self.chiral = self.intern(candidate)
                break
        else:
            raise AssertionError("no chirality phase")
        self.phi = {name: {} for name in ("F", "F'", "B", "B'")}
        for a in range(self.n):
            self.phi["F"].update(self.term((a,), self.gamma[a]))
            self.phi["F'"].update(self.term((a,), self.multiply(self.gamma[a], self.chiral)))
        for a, b in combinations(range(self.n), 2):
            matrix = self.multiply(self.gamma[a], self.gamma[b])
            self.phi["B"].update(self.term((a, b), matrix))
            dual = self.multiply(matrix, self.chiral)
            self.phi["B'"].update(self.term((a, b), self.imaginary(dual)))

    def intern(self, matrix):
        # Strip only the real sign; iM remains a separate exact matrix.
        sign = -1 if matrix.phase[0] >= 2 else 1
        if sign < 0:
            matrix = -matrix
        key = matrix.perm.tobytes(), matrix.phase.tobytes()
        if key not in self.ids:
            self.ids[key] = len(self.matrices)
            self.matrices.append(matrix)
        return self.ids[key], sign

    def materialize(self, matrix):
        index, sign = matrix
        return self.matrices[index] if sign == 1 else -self.matrices[index]

    @lru_cache(None)
    def matrix_product(self, left, right):
        return self.intern(self.matrices[left] @ self.matrices[right])

    def multiply(self, left, right):
        index, sign = self.matrix_product(left[0], right[0])
        return index, sign * left[1] * right[1]

    @lru_cache(None)
    def matrix_i(self, index):
        return self.intern(self.matrices[index].times_i_power(1))

    def imaginary(self, matrix):
        index, sign = self.matrix_i(matrix[0])
        return index, sign * matrix[1]

    @lru_cache(None)
    def blade(self, indices):
        out = self.identity
        for index in indices:
            out = self.multiply(out, self.gamma[index])
        return out

    @staticmethod
    def term(indices, matrix):
        return {(indices, matrix[0]): matrix[1]}

    def wedge(self, left, right, bracket=None):
        if bracket not in (None, "C", "A"):
            raise ValueError("unknown bracket")
        out = {}
        for (lf, lm), lc in left.items():
            for (rf, rm), rc in right.items():
                form, parity = exterior(lf, rf)
                if not parity:
                    continue
                terms = [self.matrix_product(lm, rm)]
                if bracket:
                    index, sign = self.matrix_product(rm, lm)
                    terms.append((index, sign * (-1 if bracket == "C" else 1)))
                for matrix in terms:
                    if bracket == "A":
                        matrix = self.imaginary(matrix)
                    key = form, matrix[0]
                    out[key] = out.get(key, 0) + parity * lc * rc * matrix[1]
        return {key: value for key, value in out.items() if value}

    @lru_cache(None)
    def star_basis(self, indices):
        complement = tuple(i for i in self.volume if i not in indices)
        _, sign = exterior(indices, complement)
        for i in indices:
            sign *= self.metric[i]
        return complement, sign

    def star(self, form):
        out = {}
        for (indices, matrix), value in form.items():
            complement, sign = self.star_basis(indices)
            out[complement, matrix] = sign * value
        return out

    @lru_cache(None)
    def product_trace(self, left, right):
        # Deliberately trace a matrix product, not its Clifford scalar coefficient.
        return (self.matrices[left] @ self.matrices[right]).trace()

    def pair(self, left, right):
        out = ZERO
        for (lf, lm), lc in left.items():
            for (rf, rm), rc in right.items():
                form, sign = exterior(lf, rf)
                if sign and form == self.volume:
                    out = zadd(out, zscale(self.product_trace(lm, rm), sign * lc * rc))
        return out

    @lru_cache(None)
    def column_basis(self, mode, column, indices, matrix):
        xstar = self.star({(indices, matrix): 1})
        names = column.split("+")
        if len(names) == 1:
            return self.wedge(self.phi[names[0]], xstar, mode[0])
        inner = self.wedge(self.phi[names[1]], xstar, mode[1])
        outer = self.wedge(self.phi[names[0]], self.star(inner), mode[2])
        return self.star(outer)

    def column(self, mode, column, x):
        if mode not in MODES or column not in COLUMNS:
            raise ValueError("unknown mode or column")
        return add(*(scale(self.column_basis(mode, column, f, m), c)
                     for (f, m), c in x.items()))

    def operator(self, mode, phi1, phi2, x):
        """Direct (9.3), independently of the six-column assembly."""
        sx = self.star(x)
        first = self.wedge(phi1, sx, mode[0])
        inner = self.wedge(phi2, sx, mode[1])
        second = self.star(self.wedge(phi1, self.star(inner), mode[2]))
        return add(first, scale(second, Fraction(-1, 2)))

    def one_basis(self):
        blades = [self.blade(tuple(i for i in self.volume if mask & (1 << i)))
                  for mask in range(1 << self.n)]
        return [self.term((i,), matrix) for i in self.volume for matrix in blades]


class Echelon:
    """Streaming exact rational row elimination, implemented here, without a CAS."""
    def __init__(self, width):
        self.width = width
        self.rows = {}

    def insert(self, row):
        row = {k: exact(v) for k, v in row.items() if v}
        while row:
            pivot = min(row)
            value = row[pivot]
            if pivot not in self.rows:
                self.rows[pivot] = {k: v / value for k, v in row.items()}
                return True
            for k, v in self.rows[pivot].items():
                total = row.get(k, 0) - value * v
                if total:
                    row[k] = total
                else:
                    row.pop(k, None)
        return False

    def kernel(self):
        result = []
        for free in range(self.width):
            if free in self.rows:
                continue
            vector = {free: Fraction(1)}
            for pivot in sorted(self.rows, reverse=True):
                value = -sum(v * vector.get(k, 0)
                             for k, v in self.rows[pivot].items() if k != pivot)
                if value:
                    vector[pivot] = value
            result.append(vector)
        return result


def column_kernel(columns):
    rows = {}
    for i, column in enumerate(columns):
        for k, value in column.items():
            if value:
                rows.setdefault(k, {})[i] = value
    solver = Echelon(len(columns))
    for row in rows.values():
        solver.insert(row)
    return solver.kernel()


def sum_maps(maps, coefficients):
    return add(*(scale(maps[i], c) for i, c in coefficients.items()))


def apply_map(matrix, form):
    output = {}
    for (o, i), value in matrix.items():
        if i in form:
            output[o] = output.get(o, 0) + value * form[i]
    return {k: v for k, v in output.items() if v}


def compose(left, right):
    by_middle = {}
    for (o, i), v in left.items():
        by_middle.setdefault(i, []).append((o, v))
    out = {}
    for (middle, i), v in right.items():
        for o, w in by_middle.get(middle, []):
            key = o, i
            out[key] = out.get(key, 0) + v * w
    return {k: v for k, v in out.items() if v}


class Independent:
    def __init__(self):
        self.a = Algebra(3, 1)
        a = self.a
        # Construct the Dirac pairing directly from the timelike gamma.
        raw = a.materialize(a.gamma[3])
        pairing = next(raw.times_i_power(k) for k in range(4)
                       if raw.times_i_power(k).dagger() == raw.times_i_power(k))
        self.phase = {}
        self.grade = {}
        self.coordinate = {}
        for grade in range(5):
            for indices in combinations(range(4), grade):
                blade = a.blade(indices)
                matrix = a.materialize(blade)
                valid = []
                for phase in (0, 1):
                    u = matrix.times_i_power(phase)
                    if u.dagger() @ pairing == -(pairing @ u):
                        valid.append(phase)
                assert len(valid) == 1, "unique real-form phase"
                u = a.intern(matrix.times_i_power(valid[0]))
                self.phase[indices] = u
                self.grade[u[0]] = grade
                # Rational coefficient on this canonical matrix id.
                self.coordinate[u[0]] = u[1]
        self.bases = {d: [(f, u[0]) for f in combinations(range(4), d)
                          for u in self.phase.values()] for d in range(5)}

    def basis(self, degree, grade):
        return [k for k in self.bases[degree] if self.grade[k[1]] == grade]

    def canonical(self, form):
        """Require real coefficients on the selected u(A) matrix ids."""
        assert all(m in self.coordinate for f, m in form), "left real form"
        return form

    def generator(self, key, aidx, bidx):
        a = self.a
        f, m = key
        j = a.term((), a.blade((aidx, bidx)))
        out = scale(a.wedge(j, {key: 1}, "C"), Fraction(1, 2))
        for position, index in enumerate(f):
            if index == aidx:
                replacement, coefficient = bidx, -a.metric[bidx]
            elif index == bidx:
                replacement, coefficient = aidx, a.metric[aidx]
            else:
                continue
            new = f[:position] + (replacement,) + f[position + 1:]
            if len(set(new)) != len(new):
                continue
            inversions = sum(new[i] > new[j] for i in range(len(new)) for j in range(i + 1, len(new)))
            out = add(out, {(tuple(sorted(new)), m): coefficient * (-1) ** inversions})
        return self.canonical(out)

    def equivariant(self):
        maps, dimensions = [], {}
        for ingrade in range(5):
            bi = self.basis(2, ingrade)
            for outgrade in range(5):
                bo = self.basis(3, outgrade)
                ii, oi = {k: i for i, k in enumerate(bi)}, {k: i for i, k in enumerate(bo)}
                width = len(bi) * len(bo)
                solver = Echelon(width)
                for aidx, bidx in combinations(range(4), 2):
                    ri = [self.generator(k, aidx, bidx) for k in bi]
                    ro = [self.generator(k, aidx, bidx) for k in bo]
                    outrows = [{} for _ in bo]
                    for col, image in enumerate(ro):
                        for k, v in image.items():
                            outrows[oi[k]][col] = v
                    for r in range(len(bo)):
                        for s in range(len(bi)):
                            row = {t * len(bi) + s: v for t, v in outrows[r].items()}
                            for k, v in ri[s].items():
                                key = r * len(bi) + ii[k]
                                row[key] = row.get(key, 0) - v
                            solver.insert(row)
                vectors = solver.kernel()
                if vectors:
                    dimensions[f"{ingrade},{outgrade}"] = len(vectors)
                for vector in vectors:
                    maps.append({(bo[k // len(bi)], bi[k % len(bi)]): v for k, v in vector.items()})
        return maps, dimensions

    def blocks(self):
        a = self.a
        specs = [(mode + "CC", name) for mode in "CA" for name in ("F", "F'")]
        specs += [("C" + inner + outer, first + "+" + second)
                  for inner in "CA" for outer in "CA" for first in ("F", "F'") for second in ("B", "B'")]
        result = []
        for mode, column in specs:
            matrix = {}
            for key in self.bases[2]:
                for o, v in self.canonical(a.column(mode, column, {key: 1})).items():
                    matrix[o, key] = v
            result.append(matrix)
        return specs, result

    def pair_column(self, image):
        """All pairings with basis one-forms; actual normalized matrix trace."""
        a = self.a
        out = {}
        for index, key in enumerate(self.bases[1]):
            re, im = a.pair({key: 1}, image)
            if re:
                out[index, 0] = Fraction(re, a.dim)
            if im:
                out[index, 1] = Fraction(im, a.dim)
        return out

    def c1(self, matrix):
        a = self.a
        output = {}
        for k in range(4):
            ek = a.term((k,), a.identity)
            pairings = [self.pair_column(apply_map(matrix, a.wedge(ek, {key: 1})))
                        for key in self.bases[1]]
            for i, j in combinations_with_replacement(range(64), 2):
                for channel in (0, 1):
                    v = pairings[j].get((i, channel), 0) + pairings[i].get((j, channel), 0)
                    if v:
                        output[k, i, j, channel] = v
        return output

    def c2(self, matrix):
        a = self.a
        paired = {}
        for i, j in combinations_with_replacement(range(64), 2):
            t, s = {self.bases[1][i]: 1}, {self.bases[1][j]: 1}
            form = add(a.wedge(t, s), a.wedge(s, t))
            paired[i, j] = self.pair_column(apply_map(matrix, form))

        def d(alpha, i, j, channel):
            return paired[min(i, j), max(i, j)].get((alpha, channel), 0)

        result = {norm: {} for norm in ("N0", "N1", "N2")}
        for alpha in range(64):
            for i, j in combinations_with_replacement(range(64), 2):
                divisor = 2 if i == j else 1
                for channel in (0, 1):
                    direct = d(alpha, i, j, channel)
                    cross = d(i, alpha, j, channel) + d(j, alpha, i, channel)
                    # b = h (uv+vu), h = 0, 1/2, 1 for N0,N1,N2.
                    for norm, h in (("N0", Fraction(0)), ("N1", Fraction(1, 2)), ("N2", Fraction(1))):
                        v = ((2 * h / 3 - 1) * direct + 2 * h / 3 * cross) / divisor
                        if v:
                            result[norm][alpha, i, j, channel] = v
        return result

    def response(self, matrix):
        """Fit and verify all KN products using an independently built tensor basis."""
        a = self.a
        symmetric = []
        for i, j in combinations_with_replacement(range(4), 2):
            symmetric.append({(i, j): 1, (j, i): 1})
        solver = Echelon(5)
        for s, t in combinations_with_replacement(symmetric, 2):
            def curvature(i, j, k, l):
                return (s.get((i, k), 0) * t.get((j, l), 0) + s.get((j, l), 0) * t.get((i, k), 0)
                        - s.get((i, l), 0) * t.get((j, k), 0) - s.get((j, k), 0) * t.get((i, l), 0))
            ricci = {(j, l): sum(a.metric[i] * curvature(i, j, i, l) for i in range(4))
                     for j in range(4) for l in range(4)}
            scalar = sum(a.metric[j] * ricci[j, j] for j in range(4))
            xi = add(*(scale(a.term((i, j), a.blade((k, l))),
                            Fraction(curvature(i, j, k, l) * a.metric[k] * a.metric[l], 2))
                       for i, j in combinations(range(4), 2) for k, l in combinations(range(4), 2)))
            actual = a.star(apply_map(matrix, xi))
            targets = []
            for tensor in (ricci, {(i, j): scalar * a.metric[i] if i == j else 0
                                   for i in range(4) for j in range(4)}):
                for dual in (False, True):
                    target = {}
                    for (i, j), value in tensor.items():
                        gamma = a.multiply(a.gamma[j], a.chiral) if dual else a.gamma[j]
                        target = add(target, scale(a.term((i,), gamma), value * a.metric[j]))
                    targets.append(target)
            for key in set(actual).union(*(set(t) for t in targets)):
                solver.insert({**{i: target.get(key, 0) for i, target in enumerate(targets)}, 4: -actual.get(key, 0)})
        kernel = solver.kernel()
        assert len(kernel) == 1 and kernel[0].get(4), "response lies in four-dimensional curvature span"
        return [kernel[0].get(i, 0) / kernel[0][4] for i in range(4)]


def einstein_dimension(responses):
    conditions = [{0: r[0] + 2 * r[2], 1: r[1] + 2 * r[3]} for r in responses]
    admissible = column_kernel(conditions)
    image = [{i: sum(responses[j][i] * c for j, c in vector.items()) for i in (0, 1)}
             for vector in admissible]
    return len(image) - len(column_kernel(image))


def star_form(form, eta, prime=False):
    """Scalar exterior star, independent also of the matrix form representation."""
    out = {}
    n = len(eta)
    for indices, value in form.items():
        complement = tuple(i for i in range(n) if i not in indices)
        coefficient = exterior(indices, complement)[1]
        for i in indices:
            coefficient *= eta[i]
        if prime:
            coefficient *= (-1) ** len(indices)
        out[complement] = coefficient * value
    return out


def scalar_pair(left, right, eta, prime=False):
    total = 0
    for f, v in left.items():
        for g, w in star_form(right, eta, prime).items():
            indices, parity = exterior(f, g)
            if len(indices) == len(eta):
                total += parity * v * w
    return total


def sign_table():
    output = []
    for n in (4, 14):
        for p in range(n + 1):
            eta = (1,) * p + (-1,) * (n - p)
            for prime in (False, True):
                adjoints, masses = set(), set()
                for i in range(n):
                    one = {(i,): 1}
                    so = star_form(one, eta, prime)
                    masses.add(scalar_pair(so, so, eta, prime) * scalar_pair(one, one, eta, prime))
                    for missing in range(n):
                        other = {tuple(j for j in range(n) if j != missing): 1}
                        left = scalar_pair(so, other, eta, prime)
                        right = scalar_pair(one, star_form(other, eta, prime), eta, prime)
                        if left or right:
                            assert left in (-1, 1) and right in (-1, 1)
                            adjoints.add(left * right)
                assert len(adjoints) == len(masses) == 1
                output.append({"signature": [p, n - p], "conv": "prime" if prime else "pinned",
                               "star_dag_sign_1form": adjoints.pop(), "mass_sign": masses.pop()})
    return output


def transpose(matrix):
    return {(i, o): v for (o, i), v in matrix.items()}


def metric_adjoint(matrix, input_gram, output_gram):
    return {(i, o): v * output_gram[o] / input_gram[i] for (o, i), v in matrix.items()}


def fourier_and_ym(independent, operators):
    """Rational matrices after factoring out the known power of i per term.

    D is K wedge; d=iD, delta=iQ. Thus a kinetic symbol is -Q X*X D.
    Action coefficients are obtained by transposing the two Fourier legs,
    independently of the Hodge formula for Q and of metric-adjoint formulas.
    """
    a = independent.a
    vectors = [(i,) for i in range(4)] + list(combinations(range(4), 2))
    output = {"fourier": [], "ym_symbol": []}
    for prime in (False, True):
        def star(x):
            return add(*(scale(a.star({key: value}), (-1) ** len(key[0]) if prime else 1)
                         for key, value in x.items()))

        grams = {}
        stars = {}
        for degree in (1, 2, 3):
            grams[degree] = {}
            stars[degree] = {}
            for key in independent.bases[degree]:
                sx = star({key: 1})
                re, im = a.pair({key: 1}, sx)
                assert not im and re in (-a.dim, a.dim)
                grams[degree][key] = Fraction(re, a.dim)
                for o, v in sx.items():
                    stars[degree][o, key] = v
        h1 = {(k, k): v for k, v in grams[1].items()}
        h3 = {(k, k): v for k, v in grams[3].items()}
        sinv = {(i, o): Fraction(1, v) for (o, i), v in stars[1].items()}
        sd = metric_adjoint(stars[1], grams[1], grams[3])
        for name, x in operators.items():
            xd = metric_adjoint(x, grams[2], grams[3])
            checks = {"kappa0: action == printed_1": True,
                      "kappa1: action == printed_2 + printed_3": True,
                      "kappa1: action == printed_2 + derived_3": True,
                      "kappa2: action == printed_4": True,
                      "kappa2: action == derived_4": True,
                      "derived_3 == -printed_3": True,
                      "derived_4 == -printed_4": True}
            nonvacuous = {"printed_" + str(i): False for i in range(1, 5)}
            ratios, mismatches = set(), 0
            for vector in vectors:
                kform = add(*(a.term((i,), a.identity) for i in vector))
                derivatives = {}
                for degree in (1, 2):
                    derivatives[degree] = {(o, key): v for key in independent.bases[degree]
                                           for o, v in a.wedge(kform, {key: 1}).items()}
                d = derivatives[1]
                q = compose(sinv, compose(derivatives[2], stars[2]))
                xdmat = compose(x, d)
                kinetic = scale(compose(q, compose(xd, xdmat)), -1)
                ym = scale(compose(q, d), -1)
                for key in set(kinetic) | set(ym):
                    u, v = kinetic.get(key, 0), ym.get(key, 0)
                    if v:
                        ratios.add(Fraction(u, v))
                    elif u:
                        mismatches += 1
                action0 = scale(compose(transpose(xdmat), compose(h3, xdmat)), 2)
                action1 = scale(add(scale(compose(transpose(xdmat), compose(h3, stars[1])), -1),
                                    compose(transpose(stars[1]), compose(h3, xdmat))), 2)
                action2 = scale(compose(transpose(stars[1]), compose(h3, stars[1])), 2)
                p1 = scale(compose(h1, kinetic), 2)
                p2 = scale(compose(h1, compose(q, compose(xd, stars[1]))), 2)
                p3 = scale(compose(h1, compose(stars[3], xdmat)), 2)
                p4 = scale(h1, 2)
                r3 = scale(compose(h1, compose(sd, xdmat)), 2)
                r4 = scale(compose(h1, compose(sd, stars[1])), 2)
                current = [action0 == p1, action1 == add(p2, p3), action1 == add(p2, r3),
                           action2 == p4, action2 == r4, r3 == scale(p3, -1), r4 == scale(p4, -1)]
                for key, value in zip(checks, current):
                    checks[key] &= value
                for key, value in zip(nonvacuous, (p1, p2, p3, p4)):
                    nonvacuous[key] |= bool(value)
            row = {"signature": [3, 1], "conv": "prime" if prime else "pinned", "map": name}
            output["fourier"].append(dict(row, checks=checks, nonvacuous=nonvacuous))
            output["ym_symbol"].append(dict(row, ratios=[str(v) for v in sorted(ratios)], mismatches=mismatches,
                                           ym_proportional=not mismatches and len(ratios) == 1 and 0 not in ratios))
    return output


def controls():
    # Independently specified elimination controls: a rational rank-one system,
    # a full-rank system, and an entry large enough to expose fixed-width loss.
    e = Echelon(3)
    assert e.insert({0: 2, 1: 1, 2: -1})
    assert not e.insert({0: 4, 1: 2, 2: -2})
    assert e.kernel() == [{1: Fraction(1), 0: Fraction(-1, 2)}, {2: Fraction(1), 0: Fraction(1, 2)}]
    e.insert({1: 1})
    e.insert({2: 2 ** 64})
    assert e.kernel() == []
    assert exterior((0,), (0,)) == ((), 0)
    assert exterior((1,), (0,)) == ((0, 1), -1)
    a = Algebra(3, 1)
    identity = a.term((), a.identity)
    assert a.pair(identity, a.term(a.volume, a.identity)) == (4, 0)
    for i in range(4):
        for j in range(4):
            x, y = a.term((), a.gamma[i]), a.term((), a.gamma[j])
            assert add(a.wedge(x, y), a.wedge(y, x)) == (scale(identity, 2 * a.metric[i]) if i == j else {})
    for degree in range(5):
        for indices in combinations(range(4), degree):
            x = a.term(indices, a.identity)
            assert a.star(a.star(x)) == scale(x, (-1) ** (degree * (4 - degree) + 1))
    x = a.term((0, 1), a.blade((0, 1)))
    first = add(scale(a.term((0, 2, 3), a.gamma[1]), 2), scale(a.term((1, 2, 3), a.gamma[0]), -2))
    assert a.column("CCC", "F", x) == first
    assert a.column("CAA", "F+B", x) == scale(a.star(a.phi["F"]), -4)
    assert scale(scale(identity, 2 ** 62), 4) == scale(identity, 2 ** 64)
    assert scale(identity, Fraction(1, 3)) == {((), a.identity[0]): Fraction(1, 3)}


def emit(name, data):
    print(name + ": " + json.dumps(data, sort_keys=True), flush=True)


def main():
    controls()
    emit("controls", {"passed": True})
    model = Independent()
    maps, dimensions = model.equivariant()
    emit("equivariant", {"dimension": len(maps), "block_dimensions": dimensions})
    specs, blocks = model.blocks()
    relations = column_kernel(blocks)
    emit("blocks", {"rank": len(blocks) - len(relations), "zero_relations": len(relations),
                    "names": [mode + ":" + column for mode, column in specs],
                    "relations": [{str(k): str(v) for k, v in relation.items()} for relation in relations]})
    c1 = column_kernel([model.c1(matrix) for matrix in maps])
    survivors = [sum_maps(maps, vector) for vector in c1]
    responses = [model.response(matrix) for matrix in survivors]
    emit("c1", {"dimension": len(c1), "einstein_dimension": einstein_dimension(responses),
                "responses": [[str(v) for v in r] for r in responses]})
    c2 = [model.c2(matrix) for matrix in survivors]
    emit("joint", {norm: {"dimension": len(column_kernel([c[norm] for c in c2]))}
                   for norm in ("N0", "N1", "N2")})
    emit("star_signs", sign_table())
    # Assemble from the independently evaluated 20 blocks, using the written
    # definitions, not any production constructor or runtime result.
    by_name = dict(zip(specs, blocks))
    caa = add(by_name["CCC", "F"], scale(by_name["CAA", "F+B"], Fraction(-1, 2)))
    eop = add(scale(by_name["CCC", "F"], -2), scale(by_name["CCC", "F+B"], -1), by_name["CAA", "F+B"])
    emit("e_op_response", [str(v) for v in model.response(eop)])
    for name, rows in fourier_and_ym(model, {"CAA": caa, "E_OP": eop}).items():
        emit(name, rows)


if __name__ == "__main__":
    main()

