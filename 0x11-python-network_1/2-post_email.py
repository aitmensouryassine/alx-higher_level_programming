#!/usr/bin/python3
"""Python script that:
    * takes in a URL and an email
    * sends a POST request to the passed URL with
        the email as a parameter
    * displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
