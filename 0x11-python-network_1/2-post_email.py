#!/usr/bin/python3
"""Script to send an email via POST request and display the response body"""

if __name__ == "__main__":
    import urllib.request as ulib
    from sys import argv

    data = urllib.parse.urlencode({"email": argv[2]}).encode("UTF-8")
    request = ulib.Request(argv[1], data)
    with ulib.urlopen(request, data) as response:
        content = response.read().decode("UTF-8")
        print("Response Body: {}".format(content))
