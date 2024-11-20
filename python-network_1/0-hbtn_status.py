#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status using urllib"""

from urllib import request

url = "http://0.0.0.0:5050/status"

with request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))

