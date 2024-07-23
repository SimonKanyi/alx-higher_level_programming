#!/usr/bin/python3
import requests
import sys

def fetch_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        # Iterate over the first 10 commits
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print("Error fetching commits")

if __name__ == "__main__":
    # Ensure the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo_name> <owner_name>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    fetch_commits(repo_name, owner_name)
