#!/usr/bin/python3
"""Python script that:
    * takes in a URL
    * sends a request to the URL
    * displays the value of the variable X-Request-Id
    in the response header
    by using requests package
"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers.get("X-Request-Id"))
