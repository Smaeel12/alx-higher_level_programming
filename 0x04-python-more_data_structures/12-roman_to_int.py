#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and isinstance(roman_string, str):
        number = 0
        roman_dict = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        prev_value = 0
        for c in roman_string[::-1]:
            current_value = roman_dict[c]
            if current_value >= prev_value:
                number += current_value
            else:
                number -= current_value
            prev_value = current_value
        return number
    return None
