#!/bin/sh

# Ensure the script stops on any error
set -e

echo "<<Start>>"
# Print the Python interpreter path
echo "Using Python interpreter: $(which python3)"

# Check if libraries are installed in this Python environment
python3 -c "import base64; print('base64 is installed.')"
python3 -c "import json; print('json is installed.')"
python3 -c "import collections; print('collections is installed.')"

echo "###################################"
read -p "Please enter your python file path: " path

cd $path || { echo "Directory not found"; exit 1; }

# Run python file.
python3 main.py

