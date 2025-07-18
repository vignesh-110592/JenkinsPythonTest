# convert_with_libreoffice.py

import subprocess
import os

def convert_to_pdf(input_docx_path, output_dir):
    if not os.path.exists(input_docx_path):
        print(f"❌ File not found: {input_docx_path}")
        return

    # LibreOffice CLI conversion
    cmd = [
        "libreoffice",
        "--headless",
        "--convert-to", "pdf",
        "--outdir", output_dir,
        input_docx_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ Converted: {input_docx_path}")
    else:
        print(f"❌ Error: {result.stderr}")

# Example usage
if __name__ == "__main__":
    files_to_convert = [
        "/app/Lebenslauf.docx",
        "/app/Anschreiben.docx"
    ]
    output_dir = "/app/pdf_output"

    os.makedirs(output_dir, exist_ok=True)

    for docx_file in files_to_convert:
        convert_to_pdf(docx_file, output_dir)
