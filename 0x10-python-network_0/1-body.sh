#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" # L:location s:désactiver l'affichage de la progression
