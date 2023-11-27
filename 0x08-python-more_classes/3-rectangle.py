#!/usr/bin/python3
"""creates class Rectangle"""


class Rectangle:
    """defines class Rectangle with private instance attributes width/height
and public instance methods to return the rectangle area and perimeter
and can print the rectangle using '#' with print() or str()"""

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
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
    def __str__(self):
        """ prints representation of rectangle with # """
        r_string = ""
        if self.__height == 0 or self.__width == 0:
            return r_string
        for i in range(self.__height):
            r_string += ("#" * self.__width)
            if i < self.__height - 1:
                r_string += '\n'
        return r_string
