#!/usr/bin/python3
def no_c(my_string):
    string_1 = my_string.translate({ord(i): None for i in 'cC'})
    return string_1
