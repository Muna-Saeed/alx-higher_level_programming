#!/usr/bin/python3
"""dictionary description with simple data structure for JSON an object."""


def class_to_json(obj):
    """"A dictionary the object's attributes in a JSON serializable format."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__slots__"):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        raise TypeError("Object of type {} is not serializable."
                        .format(type(obj).__name__))
