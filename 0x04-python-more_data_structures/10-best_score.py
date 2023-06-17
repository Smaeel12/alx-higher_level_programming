#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list = a_dictionary.items()
        score = 0
        for tuple in list:
            if tuple[1] > score:
                score = tuple[1]
                key = tuple[0]
        return key
    return None
