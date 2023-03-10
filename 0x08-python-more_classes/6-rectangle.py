#!/usr/bin/python3
"""
A Rectangle Class
"""


class Rectangle:
    """
    Defines a Rectangle Object
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialization of an object

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates the area
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints the Rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for w in range(self.__height):
            for h in range(self.__width):
                string += "#"
            if w != self.__height - 1:
                string += "\n"

        return string

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
