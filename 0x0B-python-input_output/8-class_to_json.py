#!/usr/bin/python3
""" dictionary description with a simple data structure for JSON serialization of an object."""


def class_to_json(obj):
    """"A dictionary representing the object's attributes in a JSON serializable format."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__slots__"):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        raise TypeError(f"Object of type {type(obj).__name__} is not serializable.")
