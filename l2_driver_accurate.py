from sys import stdin, stdout
from numpy import column_stack

import lab2.reader as reader
import lab2.gauss as gauss
import lab2.eps as eps

from lab2.writer import write_mat, write_vector

f_in = open('l2_test.txt', 'r')
f_out = stdout


try:
    task, A, b = reader.read_task(f_in)
    A_trg = gauss.gauss_triangle(A)
    if task == 1:
        x, b_res = gauss.solve(A_trg, b)
        e = eps.vec_eps(A, x, b)
        n = eps.norm(e)

        for i, a in enumerate(A_trg):
            if i == 0:
                continue
            f_out.write('A_{}\n'.format(i))
            write_mat(f_out, a)
        for i, b in enumerate(b_res):
            if i == 0:
                continue
            f_out.write('b_{}\n'.format(i))
            write_vector(f_out, b)

        write_vector(f_out, x)
        write_vector(f_out, e)
        f_out.write(str(n))
    elif task == 2:
        d = gauss.det(A_trg)
        f_out.write(str(d))
    elif task == 3:
        inv = gauss.inverse(A_trg)
        for i, inv_v in enumerate(inv):
            f_out.write('e_{}\n'.format(i+1))
            write_vector(f_out, inv_v)
        inv_mat = column_stack(tuple(inv))
        write_mat(f_out, inv_mat)
    f_out.write('\n')
finally:
    if f_in != stdin:
        f_in.close()
    if f_out != stdout:
        f_out.close()
