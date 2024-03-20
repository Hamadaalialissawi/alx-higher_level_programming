#!/usr/bin/python3
# get a random number
import random
number = random.randint(-10000, 10000)
# the last digit of the number
# if the number less than zero
if number < 0:
    last_digit = number * -1
    last_digit = (last_digit % 10) * -1
else:
    last_digit = number % 10
# if the last digit is greater than 5
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
# if the last digit is 0: the string and is 0
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
# if the last digit is less than 6 and not 0:
else:
    print(f"Last digit of {number} is \
{last_digit} and is less than 6 and not 0")
