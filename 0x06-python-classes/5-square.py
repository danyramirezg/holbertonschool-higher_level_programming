#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Creates a Square class"""

    def __init__(self, size=0):
        """Initializes Square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        area = self.__size * self.__size

        return area

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
