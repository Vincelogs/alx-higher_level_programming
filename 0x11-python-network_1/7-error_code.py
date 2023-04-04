#!/usr/bin/python3
""" returns request content or error code with requests package """
from sys import argv
from requests import get

if __name__ == "__main__":
    request = get(argv[1])
    if request.status_code >= 400:
        print("Error code:", request.status_code)
    else:
        print(request.text)
