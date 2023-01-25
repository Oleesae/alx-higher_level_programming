#!/usr/bin/python3
"""A Square class."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """
        Instantiates a square

        Args:
            size: size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Private instance setter

        Args:
            value: size of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
