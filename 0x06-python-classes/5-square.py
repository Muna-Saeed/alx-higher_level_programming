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

    """Prints the square with the character "#"."""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
