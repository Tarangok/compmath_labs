import numpy as np
from lab2.eps import norm


# Методы итерации предполагают, что на главной диагонали
# матрицы A находятся ненулевые элементы.
# Если это не так, то если в каждом столбце есть хотя бы один
# ненулевой элемент, то можно прибавить строку с этим эл-том
# к строке с эл-том главной диагонали, чтобы получить экви-
# валентную систему, но с ненулевым эл-том ГД.

def make_alpha(A: np.ndarray):
    alpha = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            alpha[i, j] = 0.0 if i == j else -A[i, j] / A[i, i]
    return alpha


def make_beta(A, b: np.ndarray):
    beta = np.zeros(b.shape[0])
    for i in range(A.shape[0]):
        beta[i] = b[i] / A[i, i]
    return beta


def test_diag(A: np.ndarray):
    N = A.shape[0]
    for i in range(N):
        diag = abs(A[i, i])
        nondiag = sum(abs(A[i, j]) for j in range(N) if i != j)
        if diag <= nondiag:
            return False
    return True


def solve(alpha: np.ndarray, beta: np.ndarray, b, eps):
    '''Проводит итерационный процесс для решения СЛАУ'''
    def new_x(a, b, x):
        n = x.shape[0]
        ret = np.zeros(x.shape)
        for i in range(n):
            s1 = sum(a[i, j] * ret[j] for j in range(i))
            s2 = sum(a[i, j] * x[j] for j in range(i+1, n))
            ret[i] = b[i] + s1 + s2
        return ret

    # начальное приближение
    x = b.copy()

    n = norm(alpha)
    k_eps = (1 - n)/n * eps

    xn = new_x(alpha, beta, x)
    n_diff = norm(xn - x)
    while n_diff >= k_eps:
        x = xn
        xn = new_x(alpha, beta, x)
        n_diff = norm(xn - x)

    return xn
