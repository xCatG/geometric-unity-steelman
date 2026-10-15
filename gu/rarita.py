"""Rarita-Schwinger projector, charge conjugation and the Cartan weight adapter (B03).

Conventions (experiments/B03/ansatz.md, rev 1.1):
- Physical gammas G_a = gu.clifford.gammas(p, q); eta_a = +1 for a < p, -1 otherwise.
- Euclidean frame E_a = G_a (eta_a = +1) or -i G_a (eta_a = -1), so E_a^2 = 1.
- Cartan pairs are Jordan-Wigner pairs (2k, 2k+1); h_k = -i E_{2k} E_{2k+1} is diagonal with
  entries +-1, the doubled weight coordinate y_k of each basis spinor.
- A split lists the horizontal pairs first, then the normal pairs.
- Q^a_b = d delta^a_b I - G^a G_b with G^a = eta_a G_a; P = Q/d; the RS space is im Q.
All matrices are exact: Mono (Z[i] monomials) or scipy int64 sparse in realified form [[R,-I],[I,R]].
"""
from collections import Counter

import numpy as np
from scipy import sparse as sp

from gu.clifford import Mono, chirality, eta, gammas

SPLITS = {
    "7,7|1,3+6,4": (7, 7, ((6, 7), (8, 9)), ((0, 1), (2, 3), (4, 5), (10, 11), (12, 13))),
    "9,5|1,3+8,2": (9, 5, ((8, 9), (10, 11)), ((0, 1), (2, 3), (4, 5), (6, 7), (12, 13))),
    "9,5|3,1+6,4": (9, 5, ((6, 7), (8, 9)), ((0, 1), (2, 3), (4, 5), (10, 11), (12, 13))),
    "3,1|1,1+2,0": (3, 1, ((2, 3),), ((0, 1),)),
}


def split_signatures(key: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """(horizontal, normal) signatures of a split, counted from the axis lists."""
    p, q, hor, nor = SPLITS[key]
    sig = eta(p, q)
    count = lambda pairs: (sum(sig[a] > 0 for pr in pairs for a in pr),
                           sum(sig[a] < 0 for pr in pairs for a in pr))
    return count(hor), count(nor)


def euclid(p: int, q: int) -> list[Mono]:
    return [g if a < p else g.times_i_power(3) for a, g in enumerate(gammas(p, q))]


def spin_weights(key: str) -> list[tuple[int, ...]]:
    """Doubled weight of each standard basis spinor, horizontal coordinates first."""
    p, q, hor, nor = SPLITS[key]
    E = euclid(p, q)
    n = E[0].n
    cols = []
    for a, b in hor + nor:
        h = (E[a] @ E[b]).times_i_power(3)
        if not np.array_equal(h.perm, np.arange(n)) or any(h.phase % 2):
            raise AssertionError(f"Cartan pair {(a, b)} is not diagonal with real signs")
        cols.append([1 if ph == 0 else -1 for ph in h.phase])
    return [tuple(c[j] for c in cols) for j in range(n)]


def even(w) -> bool:
    return sum(1 for x in w if x < 0) % 2 == 0


def chirality_vs_parity(key: str) -> int:
    """s with gu.clifford.chirality(p, q) = s * Pi, Pi = +1 on even-minus weights (asserted)."""
    p, q = SPLITS[key][:2]
    C = chirality(p, q)
    ws = spin_weights(key)
    n = len(ws)
    if not np.array_equal(C.perm, np.arange(n)):
        raise AssertionError("chirality is not diagonal in the Jordan-Wigner basis")
    signs = [1 if ph == 0 else -1 for ph in C.phase]
    par = [1 if even(w) else -1 for w in ws]
    s = signs[0] * par[0]
    if any(c != s * x for c, x in zip(signs, par)):
        raise AssertionError("chirality is not a multiple of the weight parity")
    return s


def spinor_character(key: str, chir: int) -> Counter:
    """Weight character of S_+ (chir=+1, even) or S_- (chir=-1) from the basis weights."""
    return Counter(w for w in spin_weights(key) if even(w) == (chir == 1))


def rs_character(key: str, chir: int, Q=None) -> Counter:
    """Weight character of im Q on V (x) S_chir, read from the realified matrix Q itself.

    Scope (Layer 1, spec section 5): conjugation by c is a GL(14, C) similarity that identifies
    the complexified so(p,q) module with the so(14, C) one, so this character is the same for
    every signature. Real-form data live only in J (j_square, j_weight_signs) and in
    chirality_vs_parity. Only the 7 Cartan-pair blocks are read; the other blocks are pinned by
    verify_split (Q^2 = dQ, gamma.Q = 0 and covariance), so call this through verify_split.

    Q defaults to the production projector_Q(p, q). Its blocks are conjugated into the Euclidean
    frame, Q''^a_b = c_a Q^a_b c_b^-1 with c = 1 or i. For a Cartan pair (a, b) the vectors
    u_s = E_a + s i E_b (s = +-1) carry doubled weight 2s, with dual rows (1, -s i)/2, so the
    diagonal entry on u_s (x) e_j is (Q''aa + Q''bb + s i Q''ab - s i Q''ba)[j, j] / 2. Once Q^2 = dQ
    and Q commutes with the Cartan generators (verify_split), the multiplicity of a weight is the
    sum of those entries over the weight space, divided by d.
    """
    p, q, hor, nor = SPLITS[key]
    d, sig = p + q, eta(p, q)
    if Q is None:
        Q = projector_Q(p, q)
    n = gammas(p, q)[0].n
    dn = d * n
    Q = Q.tocsr()

    def entry(a, b, j):  # c_a Q^a_b[j, j] c_b^-1 as an exact Gaussian integer (re, im)
        re, im = int(Q[a * n + j, b * n + j]), int(Q[dn + a * n + j, b * n + j])
        for _ in range(((sig[a] < 0) - (sig[b] < 0)) % 4):
            re, im = -im, re
        return re, im

    ws = spin_weights(key)
    twice = Counter()                                  # 2 * trace, real part; imaginary checked
    for k, (a, b) in enumerate(hor + nor):
        for j, w in enumerate(ws):
            if even(w) != (chir == 1):
                continue
            aa, bb, ab, ba = entry(a, a, j), entry(b, b, j), entry(a, b, j), entry(b, a, j)
            for s in (1, -1):
                # s i (ab - ba): real part -s * Im(ab - ba), imaginary part s * Re(ab - ba)
                re = aa[0] + bb[0] - s * (ab[1] - ba[1])
                im = aa[1] + bb[1] + s * (ab[0] - ba[0])
                if im:
                    raise AssertionError(f"non-real diagonal entry at pair {(a, b)}, spinor {j}")
                v = list(w)
                v[k] += 2 * s
                twice[tuple(v)] += re
    out = Counter()
    for v, t in twice.items():
        if t % (2 * d):
            raise AssertionError(f"trace {t}/2 on weight {v} is not a multiple of d")
        if t:
            out[v] = t // (2 * d)
    return out


# ---- exact sparse realified matrices

def _pair(m: Mono):
    r, i = m.to_dense()
    return sp.csr_matrix(r), sp.csr_matrix(i)


def _realify(r, i):
    return sp.bmat([[r, -i], [i, r]], format="csr")


def _same(a, b) -> bool:
    return (a - b).count_nonzero() == 0


def projector_Q(p: int, q: int):
    """Realified Q (2 d n square, int64): blocks Q^a_b = d delta I - eta_a G_a G_b."""
    G, sig, d = gammas(p, q), eta(p, q), p + q
    n = G[0].n
    one = sp.identity(n, dtype=np.int64, format="csr")
    R, I = [], []
    for a in range(d):
        rr, ii = [], []
        for b in range(d):
            r, i = _pair(G[a] @ G[b])
            r, i = -sig[a] * r, -sig[a] * i
            if a == b:
                r = r + d * one
            rr.append(r)
            ii.append(i)
        R.append(rr)
        I.append(ii)
    return _realify(sp.bmat(R, format="csr"), sp.bmat(I, format="csr"))


def contraction(p: int, q: int):
    """Realified gamma contraction psi -> sum_a G_a psi^a, V (x) S -> S."""
    G = gammas(p, q)
    r, i = zip(*(_pair(g) for g in G))
    return _realify(sp.hstack(r, format="csr"), sp.hstack(i, format="csr"))


def generator(p: int, q: int, a: int, b: int):
    """Realified 2 * rho(X_ab) on V (x) S for X_ab = G_a G_b / 2 (vector part times 2)."""
    G, sig, d = gammas(p, q), eta(p, q), p + q
    n = G[0].n
    vec = sp.lil_matrix((d, d), dtype=np.int64)
    vec[a, b] = 2 * sig[b]
    vec[b, a] = -2 * sig[a]
    sr, si = _pair(G[a] @ G[b])
    eye_d = sp.identity(d, dtype=np.int64, format="csr")
    eye_n = sp.identity(n, dtype=np.int64, format="csr")
    return _realify(sp.kron(vec.tocsr(), eye_n) + sp.kron(eye_d, sr), sp.kron(eye_d, si))


def projector_controls(p: int, q: int):
    """Two realified maps S -> V (x) S built by hand, not from Q.

    T: chi -> (G_1 chi, G_0 chi, 0, ...) is gamma-traceless (G_0 G_1 + G_1 G_0 = 0), so P must fix it.
    W: chi -> (eta_a G_a chi)_a is gamma-inserted, so P must kill it.
    """
    G, sig, d = gammas(p, q), eta(p, q), p + q
    zero = sp.csr_matrix((G[0].n, G[0].n), dtype=np.int64)

    def stack(blocks):
        r, i = zip(*(_pair(m) if m is not None else (zero, zero) for m in blocks))
        return _realify(sp.vstack(r, format="csr"), sp.vstack(i, format="csr"))

    T = stack([G[1], G[0]] + [None] * (d - 2))
    W = stack([G[a].times_i_power(0 if sig[a] > 0 else 2) for a in range(d)])
    return T, W


def chirality_on_vs(p: int, q: int):
    """Realified 1 (x) C on V (x) S."""
    cr, ci = _pair(chirality(p, q))
    eye_d = sp.identity(p + q, dtype=np.int64, format="csr")
    return _realify(sp.kron(eye_d, cr), sp.kron(eye_d, ci))


def euclidean_conjugation_ok(p: int, q: int) -> bool:
    """Check c_a (-eta_a G_a G_b) c_b^{-1} = -E_a E_b for all a, b, with c_a = 1 or i (G_a = c_a E_a).

    The d delta I part is unchanged by the conjugation, so this proves c Q c^{-1} = Q''.
    """
    G, E, sig, d = gammas(p, q), euclid(p, q), eta(p, q), p + q
    for a in range(d):
        for b in range(d):
            k = (1 if sig[a] < 0 else 0) - (1 if sig[b] < 0 else 0)      # c_a / c_b
            lhs = (G[a] @ G[b]).times_i_power(k + (2 if sig[a] > 0 else 0))  # times -eta_a
            if not lhs == -(E[a] @ E[b]):
                return False
    return True


# ---- charge conjugation J = B o conj

def charge_conjugation(p: int, q: int) -> Mono:
    """B = product of the purely imaginary gammas (in index order); J = B o complex conjugation."""
    G = gammas(p, q)
    B = Mono.identity(G[0].n)
    for g in G:
        odd = g.phase % 2
        if all(odd):
            B = B @ g
        elif any(odd):
            raise AssertionError("gamma with mixed real/imaginary entries")
    return B


def conj(m: Mono) -> Mono:
    return Mono(m.perm, -m.phase)


def j_square(p: int, q: int) -> int:
    B = charge_conjugation(p, q)
    sq = B @ conj(B)
    if sq == Mono.identity(B.n):
        return 1
    if sq == -Mono.identity(B.n):
        return -1
    raise AssertionError("B conj(B) is not +-1")


def j_commutes_with_generators(p: int, q: int) -> bool:
    G, B = gammas(p, q), charge_conjugation(p, q)
    return all(B @ conj(G[a] @ G[b]) == (G[a] @ G[b]) @ B
               for a in range(p + q) for b in range(a + 1, p + q))


def j_preserves_chirality(p: int, q: int) -> bool:
    B, C = charge_conjugation(p, q), chirality(p, q)
    return B @ conj(C) == C @ B


def j_on_vs(p: int, q: int):
    """Realified antilinear J on V (x) S: (1 (x) B) composed with complex conjugation."""
    br, bi = _pair(charge_conjugation(p, q))
    d, n = p + q, br.shape[0]
    eye_d = sp.identity(d, dtype=np.int64, format="csr")
    lin = _realify(sp.kron(eye_d, br), sp.kron(eye_d, bi))
    cj = sp.diags([1] * (d * n) + [-1] * (d * n), dtype=np.int64, format="csr")
    return lin @ cj


def j_weight_signs(key: str) -> tuple[int, ...]:
    """sigma with weight(J e_j) = sigma * weight(e_j) coordinatewise, the same for every j (asserted).

    J e_j = B e_j (basis vectors are real), so J moves the weight of e_j to that of e_{B.perm[j]}.
    """
    p, q = SPLITS[key][:2]
    B = charge_conjugation(p, q)
    ws = spin_weights(key)
    sigma = None
    for j, w in enumerate(ws):
        u = ws[int(B.perm[j])]
        s = tuple(1 if a == b else -1 if a == -b else 0 for a, b in zip(w, u))
        if 0 in s or (sigma is not None and s != sigma):
            raise AssertionError("J does not act on weights by a fixed sign pattern")
        sigma = s
    return sigma


# ---- the single implementation gate, shared by the runner and the tests (P2)

RS_HW = {1: (1, 0, 0, 0, 0, 0, 1), -1: (1, 0, 0, 0, 0, 1, 0)}
S_HW = {1: (0, 0, 0, 0, 0, 0, 1), -1: (0, 0, 0, 0, 0, 1, 0)}
J_SQUARE = {(7, 7): 1, (9, 5): -1}                     # [lit] Figueroa-O'Farrill, Table 2


def verify_split(key: str, Q=None) -> dict:
    """Assert every test-0/3/4 gate for one split, on the production Q unless Q is supplied.

    Gates: Q^2 = dQ; gamma.Q = 0; tr Q = d(d-1) dim S and half of it per chirality; P fixes the
    hand-built traceless map T and kills the gamma-inserted map W; Q commutes with every adjacent and every Cartan-pair generator;
    euclidean_conjugation_ok; at d = 14 the weight characters of S_chir and of im Q (read from Q)
    equal reps.py's restrictions; J commutes with the generators and with Q, preserves chirality
    at d = 14, and has the literature J^2. Returns the summary row recorded in result.json.
    """
    from gu.reps import Simple, d7_to_d5a1a1, split_14

    p, q, hor, nor = SPLITS[key]
    d = p + q
    n = gammas(p, q)[0].n
    Q = projector_Q(p, q) if Q is None else Q.tocsr()
    assert (Q @ Q - d * Q).count_nonzero() == 0, "Q^2 != dQ"
    assert (contraction(p, q) @ Q).count_nonzero() == 0, "gamma.Q != 0"
    total = int(Q.diagonal().sum()) // 2
    assert total == d * (d - 1) * n, f"tr Q = {total}"
    C = chirality_on_vs(p, q)
    twisted = int((Q @ C).diagonal().sum()) // 2
    assert twisted == 0, "tr Q not split evenly between the chiralities"
    T, W = projector_controls(p, q)
    assert T.count_nonzero() and (contraction(p, q) @ T).count_nonzero() == 0, "T not traceless"
    assert (Q @ T - d * T).count_nonzero() == 0, "P does not fix a traceless vector"
    assert W.count_nonzero() and (Q @ W).count_nonzero() == 0, "P does not kill gamma-inserted"
    pairs = [(a, a + 1) for a in range(d - 1)] + [pr for pr in hor + nor]
    for a, b in pairs:
        X = generator(p, q, a, b)
        assert (Q @ X - X @ Q).count_nonzero() == 0, f"Q not covariant under {(a, b)}"
    assert euclidean_conjugation_ok(p, q)
    J = j_on_vs(p, q)
    assert j_commutes_with_generators(p, q) and (J @ Q - Q @ J).count_nonzero() == 0
    assert j_preserves_chirality(p, q) == (d == 14)
    row = {"split": key, "signatures": split_signatures(key),
           "chirality_vs_parity": chirality_vs_parity(key), "trace_Q": total,
           "J_square": j_square(p, q), "J_preserves_chirality": d == 14,
           "J_weight_signs": j_weight_signs(key)}
    if d == 14:
        assert row["J_square"] == J_SQUARE[(p, q)]
        D7 = Simple("D", 7)
        for chir in (1, -1):
            def restrict(ch):
                out = Counter()
                for w, m in ch.items():
                    out[split_14(w)] += m
                return out
            assert restrict(spinor_character(key, chir)) == d7_to_d5a1a1(D7.character(S_HW[chir]))
            assert restrict(rs_character(key, chir, Q)) == d7_to_d5a1a1(D7.character(RS_HW[chir])), \
                f"im Q character differs from RS at chirality {chir}"
        row["matrix_RS_character_equals_reps"] = True
    else:
        dims = [sum(rs_character(key, c, Q).values()) for c in (1, -1)]
        assert dims == [(d - 1) * n // 2] * 2, f"RS dimensions {dims}"
    return row
