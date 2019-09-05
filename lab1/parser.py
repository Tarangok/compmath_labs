from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        implicit_application,
                                        implicit_multiplication)
from sympy.abc import x

class Function:
    def __init__(self, expr):
        transformations = standard_transformations + (implicit_application,
                                                      implicit_multiplication)
        self.fun = parse_expr(expr.replace('^', '**'),
        transformations=transformations)

    def __call__(self, arg):
        return float(self.fun.subs({x : arg}))
