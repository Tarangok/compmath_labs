import lab3.reader as reader
from sys import stdin, stdout
import lab3.danilevsky as dan

from matrix.writer import write_mat
from matrix.det import det
from numpy import eye


f_in = open('l3_test.txt', 'r')
f_out = open('res.txt', 'w')

try:
    eps = 1e-5

    t, A = reader.read_task(f_in)
    n = A.shape[0]

    P, M, _ = dan.danilevsky(A)
    F = dan.make_poly(P)
    L = dan.solve_poly(F)

    S = None
    f_out.write('frobenius mtx:\n')
    write_mat(f_out, P)

    for l in L:
        f_out.write(f'lambda={l["r"]}\n')
        if t == reader.EIGENVALUE:
            d = det(A - eye(n).dot(l['r']))
            f_out.write(f'det(A-lE)={d}\n')
        elif t == reader.EIGENVECTOR:
            S = dan.make_S(M) if S is None else S
            y = dan.get_frob_eigenvec(l['r'], n)
            x = S.dot(y)
            f_out.write('x:\n')
            write_mat(f_out, x)
            f_out.write('eps vector:\n')
            write_mat(f_out, A.dot(x) - x.dot(l['r']))
        f_out.write(f'k={l["k"]}\n')
finally:
    if f_in is not stdin:
        f_in.close()
    if f_out is not stdout:
        f_out.close()
