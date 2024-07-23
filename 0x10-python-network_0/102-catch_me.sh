#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to get a response containing "You got me!"

curl -s -X PUT -H "Content-Type: application/json" -d '{"user_id": 98}' "0.0.0.0:5000/catch_me"
