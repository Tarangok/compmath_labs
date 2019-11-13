from interp.grid import EquilateralGrid
from functools import reduce
from operator import mul


def make_eq_grid(a, b, n):
    return EquilateralGrid(a, (b-a)/n, n+1)


def product(S):
    '''Произведение чисел в последовательности S'''
    return reduce(mul, S, 1.0)


class LagrangePolynomialN:
    '''Класс объекта полинома Лагранжа на неравномерной сетке'''
    def __init__(self, X, Y):
        '''X - табличные значения x,
        Y - табличные значения функции'''
        def coeff(i):
            # вычисляет коэффициенты полинома
            xdiffs = [X[i] - X[j] for j in range(len(X)) if i != j]
            return Y[i] / product(xdiffs)
        self.X = X
        self.C = [coeff(i) for i in range(len(Y))]

    # вычисляет функции полинома
    def phi(self, x, *excluded):
        gen = (x - self.X[j] for j in range(len(self.X)) if j not in excluded)
        return product(gen)

    # вычисляет значение полинома или его производных (1, 2)
    def __call__(self, x, der=0):
        def d0(x):
            return sum(c * self.phi(x, i) for i, c in enumerate(self.C))

        def d1(x):
            res = 0.0
            for i, c in enumerate(self.C):
                p = sum(self.phi(x, i, j)
                        for j in range(len(self.C))
                        if j != i)
                res += c * p
            return res

        ders = [d0, d1]
        try:
            return ders[der](x)
        except KeyError:
            raise ValueError(f'Derivative {der} not supported')
