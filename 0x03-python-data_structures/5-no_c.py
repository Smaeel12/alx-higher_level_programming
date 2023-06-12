#!/usr/bin/python3
def no_c(my_string):
    i = 0
    List = list(my_string)
    if 'c' in List:
        List.remove('c')
    if 'C' in List:
        List.remove('C')
    new_string = "".join(List)
    return new_string
