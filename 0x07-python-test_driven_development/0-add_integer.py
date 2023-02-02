#!/usr/bin/python3
"""0-add_integer.py"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b.
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
