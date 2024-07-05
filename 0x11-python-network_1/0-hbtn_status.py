#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib
and displays the body of the response in a specified format.
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()

    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {data.decode('utf-8')}")
