#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_list = list(a_dictionary.keys())
    s_list.sort()
    for i in s_list:
        print(i, a_dictionary.get(i), sep=": ")
