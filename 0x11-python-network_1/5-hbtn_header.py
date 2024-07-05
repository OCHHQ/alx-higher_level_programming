#!/usr/bin/python3


"""
Python script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable in the response header.
"""


import requests
import sys


def fetch_x_request_id(url):
    """
    Function to fetch and print the X-Request-Id header value from a URL.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
