#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argl = len(sys.argv)
    sum = 0

    if argl > 1:
        for i in range(1, argl):
            sum += int(argv[i])
    print("{:d}".format(sum))
