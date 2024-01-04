#!/usr/bin/python3
"""creates a class Rectangle"""


class Rectangle:
    """defines a class Rectangle with with private instance attributes width/height"""

    def __init__(self, width=0, height=0):
        """instantiates class instance with optional width/height attributes"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets private instance attribute width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets private instance attribute height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

