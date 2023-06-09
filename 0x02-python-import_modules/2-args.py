#!/usr/bin/python3
from sys import argv
num_args = len(argv[1:])
if num_args == 1:
    str = "argument:"
else:
    str = "argumentsi:"
print(f"{num_args:d} {str:s}")
for i in range(1, num_args + 1):
    print(f"{i:d}: {argv[i]:s}")
