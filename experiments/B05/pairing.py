"""B05 Task 4: chirality behaviour of Spin(p,q)-invariant Hermitian forms, the U(1)s they admit, and bilinear variations.

Exact facts about the existing monomial gammas (`gu.clifford`). ASSUMPTION (labelled, not recovered from the
source): GU (3.31), p. 24, embeds complex Dirac Spin(7,7) in U(64,64) but prints no Hermitian form. The two
forms below are candidate representatives of that U(64,64); the draft does not say which, if either, it uses.
"""
from __future__ import annotations

from gu.clifford import Mono, chirality, dirac_pairing, gammas


def _hermitian_phase(m: Mono) -> Mono:
    for k in range(4):
        c = m.times_i_power(k)
        if c.dagger() == c:
            return c
    raise AssertionError("no Hermitian phase")


def spacelike_pairing(p: int, q: int) -> Mono:
    """Phase times the product of the spacelike gammas, chosen Hermitian (the other candidate form)."""
    G = gammas(p, q)
    out = Mono.identity(G[0].n)
    for g in G[:p]:
        out = out @ g
    return _hermitian_phase(out)


def forms(p: int, q: int) -> dict[str, Mono]:
    return {"timelike": dirac_pairing(p, q), "spacelike": spacelike_pairing(p, q)}


def invariant(p: int, q: int, A: Mono) -> bool:
    """Sigma^dagger A + A Sigma = 0 for every Sigma = G_a G_b, a < b."""
    G = gammas(p, q)
    return all((G[a] @ G[b]).dagger() @ A == -(A @ G[a] @ G[b])
               for a in range(p + q) for b in range(a + 1, p + q))


def relation_to_chirality(p: int, q: int, A: Mono) -> str:
    C = chirality(p, q)
    if A @ C == C @ A:
        return "commute"
    if A @ C == -(C @ A):
        return "anticommute"
    return "neither"


def in_isometry_algebra(X: Mono, A: Mono) -> bool:
    """X in u(A) iff X^dagger A + A X = 0."""
    return X.dagger() @ A == -(A @ X)


def u1_membership(p: int, q: int, A: Mono) -> dict[str, bool]:
    """Which of the central phase iI, the axial phase iC and the real chiral boost C lie in u(A)."""
    C = chirality(p, q)
    iI = Mono.identity(C.n).times_i_power(1)
    return {"central_iI": in_isometry_algebra(iI, A),
            "axial_iC": in_isometry_algebra(C.times_i_power(1), A),
            "chiral_boost_C": in_isometry_algebra(C, A)}


def sharp(S: Mono, A: Mono) -> Mono:
    """S^sharp = A^-1 S^dagger A. Monomials with unit phases are unitary, so A^-1 = A^dagger."""
    if not A @ A.dagger() == Mono.identity(A.n):
        raise AssertionError("A is not unitary")
    return A.dagger() @ S.dagger() @ A


def bilinear_invariant(K: Mono, S: Mono, Sbar: Mono) -> bool:
    """delta(psibar K psi) = psibar (Sbar K + K S) psi vanishes, for fixed K, delta psi = S psi, delta psibar = psibar Sbar.

    For the R1 (Dirac adjoint, fixed A) branch Sbar = sharp(S, A); for R0 (independent bar) Sbar is free.
    Monomial products are monomials, so Sbar K + K S = 0 iff Sbar K = -(K S).
    """
    return Sbar @ K == -(K @ S)


def signature_of(A: Mono) -> tuple[int, int]:
    """(n_plus, n_minus) of a Hermitian monomial form A; exact via its 1- and 2-cycles."""
    if not A.dagger() == A:
        raise ValueError("signature_of requires a Hermitian form")
    plus = minus = 0
    seen = set()
    for j in range(A.n):
        if j in seen:
            continue
        i = int(A.perm[j])
        if i == j:                                   # diagonal entry of a Hermitian form is +1 or -1
            plus, minus = (plus + 1, minus) if int(A.phase[j]) == 0 else (plus, minus + 1)
            seen.add(j)
        else:                                        # Hermitian 2x2 block [[0, conj z], [z, 0]]: one +, one -
            plus, minus = plus + 1, minus + 1
            seen.update((i, j))
    return plus, minus
