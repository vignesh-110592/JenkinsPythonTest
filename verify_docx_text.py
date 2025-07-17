from docx import Document
import os

def verify_placeholders(file_path, expected_values):
    doc = Document(file_path)
    text = "\n".join([p.text for p in doc.paragraphs])
    for key, val in expected_values.items():
        if val not in text:
            print(f"❌ Verification failed: {val} not found in {file_path}")
            return False
    print(f"✅ Verified: {file_path}")
    return True

def main():
    workspace = os.getenv("WORKSPACE", "/app")
    resume = os.path.join(workspace, "Lebenslauf.docx")
    cover = os.path.join(workspace, "Anschreiben_Vignesh.docx")

    from datetime import datetime
    today = datetime.now().strftime("%d.%m.%Y")

    all_ok = True
    all_ok &= verify_placeholders(resume, {
        "Date": today
    })
    all_ok &= verify_placeholders(cover, {
        "Date": today,
        "Company_name": "Alten GmbH",
        "Person_name": "John Doe",
        "Position_name": "Software Engineer"
    })

    if not all_ok:
        raise Exception("❌ Verification failed.")

if __name__ == "__main__":
    main()
