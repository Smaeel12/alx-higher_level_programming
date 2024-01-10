#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and isinstance(roman_string, str):
        number = 0
        roman_dict = {
                'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for c in roman_string:
            if number < roman_dict[c]:
                number = roman_dict[c] - number
            else:
                number += roman_dict[c]
        return number
    return None
