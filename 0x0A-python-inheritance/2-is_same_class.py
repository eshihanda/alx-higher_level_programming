#!/usr/bin/python3
"""defines a function to determine if an object is an 
instance of a specified class, otherwise False"""


def is_same_class(obj, a_class):
    """ returns True if an object isan instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
