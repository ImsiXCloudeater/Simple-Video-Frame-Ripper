#!/bin/bash

# Navigate to the directory containing the Python scripts
cd program

# Run the dependency installer script and wait for it to finish
python3 install_py.py

# Check if the install_py.py script succeeded
if [ $? -eq 0 ]; then
    # Run the main application script
    python3 vfr.pyw
else
    echo "Dependency installation failed. Please check the install_py.py script."
fi
