#!/usr/bin/python3
"""Script to fetch and display the status from a URL"""

if __name__ == "__main__":
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Server Status:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
