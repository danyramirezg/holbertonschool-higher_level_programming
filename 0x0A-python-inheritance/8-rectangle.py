#!/usr/bin/python3


""""class BaseGeometry"""


class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    """Public instance method: def integer_validator(self, name, value):
     that validates value"""

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
