FROM python:3.11-slim

WORKDIR /app

# Install required Python packages
RUN pip install python-docx

# Copy script and documents into the container (for local test)
COPY . .

CMD ["python", "test.py"]
