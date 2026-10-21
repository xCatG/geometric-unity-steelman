"""B07 option C, Q3/Q4: dispersion roots and sign data of the linearized system (design rev 3.1, §4 Q3-Q4).

On a ray k = w u (kappa = 1): det U(w u) = det(*) det(i w N(u) + 1), so the roots are w = i/nu over the nonzero
eigenvalues nu of the rational matrix N(u); w^2 = -1/nu^2. The characteristic polynomial chi(nu) of N(u) is exact
(python-flint) and factored over Q. Each irreducible factor f != nu is classified by the roots of
    h(w2) = numerator of Res_nu(f(nu), nu^2 - s) at s = -1/w2      (one root w2 = w^2 per root nu of f),
as real positive (massive-type, 3c), real negative (tachyonic-type, 3e1) or non-real (3e2), exactly (sympy real roots).
For a rational root w^2 = d > 0 (factor nu^2 + 1/d), kernels and forms live over Q(theta), theta = sqrt(-d). They are
computed on the realification x + theta y -> (x, y): an operator A + theta B acts by [[A, -dB], [B, A]], a Hermitian
form A + theta B (A symmetric, B antisymmetric) has real form [[A, -dB], [dB, dA]], and real inertias are doubled.
Q3 kernel data at every root (any irreducible factor f, degree m) are computed over K = Q[nu]/f through the regular
representation (nu -> the companion matrix of f): a K-matrix sum_j B_j nu^j acts on Q^(64 m) as sum_j B_j (x) C^j, and
K-dimensions are Q-dimensions / m. They hold for every root of f (Galois conjugates).
"""
from __future__ import annotations

from fractions import Fraction

import sympy as sp
from flint import fmpq, fmpq_mat

from gu.inertia import inertia
from experiments.B07.optionc.sector import entries, fq, is_zero, mat

NU, S_, W2 = sp.symbols("nu s w2")


class ConsistencyFailure(AssertionError):
    """An internal consistency control of the spectral backend failed: a hard gate, recorded as failed_control."""


def nullspace(M: fmpq_mat) -> fmpq_mat:
    """Exact rational nullspace basis, as the columns of a matrix (ncols x dim)."""
    R, rank = M.rref()
    n = M.ncols()
    pivots, r = [], 0
    for c in range(n):
        if r < rank and R[r, c] != 0:
            pivots.append(c)
            r += 1
    free = [c for c in range(n) if c not in set(pivots)]
    K = fmpq_mat(n, max(len(free), 1))
    for j, fc in enumerate(free):
        K[fc, j] = 1
        for i, pc in enumerate(pivots):
            K[pc, j] = -R[i, fc]
    return K if free else fmpq_mat(n, 0)


def dim_kernel(M: fmpq_mat) -> int:
    return M.ncols() - M.rank()


def block(rows: list[list[fmpq_mat]]) -> fmpq_mat:
    """Block matrix from equal-size square blocks."""
    n = rows[0][0].nrows()
    out = fmpq_mat(n * len(rows), n * len(rows[0]))
    for bi, r in enumerate(rows):
        for bj, B in enumerate(r):
            for i in range(n):
                for j in range(n):
                    if B[i, j] != 0:
                        out[bi * n + i, bj * n + j] = B[i, j]
    return out


def ident(n: int) -> fmpq_mat:
    I = fmpq_mat(n, n)
    for i in range(n):
        I[i, i] = 1
    return I


def sym_inertia(Q: fmpq_mat) -> tuple[int, int, int]:
    return inertia(sp.Matrix([[sp.Rational(int(Q[i, j].p), int(Q[i, j].q)) for j in range(Q.ncols())]
                              for i in range(Q.nrows())]))


def restricted_inertia(Q: fmpq_mat, K: fmpq_mat, halve: bool) -> list[int] | None:
    if K.ncols() == 0:
        return [0, 0, 0]
    t = sym_inertia(K.transpose() * Q * K)
    if halve:
        if any(x % 2 for x in t):
            raise ConsistencyFailure(f"realified inertia not even: {t}")
        t = tuple(x // 2 for x in t)
    return list(t)


def charpoly_factors(N: fmpq_mat) -> dict:
    """chi(nu) of N, factored over Q: the nilpotent multiplicity and the other irreducible factors."""
    chi = N.charpoly()
    _, facs = chi.factor()
    out = {"degree": chi.degree(), "nilpotent_multiplicity": 0, "factors": []}
    for f, e in facs:
        c = [Fraction(int(x.p), int(x.q)) for x in f.coeffs()]
        if c == [0, 1]:
            out["nilpotent_multiplicity"] = int(e)
        else:
            out["factors"].append({"coeffs": c, "exponent": int(e)})
    return out


def classify_factor(coeffs: list[Fraction]) -> dict:
    """Roots w^2 = -1/nu^2 for the roots nu of one irreducible factor (kappa = 1), exactly."""
    f = sp.Poly(sum(sp.Rational(c.numerator, c.denominator) * NU ** i for i, c in enumerate(coeffs)), NU)
    g = sp.Poly(sp.resultant(f.as_expr(), NU ** 2 - S_, NU), S_)
    h = sp.Poly(sp.numer(sp.together(g.as_expr().subs(S_, -1 / W2))), W2)
    real = sp.real_roots(h)
    pos = [r for r in real if r > 0]
    neg = [r for r in real if r < 0]
    if any(r == 0 for r in real):
        raise ConsistencyFailure("w^2 = 0 root: impossible for kappa != 0 (control 9)")
    return {"factor": str(f.as_expr()), "degree": f.degree(),
            "massive_type": [str(r) for r in pos], "tachyonic_type": [str(r) for r in neg],
            "non_real": h.degree() - len(real),
            "rational_massive": [str(r) for r in pos if r.is_Rational]}


def form_realified(A: fmpq_mat, B: fmpq_mat, dq: fmpq) -> fmpq_mat:
    """Real symmetric form of the Hermitian form A + theta B over Q(theta), theta^2 = -d (A symmetric, B antisymmetric)."""
    return block([[A, -B * dq], [B * dq, A * dq]])


def op_realified(A: fmpq_mat, B: fmpq_mat, dq: fmpq) -> fmpq_mat:
    """Real matrix of the operator A + theta B over Q(theta), theta^2 = -d."""
    return block([[A, -B * dq], [B, A]])


def hermitian_inertia(A: fmpq_mat, B: fmpq_mat, d: Fraction, K: fmpq_mat | None = None) -> list[int]:
    """Inertia of A + theta B (restricted to the realified subspace K, default everything), halved."""
    Q = form_realified(A, B, fq(d))
    return restricted_inertia(Q, K if K is not None else ident(Q.nrows()), True)


def root_data(N: fmpq_mat, S0: fmpq_mat, R1: fmpq_mat, S2: fmpq_mat, AtGA: fmpq_mat, d: Fraction,
              exponent: int, S0_check: fmpq_mat | None = None) -> list[dict]:
    """Q3 (ii) and Q4 (i)-(ii) at the real roots w0 = +-sqrt(d) (d > 0 rational, factor nu^2 + 1/d with `exponent`).
    S0_check: S0(u) from an independent path (fourier_terms) for the check Q_U = (1/4) V^dag M'' V = (1/2) V^dag S0 V."""
    n, dq = N.nrows(), fq(d)
    I = ident(n)
    geom_U = dim_kernel(N * N + I * fq(1 / d))
    if geom_U % 2:
        raise ConsistencyFailure("ker(N^2 + 1/d) has odd dimension")
    geom_U //= 2
    out = []
    for sgn in (1, -1):
        A_M, B_M = S0 * dq + S2, R1 * sgn
        KM = nullspace(block([[A_M, -B_M * dq], [B_M, A_M]]))
        KU = nullspace(block([[N, I * sgn], [-I * fq(Fraction(sgn) / d), N]]))
        if KM.ncols() % 2 or KU.ncols() % 2 or KU.ncols() // 2 != geom_U:
            raise ConsistencyFailure("realified kernel dimension inconsistent")
        A_H, B_H = S0 * fq(2 * sgn * d), R1
        QH = form_realified(A_H, B_H, dq)
        QU = form_realified(AtGA, AtGA * 0, dq)
        both = fmpq_mat(KM.nrows(), KM.ncols() + KU.ncols())
        for i in range(KM.nrows()):
            for j in range(KM.ncols()):
                both[i, j] = KM[i, j]
            for j in range(KU.ncols()):
                both[i, KM.ncols() + j] = KU[i, j]
        dim_M = KM.ncols() // 2
        deriv = restricted_inertia(QH, KM, True)
        second = restricted_inertia(QU, KU, True)
        rec = {"w0": f"{'' if sgn > 0 else '-'}sqrt({d})", "w0_squared": str(d),
               "multiplicity_det_U": exponent, "dim_ker_U": geom_U, "dim_ker_M": dim_M,
               "kernel_gap_hermitian_radical": dim_M - geom_U, "multiplicity_det_M": 2 * exponent,
               "semisimple_U": geom_U == exponent, "semisimple_M": dim_M == 2 * exponent,
               "derivative_form_inertia": deriv, "derivative_form_rank": deriv[0] + deriv[1],
               "second_order_form_inertia": second, "second_order_form_rank": second[0] + second[1],
               "control_ker_U_in_ker_M": both.rank() == KM.rank(),
               "control_derivative_form_zero_on_ker_U": is_zero(KU.transpose() * QH * KU)}
        if S0_check is not None:
            half = S0_check * fmpq(1, 2)
            rec["control_QU_quarter_second_derivative"] =                 KU.transpose() * QU * KU == KU.transpose() * form_realified(half, half * 0, dq) * KU
        if rec["semisimple_M"] and deriv[2]:
            raise ConsistencyFailure("zero direction in the derivative form at a root certified semisimple")
        out.append(rec)
    return out


def kernel_s0_data(S0: fmpq_mat, R1: fmpq_mat, G1: fmpq_mat, L: fmpq_mat, A: fmpq_mat, exact_dim: int = 16) -> dict:
    """Q3 (iii) nested kernels {u (x) lambda} <= ker A(u) <= ker S0(u), and Q4 (iii) restricted forms on ker S0(u).
    `controls` (hard gates in the runner): rank L = exact_dim, A L = 0, S0 ker A = 0, nullity S0 >= exact_dim."""
    KA = nullspace(A)
    ctrl = {"exact_rank": L.rank() == exact_dim, "exact_in_ker_A": is_zero(A * L),
            "ker_A_in_ker_S0": is_zero(S0 * KA) if KA.ncols() else True, "nullity_S0_at_least_exact": dim_kernel(S0) >= exact_dim}
    if not all(ctrl.values()):
        return {"controls": ctrl}
    V0 = nullspace(S0)
    r1 = V0.transpose() * R1 * V0
    herm = sp.Matrix([[sp.I * sp.Rational(int(r1[i, j].p), int(r1[i, j].q)) for j in range(r1.ncols())]
                      for i in range(r1.nrows())]) if V0.ncols() else sp.zeros(0, 0)
    return {"controls": ctrl, "dim_exact_directions": L.rank(),
            "dim_ker_A": dim_kernel(A), "dim_ker_S0": V0.ncols(),
            "quotient_kerA_over_exact": dim_kernel(A) - L.rank(), "quotient_kerS0_over_kerA": V0.ncols() - dim_kernel(A),
            "S1_restricted_inertia": list(inertia(herm)) if V0.ncols() else [0, 0, 0],
            "G1_restricted_inertia": restricted_inertia(G1, V0, False)}


def spacelike_relation(chi_t: list[Fraction], chi_s: list[Fraction]) -> bool:
    """Covariance consequence chi_s(i y) = chi_t(y): odd coefficients vanish and c_t[j] = (-1)^(j/2) c_s[j]."""
    if len(chi_t) != len(chi_s):
        return False
    for j, (ct, cs) in enumerate(zip(chi_t, chi_s)):
        if j % 2 and (ct or cs):
            return False
        if not j % 2 and ct != (-1) ** (j // 2) * cs:
            return False
    return True


def coeffs(N: fmpq_mat) -> list[Fraction]:
    return [Fraction(int(x.p), int(x.q)) for x in N.charpoly().coeffs()]


# ---- Q3 (ii) at every root: exact kernels over K = Q[nu]/f ----
def companion(c: list[Fraction]) -> fmpq_mat:
    """Multiplication by nu on Q[nu]/f in the basis 1, nu, ..., nu^(m-1) (c: coefficients of f, low to high)."""
    c = [Fraction(x) / Fraction(c[-1]) for x in c]
    m = len(c) - 1
    C = fmpq_mat(m, m)
    for j in range(m - 1):
        C[j + 1, j] = 1
    for i in range(m):
        C[i, m - 1] = fq(-c[i])
    return C


def over_field(terms: list[fmpq_mat], C: fmpq_mat) -> fmpq_mat:
    """The K-matrix sum_j terms[j] nu^j as a rational matrix on Q^(rows m) (regular representation)."""
    r, s, m = terms[0].nrows(), terms[0].ncols(), C.nrows()
    pw = [ident(m)]
    for _ in terms[1:]:
        pw.append(pw[-1] * C)
    out = fmpq_mat(r * m, s * m)
    for B, P in zip(terms, pw):
        Pn = [(a, e, P[a, e]) for a in range(m) for e in range(m) if P[a, e] != 0]
        for i in range(r):
            for j in range(s):
                b = B[i, j]
                if b != 0:
                    for a, e, v in Pn:
                        out[i * m + a, j * m + e] = out[i * m + a, j * m + e] + b * v
    return out


def factor_root_data(N: fmpq_mat, S0: fmpq_mat, R1: fmpq_mat, S2: fmpq_mat, cls: dict, coeffs: list[Fraction],
                     exponent: int) -> dict:
    """Q3 (ii) at the roots w0 = i/nu of one irreducible factor f (kappa = 1): U(w0) = -(S/nu)(N - nu), so
    ker U = ker(N - nu); nu^2 M(w0) = -S0 - nu R1 + nu^2 S2. Partial multiplicities of U are the Jordan block sizes of
    N at nu; those of M are recorded only when M is semisimple there ("not computed" otherwise).
    Precondition for multiplicity_det_M = 2 * exponent: u = det U is even (the caller gates it), so the roots i/nu and
    -i/nu of u(w) u(-w) have equal multiplicity."""
    n, m = N.nrows(), len(coeffs) - 1
    C, I = companion(coeffs), ident(n)
    Ub, Mb = over_field([N, I * -1], C), over_field([S0 * -1, R1 * -1, S2], C)
    dims = [dim_kernel(Ub), dim_kernel(Mb)]
    ranks, P = [n * m], Ub
    for j in range(exponent):
        if j:
            P = P * Ub
        ranks.append(P.rank())
    if any(x % m for x in dims + ranks):
        raise ConsistencyFailure("K-dimension not a multiple of [K:Q]")
    dU, dM = dims[0] // m, dims[1] // m
    ranks = [x // m for x in ranks]
    if n - ranks[-1] != exponent:
        raise ConsistencyFailure("generalized eigenspace dimension != exponent in chi")
    ge = [ranks[j - 1] - ranks[j] for j in range(1, exponent + 1)] + [0]     # number of blocks of size >= j
    partial = sorted((j for j in range(1, exponent + 1) for _ in range(ge[j - 1] - ge[j])), reverse=True)
    KU = nullspace(Ub)
    n_real = len(cls["massive_type"])
    reading = ("hermitian_radical" if n_real == m else "cross_annihilator" if n_real == 0
               else "hermitian_radical at the massive-type roots, cross_annihilator at the others")
    return {"factor": cls["factor"], "field_degree": m, "multiplicity_det_U": exponent,
            "multiplicity_det_M": 2 * exponent, "dim_ker_U": dU, "dim_ker_M": dM, "kernel_gap": dM - dU,
            "kernel_gap_reading": reading, "partial_multiplicities_U": partial, "semisimple_U": dU == exponent,
            "semisimple_M": dM == 2 * exponent,
            "partial_multiplicities_M": [1] * (2 * exponent) if dM == 2 * exponent else "not computed",
            "control_ker_U_in_ker_M": is_zero(Mb * KU) if KU.ncols() else True}


def q4_status(cls: dict, coeffs: list[Fraction]) -> str:
    """Which Q4 (i)-(ii) branch a factor's roots take (design Q4, unsupported cases)."""
    if len(coeffs) == 3 and coeffs[1] == 0 and coeffs[2] == 1 and coeffs[0] > 0:     # nu^2 + 1/d
        return "computed"
    return "requires_algebraic_extension" if cls["massive_type"] else "not_applicable"


# ---- control 4: det M(w) = det(2 G3) u(w) u(-w) on a ray, u = det U from chi(N) (an independent path) ----
def det_values(S0: fmpq_mat, R1: fmpq_mat, S2: fmpq_mat, ts: list[int]) -> list[fmpq]:
    """det M(i t) = det(-t^2 S0 - t R1 + S2) at the sample points (M(w) = w^2 S0 + i w R1 + S2 on the ray)."""
    return [(S0 * -(t * t) - R1 * t + S2).det() for t in ts]


def det_identity(S0: fmpq_mat, R1: fmpq_mat, S2: fmpq_mat, N: fmpq_mat, S: fmpq_mat, G3: fmpq_mat) -> bool:
    """Both sides are polynomials of degree <= 2n in t (w = i t), so agreement at 2n + 1 points is the identity.
    u(i t) = det(S) det(1 - t N) = det(S) sum_j chi_j t^(n - j)."""
    n = N.nrows()
    chi = N.charpoly().coeffs()
    ts = list(range(2 * n + 1))
    lhs = det_values(S0, R1, S2, ts)
    c = (G3 * 2).det() * S.det() ** 2
    u = lambda t: sum((chi[j] * fmpq(t) ** (n - j) for j in range(n + 1)), fmpq(0))
    return all(v == c * u(t) * u(-t) for v, t in zip(lhs, ts))


def ray_label(values: list[fmpq]) -> str:
    """Raw ray diagnostic of det M on a sampled ray (more samples than its degree): zero / constant / nonconstant."""
    if all(v == 0 for v in values):
        return "zero_on_sampled_ray"
    return "constant_on_sampled_ray" if all(v == values[0] for v in values) else "nonconstant_on_sampled_ray"


def interpolate(ts: list[int], vals: list[fmpq]) -> list[Fraction]:
    """Exact Newton interpolation; coefficients low to high, trailing zeros dropped."""
    xs, c = [Fraction(t) for t in ts], [Fraction(int(v.p), int(v.q)) for v in vals]
    for j in range(1, len(xs)):
        for i in range(len(xs) - 1, j - 1, -1):
            c[i] = (c[i] - c[i - 1]) / (xs[i] - xs[i - j])
    poly = [Fraction(0)] * len(xs)
    for i in range(len(xs) - 1, -1, -1):          # Horner on the Newton form: poly = poly * (x - xs[i]) + c[i]
        new = [Fraction(0)] * len(xs)
        for k, a in enumerate(poly[:-1]):
            new[k + 1] += a
            new[k] -= a * xs[i]
        new[0] += c[i]
        poly = new
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


# ---- control 7: backend toys with pinned answers (a hard gate, run before any named operator) ----
def gram_toy(G: list[int]):
    """U(w) = C + i w A_U with C = diag(1, -1), A_U = [[0, 1], [1, 0]] (roots w = +-1), Gram G."""
    C, AU, Gm = mat([[1, 0], [0, -1]]), mat([[0, 1], [1, 0]]), mat([[G[0], 0], [0, G[1]]])
    N = C.inv() * AU
    S0 = 2 * AU.transpose() * Gm * AU
    R1 = 2 * (C.transpose() * Gm * AU - AU.transpose() * Gm * C)
    S2 = 2 * C.transpose() * Gm * C
    return N, S0, R1, S2, AU.transpose() * Gm * AU


def first_order_toy(N: list[list], G: list[int]):
    """S = I, A = N, Gram diag(G): (N, S0, R1, S2, A^T G A)."""
    Nm, Gm = mat(N), mat([[G[i] if i == j else 0 for j in range(len(G))] for i in range(len(G))])
    return (Nm, 2 * Nm.transpose() * Gm * Nm, 2 * (Gm * Nm - Nm.transpose() * Gm), 2 * Gm,
            Nm.transpose() * Gm * Nm)


def backend_controls() -> dict:
    """Control 7. Every entry compares with a hand answer pinned here; all must be True."""
    out = {}
    one, zero, ts, ts9 = mat([[1]]), mat([[0]]), list(range(5)), list(range(9))
    # scalar waves on a ray (1 x 1, M(w) = w^2 S0 + i w R1 + S2): massless timelike w^2, massless null 0, massive w^2 - 4
    out["scalar_massless_timelike"] = interpolate(ts, det_values(one, zero, zero, ts)) == [0, 0, -1]
    out["scalar_massless_null_zero_polynomial"] = ray_label(det_values(zero, zero, zero, ts)) == "zero_on_sampled_ray"
    out["scalar_massive"] = interpolate(ts, det_values(one, zero, mat([[-4]]), ts)) == [-4, 0, -1]
    # singular leading coefficient: S0 = diag(1, 0), S2 = -I, so det M(i t) = t^2 + 1, degree 2 < 4
    out["singular_leading_degree_deficit"] = interpolate(ts9, det_values(
        mat([[1, 0], [0, 0]]), mat([[0, 0], [0, 0]]), mat([[-1, 0], [0, -1]]), ts9)) == [1, 0, 1]
    # classification and the nilpotent degree deficit (algebraic, not geometric, multiplicity of 0)
    out["classify_massive"] = classify_factor([Fraction(4), 0, 1])["massive_type"] == ["1/4", "1/4"]
    out["classify_tachyonic"] = classify_factor([Fraction(-4), 0, 1])["tachyonic_type"] == ["-1/4", "-1/4"]
    out["classify_non_real"] = classify_factor([Fraction(1), 0, 1, 0, 1])["non_real"] == 4
    out["nilpotent_algebraic_multiplicity"] = charpoly_factors(mat([[0, 1], [0, 0]])) == \
        {"degree": 2, "nilpotent_multiplicity": 2, "factors": []}
    # Gram of a square symbol: G = I forces a non-semisimple M root; G = diag(1, -1) gives a neutral derivative form
    for G, want in (([1, 1], (1, 1, False, [0, 0, 1], [1, 0, 0], 0)), ([1, -1], (1, 2, True, [1, 1, 0], [0, 0, 1], 1))):
        recs = root_data(*gram_toy(G), Fraction(1), 1)
        out[f"gram_toy_{G}"] = all((r["dim_ker_U"], r["dim_ker_M"], r["semisimple_M"], r["derivative_form_inertia"],
                                    r["second_order_form_inertia"], r["kernel_gap_hermitian_radical"]) == want
                                   and r["control_ker_U_in_ker_M"] and r["control_derivative_form_zero_on_ker_U"]
                                   for r in recs)
        N_, S0_, R1_, S2_, _ = gram_toy(G)
        f = factor_root_data(N_, S0_, R1_, S2_, classify_factor([Fraction(1), 0, 1]), [Fraction(1), 0, 1], 1)
        out[f"gram_toy_{G}_over_field"] = (f["dim_ker_U"], f["dim_ker_M"]) == want[:2] and f["control_ker_U_in_ker_M"]
    # Jordan chain: N = [[J, I], [0, J]], J = [[0, 1], [-1, 0]]: one block of size 2 at nu = +-i
    t = first_order_toy([[0, 1, 1, 0], [-1, 0, 0, 1], [0, 0, 0, 1], [0, 0, -1, 0]], [1, 1, 1, 1])
    f = factor_root_data(t[0], t[1], t[2], t[3], classify_factor([Fraction(1), 0, 1]), [Fraction(1), 0, 1], 2)
    out["jordan_chain"] = (f["dim_ker_U"], f["partial_multiplicities_U"], f["semisimple_U"]) == (1, [2], False)
    rec = root_data(*t, Fraction(1), 2)[0]
    out["jordan_chain_realified"] = (rec["dim_ker_U"], rec["semisimple_U"]) == (1, False)
    # a real eigenvalue (tachyonic-type root) with an even spectrum: N = diag(2, -2), G = I, factor nu - 2.
    # det M(w) = det(2) (1 + 4 w^2)^2: the root w = i/2 has multiplicity 2; ker U = <e1>, ker M = everything (2-dim),
    # so M is semisimple there with a cross-annihilator gap of 1.
    t = first_order_toy([[2, 0], [0, -2]], [1, 1])
    f = factor_root_data(t[0], t[1], t[2], t[3], classify_factor([Fraction(-2), 1]), [Fraction(-2), 1], 1)
    out["real_eigenvalue_root"] = (f["dim_ker_U"], f["dim_ker_M"], f["multiplicity_det_M"], f["semisimple_M"],
                                   f["kernel_gap"], f["kernel_gap_reading"], f["control_ker_U_in_ker_M"]) == \
        (1, 2, 2, True, 1, "cross_annihilator", True)
    # Q(sqrt(-d)) Hermitian elimination: d = 1 against gu.inertia (imaginary off-diagonals, an off-diagonal pivot, zero
    # directions), a non-square d = 2 by hand, and the conjugation convention through a restriction
    fixtures = [([[1, 0], [0, -1]], [[0, 1], [-1, 0]]), ([[0, 0], [0, 0]], [[0, 1], [-1, 0]]),
                ([[0, 1], [1, 0]], [[0, 1], [-1, 0]]), ([[1, 0], [0, 1]], [[0, 1], [-1, 0]]),
                ([[2, 1, 0], [1, 0, 0], [0, 0, -1]], [[0, 0, 1], [0, 0, 2], [-1, -2, 0]])]
    out["hermitian_d1_vs_gu_inertia"] = all(
        hermitian_inertia(mat(a), mat(b), Fraction(1)) == list(inertia(sp.Matrix(a) + sp.I * sp.Matrix(b)))
        for a, b in fixtures)
    # d = 2: [[1, theta], [-theta, 1]] has det 1 - 2 < 0; [[2, theta], [-theta, 1]] has det 0
    out["hermitian_d2_hand"] = (
        hermitian_inertia(mat([[1, 0], [0, 1]]), mat([[0, 1], [-1, 0]]), Fraction(2)) == [1, 1, 0]
        and hermitian_inertia(mat([[2, 0], [0, 1]]), mat([[0, 1], [-1, 0]]), Fraction(2)) == [1, 0, 1])
    # ker [[1, i], [0, 0]] = span (-i, 1); there H = [[0, i], [-i, 0]] gives conj(v)^T H v = -2 (the other convention, +2)
    K = nullspace(op_realified(mat([[1, 0], [0, 0]]), mat([[0, 1], [0, 0]]), fq(Fraction(1))))
    out["conjugation_convention"] = hermitian_inertia(mat([[0, 0], [0, 0]]), mat([[0, 1], [-1, 0]]), Fraction(1),
                                                      K) == [0, 1, 0]
    # second-order form at non-unit d: N = [[0, -1/2], [1, 0]], G = diag(-4, 3), d = 2: v = (theta/2, 1), Q_U = 1/2;
    # N = [[0, -2], [2, 0]], G = diag(-1, 3), d = 1/4: v = (1, -i), Q_U = 4 (-1 + 3) = 8
    for name, Nt, Gt, d in (("d2", [[0, Fraction(-1, 2)], [1, 0]], [-4, 3], Fraction(2)),
                            ("d1_4", [[0, -2], [2, 0]], [-1, 3], Fraction(1, 4))):
        t = first_order_toy(Nt, Gt)
        recs = root_data(*t, d, 1, S0_check=t[1])
        out[f"second_order_form_{name}"] = all((r["dim_ker_U"], r["second_order_form_inertia"]) == (1, [1, 0, 0])
                                               and r["control_QU_quarter_second_derivative"] for r in recs)
    return out
