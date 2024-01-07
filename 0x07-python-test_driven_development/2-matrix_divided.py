#!/usr/bin/python3
"""defines a function to divide elements in a matrix"""


def matrix_divided(matrix, div):
    """divides a mtrix by a number div"""
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(errorMessage)
        for element in row:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError(errorMessage)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(errorMessage)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
