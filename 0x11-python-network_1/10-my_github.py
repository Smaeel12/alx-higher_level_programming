#!/usr/bin/python3
"""Script to fetch user id from GitHub API"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password)).json()
    user_id = response.get("id")
    print(user_id if "id" in response else "None")
