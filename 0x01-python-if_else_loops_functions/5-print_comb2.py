#!/usr/bin/python3

# for i in range(100):
#   end = ', ' if i != 99 else '\n'
#   print(f'{i:0>2d}', end=', ')

for i in range(99):
    print(f'{i:0>2d}', end=', ')
else:
    print('99')
