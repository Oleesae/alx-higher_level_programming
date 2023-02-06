#!/usr/bin/python3
"""
A lookup module

"""


def lookup(obj):
    """ obj -> list

    Returns a list of available attributes
    and methods of an object
    """
    return dir(obj)
