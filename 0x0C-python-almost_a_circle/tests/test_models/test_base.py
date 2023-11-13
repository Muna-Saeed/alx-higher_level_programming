#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
import json
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_assignment(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id_increment_after_assignment(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_id_type(self):
        b6 = Base()
        self.assertIsInstance(b6.id, int)

    def test_to_json_string_empty(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(
            json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        )

    def test_from_json_string_empty(self):
        list_objs = Base.from_json_string(None)
        self.assertEqual(list_objs, [])

    def test_from_json_string(self):
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        list_objs = Base.from_json_string(json_string)
        self.assertEqual(
            list_objs, [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        )

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            json_data = file.read()
            self.assertEqual(
                json_data,
                '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, '
                '{"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]',
            )

    def test_save_to_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            json_data = file.read()
            self.assertEqual(
                json_data,
                '[{"id": 1, "size": 5, "x": 0, "y": 0}, '
                '{"id": 2, "size": 7, "x": 9, "y": 1}]',
            )

    def test_create_rectangle(self):
        """Test create method for Rectangle"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1, r2)
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create method for Square"""
        s1 = Square(5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s1, s2)
        self.assertIsNot(s1, s2)

    def test_load_from_file_rectangle(self):
        """Test load_from_file method for Rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        """Save rectangles to file"""
        Rectangle.save_to_file(list_rectangles_input)

        """Load rectangles from file"""
        list_rectangles_output = Rectangle.load_from_file()

        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(len(list_rectangles_output), 2)

        """Check if loaded rectangles match original rectangles"""
        for rect_input, rect_output in zip(
            list_rectangles_input, list_rectangles_output
        ):
            self.assertIsInstance(rect_output, Rectangle)
            self.assertEqual(rect_input, rect_output)
            self.assertIsNot(rect_input, rect_output)

        """Delete the created file"""
        os.remove("Rectangle.json")

    def test_load_from_file_square(self):
        """Test load_from_file method for Square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        """Save squares to file"""
        Square.save_to_file(list_squares_input)

        """Load squares from file"""
        list_squares_output = Square.load_from_file()

        self.assertIsInstance(list_squares_output, list)
        self.assertEqual(len(list_squares_output), 2)

        """Check if loaded squares match original squares"""
        for square_input, square_output in zip(list_squares_input, list_squares_output):
            self.assertIsInstance(square_output, Square)
            self.assertEqual(square_input, square_output)
            self.assertIsNot(square_input, square_output)

        """Delete the created file"""
        os.remove("Square.json")


def test_csv_serialization_deserialization():
    """
    Test CSV serialization and deserialization.
    """
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file_csv(list_squares_input)

    list_squares_output = Square.load_from_file_csv()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))


def test_drawing():
    """
    Test drawing rectangles and squares using Turtle graphics.
    """
    list_rectangles = [
        Rectangle(100, 40),
        Rectangle(90, 110, 30, 10),
        Rectangle(20, 25, 110, 80),
    ]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)


if __name__ == "__main__":
    unittest.main()
