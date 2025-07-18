from docx2pdf import convert
import os

if os.path.exists("sample.docx"):
    try:
        convert("sample.docx", "pdf_output")
        print("✅ Conversion successful")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
else:
    print("❌ sample.docx not found in workspace")
