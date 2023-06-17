#!/usr/bin/python3
def roman_to_int(roman_string):
    value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000
                  }
    value_list = []
    integer = 0
    for char in roman_string:
        for key in value_dict:
            if char == key:
                value_list.append(value_dict[key])
    for value in value_list:
        if integer < value:
            integer = value - integer
        else:
            integer += value
    return integer
