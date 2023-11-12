#!/usr/bin/python3
'''Rectangle module unit tests.'''

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def test_rectangle_attributes(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(5, 5, 1, 2, 3)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 3)

    def test_rectangle_setters(self):
        r3 = Rectangle(10, 2)
        r3.width = 5
        r3.height = 3
        r3.x = 2
        r3.y = 1

        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 3)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 1)

    def test_rectangle_attribute_validation(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            Rectangle(-10, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2)
            r.width = "10"
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.width = 0
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2)
            r.x = [1, 2, 3]
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.x = -1
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")
    def test_rectangle_area(self):
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

        r5 = Rectangle(2, 10)
        self.assertEqual(r5.area(), 20)

        r6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r6.area(), 56)

    def test_rectangle_display(self):
        r7 = Rectangle(4, 6)
        expected_output = "####\n" * 6
        captured_output = StringIO()
        sys.stdout = captured_output
        r7.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r8 = Rectangle(2, 2)
        expected_output = "##\n" * 2
        captured_output = StringIO()
        sys.stdout = captured_output
        r8.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
