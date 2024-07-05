#!/usr/bin/python3


"""
This script takes in a letter and sends a POST request to a specified URL
with the letter as a parameter.
"""


import requests
import sys


def search_user(letter):
    """
    Sends a POST request to the search_user API with the provided letter.
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()
        if response_json:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":

    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
