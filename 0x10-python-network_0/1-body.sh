#!/bin/bash
# Send a GET request using curl and display the body of the response for a 200 status code
curl -sL "$1" -w "%{http_code}" -o /dev/null | {
    read -r status
    [ "$status" -eq 200 ] && curl -s "$1"
}
