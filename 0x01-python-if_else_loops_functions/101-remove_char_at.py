#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str
    if n >= 0 and n <= len(new_str):
        list_1 = list(str)
        list_1.pop(n)
        new_str = ''.join(list_1)
        return new_str
    return new_str
