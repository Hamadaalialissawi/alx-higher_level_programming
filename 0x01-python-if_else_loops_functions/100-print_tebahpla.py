#!/usr/bin/python3

m = 25  # Difference between letters from 97 to 122
n = 9  # Difference between letters 97 and 88
# loop to chmose the  characters from ascii table
for i in range(97, 123):
    if i % 2 == 1:
        z = i + m
        m = m - 4
    else:
        z = i - n
        n = n + 4
    print(chr(z), end='')
