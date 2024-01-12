#!/usr/bin/python3
"""Python script that post request from a url
"""
import urllib.request
import urllib.parse
import sys


def main():
    """Python script that fetches a variable from header
    """
    url = sys.argv[1]
    email = {'email' : sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii') # data should be in bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf-8')
        print(page)


if __name__ == "__main__":
    main()
