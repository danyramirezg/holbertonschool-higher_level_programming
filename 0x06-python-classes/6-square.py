#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Creates a Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square"""
        self.size = size
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
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
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
        if self.position:
            if self.size > 0:
                print('\n' * self.position[1], end="")
                for i in range(self.__size):
                    print('' * self.position[0], end="")
                    print("#" * self.size)
        if self.__size == 0:
            print("")
