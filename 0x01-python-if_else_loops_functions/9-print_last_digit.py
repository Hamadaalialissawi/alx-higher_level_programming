#!/usr/bin/python3
"""
print_last_digit: function that prints the last digit of a number

@number: the argument
Return: num_2
"""


def print_last_digit(number):
    if number >= 0:
        num_2 = (number % 10)
    else:
        num_2 = ((number * -1) % 10)

    print(num_2, end='')
    return num_2
