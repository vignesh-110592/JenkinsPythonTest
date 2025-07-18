# Dockerfile
FROM python:3.11-slim

# Install LibreOffice
RUN apt-get update && apt-get install -y \
    libreoffice \
    ttf-mscorefonts-installer \
    fonts-crosextra-carlito \
    fonts-crosextra-caladea \
    fontconfig \
    && fc-cache -fv

# Install required Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app

# Copy your scripts into container
COPY . /app
