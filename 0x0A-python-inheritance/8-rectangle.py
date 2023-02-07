#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle class
    
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
