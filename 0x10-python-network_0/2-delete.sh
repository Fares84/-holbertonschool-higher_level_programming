#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sX DELETE "$1" # X: l'option curl qui définit la méthode HTTP utilisée
