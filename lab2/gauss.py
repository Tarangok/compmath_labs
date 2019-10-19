import numpy


def gauss_triangle(A: numpy.ndarray):
    '''Порождает последовательность матриц для м-да Гаусса'''
    size = A.shape[0]
    ret = [A.copy()]

    for k in range(size):
        a_kk = ret[-1][k, k]

        new = ret[-1].copy()

        new[k, k] = 1.0
        for i in range(k+1, size):
            new[i, k] = 0.0
        for j in range(k+1, size):
            new[k, j] = ret[-1][k, j] / a_kk
            for i in range(k+1, size):
                new[i, j] = ret[-1][i, j] - ret[-1][i, k] * new[k, j]
        ret.append(new)
    return ret


def det(A_trg):
    '''По результатам gauss_triangle вычисляет детерминант'''
    ret = 1.0
    for i in range(len(A_trg)-1):
        ret *= A_trg[i][i, i]
    return ret


def solve(A_trg, b):
    '''По результатам gauss_triangle решает СЛАУ Ax = b'''
    size = b.size
    ret = [b.copy()]
    for k in range(size):
        new = ret[-1].copy()
        new[k] = ret[-1][k] / A_trg[k][k, k]
        for i in range(k+1, size):
            new[i] = ret[-1][i] - A_trg[k][i, k] * new[k]
        ret.append(new)
    x = numpy.ndarray(size)
    for i in range(size-1, -1, -1):
        x[i] = ret[i+1][i]
        for j in range(i+1, size):
            x[i] -= A_trg[i+1][i, j] * x[j]
    return x, ret


def inverse(A_trg):
    '''По результатам gauss_triangle с помощью solve вычисляет обр. матрицу'''
    ret = []
    es = []
    size = len(A_trg)-1

    for k in range(size):
        vec = numpy.zeros(size)
        vec[k] = 1.0
        r, e = solve(A_trg, vec)
        ret.append(r)
        es.append(e[size])

    return ret, es
