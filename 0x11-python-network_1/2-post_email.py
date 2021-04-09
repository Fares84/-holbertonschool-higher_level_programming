#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8) """
from urllib import request
from urllib import parse
import sys


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}

    data = urllib.parse.urlcode(values)
    data = data.encode()
    _request = urllib.request.Request(url, data)
    with urllib.request.urlopen(_request) as response:
        print(response.read().decode())
