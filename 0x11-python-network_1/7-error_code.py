#!/usr/bin/python3


"""
Python script that takes in a URL, sends a request to the URL and displays
"""


import requests
import sys


def fetch_url(url):
    """
    Function GET request to a URL and display the response body or error code.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
