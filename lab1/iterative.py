def iterative(f, a, b, eps):
    def extreme(f, a, b):
        return max(abs(f(a, 1)), abs(f(b, 1)))

    def phi(f, a, b, m):
        return lambda x: (x - f(x) / m)

    p = phi(f, a, b, extreme(f, a, b))

    x = (a + b) / 2
    xn = p(x)

    while abs(x - xn) > eps or abs(f(xn)) > eps:
        x = xn
        xn = p(x)

    return xn, abs(x - xn), abs(f(xn))
