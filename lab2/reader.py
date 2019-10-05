from typing import TextIO
import numpy as np


def read_task(fp: TextIO):
    task_type = int(fp.readline())
    size = int(fp.readline())

    A = np.ndarray((size, size))
    if task_type == 1:
        b = np.ndarray(size)
    else:
        b = None

    for i in range(size):
        numbers = fp.readline().split()
        for j in range(size):
            A[i, j] = float(numbers[j])
        if task_type == 1:
            b[i] = float(numbers[size])

    return task_type, A, b
