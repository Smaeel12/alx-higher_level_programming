#!/usr/bin/python3
"""Script to send a letter via POST request and display the response"""

if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id", ""), data.get("name", "")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
