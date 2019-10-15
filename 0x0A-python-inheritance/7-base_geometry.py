#!/usr/bin/python3

""""class BaseGeometry"""


class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    """Public instance method: def integer_validator(self, name, value):
     that validates value"""

    def integer_validator(self, name, value):

        if value is not int:
            raise TypeError(name, "must be an integer")
        if value <= 0:
            raise ValueError(name, "must be greater than 0")
