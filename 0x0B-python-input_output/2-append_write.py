#!/usr/bin/python3
"""defines a function to append a string to the
end of a file"""


def append_write(filename="", text=""):
    """appends a string to the end of a text file
    and returns number of characters added"""
    with open(filename, 'a+') as f:
        return f.write(text)
