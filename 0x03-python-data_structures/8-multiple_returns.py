#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        lenght = len(sentence)
        if lenght > 0:
            first_c = sentence[0]
        return (lenght, first_c)
    return None
