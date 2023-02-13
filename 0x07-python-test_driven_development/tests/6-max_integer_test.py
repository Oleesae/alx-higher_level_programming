#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A test case testing the function
    `max_integer` which finds and
    returns the maximum integer in a list
    """

    def test_empty_list(self):
        """checks for an empty list
        
        Returns None
        """
        value = max_integer([])
        self.assertIs(value, None)

    def test_no_argument(self):
        """checks for no argument
        
        Returns None
        """

        value = max_integer()
        self.assertEqual(value, None)

    def test_duplicate_max_value(self):
        """
        checks for duplicate max values
        Returns the value
        """

        value = max_integer([1, 2, 2, 54, 34, 89, 89])
        self.assertEqual(value, 89)

    def test_max_value(self):
        """
        checks for max value

        Returns the largest value
        """

        value = max_integer([5, 87, 22, 94, 23, 23,41])
        self.assertEqual(value, 94)
    
    def test_one_value(self):
        """
        checks in a list of one value

        Returns the largest value
        """

        value = max_integer([5])
        self.assertEqual(value, 5)

    def test_negative_values(self):
        """
        checks in a list of negative values

        Returns the largest value
        """

        value = max_integer([-5, -34, -1, -75, -4, -33])
        self.assertEqual(value, -1)

    def test_one_negative_value(self):
        """
        checks in a list of one negative values

        Returns the largest value
        """

        value = max_integer([-5, 34, 1, 75, 4, 33])
        self.assertEqual(value, 75)

    def test_max_beginning(self):
        """
        checks in a list of values

        Returns the largest value
        """

        value = max_integer([95, 34, 1, 75, 4, 33])
        self.assertEqual(value, 95)
