#!/usr/bin/python3
"""defines Base class"""


class Base():
    """creates the base classs that manages 
    id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes to given id or"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
