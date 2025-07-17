# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy scripts into container
COPY *.py /app/

# Install dependencies
RUN pip install --no-cache-dir python-docx docx2pdf

# Default command (can be overridden in `docker run`)
CMD ["python", "replace_docx_text.py"]
