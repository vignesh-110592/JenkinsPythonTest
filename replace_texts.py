import sys
from docx import Document
import os

def replace_text_in_doc(input_path, replacements, output_path):
    doc = Document(input_path)

    for para in doc.paragraphs:
        for placeholder, new_text in replacements.items():
            if placeholder in para.text:
                para.text = para.text.replace(placeholder, new_text)

    doc.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python replace_texts.py <CompanyName> <PositionName> <PersonName>")
        sys.exit(1)

    # Input values from command-line
    company_name = sys.argv[1]
    position_name = sys.argv[2]
    person_name = sys.argv[3]
    
    input_doc = "Anschreiben.docx"
    temp_doc = "Anschreiben_Temp.docx"
    final_doc = "Anschreiben_Vignesh.docx"

    # Define your placeholder-replacement mapping
    replacements = {
        "Company_name": "Company_name",
        "Position_name": "Position_name",
        "Person_name": "Person_name",
    }

    replace_text_in_doc(input_doc, replacements, temp_doc)

    
    #os.remove(input_doc)
    os.rename(temp_doc, final_doc)

    print(f"Replaced texts in {final_doc}")
