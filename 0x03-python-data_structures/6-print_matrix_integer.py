#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx1 in range(len(matrix)):
        for idx2 in range(len(matrix[idx1])):
            print("{:d}".format(matrix[idx1][idx2]), end="")
            if idx2 != len(matrix[idx1]) - 1:
                print(" ", end="")
        print()
