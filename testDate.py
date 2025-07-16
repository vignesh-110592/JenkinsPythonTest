from docx import Document
from datetime import datetime
import os
import sys

def verify_date_in_docx(file_path, expected_date):
    try:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            if expected_date in paragraph.text:
                print(f"✅ Date '{expected_date}' found in {os.path.basename(file_path)}")
                return True
        print(f"❌ Date '{expected_date}' NOT found in {os.path.basename(file_path)}")
        return False
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False

def verify_dates_in_documents(dest_dir, filenames, expected_date):
    all_passed = True
    for filename in filenames:
        file_path = os.path.join(dest_dir, filename)
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            all_passed = False
            continue
        if not verify_date_in_docx(file_path, expected_date):
            all_passed = False
    return all_passed

# --- CONFIGURATION ---
destination_workspace = "/dest"  # Docker-mounted path to Jenkins 'test' workspace
files_to_verify = ["AnschreibenRaw.docx", "LebenslaufRaw.docx"]
expected_date = datetime.now().strftime("%d.%m.%Y")

success = verify_dates_in_documents(destination_workspace, files_to_verify, expected_date)

if not success:
    sys.exit(1)  # Make Jenkins pipeline fail if any verification fails
