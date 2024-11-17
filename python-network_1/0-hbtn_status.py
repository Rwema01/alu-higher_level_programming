#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status or http://0.0.0.0:5050/status."""
import urllib.request
import urllib.error

if __name__ == "__main__":
    # URL to fetch; change this to test the other URL
    url = "https://intranet.hbtn.io/status"
    
    # Create a request with necessary headers
    request = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html',
        'Connection': 'keep-alive'
    })
    
    try:
        # Open the URL and read the response
        with urllib.request.urlopen(request) as response:
            body = response.read()
            # Print the response details
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
    except Exception as e:
        print(f"Error: {str(e)}")
