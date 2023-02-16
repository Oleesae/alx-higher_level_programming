#!/usr/bin/python3
"""
Base class

Manages id attribute
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a list string representation of a
        dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            j_str = json.dumps([])

        j_str = json.dumps(list_dictionaries)
        return j_str
