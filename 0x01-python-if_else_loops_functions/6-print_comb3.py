#!/usr/bin/python3

# program to print all possible different combinations of two digits
# print the first digit
for i in range(10):
    # print the secound digit
    for j in range(i + 1, 10):
        print("{}{}, ".format(i, j), end='')
# print new line
print("")
