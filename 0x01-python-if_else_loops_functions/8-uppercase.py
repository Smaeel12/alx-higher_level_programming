#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        str_i = ord(str[i])
        if str_i > 90:
            str_i -= 32
            str_i = chr(str_i)
        else:
            str_i = chr(str_i)
        print("{}".format(str_i), end="")
    print("")
