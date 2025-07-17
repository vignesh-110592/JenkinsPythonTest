from docx2pdf import convert
import os

source = "C:/ProgramData/Jenkins/.jenkins/workspace/test"
dest = "C:/ProgramData/Jenkins/.jenkins/workspace/pdf_output"

if not os.path.exists(dest):
    os.makedirs(dest)

convert(source, dest)
print("✅ Converted to PDF.")
