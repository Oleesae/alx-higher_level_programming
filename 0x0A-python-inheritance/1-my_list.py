#!/usr/bin/python3
"""
A Mylist module

"""


class MyList(list):
    """
    A MyList class
    A subclass of list

    """

    def __init__(self):
        """ Initializes object """

        super().__init__()

    def print_sorted(self):
        """ Prints a sorted list """

        print(sorted(self.copy()))
