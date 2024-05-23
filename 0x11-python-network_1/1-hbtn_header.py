#!/usr/bin/python3
"""Python script that shows
    X-Request_Id Header of an URL """

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
