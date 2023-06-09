#!/usr/bin/python3
from sys import argv
num_args = len(argv)
if num_args == 1:
    str = "."
if num_args == 2:
    str = " argument:"
else:
    str = " arguments:"

print(f"{num_args - 1:d}{str:s}")
for i in range(1, num_args):
    print(f"{i:d}: {argv[i]:s}")
