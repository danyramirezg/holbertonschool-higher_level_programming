#!/usr/bin/python3

"""function that prints a square
with the character #
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float:
        raise TypeError("size must be an integer")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
