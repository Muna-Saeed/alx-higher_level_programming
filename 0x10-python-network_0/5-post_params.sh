#!/bin/bash
# Set variables for the POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request using curl with the specified parameters and display the body of the response
curl -sX POST "$1" -d "email=$email&subject=$subject"
