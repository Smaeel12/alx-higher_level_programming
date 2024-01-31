#!/usr/bin/python3
""" This module contain function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices

    Args:
        m_a(list[list[int, float]]): First matrix.
        m_b(list[list[int, float]]): Second matrix.

    Raises:
        TypeError: Exception if one of the matrices is not (list of lists)
            of integers/float.
        TypeError: Exception if one of the matrices is not a rectangle
            (all ‘rows’ should be of the same size)
        ValueError: if one of the matrices empty
        ValueError: if m_a and m_b can't be multiplied
        ZeroDivisionError: Exception if division by zero.

    Return:
        The product of two matricies
    """
    # Check the m_b m_b
    if type(m_a) is list:
        if len(m_a) == 0:
            raise ValueError("m_a can't be empty")
        for row in m_a:
            if type(row) is list:
                if len(row) == 0:
                    raise ValueError("m_a can't be empty")
                else:
                    for elist in row:
                        if type(elist) not in [int, float]:
                            raise TypeError("m_a should contain only integers\
                                    or floats")
            elif type(row) is not list:
                raise TypeError("m_a must be a list of lists")
            elif len(row) == 0:
                raise ValueError("m_a can't be empty")
            if len(row) != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")
    else:
        raise TypeError("m_a must be a list")

    # Check the m_b m_b
    if type(m_b) is list:
        if len(m_b) == 0:
            raise ValueError(m_b + " can't be empty")
        for row in m_b:
            if type(row) is list:
                if len(row) == 0:
                    raise ValueError("m_b can't be empty")
                else:
                    for ele in row:
                        if type(ele) not in [int, float]:
                            raise TypeError("m_b should contain only" +
                                            " integers or floats")
            elif type(row) is not list:
                raise TypeError("m_b must be a list of lists")
            elif len(row) == 0:
                raise ValueError("m_b can't be empty")
            if len(row) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
    else:
        raise TypeError("m_b must be a list")

    col_a = len(m_a[0])
    row_b = len(m_b)

    if col_a == row_b:
        rows = len(m_a)
        cols = len(m_b[0])
        result_mat = []
        for i in range(rows):
            fil = []
            for j in range(cols):
                fil.append(0)
            result_mat.append(fil)
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result_mat[i][j] += m_a[i][k] * m_b[k][j]
        return result_mat
    else:
        raise ValueError("m_a and m_b can't be multiplied")
