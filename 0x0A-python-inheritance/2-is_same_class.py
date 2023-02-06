#!/usr/bin/python3
"""
is_same_class module

"""


def is_same_class(obj, a_class):
    """ object, class -> bool

    Returns True if the obj is exactly an instance
    of the specified class; otherwise False.
    """
    if type(obj) == a_class:
        return True

    return False
