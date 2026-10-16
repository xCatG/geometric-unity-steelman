"""Independent matrix re-derivation of B07, reading V (not a blind comparison).

Run from the repository root: uv run python -m experiments.B07.rederive
Only gu.clifford is shared with the production calculation; no gu.forms,
gu.cliffform, gu.shiab or B07 modules are imported. Exterior forms use sorted
index tuples and explicit monomial matrices, interned up to a real sign.
Products and traces use Mono matrix operations, never a blade-product rule.

Conventions (B02 transcription, (9.3)):
  eta = diag(+1 repeated p, -1 repeated q); vol = e^0 wedge ... wedge e^(n-1).
  Gamma_a Gamma_b + Gamma_b Gamma_a = 2 eta_ab; gamma blades are ordered.
  C = i^s Gamma_0 ... Gamma_(n-1), with the smallest s in {0,1,2,3}
      making C Hermitian and C^2 = 1 (s=1 at (3,1), s=0 at (7,7)).
  F = sum e^a Gamma_a, F' = sum e^a Gamma_a C;
  B = sum_(a<b) e^ab Gamma_a Gamma_b, B' = sum e^ab i Gamma_a Gamma_b C.
  No factorials or further generator normalization. Dressing epsilon = 1.
  *e^I = sign(I,I-complement) product_(a in I) eta_aa e^(I-complement).
  C-bracket = XY-YX, A-bracket = i(XY+YX), on matrix coefficients;
      the exterior factors retain their order. Mode order: first, inner, outer.
  X(x) = [Phi1,*x] - (1/2)*[Phi1,*[Phi2,*x]].
  Six columns: F, F+B, F+B', F', F'+B, F'+B'. The '+' labels denote
      the second term WITHOUT -1/2, not a sum with the first term.
      Coefficients: alpha, -alpha gamma/2, -alpha delta/2,
                    beta, -beta gamma/2, -beta delta/2.
  Tr is the actual matrix trace, of dimension 2^(n/2): 4 in 4D, 128 in 14D.
      result.json uses Tr/2^(n/2); only normalized witness values divide by it.
  N1: b(u,v) = (u wedge v + v wedge u)/2 for one-forms.

C1 is enumerated on k and all t_i,a_j with i<=j. C2 is enumerated on every
alpha and i<=j: diagonal values and off-diagonal polynomial coefficients.
We compute 3*C2 as -2 D(alpha,t_i,t_j)+D(t_i,alpha,t_j)+D(t_j,alpha,t_i),
where D(a,u,v)=Tr(a wedge X(u wedge v + v wedge u)); divide by two on the
diagonal. This integer rescaling preserves kernels and nonzero-entry counts.
Exact nullspaces are over C (all coefficients lie in Q(i)). The 64 one-forms
at n=4 span the complexification of the real adjoint space. These are 4D
family identities; the three 14D evaluations have counterexample scope only.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
import json
from numbers import Integral

import numpy as np
import sympy as sp

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


def nullspace(columns):
    """Remove duplicate rows, then take the exact complex nullspace (six columns)."""
    keys = set().union(*(set(col) for col in columns))
    rows = {tuple(col.get(key, ZERO) for col in columns) for key in keys}
    matrix = sp.Matrix([[sp.Rational(re) + sp.I * sp.Rational(im) for re, im in row]
                        for row in sorted(rows)]) if rows else sp.zeros(0, len(columns))
    return [[str(x) for x in vector] for vector in matrix.nullspace()]


def c1_columns(algebra, mode, basis):
    columns = []
    for column in COLUMNS:
        entries = {}
        for k in algebra.volume:
            ek = algebra.term((k,), algebra.identity)
            images = [algebra.column(mode, column, algebra.wedge(ek, a)) for a in basis]
            for i, j in combinations_with_replacement(range(len(basis)), 2):
                value = zadd(algebra.pair(basis[i], images[j]), algebra.pair(basis[j], images[i]))
                if value != ZERO:
                    entries[k, i, j] = value
        columns.append(entries)
    return columns


def c2_columns(algebra, mode, basis):
    """Polarized 3*C2 under N1, from a symmetric bilinear product table."""
    pairs = list(combinations_with_replacement(range(len(basis)), 2))
    products = {(i, j): add(algebra.wedge(basis[i], basis[j]), algebra.wedge(basis[j], basis[i]))
                for i, j in pairs}
    columns = []
    for column in COLUMNS:
        d = {}
        for (i, j), form in products.items():
            image = algebra.column(mode, column, form)
            if image:
                for a, alpha in enumerate(basis):
                    value = algebra.pair(alpha, image)
                    if value != ZERO:
                        d[a, i, j] = value

        def lookup(a, i, j):
            return d.get((a, min(i, j), max(i, j)), ZERO)

        entries = {}
        for a in range(len(basis)):
            for i, j in pairs:
                value = zadd(zscale(lookup(a, i, j), -2),
                             zadd(lookup(i, a, j), lookup(j, a, i)))
                if value != ZERO:
                    entries[a, i, j] = zscale(value, Fraction(1, 2)) if i == j else value
        columns.append(entries)
    return columns


def controls():
    """Identity controls, with hand expectations rather than survey outcomes."""
    a = Algebra(3, 1)
    ident = a.term((), a.identity)
    assert a.chirality_phase == 1, "chirality phase"
    assert a.pair(ident, a.term(a.volume, a.identity)) == (4, 0), "actual matrix trace"
    assert a.pair(ident, a.term(a.volume, a.imaginary(a.identity))) == (0, 4), "imaginary trace"
    for i in range(4):
        for j in range(4):
            x, y = a.term((), a.gamma[i]), a.term((), a.gamma[j])
            expected = scale(ident, 2 * a.metric[i]) if i == j else {}
            assert add(a.wedge(x, y), a.wedge(y, x)) == expected, "Clifford relation"
    for size in range(5):
        for indices in combinations(range(4), size):
            form = a.term(indices, a.identity)
            norm = 1
            for i in indices:
                norm *= a.metric[i]
            assert a.wedge(form, a.star(form)) == scale(a.term(a.volume, a.identity), norm), "Hodge metric"
            assert a.star(a.star(form)) == scale(form, (-1) ** (size * (4 - size) + 1)), "Hodge square"
    e0, e1 = (a.term((i,), a.identity) for i in (0, 1))
    assert a.wedge(e0, e0) == {}, "wedge repeated index"
    assert a.wedge(e0, e1) == scale(a.wedge(e1, e0), -1), "wedge parity"
    x = a.term((0, 1), a.blade((0, 1)))
    # [F,*e01 Gamma01] = 2 e023 Gamma1 - 2 e123 Gamma0.
    first = add(scale(a.term((0, 2, 3), a.gamma[1]), 2),
                scale(a.term((1, 2, 3), a.gamma[0]), -2))
    assert a.column("CCC", "F", x) == first, "hand first term"
    # Inner A gives -2i vol, *vol=-1; outer A gives -4F.
    assert a.column("CAA", "F+B", x) == scale(a.star(a.phi["F"]), -4), "hand second term"
    assert a.operator("CAA", a.phi["F"], a.phi["B"], x) == add(first, scale(a.star(a.phi["F"]), 2)), "hand minus half"
    assert scale(ident, Fraction(1, 3)) == {((), a.identity[0]): Fraction(1, 3)}, "rational exactness"
    assert scale(scale(ident, 2**62), 4) == scale(ident, 2**64), "large integer exactness"
    assert scale(scale(ident, np.int64(2**62)), 4) == scale(ident, 2**64), "fixed-width integer exactness"
    assert scale(scale(ident, Fraction(np.int64(2**62), 1)), 4) == scale(ident, 2**64), "fixed-width rational exactness"
    try:
        scale(ident, 0.5)
    except ValueError:
        pass
    else:
        raise AssertionError("float accepted")
    # alpha=u=e0 Gamma0, v=e1 Gamma1: uv+vu=2 e01 Gamma01.
    # The hand first term above gives D(u,u,v)=-16, D(v,u,u)=0,
    # and D(v,u,v)=-16 (e1 wedge e023 has negative orientation).
    # Thus the off-diagonal 3*C2 is 16, and 3*C2(u;v)=-16.
    u, v = (a.term((i,), a.gamma[i]) for i in (0, 1))
    residual = c2_columns(a, "CCC", [u, v])[0]
    assert residual[0, 0, 1] == (16, 0), "C2 off-diagonal"
    assert residual[0, 1, 1] == (-16, 0), "C2 diagonal"
    assert (0, 0, 0) not in residual, "C2 zero entry"
    # Kernel control: i*x+y=0 has vector (i,1).
    assert nullspace([{0: (0, 1)}, {0: (1, 0)}]) == [["I", "1"]], "complex kernel"


def witnesses():
    a = Algebra(7, 7)
    assert a.chirality_phase == 0
    # Inputs copied from result.json; expected values are not used in computation.
    specs = (("CCC", "literal", (0,), (0, 1)),
             ("CAA", "Einstein", (2,), (1, 2)),
             ("CAC", "chiral", (2,), (1, 2)))
    out = []
    for mode, name, ti, ai in specs:
        phi1 = add(a.phi["F"], a.phi["F'"]) if mode == "CAC" else a.phi["F"]
        phi2 = a.phi["B'"] if mode == "CAC" else a.phi["B"]
        t, alpha = a.term((0,), a.blade(ti)), a.term((1,), a.blade(ai))
        ek = a.term((0,), a.identity)
        image_a = a.operator(mode, phi1, phi2, a.wedge(ek, alpha))
        image_t = a.operator(mode, phi1, phi2, a.wedge(ek, t))
        value = zadd(a.pair(t, image_a), a.pair(alpha, image_t))
        out.append({"branch": name, "mode": mode, "k": 0,
                    "t": [0, list(ti)], "a": [1, list(ai)],
                    "matrix_trace": [str(x) for x in value],
                    "normalized_trace": [str(Fraction(x, a.dim)) for x in value]})
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--controls-only", action="store_true")
    args = parser.parse_args()
    controls()
    print("CONTROLS: PASS", flush=True)
    if args.controls_only:
        return
    print("COLUMNS: " + json.dumps(COLUMNS), flush=True)
    a = Algebra(3, 1)
    basis = a.one_basis()
    for mode in MODES:
        c1 = c1_columns(a, mode, basis)
        kernel = nullspace(c1)
        print("C1: " + json.dumps({"mode": mode, "kernel_dimension": len(kernel),
                                   "kernel": kernel, "nonzero": [len(c) for c in c1]}), flush=True)
        if mode in ("CCC", "CAA"):
            c2 = c2_columns(a, mode, basis)
            kernel = nullspace(c2)
            print("C2_N1: " + json.dumps({"mode": mode, "kernel_dimension": len(kernel),
                                          "kernel": kernel, "nonzero": [len(c) for c in c2]}), flush=True)
    for witness in witnesses():
        print("WITNESS_7_7: " + json.dumps(witness), flush=True)


if __name__ == "__main__":
    main()
