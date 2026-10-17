"""Independent exact Task 4 check, using gamma matrices and documented formulas.

No producing escape/B02 implementation is imported. Curvature is built as the
kernel of the Bianchi equations on Sym^2(Lambda^2); all ranks are over Q.
Forms carry actual 4 by 4 SymPy matrices, including in the trace pairing.

The B02 README's xi sum is interpreted as a<b and c<d, with coefficient 1/2.
That interpretation is pinned by its independent KN(g,g) response control.
E_OP uses the three-block formula in B07/phase2/README.md, newly allowed by
the addendum. The raw second block excludes (9.3)'s external -1/2 coefficient;
its convention is checked against that README's linear response, not fitted Q.

Run normally with no arguments. --fault selects a precommitted seeded fault;
each such run must fail a mathematical comparison, not an import or syntax gate.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, product
import json
from numbers import Integral
from pathlib import Path
import subprocess
from time import perf_counter_ns

import sympy as s

from gu.clifford import gammas


PAIRS = tuple(combinations(range(4), 2))
INDICES = tuple(product(range(4), repeat=4))
INDEX = {abcd: i for i, abcd in enumerate(INDICES)}
HALF = s.Rational(1, 2)
ZERO = s.zeros(4)
IDENTITY = s.eye(4)


def exact(value):
    """One numeric gate: integers, rationals, and Gaussian rationals only."""
    if isinstance(value, Integral):
        return s.Integer(value)
    if isinstance(value, Fraction):
        return s.Rational(value.numerator, value.denominator)
    if isinstance(value, s.Expr) and not value.has(s.Float):
        re, im = s.expand(value).as_real_imag()
        if re.is_Rational and im.is_Rational:
            return re + s.I * im
    raise TypeError('exact rational or Gaussian rational required')


def clean(matrix):
    return matrix.applyfunc(exact)


def tidy(form):
    normalized = {f: clean(m) for f, m in form.items()}
    return {f: m for f, m in normalized.items() if m != ZERO}


def add(x, y, coefficient=1):
    coefficient = exact(coefficient)
    out = dict(x)
    for f, matrix in y.items():
        out[f] = out.get(f, ZERO) + coefficient * matrix
    return tidy(out)


def wedge_sign(a, b):
    if a & b:
        return 0
    inversions = sum(1 for i in range(4) for j in range(4)
                     if a & (1 << i) and b & (1 << j) and i > j)
    return (-1) ** inversions


def components(form, degree):
    """Real coordinates: keep real/imaginary parts, not complex ranks."""
    result = []
    for f in range(16):
        if f.bit_count() == degree:
            for z in form.get(f, ZERO):
                result.extend(exact(z).as_real_imag())
    return s.Matrix(result)


def matrix_coordinates(matrix):
    return s.Matrix([part for z in matrix for part in exact(z).as_real_imag()])


class Model:
    def __init__(self, p, fault=None):
        self.p = p
        self.metric = tuple(1 if a < p else -1 for a in range(4))
        self.g = s.diag(*self.metric)
        self.fault = fault
        self.gamma = []
        for mono in gammas(p, 4 - p):
            re, im = mono.to_dense()
            self.gamma.append(s.Matrix(4, 4, lambda a, b:
                                       exact(re[a, b]) + s.I * exact(im[a, b])))
        self.blade = []
        for mask in range(16):
            matrix = IDENTITY
            for a in range(4):
                if mask & (1 << a):
                    matrix = matrix * self.gamma[a]
            self.blade.append(clean(matrix))
        # Choose chirality from its defining C^2=1 and Hermiticity conditions.
        self.chirality = next(clean(s.I ** k * self.blade[15]) for k in range(4)
                              if clean((s.I ** k * self.blade[15]) ** 2) == IDENTITY
                              and (s.I ** k * self.blade[15]).H
                              == s.I ** k * self.blade[15])
        self.F = {1 << a: self.gamma[a] for a in range(4)}
        self.Fprime = {f: clean(m * self.chirality) for f, m in self.F.items()}
        self.B = {(1 << a) | (1 << b): self.gamma[a] * self.gamma[b]
                  for a, b in PAIRS}
        self.Bprime = {f: clean(s.I * m * self.chirality) for f, m in self.B.items()}

    def weight(self, mask):
        out = 1
        for a in range(4):
            if mask & (1 << a):
                out *= self.metric[a]
        return out

    def star(self, form):
        return tidy({15 ^ f: wedge_sign(f, 15 ^ f) * self.weight(f) * m
                     for f, m in form.items()})

    def bracket(self, x, y, mode):
        out = {}
        for f, a in x.items():
            for g, b in y.items():
                sign = wedge_sign(f, g)
                if sign:
                    matrix = a * b - b * a if mode == 'C' else s.I * (a * b + b * a)
                    out[f | g] = out.get(f | g, ZERO) + sign * matrix
        return tidy(out)

    def shiab(self, x, mode):
        f, b = (add(self.F, self.Fprime), self.Bprime) if mode == 'CAC' else (self.F, self.B)
        sx = self.star(x)
        first = self.bracket(f, sx, mode[0])
        inner = self.star(self.bracket(b, sx, mode[1]))
        second = self.star(self.bracket(f, inner, mode[2]))
        coefficient = HALF if self.fault == 'scalar-sign' else -HALF
        return add(first, second, coefficient)

    def first(self, x, phi, mode):
        """Raw first block of (9.3): [phi wedge *x]."""
        return self.bracket(phi, self.star(x), mode)

    def second(self, x, phi1, phi2, modes):
        """Raw nested block: *[phi1 wedge *[phi2 wedge *x]], inner then outer.

        The external -1/2 belongs to shiab, not to this building block.
        """
        inner = self.star(self.bracket(phi2, self.star(x), modes[0]))
        return self.star(self.bracket(phi1, inner, modes[1]))

    def e_op(self, x):
        """Phase 2 README: -2 first[C](F) - second[CC](F,B) + second[AA](F,B)."""
        first_coefficient = 2 if self.fault == 'eop-first-sign' else -2
        second_coefficient = HALF if self.fault == 'eop-second-scale' else 1
        result = add({}, self.first(x, self.F, 'C'), first_coefficient)
        result = add(result, self.second(x, self.F, self.B, 'CC'), -1)
        return add(result, self.second(x, self.F, self.B, 'AA'), second_coefficient)

    def embed_tensor(self, tensor):
        """E_F(H) = sum e^a H_a^b Gamma_b, with its second index raised."""
        tensor = clean(tensor)
        return tidy({1 << a: sum((tensor[a, b] * self.metric[b] * self.gamma[b]
                                  for b in range(4)), ZERO) for a in range(4)})

    def pairing(self, x, y):
        # Exactly Tr(x wedge *y)/4; no scalar-blade shortcut.
        out = s.S.Zero
        for f, a in x.items():
            for g, b in self.star(y).items():
                if f | g == 15:
                    out += wedge_sign(f, g) * s.trace(a * b) / 4
        return exact(out)

    def xi(self, tensor):
        tensor = tuple(exact(z) for z in tensor)
        factor = 2 if self.fault == 'xi-scale' else HALF
        out = {}
        for a, b in PAIRS:
            matrix = ZERO
            for c, d in PAIRS:
                matrix += (factor * tensor[INDEX[a, b, c, d]] * self.metric[c]
                           * self.metric[d] * self.gamma[c] * self.gamma[d])
            out[(1 << a) | (1 << b)] = matrix
        return tidy(out)

    def ricci(self, tensor):
        return s.Matrix(4, 4, lambda b, d: sum(
            self.metric[a] * tensor[INDEX[a, b, a, d]] for a in range(4)))

    def scalar(self, ricci):
        return sum(self.metric[a] * ricci[a, a] for a in range(4))

    def kn(self, a, b):
        return s.Matrix([a[i, k] * b[j, l] + a[j, l] * b[i, k]
                         - a[i, l] * b[j, k] - a[j, k] * b[i, l]
                         for i, j, k, l in INDICES])

    def split(self, tensor):
        ric = self.ricci(tensor)
        scalar = self.scalar(ric)
        traceless = ric - scalar * self.g / 4
        weyl = tensor - self.kn(self.g, ric) / 2 + scalar * self.kn(self.g, self.g) / 12
        return weyl, traceless, scalar

    def contract(self, x, y):
        return sum(self.metric[a] * self.metric[b] * self.metric[c] * self.metric[d]
                   * x[k] * y[k] for k, (a, b, c, d) in enumerate(INDICES))

    def dual(self, tensor):
        factor = 1 if self.fault == 'dual-half' else HALF
        return s.Matrix([factor * sum(s.LeviCivita(c, d, e, f) * self.metric[e]
                                    * self.metric[f] * tensor[INDEX[a, b, e, f]]
                                    for e in range(4) for f in range(4))
                         for a, b, c, d in INDICES])

    def invariants(self, left, right):
        w, r, scalar = left
        v, t, other_scalar = right
        even = self.contract(w, v)
        odd = (self.contract(w, self.dual(v)) + self.contract(v, self.dual(w))) / 2
        ric = sum(self.metric[a] * self.metric[b] * r[a, b] * t[a, b]
                  for a in range(4) for b in range(4))
        return [even, odd, ric, scalar * other_scalar]

    def cayley(self, blade):
        k = blade.bit_count()
        # B02 transcription: sharp sign (-1)^(q*k + k*(k-1)/2).
        sharp_sign = (-1) ** ((4 - self.p) * k + k * (k - 1) // 2)
        generator = self.blade[blade] * (1 if sharp_sign == -1 else s.I)
        x = generator / 2
        h = clean((IDENTITY - x) * (IDENTITY + x).inv())
        inverse = clean(h.inv())
        return h, inverse

    @staticmethod
    def conjugate(form, left, right):
        return tidy({f: clean(left * m * right) for f, m in form.items()})

    def dressed(self, form, h, inverse):
        return self.conjugate(self.shiab(self.conjugate(form, h, inverse), 'CCC'), inverse, h)


def curvature_basis():
    """Symmetric 6x6 pair tensors, then impose every cyclic Bianchi equation."""
    candidates = []
    for i in range(6):
        for j in range(i, 6):
            tensor = s.zeros(256, 1)
            for left, right in {(i, j), (j, i)}:
                a, b = PAIRS[left]
                c, d = PAIRS[right]
                for aa, bb, sign1 in ((a, b, 1), (b, a, -1)):
                    for cc, dd, sign2 in ((c, d, 1), (d, c, -1)):
                        tensor[INDEX[aa, bb, cc, dd]] = sign1 * sign2
            candidates.append(tensor)
    bianchi = s.Matrix([[t[INDEX[a, b, c, d]] + t[INDEX[a, c, d, b]]
                         + t[INDEX[a, d, b, c]] for t in candidates]
                        for a, b, c, d in INDICES])
    spanning = s.Matrix.hstack(*candidates)
    basis = [spanning * v for v in bianchi.nullspace()]
    assert s.Matrix.hstack(*basis).rank() == 20, 'algebraic-curvature basis rank'
    return basis


def fit(design, values):
    coefficients, parameters = design.gauss_jordan_solve(s.Matrix(values))
    assert parameters.rows == 0, 'four invariants must be identifiable'
    assert design * coefficients == s.Matrix(values), 'all 210 polarized equations'
    return [exact(z) for z in coefficients]


def show(value):
    if isinstance(value, (list, tuple)):
        return '(' + ', '.join(show(z) for z in value) + ')'
    return str(value)


class Report:
    def __init__(self):
        self.agree = 0
        self.disagree = 0
        self.unavailable = 0

    def compare(self, quantity, value, expected):
        okay = value == expected
        self.agree += okay
        self.disagree += not okay
        status = 'agree' if okay else 'DISAGREE'
        print(f'| {quantity} | {show(value)} | {show(expected)} | {status} |', flush=True)
        if not okay:
            print(f'FINDING: {quantity}: {show(value)} != {show(expected)}', flush=True)

    def missing(self, quantity, expected):
        self.unavailable += 1
        print(f'| {quantity} | not independently reconstructible | {show(expected)} | unavailable |', flush=True)


def controls(model, report, label):
    # A hand-built diagonal pair Weyl tensor. Pair entries solve Ric=0 directly:
    # R0101=R2323=e0*e1, R0202=R1313=-e0*e2, R0303=R1212=0,
    # with signature factors instead handled by R_abab=e_a*e_b*k_ab.
    weights = {(0, 1): 1, (0, 2): -1, (0, 3): 0,
               (1, 2): 0, (1, 3): -1, (2, 3): 1}
    w = s.zeros(256, 1)
    for (a, b), value in weights.items():
        value *= model.metric[a] * model.metric[b]
        w[INDEX[a, b, a, b]] = w[INDEX[b, a, b, a]] = value
        w[INDEX[a, b, b, a]] = w[INDEX[b, a, a, b]] = -value
    report.compare(f'{label} hand W Ricci', list(model.ricci(w)), [0] * 16)
    # Independent hand dual: for each ordered cd, only its complementary ef
    # contributes after the two antisymmetric terms cancel the 1/2.
    hand_dual = s.zeros(256, 1)
    for a, b, c, d in INDICES:
        if c != d:
            e, f = tuple(k for k in range(4) if k not in (c, d))
            hand_dual[INDEX[a, b, c, d]] = (s.LeviCivita(c, d, e, f)
                * model.metric[e] * model.metric[f] * w[INDEX[a, b, e, f]])
    report.compare(f'{label} dual matches hand complement construction', model.dual(w) == hand_dual, True)
    report.compare(f'{label} W.W nonvacuity', model.contract(w, w), 16)
    report.compare(f'{label} W.*(hand *W)', model.contract(w, model.dual(hand_dual)), -16)
    # W+*W makes the parity-odd pairing nonzero, so a missing half is detectable.
    mixed = w + hand_dual
    report.compare(f'{label} mixed W.*W normalization', model.contract(mixed, model.dual(mixed)), -32)
    gg = model.kn(model.g, model.g)
    ric = model.ricci(gg)
    report.compare(f'{label} KN(g,g) Ricci=6g', ric == 6 * model.g, True)
    report.compare(f'{label} KN(g,g) scalar', model.scalar(ric), 24)
    report.compare(f'{label} KN(g,g) Ric.Ric', sum(model.metric[a] * model.metric[b] * ric[a, b] ** 2
                                               for a in range(4) for b in range(4)), 144)
    for mode, coefficient in (('CCC', -6), ('CAA', 6)):
        response = model.star(model.shiab(model.xi(gg), mode))
        report.compare(f'{label} KN(g,g) *{mode}(xi)=({coefficient})F',
                       response == tidy({f: coefficient * m for f, m in model.F.items()}), True)
    e_output = model.e_op(model.xi(gg))
    report.compare(f'{label} KN(g,g) Q(E_OP)', model.pairing(e_output, e_output), -576)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fault', choices=('xi-scale', 'dual-half', 'scalar-sign',
                                           'eop-first-sign', 'eop-second-scale'))
    args = parser.parse_args()
    start = perf_counter_ns()
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    print(f'source_commit: {commit}\nfault: {args.fault or "none"}', flush=True)
    data = json.loads(Path(__file__).with_name('result.json').read_text(encoding='utf-8'))
    report = Report()
    print('| Quantity | Independent value | Task 2/3 or documented control | Comparison |')
    print('|---|---|---|---|')
    # P4 adapter controls: these run before any mathematical computation.
    report.compare('exact rational adapter', exact(Fraction(2, 3)), s.Rational(2, 3))
    report.compare('exact large integer adapter', exact(2 ** 62) * 4, s.Integer(2 ** 64))
    rejected = 0
    for inexact in (0.5, s.Float('0.5'), complex(1, 0)):
        try:
            exact(inexact)
        except TypeError:
            rejected += 1
    report.compare('inexact inputs rejected', rejected, 3)
    basis = curvature_basis()
    for p in (3, 1):
        label = f'({p},{4-p})'
        model = Model(p, args.fault)
        original1 = next(row for row in data['E1'] if row['signature'] == [p, 4 - p])
        original2 = next(row for row in data['E2'] if row['signature'] == [p, 4 - p])
        report.compare(f'{label} curvature dimension', len(basis), original1['basis_dim'])
        ricci_map = s.Matrix.hstack(*(s.Matrix(list(model.ricci(t))) for t in basis))
        weyl = [s.Matrix.hstack(*basis) * v for v in ricci_map.nullspace()]
        report.compare(f'{label} Weyl dimension', len(weyl), original2['weyl_dim'])
        splits = [model.split(t) for t in basis]
        report.compare(f'{label} Weyl projection has zero Ricci',
                       all(model.ricci(w) == ZERO for w, _, _ in splits), True)
        pairs = [(i, j) for i in range(20) for j in range(i, 20)]
        design = s.Matrix([model.invariants(splits[i], splits[j]) for i, j in pairs])
        report.compare(f'{label} invariant design rank', design.rank(), 4)
        inputs = [model.xi(t) for t in basis]
        for mode, name in (('CCC', 'CCC literal'), ('CAA', 'CAA Einstein'), ('CAC', 'CAC chiral')):
            outputs = [model.shiab(x, mode) for x in inputs]
            # CAC can be a nonzero null response; enforce nonvacuity on outputs.
            report.compare(f'{label} {mode} nonzero response exists', any(outputs), True)
            coefficients = fit(design, [model.pairing(outputs[i], outputs[j]) for i, j in pairs])
            for part, selector in (('re', s.re), ('im', s.im)):
                report.compare(f'{label} Q({mode}) {part} fit (210 pairs)',
                               [selector(z) for z in coefficients],
                               [s.Rational(z) for z in original1['Q']['pinned'][name][part]])
            report.compare(f'{label} {mode} undressed Weyl rank',
                           s.Matrix.hstack(*(components(model.shiab(model.xi(t), mode), 3)
                                             for t in weyl)).rank(),
                           original2['modes'][mode]['undressed_leak_rank'])
        e_outputs = [model.e_op(x) for x in inputs]
        report.compare(f'{label} E_OP linear response 2E_F(Ric)-S E_F(g) (20 inputs)',
                       all(model.star(output) == model.embed_tensor(
                           2 * model.ricci(t) - model.scalar(model.ricci(t)) * model.g)
                           for t, output in zip(basis, e_outputs)), True)
        e_coefficients = fit(design, [model.pairing(e_outputs[i], e_outputs[j]) for i, j in pairs])
        report.compare(f'{label} Q(E_OP) re/im fits',
                       [[selector(z) for z in e_coefficients] for selector in (s.re, s.im)],
                       [[s.Rational(z) for z in original1['Q']['pinned']['E_OP'][part]]
                        for part in ('re', 'im')])
        controls(model, report, label)
        # Direct matrix centralizer in the six real bivector spin directions.
        for blade in range(1, 16):
            h, inverse = model.cayley(blade)
            commutators = [matrix_coordinates(clean(m * h - h * m)) for m in model.B.values()]
            centralizer = 6 - s.Matrix.hstack(*commutators).rank()
            for mode in ('CCC', 'CAA', 'CAC'):
                old = next(row for row in original2['modes'][mode]['rows'] if row['blade'] == blade)
                report.compare(f'{label} blade {blade:04b} centralizer vs {mode} residual', centralizer, old['residual'])
            # Independent U(A) control using a Hermitian timelike gamma product.
            pairing = IDENTITY
            for a in range(p, 4):
                pairing = pairing * model.gamma[a]
            pairing = next(clean(s.I ** k * pairing) for k in range(4)
                           if (s.I ** k * pairing).H == s.I ** k * pairing)
            report.compare(f'{label} blade {blade:04b} h^dagger A h=A', clean(h.H * pairing * h) == pairing, True)
        if p == 3:
            for blade in (1, 3, 7, 15):
                h, inverse = model.cayley(blade)
                outputs = [model.dressed(model.xi(t), h, inverse) for t in weyl]
                rank = s.Matrix.hstack(*(components(x, 3) for x in outputs)).rank()
                old = next(row for row in original2['modes']['CCC']['rows'] if row['blade'] == blade)
                report.compare(f'{label} CCC blade {blade:04b} leak rank', rank, old['leak_rank'])
                aligned = [model.dressed(model.conjugate(model.xi(t), inverse, h), h, inverse) for t in weyl]
                report.compare(f'{label} CCC blade {blade:04b} transported Weyl defect',
                               sum(bool(x) for x in aligned), old['cov_defect'])
            x = {}
            for (f, c), coefficient in {(3, 9): -12, (9, 3): 12, (6, 12): -12, (12, 6): 12}.items():
                x[f] = x.get(f, ZERO) + coefficient * model.blade[c]
            weyl_columns = s.Matrix.hstack(*(components(model.xi(t), 2) for t in weyl))
            report.compare('P4 witness belongs to xi(Weyl)',
                           weyl_columns.row_join(components(x, 2)).rank(), 10)
            h, inverse = model.cayley(7)
            transported = model.conjugate(x, h, inverse)
            grade3 = {}
            for f, matrix in transported.items():
                for c in range(16):
                    if c.bit_count() == 3:
                        coefficient = exact(s.trace(model.blade[c].inv() * matrix) / 4)
                        if coefficient:
                            grade3[f, c] = coefficient
            print('P4 transported grade-3 coefficients: ' + show(sorted(grade3.items())), flush=True)
            report.compare('P4 witness transported grade-3 is nonzero', bool(grade3), True)
            report.compare('P4 witness dressed CCC output zero', model.dressed(x, h, inverse) == {}, True)
    print('E_OP SOURCE: phase2/README.md supplies -2 first[C] - second[CC] + second[AA]; '
          'raw blocks follow (9.3), with their normalization checked against the documented linear response.', flush=True)
    print('CONVENTION: xi uses 1/2 sum over a<b, c<d; B02 README omits those summation ranges, '
          'but its KN(g,g) response pins this normalization.', flush=True)
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == commit, 'HEAD changed during run'
    elapsed_ms = (perf_counter_ns() - start) // 1_000_000
    print(f'SUMMARY: agree={report.agree}, disagree={report.disagree}, unavailable={report.unavailable}; elapsed_ms={elapsed_ms}', flush=True)
    assert report.disagree == 0, f'{report.disagree} mathematical comparisons disagree (see FINDING rows)'
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
