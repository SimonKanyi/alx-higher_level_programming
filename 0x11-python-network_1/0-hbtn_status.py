#!/usr/bin/python3
# Fetches https://alx-intranet.hbtn.io/status and displays the response

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
