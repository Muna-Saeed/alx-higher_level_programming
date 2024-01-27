#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Set default value for q if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the payload
    payload = {"q": q}

    # Make the POST request
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Parse the response as JSON
        json_response = response.json()

        # Check if JSON is not empty and properly formatted
        if json_response:
            print("[{}] {}".format(
                json_response.get("id"),
                json_response.get("name")
                ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
