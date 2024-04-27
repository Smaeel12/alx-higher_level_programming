#!/usr/bin/python3
"""Script to handle HTTP errors and display response body"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error Code: {}".format(response.status_code))
    else:
        print("Response Body: {}".format(response.text))
