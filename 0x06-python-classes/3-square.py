#!/usr/bin/python3

"""Represents a square with a given size."""

class Square:
    """nitializes a Square instance."""
    def init(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Calculates and returns the area of the square."""
    def area(self):
        return self.__size ** 2
