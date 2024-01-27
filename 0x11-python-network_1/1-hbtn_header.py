#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header
of the response.
"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        # Get the value of the X-Request-Id header
        x_request_id = response.getheader('X-Request-Id')

        print(x_request_id)
