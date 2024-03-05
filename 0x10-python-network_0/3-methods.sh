#!/bin/bash
# A script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -X OPTIONS "$1" -i | grep "Allow" | cut -d ' ' -f 2-
