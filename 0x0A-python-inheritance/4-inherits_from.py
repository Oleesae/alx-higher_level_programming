#!/usr/bin/python3
"""
inherits_from module

"""


def inherits_from(obj, a_class):
    """ object, class -> bool

    Returns True if the obj is exactly an instance
    of the specified class; otherwise False.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
