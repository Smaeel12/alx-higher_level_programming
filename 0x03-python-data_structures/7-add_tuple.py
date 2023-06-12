#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    while len_a != 2:
        list_a.append(0)
        len_a += 1
    while len_b != 2:
        list_b.append(0)
        len_b += 1
    new_tuple = (list_a[0] + list_b[0], list_a[1] + list_b[1])
    return new_tuple
