#!/usr/bin/python3

""" function that divides
all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists
    of integers/floats
    Returns a new matrix
    """

    new = []

    # if matrix is None:
    #   return None
    if matrix == [] or matrix == [[]]:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix)):
        if type(matrix[row]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for i in range(len(matrix[row])):
            if type(matrix[row][i]) is not int and type(
                    matrix[row][i]) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")
    for d in matrix:
        new.append(list(map(lambda x: round(x / div, 2), d)))
    return new
