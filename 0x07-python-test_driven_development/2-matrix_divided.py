#!/usr/bin/python3
"""defines function that divides a matrix"""

def matrix_divided(matrix, div):
    """ Divide a matrix by a number div, rounded to two decimal places """
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"
    div_error = "div must be a number"
    zero_div_error = "division by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) is not int and type(div) is not float:
        raise TypeError(div_error)
    if div is 0:
        raise ZeroDivisionError(zero_div_error)
    size = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(list_error)
        if len(row) != size:
            raise TypeError(size_error)
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(list_error)
            result = element / div
            new_list.append(round(result, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix

