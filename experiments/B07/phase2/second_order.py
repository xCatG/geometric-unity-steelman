"""B07 Phase 2, item 2: the variation of the second-order Lagrangian (9.11) against the printed (9.12)-(9.15).

I2 = <U, U>, U = X(F_A) + kappa * T (9.7), with the metric trace pairing <x, y> = Tr(x ^ *y)/2^(n/2) (`mpair`),
eps and the metric fixed, delta T = alpha. Flat model, linear order in T: U_lin(T) = X(dT) + kappa *T.

Exact Fourier test (H14). For T = t e^{i k.x} and alpha = a e^{-i k.x} on a flat torus, d -> i K ^ (K = sum k_i e^i),
and the first variation of the quadratic part of I2 is the bilinear form
    B(a, t) = 2 <X(-i K ^ a) + kappa *a, X(i K ^ t) + kappa *t>,
computed from the action alone (no adjoints). It is compared with <a, P t> for explicit operators P assembled from
    delta (codifferential, symbol on m-forms: u -> (-1)^m *^{-1}(i K ^ *u)), X* (metric adjoint via the diagonal Gram
    matrix of basis forms), *^{-1}, and *^dag (metric adjoint of *, explicit),
term by term and order by order in kappa, over k in {e_i} and {e_i + e_j}. The kappa^0, kappa^1, kappa^2 parts are
homogeneous in k of degree 2, 1, 0, and these vectors determine homogeneous forms of degree <= 2 (they would not
determine a general inhomogeneous polynomial of degree 2).
Conventions: "pinned" (* of gu.forms; a ^ *b = <a, b> vol) and "prime" (*' = (-1)^deg *, with its own pairing).
"""
from __future__ import annotations

import itertools

from gu.cliffform import GQ, plus, scale, star
from experiments.B07 import variation as V

I = GQ(0, 1)


def star_c(x: dict, eta: list[int], conv: str) -> dict:
    if conv == "pinned":
        return star(x, eta)
    if conv == "prime":
        return plus(*[{k: v * (-1) ** k[0].bit_count()} for k, v in star(x, eta).items()]) if x else {}
    raise ValueError(conv)


def mpair(x: dict, y: dict, eta: list[int], conv: str) -> GQ:
    """<x, y>_conv = Tr(x ^ *_conv y)/2^(n/2)."""
    return V.pair(x, star_c(y, eta, conv), eta)


def forms(n: int, deg: int, scalar_only: bool = False) -> list[dict]:
    blades = [0] if scalar_only else range(1 << n)
    return [{(sum(1 << i for i in c), A): GQ(1)} for c in itertools.combinations(range(n), deg) for A in blades]


def adjoint(Y, n: int, deg_in: int, deg_out: int, eta: list[int], conv: str):
    """Metric adjoint Y*: Omega^deg_out -> Omega^deg_in of Y: Omega^deg_in -> Omega^deg_out (diagonal Gram)."""
    Y, basis = V.Linear(Y), forms(n, deg_in)
    gram = []
    for b in basis:
        g = mpair(b, b, eta, conv)
        if g.im != 0 or g.re not in (1, -1):
            raise AssertionError(f"Gram is not diagonal +-1 at {b}: {g}")
        gram.append((b, g.re))

    def Ys(u: dict) -> dict:
        return plus(*[scale(b, mpair(Y(b), u, eta, conv) * GQ(g)) for b, g in gram])
    return Ys


def star_inv(x: dict, eta: list[int], conv: str) -> dict:
    """*^{-1} by the computed square of * on each homogeneous basis element."""
    out: dict = {}
    for k, v in x.items():
        e = {k: GQ(1)}
        ss = star_c(star_c(e, eta, conv), eta, conv)
        (k2, w), = ss.items()
        assert k2 == k and w.im == 0 and w.re in (1, -1)
        out = plus(out, scale(star_c(e, eta, conv), v * w))
    return out


def star_adjoint_sign(p: int, q: int, k: int, conv: str) -> int:
    """s with *^dag = s * from Omega^(n-k) to Omega^k, checked on every basis pair (scalar Clifford factor: * acts on
    the form factor only, so the sign does not depend on the Clifford coefficient)."""
    eta, n = V.eta_of(p, q), p + q
    signs = set()
    for a in forms(n, k, scalar_only=True):
        for u in forms(n, n - k, scalar_only=True):
            l, r = mpair(star_c(a, eta, conv), u, eta, conv), mpair(a, star_c(u, eta, conv), eta, conv)
            if l or r:
                signs.add(int(l.re * r.re))
    assert len(signs) == 1, signs
    return signs.pop()


def mass_sign(p: int, q: int, conv: str) -> int:
    """t with *^dag * = t Id on 1-forms."""
    eta, n = V.eta_of(p, q), p + q
    signs = {int(mpair(star_c(a, eta, conv), star_c(a, eta, conv), eta, conv).re * mpair(a, a, eta, conv).re)
             for a in forms(n, 1, scalar_only=True)}
    assert len(signs) == 1, signs
    return signs.pop()


def wavevectors(n: int) -> list[list[int]]:
    return [[int(i == a) for i in range(n)] for a in range(n)] + \
           [[int(i in (a, b)) for i in range(n)] for a, b in itertools.combinations(range(n), 2)]


def fourier_terms(X, p: int, q: int, kv: list[int], conv: str) -> dict:
    """Matrices {name: {(ai, ti): GQ}} over basis 1-forms a, t, for one wavevector kv.

    action_k0/k1/k2: kappa^0, kappa^1, kappa^2 parts of B(a, t);
    printed_1..4: <a, 2 * term> for (9.13)'s terms, term 2 repaired by inserting * (literal term 2 is ill-typed);
    derived_3, derived_4: <a, 2 * kappa *^dag X(i K ^ t)> and <a, 2 * kappa^2 *^dag * t> (kappa set to 1).
    """
    eta, n = V.eta_of(p, q), p + q
    X = V.Linear(X)
    Xs = adjoint(X, n, 2, n - 1, eta, conv)
    Sd = adjoint(lambda x: star_c(x, eta, conv), n, 1, n - 1, eta, conv)
    K = {(1 << i, 0): GQ(c) for i, c in enumerate(kv) if c}

    def dsym(u, sgn):  # symbol of d on e^{sgn i k.x}
        return scale(V.wedge_prod(K, u, eta), I * GQ(sgn))

    def delta(u, deg):  # symbol of the codifferential on m-forms, e^{+i k.x}
        return scale(star_inv(dsym(star_c(u, eta, conv), 1), eta, conv), GQ((-1) ** deg))

    basis = V.one_forms(n)
    out = {name: {} for name in ("action_k0", "action_k1", "action_k2", "printed_1", "printed_2", "printed_3",
                                 "printed_4", "derived_3", "derived_4")}
    for ti, t in enumerate(basis):
        Xdt = X(dsym(t, 1))
        st = star_c(t, eta, conv)
        P = {"printed_1": delta(Xs(Xdt), 2), "printed_2": delta(Xs(st), 2), "printed_3": star_c(Xdt, eta, conv),
             "printed_4": t, "derived_3": Sd(Xdt), "derived_4": Sd(st)}
        for ai, a in enumerate(basis):
            Xda = X(dsym(a, -1))
            sa = star_c(a, eta, conv)
            vals = {"action_k0": mpair(Xda, Xdt, eta, conv) * GQ(2),
                    "action_k1": (mpair(Xda, st, eta, conv) + mpair(sa, Xdt, eta, conv)) * GQ(2),
                    "action_k2": mpair(sa, st, eta, conv) * GQ(2)}
            vals.update({nm: mpair(a, u, eta, conv) * GQ(2) for nm, u in P.items()})
            for nm, v in vals.items():
                if v:
                    out[nm][(ai, ti)] = v
    return out


def lin(*terms) -> dict:
    """Sum of (coefficient, matrix) pairs."""
    out: dict = {}
    for c, m in terms:
        for k, v in m.items():
            w = out.get(k, GQ()) + v * GQ(c)
            if w:
                out[k] = w
            else:
                out.pop(k, None)
    return out


def compare(X, p: int, q: int, conv: str) -> dict:
    """Which printed/derived combinations equal the action's variation, over all wavevectors."""
    checks = {"kappa0: action == printed_1": lambda m: lin((1, m["action_k0"]), (-1, m["printed_1"])),
              "kappa1: action == printed_2 + printed_3": lambda m: lin((1, m["action_k1"]), (-1, m["printed_2"]),
                                                                        (-1, m["printed_3"])),
              "kappa1: action == printed_2 + derived_3": lambda m: lin((1, m["action_k1"]), (-1, m["printed_2"]),
                                                                        (-1, m["derived_3"])),
              "kappa2: action == printed_4": lambda m: lin((1, m["action_k2"]), (-1, m["printed_4"])),
              "kappa2: action == derived_4": lambda m: lin((1, m["action_k2"]), (-1, m["derived_4"])),
              "derived_3 == -printed_3": lambda m: lin((1, m["derived_3"]), (1, m["printed_3"])),
              "derived_4 == -printed_4": lambda m: lin((1, m["derived_4"]), (1, m["printed_4"]))}
    res = {name: True for name in checks}
    nonvacuous = {name: False for name in ("printed_1", "printed_2", "printed_3", "printed_4")}
    for kv in wavevectors(p + q):
        m = fourier_terms(X, p, q, kv, conv)
        for name, f in checks.items():
            res[name] &= not f(m)
        for name in nonvacuous:
            nonvacuous[name] |= bool(m[name])
    return {"signature": [p, q], "conv": conv, "checks": res, "nonvacuous": nonvacuous}


def ym_symbol(X, p: int, q: int, conv: str = "pinned") -> dict:
    """Is the kappa^0 kinetic symbol a -> delta X*X(iK ^ a) one scalar multiple of the ordinary Yang-Mills symbol
    a -> delta(iK ^ a), for every wavevector? This is the (9.14) Yang-Mills reading at principal-symbol level. In 4D a
    term lambda * in X*X drops out: delta(*(iK ^ a)) = +-*^{-1}(iK ^ iK ^ a) = 0 since K ^ K = 0. So, unlike X*X ~ Id,
    one common nonzero ratio is necessary and sufficient for the flat constant-coefficient quadratic kinetic operator
    to be a multiple of ordinary Yang-Mills (not for equality of actions, nor for curved or nonlinear equations).
    Ratios over all nonzero YM entries; a nonzero entry where the YM symbol vanishes is a mismatch. Both symbols are
    homogeneous quadratics in k, so a shared ratio on these wavevectors holds for all k. Codifferential symbol as in
    `fourier_terms` (degree 2)."""
    eta, n = V.eta_of(p, q), p + q
    X = V.Linear(X)
    Xs = adjoint(X, n, 2, n - 1, eta, conv)

    def delta2(u):
        return star_inv(scale(V.wedge_prod(K, star_c(u, eta, conv), eta), I), eta, conv)

    ratios, mismatches = set(), 0
    for kv in wavevectors(n):
        K = {(1 << i, 0): GQ(c) for i, c in enumerate(kv) if c}
        for t in V.one_forms(n):
            dt = scale(V.wedge_prod(K, t, eta), I)
            sx, s0 = delta2(Xs(X(dt))), delta2(dt)
            for key in set(sx) | set(s0):
                u, v = sx.get(key, GQ()), s0.get(key, GQ())
                if not v:
                    mismatches += bool(u)
                    continue
                w, m = u * GQ(v.re, -v.im), v.re ** 2 + v.im ** 2
                ratios.add(str(GQ(w.re / m, w.im / m)))
    return {"signature": [p, q], "conv": conv, "ratios": sorted(ratios), "mismatches": mismatches,
            "ym_proportional": mismatches == 0 and len(ratios) == 1 and str(GQ()) not in ratios}


def xstar_x(X, p: int, q: int, conv: str = "pinned") -> dict:
    """Is X* X a multiple of the identity on ad-valued 2-forms? (the (9.14) Yang-Mills reading)."""
    eta, n = V.eta_of(p, q), p + q
    X = V.Linear(X)
    Xs = adjoint(X, n, 2, n - 1, eta, conv)
    ratios, offdiag = set(), 0
    for b in forms(n, 2):
        img = Xs(X(b))
        (k,) = b
        rest = {kk: v for kk, v in img.items() if kk != k}
        offdiag += bool(rest)
        ratios.add(str(img.get(k, GQ())))
    return {"signature": [p, q], "diagonal_values": sorted(ratios), "offdiagonal_rows": offdiag,
            "multiple_of_identity": offdiag == 0 and len(ratios) == 1}
