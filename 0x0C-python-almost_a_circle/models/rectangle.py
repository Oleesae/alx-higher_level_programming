#!/usr/bin/python3
"""A rectangle Class"""
Base = __import__('base').Base


class Rectangle(Base):
    """
    A Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an object instance """

        super().__init__()
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
        self.__width = value

    @property
    def height(self):
        """returns the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """updates the value of the height attribute"""
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """updates the value of x"""
        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """updates the value of y"""
        self.__y = value
