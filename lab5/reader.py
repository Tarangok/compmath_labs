from typing import TextIO
from interp.grid import EquilateralGrid, NonequilateralGrid
from lab5.lagrange import make_eq_grid
from functions.scalar import ScalarFunction


def read_task(fp: TextIO):
    der = int(fp.readline())
    n = int(fp.readline())

    grid_type = fp.readline()[:1]
    if grid_type == 'e':
        a, b = tuple(float(r) for r in fp.readline().split(' '))
        grid = make_eq_grid(a, b, n)
    elif grid_type == 'n':
        X = [float(r) for r in fp.readline().split(' ')]
        if len(X) != n+1:
            raise ValueError(f'Grid not of length {n+1}')
        grid = NonequilateralGrid(X)
    else:
        raise ValueError('Unrecognized task type')

    Y = [float(r) for r in fp.readline().split(' ')]
    m = int(fp.readline())  # не исп.
    Xres = [float(r) for r in fp.readline().split(' ')]
    if len(Xres) != m:
        raise ValueError(f'Res grid not of length {m}')
    f = fp.readline()
    F = ScalarFunction(f) if f != '' else None

    return grid, Y, Xres, F, der
