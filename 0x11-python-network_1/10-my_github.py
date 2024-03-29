#!/usr/bin/python3
""" Github authentication script """
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    req = get("https://api.github.com/user", auth=auth)
    print(req.json().get('id'))
