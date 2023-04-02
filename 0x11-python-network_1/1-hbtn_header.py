#!/usr/bin/python3
""" script should take in url and sends a request"""

from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))

