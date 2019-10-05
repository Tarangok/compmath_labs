from math import inf


def secant(f, a, b, eps):
    def divisor(a, b):
        fa = f(a)
        fb = f(b)
        return (a*fb - b*fa) / (fb - fa)

    prev = inf
    cur = divisor(a, b)
    fc = f(cur)
    while abs(fc) >= eps or abs(cur - prev) >= eps:
        if f(a)*fc <= 0:
            b = cur
        elif f(b)*fc <= 0:
            a = cur
        else:
            break  # fc ~= 0
        prev = cur
        cur = divisor(a, b)
        if prev-cur == 0.0:
            break
        fc = f(cur)
    return cur, abs(cur-prev), abs(fc)
