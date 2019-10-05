import numpy
from math import sqrt


def vec_eps(A, x, b):
    return A.dot(x) - b


def mat_eps(A, X):
    return A * X - numpy.identity(A.shape[0])


def norm(M):
    ret = 0.0
    for e in numpy.nditer(M):
        ret += e**2
    return sqrt(ret)
