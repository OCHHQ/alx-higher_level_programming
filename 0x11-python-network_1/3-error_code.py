#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints: Error code: followed by
the HTTP status code.
"""

import urllib.request
import urllib.error
import sys


def error_code(url):
    """
    Function to send a request to the URL and handle errors.
    """
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")  # Added whitespace after :


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    error_code(url)
