#!/bin/bash

URL="http://192.168.72.207:5000/health"

echo "Checking applications status..."

if curl --silent --fail "$URL"; then
	echo
	echo "Application is running!"
else
	echo
	echo "Application is not responding"
	exit 1
fi
