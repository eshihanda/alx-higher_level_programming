#!/usr/bin/python3
"""creates class Square with
private instance attribute size and public instance method"""


class Square:
    """defines class and instantiates validated private instance attribute
and also includes public instance method."""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates and returns current area of the square"""
        return(self.__size * self.__size)
