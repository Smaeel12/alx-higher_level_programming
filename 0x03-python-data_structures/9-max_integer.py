#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    MAX = 0
    for idx in my_list:
        if idx > MAX:
            MAX = idx
    return MAX
