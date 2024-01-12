#!/usr/bin/python3
"""Python script that sends a request to a URL
"""
import urllib.request
import urllib.error
import sys


def main():
    """Python script that fetches a variable from header
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            val = response.read().decode('utf-8')
            print(val)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
