#!/usr/bin/python3
""" module uses urllib to make a request """
import urllib.request

if __name__ == "__main__":
    """ making request to provided URL """
    url = 'https://intranet.hbtn.io/status'
    
    # Set up a user-agent to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Create the Request object with the URL and headers
    request = urllib.request.Request(url, headers=headers)
    
    try:
        # Open the URL with the request
        with urllib.request.urlopen(request) as response:
            html = response.read()
            print('Body response:')
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
