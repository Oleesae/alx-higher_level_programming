#!/usr/bin/python3
""" Converts JSON string to Object """


import json


def from_json_string(my_str):
    """str -> object

    Returns an object(Python data structure)
    represented by a JSON string
    """

    return json.loads(my_str)
