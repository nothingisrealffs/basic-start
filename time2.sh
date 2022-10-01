#!/bin/bash
dateFromServer=$(curl -v --silent https://nist.time.gov/ 2>&1 \ | grep '< Date' | sed -e 's/< Date: //')
dateFromServer=$(date +"%Y-%m-%d %H:%M:%S" -d "$dateFromServer")
echo $dateFromServer
IFS=' '     # space is set as delimiter
read -ra ADDR <<< "$dateFromServer"   # str is read into an array as tokens separated by IFS
for i in "${ADDR[@]}"; do   # access each element of array
    echo "$i"
done