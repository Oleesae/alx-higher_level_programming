#!/usr/bin/python3
"""Object file to json function"""


import json


def load_from_json_file(filename):
    """file object -> json object

    Creates an Object from a JSON file
    """

    with open(filename, 'r+', encoding="utf-8") as f:
        string = f.read()
        obj = json.loads(string)
        return obj
