#!/usr/bin/python3
"""Python script that:
    * takes in a URL and an email address
    * sends a POST request to the passed URL
    with the email as a parameter
    * displays the body of the response
"""
from sys import argv
import requests


if __name__ == "__main__":
    data = {"email": argv[2]}
    resp = requests.post(argv[1], data=data)
    print(resp.text)
