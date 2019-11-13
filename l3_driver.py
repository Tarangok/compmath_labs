import lab3.reader as reader
from sys import stdin, stdout
import lab3.danilevsky as dan
from lab3.aberth import aberth

from matrix.writer import write_mat
from matrix.det import det
from numpy import eye


f_in = open('l3_test.txt', 'r')
f_out = stdout

try:
    eps = 1e-5

    t, A = reader.read_task(f_in)
    n = A.shape[0]

    P, M, _ = dan.danilevsky(A)
    F = dan.make_poly(P)
    L = aberth(F, eps)

    S = None
    write_mat(f_out, P)

    for l in L:
        f_out.write(f'{l}\n')
        if t == reader.EIGENVALUE:
            d = det(A - eye(n).dot(l))
            f_out.write(f'{d}\n')
        elif t == reader.EIGENVECTOR:
            S = dan.make_S(M) if S is None else S
            x = S.dot(dan.get_frob_eigenvec(l, n))
            write_mat(f_out, A.dot(x) - x.dot(l))
finally:
    if f_in is not stdin:
        f_in.close()
    if f_out is not stdout:
        f_out.close()
