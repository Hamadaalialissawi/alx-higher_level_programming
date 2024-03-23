#!/usr/bin/python3
"""
fizzbuzz: function that prints the numbers from 1 to 100 separated by a space.
"""


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0 and i % 5 != 0:
            print("Fizz ", end='')
        elif i % 5 == 0 and i % 3 != 0:
            if i == 100:
                print("Buzz")
            else:
                print("Buzz ", end='')
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz ", end='')
        else:
            print("{} ".format(i), end='')
