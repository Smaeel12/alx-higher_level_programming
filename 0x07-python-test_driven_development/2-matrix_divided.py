#!/usr/bin/python3
""" This module contain a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix_divided function that divides all elements of a matrix.

    Args:
        matrix(list[list[int, float]]): a matrix.
        div(int): a number (integer or float).

    Raises:
        TypeError: Exception if matrix is not (list of lists)
            of integers/float.
        TypeError: Exception if div is not a number.
        ZeroDivisionError: Exception if division by zero.

    Returns:
        (list of lists) of integers/float: returns a new matrix.
    """

    if type(div) not in [int, float] or div != div\
            or abs(div) > 1.7976931348623158e+308:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif isinstance(matrix, list) and type(div) in (int, float) and div != 0:
        new_matrix = [alist.copy() for alist in matrix]
        size = -1
        for elist in new_matrix:
            if (size == -1):
                size = len(elist)
            else:
                if size != len(elist):
                    raise TypeError("Each row of the matrix must have \
the same size")
            if isinstance(elist, list):
                for idx, num in enumerate(elist):
                    if type(num) in (int, float) and num == num\
                            and abs(num) <= 1.7976931348623158e+308:
                        elist[idx] = round(num / div, 2)
                    else:
                        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            else:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    return new_matrix
