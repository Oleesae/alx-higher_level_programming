#!/usr/bin/python3
def uppercase(str):
    for word in range(len(str)):
        if ord(str[word]) in range(97, 123):
            dif = 32
        else:
            dif = 0
        print('{:c}'.format(ord(str[word] - num), end="")
    print()
