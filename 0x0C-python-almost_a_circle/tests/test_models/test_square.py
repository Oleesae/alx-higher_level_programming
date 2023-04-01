#!/usr/bin/python3
"""
Unittests for Square class
"""

import unittest
import os
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Testing the Square class
    """

    def test_id(self):
        """Tests for id"""
        
        sq = Square(4)
        sq1 = Square(8)
        sq2 = Square(3, 3, 1, 5)
        sq3 = Square(7)
        self.assertEqual(sq.id, sq1.id - 1)
        self.assertEqual(sq1.id, sq3.id - 1)

    def test_size(self):
        """Tests for the size attribute"""
        
        sq = Square(3)
        self.assertEqual(sq.size, 3)

    def test_x_arg(self):
        """Tests for the x attribute"""

        sq = Square(4, 5)
        self.assertIsInstance(sq.x, int)

    def test_size_not_int(self):
        """Tests for the size arg if not integer type"""

        with self.assertRaises(TypeError):
            sq = Square("3")

    def test_y_arg(self):
        """Test for y attribute"""

        sq = Square(4, 5, 2)
        self.assertIsInstance(sq.y, int)

    def test_x_raises(self):
        """Test for x arg value and type"""

        with self.assertRaises(TypeError):
           sq = Square(4, "5")

        with self.assertRaises(ValueError):
            sq = Square(4, -3)

    def test_y_raises(self):
        """Test for y arg type and value"""

        with self.assertRaises(TypeError):
            sq = Square(5, 2, "3")

        with self.assertRaises(ValueError):
            sq = Square(3, 2, -4)

    def test_size_gt_than_zero(self):
        """Test size if greater than zero"""

        with self.assertRaises(ValueError):
            sq = Square(-4)

        with self.assertRaises(ValueError):
            sq = Square(0)

    def test_area(self):
        """Tests the value of area of square"""

        sq = Square(4)
        self.assertEqual(sq.area(), sq.size * sq.size)

    def test_str(self):
        """Tests the str method"""

        new_sq = Square(3, 4, 2, 34)
        str_val = new_sq.__str__()
        self.assertIsInstance(str_val, str)
        self.assertEqual(str_val, "[Square] (34) 4/2 - 3")

    def test_display_no_xy(self):
        """Tests display method without x and y args"""

        expected_output = '###\n###\n###\n'
        captured_out = StringIO()
        sys.stdout = captured_out
        sq = Square(3)
        sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), expected_output)

    def test_display_x_only(self):
        """Tests the display method without the y arg"""
        expected_output = "    ##\n    ##\n"
        captured_out = StringIO()
        sys.stdout = captured_out
        sq = Square(2, 4)
        sq.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_out.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test the display method with x and y args"""

        expected_output = "\n\n  ###\n  ###\n  ###\n"
        captured_out = StringIO()
        sys.stdout = captured_out
        sq = Square(3, 2, 2)
        sq.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_out.getvalue(), expected_output)

    def test_to_dictionay(self):
        """Tests the to dictionary method"""

        sq = Square(3, 7, 6, 23)
        expected = {'id': 23, 'size': 3, 'x': 7, 'y':6}
        self.assertEqual(sq.to_dictionary(), expected)

    def test_update_id(self):
        """Tests the update method for id"""
        new = Square(3, 2, 3, 2)
        self.assertEqual(new.id, 2)
        new.update(44)
        self.assertEqual(new.id, 44)

    def test_update_size(self):
        """Tests the update method of size property"""

        sq = Square(2)
        self.assertEqual(sq.size, 2)
        sq.update(44, 5)
        self.assertEqual(sq.width, 5)

    def test_update_x(self):
        """Tests the update method for the x value"""

        sq = Square(3, 4)
        self.assertEqual(sq.x, 4)
        sq.update(44, 5, 8)
        self.assertEqual(sq.x, 8)

    def test_update_y(self):
        """Tests the update method for the y value"""

        sq = Square(4, 4, 2, 2)
        self.assertEqual(sq.y, 2)
        sq.update(44, 5, 17, 7)
        self.assertEqual(sq.y, 7)
    
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

    def test_update_kwargs_x(self):
        """Tests the update kwargs for x"""

        new = Rectangle(2, 8)
        new.update(**{'id': 23, 'width': 1, 'height': 3, 'x': 5})
        self.assertEqual(new.x, 5)

    def test_update_kwargs_y(self):
        """Tests the update kwargs for y"""

        new = Rectangle(5, 8)
        new.update(**{'id': 34, 'width': 3, 'height': 8, 'x': 8, 'y': 2})
        self.assertEqual(new.y, 2)
