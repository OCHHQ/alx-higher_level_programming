#!/usr/bin/python3

"""
This script fetches the 10 most recent commits from a specified GitHub repo
and prints them in the format <sha>: <author name>
"""

import requests
import sys


def fetch_commits(repo, owner):
    """
    Fetches the 10 most recent commits from the specified repository.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, params={'per_page': 10})

    if response.status_code != 200:
        print(f"Error:Unable to fetch  (status code: {response.status_code})")
        return

    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    fetch_commits(repo_name, owner_name)
