#!/usr/bin/python3
"""
Unittests for Rectangle class
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Testing the Rectangle class
    """

    def setUp(self):
        self.a = Rectangle(2, 7)
        self.b = Rectangle(4, 2, 8)
        self.c = Rectangle(3, 2, 7, 6, 23)
        self.d = Rectangle(13, 16, 2, 8)

    def tearDown(self):
        pass

    def test_id(self):
        self.assertEqual(self.a.id, self.b.id - 1)
        self.assertEqual(self.b.id, self.d.id - 1)

    def test_width_height(self):
        self.assertEqual(self.c.width, 3)
        self.assertEqual(self.c.height, 2)

    def test_x_arg(self):
        self.assertIsInstance(self.b.x, type(self.b.x))
        self.assertIsInstance(self.c.x, type(self.c.x))

    def test_width_not_int(self):
        """Tests for the width arg if not integer type"""

        with self.assertRaises(TypeError):
            new_rec = Rectangle("2", 3)

    def test_y_arg(self):
        self.assertIsInstance(self.c.y, type(self.c.y))
        self.assertIsInstance(self.d.y, type(self.d.y))

    def test_height_not_int(self):
        """Tests for the height arg if not integer type"""

        with self.assertRaises(TypeError):
            new_rec = Rectangle(3, "3")

    def test_x_not_int(self):
        """Test for x arg if not integer"""

        with self.assertRaises(TypeError):
            new_rec = Rectangle(13, 3, "7")

    def test_y_not_int(self):
        """Test for y arg if not integer"""

        with self.assertRaises(TypeError):
            new_rec = Rectangle(8, 2, 8, "2")

    def test_width_gt_than_zero(self):
        """Test width if greater than zero"""

        with self.assertRaises(ValueError):
            new_rec = Rectangle(-4, 3)

    def test_height_gt_than_zero(self):
        """Test height if greater than zero"""

        with self.assertRaises(ValueError):
            new_rec = Rectangle(2, -12)
    
