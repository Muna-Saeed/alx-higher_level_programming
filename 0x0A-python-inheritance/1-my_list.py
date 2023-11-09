#!/usr/bin/python3
"""print_sorted"""


class MyList(list):
    """a class MyList that inherits from list"""

    def print_sorted(self):
        """public instnce method that prints the list, but sorted"""
        print(sorted(self))
