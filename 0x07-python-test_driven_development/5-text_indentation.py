#!/usr/bin/python3
"""
A Text Indentation Module

"""


def text_indentation(text):
    """ str -> str

    Returns a formatted string. prints 2 newlines
    after each '.' '?' and ':'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i, c in enumerate(text):
        if c != ' ':
            flag = True
        if c in ".:?":
            print("{}\n".format(c))
            flag = False
        elif flag:
            print(c, end="")
    if flag == False:
        print()
