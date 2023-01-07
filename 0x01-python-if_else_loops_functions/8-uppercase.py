#!/usr/bin/python3
def uppercase(str):
    for word in str:
        if ord(word) in range(97, 123):
            word = ord(word) - 32
            print('{:c}'.format(word))
