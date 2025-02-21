#!/bin/bash

# 1. Check if the correct number of arguments is provided
if [ $# -eq 0 ]; then
    echo "Error: missing argument"
    exit 1
fi

FILE=$1

# 2. Check if the file exists and is readable
if [ ! -f "$FILE" ] || [ ! -r "$FILE" ]; then
    echo "Error: cannot read file $FILE"
    exit 1
fi

# 3. Process the text file to count word frequency
echo "Word Frequency"
tr '[:upper:]' '[:lower:]' < "$FILE" | tr -cs 'a-z' '\n' | sort | uniq -c | awk '{print $2, $1}'