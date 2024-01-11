#!/usr/bin/python3
"""defines a function to determine if an object is an instance of a subclass"""


def inherits_from(obj, a_class):
    """returns true if an object is an instance of a subclass"""
    if issubclass(type(obj), a_class) and type(obj) !=a_class:
        return True
    else:
        return False
