def combo(f, a, b, eps):
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

    while abs((b-a)/2) >= eps or abs(f(x)) >= eps:
        c = a - f(a) * (b-a) / (f(b) - f(a))
        if f(a) * f(a, 2) > 0:
            a = a - f(a)/f(a, 1)
            b = c
        else:
            a = c
            b = b - f(b)/f(b, 1)
        x = (a+b)/2

    return x, abs((b-a)/2), abs(f(x))
