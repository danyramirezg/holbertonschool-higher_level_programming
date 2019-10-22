#!/usr/bin/python3

from models.base import Base

"""Class Rectangle that inherits from Base"""


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create constructor init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set the property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the widht"""
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Set the getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Set the property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Set the property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) == int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.height * self.width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.y, end="")
        for col in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Method that returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Method to update"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Method dictionary"""
        dicti = {'id': self.id, 'width': self.width, 'height': self.height,
                 'x': self.x, 'y': self.y}
        return dicti
