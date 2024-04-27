#!/usr/bin/python3
"""Script to handle HTTP errors and display response body"""

if __name__ == "__main__":
    import urllib.request as ulib
    from sys import argv

    try:
        with ulib.urlopen(argv[1]) as response:
            content = response.read().decode("UTF-8")
            print("{}".format(content))
    except ulib.HTTPError as e:
        print("Error Code: {}".format(e.code))
