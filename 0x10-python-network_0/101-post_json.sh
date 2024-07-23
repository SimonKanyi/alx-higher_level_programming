#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the body and displays the body of the response

# Check if exactly two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Assign arguments to variables
URL=$1
JSON_FILE=$2

# Send POST request with JSON file contents
curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"
