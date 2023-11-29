#!/usr/bin/python3
"""defines a function that prints first name and last name"""

def say_my_name(first_name, last_name=""):
    """prints first name and last name with the input my name is"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
