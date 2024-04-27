#!/usr/bin/python3
"""Script to send an email via POST request and display the response body"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.post(argv[1], data={"email": argv[2]})
    print("Response Body: {}".format(response.text))
