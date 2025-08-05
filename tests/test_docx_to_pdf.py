import subprocess
import sys
import shutil
from pathlib import Path
from docx import Document
import pytest
import os


def find_soffice():
    # First try standard PATH lookup
    soffice = shutil.which("soffice")
    if soffice:
        return soffice

    # Fallback: try OS-specific paths
    if sys.platform == "darwin":
        path = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
        return path if Path(path).exists() else None
    elif sys.platform == "win32":
        possible_paths = [
            os.environ.get("ProgramFiles", "") + "\\LibreOffice\\program\\soffice.exe",
            os.environ.get("ProgramFiles(x86)", "") + "\\LibreOffice\\program\\soffice.exe",
        ]
        for path in possible_paths:
            if Path(path).exists():
                return path
    elif sys.platform.startswith("linux"):
        path = "/usr/bin/soffice"
        return path if Path(path).exists() else None

    return None


def convert_with_libreoffice(input_path: Path, output_dir: Path):
    soffice_path = find_soffice()
    if not soffice_path:
        raise FileNotFoundError("LibreOffice (soffice) is not available.")

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

    return output_dir / (input_path.stem + ".pdf")


@pytest.mark.skipif(find_soffice() is None, reason="LibreOffice (soffice) not found")
def test_docx_to_pdf_libreoffice(tmp_path):
    docx_path = tmp_path / "sample.docx"
    doc = Document()
    doc.add_paragraph("This is a test document.")
    doc.save(docx_path)

    output_pdf = convert_with_libreoffice(docx_path, tmp_path)
    assert output_pdf.exists(), f"PDF was not created: expected at {output_pdf}"
