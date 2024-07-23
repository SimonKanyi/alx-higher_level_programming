#!/usr/bin/python3
# Sends a POST request with an email parameter and displays the response body decoded in UTF-8

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request and read the response
    with request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
    
    print(body)
