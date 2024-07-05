#!/bin/bash
# Send a GET request with X-School-User-Id header set to 98 and display the body of the response
curl -sH "X-School-User-Id: 98" "$1"
