#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if i != 8 or j != 9:
                print(f'{i:d}{j:d}', end=', ')
            else:
                print(f'{i:d}{j:d}')
