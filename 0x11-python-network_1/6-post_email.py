#!/usr/bin/python3


"""
Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the
response.
"""


import requests
import sys


def post_email(url, email):
    """
    send a POST request with email as a parameter and display response body.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> ")
        print("<email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
