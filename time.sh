#!/bin/bash
dateFromServer=$(curl -v --silent --insecure https://google.com/ 2>&1 \
   | grep Date | sed -e 's/< date: //')
print