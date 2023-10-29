#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Initializes a TestMaxInteger instance."""

    def test_empty_list(self):
        # Test for an empty list
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        # Test for a list of positive numbers
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        # Test for a list of negative numbers
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        # Test for a list of mixed positive and negative numbers
        result = max_integer([-1, 2, -3, 4])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        # Test for a list with duplicate numbers
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

    def test_single_number(self):
        # Test for a list with a single number
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_large_numbers(self):
        # Test for a list with large numbers
        result = max_integer([999999, 1000000, 888888])
        self.assertEqual(result, 1000000)


if __name__ == "__main__":
    unittest.main()
