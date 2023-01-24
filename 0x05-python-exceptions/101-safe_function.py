#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as e:
        ret = None
        print("Exception: {}".format(e))
    finally:
        return ret
