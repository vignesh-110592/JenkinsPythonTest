# convert_to_pdf_windows.py

from docx2pdf import convert
import os

source_files = ["Anschreiben.docx", "Lebenslauf.docx"]
output_dir = "pdf_output"

os.makedirs(output_dir, exist_ok=True)

for file in source_files:
    if os.path.exists(file):
        print(f"Converting {file} to PDF...")
        convert(file, output_dir)
    else:
        print(f"File not found: {file}")
