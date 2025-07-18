import sys
from docx import Document
import os

def replace_text_in_doc(input_path, replacements, output_path):
    doc = Document(input_path)

    def replace_in_runs(runs, replacements):
        for run in runs:
            for placeholder, new_text in replacements.items():
                if placeholder in run.text:
                    run.text = run.text.replace(placeholder, new_text)

    # Replace in paragraphs
    for para in doc.paragraphs:
        replace_in_runs(para.runs, replacements)

    doc.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python replace_texts.py <CompanyName> <PositionName> <PersonName>")
        sys.exit(1)

    # Input values from command-line
    company_name = sys.argv[1]
    position_name = sys.argv[2]
    person_name = sys.argv[3]
    
    input_doc = "AnschreibenRaw.docx"
    temp_doc = "Anschreiben_Temp.docx"
    final_doc = "Anschreiben_Vignesh.docx"

    # Define your placeholder-replacement mapping
    replacements = {
        "Company_name": company_name,
        "Position_name": position_name,
        "Person_name": person_name,
    }

    replace_text_in_doc(input_doc, replacements, temp_doc)

    
    #os.remove(input_doc)
    os.rename(temp_doc, final_doc)

    print(f"Replaced texts in {final_doc}")
