#!/usr/bin/python3
"""defines a class with public instance method"""


class BaseGeometry:
    """class with public instance method that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")
