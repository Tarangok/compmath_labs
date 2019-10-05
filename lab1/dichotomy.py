def dichotomy(f, a, b, eps):
    x = (a+b)/2
    while abs(f(x)) >= eps or abs((b-a)/2) >= eps:
        if f(a)*f(x) <= 0:
            b = x
        else:
            a = x
        x = (a+b)/2
    return x, abs((b-a)/2), abs(f(x))
