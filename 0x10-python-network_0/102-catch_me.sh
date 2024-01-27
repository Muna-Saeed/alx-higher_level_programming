#!/bin/bash
# Make a request to the specified URL that causes the server to respond with a message containing You got me!
curl -sw "You got me!" 0.0.0.0:5000/catch_me
