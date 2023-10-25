#!/usr/bin/python3
import math

"""Represents a class MagicClass"""


class MagicClass:
    """Initializes a MagicClass instance."""

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """This method calculates and returns the area of the circle"""

    def area(self):
        return math.pi * self.__radius ** 2

    """This method calculates and returns the circumference of the circle"""

    def circumference(self):
        return 2 * math.pi * self.__radius
