#!/usr/bin/python3
"""defines a class rectangle that inherits
from the basegeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from base class"""
    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width
