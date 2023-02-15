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

