#!/usr/bin/python3
"""defines function to read text file and prints to stdout"""


def read_file(filename=""):
    """reads text file and prints to stdout"""
    with open(filename, 'r') as f:
        f_content = f.read()
        print(f_content, end="")
