#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in
            zip(a_dictionary.keys(), a_dictionary.values())}
