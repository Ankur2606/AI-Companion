#!/bin/bash

# Install Docker (if not already installed)
curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

streamlit run app.py