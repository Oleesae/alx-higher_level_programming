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
    for i in range(len(text)):
        print(text[i], end='')
        if text[i] == '.' or text[i] == ':' or text[i] == '?':
            print("\n")
