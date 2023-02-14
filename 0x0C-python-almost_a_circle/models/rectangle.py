#!/usr/bin/python3
"""A rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """
    A Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an object instance """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns the value of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """updates the value of the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """updates the value of the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """updates the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """updates the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints the shape of the rectangle
        with the `#` character
        """

        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i != self.__height - 1:
                string += "\n"
        print(string)

    def __str__(self):
        """
        Prints a string representation of the
        Rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.__y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return string
