#!/bin/bash
# Send a POST request using curl with the contents of the JSON file and display the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
