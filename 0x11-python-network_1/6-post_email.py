#!/usr/bin/python3
"""Python script that post request from a url
"""
import requests
import sys


def main():
    """Python script that fetches a variable from header
    """
    url = sys.argv[1]
    headers = {'email': sys.argv[2]}

    r = requests.post(url, headers=headers)
    print(r.text)


if __name__ == "__main__":
    main()
