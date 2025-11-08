#!/bin/bash

# Navigate to the script's directory
workdir=$(dirname "$0")
cd "$workdir" || exit 1

# Set up a virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the Flask application with Hypercorn
# api:app refers to the api.py file and the app object inside it
hypercorn api:app --bind 0.0.0.0:8000 --workers 4
