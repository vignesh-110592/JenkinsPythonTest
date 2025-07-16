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
        print("Usage: python test.py <new_company_name>")
        sys.exit(1)
    input_docx = "/app/AnschreibenRaw.docx"
    search_text = ["Company_name", "Position_name", "Person_name"]  # e.g., Company_name
    #placeholder = "Company_name"  # e.g., Company_name
    replacement = sys.argv[1]  # e.g., Alten
    
    position_name = sys.argv[2]
    person_name = sys.argv[3]
    output_docx = "/app/Anschreiben_Vignesh.docx"
    for arg in range(len(sys.argv)-1):
        replace_text_in_doc(input_docx, search_text[arg], sys.argv[arg+1], output_docx)

    #replace_text_in_doc(input_docx, "Company_name", replacement, output_docx)
    print("Replacement complete. Output saved to", output_docx)
