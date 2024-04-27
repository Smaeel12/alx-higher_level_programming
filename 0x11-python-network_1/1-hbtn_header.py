#!/usr/bin/python3
"""Script to fetch and display the X-Request-Id header value from a URL"""

if __name__ == "__main__":
    import sys
    import urllib.request as ulib

    with ulib.urlopen(sys.argv[1]) as response:
        request_id = response.getheader("X-Request-Id")
        print(request_id)
