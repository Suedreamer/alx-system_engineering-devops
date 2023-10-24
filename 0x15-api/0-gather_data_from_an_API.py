#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


if __name__ == "__main__":
    # Define the URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # print the titles of completed tasks with indentation
    [print("\t {}".format(c)) for c in completed]
