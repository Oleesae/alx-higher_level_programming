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
            return "[]"

        j_str = json.dumps(list_dictionaries)
        return j_str

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string repersentation
        of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w+', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""
        if json_string is None or json_string == "":
            return []
        j_list = json.loads(json_string)
        return j_list
