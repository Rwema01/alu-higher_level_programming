#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status using urllib package.
It displays the response body with proper formatting and decoding.
"""

import urllib.request

def fetch_status():
    """Fetch the status of the URL and print formatted body response"""
    url = 'https://alu-intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()
