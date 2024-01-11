#!/usr/bin/python3
"""defines a class with public instance methods for are and integer validation"""


class BaseGeometry:
    """class with public instance methods"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
