#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -o /dev/null -s -w "%{http_code}\n" "$1" # -s throws away the progress meter -w  prints the required status code -o save to file 
