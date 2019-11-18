from lab5.lagrange import LagrangePolynomialN, LagrangePolynomialE
from lab5.reader import read_task

from sys import stdin, stdout
from math import sqrt


print('Pick test file\n1-equilat grid\n2-nonequilat grid\n')
choice = int(input())

if not 0 < choice < 3:
    raise ValueError('bad choice')

files = ['lab5/l5_test_eq.txt', 'lab5/l5_test_neq.txt']

f_in = open(files[choice-1], 'r')
f_out = open('res.txt', 'w')


try:
    t, X, Y, Xr, F, der = read_task(f_in)
    if t == 'n':
        L = LagrangePolynomialN(X, Y)
    else:
        L = LagrangePolynomialE(*X, Y)
    Yr = [L(xr, der) for xr in Xr]

    for x, y in zip(Xr, Yr):
        f_out.write(f'{x} {y}\n')

    if F is not None:
        std = sum(sqrt((F(x)-L(x)) ** 2) for x in Xr)  # или Xr
        f_out.writelines(f'{std}\n')
finally:
    if f_in is not stdin:
        f_in.close()
    if f_out is not stdout:
        f_out.close()
