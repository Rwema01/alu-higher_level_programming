cript to display the size of the response body for a given URL

curl -sI "$1" | grep -i Content-Length | cut -d " " -f2

