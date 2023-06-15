#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx = matrix[:].copy()
    for i in range(len(mx)):
        mx[i] = list(map(lambda x: x*x, mx[i]))
    return mx
