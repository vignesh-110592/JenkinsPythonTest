from docx import Document
from datetime import datetime, timedelta

def replace_yesterday_with_today(doc_path):
    today = datetime.today().strftime("%d.%m.%Y")
    print(today)
    yesterday = (datetime.today() - timedelta(days=1)).strftime("%d.%m.%Y")
    print(yesterday)
    doc = Document(doc_path)

    def replace_in_runs(runs):
        for run in runs:
            if yesterday in run.text:
                print("found")
                run.text = run.text.replace(yesterday, today)

    # Replace in normal paragraphs
    for para in doc.paragraphs:
        replace_in_runs(para.runs)


    # Overwrite the same file
    doc.save(doc_path)

# Example usage
replace_yesterday_with_today("AnschreibenRaw.docx")
