#!/bin/bash
# Send an OPTIONS request using curl and display the allowed methods
curl -sI -X OPTIONS "$1" | grep -i "Allow" | awk '{print $2}'
