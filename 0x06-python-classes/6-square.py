#!/usr/bin/python3
"""Represents a square with a given size and position."""


class Square:
    """Initializes a Square instance."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """Retrieves the position of the square."""
    @property
    def position(self):
        return self.__position

    """Sets the position of the square."""
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Calculates and returns the area of the square."""
    def area(self):
        return self.__size ** 2

    """Prints the square with the character "#"."""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
