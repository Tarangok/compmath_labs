from lab2.seidel import seidel_norm
from lab2.eps import vec_eps, norm
import lab2.reader as reader
import lab2.writer as writer

from sys import stdin, stdout
from math import log10, trunc, ceil


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return trunc(stepper * number) / stepper


f_in = open('l2_test_iterative.txt', 'r')
f_out = open('res.txt', 'w')

try:
    task, A, b = reader.read_task(f_in)
    if task != 1:  # не решение СЛАУ
        raise ValueError('Not a SOLE solving task!')

    eps = float(f_in.readline())
    precision = ceil(-log10(eps))
    alpha, beta, x = seidel_norm(A, b, eps)

    f_out.write('alpha:\n')
    writer.write_mat(f_out, alpha, precision)
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
finally:
    if f_in != stdin:
        f_in.close()
    if f_out != stdout:
        f_out.close()
