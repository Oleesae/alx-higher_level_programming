#!/usr/bin/python3
"""
Append write module
"""


def append_write(filename="", text=""):
    """ append_write(filename="", text="") -> file stream

    Appends text to filename
    """

    with open(filename, 'a+', encoding="utf-8") as f:
        append = f.write(text)
        return append
