#!/usr/bin/python3
"""
This module contain a function that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def binomialCoeff(n, k):
    """
    function to calculate Binomial Coefficient C(n, k).

    Args:
        n (int): first parameter
        k (int): second parameter

    Returns:
        res (int) Binomial Coefficient
    """
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def pascal_triangle(n):
    """
    function that represente the Pascal’s triangle of n

    Args:
        n (int): number

    Returns:
        p_list (list[list]): Pascal's Triangle
    """
    p_list = []
    for line in range(0, n):
        e_list = []
        for i in range(0, line + 1):
            e_list.append(binomialCoeff(line, i))
        p_list.append(e_list)
    return p_list
