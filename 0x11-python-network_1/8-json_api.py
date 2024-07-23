#!/usr/bin/python3
import requests
import sys

def main():
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    
    response = requests.post(url, data={"q": letter})
    
    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
