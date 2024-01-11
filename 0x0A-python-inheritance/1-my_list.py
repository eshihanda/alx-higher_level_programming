#!/usr/bin/python3
"""defines a class that inherits from another class"""


class MyList(list):
    """class that inherits from another class"""

    def print_sorted(self):
        print(sorted(self))
