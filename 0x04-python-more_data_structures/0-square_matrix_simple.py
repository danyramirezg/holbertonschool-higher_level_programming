#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new = []
        for j in i:
            new.append(j ** 2)
        new_matrix.append(new)
    return new_matrix
