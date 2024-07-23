#!/usr/bin/python3
# Fetches a URL and displays the value of the X-Request-Id header

import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
    
    print(x_request_id)
