#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None and len(my_list) != 0:
        my_list.sort(reverse=True)
        return my_list[0]
