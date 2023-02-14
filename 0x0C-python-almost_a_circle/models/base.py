#!/usr/bin/python3
"""
Base class

Manages id attribute
"""


class Base:
    """ A Base class managing the number
    of object instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
