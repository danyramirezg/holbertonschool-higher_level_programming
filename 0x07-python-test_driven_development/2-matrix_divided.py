#!/usr/bin/python3
def matrix_divided(matrix, div):
    if matrix is not int or matrix is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
