#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    allowed_ops = ['+', '-', '*', '/']
    funcs = [add, sub, mul, div]
    if op in allowed_ops:
        print(f'{a} {op} {b} = {funcs[allowed_ops.index(op)](a, b)}')
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
