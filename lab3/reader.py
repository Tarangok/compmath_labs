from typing import TextIO
import numpy as np


EIGENVALUE = 1
EIGENVECTOR = 2


def read_task(fp: TextIO):
    t = int(fp.readline())
    if not (0 < t < 3):
        raise ValueError('Incorrect task type')

    n = int(fp.readline())

    A = np.ndarray((n, n))

    for i in range(n):
        numbers = fp.readline().split()
        for j in range(n):
            A[i, j] = float(numbers[j])

    return t, A
