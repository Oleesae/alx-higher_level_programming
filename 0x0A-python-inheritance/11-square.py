#!/usr/bin/python3
"""
A Square class derived from A Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a Square with a Rectangle parent class
    """

    def __init__(self, size):
        """ Initializes an instance of a Square object
        with Rectangle attributes
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
