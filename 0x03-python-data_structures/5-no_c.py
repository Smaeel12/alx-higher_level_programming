#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        List = list(my_string)
        for idx in List:
            if idx == 'c' or idx == 'C':
                List.remove(idx)
        my_string = "".join(List)
        return my_string
