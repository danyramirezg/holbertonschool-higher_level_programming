#!/usr/bin/python3
"""Function that adds 2 integers
a and b must be integers or floats,
otherwise raise a TypeError

"""


def add_integer(a, b=98):
    """
     a and b must be first casted to integers if they are float
    """
    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
