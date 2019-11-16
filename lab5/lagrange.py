from interp.grid import EquilateralGrid
from functools import reduce
from operator import mul
from math import factorial


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

        def d2(x):
            res = 0.0
            for i, c in enumerate(self.C):
                p = 0.0
                for j in range(len(self.C)):
                    if j != i:
                        p += sum(self.phi(x, i, j, k)
                                 for k in range(len(self.C))
                                 if k != i and k != j)
                res += c * p
            return res

        ders = [d0, d1, d2]
        try:
            return ders[der](x)
        except IndexError:
            raise ValueError(f'Derivative {der} not supported')


class LagrangePolynomialE:
    '''Полином Лагранжа на равномерной сетке'''
    def __init__(self, a, b, n, Y):
        def coeff(bc, i):
            return (-1) ** (n-i) * Y[i] / bc

        i = 0
        ifac = 1
        nfac = factorial(n)

        self.coeffs = []
        while i <= n:
            self.coeffs.append(coeff(ifac*nfac, i))
            ifac *= i+1
            if n != i:
                nfac /= (n-i)
            i += 1
        self.step = (b-a) / n
        self.initial = a

    def phi(self, q, *excluded):
        gen = (q - j for j in range(len(self.coeffs)) if j not in excluded)
        return product(gen)

    def __call__(self, x, der=0):
        def d0(q):
            return sum(c * self.phi(q, i) for i, c in enumerate(self.coeffs))

        def d1(q):
            res = 0.0
            for i, c in enumerate(self.coeffs):
                p = sum(self.phi(q, i, j)
                        for j in range(len(self.coeffs))
                        if i != j)
                res += c * p
            return res / self.step

        def d2(q):
            res = 0.0
            for i, c in enumerate(self.C):
                p = 0.0
                for j in range(len(self.C)):
                    if j != i:
                        p += sum(self.phi(q, i, j, k)
                                 for k in range(len(self.C))
                                 if k != i and k != j)
                res += c * p
            return res / (self.step * self.step)

        q = (x - self.initial)/self.step

        ders = [d0, d1, d2]
        try:
            return ders[der](q)
        except IndexError:
            raise ValueError(f'Derivative {der} not supported')
