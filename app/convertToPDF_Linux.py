# convert_to_pdf_linux.py

import subprocess
from datetime import datetime
import os
import sys
from os.path import dirname, join

source_files = ["Anschreiben.docx", "Lebenslauf.docx"]
workspace_dir = dirname(dirname(__file__))  # assumes script is in app/
output_dir = join(workspace_dir, "output")

os.makedirs(output_dir, exist_ok=True)
current_date = datetime.today().strftime("%d.%m.%Y")

# Check if Lebenslauf.pdf exists and skip if already updated today
lebenslauf_pdf = join(output_dir, "Lebenslauf.pdf")
if os.path.exists(lebenslauf_pdf):
    modified_timestamp = os.path.getmtime(lebenslauf_pdf)
    modified_date = datetime.fromtimestamp(modified_timestamp).strftime("%d.%m.%Y")
    if modified_date == current_date:
        print("File Lebenslauf.pdf was modified today. Skipping conversion.")
        source_files.remove("Lebenslauf.docx")  # skip in loop

for file in source_files:
    file_path = join(output_dir, file)
    if not os.path.exists(file_path):
        print(f"File not found: {file}")
        sys.exit(1)

    print(f"Attempting to convert {file}...")
    try:
        subprocess.run([
            "libreoffice", "--headless", "--convert-to", "pdf",
            file_path, "--outdir", output_dir
        ], check=True)
        print(f"Conversion successful: {file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion of {file}: {e}")
        sys.exit(1)
