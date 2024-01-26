#!/bin/bash
# Send a request using curl and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
