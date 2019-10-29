import numpy as np
from functions.polynomial import PolynomialFunction as Poly
from functools import reduce


def get_eigenvec(L, n):
    # TODO: сделать получение СВ из СЧ
    pass


def danilevsky(A: np.ndarray):
    '''Порождает м-цу Фробениуса P
и м-цы M и M^-1'''
    def make_m(A, k):
        n = A.shape[0]
        ret = np.ndarray(A.shape)
        for i in range(n):
            for j in range(n):
                if i != k:
                    ret[i, j] = 0.0 if i != j else 1.0
                elif j != k:
                    ret[i, j] = - A[k+1, j] / A[k+1, k]
                else:
                    ret[i, j] = 1 / A[k+1, k]
        return ret

    def make_m_inv(A, k):
        n = A.shape[0]
        ret = np.ndarray(A.shape)
        for i in range(n):
            for j in range(n):
                if i != k:
                    ret[i, j] = 0.0 if i != j else 1.0
                else:
                    ret[i, j] = A[k+1, j]
        return ret

    n = A.shape[0]
    M = [None for i in range(n-1)]
    M_inv = [None for i in range(n-1)]

    for i in range(n-2, -1, -1):
        M[i] = make_m(A, i)
        M_inv[i] = make_m_inv(A, i)
        A_til = A.dot(M[i])
        A = M_inv[i].dot(A_til)

    return A, M, M_inv


def make_poly(P):
    '''Порождает полином из первой строки
м-цы Фробениуса'''
    return Poly([-p for p in reversed(P[0])] + [1.0])


def make_S(M):
    '''Порождает матрицу S из матриц M1..Mn-1'''

    # reduce(np.dot, reversed(M)) =
    # = Mn-1 * Mn-2 * ... * M1
    return reduce(np.dot, reversed(M))
