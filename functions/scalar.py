import sympy
from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        implicit_application,
                                        implicit_multiplication,
                                        convert_xor,
                                        function_exponentiation)
from sympy.abc import x
from math import log10, e

class ScalarFunction:
    """Класс, инкапсулирующий вычисление скалярной функции, заданной в виде строки
определенного формата"""
    def __init__(self, expr):
        # преобразования для парсера sympy
        transformations = standard_transformations + (implicit_multiplication, # умножение без знака умножения
                                                      implicit_application,  # применение скалярных ф-ий без скобок
                                                      convert_xor,
                                                      function_exponentiation) # каретка как символ возведения в степень
        # замены для парсера
        replacers = {'e' : e,
                     'tg' : sympy.functions.tan,
                     'ctg' : sympy.functions.cot,
                     'lg' : sympy.Lambda(x, sympy.functions.log(x) / sympy.functions.log(10))}
        
        expr = expr.lower()
        
        self.fun = parse_expr(expr,
                              transformations = transformations,
                              local_dict=replacers)
        if self.fun.free_symbols - {x} != set():
            raise ValueError('Выражение содержит переменные кроме x')
        
    def __call__(self, arg, deriv=0):
        res = self.fun if deriv == 0 else self.fun.diff(*(x for i in range(0, deriv)))
        return float(res.subs({x : arg}))
