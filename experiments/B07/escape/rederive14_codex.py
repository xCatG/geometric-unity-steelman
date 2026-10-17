"""Independent exact matrix reconstruction of the bounded 14D E2 witnesses.

Sources: the 2026-10-17 14D plan's mathematics section; B02 transcription,
proofs and README; B07 escape derivations E2; phase2 derivations H12-H14;
gu.clifford's gamma matrices, Dirac pairing and documented chirality convention.
No producing implementation is imported. result14.json is comparison data only.
All Clifford calculations use actual sparse matrix entries over Q(i).
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
from math import lcm
from numbers import Integral
from operator import index
from pathlib import Path
import subprocess
from time import perf_counter_ns

from flint import fmpq
from gu.clifford import gammas, dirac_pairing


def rational(x):
    """One exact adapter; never truncate, including numpy integer inputs."""
    if isinstance(x, fmpq):
        return x
    if isinstance(x, Integral):
        return fmpq(index(x))
    if isinstance(x, Fraction):
        return fmpq(x.numerator, x.denominator)
    if isinstance(x, str):
        return fmpq(x)
    raise TypeError('exact rational required')


Z = (fmpq(0), fmpq(0))
ONE = (fmpq(1), fmpq(0))
IM = (fmpq(0), fmpq(1))
UNITS = (ONE, IM, (-ONE[0], ONE[1]), (IM[0], -IM[1]))
FAULT = None


def qa(x, y):
    return x[0] + y[0], x[1] + y[1]


def qm(x, y):
    return x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0]


def qc(x):
    return x[0], -x[1]


def clean(x):
    return {k: v for k, v in x.items() if v != Z}


def ma(x, y):
    out = dict(x)
    for k, v in y.items():
        out[k] = qa(out.get(k, Z), v)
    return clean(out)


def ms(x, scalar):
    if not isinstance(scalar, tuple):
        scalar = (rational(scalar), fmpq(0))
    return clean({k: qm(v, scalar) for k, v in x.items()})


def mm(x, y):
    """Ordinary sparse matrix multiplication, no Clifford-mask arithmetic."""
    rows = defaultdict(list)
    for (j, k), v in y.items():
        rows[j].append((k, v))
    out = {}
    for (i, j), u in x.items():
        for k, v in rows[j]:
            key = (i, k)
            out[key] = qa(out.get(key, Z), qm(u, v))
    return clean(out)


def md(x):
    return {(j, i): qc(v) for (i, j), v in x.items()}


def mono_matrix(g):
    return {(index(r), j): UNITS[index(g.phase[j]) % 4]
            for j, r in enumerate(g.perm)}


def ids(mask):
    return tuple(i for i in range(mask.bit_length()) if mask & (1 << i))


def wedge_sign(a, b):
    if a & b:
        return 0
    return (-1) ** sum((b & ((1 << i)-1)).bit_count() for i in ids(a))


def form_add(x, y):
    out = dict(x)
    for f, m in y.items():
        out[f] = ma(out.get(f, {}), m)
    return {f: m for f, m in out.items() if m}


def form_scale(x, a):
    return {f: z for f, m in x.items() if (z := ms(m, a))}


def bracket(x, y, mode):
    out = {}
    for f, u in x.items():
        for g, v in y.items():
            s = wedge_sign(f, g)
            if s:
                z = ma(mm(u, v), ms(mm(v, u), -1 if mode == 'C' else 1))
                z = ms(z, (fmpq(0), fmpq(s)) if mode == 'A' else s)
                out[f | g] = ma(out.get(f | g, {}), z)
    return {f: m for f, m in out.items() if m}


class Model:
    def __init__(self, p, q):
        self.p, self.q, self.n = p, q, p + q
        self.eta = [1]*p + [-1]*q
        self.full = (1 << self.n)-1
        raw = gammas(p, q)
        self.d = raw[0].n
        self.eye = {(j, j): ONE for j in range(self.d)}
        self.g = [mono_matrix(g) for g in raw]
        self.A = mono_matrix(dirac_pairing(p, q))
        self.blades = {0: self.eye}
        # Actual monomial matrix products supply the trace-dual basis. Group
        # by permutation support only to avoid summing identically zero traces.
        self.monomials = [(tuple(range(self.d)), (0,)*self.d)]
        gm = [(tuple(map(index, g.perm)), tuple(map(index, g.phase))) for g in raw]
        self.buckets = defaultdict(list)
        for mask in range(1 << self.n):
            if mask:
                k = mask.bit_length()-1
                ap, az = self.monomials[mask ^ (1 << k)]
                bp, bz = gm[k]
                self.monomials.append((tuple(ap[bp[j]] for j in range(self.d)),
                                       tuple((bz[j]+az[bp[j]]) % 4 for j in range(self.d))))
            perm, phase = self.monomials[mask]
            # Jordan-Wigner matrices have xor-permutation supports; verify it.
            assert all(r == (j ^ perm[0]) for j, r in enumerate(perm))
            self.buckets[perm[0]].append((mask, perm, phase))
        vol = self.blade(self.full)
        self.C = next(z for unit in UNITS if
                      (z := ms(vol, unit)) == md(z) and mm(z, z) == self.eye)
        self.F = {1 << a: g for a, g in enumerate(self.g)}
        self.Fp = {1 << a: mm(g, self.C) for a, g in enumerate(self.g)}
        self.B = {(1 << a) | (1 << b): mm(self.g[a], self.g[b])
                  for a, b in combinations(range(self.n), 2)}
        self.Bp = {f: ms(mm(m, self.C), IM) for f, m in self.B.items()}

    def blade(self, mask):
        if mask not in self.blades:
            perm, phase = self.monomials[mask]
            self.blades[mask] = {(r, j): UNITS[phase[j]] for j, r in enumerate(perm)}
        return self.blades[mask]

    def coordinates(self, x):
        """Tr(G_C^{-1} M)/dim(S); G_C^{-1}=G_C dagger for these gammas."""
        out = {}
        for f, mat in x.items():
            rebuilt = {}
            for offset in sorted({r ^ c for r, c in mat}):
                for mask, perm, phase in self.buckets[offset]:
                    acc = Z
                    for j, r in enumerate(perm):
                        acc = qa(acc, qm(UNITS[(-phase[j]) % 4], mat.get((r, j), Z)))
                    acc = (acc[0]/self.d, acc[1]/self.d)
                    if acc != Z:
                        out[f, mask] = acc
                        rebuilt = ma(rebuilt, ms(self.blade(mask), acc))
            assert rebuilt == mat, 'trace extraction must reconstruct the entire matrix'
        return out

    def star(self, x):
        out = {}
        for f, mat in x.items():
            comp = self.full ^ f
            metric = 1
            for a in ids(f):
                metric *= self.eta[a]
            if FAULT == 'star':
                metric = 1
            out[comp] = ms(mat, wedge_sign(f, comp)*metric)
        return out

    def operator(self, x, mode, h=None, hi=None):
        f, b = (form_add(self.F, self.Fp), self.Bp) if mode == 'CAC' else (self.F, self.B)
        if h is not None:
            f, b = self.conjugate(f, hi, h), self.conjugate(b, hi, h)
        sx = self.star(x)
        first = bracket(f, sx, mode[0])
        inner = self.star(bracket(b, sx, mode[1]))
        second = self.star(bracket(f, inner, mode[2]))
        return self.star(form_add(first, form_scale(second, Fraction(-1, 2))))

    @staticmethod
    def conjugate(x, left, right):
        return {f: z for f, m in x.items() if (z := mm(mm(left, m), right))}

    def curvature(self, axes):
        r = {}
        for i, j, value in ((0, 1, 1), (2, 3, 1), (0, 2, -1), (1, 3, -1)):
            a, b = axes[i], axes[j]
            v = value * (1 if FAULT == 'curvature' else self.eta[a]*self.eta[b])
            for u, w, s in ((a, b, 1), (b, a, -1)):
                for y, z, t in ((a, b, 1), (b, a, -1)):
                    r[u, w, y, z] = rational(s*t*v)
        return r

    def xi(self, r):
        out = {}
        for (a, b, c, d), v in r.items():
            if a < b and c < d:
                factor = 1 if FAULT == 'xi' else rational(Fraction(1, 2))
                z = ms(mm(self.g[c], self.g[d]), v*self.eta[c]*self.eta[d]*factor)
                f = (1 << a) | (1 << b)
                out[f] = ma(out.get(f, {}), z)
        return {f: m for f, m in out.items() if m}

    def is_weyl_tensor(self, r):
        get = lambda a, b, c, d: r.get((a, b, c, d), fmpq(0))
        for a, b, c, d in product(range(self.n), repeat=4):
            v = get(a, b, c, d)
            if v != -get(b, a, c, d) or v != -get(a, b, d, c) or v != get(c, d, a, b):
                return False
            if v + get(a, c, d, b) + get(a, d, b, c):
                return False
        return all(not sum(self.eta[a]*get(a, b, a, d) for a in range(self.n))
                   for b, d in product(range(self.n), repeat=2))

    def transport_in_weyl(self, x):
        co = self.coordinates(x)
        if any(f.bit_count() != 2 or c.bit_count() != 2 or z[1]
               for (f, c), z in co.items()):
            return False
        r = {}
        for (f, c), z in co.items():
            a, b = ids(f)
            u, v = ids(c)
            entry = 2*z[0]*self.eta[u]*self.eta[v]
            for i, j, s in ((a, b, 1), (b, a, -1)):
                for k, ell, t in ((u, v, 1), (v, u, -1)):
                    r[i, j, k, ell] = s*t*entry
        assert self.xi(r) == x, 'inverse xi must rebuild the transported matrix form'
        den = lcm(*(index(v.denominator) for v in r.values()))
        integer_r = {k: v*den for k, v in r.items()}
        assert all(v.denominator == 1 for v in integer_r.values())
        return self.is_weyl_tensor(integer_r)

    def dressing(self, blade):
        g = self.blade(blade)
        u = None
        for phase in (0, 1):
            candidate = ms(g, UNITS[phase])
            if not ma(mm(md(candidate), self.A), mm(self.A, candidate)):
                u = candidate
                break
        assert u is not None, 'a Dirac-skew phase must exist'
        square = mm(u, u)
        s = 1 if square == self.eye else -1
        assert square == ms(self.eye, s)
        t = rational(Fraction(1, 2))
        a, b = (1+t*t*s)/(1-t*t*s), -2*t/(1-t*t*s)
        h = ma(ms(self.eye, a), ms(u, b))
        hi = ma(ms(self.eye, a), ms(u, -b))
        assert mm(h, hi) == self.eye
        # Verify the Cayley equation itself, independent of its expanded form.
        assert mm(h, ma(self.eye, ms(u, t))) == ma(self.eye, ms(u, -t))
        in_u_a = mm(mm(md(h), self.A), h) == self.A
        spin0 = None  # Production leaves odd blades unclassified.
        if blade.bit_count() == 2:
            reverse_h = ma(ms(self.eye, a), ms(u, -b))
            even = all(c.bit_count() % 2 == 0 for _, c in self.coordinates({0: h}))
            vector_image = self.coordinates({1 << j: mm(mm(h, v), reverse_h)
                                             for j, v in enumerate(self.g)})
            vector_preserved = all(c.bit_count() == 1 for _, c in vector_image)
            # E2.3 supplies the continuous Cayley path for 0 <= t <= 1/2;
            # 1-t^2*s is positive for both s signs, hence no path pole.
            spin0 = (phase == 0 and even and mm(h, reverse_h) == self.eye
                     and vector_preserved and a > 0 and a*a-s*b*b == 1
                     and 1-t*t*s > 0)
        return h, hi, phase, in_u_a, spin0


def encode(co):
    return [[list(k), [str(v[0]), str(v[1])]] for k, v in sorted(co.items())]


def controls():
    assert rational(2**62)*4 == 2**64
    assert rational(Fraction(2, 3))*3 == 2
    try:
        rational(0.5)
    except TypeError:
        pass
    else:
        raise AssertionError('float adapter must reject')
    m = Model(3, 1)
    for a, b in product(range(4), repeat=2):
        assert ma(mm(m.g[a], m.g[b]), mm(m.g[b], m.g[a])) == ms(m.eye, 2*m.eta[a] if a == b else 0)
    # Independent hand expectations exercise all three seeded faults.
    assert m.star({8: m.eye}) == {7: m.eye}, 'timelike Hodge sign'
    r = m.curvature((0, 1, 2, 3))
    assert r[2, 3, 2, 3] == -1, 'mixed-plane sectional sign'
    assert m.is_weyl_tensor(r), 'small Weyl input'
    x = m.xi(r)
    assert m.coordinates(x)[3, 3] == (rational(Fraction(1, 2)), fmpq(0)), 'xi ordered-pair normalization'
    assert m.transport_in_weyl(x)
    assert not m.transport_in_weyl({3: m.g[0]}), 'ambient non-bivector impostor'
    assert not m.transport_in_weyl({3: m.blade(3)}), 'non-Ricci-flat impostor'
    assert m.coordinates({1: ms(m.g[0], Fraction(2, 3))}) == {(1, 1): (rational(Fraction(2, 3)), fmpq(0))}
    assert m.coordinates({1: ms(m.g[0], 2**64)}) == {(1, 1): (rational(2**64), fmpq(0))}
    for mode in ('CCC', 'CAA', 'CAC'):
        assert not m.operator(x, mode), 'undressed 4D Weyl annihilation'
        h, hi, _, group, spin = m.dressing(3)
        assert group and spin
        assert m.operator(x, mode, h, hi), '4D witness non-vacuity'
        assert not m.operator(m.conjugate(x, hi, h), mode, h, hi), '4D covariance'
    print(json.dumps({'event': 'controls', 'status': 'PASS'}), flush=True)


def main():
    global FAULT
    parser = argparse.ArgumentParser()
    parser.add_argument('--fault', choices=['star', 'curvature', 'xi'])
    args = parser.parse_args()
    FAULT = args.fault
    started = perf_counter_ns()
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    print(json.dumps({'event': 'start', 'source_commit': source, 'fault': FAULT}), flush=True)
    controls()
    # Results are generated without consulting comparison values or row metadata.
    computed = []
    hand = []
    for p, q in ((7, 7), (9, 5)):
        m = Model(p, q)
        if p == 7:
            for blade, a, b in ((3, Fraction(3, 5), Fraction(-4, 5)),
                                (129, Fraction(5, 3), Fraction(-4, 3))):
                h, *_ = m.dressing(blade)
                assert h == ma(ms(m.eye, a), ms(m.blade(blade), b))
                hand.append({'blade': blade, 'a': str(a), 'b': str(b), 'agree': True})
        for axes in ((0, 1, 2, 3), (0, 1, 2, p)):
            r = m.curvature(axes)
            assert r and m.is_weyl_tensor(r), 'nonzero 14D Weyl input'
            x = m.xi(r)
            assert x and m.transport_in_weyl(x)
            outside = [a for a in range(m.n) if a not in axes][:2]
            blades = [1 << axes[0]] + [(1 << a) | (1 << b) for a, b in combinations(axes, 2)]
            blades += [(1 << outside[0]) | (1 << outside[1])]
            undressed = {mode: not m.operator(x, mode) for mode in ('CCC', 'CAA', 'CAC')}
            for blade in blades:
                h, hi, phase, group, spin = m.dressing(blade)
                inverse_transport = m.conjugate(x, h, hi)
                row = {'signature': [p, q], 'axes': list(axes), 'blade': blade,
                       'phase': phase, 'in_u_a': group, 'spin0': spin,
                       'commutes': all(mm(h, v) == mm(v, h) for v in x.values()),
                       'transport_in_weyl': m.transport_in_weyl(inverse_transport), 'modes': {}}
                for mode in ('CCC', 'CAA', 'CAC'):
                    output = m.operator(x, mode, h, hi)
                    # Evaluate both sides; the covariance control is not defined as zero.
                    cov = m.operator(m.conjugate(x, hi, h), mode, h, hi)
                    co = m.coordinates(output)
                    row['modes'][mode] = {'output': encode(co), 'leak_terms': len(co),
                                          'undressed_zero': undressed[mode], 'cov_zero': not cov}
                if blade == blades[-1]:
                    assert row['commutes'] and row['transport_in_weyl']
                    assert all(not z['output'] for z in row['modes'].values()), 'outside-plane hand zero'
                computed.append(row)
                print(json.dumps({'event': 'computed', **row}), flush=True)
        del m
    assert len(computed) == 32
    assert all(any(row['modes'][mode]['output'] for row in computed) for mode in ('CCC', 'CAA', 'CAC'))
    reference_path = Path(__file__).with_name('result14.json')
    reference = json.loads(reference_path.read_text(encoding='utf-8'))
    expected = {(tuple(block['signature']), tuple(row['axes']), row['blade']): row
                for block in reference['E2_14D'] for row in block['rows']}
    assert len(expected) == 32
    comparisons = []
    for row in computed:
        key = (tuple(row['signature']), tuple(row['axes']), row['blade'])
        ref = expected[key]
        for field in ('phase', 'in_u_a', 'spin0', 'commutes', 'transport_in_weyl'):
            comparisons.append((key, field, row[field], ref[field]))
        for mode in ('CCC', 'CAA', 'CAC'):
            for field in ('output', 'leak_terms', 'undressed_zero', 'cov_zero'):
                comparisons.append((key, mode+'.'+field, row['modes'][mode][field], ref['modes'][mode][field]))
    disagreements = 0
    for key, quantity, actual, expected_value in comparisons:
        agree = actual == expected_value
        disagreements += not agree
        print(json.dumps({'event': 'comparison', 'key': key, 'quantity': quantity,
                          'actual': actual, 'expected': expected_value, 'agree': agree}), flush=True)
    print(json.dumps({'event': 'summary', 'comparisons': len(comparisons),
                      'disagreements': disagreements, 'hand_cayley': hand,
                      'runtime_ns': perf_counter_ns()-started,
                      'reference_source_commit': reference['source_commit']}), flush=True)
    assert not disagreements, 'comparison disagreement; preserve and report every finding'


if __name__ == '__main__':
    main()
