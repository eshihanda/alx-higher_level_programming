#!/usr/bin/python3
"""creates class Rectangle"""


class Rectangle:
    """defines class Rectangle with private instance attributes width/height
and public instance methods to return the rectangle area and perimeter
and public class attributes to track of number of instances and print symbol
and can print the rectangle using print_symbol with print() or str()
and returns representation of the rectangle to be used by eval()
and prints message when deleted"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instantiates class instance with optional width/height attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """returns string representation of rectangle for print() and str()"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height):
            for column in range(self.__width):
                string += str(self.print_symbol)
            string += "\n"
        string = string[:-1]
        return string

    def __repr__(self):
        """returns string representation of rectangle for eval()"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints goodbye message when rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
