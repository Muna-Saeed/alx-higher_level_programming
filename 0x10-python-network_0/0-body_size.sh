#!/bin/bash
# Takes in a URL, SendS a request using curl and displays the size of the body in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
