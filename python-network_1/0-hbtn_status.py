#!/usr/bin/python3
"""
Fetch status of alx.intranet site
 This script fetches https://alu-intranet.hbtn.io/status using urllib package.
 It displays the response body with proper formatting and decoding.
 The script can be easily updated to fetch data from another URL such as http://0.0.0.0:5050/status (for testing purposes).

"""
import urllib.request

def fetch_status():
 """
 Fetch the status of the alx intranet site and print formatted body response.
 """
 url = 'https://alu-intranet.hbtn.io/status'
 # Testing purpose
 # url = 'http://0.0.0.0:5050/status'

 with urllib.request.urlopen(url) as response:
 data = response.read()

 print("Body response:")
 print("\t- type: ", type(data))
 print("\t- content: ", data)
 print("\t- utf8 content: ", data.decode('utf-8'))

if __name__ == "__main__":
 fetch_status()
