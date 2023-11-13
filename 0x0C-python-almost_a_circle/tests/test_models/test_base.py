import unittest
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
        self.assertEqual(json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_from_json_string_empty(self):
        list_objs = Base.from_json_string(None)
        self.assertEqual(list_objs, [])

    def test_from_json_string(self):
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        list_objs = Base.from_json_string(json_string)
        self.assertEqual(list_objs, [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}])

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, '
                                         '{"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]')

    def test_save_to_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, '[{"id": 1, "size": 5, "x": 0, "y": 0}, '
                                         '{"id": 2, "size": 7, "x": 9, "y": 1}]')

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rectangles[1].to_dictionary(), r2.to_dictionary())

    def test_load_from_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(squares[1].to_dictionary(), s2.to_dictionary())

if __name__ == '__main__':
    unittest.main()
