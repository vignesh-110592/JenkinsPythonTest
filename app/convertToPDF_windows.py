# convert_to_pdf_windows.py

from docx2pdf import convert
from datetime import datetime
import os
import sys
from os.path import dirname

source_files = ["Anschreiben.docx", "Lebenslauf.docx"]
output_dir = "C:\\Users\\svvav\\Desktop\\Doc"

os.makedirs(output_dir, exist_ok=True)
current_date = datetime.today().strftime("%d.%m.%Y")
modified_timestamp = os.path.getmtime(os.path.join(output_dir, "Lebenslauf.pdf"))
modified_date = datetime.fromtimestamp(modified_timestamp).strftime("%d.%m.%Y")
#print(modified_date)
repodir= dirname(dirname(__file__))
for file in source_files:   
    #os.path.join(repodir, "output").exists()
    file_path = os.path.join(repodir, "output", file)
    if os.path.exists(file_path):

        if file == "Lebenslauf.docx":
            if modified_date == current_date :
                print(f"File Lebenslauf.pdf was modified today. Skipping conversion.")
                continue
            else:
                print(f"File Lebenslauf.pdf was last modified on {modified_date}. Attempting to convert {file}...")
                try:
                    convert(file_path, output_dir)
                    print(f"Conversion successful: {file}")
                except Exception as e:
                    print(f"Error during conversion: {e}")
                    sys.exit(1)
        else:
            print(f"Attempting to convert {file}...")
            try:
                convert(file_path, output_dir)
                print(f"Conversion successful: {file}")
            except Exception as e:
                print(f"Error during conversion: {e}")
                sys.exit(1)
    else:
        print(f"File not found: {file}")
        sys.exit(1)



