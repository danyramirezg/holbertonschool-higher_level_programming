#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Creates a Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square"""
        self.__size = size
        try:
            self.position = position
        except TypeError as err:
            print(err)
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
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
