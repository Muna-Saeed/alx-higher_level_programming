#!/usr/bin/python3
"""
script that sends a POST request to a specified URL
with an email as a parameter and then displays
the body of the response.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Assign URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Make the POST request
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print(body)       
