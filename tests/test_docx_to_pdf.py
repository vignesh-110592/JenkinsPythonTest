import subprocess
import sys
import shutil
import pytest
from pathlib import Path
from docx import Document


def convert_with_libreoffice(input_path: Path, output_dir: Path):
    # Ensure soffice is available
    soffice_path = shutil.which("soffice")
    if not soffice_path:
        raise FileNotFoundError("LibreOffice (soffice) is not installed or not in PATH.")

    # Run the conversion
    result = subprocess.run(
        [
            soffice_path,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", str(output_dir),
            str(input_path)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        raise RuntimeError(f"LibreOffice conversion failed:\n{result.stderr.decode()}")

    # Return path to output PDF
    return output_dir / (input_path.stem + ".pdf")


@pytest.mark.skipif(shutil.which("soffice") is None, reason="LibreOffice is not installed")
def test_docx_to_pdf_libreoffice(tmp_path):
    # Create DOCX file
    docx_path = tmp_path / "sample.docx"
    pdf_path = tmp_path / "sample.pdf"

    doc = Document()
    doc.add_paragraph("This is a test document.")
    doc.save(docx_path)

    # Convert to PDF
    output_pdf = convert_with_libreoffice(docx_path, tmp_path)

    # Assert file was created
    assert output_pdf.exists(), f"PDF was not created: expected at {output_pdf}"
