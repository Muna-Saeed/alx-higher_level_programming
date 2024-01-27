#!/usr/bin/python3
"""
Script that lists the 10 most recent commits
of a given GitHub repository and owner.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: {} <repository name> <owner name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract repository name and owner name from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for commits
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repo_name
            )

    # Make a GET request to the GitHub API
    response = requests.get(url)

    # Checks if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the list of commits from the JSON response
        commits = response.json()

        # Prints the 10 most recent commits
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = (
                commit.get("commit", {})
                .get("author", {})
                .get("name", "Unknown")
            )
            print("{}: {}".format(sha, author_name))
    else:
        # Print an error message if the request was not successful
        print(
                "Error: Unable to fetch commits. Status code:",
                response.status_code
                )
