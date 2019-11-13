from lab5.lagrange import LagrangePolynomialN
from lab5.reader import read_task

from interp.grid import EquilateralGrid, NonequilateralGrid
from interp.function import GridFunction

from sys import stdin, stdout
from math import sqrt


f_in = open('lab5/l5_test.txt', 'r')
f_out = stdout

try:
    X, Y, Xr, F, der = read_task(f_in)
    L = LagrangePolynomialN(X, Y)
    Yr = [L(xr, der) for xr in Xr]

    for x, y in zip(Xr, Yr):
        f_out.write(f'{x} {y}\n')

    if F is not None:
        std = sum(sqrt((F(x)-L(x)) ** 2) for x in X)  # или Xr
        f_out.writelines(f'{std}\n')
finally:
    if f_in is not stdin:
        f_in.close()
    if f_out is not stdout:
        f_out.close()
