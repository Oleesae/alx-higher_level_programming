#!/usr/bin/python3
def uppercase(str):
    i = 0

    while i < len(str):
        if ord(str[i]) in range(97, 123):
            print("{:c}".format(ord(str[i]) - 32), end='')
        else:
            print("{:c}".format(ord(str[i])), end='')
        i += 1
    else:
        print()
                

