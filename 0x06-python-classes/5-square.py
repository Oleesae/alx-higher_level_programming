#!/usr/bin/pythona3
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


    def my_print(self):
        """
        Prints a square
        """

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
                j += 1
            i += 1
            print()
