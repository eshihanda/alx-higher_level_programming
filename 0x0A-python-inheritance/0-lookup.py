#!/usr/bin/python3
"""defines a function that list available attributes
and methods of an object"""


def lookup(obj):
    """return a list of available attributes and methods of an object"""

    return dir(obj)
