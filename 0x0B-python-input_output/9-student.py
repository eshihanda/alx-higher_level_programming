#!/usr/bin/python3
"""creates a class studens plus public instance methods
and instantiation"""


class Student:
    """class"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of class"""
        return self.__dict__
