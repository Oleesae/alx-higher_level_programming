#!/usr/bin/python3
"""
Unitests for the Base class
"""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """
    A test case for the Initialization of the
    Base class
    """

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(89)
        self.b4 = Base()

    def tearDown(self):
        pass

    def test_no_args(self):
        self.assertEqual(self.b1.id, self.b2.id - 1)

    def test_unique(self):
        self.assertEqual(self.b3.id, 89)

    def test_mixed_id(self):
        self.assertEqual(self.b2.id, self.b4.id - 1)

    def test_json_string(self):
        """Tests the json to string metod"""

        sq = Square(3, 2, 1, 5)
        sqd = sq.to_dictionary()
        json_sq = Square.to_json_string([sqd])
        self.assertIsInstance(sqd, dict)
        self.assertIsInstance(json_sq, str)
        self.assertEqual(json_sq, '[{"id": 5, "size": 3, "x": 2, "y": 1}]')

        
