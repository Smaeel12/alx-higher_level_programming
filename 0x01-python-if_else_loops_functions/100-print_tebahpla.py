#!/usr/bin/python3
i = 122
j = 89
while (i > 96 and j > 64):
    print('{:c}{:c}'.format(i, j), end='')
    i -= 2
    j -= 2
