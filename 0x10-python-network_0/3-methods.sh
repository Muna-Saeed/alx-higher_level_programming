#!/bin/bash
# Send an OPTIONS request using curl and display the allowed methods
curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print $2}'
