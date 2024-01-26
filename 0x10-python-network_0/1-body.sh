#!/bin/bash
# Send a GET request using curl and display the body of the response for a 200 status code
curl -sX GET $1 -L
