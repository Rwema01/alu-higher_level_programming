#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status and http://0.0.0.0:5050/status
using urllib, and prints the body response with the required formatting.
"""

import urllib.request

# Fetching from https://alu-intranet.hbtn.io/status
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()

    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(body.decode('utf-8')))

# Fetching from http://0.0.0.0:5050/status
with urllib.request.urlopen('http://0.0.0.0:5050/status') as response:
    body = response.read()

    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(body.decode('utf-8')))

