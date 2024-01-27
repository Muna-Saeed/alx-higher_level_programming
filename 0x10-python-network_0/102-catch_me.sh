#!/bin/bash
# Make a request to the specified URL and follow the redirection
curl -sL -i -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
