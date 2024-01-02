#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 5 else -((-number) % 10)
if last_digit > 5:
    result = f'greater than 5'
elif last_digit == 0:
    result = f'0'
else:
    result = f'less than 6 and not 0'
print(f'Last digit of {number:d} is {last_digit:d} and is {result}')
