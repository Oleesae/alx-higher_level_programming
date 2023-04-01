#!/usr/bin/python3
"""
Unittests for Rectangle class
"""

import unittest
import os
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Testing the Rectangle class
    """

    def setUp(self):
        self.a = Rectangle(2, 3)
        self.b = Rectangle(4, 2, 4)
        self.c = Rectangle(3, 2, 7, 6, 23)
        self.d = Rectangle(3, 6, 2, 2)

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

    def test_str(self):
        """Tests the str method"""

        str_val = self.c.__str__()
        self.assertIsInstance(str_val, str)
        self.assertEqual(str_val, "[Rectangle] (23) 7/6 - 3/2")

    def test_display_no_xy(self):
        """Tests display method without x and y args"""

        expected_output = '##\n##\n##\n'
        captured_out = StringIO()
        sys.stdout = captured_out
        self.a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), expected_output)

    def test_display_x_only(self):
        """Tests the display method without the y arg"""
        expected_output = "    ####\n    ####\n"
        captured_out = StringIO()
        sys.stdout = captured_out
        self.b.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_out.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test the display method with x and y args"""

        expected_output = "\n\n  ###\n  ###\n"
        expected_output += "  ###\n  ###\n  ###\n  ###\n"
        captured_out = StringIO()
        sys.stdout = captured_out
        self.d.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_out.getvalue(), expected_output)

    def test_to_dictionay(self):
        """Tests the to dictionary method"""

        expected = {'id': 23, 'width': 3, 'height': 2, 'x': 7, 'y':6}
        self.assertEqual(self.c.to_dictionary(), expected)

    def test_update_id(self):
        """Tests the update method for id"""
        new = Rectangle(3, 2)
        new.update(44)
        self.assertEqual(new.id, 44)

    def test_update_width(self):
        """Tests the update method of width property"""

        self.assertEqual(self.a.width, 2)
        self.a.update(44, 5)
        self.assertEqual(self.a.width, 5)

    def test_update_height(self):
        """Tests the update method for the height value"""

        self.assertEqual(self.a.height, 3)
        self.a.update(44, 5, 17)
        self.assertEqual(self.a.height, 17)

    def test_update_x(self):
        """Tests the update method for the x value"""

        self.assertEqual(self.a.x, 0)
        self.a.update(44, 5, 17, 5)
        self.assertEqual(self.a.x, 5)

    def test_update_y(self):
        """Tests the update method for the y value"""

        self.assertEqual(self.a.y, 0)
        self.a.update(44, 5, 17, 5, 6)
        self.assertEqual(self.a.y, 6)
    
    def test_update_kwargs_id(self):
        """Tests the update kwargs for id"""

        new = Rectangle(5, 8)
        new.update(**{'id': 38})
        self.assertEqual(new.id, 38)

    def test_update_kwargs_width(self):
        """Tests the update kwargs for width"""

        new = Rectangle(5, 2)
        new.update(**{'id': 23, 'width': 13})
        self.assertEqual(new.width, 13)

    def test_update_kwargs_height(self):
        """Tests the update kwargs for height"""

        new = Rectangle(2, 8)
        new.update(**{'id': 23, 'width': 13, 'height': 7})
        self.assertEqual(new.height, 7)
