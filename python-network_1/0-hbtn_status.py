#!/usr/bin/python3
"""
This script fetches the status of two different URLs
and displays the response content in various formats.

It fetches:
    - https://alu-intranet.hbtn.io/status
    - http://0.0.0.0:5050/status (for local server)

The script shows the type, content, and UTF-8 decoded content of the response.
"""

import urllib.request

def fetch_status(url):
    """Fetches and prints the status of a given URL"""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

# Fetch status for the first URL
url_1 = "https://alu-intranet.hbtn.io/status"
fetch_status(url_1)

# Fetch status for the second URL
url_2 = "http://0.0.0.0:5050/status"
fetch_status(url_2)

