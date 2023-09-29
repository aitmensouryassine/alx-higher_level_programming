#!/usr/bin/python3
"""Python script that:
    * takes in a URL
    * sends a request to the URL
    * displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
       resp = urllib.request.urlopen(req)
       print(resp.read().decode('utf-8'))
    except urllib.error.URLError as error:
        print("Error code: {}".format(error.code))
