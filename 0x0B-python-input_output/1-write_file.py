#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
