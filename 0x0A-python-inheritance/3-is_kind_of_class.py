#!/usr/bin/python3
"""is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of or inherited from a_class, else False.
    """
    return isinstance(obj, a_class)
