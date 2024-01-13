#!/usr/bin/python3
"""defines a function to write a string to a text file"""


def write_file(filename="", text=""):
    """write a string to a text file and returns the characteers written"""
    with open(filename, 'w') as f:
        return f.write(text)
