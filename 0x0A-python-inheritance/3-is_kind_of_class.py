#!/usr/bin/python3
"""
is_kind_of_class module

"""


def is_kind_of_class(obj, a_class):
    """ object, class -> bool

    Returns True if the obj is exactly an instance
    of the specified class; otherwise False.
    """
    if isinstance(obj, a_class):
        return True

    return False
