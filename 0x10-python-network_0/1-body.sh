#!/bin/bash
# Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

# Use curl to fetch the URL and include -s for silent mode and -L to follow redirects
# Pipe the output to grep to find the body of the response after a 200 status code
curl -sL "$1" | grep -oP '(?<=<body>).*(?=</body>)'
