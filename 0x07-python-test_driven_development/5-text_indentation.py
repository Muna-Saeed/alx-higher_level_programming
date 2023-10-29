#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters: ., ? and :"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    result = ""
    add_newline = False

    for char in text:
        if char == " " and not add_newline:
            continue

        result += char

        if char in chars:
            result += "\n\n"
            add_newline = True
        elif add_newline and char == " ":
            add_newline = False

    lines = result.rstrip().split("\n")
    formatted_result = "\n".join(line.strip() for line in lines)
    print(formatted_result)
