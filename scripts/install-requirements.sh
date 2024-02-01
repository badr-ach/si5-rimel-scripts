#!/bin/bash

# Check if a requirements.txt file exists
if [ -f requirements.txt ]; then
    # Install Python packages using pip
    pip install -r requirements.txt
    echo "Packages installed successfully."
else
    echo "Error: requirements.txt file not found."
fi
