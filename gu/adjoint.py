# gu/adjoint.py
"""The internal gauge algebra u(A) (= u(64,64) for d=14, q>=1) and its group, exactly.

Complex n x n matrices are embedded as real 2n x 2n rational matrices,
a+ib -> [[a,-b],[b,a]]. Under this embedding M^dagger becomes the transpose, so
u(A) = {M : M^T A + A M = 0} and U(A) = {h : h^T A h = A} are tested over QQ,
restricted to complex-linear block matrices. A must be a nonsingular Hermitian pairing.
The basis of u(A) is never materialized (spec rev 4.1, section 5).
"""
from __future__ import annotations

import numpy as np
from numbers import Integral, Rational
from flint import fmpq, fmpq_mat

from gu.clifford import Mono


class SingularCayley(ValueError):
    """det(I + X) = 0: rescale or resample X. Not an operator failure."""


def embed(re: np.ndarray, im: np.ndarray) -> fmpq_mat:
    re, im = np.asarray(re, dtype=object), np.asarray(im, dtype=object)
    if re.ndim != 2 or re.shape[0] != re.shape[1] or im.shape != re.shape:
        raise ValueError('real and imaginary parts must be same-sized square matrices')
    n = re.shape[0]
    re = np.array([_rational(x) for x in re.flat], dtype=object).reshape(re.shape)
    im = np.array([_rational(x) for x in im.flat], dtype=object).reshape(im.shape)
    big = np.zeros((2 * n, 2 * n), dtype=object)
    big[0::2, 0::2] = re
    big[0::2, 1::2] = -im
    big[1::2, 0::2] = im
    big[1::2, 1::2] = re
    return fmpq_mat(2 * n, 2 * n, list(big.flat))


def _rational(x):
    if isinstance(x, fmpq):
        return x
    if isinstance(x, Integral):
        return fmpq(int(x))
    if isinstance(x, Rational):
        return fmpq(int(x.numerator), int(x.denominator))
    raise ValueError('embedding requires exact rational entries; floats are forbidden')


def _square(M):
    return isinstance(M, fmpq_mat) and M.nrows() == M.ncols()


def _complex_linear(M):
    if not _square(M) or M.nrows() % 2:
        return False
    return all(M[i, j] == M[i + 1, j + 1] and M[i, j + 1] == -M[i + 1, j]
               for i in range(0, M.nrows(), 2) for j in range(0, M.ncols(), 2))


def _pairing(A):
    if not _complex_linear(A) or A.transpose() != A or A.det() == 0:
        raise ValueError('A must embed a nonsingular Hermitian pairing')


def from_mono(m: Mono) -> fmpq_mat:
    return embed(*m.to_dense())


def _eye(n: int) -> fmpq_mat:
    return fmpq_mat(n, n, [1 if i == j else 0 for i in range(n) for j in range(n)])


def is_in_algebra(M: fmpq_mat, A: fmpq_mat) -> bool:
    _pairing(A)
    if not _complex_linear(M) or M.nrows() != A.nrows():
        return False
    return M.transpose() * A + A * M == fmpq_mat(A.nrows(), A.ncols())


def is_in_group(h: fmpq_mat, A: fmpq_mat) -> bool:
    _pairing(A)
    if not _complex_linear(h) or h.nrows() != A.nrows():
        return False
    return h.transpose() * A * h == A


def random_algebra_element(A: fmpq_mat, rng: np.random.Generator,
                           nonzeros: int = 8, scale: int = 3) -> fmpq_mat:
    """X = (Y - A Y^dagger A) / scale for a sparse Gaussian-integer Y. Requires A^2 = I."""
    _pairing(A)
    if not isinstance(nonzeros, Integral) or nonzeros < 0 or not isinstance(scale, Integral) or scale <= 0:
        raise ValueError('nonzeros must be a nonnegative integer and scale a positive integer')
    nonzeros, scale = int(nonzeros), int(scale)
    N = A.nrows()
    if A * A != _eye(N):
        raise ValueError("random_algebra_element() assumes A^2 = I")
    n = N // 2
    re = np.zeros((n, n), dtype=np.int64)
    im = np.zeros((n, n), dtype=np.int64)
    for _ in range(nonzeros):
        i, j = rng.integers(0, n, 2)
        re[i, j] += rng.integers(-2, 3)
        im[i, j] += rng.integers(-2, 3)
    Y = embed(re, im)
    return (Y - A * Y.transpose() * A) * fmpq(1, scale)


def cayley(X: fmpq_mat) -> fmpq_mat:
    """h = (I - X)(I + X)^{-1}; in U(A) whenever X is in u(A)."""
    if not _square(X):
        raise ValueError('Cayley requires a square exact rational matrix')
    I = _eye(X.nrows())
    D = I + X
    if D.det() == 0:
        raise SingularCayley("det(I + X) = 0")
    return (I - X) * D.inv()
