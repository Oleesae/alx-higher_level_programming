#!/bin/bash
# Send an OPTIONS request to the server and display the allowed methods
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-