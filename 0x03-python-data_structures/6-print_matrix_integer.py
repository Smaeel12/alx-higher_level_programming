#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for alist in matrix:
        for n in alist:
            print(n, end='')
            if n != alist[-1]:
                print(end=' ')
        print()
