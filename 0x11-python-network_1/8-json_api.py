#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
           Display Not a valid JSON if the JSON is invalid
           Display No result if the JSON is empty
Packages: only requests and sys
Tested on container running on port 5000, json random generated """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    
    value = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    _req = requests.post(url, value)
    try:
        json_data = _req.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        except:
            print("Not a valid JSON")
