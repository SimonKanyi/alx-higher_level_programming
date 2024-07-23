#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# The request includes variables email with the value test@gmail.com and subject with the value I will always be here for PLD
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
