# experiments/B02/response.py
"""Test 5 at identity scope: the closed-form response of (9.3) on a spanning set.

For every R = KN(s, t) over unordered pairs of a symmetric basis (5565 tensors at
n = 14, rank 3185 = dim of algebraic curvature tensors, checked in spanning_rank),
every bracket assignment, Phi1 in {F, F'} and Phi2 in {B, B', 0}, assert
  *shiab(xi(R)) == -[m0=C] E_T(Ric) + S/2 ([m1m2=AA] ga E_T(g) + [m1m2=AC] de E_T'(g)).
By multilinearity in (Phi1, Phi2) this proves the formula for every real
(alpha, beta, gamma, delta) and, by linearity in R, on all algebraic curvature.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import numpy as np
from flint import nmod_mat

from gu.cliffform import plus, scale, star
from gu.curvature import dims, is_algebraic_curvature, kulkarni_nomizu, ricci, scalar
from gu.shiab import assemble, embed_tensor, eta_of, phi_basis, shiab_parts, xi

MODES = ["".join(m) for m in itertools.product("CA", repeat=3)]
PRIME = 1_000_003


def sym_basis(n: int) -> list[np.ndarray]:
    """s_ij = E_ij + E_ji for i < j, and s_ii = E_ii (diagonal entry 1, not 2)."""
    out = []
    for i in range(n):
        for j in range(i, n):
            s = np.zeros((n, n), dtype=np.int64)
            s[i, j] = s[j, i] = 1
            out.append(s)
    return out


def spanning_pairs(n: int) -> list[tuple[int, int]]:
    return list(itertools.combinations_with_replacement(range(n * (n + 1) // 2), 2))


def spanning_rank(n: int) -> tuple[int, int]:
    """(rank mod PRIME of the KN products, dim of algebraic curvature tensors).

    rank mod p <= rank over Q <= dim, so equality certifies spanning over Q, provided
    every row is an algebraic curvature tensor (the chart is Sym^2(Lambda^2), which has
    C(n,4) more coordinates than dim: 1 at n = 4, 1001 at n = 14; asserted below).
    """
    sym = sym_basis(n)
    cols = [(a, b, c, d) for a, b in itertools.combinations(range(n), 2)
            for c, d in itertools.combinations(range(n), 2) if (a, b) <= (c, d)]
    rows = []
    for s, t in spanning_pairs(n):
        R = kulkarni_nomizu(sym[s], sym[t])
        if not is_algebraic_curvature(R):
            raise AssertionError(f"KN product {(s, t)} is not algebraic")
        rows.append([int(R[k]) % PRIME for k in cols])
    return nmod_mat(rows, PRIME).rank(), sum(dims(n))


def check_signature(p: int, q: int, limit: int | None = None) -> dict:
    eta, n = eta_of(p, q), p + q
    g = np.diag(eta).astype(np.int64)
    phis = phi_basis(p, q)
    T = {"F": (1, 0), "F'": (0, 1)}
    Eg = {k: embed_tensor(g, *ab, p, q) for k, ab in T.items()}
    Eg_swap = {k: embed_tensor(g, ab[1], ab[0], p, q) for k, ab in T.items()}
    sym = sym_basis(n)
    pairs = spanning_pairs(n)[:limit]
    checked = nonzero = 0
    for s, t in pairs:
        R = kulkarni_nomizu(sym[s], sym[t])
        x = xi(R, eta)
        S = Fraction(int(scalar(R, eta)), 2)
        Ric = ricci(R, eta)
        for k1, (al, be) in T.items():
            ERic = embed_tensor(Ric, al, be, p, q)
            for k2, (ga, de) in (("B", (1, 0)), ("B'", (0, 1)), (None, (0, 0))):
                parts = shiab_parts(phis[k1], phis[k2] if k2 else {}, x, eta)
                for m in MODES:
                    raw = assemble(parts, m)
                    if any(f.bit_count() != n - 1 for f, _ in raw):
                        raise AssertionError(f"degree (test 1) at {(p, q, s, t, k1, k2, m)}")
                    got = star(raw, eta)
                    nonzero += bool(got)
                    want = scale(ERic, -1) if m[0] == "C" else {}
                    if m[1:] == "AA":
                        want = plus(want, scale(Eg[k1], S * ga))
                    if m[1:] == "AC":
                        want = plus(want, scale(Eg_swap[k1], S * de))
                    if got != want:
                        raise AssertionError(f"mismatch at {(p, q, s, t, k1, k2, m)}")
                    checked += 1
    return {"signature": [p, q], "inputs": len(pairs), "cases": checked, "nonzero_outputs": nonzero}


if __name__ == "__main__":
    p, q = int(sys.argv[1]), int(sys.argv[2])
    lim = int(sys.argv[3]) if len(sys.argv) > 3 else None
    print(check_signature(p, q, lim))
