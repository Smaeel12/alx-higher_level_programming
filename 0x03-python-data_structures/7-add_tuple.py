#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_a = (tuple_a[:2] + (0, 0))[:2]
    new_b = (tuple_b[:2] + (0, 0))[:2]
    return tuple(sum(t) for t in zip(new_a, new_b))
