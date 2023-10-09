#!/usr/bin/python3
"""
MyInt class that inherits from int
"""

class MyInt(int):
    """
    Inherits from int class.
    Inverts the '==' and '!=' operators
    """

    def __eq__(self, value):
        """Returns the operation for '!='. """
        return self.real != value

    def __ne__(self, value):
        """Returns the operation for '=='. """
        return self.real == value
