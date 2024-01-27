# 0x11 Python - Network #1

This repository contains Python scripts for tasks related to network operations using the `urllib` and `requests` libraries.

## Task List:

### 0. What's my status? #0
- Script: [0-hbtn_status.py](0x11-python-network_1/0-hbtn_status.py)
- Description: Python script that fetches https://alx-intranet.hbtn.io/status using the `urllib` package. It displays information about the response body.

### 1. Response header value #0
- Script: [1-hbtn_header.py](0x11-python-network_1/1-hbtn_header.py)
- Description: Python script that takes a URL, sends a request, and displays the value of the `X-Request-Id` variable found in the header of the response using `urllib` and `sys`.

### 2. POST an email #0
- Script: [2-post_email.py](0x11-python-network_1/2-post_email.py)
- Description: Python script that takes a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response using `urllib` and `sys`.

### 3. Error code #0
- Script: [3-error_code.py](0x11-python-network_1/3-error_code.py)
- Description: Python script that takes a URL, sends a request, and displays the body of the response. It handles `urllib.error.HTTPError` exceptions and prints the error code if it's greater than or equal to 400.

### 4. What's my status? #1
- Script: [4-hbtn_status.py](0x11-python-network_1/4-hbtn_status.py)
- Description: Python script that fetches https://alx-intranet.hbtn.io/status using the `requests` package. It displays information about the response body.

### 5. Response header value #1
- Script: [5-hbtn_header.py](0x11-python-network_1/5-hbtn_header.py)
- Description: Python script that takes a URL, sends a request, and displays the value of the `X-Request-Id` variable in the response header using `requests` and `sys`.

### 6. POST an email #1
- Script: [6-post_email.py](0x11-python-network_1/6-post_email.py)
- Description: Python script that takes a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response using `requests` and `sys`.

### 7. Error code #1
- Script: [7-error_code.py](0x11-python-network_1/7-error_code.py)
- Description: Python script that takes a URL, sends a request, and displays the body of the response. It prints the error code if it's greater than or equal to 400 using `requests` and `sys`.

### 8. Search API
- Script: [8-json_api.py](0x11-python-network_1/8-json_api.py)
- Description: Python script that takes a letter, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. It displays information based on the JSON response using `requests`.

### 9. My GitHub!
- Script: [10-my_github.py](0x11-python-network_1/10-my_github.py)
- Description: Python script that takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user id using Basic Authentication. It uses `requests` and `sys`.

### 10. Time for an interview! (Advanced)
- Script: [100-github_commits.py](0x11-python-network_1/100-github_commits.py)
- Description: Python script that lists 10 commits (from most recent to oldest) of the repository "rails" by the user "rails" using the GitHub API. It uses `requests` and `sys`.
