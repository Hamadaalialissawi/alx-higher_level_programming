#!/usr/bin/python3

"""
remove_char_at: function creates a copy of the string
and removing the character at the position n

@str: first argument
@n: second argument
Return: new_str
"""


def remove_char_at(str, n):
    if n >= 0:
        new_str = str[:n] + str[n + 1:]
        return new_str
    else:
        return str
