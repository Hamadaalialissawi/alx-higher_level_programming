#!/usr/bin/python3

"""
uppercase: function to convert lowercase to uppercase characters
@str: the string
"""


def uppercase(str):
    for char in str:  # check the string
        if 97 <= ord(char) <= 122:  # convert the lowercase to uppercase
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print(upper_char, end='')
    print("")
