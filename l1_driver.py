from lab1.dichotomy import dichotomy
from lab1.golden import golden
from lab1.newton import newton
from lab1.iterative import iterative
from lab1.secant import secant
from lab1.combo import combo

from functions.scalar import ScalarFunction
from sys import stdin, stdout
from math import log10, ceil, trunc


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return trunc(stepper * number) / stepper


methods = [dichotomy, secant, golden, newton, iterative, combo]


try:
    f_in = open('in.txt')
    f_out = open('res.txt', 'w')

    choice = int(f_in.readline()) - 1
    f = ScalarFunction(f_in.readline())
    a, b = tuple(float(i) for i in f_in.readline().split())
    eps = float(f_in.readline())

    if f(a)*f(b) > 0:
        raise ValueError('Неподходящий промежуток')

    precision = ceil(-log10(eps))

    if methods[choice] is None:
        raise NotImplementedError('Метод не реализован')

    x, darg, df = methods[choice](f, a, b, eps)
    f_out.writelines('{:.{prec}f}\n'.format(truncate(x, precision),
                                            prec=precision))
    f_out.writelines('{:.{prec}e}\n'.format(darg, prec=precision))
    f_out.writelines('{:.{prec}f}\n'.format(truncate(df, precision),
                                            prec=precision))
finally:
    if f_in != stdin:
        f_in.close()
    if f_out != stdout:
        f_out.close()
