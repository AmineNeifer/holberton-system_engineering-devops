#!/bin/bash
#sends a GET request to the URL and A header variable X-HolbertonSchool-User-Id: 98
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
