#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    args = argv[1:]
    result = 0
    for i in args:
        result += int(i)
    print(result)
