import numpy as np


def write_mat(fp, m, prec=9):
    np.savetxt(fp, m, fmt='%0.{}e'.format(prec))
