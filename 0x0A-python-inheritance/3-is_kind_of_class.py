#!/usr/bin/python3
"""defines a function that determines if an object is 
an instance of a class or class inherited from"""


def is_kind_of_class(obj, a_class):
    """returns true if an object is an instance of class it inherits from"""
    return (isinstance(obj, a_class))
