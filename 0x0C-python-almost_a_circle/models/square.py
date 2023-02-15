#!/usr/bin/python3
"""
A square class that inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A definition of the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square object"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints a string representation of the
        Square
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.height)
        return string

    @property
    def size(self):
        """ returns the value of the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """updates the value of the size attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates values of the square object"""

        attrs = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])
