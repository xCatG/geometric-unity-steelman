# tests/test_clifford.py
import pytest
import numpy as np

from gu.clifford import Mono, chirality, dirac_pairing, eta, gammas

SIGS = [(1, 1), (3, 1), (14, 0), (7, 7), (9, 5)]


@pytest.mark.parametrize("p,q", SIGS)
def test_clifford_relations(p, q):
    G, e = gammas(p, q), eta(p, q)
    n = 2 ** ((p + q) // 2)
    I = Mono.identity(n)
    assert all(g.n == n for g in G)
    for a in range(p + q):
        assert G[a] @ G[a] == (I if e[a] == 1 else -I)
        for b in range(a + 1, p + q):
            assert G[a] @ G[b] == -(G[b] @ G[a])


@pytest.mark.parametrize("p,q", SIGS)
def test_dirac_pairing(p, q):
    G, A = gammas(p, q), dirac_pairing(p, q)
    I = Mono.identity(A.n)
    assert A.dagger() == A
    assert A @ A == I
    if q == 0:
        assert A == I
    else:
        assert A.trace() == (0, 0)  # A^2 = I, Hermitian, traceless => inertia (n/2, n/2)
    for g in G:  # A G_a A^-1 = (-1)^q G_a^dagger
        rhs = g.dagger() @ A
        assert A @ g == (rhs if q % 2 == 0 else -rhs)


@pytest.mark.parametrize("p,q", SIGS)
def test_spin_generators_are_A_skew(p, q):
    G, A = gammas(p, q), dirac_pairing(p, q)
    for a in range(p + q):
        for b in range(a + 1, p + q):
            S = G[a] @ G[b]
            assert S.dagger() @ A == -(A @ S)


@pytest.mark.parametrize("p,q", SIGS)
def test_chirality(p, q):
    G, C = gammas(p, q), chirality(p, q)
    assert C @ C == Mono.identity(C.n)
    assert C.dagger() == C
    assert C.trace() == (0, 0)
    for g in G:
        assert C @ g == -(g @ C)


@pytest.mark.parametrize("p,q", [(1, 1), (3, 1), (7, 7), (9, 5)])
def test_spacelike_timelike_product_is_anti_isometry(p, q):
    # spec rev 4, section 4: gamma_s gamma_t is NOT in U(A)
    G, A = gammas(p, q), dirac_pairing(p, q)
    h = G[0] @ G[p]
    assert h.dagger() @ A @ h == -A


def test_odd_dimension_rejected():
    with pytest.raises(ValueError):
        gammas(2, 1)


def test_dense_roundtrip():
    G = gammas(1, 1)
    re, im = G[1].to_dense()
    assert (re ** 2 + im ** 2).sum() == 2  # one unit entry per column


@pytest.mark.parametrize('p,q', [(-1, 3), (1.0, 1), (1, 1.0)])
def test_signature_inputs_are_exact_nonnegative(p, q):
    """Control: reject negative counts and floating dimensions before construction."""
    for operation in (eta, gammas, dirac_pairing, chirality):
        with pytest.raises(ValueError):
            operation(p, q)


@pytest.mark.parametrize('perm,phase', [([0.0, 1], [0, 0]), ([0, 1], [0, 0.5]),
                                      ([0, 0], [0, 0]), ([0, 2], [0, 0]),
                                      ([0, 1], [0]), ([[0, 1]], [[0, 0]])])
def test_monomial_constructor_rejects_lossy_or_invalid_data(perm, phase):
    """Control: invalid permutations and fractional phases cannot silently truncate."""
    with pytest.raises(ValueError):
        Mono(perm, phase)


def test_monomial_dense_operations_hand_fixture():
    """Sampled control: non-involutive cycle catches reversed composition/dagger indexing."""
    a = Mono([1, 2, 0], [1, 2, 3])
    b = Mono([2, 0, 1], [0, 1, 2])
    assert a @ b == Mono([0, 1, 2], [3, 2, 0])
    assert a.dagger() == Mono([2, 0, 1], [1, 3, 2])
    re, im = a.to_dense()
    assert re.tolist() == [[0, 0, 0], [0, 0, 0], [0, -1, 0]]
    assert im.tolist() == [[0, 0, -1], [1, 0, 0], [0, 0, 0]]
    assert a @ a.dagger() == Mono.identity(3)
    with pytest.raises(ValueError):
        a.times_i_power(0.5)
    with pytest.raises(ValueError):
        Mono.identity(2.0)


def test_jordan_wigner_orientation():
    """Control: prescribed Pauli Y gives iY=[[0,1],[-1,0]], not its negative."""
    re, im = gammas(1, 1)[1].to_dense()
    assert re.tolist() == [[0, 1], [-1, 0]]
    assert not im.any()
