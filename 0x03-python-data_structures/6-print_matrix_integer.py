#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for alist in [[c for c in r] for r in matrix]:
            for n in alist[:-1]:
                print('{}'.format(n), end=' ')
            print('{}'.format(n + 1))
    else:
        print()
