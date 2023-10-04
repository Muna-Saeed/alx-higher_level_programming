#!/usr/bin/python3
def uppercase(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
    print("{}".format(result), end="\n")
