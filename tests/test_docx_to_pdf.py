import os
import sys
import tempfile
import shutil
import platform
import pytest
from pathlib import Path
from docx import Document

@pytest.mark.skipif(platform.system() == "Linux", reason="docx2pdf does not support Linux")
def test_docx_to_pdf_cross_platform():
    try:
        from docx2pdf import convert
    except ImportError:
        pytest.fail("docx2pdf is not installed")

    # Create a temporary workspace
    temp_dir = Path(tempfile.mkdtemp())
    docx_file = temp_dir / "sample.docx"
    pdf_file = temp_dir / "sample.pdf"

    # Step 1: Create a sample DOCX file
    doc = Document()
    doc.add_paragraph("Hello world from test_docx_to_pdf")
    doc.save(docx_file)

    # Step 2: Convert DOCX to PDF
    convert(str(docx_file), str(pdf_file))

    # Step 3: Assert the PDF file exists and is non-empty
    assert pdf_file.exists(), "PDF file was not created"
    assert pdf_file.stat().st_size > 0, "PDF file is empty"

    # Clean up
    shutil.rmtree(temp_dir)
