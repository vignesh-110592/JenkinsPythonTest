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
    if len(sys.argv) != 4:
        print("Usage: python test.py <input_docx> <placeholder> <replacement>")
        sys.exit(1)

    input_docx = sys.argv[1]  # e.g., /app/AnschreibenRaw.docx
    placeholder = sys.argv[2]  # e.g., Company_name
    replacement = sys.argv[3]  # e.g., Google
    output_docx = os.path.join(os.path.dirname(input_docx), "AnschreibenFinal.docx")

    replace_text_in_doc(input_docx, placeholder, replacement, output_docx)
    print("Replacement complete. Output saved to", output_docx)
