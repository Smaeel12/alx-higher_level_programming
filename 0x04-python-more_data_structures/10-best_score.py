#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        v = 0
        k = ''
        for k1, v1 in a_dictionary.items():
            if v < v1:
                v = v1
                k = k1
        return k
