#!/bin/bash
# a script that sends a GET request to a URL and displays the response body 
curl -X GET -sH "X-School-USer-Id: 98" "$1" 
