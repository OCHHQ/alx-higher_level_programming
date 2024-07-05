#!/usr/bin/python3


"""
This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's ID.
"""


import requests
import sys


def get_github_id(username, token):
    """
    GitHub user ID using the provided username and personal access token.
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('id')
    else:
        return None


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    user_id = get_github_id(username, token)
    print(user_id)
