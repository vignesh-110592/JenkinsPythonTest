FROM python:3.11-slim

WORKDIR /app

COPY updateDate.py .

RUN pip install python-docx
