from math import inf

def dichotomy(f, a, b, eps):
    c = (a+b)/2
    while abs(f(c)) > eps or (b-a)/2 > eps:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
    x = (b+a)/2
    return x, abs((b-a)/2), abs(f(x))
