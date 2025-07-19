# convert_to_pdf_windows.py

from docx2pdf import convert
from datetime import datetime
import os

source_files = ["Anschreiben.docx", "Lebenslauf.docx"]
output_dir = "C:\\Users\\svvav\\Desktop\\Doc"

os.makedirs(output_dir, exist_ok=True)
current_date = datetime.today().strftime("%d.%m.%Y")
modified_timestamp = os.path.getmtime("Lebenslauf.docx")
modified_date = datetime.fromtimestamp(modified_timestamp).strftime("%d.%m.%Y")

for file in source_files:
    if os.path.exists(file):

        if modified_date == current_date and file == "Lebenslauf.docx":
            print(f"File '{file}' was modified today. Skipping conversion.")
            continue
        else:
            print(f"File '{file}' was last modified on {modified_date}. Attempting to convert {file}...")
            try:
                convert(file, output_dir)
                print(f"Conversion successful: {file}")
            except Exception as e:
                print(f"Error during conversion: {e}")
    else:
        print(f"File not found: {file}")



