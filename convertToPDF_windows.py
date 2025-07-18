# convert_to_pdf_windows.py

from docx2pdf import convert
import os

source_files = ["Anschreiben.docx", "Lebenslauf.docx"]
output_dir = "C:\\Users\\svvav\\Desktop\\Doc"

os.makedirs(output_dir, exist_ok=True)

for file in source_files:
    if os.path.exists(file):
        print(f"Attempting to convert {file}...")
        try:
            convert(file, output_dir)
            print(f"Conversion successful: {file}")
        except Exception as e:
            print(f"Error during conversion: {e}")
    else:
        print(f"File not found: {file}")



