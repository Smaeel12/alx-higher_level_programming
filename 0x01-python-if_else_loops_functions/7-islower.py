#!/usr/bin/python3
def islower(c):
    c_i = ord(c)
    if c_i > 96 and c_i < 123:
        return True
    else:
        return False
