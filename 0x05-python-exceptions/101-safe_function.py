#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as e:
        ret = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return ret
