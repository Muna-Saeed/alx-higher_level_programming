#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
