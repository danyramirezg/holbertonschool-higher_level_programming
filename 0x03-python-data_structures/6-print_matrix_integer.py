#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and any(matrix) is False:
        print()
    for i in matrix:
        result = 0
        for x in i:
            if result == len(i) - 1:
                print("{:d}".format(x), end="")
                print()
            else:
                print("{}".format(x), end="")
            result += 1
