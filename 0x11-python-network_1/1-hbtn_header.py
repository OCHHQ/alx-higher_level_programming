#!/usr/bin/python3

"""
This script takes a URL as an argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found.
"""

import urllib.request
import sys


def main():
    """
    Main function to retrieve X-Request-Id from the header of a URL response.
    """
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            x_request_id = response.headers.get('X-Request-Id')
            print(x_request_id)
    except urllib.error.HTTPError as e:
        print("Error:", e)


if __name__ == "__main__":

    main()
