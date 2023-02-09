#!/usr/bin/python3
"""A Student class"""


class Student:
    """Defines a Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of the student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the object"""

        return self.__dict__
