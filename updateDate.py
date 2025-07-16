from docx import Document
from datetime import datetime
import os
import sys

def update_date_placeholder(source_dir, destination_dir, filename="AnschreibenRaw.docx", placeholder="__DATE__"):
    today = datetime.today().strftime("%d.%m.%Y")

    input_path = os.path.join(source_dir, filename)
    output_path = os.path.join(destination_dir, filename)

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    doc = Document(input_path)

    # Replace in paragraphs
    for para in doc.paragraphs:
        for run in para.runs:
            if placeholder in run.text:
                run.text = run.text.replace(placeholder, today)

    # Replace in tables
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    for run in para.runs:
                        if placeholder in run.text:
                            run.text = run.text.replace(placeholder, today)

    os.makedirs(destination_dir, exist_ok=True)
    doc.save(output_path)
    print(f"Updated file saved to: {output_path}")

if __name__ == "__main__":
    source_dir = "/source"
    destination_dir = "/dest"
    update_date_placeholder(source_dir, destination_dir)
