#!/usr/bin/python3
"""JSON string module"""


def to_json_string(my_obj):
    """object -> str

    Returns the JSON representation
    of an object(string)
    """

    json_string = json.dumps(my_obj)
    return json_string
