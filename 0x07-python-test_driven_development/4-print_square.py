#!/usr/bin/python3
"""

Print square module

"""


def print_square(size):
    """ (int) -> char(#)

    Returns a square of size 'size' printed with #.
    size must be an integer.

    Precondition: size >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
