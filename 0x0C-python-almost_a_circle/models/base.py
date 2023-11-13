#!/usr/bin/python3
"""Base class module"""
import json
import csv


class Base:
    """
    Base class for serialization, deserialization, and drawing of rectangles and squares.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): The ID of the instance. If not provided, it will be automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_csv_row(instance):
        """
        Converts an instance of a Rectangle or Square to a CSV row.

        Args:
            instance (Rectangle or Square): The instance to convert.

        Returns:
            list: The CSV row representing the instance.
        """
        if isinstance(instance, Rectangle):
            return [instance.id, instance.width, instance.height, instance.x, instance.y]
        elif isinstance(instance, Square):
            return [instance.id, instance.size, instance.x, instance.y]

    @staticmethod
    def from_csv_row(row):
        """
        Creates an instance of Rectangle or Square from a CSV row.

        Args:
            row (list): The CSV row representing the instance.

        Returns:
            Rectangle or Square: The created instance.
        """
        if len(row) == 5:
            return Rectangle(*row[1:])
        elif len(row) == 4:
            return Square(*row[1:])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of Rectangle or Square instances to a CSV file.

        Args:
            list_objs (list): The list of instances to serialize.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(cls.to_csv_row(obj))

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a list of Rectangle or Square instances from a CSV file.

        Returns:
            list: The deserialized list of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    instance = cls.from_csv_row(row)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws the rectangles and squares using Turtle graphics.

        Args:
            list_rectangles (list): The list of Rectangle instances to draw.
            list_squares (list): The list of Square instances to draw.
        """
        import turtle
        
        def draw_rectangle(rectangle):
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)
            turtle.penup()

        def draw_square(square):
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.penup()

        turtle.speed(0)
        turtle.shape("turtle")

        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        for square in list_squares:
            draw_square(square)

        turtle.exitonclick()

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): The JSON string representation.

        Returns:
            list: A list of dictionaries.

        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a file in JSON format.

        Args:
            list_objs (list): A list of instances.

        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file in JSON format.

        Returns:
            list: A list of instances.

        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                return [cls.create(**dictionary) for dictionary in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set based on a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary containing the attributes.

        Returns:
            object: An instance of the class with attributes set according to the dictionary.

        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy
