#!/usr/bin/python3
"""defines a function to read a text and prints it"""


def read_file(filename=""):
    """reads a text and prints it to stdout"""
    with open(filename, 'r') as f:
        f.content = f.read()
        print(f.content, end="")
