#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = argv[1:]
    nargs = len(args)
    if nargs == 0:
        print('0 arguments.')
    elif nargs == 1:
        print('1 argument:')
        print('1: {}'.format(args[0]))
    else:
        print('{:d} arguments:'.format(nargs))
        for i, arg in enumerate(args):
            print('{:d}: {}'.format(i + 1, arg))
