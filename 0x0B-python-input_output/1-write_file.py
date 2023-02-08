#!/usr/bin/python3
""" Write file module """


def write_file(filename="", text=""):
    """ write_file(filename="", text="") -> file object

    writes text into filename
    """

    with open(filename, 'w+', encoding="utf-8") as f:
        write = f.write(text)
        return write
