#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_create_square(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_update(self):
        s = Square(5)
        s.update(10, 7, 3, 2)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 2)

    def test_string_representation(self):
        s = Square(5, 2, 3, 10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")

    def test_getter_setter_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)

        with self.assertRaises(TypeError):
            s.size = "9"

if __name__ == "__main__":
    unittest.main()
