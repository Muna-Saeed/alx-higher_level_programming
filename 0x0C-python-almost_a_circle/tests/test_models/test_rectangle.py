#!/usr/bin/python3
'''Rectangle module unit tests.'''

import unittest
from models.rectangle import Rectangle
from models.base import Base


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


if __name__ == '__main__':
    unittest.main()
