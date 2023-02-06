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
