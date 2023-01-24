#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as te:
        print("Exception: {}".format(te))
        return False
    else:
        return True
