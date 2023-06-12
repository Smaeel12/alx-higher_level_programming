#!/usr/bin/python3
from string import ascii_uppercase

def print_alphabet(letters):
    if len(letters) > 0:
        print(letters[0], end='')
        print_alphabet(letters[1:])

print_alphabet(ascii_uppercase)

