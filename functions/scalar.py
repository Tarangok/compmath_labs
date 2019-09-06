from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        implicit_application,
                                        implicit_multiplication,
                                        split_symbols)
from sympy.abc import *
from math import exp

class ScalarFunction:
    """Класс, инкапсулирующий вычисление скалярной функции, заданной в виде строки
определенного формата"""
    def __init__(self, expr):
        # преобразования для парсера sympy
        transformations = standard_transformations + (implicit_multiplication, # умножение без знака умножения
                                                      implicit_application,) # применение скалярных ф-ий без скобок
        
        expr = expr.replace('e', 'E')
        expr = expr.replace('tg', 'tan')
        expr = expr.replace('ctg', 'cot')
        expr = expr.replace('^', '**')

        self.fun = parse_expr(expr,
                              transformations = transformations)
        if self.fun.free_symbols - {x} != set():
            raise ValueError('Выражение содержит переменные кроме x')
        
    def __call__(self, arg):
        return float(self.fun.subs({x : arg}))
