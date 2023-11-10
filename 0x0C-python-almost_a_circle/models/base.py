#!/usr/bin/python3
"""Base class module"""


class Base:
    """
    Base class that manages the id attribute for all other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
