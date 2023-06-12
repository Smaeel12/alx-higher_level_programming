#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        new_str = ""
        List = list(my_string)
        for idx in List:
            if idx == 'c' or idx == 'C':
                List.remove(idx)
        new_str = "".join(List)
        return new_str
    else:
        return None
