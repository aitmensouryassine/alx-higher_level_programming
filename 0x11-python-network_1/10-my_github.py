#!/usr/bin/python3
"""Python script that:
    * takes your GitHub credentials (username and password)
    * uses the GitHub API to display your id
    * must use Basic Authentication with a personal access
    token as password to access to your information
    (only read:user permission is needed)
    * The first argument will be your username
    * The second argument will be your password
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    basic_auth = HTTPBasicAuth(argv[1], argv[2])
    resp = requests.get(url, auth=basic_auth)
    print(resp.json().get("id"))
