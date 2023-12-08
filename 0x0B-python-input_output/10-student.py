#!/usr/bin/python3
"""defines class Student"""


class Student():
    """class to define student"""

    def __init__(self, first_name, last_name, age):
        """initializes student instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        dic = {}
        if type(attrs) != list:
            return self.__dict__
        else:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
            for key in self.__dict__:
                if key in attrs:
                    dic[key] = self.__dict__[key]
        return dic
