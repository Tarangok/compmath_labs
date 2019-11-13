from functions.scalar import ScalarFunction


class AnalyticalFunction:
    def __init__(self, f_str: str, grid):
        self.f = ScalarFunction(f_str)
        self.x = grid

    def __getitem__(self, i):
        return self.f(self.x[i])

    def __len__(self):
        return len(self.x)


class GridFunction:
    def __init__(self, y_seq):
        self.f = y_seq

    def __getitem__(self, i):
        return self.f[i]

    def __len__(self):
        return len(self.f)
