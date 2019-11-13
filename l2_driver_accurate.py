from sys import stdin, stdout
from numpy import column_stack, identity

import lab2.reader as reader
import lab2.gauss as gauss
import matrix.norm as norm

from matrix.writer import write_mat

f_in = open('l2_test_accurate.txt', 'r')
f_out = open('res.txt', 'w')


try:
    task, A, b = reader.read_task(f_in)
    A_trg = gauss.gauss_triangle(A)
    if task == 1:
        x, b_res = gauss.solve(A_trg, b)
        e = norm.vec_eps(A, x, b)
        n = norm.norm(e)

        for i, a in enumerate(A_trg):
            if i == 0:
                continue
            f_out.write('A_{}\n'.format(i))
            write_mat(f_out, a)
        for i, b in enumerate(b_res):
            if i == 0:
                continue
            f_out.write('b_{}\n'.format(i))
            write_mat(f_out, b)

        f_out.write('x\n')
        write_mat(f_out, x)
        f_out.write('eps\n')
        write_mat(f_out, e)
        f_out.write('norm\n')
        f_out.write(str(n))
    elif task == 2:
        d = gauss.det(A_trg)
        f_out.write(str(d))
    elif task == 3:
        inv, es = gauss.inverse(A_trg)
        for i, e in enumerate(es):
            f_out.write('e_{}\n'.format(i+1))
            write_mat(f_out, e)
        inv_mat = column_stack(tuple(inv))
        f_out.write('A^(-1)\n')
        write_mat(f_out, inv_mat)
        f_out.write('eps\n')
        e = A.dot(inv_mat) - identity(A.shape[0])
        write_mat(f_out, e)
        f_out.write('norm\n')
        f_out.write(str(eps.norm(e)))
    f_out.write('\n')
finally:
    if f_in != stdin:
        f_in.close()
    if f_out != stdout:
        f_out.close()
