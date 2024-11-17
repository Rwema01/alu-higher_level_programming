#!/usr/bin/python3
"""
Fetches and displays the status of a URL.

This script fetches the status of a given URL and prints the body of the response in the specified format.
The script is designed to work for both https://intranet.hbtn.io/status and http://0.0.0.0:5050/status.
"""
import urllib.request

url = 'https://intranet.hbtn.io/status'  # Change to 'http://0.0.0.0:5050/status' if needed

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read()

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))
