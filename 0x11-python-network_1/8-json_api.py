#!/usr/bin/python3
"""Python script that:
    * takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter
    as a parameter
    * If the response body is properly JSON formatted and
    not empty, display the id and name like this: [<id>] <name>
    * Display Not a valid JSON if the JSON is invalid
    * Display No result if the JSON is empty
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    lettre = "" if len(argv) == 1 else argv[1]
    data = {"q": lettre}
    r = requests.post(url, data=data)
    try:
        resp = r.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
