#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Creates a Square class"""
    def __init__(self, size=0):
        """Initializes Square"""
        self._size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

