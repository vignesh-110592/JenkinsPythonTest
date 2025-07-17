from docx2pdf import convert
import os

sourceAnschreiben = "C:/ProgramData/Jenkins/.jenkins/workspace/test/Anschreiben.docx"
sourceLebenslauf = "C:/ProgramData/Jenkins/.jenkins/workspace/test/Lebenslauf.docx"
dest = "C:/ProgramData/Jenkins/.jenkins/workspace/test/pdf_output"

if not os.path.exists(dest):
    os.makedirs(dest)

convert(sourceAnschreiben, dest)
convert(sourceLebenslauf, dest)
print("✅ Converted to PDF.")
