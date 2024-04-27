#!/usr/bin/python3
"""Script to fetch and display the X-Request-Id header value from a URL"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    print("X-Request-Id: {}".format(response.headers.get("X-Request-Id")))
