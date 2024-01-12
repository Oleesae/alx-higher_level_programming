#!/usr/bin/python3
"""Python script that gets from a URL and checks for error
"""
import requests
import sys


def main():
    """Python script that fetches a variable from header
    """
    url = sys.argv[1]

    r = requests.get(url)

    if (r.status_code >= 400):
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    main()
