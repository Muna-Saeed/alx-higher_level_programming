#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using requests.
Displays the body of the response.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    # Display the body of the response
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
