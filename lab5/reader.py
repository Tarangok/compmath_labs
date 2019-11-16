from typing import TextIO
from interp.grid import EquilateralGrid, NonequilateralGrid
from lab5.lagrange import make_eq_grid
from functions.scalar import ScalarFunction


def read_task(fp: TextIO):
    der = int(fp.readline())
    n = int(fp.readline())

    t = fp.readline()[:1]
    if t == 'e':
        a, b = tuple(float(r) for r in fp.readline().split(' '))
        X = (a, b, n)
    elif t == 'n':
        X = [float(r) for r in fp.readline().split(' ')]
        if len(X) != n+1:
            raise ValueError(f'Grid not of length {n+1}')
    else:
        raise ValueError('Unrecognized task type')

    Y = [float(r) for r in fp.readline().split(' ')]
    m = int(fp.readline())  # не исп.
    Xres = [float(r) for r in fp.readline().split(' ')]
    if len(Xres) != m:
        raise ValueError(f'Res grid not of length {m}')
    f = fp.readline()
    F = ScalarFunction(f) if f != '' else None

    return t, X, Y, Xres, F, der
