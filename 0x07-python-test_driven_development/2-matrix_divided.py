#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""

    if not all(isinstance(rw, list) for rw in matrix) or \
            not all(isinstance(n, (int, float)) for rw in matrix for n in rw):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    check_len = set(len(rw) for rw in matrix)
    if len(check_len) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(n / div, 2) for n in rw] for rw in matrix]

    return new_matrix
