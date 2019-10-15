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
