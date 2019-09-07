from math import sqrt
def golden(f, a, b, eps):
    phi = (sqrt(5)+1) / 2

    d = a + (b-a)/phi
    c = b - d + a

    x = (a+b)/2

    while abs(f(x)) > eps or abs((b-a)/2) > eps:
        if f(a)*f(d) <= 0:
            b = d
        else:
            a = c
            
        d = a + (b-a)/phi
        c = b - d + a
        
        x = (a+b) / 2
    return x, abs((b-a)/2), abs(f(x))
