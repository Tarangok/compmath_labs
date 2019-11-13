import lab2.gauss as gauss


def det(A):
    return gauss.det(gauss.gauss_triangle(A))
