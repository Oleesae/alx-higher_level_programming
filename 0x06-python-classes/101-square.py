#!/usr/bin/python3
"""A Square class."""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates a square

        Args:
            size: size of the square
            position: position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        size value setter

        Args:
            value: size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        """
        position value setter

        Args:
            value: tuples indicating position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        Prints a square
        """

        string = ""
        if self.__size == 0:
            return string

        for i in range(self.__position[1]):
            string += '\n'

        for i in range(self.__size):
            for a in range(self.__position[0]):
                string += " "
            for x in range(self.__size):
                string += "#"
            if i != self.__size - 1:
                string += "\n"

        return string

    def __str__(self):
        return self.my_print()
