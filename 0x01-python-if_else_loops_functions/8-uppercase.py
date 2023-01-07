#!/usr/bin/python3
def uppercase(str):
    for word in range(len(str)):
        if ord(str[word]) > 96 and ord(str[word]) < 123:
            dif = 32
        else:
            dif = 0
        print('{:c}'.format(ord(str[word] - dif), end="")
              print()
