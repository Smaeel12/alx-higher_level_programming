#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(
            map(lambda elist:
                list(map(lambda v: pow(v, 2), elist)), matrix))
