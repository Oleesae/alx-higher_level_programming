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
        self.assertEqual(self.c.id, 23)

    def test_width_height(self):
        new_rec = Rectangle(3, 2)
        self.assertEqual(new_rec.width, 3)
        self.assertEqual(new_rec.height, 2)

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

    def test_x_raises(self):
        """Test for x arg value and type"""

        with self.assertRaises(TypeError):
            new_rec = Rectangle(13, 3, "7")

        with self.assertRaises(ValueError):
            new_rec1 = Rectangle(32, 8, -2)

    def test_y_raises(self):
        """Test for y arg type and value"""

        with self.assertRaises(TypeError):
            new_rec = Rectangle(8, 2, 8, "2")

        with self.assertRaises(ValueError):
            new_rec1 = Rectangle(7, 4, 2, -4)

    def test_width_gt_than_zero(self):
        """Test width if greater than zero"""

        with self.assertRaises(ValueError):
            new_rec = Rectangle(-4, 3)

        with self.assertRaises(ValueError):
            new_rec1 = Rectangle(0, 7)

    def test_height_gt_than_zero(self):
        """Test height if greater than zero"""

        with self.assertRaises(ValueError):
            new_rec = Rectangle(2, -12)

        with self.assertRaises(ValueError):
            new_rec1 = Rectangle(5, 0)

    def test_area(self):
        """Tests the value of area of rectangle"""

        self.assertEqual(self.c.area(), self.c.width * self.c.height)
    
