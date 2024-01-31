#!/usr/bin/python3
""" This module contain a function that multiplies 2 matrices by using
        the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices by using the module NumPy

    Args:
        m_a(list[list[int, float]]): First matrix.
        m_b(list[list[int, float]]): Second matrix.

    Returns:
        The product of two matricies
    """

    return numpy.matmul(m_a, m_b)
