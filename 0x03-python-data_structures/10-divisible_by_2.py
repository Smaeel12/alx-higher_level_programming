#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_list = my_list.copy()
    for idx in my_list:
        if idx % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
    return new_list
