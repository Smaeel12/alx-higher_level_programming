#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            s = "FizzBuzz"
            print("{} ".format(s), end="")
        elif i % 3 == 0:
            s = "Fizz"
            print("{} ".format(s), end="")
        elif i % 5 == 0:
            s = "Buzz"
            print("{} ".format(s), end="")
        else:
            print("{} ".format(i), end="")
