#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = argv[1:]
    result = 0
    for i in args:
        result += int(i)
    print(result)
