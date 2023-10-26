#!/usr/bin/python3
"""Represents a class MagicClass"""


class MagicClass:
    """Initializes a MagicClass instance."""
    def __init__(self, radius=0):
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    """This method calculates and returns the area of the circle"""
    def area(self):
        import math
        return math.pi * self.__radius ** 2

    """This method calculates and returns the circumference of the circle"""
    def circumference(self):
        import math
        return 2 * math.pi * self.__radius
