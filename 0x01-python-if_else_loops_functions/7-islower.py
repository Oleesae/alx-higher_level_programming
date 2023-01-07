#!/usr/bin/python3
def islower(c):
    if 96 < ord(c) < 123 or 65 < ord(c) < 91:
        return True
    else:
        return False
