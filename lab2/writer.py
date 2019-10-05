def write_vector(fp, v):
    for e in v:
        fp.write(str(float(e))+' ')
    fp.write('\n')


def write_mat(fp, m):
    for s in m:
        write_vector(fp, s)
