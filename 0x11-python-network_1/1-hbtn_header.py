#!/usr/bin/python3
"""
This script takes a URL as an argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
