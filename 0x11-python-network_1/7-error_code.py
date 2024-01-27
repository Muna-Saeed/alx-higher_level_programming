#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
prints: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Make the request
    response = requests.get(url)

    # Check for HTTP status code and print error if needed
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
