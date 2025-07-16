from docx import Document
from datetime import datetime
import os
import sys

def update_date_placeholder(source_workspace, destination_workspace, filename="Anschreiben.docx", placeholder="__DATE__"):
    # Format today's date
    today = datetime.today().strftime("%d.%m.%Y")

    # Build file paths
    input_path = os.path.join(source_workspace, filename)
    output_path = os.path.join(destination_workspace, filename)

    # Load the document
    doc = Document(input_path)

    # Replace in paragraphs
    for para in doc.paragraphs:
        for run in para.runs:
            if placeholder in run.text:
                run.text = run.text.replace(placeholder, today)


    # Ensure destination directory exists
    os.makedirs(destination_workspace, exist_ok=True)

    # Save the modified document
    doc.save(output_path)
    print(f"Updated file saved to: {output_path}")

# Example usage with hardcoded paths (you can change them via Jenkins env vars or params)
if __name__ == "__main__":
    source_workspace = os.environ.get("SOURCE_WORKSPACE", "C:/ProgramData/Jenkins/.jenkins/workspace/UpdateDateOnResumeAndCoverLetter")
    destination_workspace = os.environ.get("DEST_WORKSPACE", "C:/ProgramData/Jenkins/.jenkins/workspace/test")
    
    update_date_placeholder(source_workspace, destination_workspace)
