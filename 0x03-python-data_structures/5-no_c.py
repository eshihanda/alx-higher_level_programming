#!/usr/bin/env python3
def no_c(my_string):
    string_1 = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            string_1 += i

        return string_1
