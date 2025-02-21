#!/bin/bash

# 1. Check if the correct number of arguments is provided
if [ $# -lt 2 ] || [ -z "$2" ]; then
    echo "Usage: ./file_manager.sh <directory_path> <file_extension>"
    exit 1
fi

DIRECTORY=$1
EXTENSION=$2

# 2. Check if the directory exists
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: Directory $DIRECTORY does not exist."
    exit 1
fi

# 3. Define the summary.txt path
SUMMARY_FILE="$DIRECTORY/summary.txt"

# 4. Find files with the specified extension (handling different system variations)
FILES=$(find "$DIRECTORY" -maxdepth 1 -type f -name "*.$EXTENSION" | sed "s|$DIRECTORY/||")

# 5. If no matching files are found, display a message
if [ -z "$FILES" ]; then
    echo "No files with the extension $EXTENSION found in $DIRECTORY."
    exit 0
fi

# 6. Ensure the directory is writable
if [ ! -w "$DIRECTORY" ]; then
    echo "Error: Cannot write to $SUMMARY_FILE."
    exit 1
fi

# 7. Create summary.txt if it does not exist
touch "$SUMMARY_FILE" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Error: Cannot create $SUMMARY_FILE."
    exit 1
fi

# 8. Append file names to summary.txt (ensure new lines are formatted correctly)
find "$DIRECTORY" -maxdepth 1 -type f -name "*.$EXTENSION" -exec basename {} \; >> "$SUMMARY_FILE"

# 9. Ensure writing was successful
if [ $? -ne 0 ]; then
    echo "Error: Cannot write to $SUMMARY_FILE."
    exit 1
fi

# 10. Display success message
echo "File names with extension $EXTENSION have been added to $SUMMARY_FILE."
