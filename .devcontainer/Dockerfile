FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages for development
RUN pip install --no-cache-dir \
    black \
    pylint \
    autopep8 \
    yapf \
    bandit \
    flake8 \
    mypy \
    pycodestyle \
    pydocstyle

# Set working directory
WORKDIR /workspace

# Copy requirements file
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt