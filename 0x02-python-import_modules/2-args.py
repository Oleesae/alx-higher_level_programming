#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argl = len(sys.argv)

    if argl < 2:
        print("0 arguments.")
    else:
        print("{} argument".format(argl - 1), end='')
        if argl == 2:
            print(":")
        else:
            print("s:")
        for i in range(1, argl):
            print("{:d}: {:s}".format(i, argv[i]))
