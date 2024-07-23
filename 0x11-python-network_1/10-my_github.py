#!/usr/bin/python3
import requests
import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        return

    username = sys.argv[1]
    token = sys.argv[2]
    
    # GitHub API URL for user information
    url = "https://api.github.com/user"
    
    # Send GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))
    
    # Check if request was successful
    if response.status_code == 200:
        # Print user ID from the JSON response
        user_info = response.json()
        print(user_info.get('id'))
    else:
        # Print None for any unsuccessful request
        print(None)

if __name__ == "__main__":
    main()
