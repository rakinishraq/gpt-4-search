#!/bin/bash

# Navigate to the project directory
cd ~/Projects/gpt-4-search

# Activate the virtual environment
source .venv/bin/activate

# Run the Python script
python gpt_4_search.py

# Deactivate the virtual environment
deactivate

cd -
