#!/usr/bin/python3
""" script to POST request with requests package """
from sys import argv
from requests import post

if __name__ == "__main__":
    request = post(argv[1], {'email': argv[2]})
    print(request.text)
