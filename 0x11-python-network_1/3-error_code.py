#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8) """
from urllib import request
import urllib.parse
import sys
if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode())
    except urllib.error.URLRrror as r:
        print("Error code: {}".format(r.code))
