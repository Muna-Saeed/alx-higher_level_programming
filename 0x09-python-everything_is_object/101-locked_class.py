#!/usr/bin/python3

"""This module contains the LockedClass that restricts dynamic instance attribute creation."""


class LockedClass:
    """A class that prevents the creation of dynamic instance attributes, except for 'first_name'."""

    __slots__ = ["first_name"]
