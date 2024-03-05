#!/bin/bash
# A script that sends a GET request to a URL and displays the body of the response if the status code is 200
curl -s -L -X GET "$1"
