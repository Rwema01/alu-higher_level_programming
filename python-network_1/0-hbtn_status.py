#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status using urllib package.
It displays the response body with proper formatting and decoding.
The script can be easily updated to fetch data from another URL such as http://0.0.0.0:5050/status (for testing purposes).
"""

import urllib.request

def fetch_status_main():
 """
 Fetch the status of the URL and print formatted body response.
 The URL used is https://alu-intranet.hbtn.io/status, but it can be updated for testing.
 """
 url = 'https://alu-intranet.hbtn.io/status' # Default URL for production
 # Testing purpose
 # url = 'http://0.0.0.0:5050/status'

 with urllib.request.urlopen(url) as response:
 body = response.read()

 print("Body response:")
 print(f"\t- type: {type(body)}")
 print(f"\t- content: {body}")
 print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
 fetch_status_main()
