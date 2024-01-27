#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user id.
"""

import requests
import sys

if __name__ == "__main__":
    # Get username and personal access token from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Define the GitHub API endpoint for user information
    url = 'https://api.github.com/user'

    # Set up Basic Authentication with personal access token
    auth = (username, password)

    # Makes the request to the GitHub API
    response = requests.get(url, auth=auth)

    # Checks if the request was successful (status code 200)
    if response.status_code == 200:
        # Parses the response as JSON
        user_info = response.json()
        # Displays the user id
        print(user_info.get('id'))
    else:
        # Displays None if the request was not successful
        print(None)
