#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_copy = a_dictionary.copy()
    for i in dict_copy:
        dict_copy[i] = dict_copy[i] * 2
    return dict_copy
