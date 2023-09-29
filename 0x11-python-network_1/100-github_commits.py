#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest)
    of a repository of a user
    * Python script that takes 2 args: repository & owner name
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    r = requests.get(url.format(argv[2], argv[1]))
    resp = r.json()
    try:
        for c in range(10):
            print(f"{resp[c].get('sha')}: \
{resp[c].get('commit').get('author').get('name')}")
    except IndexError:
        pass
