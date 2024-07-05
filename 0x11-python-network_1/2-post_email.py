#!/usr/bin/python3
"""
This script takes an email address as an argument, sends a POST request to
a specified URL with the email, and displays the response.
"""

import urllib.request
import urllib.parse
import sys


def email_valid(email):
    """
    This function sends a POST request to the given URL with the provided email
    and returns the response.
    """
    url = "(link unavailable)"  # Specify the actual URL here
    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-post_email.py <email>")
        sys.exit(1)

    email = sys.argv[1]
    response = email_valid(email)
    print(response)
