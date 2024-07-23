#!/usr/bin/python3
# Fetches the status from https://alx-intranet.hbtn.io/status and displays the content and type

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
