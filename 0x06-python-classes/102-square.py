#!/usr/bin/python3
"""Represents a square with a given size."""


class Square:
    """Initializes a Square instance."""

    def __init__(self, size=0):
        self.size = size

    """Retrieves the size of the square."""

    @property
    def size(self):
        return self.__size

    """Sets the size of the square."""

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Calculates and returns the area of the square."""

    def area(self):
        return self.__size ** 2

    """Checks if two squares have equal areas."""

    def __eq__(self, other):
        return self.area() == other.area()

    """Checks if two squares have unequal areas."""

    def __ne__(self, other):
        return self.area() != other.area()

    """Checks if a square has a greater area than the other square."""

    def __gt__(self, other):
        return self.area() > other.area()

    """Checks if a square has a greater or equal area to the other square."""

    def __ge__(self, other):
        return self.area() >= other.area()

    """Checks if a square has a smaller area than the other square."""

    def __lt__(self, other):
        return self.area() < other.area()

    """Checks if a square has a smaller or equal area to the other square."""

    def __le__(self, other):
        return self.area() <= other.area()
