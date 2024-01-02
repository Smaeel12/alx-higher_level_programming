#!/usr/bin/python3
for i in range(97, 123):
    print('{:c}'.format(i if i != 101 and i != 113 else 0), end='')
