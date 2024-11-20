#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib"""

from urllib import request

url = "https://alu-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))

