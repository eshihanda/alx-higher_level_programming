#!/usr/bin/python3
"""defines function to print text with 2 newlines after '.' '?' or ':' chars"""


def text_indentation(text):
    """prints text with 2 newlines after '.' '?' or ':' chars"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    prev = ""
    for char in text:
        # leading whitespace
        if char is " " and char is text[0] and previous is "":
            prev = "\n"
            continue
        # whitespaces after newline
        if char is " " and prev is "\n":
            continue
        # matching character, print char, print newlines
        if char is "." or char is "?" or char is ":":
            print(char)
            print()
            prev = "\n"
        else:
            print(char, end="")
            prev = char
