#!/usr/bin/python3
"""
A Base Geometry module

"""


class BaseGeometry(object):
    """ Defines a BaseGeometry class """

    def __init__(self):
        """ Initializes an instance """
        super().__init__()

    def area(self):
        """ defines an area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value to be an integer
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
