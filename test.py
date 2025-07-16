import sys
import os
from docx import Document

def replace_text_in_doc(file_path, placeholder, new_text, output_path):
    doc = Document(file_path)
    for paragraph in doc.paragraphs:
        if placeholder in paragraph.text:
            paragraph.text = paragraph.text.replace(placeholder, new_text)
    doc.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Usage: python test.py <new_company_name>")
        sys.exit(1)
    print(len(sys.argv))
    input_docx = "/app/AnschreibenRaw.docx"
    placeholder = "Company_name"  # e.g., Company_name    
    replacement = sys.argv[1]  # e.g., Alten
    output_docx = "/app/AnschreibenF.docx"
    print(output_docx)

    replace_text_in_doc(input_docx, "Company_name", replacement, output_docx)
    print("Replacement complete. Output saved to", output_docx)
