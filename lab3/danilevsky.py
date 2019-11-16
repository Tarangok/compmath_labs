import numpy as np
from math import isclose
from functions.polynomial import PolynomialFunction as Poly
from lab3.aberth import aberth

from functools import reduce


def get_frob_eigenvec(L, n):
    '''Получение СВ для матрицы Фробениуса'''
    return np.asarray(list(L ** (n-i-1) for i in range(n)))


def make_m(A, k):
    if isclose(A[k+1, k], 0.0):
        raise ValueError('Unable to build Frobenius mtx')
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


def danilevsky(A: np.ndarray):
    '''Порождает м-цу Фробениуса P
и м-цы M и M^-1'''

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
м-цы Фробениуса P'''
    return Poly([-p for p in reversed(P[0])] + [1.0])


def solve_poly(F, eps=1e-4):
    roots = [r.real for r in aberth(F, eps) if abs(r.imag) < eps]
    roots.sort()
    print(roots)

    ret = []
    i = 0
    L = len(roots)
    while i < L:
        ret.append({'r': roots[i], 'k': 1})
        i += 1
        while i < L and abs(ret[-1]['r']-roots[i]) < eps:
            i += 1
            ret[-1]['k'] += 1
    return ret


def make_S(M):
    '''Порождает матрицу S из матриц M1..Mn-1'''

    # reduce(np.dot, reversed(M)) =
    # = Mn-1 * Mn-2 * ... * M1
    return reduce(np.dot, reversed(M))
