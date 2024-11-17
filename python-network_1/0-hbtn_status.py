#!/usr/bin/python3
"""Fetches the status of a URL and displays the response body.

This script fetches the status of a given URL and prints the body of the response
in the specified format. It works with the URL 'https://intranet.hbtn.io/status'.
"""
import urllib.request

url = 'https://intranet.hbtn.io/status'

# Updated User-Agent header without unnecessary new lines
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}

# Request the URL with the custom headers
req = urllib.request.Request(url, headers=headers)

# Open the URL and read the response
with urllib.request.urlopen(req) as response:
    content = response.read()

    # Print the response details
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))

