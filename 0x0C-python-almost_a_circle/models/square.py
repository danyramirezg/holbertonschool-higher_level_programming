#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Call the super class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The getter function"""
        return self.width

    @size.setter
    def size(self, value):
        """The setter function for the size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def __str__(self):
        """The overloading __str__ method """

        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the class Square by adding the
         public method"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        dic2 = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic2






