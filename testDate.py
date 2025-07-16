from docx import Document
from datetime import datetime
import re
import sys
import os

def find_date_in_text(text):
    # Regex to find date in dd.mm.yyyy format
    match = re.search(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
    return match.group(0) if match else None

def get_all_text(doc):
    texts = []

    # Collect paragraphs
    for para in doc.paragraphs:
        texts.append(para.text)


    return texts

def verify_date_in_doc(doc_path):
    if not os.path.exists(doc_path):
        print(f"FAIL: File not found: {doc_path}")
        return False

    doc = Document(doc_path)
    texts = get_all_text(doc)

    today = datetime.today().strftime("%d.%m.%Y")

    for text in texts:
        found_date = find_date_in_text(text)
        if found_date:
            print(f"Found date in document: {found_date}")
            if found_date == today:
                print("PASS: Date is updated correctly.")
                return True
            else:
                print(f"FAIL: Date '{found_date}' does not match today's date '{today}'.")
                return False

    print("FAIL: No date in dd.mm.yyyy format found in document.")
    return False

if __name__ == "__main__":
    # Adjust path to your destination file here
    file_path = "/dest/AnschreibenRaw.docx"

    success = verify_date_in_doc(file_path)

    if success:
        sys.exit(0)  # Success exit code for Jenkins
    else:
        sys.exit(1)  # Failure exit code for Jenkins
