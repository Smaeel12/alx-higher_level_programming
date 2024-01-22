#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_l = 0
    try:
        for no in my_list:
            if len_l == x:
                break
            len_l += 1
            print (no)
    except:
        pass
    return len_l 
