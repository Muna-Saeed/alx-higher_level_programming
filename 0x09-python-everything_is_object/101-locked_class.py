#!/usr/bin/python3

"""This module restricts dynamic instance attribute creation."""


class LockedClass:
    """prevents creation of dynamic instance attributes,except 'first_name'."""

    __slots__ = ["first_name"]
