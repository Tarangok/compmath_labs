import lab2.seidel as sei

from matrix.norm import vec_eps, norm
import lab2.reader as reader
import matrix.writer as writer

from sys import stdin, stdout
from math import log10, trunc, ceil


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return trunc(stepper * number) / stepper


f_in = open('l2_test_iterative.txt', 'r')
f_out = open('res.txt', 'w')

try:
    task, A, b = reader.read_task(f_in)
    eps = float(f_in.readline())
    precision = ceil(-log10(eps))
    A_t = A.transpose()

    C = A_t.dot(A)
    if not sei.test_diag(C):
        raise ValueError('Matrix not diagonally dominant')
    alpha = sei.make_alpha(C)

    f_out.write('alpha:\n')
    writer.write_mat(f_out, alpha, precision)

    if task == 1:  # решение СЛАУ
        d = A_t.dot(b)
        beta = sei.make_beta(C, d)

        x = sei.solve(alpha, beta, d, eps)
        f_out.write('beta:\n')
        writer.write_mat(f_out, beta, precision)

        f_out.write('x:\n')
        writer.write_mat(f_out, x, precision)

        e = vec_eps(A, x, b)
        n = norm(e)

        f_out.write('eps vec:\n')
        writer.write_mat(f_out, e, precision)
        f_out.write('norm:\n')
        f_out.writelines('{:.{prec}e}\n'.format(n, prec=precision))
    else:
        raise ValueError('Not a SOLE solving task')

finally:
    if f_in != stdin:
        f_in.close()
    if f_out != stdout:
        f_out.close()
