#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            str += idx
    return str
