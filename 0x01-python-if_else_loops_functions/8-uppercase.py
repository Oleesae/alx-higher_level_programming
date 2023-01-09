#!/usr/bin/python3
def uppercase(str):
    i = 0
    num = 0

    while i < len(str):
        if ord(str[i]) in range(97, 123):
            num = 32
        else:
            num = 0

        print("{:c}".format(ord(str[i]) - num), end='')
        i += 1
    else:
        print()
