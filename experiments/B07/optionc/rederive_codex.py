"""Independent B07 option C reconstruction from the documented formulas.

Only gu.clifford.gammas and dirac_pairing are shared with the producer.
All exterior algebra, operators, pairings, kernels and inertia are rebuilt here.
No files are written. result.json is read only after all computations finish.
"""
from itertools import combinations
from math import prod
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from gu.clifford import gammas, dirac_pairing

I = s.I
nu = s.Symbol("nu")
FORMS = {k: [m for m in range(16) if m.bit_count() == k] for k in range(5)}


def clean(x):
    return s.expand(x)


def dm(m, field=None):
    out = DomainMatrix.from_Matrix(s.Matrix(m))
    return out.convert_to(field) if field else out.to_field()


def rank(m, field=None):
    return len(dm(m, field).rref()[1])


def kernel(m, field=None):
    return dm(m, field).nullspace().to_Matrix().T


def zero(m):
    return all(s.simplify(x) == 0 for x in m)


def inertia(m):
    """Exact Hermitian congruence with scalar and neutral 2x2 pivots."""
    m = s.Matrix(m).applyfunc(s.simplify)
    assert zero(m - m.conjugate().T)
    pos = neg = 0
    while m.rows:
        pivot = next((j for j in range(m.rows) if m[j, j] != 0), None)
        if pivot is not None:
            order = [pivot] + [j for j in range(m.rows) if j != pivot]
            m = m.extract(order, order)
            d = s.simplify(m[0, 0])
            sign = s.sign(d)
            assert sign in (-1, 1), d
            pos += int(sign == 1)
            neg += int(sign == -1)
            m = (m[1:, 1:] - m[1:, :1] * m[:1, 1:] / d).applyfunc(s.simplify)
        else:
            pair = next(((a, b) for a in range(m.rows) for b in range(a + 1, m.rows)
                         if m[a, b] != 0), None)
            if pair is None:
                return [pos, neg, m.rows]
            order = list(pair) + [j for j in range(m.rows) if j not in pair]
            m = m.extract(order, order)
            pos += 1
            neg += 1
            m = (m[2:, 2:] - m[2:, :2] * m[:2, :2].inv() * m[:2, 2:]).applyfunc(s.simplify)
    return [pos, neg, 0]


def wedge_sign(a, b):
    if a & b:
        return 0
    return (-1) ** sum((b & ((1 << j) - 1)).bit_count() for j in range(4) if a >> j & 1)


def add(*terms):
    out = {}
    for scale, value in terms:
        for key, v in value.items():
            out[key] = clean(out.get(key, 0) + scale * v)
    return {key: v for key, v in out.items() if v != 0}


class Algebra:
    def __init__(self, p, q):
        self.p, self.q = p, q
        self.eta = [1] * p + [-1] * q
        def dense(m):
            a, b = m.to_dense()
            return s.Matrix(a.tolist()) + I * s.Matrix(b.tolist())
        gamma = [dense(m) for m in gammas(p, q)]
        self.blades = []
        for mask in range(16):
            g = s.eye(4)
            for j in range(4):
                if mask >> j & 1:
                    g = g * gamma[j]
            self.blades.append(g)
        a = dense(dirac_pairing(p, q))
        self.phase = []
        for g in self.blades:
            ph = next(I ** k for k in (0, 1) if zero((I ** k * g).conjugate().T * a + a * (I ** k * g)))
            self.phase.append(ph)
        self.mul = {}
        for c in range(16):
            for d in range(16):
                e = c ^ d
                coefficient = s.trace(self.blades[e].inv() * self.blades[c] * self.blades[d]) / 4
                assert zero(self.blades[c] * self.blades[d] - coefficient * self.blades[e])
                self.mul[c, d] = coefficient
        vol = self.blades[15]
        cp = next(I ** k for k in range(4)
                  if zero((I ** k * vol) ** 2 - s.eye(4)) and zero((I ** k * vol).conjugate().T - I ** k * vol))
        self.chirality_phase = cp
        self.F = {(1 << j, 1 << j): s.S.One for j in range(4)}
        self.B = {(m, m): s.S.One for m in FORMS[2]}
        self.Fp = self.right_c(self.F)
        self.Bp = add((I, self.right_c(self.B)))
        self.bases = {k: [(f, c) for f in FORMS[k] for c in range(16)] for k in range(5)}
        self.indices = {k: {key: j for j, key in enumerate(base)} for k, base in self.bases.items()}
        self.Pi = s.diag(*(self.phase[c] for f, c in self.bases[1]))
        self.G1 = self.gram(1)
        self.G3 = self.gram(3)
        self.star1 = self.matrix(lambda x: self.star(x), 1, 3)
        self.H = self.star1.T * self.G3 * self.star1
        assert self.H == (-1) ** q * self.G1

    def right_c(self, x):
        return {(f, c ^ 15): clean(v * self.chirality_phase * self.mul[c, 15]) for (f, c), v in x.items()}

    def star(self, x):
        return {(15 ^ f, c): clean(v * wedge_sign(f, 15 ^ f)
                * prod(self.eta[j] for j in range(4) if f >> j & 1)) for (f, c), v in x.items()}

    def bracket(self, x, y, mode):
        out = {}
        for (f, c), v in x.items():
            for (g, d), w in y.items():
                sign = wedge_sign(f, g)
                if not sign:
                    continue
                z = (self.mul[c, d] - self.mul[d, c]) if mode == "C" else I * (self.mul[c, d] + self.mul[d, c])
                key = (f | g, c ^ d)
                out[key] = clean(out.get(key, 0) + sign * v * w * z)
        return {key: v for key, v in out.items() if v != 0}

    def parts(self, x, f, b, modes):
        sx = self.star(x)
        first = self.bracket(f, sx, modes[0])
        inner = self.bracket(b, sx, modes[1])
        second = add((-s.Rational(1, 2), self.star(self.bracket(f, self.star(inner), modes[2]))))
        return first, second, inner

    def op(self, name, x):
        if name == "E_OP":
            first, cc, _ = self.parts(x, self.F, self.B, "CCC")
            _, aa, _ = self.parts(x, self.F, self.B, "CAA")
            return add((-2, first), (-1, cc), (1, aa))
        f, b = (add((1, self.F), (1, self.Fp)), self.Bp) if name == "CAC" else (self.F, self.B)
        first, second, _ = self.parts(x, f, b, name)
        return add((1, first), (1, second))

    def vector(self, x, degree, phased=True):
        out = s.zeros(len(self.bases[degree]), 1)
        for (f, c), v in x.items():
            out[self.indices[degree][f, c]] = clean(v / self.phase[c]) if phased else v
        return out

    def matrix(self, fn, src, dst):
        return s.Matrix.hstack(*(self.vector(fn({(f, c): self.phase[c]}), dst) for f, c in self.bases[src]))

    def gram(self, degree):
        return s.diag(*(clean(prod(self.eta[j] for j in range(4) if f >> j & 1)
                        * self.phase[c] ** 2 * self.mul[c, c]) for f, c in self.bases[degree]))

    def wedge_k(self, k, x):
        out = {}
        for a, coeff in enumerate(k):
            for (f, c), v in x.items():
                sign = wedge_sign(1 << a, f)
                if sign and coeff:
                    key = (f | (1 << a), c)
                    out[key] = clean(out.get(key, 0) + coeff * sign * v)
        return {key: v for key, v in out.items() if v != 0}

    def symbols(self, name):
        return [self.star1.inv() * self.matrix(lambda x, k=k: self.op(name, self.wedge_k(k, x)), 1, 3)
                for k in s.eye(4).columnspace()]

    def rho(self, degree, a, b):
        jab = (1 << a) | (1 << b)
        L = s.zeros(4)
        for c in range(4):
            target = jab ^ (1 << c)
            coefficient = (self.mul[jab, 1 << c] - self.mul[1 << c, jab]) / 2
            if coefficient:
                L[target.bit_length() - 1, c] = coefficient
        lam = -L.T
        out = s.zeros(len(self.bases[degree]))
        for col, (f, c) in enumerate(self.bases[degree]):
            dst = c ^ jab
            z = (self.mul[jab, c] - self.mul[c, jab]) / 2
            if z:
                out[self.indices[degree][f, dst], col] += clean(z * self.phase[c] / self.phase[dst])
            js = [j for j in range(4) if f >> j & 1]
            for at, old in enumerate(js):
                for new in range(4):
                    if not lam[new, old]:
                        continue
                    seq = js[:at] + [new] + js[at + 1:]
                    if len(set(seq)) < len(seq):
                        continue
                    sign = (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))
                    mask = sum(1 << j for j in seq)
                    out[self.indices[degree][mask, c], col] += sign * lam[new, old]
        return out, lam

    def curvature(self, r):
        return {(f, c): r[i, j] * s.Rational(1, 2)
                * prod(self.eta[a] for a in range(4) if c >> a & 1)
                for i, f in enumerate(FORMS[2]) for j, c in enumerate(FORMS[2]) if r[i, j]}

    def embedding(self, h, prime=False):
        x = {(1 << a, 1 << b): h[a, b] * self.eta[b] for a in range(4) for b in range(4) if h[a, b]}
        return self.right_c(x) if prime else x


def hessian(n, h):
    return 2 * n.T * h * n, 2 * I * (h * n - n.T * h), 2 * h


def nested(n, alg, k):
    s0, s1, _ = hessian(n, alg.H)
    v = kernel(s0)
    va = kernel(n)
    exact = s.kronecker_product(s.Matrix(k), s.eye(16))
    controls = {"exact_rank": rank(exact) == 16, "exact_in_ker_A": zero(n * exact),
                "ker_A_in_ker_S0": zero(s0 * va), "nullity_S0_at_least_exact": v.cols >= 16}
    assert all(controls.values())
    return {"dim_exact_directions": 16, "dim_ker_A": va.cols, "dim_ker_S0": v.cols,
            "quotient_kerA_over_exact": va.cols - 16, "quotient_kerS0_over_kerA": v.cols - va.cols,
            "G1_restricted_inertia": inertia(v.T * alg.G1 * v),
            "S1_restricted_inertia": inertia(v.T * s1 * v), "controls": controls}


def q2(alg, name):
    pairs = FORMS[2]
    xmap = s.Matrix.hstack(*(alg.vector(alg.op(name, alg.curvature(s.eye(36)[:, j].reshape(6, 6))), 3) for j in range(36)))
    tau = s.zeros(36)
    for a in range(6):
        for b in range(6):
            tau[6 * b + a, 6 * a + b] = 1
    eps = s.Matrix([wedge_sign(a, b) if a | b == 15 else 0 for a in pairs for b in pairs])
    p1 = eps * eps.T / 6
    p15 = (s.eye(36) - tau) / 2
    p20 = (s.eye(36) + tau) / 2 - p1
    assert [rank(m) for m in (p1, p15, p20)] == [1, 15, 20]
    assert p1 + p15 + p20 == s.eye(36)
    assert all(m * m == m for m in (p1, p15, p20))
    assert all(a * b == s.zeros(36) for a, b in combinations((p1, p15, p20), 2))
    spaces = []
    for symmetric in (True, False):
        cols = []
        for a in range(4):
            for b in range(a if symmetric else a + 1, 4):
                h = s.zeros(4)
                h[a, b] = 1
                h[b, a] = 1 if symmetric else -1
                for prime in (False, True):
                    cols.append(alg.star1 * alg.vector(alg.embedding(h, prime), 1))
        spaces.append(s.Matrix.hstack(*cols))
    e, ea = spaces
    image = xmap * p15
    r = rank(image)
    dims = [r + rank(space) - rank(image.row_join(space)) for space in spaces]
    bg = s.Matrix.hstack(alg.vector(alg.F, 1), alg.vector(alg.Fp, 1))
    # * on 3-forms equals inverse star on 1-forms for odd q.
    star3 = alg.matrix(alg.star, 3, 1)
    one = star3 * xmap * eps
    coeff = bg.gauss_jordan_solve(one)[0]
    controls = {"dims_E_Ea": [rank(e), rank(ea), rank(e.row_join(ea))],
                "intersections_sum_to_rank": sum(dims) == r,
                "schur_15_in_E_plus_Ea": rank(e.row_join(ea).row_join(image)) == rank(e.row_join(ea)),
                "schur_1_in_span_g": zero(bg * coeff - one)}
    out = {"rank_15": r, "dim_15_in_E": dims[0], "dim_15_in_Ea": dims[1],
           "one_part": {"coefficients_EF_g_EFprime_g": [str(v) for v in coeff], "rank": rank(one)},
           "controls": controls}
    if name == "CCC":
        inner = s.Matrix.hstack(*(alg.vector(alg.parts(alg.curvature(s.eye(36)[:, j].reshape(6, 6)),
                                alg.F, alg.B, "CCC")[2], 4) for j in range(36)))
        out["ccc_inner_rank_15"] = rank(inner * p15)
        controls["ccc_inner_zero_on_20_and_1"] = zero(inner * p20) and zero(inner * p1)
    # Fit and verify all algebraic curvature columns, independently of recorded responses.
    rhs, columns = [], [[], [], [], []]
    def rslot(r, a, b, c, d):
        if a == b or c == d:
            return 0
        return (1 if a < b else -1) * (1 if c < d else -1) * r[pairs.index((1 << a) | (1 << b)), pairs.index((1 << c) | (1 << d))]
    for j in range(36):
        rmat = p20[:, j].reshape(6, 6)
        ric = s.Matrix(4, 4, lambda b, d: sum(alg.eta[a] * rslot(rmat, a, b, a, d) for a in range(4)))
        scalar = sum(alg.eta[a] * ric[a, a] for a in range(4))
        tensors = [alg.embedding(ric), alg.embedding(ric, True),
                   add((scalar, alg.F)), add((scalar, alg.Fp))]
        rhs.extend(star3 * xmap * p20[:, j])
        for idx, tensor in enumerate(tensors):
            columns[idx].extend(alg.vector(tensor, 1))
    fit = s.Matrix.hstack(*(s.Matrix(col) for col in columns))
    response = fit.gauss_jordan_solve(s.Matrix(rhs))[0]
    return out, [str(x) for x in response]


def spectrum(n, alg):
    factors = s.factor_list(n.charpoly(nu).as_expr())[1]
    records = []
    nilpotent = 0
    for polynomial, exponent in factors:
        if polynomial == nu:
            nilpotent = exponent
            continue
        print("PROGRESS factor", polynomial, exponent, flush=True)
        # One exact representative suffices for ranks over the irreducible Q factor.
        roots = s.Poly(polynomial, nu).all_roots(radicals=True)
        root = roots[0]
        field = s.QQ.algebraic_field(root)
        z = -1 / root
        u = s.eye(64) + z * n
        um = s.eye(64) - z * n
        m = 2 * um.T * alg.H * u
        vu, vm = kernel(u, field), kernel(m, field)
        assert zero(m * vu)
        # Jordan block lengths from successive exact nullities.
        b = dm(n - root * s.eye(64), field)
        power = b
        nullities = [0]
        while True:
            nullity = 64 - len(power.rref()[1])
            nullities.append(nullity)
            if nullity == exponent:
                break
            assert len(nullities) <= exponent + 1
            power = power * b
        at_least = [nullities[j] - nullities[j - 1] for j in range(1, len(nullities))]
        partial = sorted([j + 1 for j, count in enumerate(at_least)
                          for _ in range(count - (at_least[j + 1] if j + 1 < len(at_least) else 0))])
        ws = [s.simplify(-1 / r ** 2) for r in roots]
        real_root = all(w.is_positive for w in ws)
        q3 = {"factor": str(polynomial), "field_degree": s.degree(polynomial, nu),
              "dim_ker_U": vu.cols, "dim_ker_M": vm.cols,
              "multiplicity_det_U": exponent, "multiplicity_det_M": 2 * exponent,
              "control_ker_U_in_ker_M": True, "kernel_gap": vm.cols - vu.cols,
              "kernel_gap_reading": "hermitian_radical" if real_root else "cross_annihilator",
              "partial_multiplicities_U": partial, "partial_multiplicities_M": "not computed",
              "semisimple_U": vu.cols == exponent, "semisimple_M": vm.cols == 2 * exponent}
        rec = {"factor": str(polynomial), "degree": int(s.degree(polynomial, nu)), "exponent": exponent,
               "massive_type": [str(w) for w in ws if w.is_positive],
               "tachyonic_type": [str(w) for w in ws if w.is_negative],
               "non_real": sum(w.is_real is False for w in ws),
               "rational_massive": [str(w) for w in ws if w.is_positive and w.is_Rational], "Q3": q3}
        q4 = []
        for d in sorted(set(w for w in ws if w.is_positive and w.is_Rational)):
            for sign in (1, -1):
                z0 = sign * I * s.sqrt(d)
                field4 = s.QQ.algebraic_field(z0)
                u0 = s.eye(64) + z0 * n
                m0 = 2 * (s.eye(64) - z0 * n).T * alg.H * u0
                v_u, v_m = kernel(u0, field4), kernel(m0, field4)
                s0, s1, _ = hessian(n, alg.H)
                # |omega| M'(omega), at both signed roots.
                derivative = sign * (2 * d * s0 + z0 * s1 / I)
                derivative_u_zero = zero(v_u.conjugate().T * derivative * v_u)
                qu = v_u.conjugate().T * n.T * alg.H * n * v_u
                quarter = v_u.conjugate().T * s0 * v_u / 2
                din = inertia(v_m.conjugate().T * derivative * v_m)
                qin = inertia(qu)
                q4.append({"w0": ("" if sign == 1 else "-") + "sqrt(" + str(d) + ")",
                           "w0_squared": str(d), "dim_ker_U": v_u.cols, "dim_ker_M": v_m.cols,
                           "multiplicity_det_U": exponent, "multiplicity_det_M": 2 * exponent,
                           "kernel_gap_hermitian_radical": v_m.cols - v_u.cols,
                           "semisimple_U": v_u.cols == exponent, "semisimple_M": v_m.cols == 2 * exponent,
                           "control_ker_U_in_ker_M": zero(m0 * v_u),
                           "control_derivative_form_zero_on_ker_U": derivative_u_zero,
                           "control_QU_quarter_second_derivative": zero(qu - quarter),
                           "derivative_form_rank": sum(din[:2]), "derivative_form_inertia": din,
                           "second_order_form_rank": sum(qin[:2]), "second_order_form_inertia": qin})
        rec["Q4"] = q4
        rec["Q4_status"] = "computed" if q4 else ("requires_algebraic_extension" if real_root else "not_applicable")
        records.append(rec)
    return {"degree": 64, "nilpotent_multiplicity": nilpotent, "factors": records}


def operator(alg, name):
    print("PROGRESS operator", alg.p, alg.q, name, flush=True)
    ns = alg.symbols(name)
    assert all(x.is_Rational for n in ns for x in n)
    hs = [hessian(n, alg.H) for n in ns]
    # C1 in raw coordinates: raw t^T (G1_raw N_raw + transpose) a.
    c1 = [alg.Pi.inv().T * (alg.G1 * n + n.T * alg.G1) * alg.Pi.inv() for n in ns]
    q1 = {"S1_identically_zero": all(zero(h[1]) for h in hs),
          "S1_rank_at_e_m": [rank(h[1]) for h in hs],
          "c1_nonzero": sum(c[i, j] != 0 for c in c1 for i in range(64) for j in range(i, 64)),
          "grade_pairs_coupled": [list(t) for t in sorted({(alg.bases[1][i][1].bit_count(), alg.bases[1][j][1].bit_count())
                                 for h in hs for i in range(64) for j in range(64) if h[1][i, j] != 0})],
          "repaired_term2_nonzero_at_e0": not zero(ns[0].T * alg.H),
          "derived_term3_nonzero_at_e0": not zero(alg.H * ns[0])}
    cov = {k: True for k in ("A_intertwines", "hessian_covariant", "pairing_invariant", "star_intertwines", "traceless")}
    for a, b in combinations(range(4), 2):
        r1, lam = alg.rho(1, a, b)
        r3, _ = alg.rho(3, a, b)
        cov["traceless"] &= s.trace(r1) == 0 and s.trace(r3) == 0
        cov["pairing_invariant"] &= zero(r1.T * alg.G1 + alg.G1 * r1) and zero(r3.T * alg.G3 + alg.G3 * r3)
        cov["star_intertwines"] &= zero(r3 * alg.star1 - alg.star1 * r1)
        for j, n in enumerate(ns):
            dn = sum((lam[i, j] * ns[i] for i in range(4)), s.zeros(64))
            cov["A_intertwines"] &= zero(r1 * n - n * r1 - dn)
            s0, s1, s2 = hs[j]
            ds0 = 2 * (dn.T * alg.H * n + n.T * alg.H * dn)
            ds1 = 2 * I * (alg.H * dn - dn.T * alg.H)
            cov["hessian_covariant"] &= all(zero(r1.T * h + h * r1 + dh) for h, dh in ((s0, ds0), (s1, ds1), (s2, s.zeros(64))))
    cov["covariance_verified"] = all(cov.values())
    assert cov["covariance_verified"]
    qtwo, response = q2(alg, name)
    ti, si = (3, 0) if alg.p == 3 else (0, 1)
    rays = {"timelike": s.eye(4)[:, ti], "spacelike": s.eye(4)[:, si], "null": s.eye(4)[:, ti] + s.eye(4)[:, si]}
    nested_results = {}
    for ray, k in rays.items():
        n = sum((k[i] * ns[i] for i in range(4)), s.zeros(64))
        nested_results[ray] = nested(n, alg, k)
    spec = spectrum(ns[ti], alg)
    return {"operator": name, "response": response, "Q1": q1, "Q2": qtwo,
            "Q3_Q4": {"covariance": cov, "kernel_S0_null": nested_results["null"],
                      "kernel_S0_spacelike": nested_results["spacelike"],
                      "rank_S0_kappa0": {k: 64 - v["dim_ker_S0"] for k, v in nested_results.items()},
                      "timelike": {"charpoly": spec, "kernel_S0": nested_results["timelike"],
                                   "rank_S0_kappa0": 64 - nested_results["timelike"]["dim_ker_S0"]}}}


def compare(actual, expected, path, rows):
    if isinstance(actual, dict) and isinstance(expected, dict):
        for key in sorted(set(actual) | set(expected)):
            if key not in actual:
                rows.append([path + "." + key, "not reconstructed", expected[key], "not reconstructed"])
            elif key not in expected:
                rows.append([path + "." + key, actual[key], "not recorded", "additional"])
            else:
                compare(actual[key], expected[key], path + "." + key, rows)
    elif isinstance(actual, list) and isinstance(expected, list) and actual and isinstance(actual[0], dict):
        key = "factor" if "factor" in actual[0] else ("w0" if "w0" in actual[0] else None)
        if key:
            aa, ee = {x[key]: x for x in actual}, {x[key]: x for x in expected}
            compare(aa, ee, path, rows)
        else:
            for j in range(max(len(actual), len(expected))):
                compare(actual[j] if j < len(actual) else None, expected[j] if j < len(expected) else None, path + "[" + str(j) + "]", rows)
    else:
        rows.append([path, actual, expected, "agree" if actual == expected else "DISAGREE"])


def main():
    # Hand checks for this independent elimination, including non-square d.
    assert inertia(s.Matrix([[0, I], [-I, 0]])) == [1, 1, 0]
    assert inertia(s.Matrix([[1, I * s.sqrt(2)], [-I * s.sqrt(2), 2]])) == [1, 0, 1]
    computed = []
    for p, q in ((3, 1), (1, 3)):
        alg = Algebra(p, q)
        computed.append({"signature": [p, q], "operators": [operator(alg, name) for name in ("CCC", "CAA", "CAC", "E_OP")]})
    # This is deliberately the first access to comparison data.
    reference = json.loads(Path("experiments/B07/optionc/result.json").read_text(encoding="utf-8"))
    rows = []
    compare({"signatures": computed}, reference, "result", rows)
    def encode(value):
        if isinstance(value, s.Integer):
            return int(value)
        if isinstance(value, s.Basic):
            return str(value)
        raise TypeError(type(value).__name__)
    print("COMPUTED_JSON " + json.dumps(computed, default=encode), flush=True)
    print("COMPARISON_JSON " + json.dumps(rows, default=encode), flush=True)
    counts = {label: sum(row[3] == label for row in rows) for label in ("agree", "DISAGREE", "additional", "not reconstructed")}
    print("SUMMARY_JSON " + json.dumps(counts), flush=True)


if __name__ == "__main__":
    main()

