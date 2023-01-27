#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new = ''
    for i in range(len(str)):
        if i is not n:
            new += str[i]
            continue
    return new
