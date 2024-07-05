#!/usr/bin/python3

"""
Python script that fetches https://alx-intranet.hbtn.io/status
Uses the requests package to make an HTTP GET request and displays the body
response in the specified format.
"""


import requests


def fetch_status():
    """
    Function to fetch the status from the URL and display the body response.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    fetch_status()
