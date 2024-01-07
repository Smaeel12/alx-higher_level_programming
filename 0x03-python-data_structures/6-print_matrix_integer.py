#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for alist in matrix:
        for n in alist:
            print('{:d}'.format(n), end='')
            if n != alist[-1]:
                print(' '.format(), end='')
        print()
