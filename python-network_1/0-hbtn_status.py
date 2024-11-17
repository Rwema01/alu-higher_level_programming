#!/usr/bin/python3
"""
This script fetches data from two URLs:
    1. https://alu-intranet.hbtn.io/status
    2. http://0.0.0.0:5050/status

It prints the type, content, and UTF-8 decoded content of the response from each URL.

For the first URL, the script fetches the status of the intranet server.
For the second URL, it fetches a custom status message from a locally running server.
"""

import urllib.request

try:
    # Fetching from https://alu-intranet.hbtn.io/status
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
except Exception as e:
    print(f"Error fetching https://alu-intranet.hbtn.io/status: {e}")

try:
    # Fetching from http://0.0.0.0:5050/status
    with urllib.request.urlopen('http://0.0.0.0:5050/status') as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
except Exception as e:
    print(f"Error fetching http://0.0.0.0:5050/status: {e}")

