#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv)
    print(num_args)
    if num_args == 1:
        str = " arguments."
    elif num_args == 2:
        str = " argument:"
    else:
        str = " arguments:"

    print(f"{num_args - 1:d}{str:s}")
    for i in range(1, num_args):
        print(f"{i:d}: {argv[i]:s}")
