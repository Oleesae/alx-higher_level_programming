#!/usr/bin/python3
"""A save to json file function"""


import json


def save_to_json_file(my_obj, filename):
    """(object, file object) -> file object

    Writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, 'w+', encoding="utf-8") as f:
        string = json.dumps(my_obj)
        f.write(string)
