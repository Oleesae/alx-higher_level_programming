#!/ur/bin/python3
"""Takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}

    r = requests.post(url, data)

    try:
        dump_r = r.json()
    except ValueError as e:
        print("Not a valid JSON")
        return

    if len(dump_r) == 0:
        print("No result")
        return

    print("[{}] {}".format(r_dumped['id'], r_dumped['name']))
