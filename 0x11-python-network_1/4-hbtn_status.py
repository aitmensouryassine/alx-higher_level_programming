#!/usr/bin/python3
"""Module that fetches https://alx-intranet.hbtn.io/status
by using the package requests
"""
import requests


if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
