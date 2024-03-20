#!/usr/bin/python3
# print alphabet in lowercase
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    else:
        print(chr(int("{}".format(i))), end='')
