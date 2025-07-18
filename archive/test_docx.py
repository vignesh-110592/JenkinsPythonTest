from docx2pdf import convert
import os

if os.path.exists("Anschreiben.docx"):
    try:
        convert("Anschreiben.docx", "pdf_output")
        print("✅ Conversion successful")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
else:
    print("❌ Anschreiben.docx not found in workspace")
