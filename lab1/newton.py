def newton(f, a, b, eps):
    def phi(f, x):
        return x - f(x) / f(x, 1)

    if f(a) * f(a, 2) > 0:
        x = a
    elif f(b) * f(b, 2) > 0:
        x = b
    else:
        c = a - f(a) * (b - a) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            x = a
        else:
            x = b

    xn = phi(f, x)
    while abs(xn - x) >= eps or abs(f(xn)) >= eps:
        x = xn
        xn = phi(f, x)

    return xn, abs(xn - x), abs(f(xn))
