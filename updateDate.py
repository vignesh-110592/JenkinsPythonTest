from docx import Document
from datetime import datetime
import os
import shutil

def replace_date_in_docx(input_path, output_path, placeholder_date, new_date):
    doc = Document(input_path)
    for paragraph in doc.paragraphs:
        if placeholder_date in paragraph.text:
            paragraph.text = paragraph.text.replace(placeholder_date, new_date)
    doc.save(output_path)

def update_dates_in_documents(dest_dir, filenames, placeholder_date):
    src_dir = os.getcwd()  # Jenkins runs from the source workspace
    today = datetime.now().strftime("%d.%m.%Y")

    for filename in filenames:
        input_path = os.path.join(src_dir, filename)
        output_path = os.path.join(dest_dir, filename)

        if not os.path.exists(input_path):
            print(f"⚠️ File not found: {input_path}")
            continue

        # Copy to destination and update in-place
        shutil.copy2(input_path, output_path)
        replace_date_in_docx(output_path, output_path, placeholder_date, today)
        print(f"✅ Updated date in {output_path}")

# --- CONFIGURATION ---
destination_workspace = "/dest"  # Mapped to Jenkins 'test' workspace
placeholder_date = "__DATE__"  # Placeholder for the date in the documents
files_to_update = ["AnschreibenRaw.docx", "LebenslaufRaw.docx"]

update_dates_in_documents(destination_workspace, files_to_update, placeholder_date)
