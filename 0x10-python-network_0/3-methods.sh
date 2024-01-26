#!/bin/bash
# Send an OPTIONS request using curl and display the allowed methods
curl -sI "$1" -X OPTIONS | grep -i "Allow" | cut -d " " -f2-
