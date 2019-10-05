#!/usr/bin/python3
def matrix_divided(matrix, div):
    new = []

    if matrix is None:
        return None

    """for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in matrix:
            if type(i) is not int or type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if matrix[0] != matrix[i]:
            raise TypeError("TypeError exception with the message Each row of the matrix must have the same size")
    if div == 0:
        raise TypeError("ZeroDivisionError")
    if type(div) is not int and type(div) is not float:
        raise TypeError("Each row of the matrix must have the same size")"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix)):
        if type(matrix[row]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in range(len(matrix[row])):
            if type(matrix[row][i]) is not int and type(matrix[row][i]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for d in matrix:
        new.append(list(map(lambda x: round(x / div, 2), d)))
    return new

