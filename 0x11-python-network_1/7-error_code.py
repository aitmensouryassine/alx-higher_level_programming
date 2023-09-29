#!/usr/bin/python3
"""Python script that:
    * takes in a URL
    * sends a request to the URL
    *  displays the body of the response
    by using requests package
"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get(argv[1])
    if resp.status_code == requests.codes.ok:
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
