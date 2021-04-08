#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -s DELETE "$1" # X:définir un en-tête HTTP sur une valeur
