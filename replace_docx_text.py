from docx import Document
from datetime import datetime
import os
import shutil

# Constants
PLACEHOLDER_DATE = "{{Date}}"
PLACEHOLDER_COMPANY = "{{Company_name}}"
PLACEHOLDER_PERSON = "{{Person_name}}"
PLACEHOLDER_POSITION = "{{Position_name}}"

today = datetime.now().strftime("%d.%m.%Y")

def replace_placeholders(file_path, replacements, output_path):
    doc = Document(file_path)
    for para in doc.paragraphs:
        for key, val in replacements.items():
            if key in para.text:
                for run in para.runs:
                    if key in run.text:
                        run.text = run.text.replace(key, val)
    doc.save(output_path)

def main():
    workspace = os.getenv("WORKSPACE", "/app")
    input_resume = os.path.join(workspace, "LebenslaufRaw.docx")
    input_cover = os.path.join(workspace, "AnschreibenRaw.docx")
    output_resume = os.path.join(workspace, "Lebenslauf.docx")
    output_cover = os.path.join(workspace, "Anschreiben_Vignesh.docx")

    # Replacements
    replace_placeholders(input_resume, {
        PLACEHOLDER_DATE: today
    }, output_resume)

    replace_placeholders(input_cover, {
        PLACEHOLDER_DATE: today,
        PLACEHOLDER_COMPANY: "Alten GmbH",
        PLACEHOLDER_PERSON: "John Doe",
        PLACEHOLDER_POSITION: "Software Engineer"
    }, output_cover)

    print("✅ DOCX placeholders updated.")

if __name__ == "__main__":
    main()
