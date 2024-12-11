FROM python:3.12-slim

# Install necessary system packages
RUN apt-get update && apt-get install -y gcc libffi-dev musl-dev build-essential && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
RUN mkdir -p /code
WORKDIR /code

# Copy requirements file
COPY requirements.txt /tmp/requirements.txt

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt && rm -rf /root/.cache/

# Add the rest of your Dockerfile configuration here
