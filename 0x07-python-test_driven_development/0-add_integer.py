#!/usr/bin/python3

"""Function that adds 2 integers"""
import math


def add_integer(a, b=89):
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer or b must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer or b must be an integer")
    if type(a) is float:
        a = math.floor(float)
    elif type(b) is float:
        b = math.floor(float)

    return a + b
