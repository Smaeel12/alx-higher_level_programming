#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = 0
    first_char = None
    if sentence:
        lenght = len(sentence)
        first_char = sentence[0]
    return lenght, first_char
