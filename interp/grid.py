from copy import copy


class EquilateralGrid:
    def __init__(self, start, step, size):
        self.start = start
        self.step = step
        self.size = size

    def __getitem__(self, i):
        if 0 <= i < self.size:
            x0 = self.start
            h = self.step
            return x0 + i * h
        else:
            raise IndexError('Grid index out of bounds')

    def __len__(self):
        return self.size + 1


class NonequilateralGrid:
    def __init__(self, seq):
        self.vals = copy(seq)

    def __getitem__(self, i):
        try:
            return self.vals[i]
        except IndexError:
            raise IndexError('Grid index out of bounds')

    def __len__(self):
        return len(self.vals)
