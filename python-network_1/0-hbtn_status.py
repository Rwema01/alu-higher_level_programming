#!/usr/bin/python3
"""
This script fetches the status of a URL (https://alu-intranet.hbtn.io/status)
using the urllib package. It retrieves the response from the URL, decodes the
content, and displays it in a formatted manner, including the type, content, and
utf-8 decoded content.

The script demonstrates the use of urllib to open and read data from a URL and 
properly handle the response within a 'with' statement to ensure proper resource 
management.
"""

import urllib.request

def fetch_status():
    """Fetch the status of the URL and print formatted body response."""
    url = 'https://alu-intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()

