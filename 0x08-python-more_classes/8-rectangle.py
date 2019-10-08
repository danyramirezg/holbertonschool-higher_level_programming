#!/usr/bin/python3

"""class Rectangle that defines
a rectangle """


class Rectangle:
    """Public class attribute
     (Initialized to 0): """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

        """Attribute Incremented during each
        new instance instantiation: """

        Rectangle.number_of_instances += 1

    """Print() and str() should print the rectangle
    with the character # """

    def __str__(self):

        """If width or height is equal to 0, return an empty string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for row in range(self.__height):
                for j in range(self.height - 1):
                    print(str(self.print_symbol) * self.__width)
                return str(self.print_symbol) * self.width

    """Static method def bigger_or_equal(rect_1, rect_2): that returns the
    biggest rectangle based on the area"""

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    """return an empty string repr() should return a string representation of
     the rectangle to be able to recreate a new instance by
     using eval()"""

    def __repr__(self):

        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """Public instance method that returns the rectangle area"""

    def area(self):

        area = self.__width * self.__height
        return area

    """Public instance method that returns the perimeter area"""

    def perimeter(self):

        if self.width == 0 or self.height == 0:
            return 0
        else:
            perimeter = (self.__width * 2) + (self.__height * 2)
            return perimeter

    """Print the message 'Bye rectangle...'
        when an instance of Rectangle is deleted"""

    def __del__(self):

        """Attribute Decremented during
         each instance deletion"""

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
