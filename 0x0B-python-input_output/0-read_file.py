#!/usr/bin/python3
""" Read File module """


def read_file(filename=""):
    """ file -> str

    Reads a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
