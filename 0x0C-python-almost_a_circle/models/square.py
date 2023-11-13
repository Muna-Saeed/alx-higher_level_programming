#!/usr/bin/python3
"""square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the Square (both width and height).
            x (int): The x-coordinate of the Square's position. Defaults to 0.
            y (int): The y-coordinate of the Square's position. Defaults to 0.
            id (int): The id of the Square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size of the Square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square.

        *args: List of arguments - no-keyworded arguments.
        **kwargs: Dictionary of keyworded arguments.

        Args:
            *args: The list of arguments passed.
            **kwargs: The dictionary of keyworded arguments passed.
        """
        attr_names = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attr_names):
                    setattr(self, attr_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
            dict: The dictionary representation of the Square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: The string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
